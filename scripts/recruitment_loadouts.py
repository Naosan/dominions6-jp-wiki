from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

from combat_data_armor import parse_armor_attributes, parse_armors
from combat_data_common import clean_label, num, tsv
from combat_data_weapons import parse_weapons

IMPORTANT_PROPERTIES = {
    "両手",
    "AP",
    "AN",
    "盾無視",
    "Defence Negate",
    "Charge",
    "Heavy Charge",
    "Repel不可",
    "Repelされない",
    "MR Negates",
    "MR Negates Easily",
    "Hard MR Negates",
    "MRで半減",
    "Soul Slay",
    "Size/STRで抵抗",
    "頭部命中率増",
    "True Damage",
    "Internal Damage",
    "騎乗時のみ",
    "徒歩時のみ",
    "盾にAttack +2（Flail）",
    "Magic weapon",
    "Nonmagical",
}


def equipment_indexes(paths: dict[str, Path]):
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
        weapon_id = num(row, "weapon_number")
        attribute = num(row, "attribute")
        if weapon_id and attribute:
            weapon_attrs[weapon_id].append((attribute, num(row, "raw_value")))

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
        {item["id"]: item for item in weapons},
        {item["id"]: item for item in armors},
    )


def unit_weapon_ids(row: dict[str, str]) -> list[int]:
    return [
        weapon_id
        for index in range(1, 8)
        if (weapon_id := num(row, f"wpn{index}")) > 0
    ]


def unit_armor_ids(row: dict[str, str]) -> list[int]:
    return [
        armor_id
        for index in range(1, 5)
        if (armor_id := num(row, f"armor{index}")) > 0
    ]


def signed(value: int) -> str:
    return f"{value:+d}"


def numeric_damage(value: object) -> bool:
    text = str(value).strip()
    return text.lstrip("-").isdigit()


def limited_properties(item: dict[str, object]) -> list[str]:
    out: list[str] = []
    for value in item.get("properties", []):
        text = str(value)
        if text in IMPORTANT_PROPERTIES or text.startswith("騎乗時のみ") or text.startswith("徒歩時のみ"):
            if text not in out:
                out.append(text)
    return out


def weapon_summary(item: dict[str, object], count: int = 1) -> str:
    name = f"{item['name']} #{item['id']}"
    if count > 1:
        name += f" ×{count}"

    damage = str(item["damage"])
    strength = str(item["strength"])
    if strength != "—" and numeric_damage(damage):
        damage = f"{damage}+{strength}"
    elif strength != "—":
        damage = f"{damage} / {strength}加算"

    parts = [f"Dmg {damage}"]
    if item["class"] == "近接":
        parts.extend(
            [
                f"Att {signed(int(item['attack']))}",
                f"Def {signed(int(item['defense']))}",
                f"Len {item['length']}",
            ]
        )
    else:
        parts.extend(
            [
                f"Prec {signed(int(item['attack']))}",
                f"Range {item['range']}",
            ]
        )
        if item["aoe"] != "—":
            parts.append(f"AoE {item['aoe']}")
        parts.append(f"Ammo {item['ammo']}")

    if int(item["attacks"]) != 1:
        parts.append(f"Attacks {item['attacks']}")

    tags: list[str] = []
    for value in item.get("types", []):
        text = str(value)
        if text not in tags:
            tags.append(text)
    for value in limited_properties(item):
        if value not in tags:
            tags.append(value)
    if tags:
        parts.append(", ".join(tags[:8]))
    if item.get("secondary") not in (None, "", "—"):
        parts.append(str(item["secondary"]))
    return f"**{name}** — " + "; ".join(parts)


def armor_summary(item: dict[str, object], count: int = 1) -> str:
    name = f"{item['name']} #{item['id']}"
    if count > 1:
        name += f" ×{count}"
    armor_type = int(item["type"])
    parts: list[str] = []
    if armor_type == 4:
        parts = [
            f"Shield Prot {item['shield']}",
            f"Parry {item['parry']}",
            f"Def {signed(int(item['defense']))}",
            f"Enc {item['enc']}",
        ]
    elif armor_type == 5:
        parts = [
            f"Body Prot {item['body']}",
            f"Def {signed(int(item['defense']))}",
            f"Enc {item['enc']}",
            f"Map penalty {item['move']}",
        ]
    elif armor_type == 6:
        parts = [
            f"Head Prot {item['head']}",
            f"Def {signed(int(item['defense']))}",
            f"Enc {item['enc']}",
        ]
    else:
        parts = [
            f"Body Prot {item['body']}",
            f"Head Prot {item['head']}",
            f"Def {signed(int(item['defense']))}",
            f"Enc {item['enc']}",
        ]
    attributes = [str(value) for value in item.get("attributes", [])]
    if attributes:
        parts.append(", ".join(attributes[:5]))
    return f"**{name}** — " + "; ".join(parts)


def grouped_summaries(
    ids: list[int],
    lookup: dict[int, dict[str, object]],
    renderer,
    missing_label: str,
) -> list[str]:
    counts = Counter(ids)
    out: list[str] = []
    for item_id in dict.fromkeys(ids):
        item = lookup.get(item_id)
        if item is None:
            out.append(f"{missing_label} #{item_id}")
        else:
            out.append(renderer(item, counts[item_id]))
    return out


