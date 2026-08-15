#!/usr/bin/env python3
"""Pinned external-source registry for all generated Dominions 6 data.

The TOML manifest is the lock file.  This module owns cache paths, downloads,
and content-integrity validation so generators can consume a verified snapshot
instead of independently trusting a URL or a non-empty cache file.
"""
from __future__ import annotations

import hashlib
import os
import re
import tempfile
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST_PATH = ROOT / "sources" / "dom6inspector.toml"
_HEX40_RE = re.compile(r"^[0-9a-f]{40}$")


class ManifestError(ValueError):
    """The source lock file is malformed or ambiguous."""


class SourceIntegrityError(RuntimeError):
    """Downloaded or cached bytes do not match the locked Git blob."""


@dataclass(frozen=True)
class SourceFile:
    """One immutable file in the pinned upstream repository snapshot."""

    path: str
    cache: str
    blob: str
    groups: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, object]:
        return {
            "path": self.path,
            "cache": self.cache,
            "blob": self.blob,
            "groups": list(self.groups),
        }


@dataclass(frozen=True)
class SourceManifest:
    """Parsed source lock file."""

    schema: int
    name: str
    repository: str
    commit: str
    tree: str
    game_version: str
    cache_template: str
    base_url_template: str
    user_agent: str
    files: tuple[SourceFile, ...]
    compatibility_modules: tuple[str, ...]
    root: Path
    path: Path

    @classmethod
    def from_path(
        cls,
        path: Path = DEFAULT_MANIFEST_PATH,
        *,
        root: Path | None = None,
    ) -> "SourceManifest":
        path = Path(path)
        with path.open("rb") as handle:
            data = tomllib.load(handle)
        return cls.from_data(data, path=path, root=root)

    @classmethod
    def from_text(
        cls,
        text: str,
        *,
        path: Path = DEFAULT_MANIFEST_PATH,
        root: Path | None = None,
    ) -> "SourceManifest":
        return cls.from_data(tomllib.loads(text), path=path, root=root)

    @classmethod
    def from_data(
        cls,
        data: dict[str, Any],
        *,
        path: Path,
        root: Path | None = None,
    ) -> "SourceManifest":
        try:
            schema = int(data["schema"])
            source = data["source"]
            name = str(source["name"])
            repository = str(source["repository"])
            commit = str(source["commit"])
            tree = str(source["tree"])
            game_version = str(source["game_version"])
            cache_template = str(source["cache"])
            base_url_template = str(source["base_url"])
            user_agent = str(source.get("user_agent", "dominions6-jp-wiki/1.0"))
            raw_files = data["files"]
        except (KeyError, TypeError, ValueError) as exc:
            raise ManifestError(f"missing or invalid source manifest field: {exc}") from exc

        if schema != 1:
            raise ManifestError(f"unsupported source manifest schema: {schema}")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
            raise ManifestError(f"invalid repository name: {repository!r}")
        for label, value in (("commit", commit), ("tree", tree)):
            if not _HEX40_RE.fullmatch(value):
                raise ManifestError(f"{label} must be a lowercase 40-character SHA: {value!r}")

        files: list[SourceFile] = []
        seen_paths: set[str] = set()
        seen_cache: set[str] = set()
        for index, raw in enumerate(raw_files):
            try:
                repository_path = str(raw["path"])
                cache_name = str(raw["cache"])
                blob = str(raw["blob"])
                groups = tuple(str(value) for value in raw.get("groups", []))
            except (KeyError, TypeError) as exc:
                raise ManifestError(f"invalid files[{index}] entry: {exc}") from exc
            _validate_relative(repository_path, f"files[{index}].path")
            _validate_relative(cache_name, f"files[{index}].cache")
            if "/" in cache_name or "\\" in cache_name:
                raise ManifestError(
                    f"files[{index}].cache must be a flat cache name: {cache_name!r}"
                )
            if not _HEX40_RE.fullmatch(blob):
                raise ManifestError(f"files[{index}].blob is not a Git SHA: {blob!r}")
            if repository_path in seen_paths:
                raise ManifestError(f"duplicate repository path: {repository_path}")
            if cache_name in seen_cache:
                raise ManifestError(f"duplicate cache name: {cache_name}")
            seen_paths.add(repository_path)
            seen_cache.add(cache_name)
            files.append(SourceFile(repository_path, cache_name, blob, groups))

        if not files:
            raise ManifestError("source manifest must register at least one file")

        compatibility = data.get("compatibility", {})
        modules = tuple(str(value) for value in compatibility.get("commit_modules", []))
        for index, module in enumerate(modules):
            _validate_relative(module, f"compatibility.commit_modules[{index}]")

        resolved_root = Path(root).resolve() if root else Path(path).resolve().parents[1]
        return cls(
            schema=schema,
            name=name,
            repository=repository,
            commit=commit,
            tree=tree,
            game_version=game_version,
            cache_template=cache_template,
            base_url_template=base_url_template,
            user_agent=user_agent,
            files=tuple(files),
            compatibility_modules=modules,
            root=resolved_root,
            path=Path(path).resolve(),
        )

    @property
    def cache_dir(self) -> Path:
        value = self.cache_template.format(
            commit=self.commit,
            repository=self.repository,
            name=self.name,
        )
        _validate_relative(value, "source.cache")
        path = (self.root / value).resolve()
        try:
            path.relative_to(self.root)
        except ValueError as exc:
            raise ManifestError(f"cache path escapes repository root: {path}") from exc
        return path

    @property
    def base_url(self) -> str:
        return self.base_url_template.format(
            commit=self.commit,
            repository=self.repository,
            name=self.name,
        ).rstrip("/")

    def source_url(self, file: SourceFile) -> str:
        quoted = urllib.parse.quote(file.path, safe="/")
        return f"{self.base_url}/{quoted}"

    def as_dict(self) -> dict[str, object]:
        return {
            "schema": self.schema,
            "name": self.name,
            "repository": self.repository,
            "commit": self.commit,
            "tree": self.tree,
            "game_version": self.game_version,
            "cache": self.cache_template,
            "base_url": self.base_url_template,
            "files": [file.as_dict() for file in self.files],
            "compatibility_modules": list(self.compatibility_modules),
        }


