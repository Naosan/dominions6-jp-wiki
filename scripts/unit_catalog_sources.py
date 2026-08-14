from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from generate_recruitment_data import (
    BY_CODE,
    COMMIT,
    FILES as RECRUIT_FILES,
    cap,
    fixed_text,
    mapping,
    nations,
    num,
    random_text,
    source,
    tsv,
    unit_data,
)
from generate_spell_item_data import (
    SCHOOLS,
    effect_map,
    nation_names,
    spell_attributes,
    spell_availability,
    spell_gem_cost,
    spell_kind,
    spell_path,
    spell_research,
)
from recruitment_loadouts import equipment_indexes

EXTRA_FILES = (
    "pretender_types_by_nation.csv",
    "attributes_by_nation.csv",
    "MagicSites.csv",
    "spells.csv",
    "effects_spells.csv",
    "attributes_by_spell.csv",
)
FILES = tuple(dict.fromkeys(RECRUIT_FILES + EXTRA_FILES))

RECRUIT_MAP_FILES = {
    "ft": ("fort_troop_types_by_nation.csv", "Fort troop", "Troop"),
    "fl": ("fort_leader_types_by_nation.csv", "Fort commander", "Commander"),
    "nt": ("nonfort_troop_types_by_nation.csv", "Fort不要・地形・外国 troop", "Troop"),
    "nl": ("nonfort_leader_types_by_nation.csv", "Fort不要・地形・外国 commander", "Commander"),
    "ct": ("coast_troop_types_by_nation.csv", "Coastal troop", "Troop"),
    "cl": ("coast_leader_types_by_nation.csv", "Coastal commander", "Commander"),
}

HERO_ATTRIBUTES = {
    139: ("Unique Hero", "hero1"),
    140: ("Unique Hero", "hero2"),
    141: ("Unique Hero", "hero3"),
    142: ("Unique Hero", "hero4"),
    143: ("Unique Hero", "hero5"),
    144: ("Unique Hero", "hero6"),
    145: ("Generic Hero", "multihero1"),
    146: ("Generic Hero", "multihero2"),
}

SUMMON_EFFECTS = {
    1: "Summon",
    31: "Summon independent",
    43: "Border summon",
    10001: "Summon",
    10021: "Summon commander",
    10037: "Farsummon",
    10038: "Independent farsummon",
}

SITE_UNIT_FIELDS = {
    **{f"mon{index}": ("Site troop recruit", "Troop") for index in range(1, 6)},
    **{f"com{index}": ("Site commander recruit", "Commander") for index in range(1, 6)},
    **{f"hmon{index}": ("Hidden troop slot", "Troop") for index in range(1, 6)},
    **{f"hcom{index}": ("Hidden commander slot", "Commander") for index in range(1, 6)},
    **{f"sum{index}": ("Site summon slot", "Summon") for index in range(1, 5)},
    "natmon": ("National site troop", "Troop"),
    "natcom": ("National site commander", "Commander"),
}

SHAPE_FIELDS = {
    "shapechange": "Shape Change",
    "firstshape": "First Shape",
    "secondshape": "Second Shape",
    "secondtmpshape": "Temporary Second Shape",
    "landshape": "Land Shape",
    "watershape": "Water Shape",
    "forestshape": "Forest Shape",
    "plainshape": "Plain Shape",
    "xpshape": "Experience Shape",
    "homeshape": "Home Shape",
    "prophetshape": "Prophet Shape",
    "cleanshape": "Clean Shape",
    "raiseshape": "Raised Shape",
}


def load_catalog_inputs(refresh: bool, offline: bool) -> tuple[dict[str, Path], list[dict[str, object]]]:
    paths = {name: source(name, refresh, offline) for name in FILES}
    nation_rows = nations()
    return paths, nation_rows


def nation_lookup(nation_rows: list[dict[str, object]]) -> dict[int, dict[str, object]]:
    return {int(nation["id"]): nation for nation in nation_rows}


def load_recruit_maps(paths: dict[str, Path]):
    return {
        key: mapping(paths[filename])
        for key, (filename, _label, _role) in RECRUIT_MAP_FILES.items()
    }


def build_recruit_relations(
    nation_rows: list[dict[str, object]],
    units: dict[int, dict[str, str]],
    maps,
):
    by_unit: dict[int, list[dict[str, object]]] = defaultdict(list)
    seen: set[tuple[int, int, str]] = set()
    for nation in nation_rows:
        nation_id = int(nation["id"])
        for key, (_filename, source_label, role) in RECRUIT_MAP_FILES.items():
            for unit_id in maps[key].get(nation_id, []):
                relation_key = (nation_id, unit_id, key)
                if relation_key in seen or unit_id not in units:
                    continue
                seen.add(relation_key)
                by_unit[unit_id].append(
                    {
                        "kind": "Recruit",
                        "nation_id": nation_id,
                        "nation": nation["name"],
                        "era": nation["code"],
                        "directory": nation["dir"],
                        "slug": nation["slug"],
                        "source": source_label,
                        "role": role,
                        "capital_only": cap(units[unit_id]),
                    }
                )
    return by_unit


