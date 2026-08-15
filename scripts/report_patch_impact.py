#!/usr/bin/env python3
"""Compare generated Wiki metrics with a base revision and audit article freshness.

The current docs directory is expected to have been generated already.  When a
baseline ref is available, the tool creates a detached temporary worktree,
runs that revision's canonical generator in ``--generate-only`` mode, and then
compares generated-page counts, Markdown table rows, bytes, and fingerprints.
Hand-written, versioned pages are checked against the game version locked in the
Dom6 Inspector source manifest.  The report is informational by default so
existing editorial debt stays visible without blocking unrelated work.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

try:
    from .audit_wiki import front_matter, generated
    from .dom6_sources import DEFAULT_MANIFEST_PATH, ROOT, ManifestError, SourceManifest
except ImportError:  # Direct execution: ``python scripts/report_patch_impact.py``
    from audit_wiki import front_matter, generated  # type: ignore
    from dom6_sources import (  # type: ignore
        DEFAULT_MANIFEST_PATH,
        ROOT,
        ManifestError,
        SourceManifest,
    )

REPORT_SCHEMA = 1
DEFAULT_REPORT_PATH = ROOT / "build" / "patch-impact.json"
VERSION_RE = re.compile(r"^[vV]?\s*(\d+(?:\.\d+)*)([A-Za-z]*)\s*$")
TABLE_LINE_RE = re.compile(r"^\s*\|.*\|\s*$")
TABLE_SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
MAX_SAMPLES = 50


@dataclass(frozen=True)
class ParsedVersion:
    numbers: tuple[int, ...]
    suffix: str

    def padded(self, length: int) -> tuple[int, ...]:
        return self.numbers + (0,) * (length - len(self.numbers))


@dataclass(frozen=True)
class GeneratedFile:
    path: str
    dataset: str
    sha256: str
    bytes: int
    table_rows: int


@dataclass(frozen=True)
class BaselineSnapshot:
    available: bool
    ref: str | None
    note: str | None
    metrics: dict[str, object] | None
    source: dict[str, str] | None


def parse_version(value: str) -> ParsedVersion | None:
    """Parse a dotted Dominions version with an optional alphabetic suffix."""

    match = VERSION_RE.fullmatch(value or "")
    if not match:
        return None
    return ParsedVersion(
        tuple(int(part) for part in match.group(1).split(".")),
        match.group(2).lower(),
    )


def compare_versions(left: str, right: str) -> int | None:
    """Return -1/0/1 for left versus right, or None when either is invalid."""

    parsed_left = parse_version(left)
    parsed_right = parse_version(right)
    if parsed_left is None or parsed_right is None:
        return None
    width = max(len(parsed_left.numbers), len(parsed_right.numbers))
    left_numbers = parsed_left.padded(width)
    right_numbers = parsed_right.padded(width)
    if left_numbers != right_numbers:
        return -1 if left_numbers < right_numbers else 1
    if parsed_left.suffix == parsed_right.suffix:
        return 0
    # Treat an unsuffixed release as the first release in that numeric series;
    # lettered hotfixes then sort after it: 6.35 < 6.35a < 6.35b.
    return -1 if parsed_left.suffix < parsed_right.suffix else 1


def table_row_count(text: str) -> int:
    """Count Markdown table body rows while excluding headers/separators."""

    lines = text.splitlines()
    count = 0
    in_table = False
    for index, line in enumerate(lines):
        if _table_separator(line) and index > 0 and TABLE_LINE_RE.match(lines[index - 1]):
            in_table = True
            continue
        if not in_table:
            continue
        if TABLE_LINE_RE.match(line):
            count += 1
        else:
            in_table = False
    return count


def _table_separator(line: str) -> bool:
    if not TABLE_LINE_RE.match(line):
        return False
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return bool(cells) and all(TABLE_SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells)


def dataset_name(relative: Path, metadata: Mapping[str, str]) -> str:
    """Return a stable, review-sized bucket for a generated Markdown page."""

    parts = relative.parts
    status = metadata.get("status", "").strip()
    if status == "stub" and parts and parts[0] == "nations":
        return "nation-stubs"
    if not parts:
        return "root"
    if parts[0] == "data":
        if len(parts) == 1:
            return "data"
        second = parts[1]
        if len(parts) == 2:
            second = Path(second).stem
        return f"data/{second}"
    return parts[0]


def collect_generated_metrics(docs: Path) -> dict[str, object]:
    """Collect deterministic metrics and fingerprints for generator-owned pages."""

    docs = docs.resolve()
    files: dict[str, GeneratedFile] = {}
    datasets: dict[str, dict[str, int]] = {}
    status_counts: dict[str, int] = {}

    for path in sorted(docs.rglob("*.md")):
        if not path.is_file():
            continue
        relative = path.relative_to(docs)
        payload = path.read_bytes()
        try:
            text = payload.decode("utf-8")
        except UnicodeDecodeError:
            text = payload.decode("utf-8", errors="replace")
        present, metadata, parse_error = front_matter(text)
        if not present or parse_error or not generated(relative, metadata):
            continue
        dataset = dataset_name(relative, metadata)
        rows = table_row_count(text)
        record = GeneratedFile(
            path=relative.as_posix(),
            dataset=dataset,
            sha256=hashlib.sha256(payload).hexdigest(),
            bytes=len(payload),
            table_rows=rows,
        )
        files[record.path] = record
        bucket = datasets.setdefault(dataset, {"pages": 0, "bytes": 0, "table_rows": 0})
        bucket["pages"] += 1
        bucket["bytes"] += record.bytes
        bucket["table_rows"] += rows
        status = metadata.get("status", "").strip() or "unspecified"
        status_counts[status] = status_counts.get(status, 0) + 1

    return {
        "totals": {
            "pages": len(files),
            "bytes": sum(record.bytes for record in files.values()),
            "table_rows": sum(record.table_rows for record in files.values()),
        },
        "datasets": {key: datasets[key] for key in sorted(datasets)},
        "status_counts": dict(sorted(status_counts.items())),
        "files": files,
    }


def _page_record(relative: Path, metadata: Mapping[str, str]) -> dict[str, str]:
    return {
        "path": relative.as_posix(),
        "title": metadata.get("title", "").strip(),
        "page_type": metadata.get("page_type", "").strip(),
        "status": metadata.get("status", "").strip(),
        "verified_version": metadata.get("verified_version", "").strip(),
        "last_verified": metadata.get("last_verified", "").strip(),
    }


def verification_inventory(docs: Path, target_version: str) -> dict[str, object]:
    """Classify hand-written, game-versioned pages against the source lock."""

    docs = docs.resolve()
    categories: dict[str, list[dict[str, str]]] = {
        "current": [],
        "stale": [],
        "ahead": [],
        "missing": [],
        "invalid": [],
        "metadata_missing": [],
        "needs_update": [],
    }
    excluded = 0
    hand_written = 0

    for path in sorted(docs.rglob("*.md")):
        if not path.is_file():
            continue
        relative = path.relative_to(docs)
        text = path.read_text(encoding="utf-8", errors="replace")
        present, metadata, parse_error = front_matter(text)
        if not present or parse_error:
            categories["metadata_missing"].append(
                {
                    "path": relative.as_posix(),
                    "message": parse_error or "front matter is missing",
                }
            )
            continue
        if generated(relative, metadata):
            continue
        if metadata.get("page_type", "").strip() in {"project", "template"}:
            excluded += 1
            continue

        hand_written += 1
        record = _page_record(relative, metadata)
        if record["status"] == "needs-update":
            categories["needs_update"].append(record)

        version = record["verified_version"]
        if not version:
            categories["missing"].append(record)
            continue
        comparison = compare_versions(version, target_version)
        if comparison is None:
            record["message"] = f"cannot compare with locked game version {target_version}"
            categories["invalid"].append(record)
        elif comparison < 0:
            categories["stale"].append(record)
        elif comparison > 0:
            categories["ahead"].append(record)
        else:
            categories["current"].append(record)

    for records in categories.values():
        records.sort(key=lambda item: item["path"])
    return {
        "target_version": target_version,
        "hand_written_pages": hand_written,
        "excluded_non_game_pages": excluded,
        **categories,
    }


def _plain_metrics(metrics: dict[str, object]) -> dict[str, object]:
    """Drop internal GeneratedFile objects before JSON serialization."""

    return {
        "totals": metrics["totals"],
        "datasets": metrics["datasets"],
        "status_counts": metrics["status_counts"],
    }


def metric_diff(
    current: dict[str, object],
    baseline: dict[str, object] | None,
) -> dict[str, object]:
    if baseline is None:
        return {
            "available": False,
            "totals": {},
            "datasets": [],
            "files": {
                "added": 0,
                "removed": 0,
                "changed": 0,
                "added_samples": [],
                "removed_samples": [],
                "changed_samples": [],
                "truncated": False,
            },
        }

    before_totals = baseline["totals"]
    after_totals = current["totals"]
    total_diff: dict[str, dict[str, int]] = {}
    for field in ("pages", "table_rows", "bytes"):
        before = int(before_totals[field])
        after = int(after_totals[field])
        total_diff[field] = {"before": before, "after": after, "delta": after - before}

    before_datasets = baseline["datasets"]
    after_datasets = current["datasets"]
    dataset_diff: list[dict[str, object]] = []
    for name in sorted(set(before_datasets) | set(after_datasets)):
        before = before_datasets.get(name, {"pages": 0, "bytes": 0, "table_rows": 0})
        after = after_datasets.get(name, {"pages": 0, "bytes": 0, "table_rows": 0})
        fields = {
            field: {
                "before": int(before[field]),
                "after": int(after[field]),
                "delta": int(after[field]) - int(before[field]),
            }
            for field in ("pages", "table_rows", "bytes")
        }
        if any(values["delta"] for values in fields.values()):
            dataset_diff.append({"dataset": name, **fields})

    current_files: dict[str, GeneratedFile] = current["files"]
    baseline_files: dict[str, GeneratedFile] = baseline["files"]
    added = sorted(set(current_files) - set(baseline_files))
    removed = sorted(set(baseline_files) - set(current_files))
    changed = sorted(
        path
        for path in set(current_files) & set(baseline_files)
        if current_files[path].sha256 != baseline_files[path].sha256
    )
    return {
        "available": True,
        "totals": total_diff,
        "datasets": dataset_diff,
        "files": {
            "added": len(added),
            "removed": len(removed),
            "changed": len(changed),
            "added_samples": added[:MAX_SAMPLES],
            "removed_samples": removed[:MAX_SAMPLES],
            "changed_samples": changed[:MAX_SAMPLES],
            "truncated": any(len(paths) > MAX_SAMPLES for paths in (added, removed, changed)),
        },
    }


def default_baseline_ref() -> str | None:
    base = os.environ.get("GITHUB_BASE_REF", "").strip()
    if base:
        return f"origin/{base}"
    if os.environ.get("GITHUB_EVENT_NAME") == "push":
        return "HEAD^"
    return None


def _git_has_path(root: Path, ref: str, relative: str) -> bool:
    completed = subprocess.run(
        ["git", "cat-file", "-e", f"{ref}:{relative}"],
        cwd=root,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return completed.returncode == 0


def _manifest_summary(manifest: SourceManifest) -> dict[str, str]:
    return {
        "repository": manifest.repository,
        "commit": manifest.commit,
        "tree": manifest.tree,
        "game_version": manifest.game_version,
    }


def build_baseline_snapshot(root: Path, ref: str | None) -> BaselineSnapshot:
    """Generate and collect docs from a detached base-revision worktree."""

    if not ref:
        return BaselineSnapshot(False, None, "no baseline ref was selected", None, None)
    required = ("scripts/build_wiki.py", "sources/dom6inspector.toml")
    missing = [path for path in required if not _git_has_path(root, ref, path)]
    if missing:
        return BaselineSnapshot(
            False,
            ref,
            "baseline predates patch-impact support: " + ", ".join(missing),
            None,
            None,
        )

    with tempfile.TemporaryDirectory(prefix="dom6-wiki-baseline-") as temporary:
        worktree = Path(temporary) / "repo"
        added = subprocess.run(
            ["git", "worktree", "add", "--detach", "--force", str(worktree), ref],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )
        if added.returncode != 0:
            note = added.stderr.strip() or added.stdout.strip() or "git worktree add failed"
            return BaselineSnapshot(False, ref, note, None, None)
        try:
            built = subprocess.run(
                [sys.executable, "scripts/build_wiki.py", "--generate-only"],
                cwd=worktree,
                text=True,
                capture_output=True,
                check=False,
            )
            if built.returncode != 0:
                detail = built.stderr.strip() or built.stdout.strip()
                if len(detail) > 2000:
                    detail = detail[-2000:]
                return BaselineSnapshot(
                    False,
                    ref,
                    f"baseline generation failed with exit code {built.returncode}: {detail}",
                    None,
                    None,
                )
            try:
                manifest = SourceManifest.from_path(
                    worktree / "sources" / "dom6inspector.toml",
                    root=worktree,
                )
                metrics = collect_generated_metrics(worktree / "docs")
            except (OSError, ManifestError, ValueError) as exc:
                return BaselineSnapshot(False, ref, f"baseline collection failed: {exc}", None, None)
            return BaselineSnapshot(
                True,
                ref,
                None,
                metrics,
                _manifest_summary(manifest),
            )
        finally:
            subprocess.run(
                ["git", "worktree", "remove", "--force", str(worktree)],
                cwd=root,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )
            subprocess.run(
                ["git", "worktree", "prune"],
                cwd=root,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )


def snapshot_from_docs(
    docs: Path,
    *,
    ref: str | None = None,
    source: dict[str, str] | None = None,
) -> BaselineSnapshot:
    return BaselineSnapshot(True, ref, None, collect_generated_metrics(docs), source)


def build_report(
    manifest: SourceManifest,
    current_metrics: dict[str, object],
    baseline: BaselineSnapshot,
    verification: dict[str, object],
) -> dict[str, object]:
    diff = metric_diff(current_metrics, baseline.metrics)
    files = diff["files"]
    return {
        "schema": REPORT_SCHEMA,
        "source": _manifest_summary(manifest),
        "baseline": {
            "ref": baseline.ref,
            "available": baseline.available,
            "note": baseline.note,
            "source": baseline.source,
        },
        "summary": {
            "generated_pages": current_metrics["totals"]["pages"],
            "generated_table_rows": current_metrics["totals"]["table_rows"],
            "generated_bytes": current_metrics["totals"]["bytes"],
            "generated_pages_added": files["added"],
            "generated_pages_removed": files["removed"],
            "generated_pages_changed": files["changed"],
            "hand_written_pages": verification["hand_written_pages"],
            "stale_pages": len(verification["stale"]),
            "unversioned_pages": len(verification["missing"]),
            "invalid_versions": len(verification["invalid"]),
            "needs_update_pages": len(verification["needs_update"]),
        },
        "current_metrics": _plain_metrics(current_metrics),
        "baseline_metrics": _plain_metrics(baseline.metrics) if baseline.metrics else None,
        "diff": diff,
        "verification": verification,
    }


def human_bytes(value: int) -> str:
    size = float(value)
    for unit in ("B", "KiB", "MiB", "GiB"):
        if size < 1024 or unit == "GiB":
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024
    return f"{value} B"


def signed(value: int) -> str:
    return f"{value:+d}"


def summary_markdown(report: dict[str, object]) -> str:
    source = report["source"]
    baseline = report["baseline"]
    summary = report["summary"]
    diff = report["diff"]
    verification = report["verification"]
    lines = [
        "## Patch impact",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Locked game version | `{source['game_version']}` |",
        f"| Current source commit | `{source['commit']}` |",
        f"| Baseline | `{baseline.get('ref') or 'none'}` |",
        f"| Generated pages | {summary['generated_pages']:,} |",
        f"| Generated table rows | {summary['generated_table_rows']:,} |",
        f"| Generated bytes | {human_bytes(int(summary['generated_bytes']))} |",
        f"| Hand-written versioned scope | {summary['hand_written_pages']:,} pages |",
        f"| Stale verification | {summary['stale_pages']:,} pages |",
        f"| Missing verified_version | {summary['unversioned_pages']:,} pages |",
        f"| Invalid verified_version | {summary['invalid_versions']:,} pages |",
        "",
    ]
    if not baseline["available"]:
        lines.extend(
            [
                "### Generated-data difference",
                "",
                f"- Baseline unavailable: {baseline.get('note') or 'unknown reason'}",
                "",
            ]
        )
    else:
        file_diff = diff["files"]
        lines.extend(
            [
                "### Generated-data difference",
                "",
                f"- Pages: {file_diff['added']} added, {file_diff['removed']} removed, {file_diff['changed']} changed.",
                "",
                "| Dataset | Pages | Table rows | Bytes |",
                "|---|---:|---:|---:|",
            ]
        )
        if not diff["datasets"]:
            lines.append("| No metric changes | 0 | 0 | 0 |")
        else:
            for entry in diff["datasets"]:
                lines.append(
                    f"| `{entry['dataset']}` | {signed(entry['pages']['delta'])} | "
                    f"{signed(entry['table_rows']['delta'])} | "
                    f"{signed(entry['bytes']['delta'])} |"
                )
        lines.append("")

    lines.extend(["### Verification freshness", ""])
    stale = verification["stale"]
    missing = verification["missing"]
    invalid = verification["invalid"]
    if not (stale or missing or invalid):
        lines.append("- Every versioned hand-written page matches the locked game version.")
    if stale:
        lines.append(
            f"- {len(stale)} page(s) were verified before `{verification['target_version']}`."
        )
        for record in stale[:MAX_SAMPLES]:
            lines.append(
                f"  - `{record['path']}`: `{record['verified_version']}`"
                + (f" ({record['last_verified']})" if record["last_verified"] else "")
            )
    if missing:
        lines.append(f"- {len(missing)} hand-written page(s) have no `verified_version`.")
    if invalid:
        lines.append(f"- {len(invalid)} page(s) use an uncomparable `verified_version`.")
    lines.append("")
    return "\n".join(lines)


def append_summary(report: dict[str, object]) -> None:
    destination = os.environ.get("GITHUB_STEP_SUMMARY")
    if not destination:
        return
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(summary_markdown(report))


def github_escape(value: object) -> str:
    return (
        str(value)
        .replace("%", "%25")
        .replace("\r", "%0D")
        .replace("\n", "%0A")
        .replace(":", "%3A")
        .replace(",", "%2C")
    )


def annotations(report: dict[str, object]) -> list[str]:
    verification = report["verification"]
    target = verification["target_version"]
    output: list[str] = []
    for record in verification["stale"][:MAX_SAMPLES]:
        message = (
            f"verified_version {record['verified_version']} is older than locked game version {target}"
        )
        output.append(
            f"::warning file=docs/{github_escape(record['path'])},title=Patch verification stale::{github_escape(message)}"
        )
    remaining = MAX_SAMPLES - len(output)
    for record in verification["invalid"][:remaining]:
        message = record.get("message") or "verified_version cannot be compared"
        output.append(
            f"::warning file=docs/{github_escape(record['path'])},title=Patch verification invalid::{github_escape(message)}"
        )
    baseline = report["baseline"]
    if not baseline["available"]:
        output.append(
            "::notice title=Patch impact baseline unavailable::"
            + github_escape(baseline.get("note") or "no baseline metrics")
        )
    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="生成Data差分と手書き記事の検証VersionをReportします。"
    )
    parser.add_argument("--docs-dir", type=Path, default=ROOT / "docs")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT_PATH)
    parser.add_argument("--baseline-ref", help="比較対象を生成するGit ref")
    parser.add_argument(
        "--baseline-docs",
        type=Path,
        help="Git worktreeを使わず比較する、生成済みbaseline docs directory",
    )
    parser.add_argument("--github-summary", action="store_true")
    parser.add_argument("--require-baseline", action="store_true")
    parser.add_argument("--fail-on-stale", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest = SourceManifest.from_path(args.manifest, root=ROOT)
        current_metrics = collect_generated_metrics(args.docs_dir)
        verification = verification_inventory(args.docs_dir, manifest.game_version)
    except (OSError, ManifestError, ValueError) as exc:
        print(f"patch-impact error: {exc}", file=sys.stderr)
        return 2

    baseline_ref = args.baseline_ref or default_baseline_ref()
    if args.baseline_docs:
        baseline = snapshot_from_docs(args.baseline_docs, ref=baseline_ref)
    else:
        baseline = build_baseline_snapshot(ROOT, baseline_ref)
    report = build_report(manifest, current_metrics, baseline, verification)

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if args.github_summary:
        append_summary(report)
    for command in annotations(report):
        print(command)

    summary = report["summary"]
    print("Patch impact")
    print(f"  Locked game version: {report['source']['game_version']}")
    print(f"  Baseline: {report['baseline']['ref'] or 'none'}")
    print(f"  Baseline available: {report['baseline']['available']}")
    print(f"  Generated pages: {summary['generated_pages']}")
    print(f"  Generated table rows: {summary['generated_table_rows']}")
    print(
        "  Generated page diff: "
        f"+{summary['generated_pages_added']} "
        f"-{summary['generated_pages_removed']} "
        f"~{summary['generated_pages_changed']}"
    )
    print(f"  Stale hand-written pages: {summary['stale_pages']}")
    print(f"  Unversioned hand-written pages: {summary['unversioned_pages']}")
    print(f"  Report: {args.report}")

    if args.require_baseline and not baseline.available:
        return 1
    if args.fail_on_stale and (verification["stale"] or verification["invalid"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
