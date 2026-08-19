#!/usr/bin/env python3
"""Generate Magic Item weapon/armor/effect reverse indexes.

This supplements the BaseI-focused Magic Item indexes by joining Item records to
already-pinned Weapon / Armor combat data and by exposing explicit Item effect,
summoning, drawback, and equip-restriction fields.
"""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import generate_spell_item_data as item_core
from combat_data_armor import parse_armor_attributes, parse_armors
from combat_data_common import clean_label, num, source, tsv
from combat_data_weapons import parse_weapons

ITEM_OUT = item_core.ITEM_OUT
START = "<!-- item-effect-index:start -->"
END = "<!-- item-effect-index:end -->"

DIRECT_EFFECT_FIELDS = (
    ("spelleffect", "Spell effect"),
    ("startbattlespell", "Start battle spell"),
    ("autocombatspell", "Auto combat spell"),
    ("itemspell", "Item spell"),
    ("ritual", "Ritual"),
)
SUMMON_FIELDS = (
    ("sumrit", "Ritual summon"),
    ("#sumrit", "Ritual summon count"),
    ("sumauto", "Automatic summon"),
    ("#sumauto", "Automatic summon count"),
    ("sumbat", "Battle summon"),
    ("#sumbat", "Battle summon count"),
    ("batstartsum2", "Battle-start summon 2"),
    ("batstartsum3", "Battle-start summon 3"),
    ("batstartsum5d6", "Battle-start summon 5d6"),
    ("retinue", "Retinue"),
    ("summoner1d6", "Summoner 1d6"),
    ("summoner2d6", "Summoner 2d6"),
)
RISK_RESTRICTION_FIELDS = (
    ("curse", "Curse"),
    ("disease", "Disease"),
    ("cursed", "Cursed"),
    ("taint", "Taint"),
    ("aging", "Aging"),
    ("eyeloss", "Eye loss"),
    ("transformwearer", "Transform wearer"),
    ("feeblemindprovince", "Feeblemind province"),
    ("bearergainsinsanity", "Bearer gains insanity"),
    ("bearergainsinsanitypermonth", "Insanity / month"),
    ("horrormarkattacker", "Horror mark attacker"),
    ("chanceofattackbyknights", "Chance of attack by knights"),
    ("lesserhorrorattackchance", "Lesser horror attack chance"),
    ("leper", "Leper"),
    ("chestwound", "Chest wound"),
    ("feeblemind", "Feeblemind"),
    ("curserandomunits", "Curse random units"),
    ("spreaddeathormisfortune", "Spread death / misfortune"),
    ("singleuse", "Single use"),
    ("mustfightinarena", "Must fight in arena"),
    ("cannotwear", "Cannot wear"),
    ("minsizetoequip", "Minimum size"),
    ("maxsizetoequip", "Maximum size"),
    ("minstrtoequip", "Minimum Strength"),
    ("minhandstoequip", "Minimum hands"),
    ("onlyuseablebyfliersormounted", "Only fliers / mounted"),
    ("nomount", "No mount"),
    ("noinanimate", "No inanimate"),
    ("nomindless", "No mindless"),
    ("magerestriction", "Mage restriction"),
    ("strrequired", "Strength required"),
    ("nononsleeper", "No nonsleeper"),
    ("monstermustbepresent", "Monster must be present"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    return parser.parse_args()


def raw_value(row: dict[str, str], key: str) -> str:
    value = (row.get(key) or "").strip()
    return "" if value in ("", "0", "0.0") else value


def explicit_features(row: dict[str, str], specs: tuple[tuple[str, str], ...]) -> list[str]:
    out: list[str] = []
    for key, label in specs:
        value = raw_value(row, key)
        if not value:
            continue
        out.append(label if value in ("1", "1.0") else f"{label}: {value}")
    return out


def load_records(paths: dict[str, Path]):
    effects = {num(row, "record_id"): row for row in tsv(paths["effects_weapons.csv"])}
    effect_names = {
        num(row, "number"): clean_label(row.get("name", ""))
        for row in tsv(paths["effects_info.csv"])
    }
    special_rows = tsv(paths["special_damage_types.csv"])
    special = {
        num(row, "bit_value"): clean_label(row.get("bit_name", ""))
        for row in special_rows
    }
    weapon_attrs = defaultdict(list)
    for row in tsv(paths["attributes_by_weapon.csv"]):
        wid, attr = num(row, "weapon_number"), num(row, "attribute")
        if wid and attr:
            weapon_attrs[wid].append((attr, num(row, "raw_value")))
    attribute_names = {
        num(row, "number"): row.get("name", "")
        for row in tsv(paths["attribute_keys.csv"])
    }
    armor_attrs = parse_armor_attributes(
        tsv(paths["attributes_by_armor.csv"]), attribute_names
    )
    weapons = parse_weapons(
        tsv(paths["weapons.csv"]), effects, effect_names, special, weapon_attrs
    )
    armors = parse_armors(
        tsv(paths["armors.csv"]),
        tsv(paths["protections_by_armor.csv"]),
        armor_attrs,
    )
    return (
        {int(row["id"]): row for row in weapons},
        {int(row["id"]): row for row in armors},
    )


def item_header(title: str, intro: str) -> list[str]:
    return [
        "---",
        f'title: "{title}"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {item_core.COMMIT}"',
        "---",
        "",
        f"# {title}",
        "",
        intro,
        "",
        "[Magic Itemデータ索引へ戻る](index.md) · [Item固有効果攻略](../../items/effects-and-procs.md)",
        "",
    ]


def weapon_profile_page(
    items: list[dict[str, object]],
    raw_by_id: dict[int, dict[str, str]],
    weapons: dict[int, dict[str, object]],
) -> str:
    selected = [
        item for item in items
        if num(raw_by_id[int(item["id"])], "weapon") in weapons
    ]
    lines = item_header(
        "Magic Item Weapon profile",
        "Magic Itemが参照するWeapon recordをCombat dataと同じdecoderで展開します。Item本体の能力とWeapon固有のDamage / propertyを分離して確認できます。",
    )
    lines += [
        f"Weaponを参照するItemは**{len(selected)}**件です。",
        "",
        "| Item | ID | Research | Req | Gem | Weapon | Dmg | Att/Prec | Def | Len/Range | AoE | Attacks | STR | Damage type | Properties | Secondary |",
        "|---|---:|---|---|---|---|---|---:|---:|---|---|---:|---|---|---|---|",
    ]
    for item in selected:
        raw = raw_by_id[int(item["id"])]
        weapon = weapons[num(raw, "weapon")]
        reach = weapon["range"] if weapon["class"] == "射撃" else weapon["length"]
        lines.append(
            f"| {item_core.esc(item['name'])} | {item['id']} | {item['construction']} | {item['path']} | {item['cost']} | "
            f"{item_core.esc(weapon['name'])} #{weapon['id']} | {item_core.esc(weapon['damage'])} | {int(weapon['attack']):+d} | "
            f"{int(weapon['defense']):+d} | {reach} | {weapon['aoe']} | {weapon['attacks']} | {weapon['strength']} | "
            f"{item_core.esc(', '.join(weapon['types']) or '—')} | {item_core.esc(', '.join(weapon['properties']) or '—')} | "
            f"{item_core.esc(weapon['secondary'])} |"
        )
    lines += [
        "",
        "!!! note \"Magic weaponとMagic damageは別\"",
        "    `Magic weapon`はEthereal等へ通常攻撃を当てるための性質、`Magic damage`はDamage type側の性質です。同じ意味ではありません。",
        "",
    ]
    return "\n".join(lines)


def armor_summary(armor: dict[str, object]) -> str:
    atype = int(armor["type"])
    attrs = ", ".join(armor["attributes"]) or "—"
    if atype == 4:
        return f"Shield Prot {armor['shield']}; Parry {armor['parry']}; Def {int(armor['defense']):+d}; Enc {armor['enc']}; {attrs}"
    if atype == 5:
        return f"Body Prot {armor['body']}; Def {int(armor['defense']):+d}; Enc {armor['enc']}; Map penalty {armor['move']}; {attrs}"
    if atype == 6:
        return f"Head Prot {armor['head']}; Def {int(armor['defense']):+d}; Enc {armor['enc']}; {attrs}"
    return f"Body Prot {armor['body']}; Head Prot {armor['head']}; Def {int(armor['defense']):+d}; Enc {armor['enc']}; {attrs}"


def armor_profile_page(
    items: list[dict[str, object]],
    raw_by_id: dict[int, dict[str, str]],
    armors: dict[int, dict[str, object]],
) -> str:
    selected = [
        item for item in items
        if num(raw_by_id[int(item["id"])], "armor") in armors
    ]
    lines = item_header(
        "Magic Item Armor profile",
        "Magic Itemが参照するArmor recordをCombat dataと同じ計算で展開し、Shield Protection / Parry / Body・Head Protection / Encumbrance等をItem側から確認します。",
    )
    lines += [
        f"Armorを参照するItemは**{len(selected)}**件です。",
        "",
        "| Item | ID | Research | Req | Gem | Armor | Combat profile | Restriction |",
        "|---|---:|---|---|---|---|---|---|",
    ]
    for item in selected:
        raw = raw_by_id[int(item["id"])]
        armor = armors[num(raw, "armor")]
        lines.append(
            f"| {item_core.esc(item['name'])} | {item['id']} | {item['construction']} | {item['path']} | {item['cost']} | "
            f"{item_core.esc(armor['name'])} #{armor['id']} | {item_core.esc(armor_summary(armor))} | {item_core.esc(item['restriction'])} |"
        )
    return "\n".join(lines)


def explicit_field_page(
    title: str,
    intro: str,
    items: list[dict[str, object]],
    raw_by_id: dict[int, dict[str, str]],
    specs: tuple[tuple[str, str], ...],
) -> str:
    selected = [
        item for item in items
        if explicit_features(raw_by_id[int(item["id"])], specs)
    ]
    lines = item_header(title, intro)
    lines += [
        f"明示fieldが抽出されたItemは**{len(selected)}**件です。",
        "",
        "| Item | ID | Research | Req | Gem | Extracted fields | Restriction |",
        "|---|---:|---|---|---|---|---|",
    ]
    for item in selected:
        features = explicit_features(raw_by_id[int(item["id"])], specs)
        lines.append(
            f"| {item_core.esc(item['name'])} | {item['id']} | {item['construction']} | {item['path']} | {item['cost']} | "
            f"{item_core.esc('; '.join(features))} | {item_core.esc(item['restriction'])} |"
        )
    lines += [
        "",
        "!!! warning \"field名以上の意味を推測しない\"",
        "    この表はBaseIの明示fieldをそのまま索引化します。発動頻度、target、battle timing、summon unitの詳細はゲーム内Item詳細とDom6 Mod Inspectorで確認してください。",
        "",
    ]
    return "\n".join(lines)


def index_block() -> str:
    return "\n".join(
        [
            START,
            "## Weapon・Armor・固有効果",
            "",
            "- [Magic Item Weapon profile](weapon-profiles.md)",
            "- [Magic Item Armor profile](armor-profiles.md)",
            "- [Item Spell・自動効果](active-effects.md)",
            "- [Summon・Retinue効果](summoning-effects.md)",
            "- [副作用・装備制限](risk-restrictions.md)",
            "",
            "Item本体のfieldだけでなく、参照Weapon / ArmorのCombat profileや特殊効果まで追う索引です。攻略上の読み方は[Item固有効果・Weapon proc・副作用](../../items/effects-and-procs.md)を参照してください。",
            END,
            "",
        ]
    )


def patch_item_index() -> None:
    path = ITEM_OUT / "index.md"
    text = path.read_text(encoding="utf-8")
    block = index_block()
    if START in text and END in text:
        before, rest = text.split(START, 1)
        _old, after = rest.split(END, 1)
        text = before + block.rstrip() + after
    else:
        anchor = "\n## 表の読み方"
        if anchor not in text:
            raise ValueError("Magic Item index insertion anchor not found")
        text = text.replace(anchor, "\n" + block + "## 表の読み方", 1)
    path.write_text(text, encoding="utf-8")


def write_pages(
    items: list[dict[str, object]],
    raw_by_id: dict[int, dict[str, str]],
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
) -> None:
    ITEM_OUT.mkdir(parents=True, exist_ok=True)
    (ITEM_OUT / "weapon-profiles.md").write_text(
        weapon_profile_page(items, raw_by_id, weapons), encoding="utf-8"
    )
    (ITEM_OUT / "armor-profiles.md").write_text(
        armor_profile_page(items, raw_by_id, armors), encoding="utf-8"
    )
    (ITEM_OUT / "active-effects.md").write_text(
        explicit_field_page(
            "Item Spell・自動効果",
            "Item recordにSpell effect、battle start、automatic combat spell、item spell、ritualが明示されているItemです。",
            items,
            raw_by_id,
            DIRECT_EFFECT_FIELDS,
        ),
        encoding="utf-8",
    )
    (ITEM_OUT / "summoning-effects.md").write_text(
        explicit_field_page(
            "Summon・Retinue Item",
            "Ritual / automatic / battle summon、battle-start summon、Retinue、Summoner系fieldが明示されたItemです。",
            items,
            raw_by_id,
            SUMMON_FIELDS,
        ),
        encoding="utf-8",
    )
    (ITEM_OUT / "risk-restrictions.md").write_text(
        explicit_field_page(
            "Item副作用・装備制限",
            "Curse、Disease、Insanity、変身、Single use、装備者条件など、Item選択時に見落とすと危険な明示fieldの索引です。",
            items,
            raw_by_id,
            RISK_RESTRICTION_FIELDS,
        ),
        encoding="utf-8",
    )
    patch_item_index()


def main() -> None:
    args = parse_args()
    names = (
        "BaseI.csv",
        "weapons.csv",
        "armors.csv",
        "effects_weapons.csv",
        "effects_info.csv",
        "special_damage_types.csv",
        "attributes_by_weapon.csv",
        "attribute_keys.csv",
        "protections_by_armor.csv",
        "attributes_by_armor.csv",
    )
    paths = {name: source(name, args.refresh, args.offline) for name in names}
    items = item_core.item_rows(paths)
    raw_by_id = {
        num(row, "id"): row
        for row in tsv(paths["BaseI.csv"])
        if num(row, "id")
    }
    weapons, armors = load_records(paths)
    write_pages(items, raw_by_id, weapons, armors)

    weapon_items = sum(num(raw_by_id[int(item["id"])], "weapon") in weapons for item in items)
    armor_items = sum(num(raw_by_id[int(item["id"])], "armor") in armors for item in items)
    active = sum(bool(explicit_features(raw_by_id[int(item["id"])], DIRECT_EFFECT_FIELDS)) for item in items)
    summons = sum(bool(explicit_features(raw_by_id[int(item["id"])], SUMMON_FIELDS)) for item in items)
    risks = sum(bool(explicit_features(raw_by_id[int(item["id"])], RISK_RESTRICTION_FIELDS)) for item in items)
    print(f"generated item weapon profiles: {weapon_items}")
    print(f"generated item armor profiles: {armor_items}")
    print(f"generated item active effects: {active}")
    print(f"generated item summon effects: {summons}")
    print(f"generated item risk/restriction effects: {risks}")


if __name__ == "__main__":
    main()
