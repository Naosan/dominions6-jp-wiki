from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.audit_sources import compatibility_issues, manifest_diff, summary_markdown
from scripts.dom6_sources import SourceManifest, git_blob_sha


def manifest_text(
    *,
    root_commit: str,
    file_blob: str,
    compatibility: tuple[str, ...] = (),
) -> str:
    modules = ", ".join(f'"{path}"' for path in compatibility)
    return f'''schema = 1

[source]
name = "example"
repository = "owner/repository"
commit = "{root_commit}"
tree = "{'b' * 40}"
game_version = "1.2"
cache = ".cache/example/{{commit}}"
base_url = "https://example.invalid/{{repository}}/{{commit}}"

[compatibility]
commit_modules = [{modules}]

[[files]]
path = "gamedata/example.csv"
cache = "example.csv"
blob = "{file_blob}"
groups = ["test"]
'''


class CompatibilityTests(unittest.TestCase):
    def test_detects_legacy_commit_drift(self) -> None:
        current = "a" * 40
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "sources").mkdir()
            (root / "scripts").mkdir()
            module = root / "scripts" / "legacy.py"
            module.write_text(f'COMMIT = "{"c" * 40}"\n', encoding="utf-8")
            manifest = SourceManifest.from_text(
                manifest_text(
                    root_commit=current,
                    file_blob=git_blob_sha(b"example"),
                    compatibility=("scripts/legacy.py",),
                ),
                path=root / "sources" / "example.toml",
                root=root,
            )
            issues = compatibility_issues(manifest)
            self.assertEqual(issues[0]["code"], "compatibility-commit-drift")
            self.assertIn(current, issues[0]["message"])


class DiffTests(unittest.TestCase):
    def test_reports_source_and_file_checksum_changes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "sources").mkdir()
            path = root / "sources" / "example.toml"
            before = SourceManifest.from_text(
                manifest_text(root_commit="a" * 40, file_blob="c" * 40),
                path=path,
                root=root,
            )
            after = SourceManifest.from_text(
                manifest_text(root_commit="d" * 40, file_blob="e" * 40),
                path=path,
                root=root,
            )
            diff = manifest_diff(after, before, baseline_ref="origin/main")
            self.assertEqual(
                diff["source_changes"]["commit"],
                {"before": "a" * 40, "after": "d" * 40},
            )
            self.assertEqual(diff["changed"][0]["path"], "gamedata/example.csv")
            self.assertIn("blob", diff["changed"][0]["fields"])

    def test_summary_contains_locked_and_runtime_checksums(self) -> None:
        report = {
            "source": {
                "game_version": "1.2",
                "repository": "owner/repository",
                "commit": "a" * 40,
                "tree": "b" * 40,
            },
            "summary": {
                "verified_files": 1,
                "total_files": 1,
                "total_bytes": 42,
                "errors": 0,
            },
            "diff": {
                "baseline_ref": "origin/main",
                "available": True,
                "source_changes": {},
                "added": [],
                "removed": [],
                "changed": [],
            },
            "files": [
                {
                    "path": "gamedata/example.csv",
                    "actual_blob": "c" * 40,
                    "sha256": "d" * 64,
                    "bytes": 42,
                }
            ],
        }
        text = summary_markdown(report)
        self.assertIn("Pinned source snapshot is unchanged", text)
        self.assertIn("gamedata/example.csv", text)
        self.assertIn("d" * 64, text)


if __name__ == "__main__":
    unittest.main()
