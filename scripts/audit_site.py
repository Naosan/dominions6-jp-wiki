#!/usr/bin/env python3
"""Audit the rendered Wiki before it is published to GitHub Pages.

The source audit validates Markdown and navigation inputs. This script validates
properties that only exist after Zensical has rendered the site: output size,
canonical URLs, generated data-record templates, search metadata, and sitemap
metadata.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tomllib
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WARNING_BYTES = 800_000_000
DEFAULT_FAILURE_BYTES = 950_000_000
DATA_RECORD_ROOTS = (
    "data/units/by-id",
    "data/sites/by-id",
    "data/items/by-id",
)
DATA_RECORD_PATTERNS = tuple(f"{root}/*/index.html" for root in DATA_RECORD_ROOTS)
DATA_RECORD_PREFIXES = tuple(f"{root}/" for root in DATA_RECORD_ROOTS)
CANONICAL_RE = re.compile(
    rb"<link\b(?=[^>]*\brel=[\"']canonical[\"'])"
    rb"(?=[^>]*\bhref=[\"']([^\"']+)[\"'])[^>]*>",
    re.IGNORECASE,
)
PRIMARY_NAV_MARKER = b'data-md-type="navigation"'
TOC_NAV_MARKER = b'data-md-type="toc"'
CONTENT_MARKER = b'data-md-component="content"'


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    path: str
    message: str


def format_bytes(value: int) -> str:
    """Return a compact binary-size label suitable for console summaries."""

    units = ("B", "KiB", "MiB", "GiB")
    amount = float(value)
    for unit in units:
        if amount < 1024 or unit == units[-1]:
            return f"{amount:.1f} {unit}" if unit != "B" else f"{int(amount)} B"
        amount /= 1024
    raise AssertionError("unreachable")


def examples(paths: list[str], limit: int = 5) -> str:
    """Format a bounded list so one regression cannot flood the report."""

    shown = paths[:limit]
    suffix = f" (+{len(paths) - limit} more)" if len(paths) > limit else ""
    return ", ".join(shown) + suffix


def read_site_url(config: Path) -> str:
    with config.open("rb") as handle:
        value = tomllib.load(handle).get("project", {}).get("site_url", "")
    return str(value).strip().rstrip("/") + "/" if value else ""


def search_metrics(path: Path, issues: list[Issue]) -> dict[str, Any]:
    metrics: dict[str, Any] = {
        "path": path.name,
        "bytes": 0,
        "items": 0,
        "data_record_items": 0,
        "data_record_ratio": 0.0,
    }
    if not path.is_file():
        issues.append(Issue("error", "search-missing", path.name, "search.json was not generated"))
        return metrics

    metrics["bytes"] = path.stat().st_size
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        issues.append(Issue("error", "search-invalid", path.name, f"could not parse search.json: {exc}"))
        return metrics

    items = payload.get("items") if isinstance(payload, dict) else None
    if not isinstance(items, list):
        issues.append(Issue("error", "search-items-invalid", path.name, "search.json has no items array"))
        return metrics

    record_items = 0
    for item in items:
        if not isinstance(item, dict):
            continue
        location = str(item.get("location") or "").lstrip("/")
        if location.startswith(DATA_RECORD_PREFIXES):
            record_items += 1

    metrics["items"] = len(items)
    metrics["data_record_items"] = record_items
    metrics["data_record_ratio"] = record_items / len(items) if items else 0.0
    return metrics


def sitemap_metrics(path: Path, site_url: str, issues: list[Issue]) -> dict[str, Any]:
    metrics: dict[str, Any] = {"path": path.name, "bytes": 0, "urls": 0}
    if not path.is_file():
        issues.append(Issue("error", "sitemap-missing", path.name, "sitemap.xml was not generated"))
        return metrics

    metrics["bytes"] = path.stat().st_size
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as exc:
        issues.append(Issue("error", "sitemap-invalid", path.name, f"could not parse sitemap.xml: {exc}"))
        return metrics

    locations = [str(node.text or "").strip() for node in root.findall(".//{*}loc")]
    metrics["urls"] = len(locations)
    if site_url:
        invalid = [value for value in locations if value and not value.startswith(site_url)]
        if invalid:
            issues.append(
                Issue(
                    "error",
                    "sitemap-url-outside-site",
                    path.name,
                    f"{len(invalid)} URL(s) do not start with {site_url}: {examples(invalid)}",
                )
            )
    return metrics


def audit(
    site_dir: Path,
    config: Path,
    *,
    warning_bytes: int = DEFAULT_WARNING_BYTES,
    failure_bytes: int = DEFAULT_FAILURE_BYTES,
) -> dict[str, Any]:
    """Return rendered-site metrics and bounded, actionable issues."""

    site_dir = site_dir.resolve()
    config = config.resolve()
    if warning_bytes < 0 or failure_bytes <= 0 or warning_bytes >= failure_bytes:
        raise ValueError("size thresholds must satisfy 0 <= warning < failure")
    if not site_dir.is_dir():
        raise FileNotFoundError(f"site directory does not exist: {site_dir}")

    issues: list[Issue] = []
    site_url = read_site_url(config)
    if not site_url:
        issues.append(Issue("warning", "site-url-missing", config.name, "project.site_url is not configured"))

    files = sorted(path for path in site_dir.rglob("*") if path.is_file())
    html_files = [path for path in files if path.suffix.lower() == ".html"]
    total_bytes = sum(path.stat().st_size for path in files)
    html_bytes = sum(path.stat().st_size for path in html_files)

    if total_bytes >= failure_bytes:
        issues.append(
            Issue(
                "error",
                "site-size-limit",
                site_dir.name,
                f"rendered site is {format_bytes(total_bytes)}; failure threshold is {format_bytes(failure_bytes)}",
            )
        )
    elif total_bytes >= warning_bytes:
        issues.append(
            Issue(
                "warning",
                "site-size-warning",
                site_dir.name,
                f"rendered site is {format_bytes(total_bytes)}; warning threshold is {format_bytes(warning_bytes)}",
            )
        )

    record_files = sorted(
        {path for pattern in DATA_RECORD_PATTERNS for path in site_dir.glob(pattern)}
    )
    if not record_files:
        issues.append(
            Issue(
                "error",
                "data-records-missing",
                site_dir.name,
                "no rendered by-id data-record pages were found",
            )
        )

    record_set = set(record_files)
    missing_canonical: list[str] = []
    invalid_canonical: list[str] = []
    duplicate_canonical: list[str] = []
    record_primary_nav: list[str] = []
    record_toc_nav: list[str] = []
    record_missing_content: list[str] = []
    canonical_pages = 0

    for path in html_files:
        relative = path.relative_to(site_dir).as_posix()
        content = path.read_bytes()

        if path.name != "404.html":
            canonical = CANONICAL_RE.findall(content)
            if not canonical:
                missing_canonical.append(relative)
            else:
                canonical_pages += 1
                if len(canonical) > 1:
                    duplicate_canonical.append(relative)
                value = canonical[0].decode("utf-8", errors="replace")
                if site_url and not value.startswith(site_url):
                    invalid_canonical.append(f"{relative} -> {value}")

        if path in record_set:
            if PRIMARY_NAV_MARKER in content:
                record_primary_nav.append(relative)
            if TOC_NAV_MARKER in content:
                record_toc_nav.append(relative)
            if CONTENT_MARKER not in content:
                record_missing_content.append(relative)

    for code, paths, message in (
        ("canonical-missing", missing_canonical, "HTML page(s) have no canonical URL"),
        ("canonical-duplicate", duplicate_canonical, "HTML page(s) have multiple canonical URLs"),
        ("canonical-outside-site", invalid_canonical, "canonical URL(s) do not start with project.site_url"),
        (
            "data-record-primary-nav",
            record_primary_nav,
            "data-record page(s) still contain the global primary navigation; the lightweight template was not applied",
        ),
        (
            "data-record-content-missing",
            record_missing_content,
            "data-record page(s) do not contain the main content component",
        ),
    ):
        if paths:
            issues.append(Issue("error", code, site_dir.name, f"{len(paths)} {message}: {examples(paths)}"))

    record_bytes = sum(path.stat().st_size for path in record_files)
    largest = sorted(
        (
            {
                "path": path.relative_to(site_dir).as_posix(),
                "bytes": path.stat().st_size,
            }
            for path in files
        ),
        key=lambda item: (-int(item["bytes"]), str(item["path"])),
    )[:20]

    metrics: dict[str, Any] = {
        "site_url": site_url,
        "files": len(files),
        "total_bytes": total_bytes,
        "html_files": len(html_files),
        "html_bytes": html_bytes,
        "canonical_pages": canonical_pages,
        "data_record_files": len(record_files),
        "data_record_bytes": record_bytes,
        "data_record_primary_navigation_pages": len(record_primary_nav),
        "data_record_toc_pages": len(record_toc_nav),
        "search": search_metrics(site_dir / "search.json", issues),
        "sitemap": sitemap_metrics(site_dir / "sitemap.xml", site_url, issues),
        "largest_files": largest,
    }
    errors = sum(issue.severity == "error" for issue in issues)
    warnings = sum(issue.severity == "warning" for issue in issues)
    return {
        "site_dir": str(site_dir),
        "config": str(config),
        "thresholds": {
            "warning_bytes": warning_bytes,
            "failure_bytes": failure_bytes,
        },
        "metrics": metrics,
        "issues": issues,
        "errors": errors,
        "warnings": warnings,
        "status": "error" if errors else "warning" if warnings else "ok",
    }


def print_result(result: dict[str, Any]) -> None:
    metrics = result["metrics"]
    search = metrics["search"]
    sitemap = metrics["sitemap"]
    print("Rendered site audit")
    print(f"  Files: {metrics['files']:,}")
    print(f"  Total size: {format_bytes(metrics['total_bytes'])}")
    print(f"  HTML: {metrics['html_files']:,} files / {format_bytes(metrics['html_bytes'])}")
    print(
        "  Data records: "
        f"{metrics['data_record_files']:,} files / {format_bytes(metrics['data_record_bytes'])}"
    )
    print(
        "  Data-record navigation: "
        f"primary={metrics['data_record_primary_navigation_pages']:,}, "
        f"toc={metrics['data_record_toc_pages']:,}"
    )
    print(
        "  Search: "
        f"{search['items']:,} items / {format_bytes(search['bytes'])} / "
        f"data records={search['data_record_items']:,} ({search['data_record_ratio']:.1%})"
    )
    print(f"  Sitemap URLs: {sitemap['urls']:,}")
    print(f"  Errors: {result['errors']}")
    print(f"  Warnings: {result['warnings']}")
    for issue in result["issues"]:
        print(f"{issue.severity.upper()}: {issue.path}: [{issue.code}] {issue.message}")


def github_summary(result: dict[str, Any]) -> str:
    metrics = result["metrics"]
    search = metrics["search"]
    sitemap = metrics["sitemap"]
    lines = [
        "## Rendered site audit",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Status | **{result['status']}** |",
        f"| Total files | {metrics['files']:,} |",
        f"| Total size | {format_bytes(metrics['total_bytes'])} |",
        f"| HTML | {metrics['html_files']:,} / {format_bytes(metrics['html_bytes'])} |",
        f"| Data-record pages | {metrics['data_record_files']:,} / {format_bytes(metrics['data_record_bytes'])} |",
        f"| Data records with global navigation | {metrics['data_record_primary_navigation_pages']:,} |",
        f"| Search index | {search['items']:,} items / {format_bytes(search['bytes'])} |",
        f"| Search entries from data records | {search['data_record_items']:,} ({search['data_record_ratio']:.1%}) |",
        f"| Sitemap URLs | {sitemap['urls']:,} |",
        f"| Errors / warnings | {result['errors']} / {result['warnings']} |",
        "",
    ]
    if result["issues"]:
        lines.extend(["### Findings", ""])
        for issue in result["issues"]:
            marker = "❌" if issue.severity == "error" else "⚠️"
            lines.append(f"- {marker} `{issue.code}` — {issue.message}")
        lines.append("")
    return "\n".join(lines)


def serializable(result: dict[str, Any]) -> dict[str, Any]:
    payload = dict(result)
    payload["issues"] = [asdict(issue) for issue in result["issues"]]
    return payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Zensical build後の公開物を監査します。")
    parser.add_argument("--site-dir", type=Path, default=ROOT / "site")
    parser.add_argument("--config", type=Path, default=ROOT / "zensical.toml")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--warning-bytes", type=int, default=DEFAULT_WARNING_BYTES)
    parser.add_argument("--failure-bytes", type=int, default=DEFAULT_FAILURE_BYTES)
    parser.add_argument("--github-summary", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        result = audit(
            args.site_dir,
            args.config,
            warning_bytes=args.warning_bytes,
            failure_bytes=args.failure_bytes,
        )
    except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
        print(f"ERROR: rendered site audit could not start: {exc}", file=sys.stderr)
        return 2

    print_result(result)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps(serializable(result), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"JSON report: {args.report}")

    if args.github_summary:
        summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary_path:
            with Path(summary_path).open("a", encoding="utf-8") as handle:
                handle.write(github_summary(result))
        else:
            print("GITHUB_STEP_SUMMARY is not set; summary output was skipped.")

    return int(result["errors"] > 0)


if __name__ == "__main__":
    raise SystemExit(main())
