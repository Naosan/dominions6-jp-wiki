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


def _html_tag_end(text: str, start: int) -> int | None:
    """Return the inclusive end of a raw HTML tag/comment, if one starts here.

    Markdown angle destinations such as ``[Guide](<guide.md>)`` and autolinks
    such as ``<https://example.com>`` are deliberately not treated as HTML.
    """

    if text.startswith("<!--", start):
        end = text.find("-->", start + 4)
        return len(text) - 1 if end < 0 else end + 2

    if start + 1 >= len(text):
        return None

    cursor = start + 1
    if text[cursor] == "/":
        cursor += 1
    elif text[cursor] in "!?":
        cursor += 1

    name_start = cursor
    while cursor < len(text) and (text[cursor].isalnum() or text[cursor] in "_-"):
        cursor += 1

    if cursor == name_start:
        return None
    if cursor < len(text) and not (text[cursor].isspace() or text[cursor] in "/>"):
        return None

    quote = ""
    while cursor < len(text):
        char = text[cursor]
        if quote:
            if char == quote:
                quote = ""
        elif char in {'"', "'"}:
            quote = char
        elif char == ">":
            return cursor
        cursor += 1
    return len(text) - 1


def strip_html_preserve_lines(text: str) -> str:
    """Replace raw HTML tags/comments with spaces while retaining line numbers."""

    output = list(text)
    cursor = 0
    while cursor < len(text):
        if text[cursor] != "<":
            cursor += 1
            continue
        end = _html_tag_end(text, cursor)
        if end is None:
            cursor += 1
            continue
        for index in range(cursor, end + 1):
            if output[index] not in "\r\n":
                output[index] = " "
        cursor = end + 1
    return "".join(output)


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
    text = strip_html_preserve_lines(text)
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
        status = metadata.get("status", "").strip()
        if not status and generated(relative, metadata):
            status = "generated"
        statuses[status or "unspecified"] += 1
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
            incoming[]H
