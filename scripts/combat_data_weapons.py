from __future__ import annotations

from collections import Counter, defaultdict

from combat_data_common import COMMIT, WEAPON_OUT, clean_label, esc, has, num

CORE_LABELS = (
    ("two_handed", "両手"), ("armor_piercing", "AP"),
    ("armor_negating", "AN"), ("ignore_shield", "盾無視"),
    ("defense_negate", "Defence Negate"), ("charge", "Charge"),
    ("heavy_charge", "Heavy Charge"), ("cannot_repel", "Repel不可"),
    ("cannot_be_repelled", "Repelされない"),
    ("mr_negates", "MR Negates"),
    ("mr_negates_easily", "MR Negates Easily"),
    ("hard_mr_negates", "Hard MR Negates"),
    ("mr_half_damage", "MRで半減"), ("soul_slaying", "Soul Slay"),
    ("size_or_strength_negates", "Size/STRで抵抗"),
    ("hit_head", "頭部命中率増"), ("underwater_ok", "水中使用可"),
    ("beam", "Beam/Breath"), ("false_damage", "False Damage"),
    ("true_damage", "True Damage"), ("internal_damage", "Internal Damage"),
)
ATTRIBUTE_LABELS = {
    266: "Ferrous", 267: "Ferrous", 268: "Flammable material",
    269: "Flammable material", 482: "Fire Bless無効", 557: "Magic",
    611: "Penetration bonus有効", 910: "追加Poison damage",
    933: "Demon/UndeadへAN Holy damage",
    935: "盾にAttack +2（Flail）", 942: "騎乗時のみ", 943: "徒歩時のみ",
}


def strength_text(mask: int) -> str:
    if has(mask, "third_strength"):
        return "STR/3"
    if has(mask, "half_strength"):
        return "STR/2"
    return "STR" if has(mask, "strength") else "—"


def damage_types(mask: int) -> list[str]:
    pairs = (
        ("slashing", "Slash"), ("piercing", "Pierce"), ("blunt", "Blunt"),
        ("fire", "Fire"), ("cold", "Cold"), ("shock", "Shock"),
        ("poison", "Poison"), ("acid", "Acid"),
        ("magic_damage", "Magic damage"), ("true_damage", "True"),
        ("internal_damage", "Internal"),
    )
    return [label for key, label in pairs if has(mask, key)]


def property_tags(mask: int, attrs: list[tuple[int, int]]) -> list[str]:
    out = [label for key, label in CORE_LABELS if has(mask, key)]
    out.append("Nonmagical" if has(mask, "nonmagical") else "Magic weapon")
    for key, label in (("intrinsic", "Intrinsic"), ("iron", "Iron"),
                       ("enemy_only", "敵のみ"),
                       ("mindless_immune", "Mindless無効"),
                       ("undead_immune", "Undead無効"),
                       ("sacred_only", "Sacredのみ")):
        if has(mask, key):
            out.append(label)
    for attr, raw in attrs:
        label = ATTRIBUTE_LABELS.get(attr)
        if label:
            if raw not in (0, 1):
                label = f"{label} {raw}"
            if label not in out:
                out.append(label)
    return out


def special_damage_text(raw: int, lookup: dict[int, str]) -> str:
    if raw in lookup and "unknown" not in lookup[raw].lower():
        return lookup[raw]
    labels = [name for bit, name in sorted(lookup.items())
              if bit > 0 and raw & bit and "unknown" not in name.lower()]
    return " + ".join(labels) if labels else f"Special {raw}"


def damage_text(effect: dict[str, str], effect_names: dict[int, str], special: dict[int, str]) -> str:
    effect_no, raw = num(effect, "effect_number"), num(effect, "raw_argument")
    if effect_no == 2:
        return str(raw)
    if effect_no == 11:
        return special_damage_text(raw, special)
    name = effect_names.get(effect_no, f"Effect {effect_no}")
    return f"{raw} {name}" if raw else name


def range_text(effect: dict[str, str]) -> str:
    base, divisor = num(effect, "range_base"), num(effect, "range_strength_divisor")
    if base:
        return str(base)
    if divisor:
        return "STR" if divisor == 1 else f"STR/{divisor}"
    return "—"


def area_text(effect: dict[str, str]) -> str:
    pct = num(effect, "area_battlefield_pct")
    if pct:
        return f"戦場{pct}%"
    base = num(effect, "area_base")
    return str(base) if base else "—"


def secondary_text(row: dict[str, str], lookup: dict[int, dict[str, str]]) -> str:
    out: list[str] = []
    for key, prefix in (("secondaryeffect", "On damage"),
                        ("secondaryeffectalways", "Always")):
        wid = num(row, key)
        if wid:
            out.append(f"{prefix}: {lookup.get(wid, {}).get('name', f'Weapon {wid}')} #{wid}")
    return "; ".join(out) or "—"


