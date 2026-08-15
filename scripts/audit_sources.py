#!/usr/bin/env python3
"""Verify the pinned Dom6 Inspector snapshot and report source-level diffs."""
from __future__ import annotations

import argparse
import ast
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Iterable

try:
    from .dom6_sources import (
        DEFAULT_MANIFEST_PATH,
        ROOT,
        ManifestError,
        SourceManifest,
        SourceRegistry,
    )
except ImportError:  # Direct execution: ``python scripts/audit_sources.py``
    from dom6_sources import (  # type: ignore
        DEFAULT_MANIFEST_PATH,
        ROOT,
        ManifestError,
        SourceManifest,
        SourceRegistry,
    )

REPORT_SCHEMA = 1


def compatibility_issues(manifest: SourceManifest) -> list[dict[str, str]]:
    """Keep legacy direct-generator constants aligned during the migration."""

    issues: list[dict[str, str]] = []
    for relative in manifest.compatibility_modules:
        path = manifest.root / relative
        if not path.is_file():
            issues.append(
                {
                    "code": "compatibility-module-missing",
                    "path": relative,
                    "message": "compatibility module does not exist",
                }
            )
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError) as exc:
            issues.append(
                {
                    "code": "compatibility-module-unreadable",
                    "path": relative,
                    "message": str(exc),
                }
            )
            continue

        assignments: list[str] = []
        for node in tree.body:
            if isinstance(node, ast.Assign):
                names = [target.id for target in node.targets if isinstance(target, ast.Name)]
                if "COMMIT" in names and isinstance(node.value, ast.Constant):
                    if isinstance(node.value.value, str):
                        assignments.append(node.value.value)
            elif isinstance(node, ast.AnnAssign):
                if (
                    isinstance(node.target, ast.Name)
                    and node.target.id == "COMMIT"
                    and isinstance(node.value, ast.Constant)
                    and isinstance(node.value.value, str)
                ):
                    assignments.append(node.value.value)

        if not assignments:
            issues.append(
                {
                    "code": "compatibility-commit-missing",
                    "path": relative,
                    "message": "top-level string COMMIT assignment was not found",
                }
            )
            continue
        for value in assignments:
            if value != manifest.commit:
                issues.append(
                    {
                        "code": "compatibility-commit-drift",
                        "path": relative,
                        "message": (
                            f"COMMIT={value} differs from manifest commit {manifest.commit}"
                        ),
                    }
                )
    return issues


def audit_registry(
    registry: SourceRegistry,
    *,
    refresh: bool = False,
    offline: bool = False,
) -> dict[str, object]:
    records: list[dict[str, object]] = []
    errors: list[dict[str, str]] = []
    for file in registry.manifest.files:
        try:
            path = registry.ensure(file, refresh=refresh, offline=offline)
            state = registry.inspect_path(file)
            state["status"] = "verified"
            state["cache_path"] = str(path.relative_to(registry.manifest.root))
            records.append(state)
        except Exception as exc:  # Preserve every file failure in one report.
            state = registry.inspect_path(file)
            state["status"] = "error"
            state["error"] = str(exc)
            cache_path = Path(str(state["cache_path"]))
            try:
                state["cache_path"] = str(cache_path.relative_to(registry.manifest.root))
            except ValueError:
                pass
            records.append(state)
            errors.append(
                {
                    "code": "source-integrity",
                    "path": file.path,
                    "message": str(exc),
                }
            )
    return {
        "files": records,
        "errors": errors,
        "verified_files": sum(record["status"] == "verified" for record in records),
        "total_files": len(records),
        "total_bytes": sum(int(record.get("bytes") or 0) for record in records),
    }