ÏHB‚ˆÜœ[œÎˆ\İÜİ—HH×BˆÜœ[—ÜÙ]™\š]HH™\œ›ÜˆˆYˆ˜Z[ÛÜœ[œÈ[ÙHØ\›š[™È‚ˆ›Üˆ][ˆš[\Î‚ˆ™[]]™HH]œ™[]]™WİÊØÜÊBˆYˆÙ[™\˜]Y
™[]]™KY]Y]WØWÙš[VÜ]JN‚ˆÛÛ[YBˆYˆ™[]]™K›˜[YHOHš[™^›YˆÜˆ™[]]™Kœ\ÖÌHOH[\]\È‚ˆÛÛ[YBˆYˆ][ˆ˜]—Ùš[\ÈÜˆ[˜ÛÛZ[™ÖÆF…Ó ¢6öçF–çVP¢÷'†ç2æVæB‡&VÆF—fRæ5÷÷6—‚‚’¢—77VW2æVæB„—77VR†÷'†å÷6WfW&—G’Â'vRÖ÷'†â"Â&VÆF—fRæ5÷÷6—‚‚’Â'vR†2æò–æ6öÖ–ærÆ–æ²÷"æf–vF–öâVçG'’"’ ¢&WGW&â°¢&f–ÆW2#¢ÆVâ†f–ÆW2’À¢&g&öçEöÖGFW%öf–ÆW2#¢g&öçEö6÷VçBÀ¢'7FGW6W2#¢F–7B‡6÷'FVB‡7FGW6W2æ—FV×2‚’’’À¢&Æö6ÅöÆ–æ·2#¢Æö6ÅöÆ–æµö6÷VçBÀ¢&æf–vF–öå÷F&vWG2#¢ÆVâ†æb’À¢&÷'†å÷vW2#¢÷'†ç2À¢&—77VW2#¢—77VW2À¢Ğ  ¦FVb&–çE÷&W7VÇB‡&W7VÇB’ÓâæöæS ¢W'&÷'2Ò¶—77VRf÷"—77VR–â&W7VÇE²&—77VW2%Ò–b—77VRç6WfW&—G’ÓÒ&W'&÷"%Ğ¢v&æ–æw2Ò¶—77VRf÷"—77VR–â&W7VÇE²&—77VW2%Ò–b—77VRç6WfW&—G’ÓÒ'v&æ–ær%Ğ¢&–çB‚%v–¶’VF—B"¢&–çB†b"Ö&¶F÷vâf–ÆW3¢·&W7VÇE²vf–ÆW2u×Ò"¢&–çB†b"g&öçBÖGFW#¢·&W7VÇE²vg&öçEöÖGFW%öf–ÆW2u×Ò"¢&–çB†b"Æö6ÂÆ–æ·3¢·&W7VÇE²vÆö6ÅöÆ–æ·2u×Ò"¢&–çB†b"æf–vF–öâF&vWG3¢·&W7VÇE²væf–vF–öå÷F&vWG2u×Ò"¢&–çB†b"÷'†âvW3¢¶ÆVâ‡&W7VÇE²v÷'†å÷vW2uÒ—Ò"¢&–çB†b"W'&÷'3¢¶ÆVâ†W'&÷'2—Ò"¢&–çB†b"v&æ–æw3¢¶ÆVâ‡v&æ–æw2—Ò"¢&–çB‚"7FGW3¢"²"Â"æ¦ö–â†b'¶¶W—Ó×·fÇVWÒ"f÷"¶W’ÂfÇVR–â&W7VÇE²'7FGW6W2%Òæ—FV×2‚’’¢f÷"—77VR–â6÷'FVB‡&W7VÇE²&—77VW2%ÒÂ¶W“ÖÆÖ&F—FVÓ¢†—FVÒç6WfW&—G’Ò&W'&÷""Â—FVÒçF‚Â—FVÒæÆ–æR÷"Â—FVÒæ6öFR’“ ¢v†W&RÒ—77VRçF‚²†b#§¶—77VRæÆ–æWÒ"–b—77VRæÆ–æRVÇ6R""¢&–çB†b'¶—77VRç6WfW&—G’çWW"‚—Ó¢·v†W&WÓ¢·¶—77VRæ6öFWÕÒ¶—77VRæÖW76vWÒ"  ¦FVbÖ–â‚’Óâ–çC ¢'6W"Ò&w'6Rä&wVÖVçE'6W"†FW67&—F–öãÒ%v–¶8îjx¾˜
8Š‰K¨´ÖWFFF8).jIÎiû¾8~8î88""¢'6W"æFEö&wVÖVçB‚"ÒÖFö72ÖF—""ÂG—SÕF‚ÂFVfVÇCÕ$ôõBò&Fö72"¢'6W"æFEö&wVÖVçB‚"ÒÖ6öæf–r"ÂG—SÕF‚ÂFVfVÇCÕ$ôõBò'¦Vç6–6ÂçFöÖÂ"¢'6W"æFEö&wVÖVçB‚"Ò×&W÷'B"ÂG—SÕF‚¢'6W"æFEö&wVÖVçB‚"Ò×7G&–7BÖÖWFFF"Â7F–öãÒ'7F÷&U÷G'VR"¢'6W"æFEö&wVÖVçB‚"ÒÖf–ÂÖöâÖ÷'†ç2"Â7F–öãÒ'7F÷&U÷G'VR"¢&w2Ò'6W"ç'6Uö&w2‚¢G'“ ¢&W7VÇBÒVF—B†&w2æFö75öF—"Â&w2æ6öæf–rÂ&w2ç7G&–7EöÖWFFFÂ&w2æf–Åööåö÷'†ç2¢W†6WB„õ4W'&÷"ÂFöÖÆÆ–"åDôÔÄFV6öFTW'&÷"’2W†3 ¢&–çB†b$U%$õ#¢VF—B6÷VÆBæ÷B7F'C¢¶W†7Ò"Âf–ÆS×7—2ç7FFW'"¢&WGW&â  ¢&–çE÷&W7VÇB‡&W7VÇB¢–b&w2ç&W÷'C ¢&w2ç&W÷'Bç&VçBæÖ¶F—"‡&VçG3ÕG'VRÂW†—7Eöö³ÕG'VR¢6W&–Æ—¦&ÆRÒF–7B‡&W7VÇB¢6W&–Æ—¦&ÆU²&—77VW2%ÒÒ¶6F–7B†—77VR’f÷"—77VR–â&W7VÇE²&—77VW2%ÕĞ¢&w2ç&W÷'Bçw&—FU÷FW‡B†§6öâæGV×2‡6W&–Æ—¦&ÆRÂVç7W&Uö66–“ÔfÇ6RÂ–æFVçCÓ"’²%Æâ"ÂVæ6öF–æsÒ'WFbÓ‚"¢&–çB†b$¥4ôâ&W÷'C¢¶&w2ç&W÷'GÒ"¢&WGW&â–çB†ç’†—77VRç6WfW&—G’ÓÒ&W'&÷""f÷"—77VR–â&W7VÇE²&—77VW2%Ò’  ¦–bõöæÖUõòÓÒ%õöÖ–åõò# ¢&—6R7—7FVÔW†—B†Ö–â‚’