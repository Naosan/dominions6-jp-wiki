from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.dom6_sources import (
    ManifestError,
    SourceIntegrityError,
    SourceManifest,
    SourceRegistry,
    git_blob_sha,
)


def manifest_text(payload: bytes, *, blob: str | None = None) -> str:
    digest = blob or git_blob_sha(payload)
    return f'''schema = 1

[source]
name = "example"
repository = "owner/repository"
commit = "{'a' * 40}"
tree = "{'b' * 40}"
game_version = "1.2"
cache = ".cache/example/{{commit}}"
base_url = "https://example.invalid/{{repository}}/{{commit}}"

[compatibility]
commit_modules = []

[[files]]
path = "gamedata/example.csv"
cache = "example.csv"
blob = "{digest}"
groups = ["test"]
'''


class _Response:
    def __init__(self, payload: bytes):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self) -> bytes:
        return self.payload


class ManifestTests(unittest.TestCase):
    def test_resolves_registered_file_by_path_cache_and_basename(self) -> None:
        payload = b"id\tname\n1\tExample\n"
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / "sources" / "example.toml"
            path.parent.mkdir()
            manifest = SourceManifest.from_text(
                manifest_text(payload), path=path, root=root
            )
            registry = SourceRegistry(manifest)
            expected = manifest.files[0]
            self.assertEqual(registry.resolve("gamedata/example.csv"), expected)
            self.assertEqual(registry.resolve("example.csv"), expected)

    def test_rejects_duplicate_cache_names(self) -> None:
        payload = b"one"
        text = manifest_text(payload) + f'''
[[files]]
path = "gamedata/other.csv"
cache = "example.csv"
blob = "{git_blob_sha(b'two')}"
'''
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / "sources" / "example.toml"
            path.parent.mkdir()
            with self.assertRaises(ManifestError):
                SourceManifest.from_text(text, path=path, root=root)


class RegistryTests(unittest.TestCase):
    def test_offline_accepts_only_a_matching_cache_blob(self) -> None:
        payload = b"id\tname\n1\tExample\n"
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / "sources" / "example.toml"
            path.parent.mkdir()
            manifest = SourceManifest.from_text(
                manifest_text(payload), path=path, root=root
            )
            registry = SourceRegistry(manifest)
            cache = registry.cache_path("example.csv")
            cache.parent.mkdir(parents=True)
            cache.write_bytes(payload)

            self.assertEqual(registry.ensure("example.csv", offline=True), cache)
            self.assertTrue(registry.inspect_path("example.csv")["valid"])

            cache.write_bytes(b"corrupted")
            with self.assertRaises(SourceIntegrityError):
                registry.ensure("example.csv", offline=True)

    def test_refresh_downloads_verifies_and_replaces_atomically(self) -> None:
        payload = b"id\tname\n1\tExample\n"
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / "sources" / "example.toml"
            path.parent.mkdir()
            manifest = SourceManifest.from_text(
                manifest_text(payload), path=path, root=root
            )
            registry = SourceRegistry(manifest)
            with patch(
                "scripts.dom6_sources.urllib.request.urlopen",
                return_value=_Response(payload),
            ):
                cache = registry.ensure("example.csv", refresh=True)

            self.assertEqual(cache.read_bytes(), payload)
            self.assertTrue(registry.inspect_path("example.csv")["valid"])
            self.assertEqual(list(cache.parent.glob("*.tmp")), [])

    def test_rejects_download_that_does_not_match_the_lock(self) -> None:
        payload = b"expected"
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / "sources" / "example.toml"
            path.parent.mkdir()
            manifest = SourceManifest.from_text(
                manifest_text(payload), path=path, root=root
            )
            registry = SourceRegistry(manifest)
            with patch(
                "scripts.dom6_sources.urllib.request.urlopen",
                return_value=_Response(b"unexpected"),
            ), patch("scripts.dom6_sources.time.sleep"):
                with self.assertRaises(RuntimeError):
                    registry.ensure("example.csv", refresh=True)


if __name__ == "__main__":
    unittest.main()