def manifest_diff(
    current: SourceManifest,
    baseline: SourceManifest | None,
    *,
    baseline_ref: str | None = None,
    note: str | None = None,
) -> dict[str, object]:
    if baseline is None:
        return {
            "baseline_ref": baseline_ref,
            "available": False,
            "note": note or "baseline manifest is unavailable",
            "source_changes": {},
            "added": [],
            "removed": [],
            "changed": [],
        }

    source_changes: dict[str, dict[str, str]] = {}
    for key in ("repository", "commit", "tree", "game_version"):
        before = str(getattr(baseline, key))
        after = str(getattr(current, key))
        if before != after:
            source_changes[key] = {"before": before, "after": after}

    before_files = {file.path: file for file in baseline.files}
    after_files = {file.path: file for file in current.files}
    added = sorted(set(after_files) - set(before_files))
    removed = sorted(set(before_files) - set(after_files))
    changed: list[dict[str, object]] = []
    for path in sorted(set(before_files) & set(after_files)):
        before = before_files[path]
        after = after_files[path]
        fields: dict[str, dict[str, object]] = {}
        for field in ("cache", "blob", "groups"):
            old = getattr(before, field)
            new = getattr(after, field)
            if old != new:
                fields[field] = {
                    "before": list(old) if isinstance(old, tuple) else old,
                    "after": list(new) if isinstance(new, tuple) else new,
                }
        if fields:
            changed.append({"path": path, "fields": fields})

    return {
        "baseline_ref": baseline_ref,
        "available": True,
        "note": note,
        "source_changes": source_changes,
        "added": added,
        "removed": removed,
        "changed": changed,
    }


def default_baseline_ref() -> str | None:
    base = os.environ.get("GITHUB_BASE_REF", "").strip()
    if base:
        return f"origin/{base}"
    if os.environ.get("GITHUB_EVENT_NAME") == "push":
        return "HEAD^"
    return None


