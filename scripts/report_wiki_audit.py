#!/usr/bin/env python3
"""Render a Wiki audit JSON report as GitHub Actions annotations and a job summary."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def escape_message(value: object) -> str:
    """Escape a GitHub workflow-command message."""

    return str(value).replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def escape_property(value: object) -> str:
    """Escape a GitHub workflow-command property."""

    return escape_message(value).replace(":", "%3A").replace(",", "%2C")


def annotation(issue: dict[str, object]) -> str:
    """Convert one audit issue into a GitHub Actions workflow command."""

    severity = str(issue.get("severity", "warning"))
    level = "error" if severity == "error" else "warning"
    path = str(issue.get("path", ".github"))
    code = str(issue.get("code", "wiki-audit"))
    message = str(issue.get("message", "Wiki audit issue"))

    properties = [f"file={escape_property(path)}", f"title={escape_property('Wiki audit: ' + code)}"]
    line = issue.get("line")
    if isinstance(line, int) and line > 0:
        properties.append(f"line={line}")
        properties.append(f"endLine={line}")

    return f"::{level} {','.join(properties)}::{escape_message(message)}"


def append_summary(report: dict[str, object], errors: list[dict[str, object]], warnings: list[dict[str, object]]) -> None:
    """Append a compact audit summary to the GitHub Actions job summary."""

    destination = os.environ.get("GITHUB_STEP_SUMMARY")
    if not destination:
        return

    statuses = report.get("statuses", {})
    status_text = ", ".join(f"`{key}`: {value}" for key, value in sorted(statuses.items())) if isinstance(statuses, dict) else "n/a"
    lines = [
        "## Wiki audit",
        "",
        "| Metric | Count |",
        "|---|---:|",
        f"| Markdown files | {report.get('files', 0)} |",
        f"| Front matter | {report.get('front_matter_files', 0)} |",
        f"| Local links | {report.get('local_links', 0)} |",
        f"| Navigation targets | {report.get('navigation_targets', 0)} |",
        f"| Orphan pages | {len(report.get('orphan_pages', [])) if isinstance(report.get('orphan_pages'), list) else 0} |",
        f"| Errors | {len(errors)} |",
        f"| Warnings | {len(warnings)} |",
        "",
        f"Statuses: {status_text}",
        "",
    ]
    with Path(destination).open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser(description="Wiki audit JSONをGitHub Actions Annotationへ変換します。")
    parser.add_argument("report", type=Path)
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    report = json.loads(args.report.read_text(encoding="utf-8"))
    raw_issues = report.get("issues", [])
    issues = [issue for issue in raw_issues if isinstance(issue, dict)] if isinstance(raw_issues, list) else []
    errors = [issue for issue in issues if issue.get("severity") == "error"]
    warnings = [issue for issue in issues if issue.get("severity") == "warning"]

    append_summary(report, errors, warnings)

    selected = errors[: max(args.limit, 0)]
    for issue in selected:
        print(annotation(issue))
    if len(errors) > len(selected):
        print(f"::notice title=Wiki audit::Only the first {len(selected)} of {len(errors)} errors were annotated.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