def parse_weapons(rows, effects, effect_names, special, attrs):
    lookup = {num(row, "id"): row for row in rows if num(row, "id")}
    out = []
    for row in rows:
        wid = num(row, "id")
        if not wid:
            continue
        effect = effects.get(num(row, "effect_record_id"), {})
        mask = num(effect, "modifiers_mask")
        ranged = bool(num(effect, "range_base") or num(effect, "range_strength_divisor"))
        ammo = num(row, "ammo")
        out.append({
            "id": wid, "name": row.get("name") or "(unnamed)",
            "class": "射撃" if ranged else "近接",
            "damage": damage_text(effect, effect_names, special),
            "attack": num(row, "att"), "defense": num(row, "def"),
            "length": num(row, "len"), "range": range_text(effect),
            "aoe": area_text(effect), "attacks": max(1, num(row, "nratt", 1)),
            "ammo": (ammo or 12) if ranged else 0, "rcost": num(row, "rcost"),
            "strength": strength_text(mask), "types": damage_types(mask),
            "properties": property_tags(mask, attrs.get(wid, [])),
            "secondary": secondary_text(row, lookup), "mask": mask,
        })
    return sorted(out, key=lambda item: (item["class"], item["id"]))


def table(items, mode: str) -> str:
    if mode == "melee":
        out = ["| Weapon | ID | Dmg | Att | Def | Len | Attacks | STR | Damage type | Properties | Secondary |",
               "|---|---:|---|---:|---:|---:|---:|---|---|---|---|"]
        for x in items:
            out.append(f"| {esc(x['name'])} | {x['id']} | {esc(x['damage'])} | {x['attack']:+d} | {x['defense']:+d} | {x['length']} | {x['attacks']} | {x['strength']} | {esc(', '.join(x['types']) or '—')} | {esc(', '.join(x['properties']) or '—')} | {esc(x['secondary'])} |")
    elif mode == "ranged":
        out = ["| Weapon | ID | Dmg | Prec | Range | AoE | Attacks | Ammo | STR | Damage type | Properties | Secondary |",
               "|---|---:|---|---:|---|---|---:|---:|---|---|---|---|"]
        for x in items:
            out.append(f"| {esc(x['name'])} | {x['id']} | {esc(x['damage'])} | {x['attack']:+d} | {x['range']} | {x['aoe']} | {x['attacks']} | {x['ammo']} | {x['strength']} | {esc(', '.join(x['types']) or '—')} | {esc(', '.join(x['properties']) or '—')} | {esc(x['secondary'])} |")
    else:
        out = ["| Weapon | ID | Class | Dmg | Att/Prec | Def | Len/Range | AoE | Attacks | STR | Damage type | Properties | Secondary |",
               "|---|---:|---|---|---:|---:|---|---|---:|---|---|---|---|"]
        for x in items:
            reach = x["range"] if x["class"] == "射撃" else x["length"]
            out.append(f"| {esc(x['name'])} | {x['id']} | {x['class']} | {esc(x['damage'])} | {x['attack']:+d} | {x['defense']:+d} | {reach} | {x['aoe']} | {x['attacks']} | {x['strength']} | {esc(', '.join(x['types']) or '—')} | {esc(', '.join(x['properties']) or '—')} | {esc(x['secondary'])} |")
    return "\n".join(out) + "\n"


def page(title: str, intro: str, items, mode: str) -> str:
    return f'''---
title: "{title}"
status: generated
verified_version: "6.35"
generated_from: "dom6inspector {COMMIT}"
---

# {title}

{intro}

!!! info "自動生成データ"
    Weapon record単体の値です。UnitのStrength、Bless、Buff、Mount、二刀流、Fatigue等を加えた最終戦闘性能ではありません。

{table(items, mode)}

## 表の読み方

- **Dmg**は基礎値または特殊効果名、**STR**はDamage / Rangeへ加算されるStrength割合。
- **Magic weapon**と**Magic damage**は別概念。
- Secondary effectの発動条件や対象はゲーム内表示で再確認する。

[武器データ索引へ戻る](index.md) · [戦闘ルール](../../../basics/combat-rules.md) · [武器と盾](../../../basics/weapons-and-shields.md)
'''