def _validate_relative(value: str, label: str) -> None:
    if not value or value.startswith(("/", "\\")):
        raise ManifestError(f"{label} must be a non-empty relative path: {value!r}")
    normalized = value.replace("\\", "/")
    if any(part in {"", ".", ".."} for part in normalized.split("/")):
        raise ManifestError(f"{label} contains an unsafe path component: {value!r}")


def git_blob_sha(data: bytes) -> str:
    """Return the SHA-1 Git assigns to these exact blob bytes."""

    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def inspect_bytes(file: SourceFile, data: bytes) -> dict[str, object]:
    actual_blob = git_blob_sha(data)
    return {
        "path": file.path,
        "cache": file.cache,
        "expected_blob": file.blob,
        "actual_blob": actual_blob,
        "sha256": sha256(data),
        "bytes": len(data),
        "groups": list(file.groups),
        "valid": actual_blob == file.blob,
    }


class SourceRegistry:
    """Resolve, download, and verify files registered by a SourceManifest."""

    def __init__(self, manifest: SourceManifest):
        self.manifest = manifest
        self._aliases = self._build_aliases(manifest.files)

    @staticmethod
    def _build_aliases(files: Iterable[SourceFile]) -> dict[str, SourceFile]:
        aliases: dict[str, SourceFile] = {}
        basename_counts: dict[str, int] = {}
        file_list = list(files)
        for file in file_list:
            basename = Path(file.path).name
            basename_counts[basename] = basename_counts.get(basename, 0) + 1
        for file in file_list:
            aliases[file.path] = file
            aliases[file.cache] = file
            basename = Path(file.path).name
            if basename_counts[basename] == 1:
                aliases[basename] = file
        return aliases

    def resolve(self, name: str | SourceFile) -> SourceFile:
        if isinstance(name, SourceFile):
            return name
        normalized = str(name).replace("\\", "/").lstrip("./")
        try:
            return self._aliases[normalized]
        except KeyError as exc:
            raise KeyError(f"source is not registered in {self.manifest.path}: {name}") from exc

    def cache_path(self, name: str | SourceFile) -> Path:
        file = self.resolve(name)
        return self.manifest.cache_dir / file.cache

    def inspect_path(self, name: str | SourceFile) -> dict[str, object]:
        file = self.resolve(name)
        path = self.cache_path(file)
        if not path.is_file():
            return {
                "path": file.path,
                "cache": file.cache,
                "expected_blob": file.blob,
                "actual_blob": None,
                "sha256": None,
                "bytes": 0,
                "groups": list(file.groups),
                "valid": False,
                "cache_path": str(path),
                "error": "cache file is missing",
            }
        result = inspect_bytes(file, path.read_bytes())
        result["cache_path"] = str(path)
        if not result["valid"]:
            result["error"] = (
                f"Git blob mismatch: expected {file.blob}, got {result['actual_blob']}"
            )
        return result

    def ensure(
        self,
        name: str | SourceFile,
        *,
        refresh: bool = False,
        offline: bool = False,
    ) -> Path:
        file = self.resolve(name)
        path = self.cache_path(file)
        path.parent.mkdir(parents=True, exist_ok=True)

        if path.is_file() and not refresh:
            state = self.inspect_path(file)
            if state["valid"]:
                return path
            if offline:
                raise SourceIntegrityError(
                    f"offline cache failed integrity validation: {path}: {state['error']}"
                )
        elif offline:
            raise FileNotFoundError(f"offline cache missing: {path}")

        payload = self._download(file)
        state = inspect_bytes(file, payload)
        if not state["valid"]:  # Defensive: _download already checks every attempt.
            raise SourceIntegrityError(
                f"downloaded source does not match lock: {file.path}: "
                f"expected {file.blob}, got {state['actual_blob']}"
            )
        self._atomic_write(path, payload)
        return path

    def ensure_all(
        self,
        *,
        refresh: bool = False,
        offline: bool = False,
    ) -> list[Path]:
        return [
            self.ensure(file, refresh=refresh, offline=offline)
            for file in self.manifest.files
        ]

    def _download(self, file: SourceFile) -> bytes:
        url = self.manifest.source_url(file)
        request = urllib.request.Request(
            url,
            headers={"User-Agent": self.manifest.user_agent},
        )
        error: Exception | None = None
        for attempt in range(3):
            try:
                with urllib.request.urlopen(request, timeout=60) as response:
                    payload = response.read()
                if not payload:
                    raise RuntimeError("empty download")
                actual_blob = git_blob_sha(payload)
                if actual_blob != file.blob:
                    raise SourceIntegrityError(
                        f"Git blob mismatch for {file.path}: "
                        f"expected {file.blob}, got {actual_blob}"
                    )
                return payload
            except (
                urllib.error.URLError,
                TimeoutError,
                RuntimeError,
                SourceIntegrityError,
            ) as exc:
                error = exc
                if attempt < 2:
                    time.sleep(2**attempt)
        raise RuntimeError(f"download failed after 3 attempts: {file.path}: {error}")

    @staticmethod
    def _atomic_write(path: Path, payload: bytes) -> None:
        descriptor, temporary = tempfile.mkstemp(
            prefix=f".{path.name}.",
            suffix=".tmp",
            dir=path.parent,
        )
        try:
            with os.fdopen(descriptor, "wb") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, path)
        except Exception:
            try:
                os.unlink(temporary)
            except FileNotFoundError:
                pass
            raise


