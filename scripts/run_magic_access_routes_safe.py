#!/usr/bin/env python3
"""Run Magic Access route generation with zero-native-mage support.

Some nations, notably LA Lemuria, do not expose a normal recruitable mage
roster through the standard nation recruitment mappings. That is a valid game
state, not incomplete data. This wrapper keeps the strict global integrity
checks while allowing such nations to receive an explicit empty-native profile.
"""
from __future__ import annotations

import generate_magic_access_routes as generator
import run_magic_access_routes as runner


NO_NATIVE_NAMES: list[str] = []
ORIGINAL_QUALITY_PAGE = generator.quality_page


def safe_validate(profiles, boosters, summon_groups, stats) -> None:
    if len(profiles) != 103:
        raise ValueError(f"nation profile count mismatch: {len(profiles)}")
    if len(boosters) < 10:
        raise ValueError(f"booster set appears incomplete: {len(boosters)}")
    if len(summon_groups) < 50:
        raise ValueError(f"summon group set appears incomplete: {len(summon_groups)}")
    if stats["route_states"] <= 0 or stats["loadouts"] <= 0:
        raise ValueError("booster route search produced no states")
    if stats["fixed_summon_relations"] <= 0:
        raise ValueError("recursive summon search produced no relations")

    NO_NATIVE_NAMES.clear()
    for profile in profiles:
        if profile["candidates"]:
            continue
        nation = profile["nation"]
        NO_NATIVE_NAMES.append(f"{nation['code']} {nation['name']}")

    stats["nations_without_native_mages"] = len(NO_NATIVE_NAMES)


def safe_quality_page(profiles, boosters, unforgeable, summon_groups, stats) -> str:
    text = ORIGINAL_QUALITY_PAGE(
        profiles,
        boosters,
        unforgeable,
        summon_groups,
        stats,
    )
    count_row = f"| Nation without native recruit Mage | {len(NO_NATIVE_NAMES)} |"
    anchor = f"| Nation profile | {len(profiles)} |"
    if count_row not in text and anchor in text:
        text = text.replace(anchor, anchor + "\n" + count_row, 1)

    section = [
        "## 通常Recruit Mageが0件の国家",
        "",
        "標準のFort / non-fort / coastal Commander mappingからMageを確認できない国家です。これはデータ欠落と断定せず、Native Pathを空としてProfileを生成します。Freespawn、国家内部処理、召喚、Pretender等は別Layerです。",
        "",
    ]
    if NO_NATIVE_NAMES:
        section.extend(f"- {name}" for name in NO_NATIVE_NAMES)
    else:
        section.append("- 該当なし")
    section.extend(["", ""])

    marker = "## 安全上の境界"
    block = "\n".join(section)
    if block not in text and marker in text:
        text = text.replace(marker, block + marker, 1)
    return text


def main() -> None:
    generator.validate = safe_validate
    generator.quality_page = safe_quality_page
    runner.main()
    print(f"nations_without_native_mages: {len(NO_NATIVE_NAMES)}")
    for name in NO_NATIVE_NAMES:
        print(f"native_mage_roster_empty: {name}")


if __name__ == "__main__":
    main()