def equipment_profile(
    row: dict[str, str],
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
) -> list[str]:
    weapon_rows = [weapons[item_id] for item_id in unit_weapon_ids(row) if item_id in weapons]
    armor_rows = [armors[item_id] for item_id in unit_armor_ids(row) if item_id in armors]
    out: list[str] = []

    if any(int(item["type"]) == 4 for item in armor_rows):
        out.append("盾持ち")
    if any("両手" in item.get("properties", []) for item in weapon_rows):
        out.append("両手武器")
    if any(item["class"] == "射撃" for item in weapon_rows):
        out.append("射撃")
    for label in ("AP", "AN", "Charge", "盾無視", "Defence Negate", "MR Negates", "Soul Slay"):
        if any(label in item.get("properties", []) for item in weapon_rows):
            out.append(label)
    if any(int(item["attacks"]) > 1 for item in weapon_rows):
        out.append("武器内多段")
    if len(unit_weapon_ids(row)) > 1:
        out.append("複数武器")
    if num(row, "ambidextrous"):
        out.append(f"Ambidextrous {num(row, 'ambidextrous')}")
    if num(row, "mountmnr") or num(row, "mounted"):
        out.append("騎乗")
    if num(row, "skilledrider"):
        out.append("Skilled Rider")
    if num(row, "tightrein"):
        out.append("Tight Rein")
    if num(row, "smartmount"):
        out.append("Smart Mount")
    if num(row, "regainmount"):
        out.append("Regain Mount")
    return out


def mount_summary(
    rider: dict[str, str],
    units: dict[int, dict[str, str]],
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
) -> str:
    mount_id = num(rider, "mountmnr")
    if not mount_id:
        return "Mounted flag（Mount recordなし）" if num(rider, "mounted") else "—"
    mount = units.get(mount_id)
    if mount is None:
        return f"Unknown mount #{mount_id}"

    stats = (
        f"HP {mount.get('hp') or '—'} / Prot {mount.get('prot') or '—'} / "
        f"MR {mount.get('mr') or '—'} / Mor {mount.get('mor') or '—'} / "
        f"Def {mount.get('def') or '—'} / Map {mount.get('mapmove') or '—'} / AP {mount.get('ap') or '—'}"
    )
    mount_weapons = grouped_summaries(
        unit_weapon_ids(mount), weapons, weapon_summary, "Unknown weapon"
    )
    mount_armors = grouped_summaries(
        unit_armor_ids(mount), armors, armor_summary, "Unknown armor"
    )
    details: list[str] = [f"**{mount.get('name') or '(unnamed)'} #{mount_id}** — {stats}"]
    if mount_weapons:
        details.append("攻撃: " + " / ".join(mount_weapons))
    if mount_armors:
        details.append("装備: " + " / ".join(mount_armors))
    return "<br>".join(details)


def equipment_table(
    items: list[dict[str, str]],
    units: dict[int, dict[str, str]],
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
) -> str:
    if not items:
        return "該当データなし。\n"
    out = [
        "| Unit | ID | Weapons | Armor | Mount | Profile |",
        "|---|---:|---|---|---|---|",
    ]
    for row in items:
        weapon_lines = grouped_summaries(
            unit_weapon_ids(row), weapons, weapon_summary, "Unknown weapon"
        )
        armor_lines = grouped_summaries(
            unit_armor_ids(row), armors, armor_summary, "Unknown armor"
        )
        profile = equipment_profile(row, weapons, armors)
        out.append(
            "| {name} | {unit_id} | {weapons} | {armors} | {mount} | {profile} |".format(
                name=str(row.get("name") or "(unnamed)").replace("|", "\\|"),
                unit_id=row["id"],
                weapons=("<br>".join(weapon_lines) or "—").replace("|", "\\|"),
                armors=("<br>".join(armor_lines) or "—").replace("|", "\\|"),
                mount=mount_summary(row, units, weapons, armors).replace("|", "\\|"),
                profile=(", ".join(profile) or "—").replace("|", "\\|"),
            )
        )
    return "\n".join(out) + "\n"


def validate_equipment_refs(
    units: dict[int, dict[str, str]],
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
) -> dict[str, object]:
    weapon_refs: set[int] = set()
    armor_refs: set[int] = set()
    mount_refs: set[int] = set()
    units_with_weapons = 0
    units_with_armor = 0
    mounted_units = 0

    for row in units.values():
        current_weapons = unit_weapon_ids(row)
        current_armors = unit_armor_ids(row)
        if current_weapons:
            units_with_weapons += 1
            weapon_refs.update(current_weapons)
        if current_armors:
            units_with_armor += 1
            armor_refs.update(current_armors)
        mount_id = num(row, "mountmnr")
        if mount_id:
            mounted_units += 1
            mount_refs.add(mount_id)

    return {
        "units_with_weapons": units_with_weapons,
        "units_with_armor": units_with_armor,
        "mounted_units": mounted_units,
        "weapon_refs": len(weapon_refs),
        "armor_refs": len(armor_refs),
        "mount_refs": len(mount_refs),
        "missing_weapons": sorted(weapon_refs - set(weapons)),
        "missing_armors": sorted(armor_refs - set(armors)),
        "missing_mounts": sorted(mount_refs - set(units)),
    }
