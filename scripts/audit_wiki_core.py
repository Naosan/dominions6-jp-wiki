#!/usr/bin/env python3
"""Audit Wiki front matter, local links, navigation targets, and orphan pages."""
from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_STATUSES = {"stub", "draft", "reviewed", "verified", "needs-update"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FIELD_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$")
LINK_RE = re.compile(
    r"!?\[[^\]]*\]\(\s*(?P<target><[^>]+>|[^)\s]+)"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
FENCE_RE = re.compile(r"^\s*(```+|~~~+)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    path: str
    message: str
    line: int | None = None


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def front_matter(text: str) -> tuple[bool, dict[str, str], str | None]:
    lines = text.lstrip("\ufeff").splitlines()
    if not lines or lines[0].strip() != "---":
        return False, {}, None
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return True, {}, "closing '---' was not found"
    values: dict[str, str] = {}
    for line in lines[1:end]:
        match = FIELD_RE.match(line)
        if match:
            values[match.group(1)] = scalar(match.group(2))
    return True, values, None


def markdown_links(text: str):
    in_fence = False
    fence_char = ""
    for number, line in enumerate(text.splitlines(), 1):
        fence = FENCE_RE.match(line)
        if fence:
            char = fence.group(1)[0]
            if not in_fence:
                in_fence, fence_char = True, char
            elif char == fence_char:
                in_fence, fence_char = False, ""
            continue
        if in_fence:
            continue
        line = INLINE_CODE_RE.sub("", line)
        for match in LINK_RE.finditer(line):
            target = match.group("target").strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1].strip()
            yield number, target


def external(target: str) -> bool:
    lowered = target.lower()
    return (
        not target
        or target.startswith(("#", "//"))
        or lowered.startswith(("http://", "https://", "mailto:", "tel:", "data:"))
        or "{{" in target
        or "}}" in target
        or "$" in target
    )


def candidates(source: Path, target: str, docs: Path) -> list[Path]:
    raw = unquote(urlsplit(target).path).replace("\\", "/")
    if not raw:
        return []
    base = docs if raw.startswith("/") else source.parent
    path = base / raw.lstrip("/") if raw.startswith("/") else base / raw
    if raw.endswith("/"):
        found = [path / "index.md"]
    elif path.suffix.lower() == ".html":
        found = [path.with_suffix(".md"), path.with_suffix("") / "index.md"]
    elif path.suffix:
        found = [path]
    else:
        found = [path, path.with_suffix(".md"), path / "index.md"]
    return [item.resolve(strict=False) for item in found]


def resolve_link(source: Path, target: str, docs: Path) -> Path | None:
    return next((path for path in candidates(source, target, docs) if path.is_file()), None)


def nav_strings(value):
    if isinstance(value, str):
        if value.endswith(".md"):
            yield value
    elif isinstance(value, list):
        for item in value:
            yield from nav_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from nav_strings(item)


def generated(relative: Path, metadata: dict[str, str]) -> bool:
    name = relative.as_posix()
    return metadata.get("status") == "stub" or (
        name.startswith("data/") and name not in {"data/index.md", "data/unit-loadouts.md"}
    )


def add_metadata_issues(
    issues: list[Issue],
    relative: Path,
    present: bool,
    metadata: dict[str, str],
    parse_error: str | None,
    strict: bool,
) -> None:
    path = relative.as_posix()
    missing_severity = "error" if strict else "warning"
    if parse_error:
        issues.append(Issue("error", "front-matter-malformed", path, parse_error))
        return
    if not present:
        issues.append(Issue(missing_severity, "front-matter-missing", path, "front matter is missing"))
        return
    if not metadata.get("title", "").strip():
        issues.append(Issue(missing_severity, "title-missing", path, "front matter has no title"))

    status = metadata.get("status", "").strip()
    if status and status not in ALLOWED_STATUSES:
        issues.append(Issue("error", "status-invalid", path, f"unknown status: {status}"))
    elif not status and not generated(relative, metadata):
        issues.append(Issue(missing_severity, "status-missing", path, "hand-written page has no status"))

    checked = metadata.get("last_verified", "").strip()
    if checked and not DATE_RE.fullmatch(checked):
        issues.append(Issue("error", "last-verified-invalid", path, "last_verified must use YYYY-MM-DD"))

    versioned = metadata.get("page_type", "").strip() not in {"project", "template"}
    if status in {"reviewed", "verified"} and versioned:
        if not metadata.get("verified_version", "").strip():
            issues.append(Issue(missing_severity, "verified-version-missing", path, "reviewed page has no verified_version"))
        if not checked:
            issues.append(Issue(missing_severity, "last-verified-missing", path, "reviewed page has no last_verified"))


def audit(docs: Path, config: Path, strict: bool = False, fail_orphans: bool = False):
    docs = docs.resolve()
    files = sorted(path.resolve() for path in docs.rglob("*.md") if path.is_file())
    file_set = set(files)
    issues: list[Issue] = []
    metadata_by_file: dict[Path, dict[str, str]] = {}
    incoming = defaultdict(int)
    statuses: Counter[str] = Counter()
    local_link_count = 0
    front_count = 0

    for path in files:
        relative = path.relative_to(docs)
        text = path.read_text(encoding="utf-8")
        present, metadata, parse_error = front_matter(text)
        front_count += int(present)
        metadata_by_file[path] = metadata
        statuses[metadata.get("status", "").strip() or "unspecified"] += 1
        add_metadata_issues(issues, relative, present, metadata, parse_error, strict)

        for line, target in markdown_links(text):
            if external(target):
                continue
            local_link_count += 1
            resolved = resolve_link(path, target, docs)
            if resolved is None:
                issues.append(Issue("error", "link-broken", relative.as_posix(), f"target does not exist: {target}", line))
            elif resolved in file_set and resolved != path:
                incoming[resolved] += 1

    with config.open("rb") as handle:
        nav = list(nav_strings(tomllib.load(handle).get("project", {}).get("nav", [])))
    nav_files: set[Path] = set()
    for target in nav:
        path = (docs / target).resolve(strict=False)
        if not path.is_file():
            issues.append(Issue("error", "nav-target-missing", config.name, f"target does not exist: {target}"))
        else:
            nav_files.add(path)
            incoming[path] += 1

    orphans: list[str] = []
    orphan_severity = "error" if fail_orphans else "warning"
    for path in files:
        relative = path.relative_to(docs)
        if generated(relative, metadata_by_file[path]):
            continue
        if relative.name == "index.md" or relative.parts[0] == "templates":
            continue
        if path in nav_files or incoming[path]:
            continue
        orphans.append(relative.as_posix())
        issues.append(Issue(orphan_severity, "page-orphan", relative.as_posix(), "page has no incoming link or navigation entry"))

    return {
        "files": len(files),
        "front_matter_files": front_count,
        "statuses": dict(sorted(statuses.items())),
        "local_links": local_link_count,
        "navigation_targets": len(nav),
        "orphan_pages": orphans,
        "issues": issues,
    }


def print_result(result) -> None:
    errors = [issue for issue in result["issues"] if issue.severity == "error"]
    warnings = [issue for issue in result["issues"] if issue.severity == "warning"]
    print("Wiki audit")
    print(f"  Markdown files: {result['files']}")
    print(f"  Front matter: {result['front_matter_files']}")
    print(f"  Local links: {result['local_links']}")
    print(f"  Navigation targets: {result['navigation_targets']}")
    print(f"  Orphan pages: {len(result['orphan_pages'])}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    print("  Status: " + ", ".join(f"{key}={value}" for key, value in result["statuses"].items()))
    for issue in sorted(result["issues"], key=lambda item: (item.severity != "error", item.path, item.line or 0, item.code)):
        where = issue.path + (f":{issue.line}" if issue.line else "")
        print(f"{issue.severity.upper()}: {where}: [{issue.code}] {issue.message}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Wikiの構造と記事Metadataを検査します。")
    parser.add_argument("--docs-dir", type=Path, default=ROOT / "docs")
    parser.add_argument("--config", type=Path, default=ROOT / "zensical.toml")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--strict-metadata", action="store_true")
    parser.add_argument("--fail-on-orphans", action="store_true")
    args = parser.parse_args()
    try:
        result = audit(args.docs_dir, args.config, args.strict_metadata, args.fail_on_orphans)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        print(f"ERROR: audit could not start: {exc}", file=sys.stderr)
        return 2

    print_result(result)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        serializable = dict(result)
        serializable["issues"] = [asdict(issue) for issue in result["issues"]]
        args.report.write_text(json.dumps(serializable, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"JSON report: {args.report}")
    return int(any(issue.severity == "error" for issue in result["issues"]))


if __name__ == "__main__":
    raise SystemExit(main())
