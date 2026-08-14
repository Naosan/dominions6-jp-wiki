#!/usr/bin/env python3
"""Generate Dominions 6 weapon, armor, and damage-type indexes."""
from __future__ import annotations

from collections import Counter, defaultdict

from combat_data_armor import parse_armor_attributes, parse_armors, write_armor_pages
from combat_data_common import COMMIT, FILES, OUT, TYPE_NAMES, clean_label, num, parse_args, source, tsv
from combat_data_weapons import damage_reference, parse_weapons, property_reference, write_weapon_pages


def write_index(weapon_count: int, armor_count: int) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.md").write_text(f'''---
title: "Combat data索引"
status: generated
verified_version: "6.35"
generated_from: "dom6inspector {COMMIT}"
---

# Combat data索引

武器、防具、Damage modifierをDominions 6.35の固定データから生成します。

## 武器

- [武器データ索引](weapons/index.md)
- [近接武器](weapons/melee.md)
- [射撃武器](weapons/ranged.md)
- [AP・AN武器](weapons/ap-an.md)
- [Elemental・Poison・Acid武器](weapons/elemental.md)
- [特殊効果武器](weapons/special.md)

## 防具

- [防具データ索引](armor/index.md)
- [盾](armor/shields.md)
- [胴鎧](armor/body-armor.md)
- [兜](armor/helmets.md)

## Damage・property

- [Weapon property・Damage type](weapon-properties.md)
- [特殊Damage・状態効果](special-damage.md)

自動索引はWeapon / Armor recordの事実を示します。Unitの最終性能はStrength、Size、攻撃回数、Cost、Bless、Buff、Formation、敵構成と組み合わせて[戦闘攻略](../../basics/index.md)で判断します。

登録件数: Weapon **{weapon_count}**、Armor **{armor_count}**。
''', encoding="utf-8")


def main() -> None:
    args = parse_args()
    paths = {name: source(name, args.refresh, args.offline) for name in FILES}
    effects = {num(r, "record_id"): r for r in tsv(paths["effects_weapons.csv"])}
    effect_names = {num(r, "number"): clean_label(r.get("name", "")) for r in tsv(paths["effects_info.csv"])}
    special_rows = tsv(paths["special_damage_types.csv"])
    special = {num(r, "bit_value"): clean_label(r.get("bit_name", "")) for r in special_rows}
    weapon_attrs = defaultdict(list)
    for r in tsv(paths["attributes_by_weapon.csv"]):
        wid, attr = num(r, "weapon_number"), num(r, "attribute")
        if wid and attr:
            weapon_attrs[wid].append((attr, num(r, "raw_value")))
    attribute_names = {num(r, "number"): r.get("name", "") for r in tsv(paths["attribute_keys.csv"])}
    armor_attrs = parse_armor_attributes(tsv(paths["attributes_by_armor.csv"]), attribute_names)
    weapons = parse_weapons(tsv(paths["weapons.csv"]), effects, effect_names, special, weapon_attrs)
    armors = parse_armors(tsv(paths["armors.csv"]), tsv(paths["protections_by_armor.csv"]), armor_attrs)
    if len(weapons) < 500:
        raise ValueError(f"weapon data appears incomplete: {len(weapons)}")
    if len(armors) < 100:
        raise ValueError(f"armor data appears incomplete: {len(armors)}")
    weapon_groups = write_weapon_pages(weapons)
    armor_groups = write_armor_pages(armors)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "weapon-properties.md").write_text(property_reference(tsv(paths["effect_modifier_bits.csv"])), encoding="utf-8")
    (OUT / "special-damage.md").write_text(damage_reference(special_rows), encoding="utf-8")
    write_index(len(weapons), len(armors))
    print(f"source commit: {COMMIT}")
    print(f"generated weapon records: {len(weapons)}")
    print(f"weapon groups: {weapon_groups}")
    print(f"generated armor records: {len(armors)}")
    print(f"armor types: {dict(Counter(TYPE_NAMES[x['type']] for x in armors))}")
    print(f"armor groups: {armor_groups}")


if __name__ == "__main__":
    main()
