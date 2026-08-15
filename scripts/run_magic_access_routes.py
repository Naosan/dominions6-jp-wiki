#!/usr/bin/env python3
"""Run Magic Access route generation and integrate cross-links safely."""
from __future__ import annotations

from pathlib import Path

import generate_magic_access_routes as generator
from generate_recruitment_data import nations

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "zensical.toml"
DATA_INDEX = ROOT / "docs" / "data" / "index.md"
MAGE_ACCESS = ROOT / "docs" / "data" / "mage-access.md"
SITE_SEARCH_INDEX = ROOT / "docs" / "data" / "site-search" / "index.md"
EXTENDED_INDEX = ROOT / "docs" / "data" / "extended-magic-access" / "index.md"
BOOSTING = ROOT / "docs" / "magic" / "boosting.md"
COMMUNIONS = ROOT / "docs" / "magic" / "communions.md"
EXTENDED_GUIDE = ROOT / "docs" / "magic" / "extended-magic-access.md"
RECRUIT_ROOT = ROOT / "docs" / "data" / "recruitment"
SITE_SEARCH_ROOT = ROOT / "docs" / "data" / "site-search"
EXTENDED_ROOT = ROOT / "docs" / "data" / "extended-magic-access"


def insert_after(path: Path, anchor: str, additions: list[str]) -> bool:
    if not path.exists():
        raise FileNotFoundError(f"required page missing: {path}")
    text = path.read_text(encoding="utf-8")
    if additions and additions[0] in text:
        return False
    if anchor not in text:
        raise ValueError(f"anchor not found in {path}: {anchor!r}")
    path.write_text(
        text.replace(anchor, anchor + "\n" + "\n".join(additions), 1),
        encoding="utf-8",
    )
    return True


def append_inline(path: Path, anchor: str, addition: str) -> bool:
    if not path.exists():
        raise FileNotFoundError(f"required page missing: {path}")
    text = path.read_text(encoding="utf-8")
    if addition.strip() in text:
        return False
    if anchor not in text:
        raise ValueError(f"inline anchor not found in {path}: {anchor!r}")
    path.write_text(
        text.replace(anchor, anchor + addition, 1),
        encoding="utf-8",
    )
    return True


def patch_navigation() -> int:
    changed = 0
    changed += insert_after(
        CONFIG,
        '    "data/extended-magic-access/data-quality.md",',
        [
            '    "data/magic-access-routes/index.md",',
            '    "data/magic-access-routes/booster-routes.md",',
            '    "data/magic-access-routes/summon-chains.md",',
            '    "data/magic-access-routes/communion-sabbath.md",',
            '    "data/magic-access-routes/empowerment-gaps.md",',
            '    "data/magic-access-routes/data-quality.md",',
        ],
    )
    changed += insert_after(
        CONFIG,
        '    "magic/extended-magic-access.md",',
        ['    "magic/magic-access-routes.md",'],
    )
    return changed


def patch_indexes_and_guides() -> int:
    changed = 0
    changed += insert_after(
        DATA_INDEX,
        "- [国家別拡張Magic Access](extended-magic-access/index.md)",
        ["- [国家別Magic Access到達経路](magic-access-routes/index.md)"],
    )
    changed += insert_after(
        MAGE_ACCESS,
        "- [国家別拡張Magic Access](extended-magic-access/index.md)",
        ["- [国家別Magic Access到達経路](magic-access-routes/index.md)"],
    )
    changed += insert_after(
        SITE_SEARCH_INDEX,
        "- [国家別拡張Magic Access](../extended-magic-access/index.md)",
        ["- [国家別Magic Access到達経路](../magic-access-routes/index.md)"],
    )
    changed += insert_after(
        EXTENDED_INDEX,
        "- [データ品質・境界](data-quality.md)",
        ["- [Magic Access到達経路](../magic-access-routes/index.md)"],
    )
    changed += insert_after(
        BOOSTING,
        "- [Communion](communions.md)",
        ["- [Magic Access到達経路](magic-access-routes.md)"],
    )
    changed += insert_after(
        COMMUNIONS,
        "- [Magic Path Boosting](boosting.md)",
        ["- [Magic Access到達経路](magic-access-routes.md)"],
    )
    changed += insert_after(
        EXTENDED_GUIDE,
        "- [Communion・Sabbath](communions.md)",
        ["- [Magic Access到達経路](magic-access-routes.md)"],
    )
    return changed


def patch_nation_pages() -> dict[str, int]:
    counts = {"recruit": 0, "site_search": 0, "extended": 0}
    for nation in nations():
        directory = str(nation["dir"])
        slug = str(nation["slug"])
        route_link = f"[Magic Access経路](../../magic-access-routes/{directory}/{slug}.md)"

        recruit = RECRUIT_ROOT / directory / f"{slug}.md"
        recruit_anchor = (
            f"[拡張Magic Access]"
            f"(../../extended-magic-access/{directory}/{slug}.md)"
        )
        counts["recruit"] += append_inline(
            recruit,
            recruit_anchor,
            f" · {route_link}",
        )

        site = SITE_SEARCH_ROOT / directory / f"{slug}.md"
        site_anchor = (
            f"[拡張Magic Access]"
            f"(../../extended-magic-access/{directory}/{slug}.md)"
        )
        counts["site_search"] += append_inline(
            site,
            site_anchor,
            f" · {route_link}",
        )

        extended = EXTENDED_ROOT / directory / f"{slug}.md"
        extended_anchor = (
            f"[Site Search能力]"
            f"(../../site-search/{directory}/{slug}.md)"
        )
        counts["extended"] += append_inline(
            extended,
            extended_anchor,
            f" · {route_link}",
        )
    return counts


def main() -> None:
    generator.main()
    navigation = patch_navigation()
    indexes = patch_indexes_and_guides()
    nation_counts = patch_nation_pages()
    print(f"patched_navigation: {navigation}")
    print(f"patched_indexes_guides: {indexes}")
    for key, value in nation_counts.items():
        print(f"patched_{key}_pages: {value}")


if __name__ == "__main__":
    main()