def write_weapon_pages(weapons):
    WEAPON_OUT.mkdir(parents=True, exist_ok=True)
    melee = [x for x in weapons if x["class"] == "近接"]
    ranged = [x for x in weapons if x["class"] == "射撃"]
    ap_an = [x for x in weapons if has(x["mask"], "armor_piercing") or has(x["mask"], "armor_negating")]
    elemental = [x for x in weapons if any(v in x["types"] for v in ("Fire", "Cold", "Shock", "Poison", "Acid"))]
    unusual = [x for x in weapons if x["secondary"] != "—" or any(v in x["properties"] for v in ("盾無視", "Defence Negate", "Soul Slay", "MR Negates", "Hard MR Negates", "True Damage", "Internal Damage"))]
    specs = (
        ("melee.md", "近接武器データ", "近接WeaponをAttack、Defence、Length、Damage属性で比較します。", melee, "melee"),
        ("ranged.md", "射撃武器データ", "射撃WeaponをPrecision、Range、AoE、Ammoで比較します。", ranged, "ranged"),
        ("ap-an.md", "AP・AN武器", "Armor Piercing / Armor Negatingを持つWeaponです。", ap_an, "mixed"),
        ("elemental.md", "Elemental・Poison・Acid武器", "対応Resistanceとの差で評価する属性Weaponです。", elemental, "mixed"),
        ("special.md", "特殊効果武器", "Secondary effect、MR判定、盾無視等を持つWeaponです。", unusual, "mixed"),
    )
    for filename, title, intro, items, mode in specs:
        (WEAPON_OUT / filename).write_text(page(title, intro, items, mode), encoding="utf-8")
    counts = Counter(x["class"] for x in weapons)
    (WEAPON_OUT / "index.md").write_text(f'''---
title: "武器データ索引"
status: generated
verified_version: "6.35"
generated_from: "dom6inspector {COMMIT}"
---

# 武器データ索引

| 区分 | 件数 | ページ |
|---|---:|---|
| 近接 | {counts['近接']} | [近接武器](melee.md) |
| 射撃 | {counts['射撃']} | [射撃武器](ranged.md) |
| AP / AN | {len(ap_an)} | [AP・AN武器](ap-an.md) |
| Elemental / Poison / Acid | {len(elemental)} | [属性武器](elemental.md) |
| 特殊効果 | {len(unusual)} | [特殊効果武器](special.md) |

Weapon record単体には装備者のStrength、攻撃回数、Cost、Bless、Buff、Formationは含まれません。

- [Weapon property・Damage type](../weapon-properties.md)
- [特殊Damage・状態効果](../special-damage.md)
- [武器と盾の攻略](../../../basics/weapons-and-shields.md)
''', encoding="utf-8")
    return {"melee": len(melee), "ranged": len(ranged), "ap_an": len(ap_an), "elemental": len(elemental), "special": len(unusual)}


def property_reference(modifier_rows) -> str:
    groups = defaultdict(list)
    for row in modifier_rows:
        bit, label = num(row, "bit_value"), clean_label(row.get("bit_name", ""))
        if not bit or not label:
            continue
        low = label.lower()
        if any(w in low for w in ("armor", "damage", "fire", "cold", "shock", "poison", "acid", "strength")):
            group = "Damage・Armor・Strength"
        elif any(w in low for w in ("shield", "repel", "charge", "two hands", "head")):
            group = "命中・盾・Repel・Charge"
        elif any(w in low for w in ("magic resistance", "mindless", "undead", "demon", "animal", "sacred", "friend", "enemy")):
            group = "対象・抵抗判定"
        else:
            group = "その他"
        groups[group].append((bit, label))
    out = ["---", 'title: "Weapon property・Damage type"', "status: generated",
           'verified_version: "6.35"', f'generated_from: "dom6inspector {COMMIT}"', "---", "",
           "# Weapon property・Damage type", "",
           "## 重要な区別", "",
           "- **Magic weapon**: Nonmagical flagを持たないWeapon。Ethereal等への命中に関係。",
           "- **Magic damage**: Damage自体の別modifierで、Magic weaponと同義ではない。",
           "- **AP**: Armor由来Protectionを一部適用。**AN**: Armor Protectionを無視。",
           "- Slash / Pierce / BluntとFire / Cold / Shock等は別の分類。", "", "## Modifier bit一覧", ""]
    for group in ("Damage・Armor・Strength", "命中・盾・Repel・Charge", "対象・抵抗判定", "その他"):
        out += [f"### {group}", "", "| Bit | Data label |", "|---:|---|"]
        out += [f"| {bit} | {esc(label)} |" for bit, label in sorted(groups[group])]
        out.append("")
    return "\n".join(out)


def damage_reference(special_rows) -> str:
    known, unknown = [], 0
    for row in special_rows:
        bit, label = num(row, "bit_value"), clean_label(row.get("bit_name", ""))
        if not bit or not label:
            continue
        if "unknown" in label.lower():
            unknown += 1
        else:
            known.append((bit, label))
    out = ["---", 'title: "特殊Damage・状態効果"', "status: generated",
           'verified_version: "6.35"', f'generated_from: "dom6inspector {COMMIT}"', "---", "",
           "# 特殊Damage・状態効果", "",
           "通常HP Damage以外の特殊bitのうち、名称が判明しているものを掲載します。", "",
           "| Bit | Data label |", "|---:|---|"]
    out += [f"| {bit} | {esc(label)} |" for bit, label in sorted(known)]
    out += ["", f"名称不明のbitは**{unknown}件**あり省略しています。", "",
            "!!! warning", "    Disease、Curse、Decay、Blind、Slow等の抵抗条件は個別Weapon・Spellのゲーム内表示を確認してください。", "",
            "[Combat data索引へ戻る](index.md)"]
    return "\n".join(out)
