#!/usr/bin/env python3
"""Public Wiki audit entry point with repository-specific compatibility rules."""
from __future__ import annotations

try:
    from . import audit_wiki_core as _core
except ImportError:  # Direct execution: ``python scripts/audit_wiki.py``
    import audit_wiki_core as _core


# Generator output and the Wiki's pre-existing editorial state are valid inputs.
# ``expanding`` remains accepted during the staged migration to the new status model.
_core.ALLOWED_STATUSES.update({"generated", "expanding"})
_core_generated = _core.generated


def generated(relative, metadata: dict[str, str]) -> bool:
    """Identify pages owned by generators rather than hand-written content."""

    return metadata.get("status") == "generated" or _core_generated(relative, metadata)


_core.generated = generated


def _html_tag_end(text: str, start: int) -> int | None:
    """Return the inclusive end of a raw HTML tag/comment starting at ``start``."""

    if text.startswith("<!--", start):
        end = text.find("-->", start + 4)
        return len(text) - 1 if end < 0 else end + 2
    if start + 1 >= len(text):
        return None

    cursor = start + 1
    if text[cursor] == "/" or text[cursor] in "!?":
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
    """Hide raw HTML tags/comments without changing Markdown line numbers."""

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


_core_markdown_links = _core.markdown_links


def markdown_links(text: str):
    """Yield Markdown links while ignoring fenced code and raw HTML attributes."""

    yield from _core_markdown_links(strip_html_preserve_lines(text))


# ``audit`` resolves these globals at runtime, so patch the boundaries once.
_core.markdown_links = markdown_links

Issue = _core.Issue
front_matter = _core.front_matter
resolve_link = _core.resolve_link
audit = _core.audit
main = _core.main


if __name__ == "__main__":
    raise SystemExit(main())
