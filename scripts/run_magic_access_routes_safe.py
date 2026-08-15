#!/usr/bin/env python3
"""Run Magic Access route generation with conservative safety patches.

Some nations, notably LA Lemuria, do not expose a normal recruitable mage
roster through the standard nation recruitment mappings. That is a valid game
state, not incomplete data. The runner also replaces per-path theoretical
Random maxima with simultaneous feasible Random outcomes, keeps ordinary path
boosters on paths the bearer already possesses, and models valid Holy boosts
for Communion/Sabbath masters that are also mages.
"""
from __future__ import annotations

import generate_magic_access_routes as generator
import magic_access_booster_semantics
import magic_access_communion_semantics
import magic_access_route_safety
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


def correct_guide_accuracy() -> bool:
    """Keep the guide aligned with the actual Communion Holy-path rule."""
    path = runner.ROUTE_GUIDE
    text = path.read_text(encoding="utf-8")
    correct = (
        "自動Profileでは、Masterが通常MageとしてArcane Pathを少なくとも一つ持つ場合、元から持つHolyを含む既知Pathへbonusを加えます。純粋なPriestをMatrixだけでMaster化した場合はHoly boostへ数えません。"
    )
    if correct in text:
        return False
    candidates = (
        "Masterが元から持つ各Magic Pathへbonusを加えます。Holyも、Masterが通常Mageとして非Holy Pathを持つ場合には対象へ含めます。純粋なPriestへMatrixだけを装備させたケースをHoly boostとしては計算しません。",
        "自動Profileでは、Masterが元から持つArcane Pathだけへbonusを加えます。Holy / Priest levelはCommunion・Sabbathの自動到達値へ加算しません。Matrixを使う非Astral Masterも、装備とFatigueの別検証が必要です。",
    )
    for old in candidates:
        if old in text:
            path.write_text(text.replace(old, correct, 1), encoding="utf-8")
            return True
    raise ValueError("Communion Holy-path guide paragraph was not found")


def safe_quality_page(profiles, boosters, unforgeable, summon_groups, stats) -> str:
    text = ORIGINAL_QUALITY_PAGE(
        profiles,
        boosters,
        unforgeable,
        summon_groups,
        stats,
    )
    count_row = f"| Nation without native recruit Mage | {len(NO_NATIVE_NAMES)} |"
    random_row = "| Random crosspath feasibility | simultaneous outcome enumeration |"
    booster_row = "| Standard booster semantics | existing paths only |"
    communion_row = "| Communion breakpoints | 2/4/8/16/32/64 slaves = +1..+6 |"
    anchor = f"| Nation profile | {len(profiles)} |"
    if count_row not in text and anchor in text:
        text = text.replace(
            anchor,
            anchor
            + "\n"
            + count_row
            + "\n"
            + random_row
            + "\n"
            + booster_row
            + "\n"
            + communion_row,
            1,
        )

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
    section.extend(
        [
            "",
            "## Random crosspathの安全策",
            "",
            "Pathごとの理論最大を一体のMageへ合成しません。Booster Forgeと再帰召喚の複合Path要求は、各Random pickを一つのPathへ割り当てた同時成立可能な結果だけで判定します。",
            "",
            "## Boosterの安全策",
            "",
            "BaseIの通常Path bonusは、装備者が既に持つPathだけを上げるBoosterとして計算します。0から新Pathを作る経路には使わず、明示的なEmpower効果、召喚、Pretender、Site等を別Layerへ残します。",
            "",
            "## Communion / Sabbathの安全策",
            "",
            "Masterが通常Mageでもある場合は、元から持つHolyもPath bonusへ含めます。純粋なPriestをMatrixだけでMaster化したケースはHoly boostへ数えません。64 Slaveの+6まで表示します。",
            "",
            "",
        ]
    )

    marker = "## 安全上の境界"
    block = "\n".join(section)
    if block not in text and marker in text:
        text = text.replace(marker, block + marker, 1)
    return text


def main() -> None:
    magic_access_booster_semantics.install(generator)
    magic_access_communion_semantics.install(generator)
    magic_access_route_safety.install(generator)
    generator.validate = safe_validate
    generator.quality_page = safe_quality_page
    runner.patch_guide_accuracy = correct_guide_accuracy
    runner.main()
    print(f"nations_without_native_mages: {len(NO_NATIVE_NAMES)}")
    for name in NO_NATIVE_NAMES:
        print(f"native_mage_roster_empty: {name}")


if __name__ == "__main__":
    main()