def load_baseline_manifest(
    current: SourceManifest,
    baseline_ref: str | None,
) -> tuple[SourceManifest | None, str | None]:
    if not baseline_ref:
        return None, "no baseline ref was selected"
    try:
        relative = current.path.relative_to(current.root).as_posix()
    except ValueError:
        return None, f"manifest is outside repository root: {current.path}"
    completed = subprocess.run(
        ["git", "show", f"{baseline_ref}:{relative}"],
        cwd=current.root,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        message = completed.stderr.strip() or completed.stdout.strip()
        return None, message or f"manifest not found at {baseline_ref}"
    try:
        return (
            SourceManifest.from_text(
                completed.stdout,
                path=current.path,
                root=current.root,
            ),
            None,
        )
    except (ManifestError, ValueError) as exc:
        return None, f"baseline manifest could not be parsed: {exc}"


def build_report(
    manifest: SourceManifest,
    audit: dict[str, object],
    compatibility: list[dict[str, str]],
    diff: dict[str, object],
) -> dict[str, object]:
    errors = list(audit["errors"])
    errors.extend(compatibility)
    return {
        "schema": REPORT_SCHEMA,
        "manifest": str(manifest.path.relative_to(manifest.root)),
        "source": {
            "name": manifest.name,
            "repository": manifest.repository,
            "commit": manifest.commit,
            "tree": manifest.tree,
            "game_version": manifest.game_version,
        },
        "summary": {
            "verified_files": audit["verified_files"],
            "total_files": audit["total_files"],
            "total_bytes": audit["total_bytes"],
            "errors": len(errors),
        },
        "files": audit["files"],
        "compatibility_issues": compatibility,
        "diff": diff,
        "errors": errors,
    }


def github_escape(value: object) -> str:
    return (
        str(value)
        .replace("%", "%25")
        .replace("\r", "%0D")
        .replace("\n", "%0A")
        .replace(":", "%3A")
        .replace(",", "%2C")
    )


def annotations(errors: Iterable[dict[str, str]]) -> list[str]:
    output: list[str] = []
    for error in errors:
        title = github_escape(f"Dom6 source audit: {error['code']}")
        message = github_escape(error["message"])
        path = error.get("path", "sources/dom6inspector.toml")
        if not path.startswith(("sources/", "scripts/", ".github/")):
            path = "sources/dom6inspector.toml"
        output.append(f"::error file={github_escape(path)},title={title}::{message}")
    return output


def human_bytes(value: int) -> str:
    size = float(value)
    for unit in ("B", "KiB", "MiB", "GiB"):
        if size < 1024 or unit == "GiB":
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024
    return f"{value} B"


def summary_markdown(report: dict[str, object]) -> str:
    source = report["source"]
    summary = report["summary"]
    diff = report["diff"]
    lines = [
        "## Dom6 source snapshot",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Game version | `{source['game_version']}` |",
        f"| Repository | `{source['repository']}` |",
        f"| Commit | `{source['commit']}` |",
        f"| Tree | `{source['tree']}` |",
        f"| Verified inputs | {summary['verified_files']} / {summary['total_files']} |",
        f"| Cached bytes | {human_bytes(int(summary['total_bytes']))} |",
        f"| Integrity errors | {summary['errors']} |",
        "",
        "### Snapshot difference",
        "",
    ]
    baseline_ref = diff.get("baseline_ref") or "none"
    lines.append(f"Baseline: `{baseline_ref}`")
    lines.append("")
    if not diff.get("available"):
        lines.append(f"- Baseline manifest unavailable: {diff.get('note') or 'unknown reason'}")
    else:
        source_changes = diff.get("source_changes") or {}
        added = diff.get("added") or []
        removed = diff.get("removed") or []
        changed = diff.get("changed") or []
        if not (source_changes or added or removed or changed):
            lines.append("- Pinned source snapshot is unchanged.")
        for key, values in source_changes.items():
            lines.append(
                f"- `{key}`: `{values['before']}` → `{values['after']}`"
            )
        if added:
            lines.append("- Added inputs: " + ", ".join(f"`{path}`" for path in added))
        if removed:
            lines.append("- Removed inputs: " + ", ".join(f"`{path}`" for path in removed))
        for entry in changed:
            fields = ", ".join(f"`{field}`" for field in entry["fields"])
            lines.append(f"- Changed `{entry['path']}`: {fields}")

    lines.extend(
        [
            "",
            "<details>",
            "<summary>Verified file checksums</summary>",
            "",
            "| Upstream path | Git blob | SHA-256 | Bytes |",
            "|---|---|---|---:|",
        ]
    )
    for record in report["files"]:
        actual_blob = record.get("actual_blob") or "—"
        digest = record.get("sha256") or "—"
        lines.append(
            f"| `{record['path']}` | `{actual_blob}` | `{digest}` | {record.get('bytes') or 0} |"
        )
    lines.extend(["", "</details>", ""])
    return "\n".join(lines)


def append_summary(report: dict[str, object]) -> None:
    destination = os.environ.get("GITHUB_STEP_SUMMARY")
    if not destination:
        return
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(summary_markdown(report))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="固定Dom6 Inspector snapshotのCacheとChecksumを検証します。"
    )
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    parser.add_argument("--report", type=Path, default=ROOT / "build" / "source-audit.json")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--refresh", action="store_true", help="all locked inputsを再取得")
    modes.add_argument("--offline", action="store_true", help="Networkを使わずCacheだけを検証")
    parser.add_argument("--baseline-ref", help="manifest差分を比較するGit ref")
    parser.add_argument("--github-summary", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest = SourceManifest.from_path(args.manifest, root=ROOT)
        registry = SourceRegistry(manifest)
    except (OSError, ManifestError) as exc:
        print(f"source manifest error: {exc}", file=sys.stderr)
        return 2

    audit = audit_registry(registry, refresh=args.refresh, offline=args.offline)
    compatibility = compatibility_issues(manifest)
    baseline_ref = args.baseline_ref or default_baseline_ref()
    baseline, baseline_note = load_baseline_manifest(manifest, baseline_ref)
    diff = manifest_diff(
        manifest,
        baseline,
        baseline_ref=baseline_ref,
        note=baseline_note,
    )
    report = build_report(manifest, audit, compatibility, diff)

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if args.github_summary:
        append_summary(report)

    for command in annotations(report["errors"]):
        print(command)
    summary = report["summary"]
    print("Dom6 source audit")
    print(f"  Manifest: {report['manifest']}")
    print(f"  Game version: {report['source']['game_version']}")
    print(f"  Commit: {report['source']['commit']}")
    print(f"  Verified files: {summary['verified_files']}/{summary['total_files']}")
    print(f"  Cached bytes: {summary['total_bytes']}")
    print(f"  Errors: {summary['errors']}")
    print(f"  Report: {args.report}")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
