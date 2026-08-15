#!/usr/bin/env python3
"""Run extended Magic Access generation with safe compatibility patches.

The generated profile uses ``sum`` for both numeric counters and truthy caster
lists. This wrapper normalizes those values to booleans, adds the hand-written
guide to navigation, and keeps cross-links on one Markdown line.
"""
from __future__ import annotations

from pathlib import Path

import generate_extended_magic_access_data as generator


def safe_sum(values, start=0):
    total = start
    for value in values:
        if isinstance(value, (list, tuple, set, dict)):
            total += int(bool(value))
        else:
            total += value
    return total


def patch_guide_navigation() -> bool:
    path = generator.CONFIG
    text = path.read_text(encoding="utf-8")
    addition = '    "magic/extended-magic-access.md",'
    if addition in text:
        return False
    anchor = '    "magic/site-search-playbook.md",'
    if anchor not in text:
        raise ValueError(f"Magic navigation anchor missing: {anchor}")
    path.write_text(
        text.replace(anchor, anchor + "\n" + addition, 1),
        encoding="utf-8",
    )
    return True


def normalize_cross_links() -> int:
    changed = 0
    marker = "\n · [拡張Magic Access]"
    replacement = " · [拡張Magic Access]"
    for profile in generator.nations_for_link_normalization:
        for root in (generator.RECRUIT_ROOT, generator.SITE_SEARCH_ROOT):
            path = root / str(profile["dir"]) / f"{profile['slug']}.md"
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            if marker not in text:
                continue
            path.write_text(text.replace(marker, replacement, 1), encoding="utf-8")
            changed += 1
    return changed


def main() -> None:
    generator.sum = safe_sum
    generator.nations_for_link_normalization = []

    original_patch = generator.patch_navigation_and_indexes

    def patched(profiles):
        generator.nations_for_link_normalization = [profile["nation"] for profile in profiles]
        counts = original_patch(profiles)
        counts["guide_navigation"] = int(patch_guide_navigation())
        counts["normalized_cross_links"] = normalize_cross_links()
        return counts

    generator.patch_navigation_and_indexes = patched
    generator.main()


if __name__ == "__main__":
    main()
