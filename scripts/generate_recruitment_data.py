#!/usr/bin/env python3
"""Generate Dominions 6 nation recruit, loadout, and mage-access pages.

Source: a pinned Dominions 6.35 snapshot from larzm42/dom6inspector.
Generated pages are factual indexes; strategy remains in docs/nations/.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

from recruitment_loadouts import (
    equipment_indexes,
    equipment_table,
    validate_equipment_refs,
)

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data/nations.tsv"
OUT = ROOT / "docs/data/recruitment"
MAGE_OUT = ROOT / "docs/data/mage-access.md"
COMMIT = "cfac4311bc0b58053b8dead7bffbc036ba9bd5dc"
BASE = f"https://raw.githubusercontent.com/larzm42/dom6inspector/{COMMIT}/gamedata"
CACHE = ROOT / ".cache/dom6inspector" / COMMIT
FILES = (
    "BaseU.csv",
    "fort_troop_types_by_nation.csv",
    "fort_leader_types_by_nation.csv",
    "nonfort_troop_types_by_nation.csv",
    "nonfort_leader_types_by_nation.csv",
    "coast_troop_types_by_nation.csv",
    "coast_leader_types_by_nation.csv",
    "weapons.csv",
    "effects_weapons.csv",
    "effects_info.csv",
    "special_damage_types.csv",
    "attributes_by_weapon.csv",
    "attribute_keys.csv",
    "armors.csv",
    "protections_by_armor.csv",
    "attributes_by_armor.csv",
)
ERAS = {
    "1": ("EA", "ea", "Early Age"),
    "2": ("MA", "ma", "Middle Age"),
    "3": ("LA", "la", "Late Age"),
}
BY_CODE = {value[0]: value for value in ERAS.values()}
PATHS = "FAWESDNGBH"
MASKS = (
    (128, "F"),
    (256, "A"),
    (512, "W"),
    (1024, "E"),
    (2048, "S"),
    (4096, "D"),
    (8192, "N"),
    (16384, "G"),
    (32768, "B"),
    (65536, "H"),
)


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char)).lower()
    value = re.sub(r"['’]", "", value.replace("&", " and "))
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def esc(value: object) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def num(row: dict[str, str], key: str, default: int = 0) -> int:
    try:
        return int(float(row.get(key) or default))
    except (TypeError, ValueError):
        return default


def yes(row: dict[str, str], key: str) -> bool:
    return row.get(key) not in (None, "", "0", "0.0")


def tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def source(name: str, refresh: bool, offline: bool) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / name
    if path.exists() and path.stat().st_size and not refresh:
        return path
    if offline:
        raise FileNotFoundError(f"offline cache missing: {path}")

    request = urllib.request.Request(
        f"{BASE}/{name}", headers={"User-Agent": "dominions6-jp-wiki/1.0"}
    )
    error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                data = response.read()
            if not data:
                raise RuntimeError("empty download")
            path.write_bytes(data)
            return path
        except (urllib.error.URLError, TimeoutError, RuntimeError) as exc:
            error = exc
            time.sleep(2**attempt)
    raise RuntimeError(f"download failed: {name}: {error}")


def nations() -> list[dict[str, object]]:
    rows = tsv(CATALOG)
    out: list[dict[str, object]] = []
    for row in rows:
        raw = row["era"].strip()
        code, directory, title = ERAS.get(raw, BY_CODE.get(raw, (None, None, None)))
        if not code:
            raise ValueError(f"unknown era: {raw}")
        out.append(
            {
                **row,
                "id": int(row["id"]),
                "code": code,
                "dir": directory,
                "era_name": title,
                "slug": slugify(row["name"]),
            }
        )
    if len({row["id"] for row in out}) != len(out):
        raise ValueError("duplicate nation id")
    if len({(row["code"], row["slug"]) for row in out}) != len(out):
        raise ValueError("duplicate nation slug")
    return out


def unit_data(path: Path) -> dict[int, dict[str, str]]:
    data = {int(row["id"]): row for row in tsv(path) if row.get("id")}
    if len(data) < 4000:
        raise ValueError(f"BaseU incomplete: {len(data)}")
    return data


def mapping(path: Path):
    out = defaultdict(list)
    for row in tsv(path):
        if row.get("monster_number") and row.get("nation_number"):
            out[int(row["nation_number"])].append(int(row["monster_number"]))
    return out


def fixed(row: dict[str, str]) -> dict[str, int]:
    return {path: num(row, path) for path in PATHS if num(row, path) > 0}


def randoms(row: dict[str, str]) -> list[tuple[int, int, int, str]]:
    out: list[tuple[int, int, int, str]] = []
    for index in range(1, 7):
        mask = num(row, f"mask{index}")
        pool = "".join(path for bit, path in MASKS if mask & bit)
        if pool:
            out.append(
                (
                    max(1, num(row, f"nbr{index}", 1)),
                    num(row, f"rand{index}", 100) or 100,
                    max(1, num(row, f"link{index}", 1)),
                    pool,
                )
            )
    return out


def fixed_text(row: dict[str, str]) -> str:
    return " ".join(f"{path}{level}" for path, level in fixed(row).items()) or "—"


def random_text(row: dict[str, str]) -> str:
    return (
        "; ".join(
            f"{count}×{chance}% +{level} [{'/'.join(pool)}]"
            for count, chance, level, pool in randoms(row)
        )
        or "—"
    )


def cap(row: dict[str, str]) -> bool:
    return yes(row, "capitalhome")


def mage(row: dict[str, str]) -> bool:
    return bool(fixed(row) or randoms(row) or yes(row, "researchbonus"))


def tags(row: dict[str, str]) -> list[str]:
    simple = (
        ("holy", "Sacred"),
        ("mounted", "Mounted"),
        ("flying", "Flying"),
        ("spy", "Spy"),
        ("assassin", "Assassin"),
        ("heal", "Healer"),
        ("mastersmith", "Master Smith"),
        ("undead", "Undead"),
        ("demon", "Demon"),
        ("magicbeing", "Magic Being"),
        ("inanimate", "Lifeless"),
        ("animal", "Animal"),
        ("aquatic", "Aquatic"),
        ("amphibian", "Amphibious"),
        ("pooramphibian", "Poor Amphibian"),
        ("glamour", "Glamour"),
        ("spellsinger", "Spellsinger"),
    )
    out = [label for key, label in simple if yes(row, key)]
    if num(row, "mor") == 50 and "Mindless" not in out:
        out.append("Mindless")
    valued = (
        ("stealthy", "Stealth"),
        ("forgebonus", "Forge"),
        ("douse", "Blood Search"),
        ("formationfighter", "Formation Fighter"),
        ("bodyguard", "Bodyguard"),
        ("patrolbonus", "Patrol"),
        ("siegebonus", "Siege"),
        ("castledef", "Castle Def"),
        ("resources", "Resources"),
        ("supplybonus", "Supply"),
        ("reclimit", "Rec limit"),
    )
    for key, label in valued:
        if yes(row, key):
            out.append(f"{label} {num(row, key):+d}")
    if num(row, "rt") == 2 or yes(row, "slowrec"):
        out.append("Slow to recruit")
    return out[:8]


def rows(ids: list[int], units: dict[int, dict[str, str]]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    seen: set[int] = set()
    for unit_id in ids:
        if unit_id in seen:
            continue
        seen.add(unit_id)
        if unit_id not in units:
            raise KeyError(f"mapped unit {unit_id} missing from BaseU")
        out.append(units[unit_id])
    return out


def val(row: dict[str, str], key: str) -> str:
    return row.get(key) or "—"


def troop_table(items: list[dict[str, str]]) -> str:
    if not items:
        return "該当データなし。\n"
    out = [
        "| Unit | ID | Size | HP | Prot | MR | Mor | Str | Att | Def | 主な属性 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in items:
        out.append(
            f"| {esc(row.get('name', '(unnamed)'))} | {row['id']} | "
            f"{val(row, 'size')} | {val(row, 'hp')} | {val(row, 'prot')} | "
            f"{val(row, 'mr')} | {val(row, 'mor')} | {val(row, 'str')} | "
            f"{val(row, 'att')} | {val(row, 'def')} | "
            f"{esc(', '.join(tags(row)) or '—')} |"
        )
    return "\n".join(out) + "\n"


def commander_table(items: list[dict[str, str]]) -> str:
    if not items:
        return "該当データなし。\n"
    out = [
        "| Commander | ID | Leadership N/U/M | Guaranteed | Random | 主な属性 |",
        "|---|---:|---|---|---|---|",
    ]
    for row in items:
        leadership = (
            f"{val(row, 'leader')}/{val(row, 'undeadleader')}/{val(row, 'magicleader')}"
        )
        out.append(
            f"| {esc(row.get('name', '(unnamed)'))} | {row['id']} | {leadership} | "
            f"{esc(fixed_text(row))} | {esc(random_text(row))} | "
            f"{esc(', '.join(tags(row)) or '—')} |"
        )
    return "\n".join(out) + "\n"


def section(
    title: str,
    troop_ids: list[int],
    leader_ids: list[int],
    units: dict[int, dict[str, str]],
    equipment: tuple[dict[int, dict[str, object]], dict[int, dict[str, object]]],
    split: bool = False,
) -> str:
    troops = rows(troop_ids, units)
    leaders = rows(leader_ids, units)
    out = [f"## {title}", ""]
    if split:
        categories = (
            ("Recruit-anywhere troops", [row for row in troops if not cap(row)], troop_table),
            ("Capital-only troops", [row for row in troops if cap(row)], troop_table),
            (
                "Recruit-anywhere commanders",
                [row for row in leaders if not cap(row)],
                commander_table,
            ),
            (
                "Capital-only commanders",
                [row for row in leaders if cap(row)],
                commander_table,
            ),
        )
        for heading, items, renderer in categories:
            out.extend([f"### {heading}", "", renderer(items)])
    else:
        out.extend(
            [
                "### Troops",
                "",
                troop_table(troops),
                "### Commanders",
                "",
                commander_table(leaders),
            ]
        )

    all_items = troops + leaders
    if all_items:
        weapons, armors = equipment
        out.extend(
            [
                "### 装備・Mount",
                "",
                equipment_table(all_items, units, weapons, armors),
            ]
        )
    return "\n".join(out).rstrip() + "\n"


def mage_summary(items: list[dict[str, str]]) -> str:
    out: list[str] = []
    for row in items:
        if not mage(row):
            continue
        text = f"{row.get('name', '(unnamed)')}: {fixed_text(row)}"
        if random_text(row) != "—":
            text += f"; {random_text(row)}"
        out.append(text)
    return " / ".join(out) or "—"


def nation_page(
    nation: dict[str, object],
    units: dict[int, dict[str, str]],
    maps,
    equipment: tuple[dict[int, dict[str, object]], dict[int, dict[str, object]]],
) -> str:
    nation_id = int(nation["id"])
    fort_troops = maps["ft"].get(nation_id, [])
    fort_leaders_ids = maps["fl"].get(nation_id, [])
    nonfort_troops = maps["nt"].get(nation_id, [])
    nonfort_leaders = maps["nl"].get(nation_id, [])
    coast_troops = maps["ct"].get(nation_id, [])
    coast_leaders = maps["cl"].get(nation_id, [])

    fort_leaders = rows(fort_leaders_ids, units)
    all_leaders = rows(fort_leaders_ids + nonfort_leaders + coast_leaders, units)
    any_fort = [row for row in fort_leaders if not cap(row)]
    capital = [row for row in fort_leaders if cap(row)]

    content = f'''---
title: "{nation['code']} {nation['name']} Recruitデータ"
status: generated
verified_version: "6.35"
nation_id: {nation_id}
generated_from: "dom6inspector {COMMIT}"
---

# {nation['code']} {nation['name']} — Recruitデータ

> **{nation['epithet']}**

[国家攻略ページへ戻る](../../../nations/{nation['dir']}/{nation['slug']}.md) · [Unit装備・Mountの読み方](../../unit-loadouts.md) · [Combat data](../../combat/index.md)

!!! info "自動生成データ"
    Dominions 6.35対応の固定スナップショットから生成した「何を雇え、何を装備しているか」の索引です。Unitの評価・生産比率・研究方針は国家攻略で扱います。

## 概要

| 項目 | 内容 |
|---|---|
| Era | {nation['era_name']}（{nation['code']}） |
| Nation | {nation['name']} |
| Epithet | {nation['epithet']} |
| Nation ID | {nation_id} |
| Any-fort magic | {esc(mage_summary(any_fort))} |
| Capital magic | {esc(mage_summary(capital))} |
| 全Recruit commander数 | {len(all_leaders)} |

### 表の読み方

- **Leadership N/U/M**: 通常 / Undead / Magic leadership。
- **Guaranteed**: 固定Magic Path。
- **Random**: `1×20% +1 [F/A/W/E]`は、20%で候補Pathの一つを1得るRandom pickを1回持つ。
- **Capital-only**: `capitalhome`属性による分類。
- **Weapons / Armor**: Unitの`wpn1..7`、`armor1..4`をWeapon / Armor recordへ結合した基礎値。
- **Mount**: Riderとは別Unit record。MountのHP・Protection・攻撃・防具を分離して表示する。
- Gold costは自動計算・Mount・Holy・Slow recruitment等の補正が複雑なため表示しない。

'''
    content += section(
        "Fort recruitment",
        fort_troops,
        fort_leaders_ids,
        units,
        equipment,
        True,
    )
    if nonfort_troops or nonfort_leaders:
        content += "\n" + section(
            "Fort不要・地形・外国Recruit",
            nonfort_troops,
            nonfort_leaders,
            units,
            equipment,
        )
    if coast_troops or coast_leaders:
        content += "\n" + section(
            "Coastal recruitment",
            coast_troops,
            coast_leaders,
            units,
            equipment,
        )

    return content + f'''\n## データ上の注意

- Weapon表は基礎Damage、Attack / Precision、Length / Range、Damage type、AP / AN等を表示する。UnitのStrengthやBless・Buffを反映した最終Damageではない。
- Armor表は装備単体のProtection・Parry・Encumbranceを表示する。UnitのNatural Protectionや魔法Buffとは別。
- RiderとMountは別のHP・Stats・攻撃を持つ。Mount喪失後の徒歩形態や条件付き武器はゲーム内表示も確認する。
- 同じWeapon IDが複数Slotにある場合は`×2`のように表示するが、実際の攻撃順、二刀流Penalty、条件付き攻撃は別処理を持つ。
- Hero、Event、Freespawn、国家固有召喚、Magic Site限定Unitは別扱い。
- 地形・建物・季節・Plane・Dominion条件で実際の候補が制限される場合がある。
- 抽出値とゲームUI上の最終Cost、形態変化、Mount込み表示が一致しない場合がある。

## 出典

- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- Data snapshot: `{COMMIT}`（Dominions 6.35）
'''


def fixed_max(items: list[dict[str, str]]) -> str:
    top = {path: 0 for path in PATHS}
    for row in items:
        for path, level in fixed(row).items():
            top[path] = max(top[path], level)
    return " ".join(f"{path}{level}" for path, level in top.items() if level) or "—"


def random_max(items: list[dict[str, str]]) -> str:
    out: list[str] = []
    for row in items:
        for count, chance, level, pool in randoms(row):
            text = f"{count}×{chance}% +{level} [{'/'.join(pool)}]"
            if text not in out:
                out.append(text)
    return "; ".join(out) or "—"


def write_indexes(ns, units, maps) -> None:
    index_lines = [
        "---",
        'title: "国家Recruitデータ"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {COMMIT}"',
        "---",
        "",
        "# 国家Recruitデータ",
        "",
        "全vanilla国家のFort / Capital / Fort不要 / Coastal Recruitと、UnitのWeapon・Armor・Mountを自動生成した索引です。",
        "",
        "- [Mage access早見表](../mage-access.md)",
        "- [Unit装備・Mountの読み方](../unit-loadouts.md)",
        "- [Combat data索引](../combat/index.md)",
        "- [国家攻略一覧](../../nations/index.md)",
        "",
    ]
    mage_lines = [
        "---",
        'title: "Mage access早見表"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {COMMIT}"',
        "---",
        "",
        "# Mage access早見表",
        "",
        "Recruit commanderの固定PathとRandom poolを比較します。Booster、Hero、Summon、Site Mage、Communionは含みません。",
        "",
        "- [国家Recruitデータ](recruitment/index.md)",
        "- [Magic Path Boosting](../magic/boosting.md)",
        "",
    ]

    for era in ("EA", "MA", "LA"):
        era_nations = [nation for nation in ns if nation["code"] == era]
        index_lines.extend(
            [
                f"## {BY_CODE[era][2]}（{era}）",
                "",
                "| ID | Nation | Epithet | Recruit data | 攻略 |",
                "|---:|---|---|---|---|",
            ]
        )
        mage_lines.extend(
            [
                f"## {era}",
                "",
                "| Nation | Any-fort fixed max | Any-fort random | Capital fixed max | Capital random |",
                "|---|---|---|---|---|",
            ]
        )
        for nation in era_nations:
            index_lines.append(
                f"| {nation['id']} | {nation['name']} | {nation['epithet']} | "
                f"[表示]({nation['dir']}/{nation['slug']}.md) | "
                f"[攻略](../../nations/{nation['dir']}/{nation['slug']}.md) |"
            )
            leaders = rows(maps["fl"].get(nation["id"], []), units)
            any_fort = [row for row in leaders if not cap(row) and mage(row)]
            capital = [row for row in leaders if cap(row) and mage(row)]
            mage_lines.append(
                f"| [{nation['name']}](recruitment/{nation['dir']}/{nation['slug']}.md) | "
                f"{esc(fixed_max(any_fort))} | {esc(random_max(any_fort))} | "
                f"{esc(fixed_max(capital))} | {esc(random_max(capital))} |"
            )
        index_lines.append("")
        mage_lines.append("")

    index_lines.extend(
        [
            "## 更新方針",
            "",
            f"生成元: `{COMMIT}`。Patch更新時はCommitを変更し、Recruit、装備参照、Mount参照、Magic accessの差分を確認します。",
            "",
        ]
    )
    mage_lines.extend(
        [
            "## 読み方",
            "",
            "`F2 E1`は、その区分のCommander群に固定F2と固定E1へのアクセスがあることを示します。同じ一体が両方を持つとは限りません。",
            "",
        ]
    )
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.md").write_text("\n".join(index_lines), encoding="utf-8")
    MAGE_OUT.parent.mkdir(parents=True, exist_ok=True)
    MAGE_OUT.write_text("\n".join(mage_lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    paths = {name: source(name, args.refresh, args.offline) for name in FILES}
    nation_rows = nations()
    units = unit_data(paths["BaseU.csv"])
    weapons, armors = equipment_indexes(paths)
    if len(weapons) < 500:
        raise ValueError(f"weapon data appears incomplete: {len(weapons)}")
    if len(armors) < 100:
        raise ValueError(f"armor data appears incomplete: {len(armors)}")

    maps = {
        "ft": mapping(paths["fort_troop_types_by_nation.csv"]),
        "fl": mapping(paths["fort_leader_types_by_nation.csv"]),
        "nt": mapping(paths["nonfort_troop_types_by_nation.csv"]),
        "nl": mapping(paths["nonfort_leader_types_by_nation.csv"]),
        "ct": mapping(paths["coast_troop_types_by_nation.csv"]),
        "cl": mapping(paths["coast_leader_types_by_nation.csv"]),
    }
    unknown_nations = sorted(
        set().union(*(set(mapping_rows) for mapping_rows in maps.values()))
        - {int(nation["id"]) for nation in nation_rows}
    )
    if unknown_nations:
        print(
            "warning: unmapped catalog nation IDs: "
            + ", ".join(map(str, unknown_nations)),
            file=sys.stderr,
        )

    equipment = (weapons, armors)
    for nation in nation_rows:
        path = OUT / str(nation["dir"]) / f"{nation['slug']}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(nation_page(nation, units, maps, equipment), encoding="utf-8")
    write_indexes(nation_rows, units, maps)

    total = sum(len(value) for mapped in maps.values() for value in mapped.values())
    validation = validate_equipment_refs(units, weapons, armors)
    print(f"source commit: {COMMIT}")
    print(f"units loaded: {len(units)}")
    print(f"nations generated: {len(nation_rows)}")
    print(f"mapped recruitment entries: {total}")
    print(f"weapon records available: {len(weapons)}")
    print(f"armor records available: {len(armors)}")
    print(f"units with weapons: {validation['units_with_weapons']}")
    print(f"units with armor: {validation['units_with_armor']}")
    print(f"mounted unit records: {validation['mounted_units']}")
    print(f"unique weapon refs: {validation['weapon_refs']}")
    print(f"unique armor refs: {validation['armor_refs']}")
    print(f"unique mount refs: {validation['mount_refs']}")
    for key, label in (
        ("missing_weapons", "unresolved weapon IDs"),
        ("missing_armors", "unresolved armor IDs"),
        ("missing_mounts", "unresolved mount unit IDs"),
    ):
        missing = validation[key]
        if missing:
            print(f"warning: {label}: {', '.join(map(str, missing))}", file=sys.stderr)


if __name__ == "__main__":
    main()