def build_hero_relations(
    rows: list[dict[str, str]],
    nation_rows: list[dict[str, object]],
    units: dict[int, dict[str, str]],
):
    nations_by_id = nation_lookup(nation_rows)
    by_unit: dict[int, list[dict[str, object]]] = defaultdict(list)
    seen: set[tuple[int, int, int]] = set()
    for row in rows:
        nation_id = num(row, "nation_number")
        attribute = num(row, "attribute")
        unit_id = num(row, "raw_value")
        if attribute not in HERO_ATTRIBUTES or nation_id not in nations_by_id or unit_id not in units:
            continue
        key = (nation_id, unit_id, attribute)
        if key in seen:
            continue
        seen.add(key)
        nation = nations_by_id[nation_id]
        hero_type, slot = HERO_ATTRIBUTES[attribute]
        by_unit[unit_id].append(
            {
                "kind": "Hero",
                "hero_type": hero_type,
                "slot": slot,
                "nation_id": nation_id,
                "nation": nation["name"],
                "era": nation["code"],
                "directory": nation["dir"],
                "slug": nation["slug"],
            }
        )
    return by_unit


def build_pretender_relations(
    rows: list[dict[str, str]],
    nation_rows: list[dict[str, object]],
    units: dict[int, dict[str, str]],
):
    nations_by_id = nation_lookup(nation_rows)
    by_unit: dict[int, list[dict[str, object]]] = defaultdict(list)
    seen: set[tuple[int, int]] = set()
    for row in rows:
        unit_id = num(row, "monster_number")
        nation_id = num(row, "nation_number")
        if unit_id not in units or nation_id not in nations_by_id:
            continue
        key = (nation_id, unit_id)
        if key in seen:
            continue
        seen.add(key)
        nation = nations_by_id[nation_id]
        by_unit[unit_id].append(
            {
                "kind": "Pretender",
                "nation_id": nation_id,
                "nation": nation["name"],
                "era": nation["code"],
                "directory": nation["dir"],
                "slug": nation["slug"],
            }
        )
    return by_unit


def build_spell_summon_relations(
    spell_rows: list[dict[str, str]],
    effect_rows: list[dict[str, str]],
    attribute_rows: list[dict[str, str]],
    units: dict[int, dict[str, str]],
):
    spells = {num(row, "id"): row for row in spell_rows if row.get("id")}
    effects = effect_map(effect_rows)
    attrs = spell_attributes(attribute_rows)
    names = nation_names()
    by_unit: dict[int, list[dict[str, object]]] = defaultdict(list)
    seen: set[tuple[int, int, int]] = set()
    unresolved: list[tuple[int, str, int, int]] = []

    for root in spell_rows:
        school = num(root, "school", -1)
        root_id = num(root, "id")
        root_name = (root.get("name") or "").strip()
        if school not in SCHOOLS or not root_name or root_name in {"Nothing", "..."}:
            continue

        current = root
        visited: set[int] = set()
        while current:
            current_id = num(current, "id")
            if current_id in visited:
                break
            visited.add(current_id)
            effect = effects.get(num(current, "effect_record_id"))
            if effect:
                effect_number = num(effect, "effect_number")
                if effect_number in SUMMON_EFFECTS:
                    unit_id = num(effect, "raw_argument")
                    if unit_id > 0 and unit_id in units:
                        key = (root_id, current_id, unit_id)
                        if key not in seen:
                            seen.add(key)
                            by_unit[unit_id].append(
                                {
                                    "kind": "Spell",
                                    "spell_id": root_id,
                                    "effect_spell_id": current_id,
                                    "spell": root_name,
                                    "school": SCHOOLS[school][0],
                                    "school_slug": SCHOOLS[school][1],
                                    "level": num(root, "researchlevel"),
                                    "research": spell_research(root),
                                    "path": spell_path(root),
                                    "type": spell_kind(effect),
                                    "cost": spell_gem_cost(root, effect),
                                    "effect": SUMMON_EFFECTS[effect_number],
                                    "count_hint": max(1, num(current, "effects_count", 1)),
                                    "availability": spell_availability(root_id, attrs, names),
                                }
                            )
                    elif unit_id:
                        unresolved.append((root_id, root_name, effect_number, unit_id))
            next_id = num(current, "next_spell")
            current = spells.get(next_id) if next_id > 0 else None
    return by_unit, unresolved


