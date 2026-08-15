#!/usr/bin/env python3
"""Run Magic Access route generation and integrate the generated pages safely.

The wrapper keeps the large generator focused on data calculations while this
file applies conservative corrections and idempotent cross-links after all
upstream generated pages exist.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import generate_magic_access_routes as generator
from generate_recruitment_data import nations, num, tsv

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "zensical.toml"
DATA_INDEX = ROOT / "docs" / "data" / "index.md"
MAGE_ACCESS = ROOT / "docs" / "data" / "mage-access.md"
EXTENDED_INDEX = ROOT / "docs" / "data" / "extended-magic-access" / "index.md"
SITE_SEARCH_INDEX = ROOT / "docs" / "data" / "site-search" / "index.md"
BOOSTING = ROOT / "docs" / "magic" / "boosting.md"
COMMUNIONS = ROOT / "docs" / "magic" / "communions.md"
EXTENDED_GUIDE = ROOT / "docs" / "magic" / "extended-magic-access.md"
ROUTE_GUIDE = ROOT / "docs" / "magic" / "magic-access-routes.md"
RECRUIT_ROOT = ROOT / "docs" / "data" / "recruitment"
SITE_SEARCH_ROOT = ROOT / "docs" / "data" / "site-search"
EXTENDED_ROOT = ROOT / "docs" / "data" / "extended-magic-access"

_ALL_MATRIX_ITEMS: list[dict[str, object]] = []


def _conservative_add_levels(
    base: dict[str, int],
    items,
) -> dict[str, int]:
    """A normal path booster raises an existing path; it does not create F0→F1."""
    levels = dict(base)
    native_paths = {path for path, level in base.items() if level > 0}
    for item in items:
        for path, bonus in item["boosts"].items():
            if path in native_paths:
                levels[path] = levels.get(path, 0) + int(bonus)
    return {path: level for path, level in levels.items() if level > 0}


def _matrix_record(row: dict[str, str]) -> dict[str, object]:
    item_type = (row.get("type") or "").strip()
    const = num(row, "constlevel")
    boosts = generator.path_boosts(row)
    return {
        "id": num(row, "id"),
        "name": (row.get("name") or f"Item {num(row, 'id')}").strip(),
        "row": row,
        "type": item_type,
        "type_title": generator.ITEM_TYPES.get(
            item_type, (item_type or "Unknown", "misc")
        )[0],
        "type_slug": generator.ITEM_TYPES.get(item_type, ("Unknown", "misc"))[1],
        "const": const,
        "construction": "Unforgeable" if const == 12 else f"Construction {const}",
        "requirements": generator.path_requirements(row),
        "requirement_text": generator.item_requirement(row),
        "cost": generator.item_gem_cost(row),
        "boosts": boosts,
        "boost_text": generator.level_text(boosts),
        "restrictions": generator.restriction_ids(row),
        "slot_usage": generator.slot_usage(item_type),
        "slot": "/".join(generator.slot_usage(item_type)) or "special",
        "standard_slot": "barding" not in generator.slot_usage(item_type),
        "matrix": True,
    }


def _install_data_corrections() -> None:
    original_load_boosters = generator.load_boosters
    original_profile = generator.profile_for_nation
    original_communion_page = generator.communion_page

    def load_boosters(data):
        global _ALL_MATRIX_ITEMS
        forgeable, unforgeable = original_load_boosters(data)
        matrices: list[dict[str, object]] = []
        for row in tsv(data["paths"]["BaseI.csv"]):
            name = (row.get("name") or "").strip()
            item_type = (row.get("type") or "").strip()
            if (
                not name
                or item_type not in generator.ITEM_TYPES
                or num(row, "constlevel") <= 0
            ):
                continue
            if num(row, "comslave") or "matrix" in name.lower():
                matrices.append(_matrix_record(row))
        matrices.sort(
            key=lambda item: (
                int(item["const"]),
                str(item["type_title"]),
                str(item["name"]),
                int(item["id"]),
            )
        )
        _ALL_MATRIX_ITEMS = matrices
        return forgeable, unforgeable

    def profile_for_nation(nation, data, boosters, unforgeable, summon_groups):
        profile, stats = original_profile(
            nation,
            data,
            boosters,
            unforgeable,
            summon_groups,
        )
        nation_id = int(nation["id"])
        profile["matrix_items"] = [
            item
            for item in _ALL_MATRIX_ITEMS
            if not item["restrictions"] or nation_id in item["restrictions"]
        ]
        return profile, stats

    def communion_page(profiles, _matrix_items):
        return original_communion_page(profiles, _ALL_MATRIX_ITEMS)

    generator.add_levels = _conservative_add_levels
    generator.load_boosters = load_boosters
    generator.profile_for_nation = profile_for_nation
    generator.communion_page = communion_page


def insert_after(path: Path, anchor: str, additions: list[str]) -> bool:
    if not path.exists():
        raise FileNotFoundError(f"required page missing: {path}")
    text = path.read_text(encoding="utf-8")
    if additions and additions[0] in text:
        return False
    if anchor not in text:
        raise ValueError(f"anchor not found in {path}: {anchor!r}")
    text = text.replace(anchor, anchor + "\n" + "\n".join(additions), 1)
    path.write_text(text, encoding="utf-8")
    return True


def insert_after_any(path: Path, anchors: list[str], additions: list[str]) -> bool:
    if not path.exists():
        raise FileNotFoundError(f"required page missing: {path}")
    text = path.read_text(encoding="utf-8")
    if additions and additions[0] in text:
        return False
    for anchor in anchors:
        if anchor in text:
            text = text.replace(anchor, anchor + "\n" + "\n".join(additions), 1)
            path.write_text(text, encoding="utf-8")
            return True
    raise ValueError(f"none of the anchors found in {path}: {anchors!r}")


def replace_once(path: Path, old: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return False
    if old not in text:
        raise ValueError(f"replacement anchor missing in {path}: {old!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    return True


def patch_guide_accuracy() -> bool:
    old = (
        "Masterが元から持つ各Magic Pathへbonusを加えます。Holyも、Masterが通常Mageとして非Holy Pathを持つ場合には対象へ含めます。純粋なPriestへMatrixだけを装備させたケースをHoly boostとしては計算しません。"
    )
    new = (
        "自動Profileでは、Masterが元から持つArcane Pathだけへbonusを加えます。Holy / Priest levelはCommunion・Sabbathの自動到達値へ加算しません。Matrixを使う非Astral Masterも、装備とFatigueの別検証が必要です。"
    )
    return replace_once(ROUTE_GUIDE, old, new)


def patch_navigation() -> tuple[bool, bool]:
    data_changed = insert_after_any(
        CONFIG,
        [
            '    "data/extended-magic-access/data-quality.md",',
            '    "data/unit-loadouts.md",',
        ],
        [
            '    "data/magic-access-routes/index.md",',
            '    "data/magic-access-routes/booster-routes.md",',
            '    "data/magic-access-routes/summon-chains.md",',
            '    "data/magic-access-routes/communion-sabbath.md",',
            '    "data/magic-access-routes/empowerment-gaps.md",',
            '    "data/magic-access-routes/data-quality.md",',
        ],
    )
    guide_changed = insert_after_any(
        CONFIG,
        [
            '    "magic/extended-magic-access.md",',
            '    "magic/communions.md",',
        ],
        ['    "magic/magic-access-routes.md",'],
    )
    return data_changed, guide_changed


def patch_indexes_and_guides() -> int:
    changed = 0
    changed += insert_after_any(
        DATA_INDEX,
        [
            "- [国家別拡張Magic Access](extended-magic-access/index.md)",
            "- [国家別Site Search能力](site-search/index.md)",
            "- [Mage access早見表](mage-access.md)",
        ],
        [
            "- [国家別Magic Access到達経路](magic-access-routes/index.md)",
            "- [Booster route](magic-access-routes/booster-routes.md)",
            "- [再帰Mage summon chain](magic-access-routes/summon-chains.md)",
            "- [Communion・Sabbath battle reach](magic-access-routes/communion-sabbath.md)",
            "- [Empowerment gap](magic-access-routes/empowerment-gaps.md)",
        ],
    )
    changed += insert_after_any(
        MAGE_ACCESS,
        [
            "- [国家別拡張Magic Access](extended-magic-access/index.md)",
            "- [国家別Site Search能力](site-search/index.md)",
            "- [国家Recruitデータ](recruitment/index.md)",
        ],
        ["- [国家別Magic Access到達経路](magic-access-routes/index.md)"],
    )
    changed += insert_after_any(
        EXTENDED_INDEX,
        [
            "- [拡張Magic Accessの読み方](../../magic/extended-magic-access.md)",
            "- [Path gain比較](path-gains.md)",
        ],
        ["- [Magic Access到達経路](../magic-access-routes/index.md)"],
    )
    changed += insert_after_any(
        SITE_SEARCH_INDEX,
        [
            "- [国家別拡張Magic Access](../extended-magic-access/index.md)",
            "- [Site Search完全ガイド](../../magic/site-search.md)",
        ],
        ["- [Magic Access到達経路](../magic-access-routes/index.md)"],
    )
    changed += insert_after_any(
        BOOSTING,
        ["- [Communion](communions.md)", "- [魔法の基本](index.md)"],
        ["- [Magic Access到達経路](magic-access-routes.md)"],
    )
    changed += insert_after_any(
        COMMUNIONS,
        ["- [Magic Path Boosting](boosting.md)", "- [魔法の基本](index.md)"],
        ["- [Magic Access到達経路](magic-access-routes.md)"],
    )
    changed += insert_after_any(
        EXTENDED_GUIDE,
        [
            "- [国家別拡張Magic Access](../data/extended-magic-access/index.md)",
            "- [国家別Mage access](../data/mage-access.md)",
            "- [Communion・Sabbath](communions.md)",
        ],
        ["- [Magic Access到達経路](magic-access-routes.md)"],
    )
    return changed


def append_inline_after_any(path: Path, anchors: list[str], addition: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if addition.strip() in text:
        return False
    for anchor in anchors:
        if anchor in text:
            path.write_text(text.replace(anchor, anchor + addition, 1), encoding="utf-8")
            return True
    raise ValueError(f"none of the inline anchors found in {path}: {anchors!r}")


def patch_detail_pages() -> dict[str, int]:
    counts = {"recruit": 0, "site_search": 0, "extended": 0}
    for nation in nations():
        directory = str(nation["dir"])
        slug = str(nation["slug"])
        route_link = f"[Magic Access route](../../magic-access-routes/{directory}/{slug}.md)"

        recruit = RECRUIT_ROOT / directory / f"{slug}.md"
        counts["recruit"] += append_inline_after_any(
            recruit,
            [
                f"[拡張Magic Access](../../extended-magic-access/{directory}/{slug}.md)",
                f"[Site Search能力](../../site-search/{directory}/{slug}.md)",
            ],
            f" · {route_link}",
        )

        site_search = SITE_SEARCH_ROOT / directory / f"{slug}.md"
        counts["site_search"] += append_inline_after_any(
            site_search,
            [
                f"[拡張Magic Access](../../extended-magic-access/{directory}/{slug}.md)",
                f"[Recruitデータ](../../recruitment/{directory}/{slug}.md)",
            ],
            f" · {route_link}",
        )

        extended = EXTENDED_ROOT / directory / f"{slug}.md"
        counts["extended"] += append_inline_after_any(
            extended,
            [
                f"[Site Search能力](../../site-search/{directory}/{slug}.md)",
                f"[通常Recruit](../../recruitment/{directory}/{slug}.md)",
            ],
            f" · {route_link}",
        )
    return counts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    _install_data_corrections()
    forwarded = [sys.argv[0]]
    if args.refresh:
        forwarded.append("--refresh")
    if args.offline:
        forwarded.append("--offline")
    old_argv = sys.argv
    try:
        sys.argv = forwarded
        generator.main()
    finally:
        sys.argv = old_argv

    accuracy = patch_guide_accuracy()
    nav_data, nav_guide = patch_navigation()
    index_changes = patch_indexes_and_guides()
    detail_counts = patch_detail_pages()

    print(f"guide_accuracy_patched: {int(accuracy)}")
    print(f"data_navigation_patched: {int(nav_data)}")
    print(f"guide_navigation_patched: {int(nav_guide)}")
    print(f"index_guide_pages_patched: {index_changes}")
    for key, value in detail_counts.items():
        print(f"{key}_detail_pages_patched: {value}")
    print(f"matrix_items_detected: {len(_ALL_MATRIX_ITEMS)}")


if __name__ == "__main__":
    main()