_DEFAULT_MANIFEST: SourceManifest | None = None
_DEFAULT_REGISTRY: SourceRegistry | None = None


def default_manifest() -> SourceManifest:
    global _DEFAULT_MANIFEST
    if _DEFAULT_MANIFEST is None:
        _DEFAULT_MANIFEST = SourceManifest.from_path(DEFAULT_MANIFEST_PATH, root=ROOT)
    return _DEFAULT_MANIFEST


def default_registry() -> SourceRegistry:
    global _DEFAULT_REGISTRY
    if _DEFAULT_REGISTRY is None:
        _DEFAULT_REGISTRY = SourceRegistry(default_manifest())
    return _DEFAULT_REGISTRY


def source(name: str, refresh: bool = False, offline: bool = False) -> Path:
    """Compatibility API matching the existing generator source() signature."""

    return default_registry().ensure(name, refresh=refresh, offline=offline)


def repository_source(
    repository_path: str,
    refresh: bool = False,
    offline: bool = False,
) -> Path:
    return source(repository_path, refresh=refresh, offline=offline)


# Convenient metadata for generators as they migrate away from local constants.
_MANIFEST = default_manifest()
COMMIT = _MANIFEST.commit
TREE = _MANIFEST.tree
GAME_VERSION = _MANIFEST.game_version
REPOSITORY = _MANIFEST.repository
CACHE = _MANIFEST.cache_dir