def build_site_relations(
    rows: list[dict[str, str]],
    units: dict[int, dict[str, str]],
):
    by_unit: dict[int, list[dict[str, object]]] = defaultdict(list)
    seen: set[tuple[int, int, str]] = set()
    unresolved: list[tuple[int, str, str, int]] = []
    for row in rows:
        site_id = num(row, "id")
        site_name = (row.get("name") or "(unnamed site)").strip()
        for field, (source_label, role) in SITE_UNIT_FIELDS.items():
            unit_id = num(row, field)
            if unit_id <= 0:
                continue
            if unit_id not in units:
                unresolved.append((site_id, site_name, field, unit_id))
                continue
            key = (site_id, unit_id, field)
            if key in seen:
                continue
            seen.add(key)
            count = 1
            if field.startswith("sum"):
                suffix = field.removeprefix("sum")
                count = max(1, num(row, f"n_sum{suffix}", 1))
            by_unit[unit_id].append(
                {
                    "kind": "Magic Site",
                    "site_id": site_id,
                    "site": site_name,
                    "path": row.get("path") or "—",
                    "rarity": num(row, "rarity"),
                    "level": num(row, "level"),
                    "field": field,
                    "source": source_label,
                    "role": role,
                    "count_hint": count,
                }
            )
    return by_unit, unresolved


def build_mount_relations(units: dict[int, dict[str, str]]):
    riders_by_mount: dict[int, list[dict[str, object]]] = defaultdict(list)
    for rider_id, row in units.items():
        mount_id = num(row, "mountmnr")
        if mount_id > 0 and mount_id in units and mount_id != rider_id:
            riders_by_mount[mount_id].append(
                {
                    "rider_id": rider_id,
                    "rider": row.get("name") or "(unnamed)",
                }
            )
    return riders_by_mount


def build_shape_relations(units: dict[int, dict[str, str]]):
    outgoing: dict[int, list[dict[str, object]]] = defaultdict(list)
    incoming: dict[int, list[dict[str, object]]] = defaultdict(list)
    unresolved: list[tuple[int, str, str, int]] = []
    seen: set[tuple[int, int, str]] = set()
    for source_id, row in units.items():
        for field, label in SHAPE_FIELDS.items():
            target_id = num(row, field)
            if target_id <= 0 or target_id == source_id:
                continue
            if target_id not in units:
                unresolved.append((source_id, row.get("name") or "(unnamed)", field, target_id))
                continue
            key = (source_id, target_id, field)
            if key in seen:
                continue
            seen.add(key)
            relation = {
                "field": field,
                "label": label,
                "source_id": source_id,
                "source": row.get("name") or "(unnamed)",
                "target_id": target_id,
                "target": units[target_id].get("name") or "(unnamed)",
            }
            outgoing[source_id].append(relation)
            incoming[target_id].append(relation)
    return outgoing, incoming, unresolved


def merge_acquisitions(*sources):
    out: dict[int, list[dict[str, object]]] = defaultdict(list)
    for source_map in sources:
        for unit_id, relations in source_map.items():
            out[unit_id].extend(relations)
    return out


def load_unit_catalog(refresh: bool = False, offline: bool = False):
    paths, nation_rows = load_catalog_inputs(refresh, offline)
    units = unit_data(paths["BaseU.csv"])
    weapons, armors = equipment_indexes(paths)
    maps = load_recruit_maps(paths)

    recruit = build_recruit_relations(nation_rows, units, maps)
    heroes = build_hero_relations(tsv(paths["attributes_by_nation.csv"]), nation_rows, units)
    pretenders = build_pretender_relations(
        tsv(paths["pretender_types_by_nation.csv"]), nation_rows, units
    )
    spell_summons, unresolved_spells = build_spell_summon_relations(
        tsv(paths["spells.csv"]),
        tsv(paths["effects_spells.csv"]),
        tsv(paths["attributes_by_spell.csv"]),
        units,
    )
    sites, unresolved_sites = build_site_relations(tsv(paths["MagicSites.csv"]), units)
    riders_by_mount = build_mount_relations(units)
    shape_outgoing, shape_incoming, unresolved_shapes = build_shape_relations(units)
    acquisitions = merge_acquisitions(recruit, heroes, pretenders, spell_summons, sites)

    return {
        "commit": COMMIT,
        "paths": paths,
        "nations": nation_rows,
        "units": units,
        "weapons": weapons,
        "armors": armors,
        "maps": maps,
        "recruit": recruit,
        "heroes": heroes,
        "pretenders": pretenders,
        "spell_summons": spell_summons,
        "sites": sites,
        "acquisitions": acquisitions,
        "riders_by_mount": riders_by_mount,
        "shape_outgoing": shape_outgoing,
        "shape_incoming": shape_incoming,
        "unresolved_spells": unresolved_spells,
        "unresolved_sites": unresolved_sites,
        "unresolved_shapes": unresolved_shapes,
    }
