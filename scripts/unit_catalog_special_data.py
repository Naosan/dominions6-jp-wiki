from __future__ import annotations

import re
from collections import defaultdict

from generate_recruitment_data import num
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
from unit_catalog_generation import NEGATIVE_MONSTER_POOLS
from unit_catalog_sources import SUMMON_EFFECTS


ITEM_UNIT_FIELDS: dict[str, dict[str, object]] = {
    "sumrit": {
        "kind": "Item Summon",
        "category": "Ritual summon",
        "count_field": "#sumrit",
        "timing": "Item-provided ritual / special action",
    },
    "sumauto": {
        "kind": "Item Summon",
        "category": "Automatic summon",
        "count_field": "#sumauto",
        "timing": "Automatic item summon",
    },
    "sumbat": {
        "kind": "Item Battle Spawn",
        "category": "Battle summon",
        "count_field": "#sumbat",
        "timing": "Battle; exact cadence is item-defined",
    },
    "retinue": {
        "kind": "Item Summon",
        "category": "Retinue",
        "amount": "1",
        "timing": "Item retinue",
    },
    "summoner1d6": {
        "kind": "Item Summon",
        "category": "Summoner 1d6",
        "amount": "1d6",
        "timing": "Item summon ability",
    },
    "summoner2d6": {
        "kind": "Item Summon",
        "category": "Summoner 2d6",
        "amount": "2d6",
        "timing": "Item summon ability",
    },
    "batstartsum2": {
        "kind": "Item Battle Spawn",
        "category": "Battle-start summon",
        "amount": "2",
        "timing": "Start of battle",
    },
    "batstartsum3": {
        "kind": "Item Battle Spawn",
        "category": "Battle-start summon",
        "amount": "3",
        "timing": "Start of battle",
    },
    "batstartsum5d6": {
        "kind": "Item Battle Spawn",
        "category": "Battle-start summon",
        "amount": "5d6",
        "timing": "Start of battle",
    },
    "transformwearer": {
        "kind": "Item Transform",
        "category": "Transform wearer",
        "amount": "1 wearer",
        "timing": "Item-defined transformation",
    },
    "raiseshape": {
        "kind": "Item Transform",
        "category": "Raised shape",
        "amount": "1 wearer",
        "timing": "Raise / return form",
    },
    "defender": {
        "kind": "Item Encounter",
        "category": "May be attacked by",
        "amount": "1 encounter",
        "timing": "Item-defined hostile encounter",
    },
}


# These effects call show_summon() with raw_argument in the pinned
# Dom6 Inspector SpellTables.js. Effects already handled by SUMMON_EFFECTS
# are excluded at runtime to avoid duplicate relations.
DIRECT_SPELL_EFFECTS: dict[int, tuple[str, int | None]] = {
    21: ("Summon commander", None),
    26: ("Summon", None),
    37: ("Farsummon", None),
    38: ("Independent farsummon", None),
    50: ("Summon", None),
    54: ("Summon", None),
    62: ("Summon", None),
    93: ("Ritual summon unique unit", None),
    119: ("Summon", None),
    130: ("Summon", None),
    137: ("Summon if not dead", None),
    141: ("Call the Birds of Splendour", 2),
}


SPECIAL_SPELL_EFFECTS: dict[int, dict[str, str | None]] = {
    34: {"category": "Wish", "label": "Wish", "table": None},
    35: {"category": "Procedural summon", "label": "Cross Breeding", "table": None},
    68: {"category": "Procedural summon", "label": "Summon Animals", "table": None},
    76: {"category": "Explicit candidate pool", "label": "Tartarian Gate", "table": "tartarian"},
    89: {"category": "Unique summon pool", "label": "Unique commander", "table": "unique"},
    98: {"category": "Procedural summon", "label": "Winged Monkeys", "table": None},
    100: {"category": "Terrain summon pool", "label": "Terrain-specific ritual summon", "table": "terrain"},
    114: {"category": "Unique summon pool", "label": "Awaken Treelord", "table": "unique"},
    120: {"category": "Explicit candidate pool", "label": "Unleash Imprisoned Ones", "table": "unleash"},
    127: {"category": "Procedural summon", "label": "Infernal Breeding", "table": None},
}


def _integer(value: object, default: int = 0) -> int:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return default


def _item_path(row: dict[str, str]) -> str:
    parts: list[str] = []
    for path_field, level_field in (
        ("mainpath", "mainlevel"),
        ("secondarypath", "secondarylevel"),
    ):
        path = (row.get(path_field) or "").strip()
        level = num(row, level_field)
        if path and level > 0:
            parts.append(f"{path}{level}")
    return "".join(parts) or "—"


def _construction(row: dict[str, str]) -> str:
    level = num(row, "constlevel")
    return "Unforgeable" if level == 12 else f"Construction {level}"


def _amount(row: dict[str, str], spec: dict[str, object]) -> str:
    if spec.get("amount") is not None:
        return str(spec["amount"])
    count_field = str(spec.get("count_field") or "")
    if count_field:
        return str(max(1, num(row, count_field, 1)))
    return "1"


def _target_text(raw_target: int, units: dict[int, dict[str, str]]) -> tuple[str, str]:
    if raw_target in units:
        return (units[raw_target].get("name") or "(unnamed)", "fixed-unit")
    if raw_target in NEGATIVE_MONSTER_POOLS:
        return (NEGATIVE_MONSTER_POOLS[raw_target], "negative-pool")
    if raw_target <= -1000:
        return (f"Montag pool {abs(raw_target)}", "montag")
    if raw_target < 0:
        return (f"Unmapped negative item target {raw_target}", "negative-sentinel")
    return (f"Unresolved target {raw_target}", "unresolved")


def build_item_unit_relations(
    rows: list[dict[str, str]],
    units: dict[int, dict[str, str]],
):
    incoming: dict[int, list[dict[str, object]]] = defaultdict(list)
    relations: list[dict[str, object]] = []
    random_targets: list[dict[str, object]] = []
    unresolved: list[tuple[int, str, str, int]] = []
    field_counts: dict[str, int] = defaultdict(int)
    item_ids: set[int] = set()
    arena_items: list[dict[str, object]] = []

    for row in rows:
        item_id = num(row, "id", -1)
        if item_id < 0:
            continue
        item_name = (row.get("name") or f"Item {item_id}").strip()
        common = {
            "item_id": item_id,
            "item": item_name,
            "item_type": (row.get("type") or "—").strip(),
            "construction": _construction(row),
            "forge_path": _item_path(row),
            "confidence": "explicit-item-field",
        }

        if num(row, "arenareward") or num(row, "mustfightinarena"):
            arena_items.append(
                {
                    **common,
                    "arena_reward": num(row, "arenareward"),
                    "must_fight": num(row, "mustfightinarena"),
                }
            )

        for field, spec in ITEM_UNIT_FIELDS.items():
            raw_target = num(row, field)
            if raw_target == 0:
                continue
            target, confidence = _target_text(raw_target, units)
            kind = str(spec["kind"])
            owner = "Item bearer / controller"
            lifetime = "Item-defined; verify the in-game description"
            if kind == "Item Battle Spawn":
                owner = "Item bearer side"
                lifetime = "Battle participant; item-defined duration"
            elif kind == "Item Transform":
                owner = "Item bearer"
                lifetime = "Transformation / raised form"
            elif kind == "Item Encounter":
                owner = "Hostile encounter / opposing side"
                lifetime = "Encounter participant; no ownership grant"

            relation = {
                **common,
                "kind": kind,
                "category": str(spec["category"]),
                "field": field,
                "amount": _amount(row, spec),
                "timing": str(spec["timing"]),
                "owner": owner,
                "lifetime": lifetime,
                "target_id": raw_target if raw_target in units else 0,
                "target": target,
                "raw_target": raw_target,
                "confidence": confidence,
            }
            relations.append(relation)
            field_counts[field] += 1
            item_ids.add(item_id)
            if raw_target in units:
                incoming[raw_target].append(relation)
            elif confidence in {"negative-pool", "montag", "negative-sentinel"}:
                random_targets.append(relation)
            else:
                unresolved.append((item_id, item_name, field, raw_target))

    return {
        "incoming": incoming,
        "relations": relations,
        "random_targets": random_targets,
        "unresolved": unresolved,
        "field_counts": dict(sorted(field_counts.items())),
        "items_with_relations": len(item_ids),
        "arena_items": arena_items,
    }


def _pool_lookup(rows: list[dict[str, str]]) -> dict[int, str]:
    return {
        num(row, "number"): (row.get("name") or "(unnamed pool)").strip()
        for row in rows
        if num(row, "number") > 0
    }


def _numbers(raw: str) -> list[int]:
    return [int(value) for value in re.findall(r"-?\d+", raw)]


def _named_array(js_text: str, name: str) -> list[int]:
    match = re.search(
        rf"MSpell\.{re.escape(name)}\s*=\s*\[(.*?)\]\s*;",
        js_text,
        re.DOTALL,
    )
    return _numbers(match.group(1)) if match else []


def _object_arrays(js_text: str, name: str) -> tuple[dict[int, list[int]], dict[int, str]]:
    match = re.search(
        rf"MSpell\.{re.escape(name)}\s*=\s*\{{(.*?)\n\}}",
        js_text,
        re.DOTALL,
    )
    if not match:
        return {}, {}
    arrays: dict[int, list[int]] = {}
    labels: dict[int, str] = {}
    entry_pattern = re.compile(
        r"(-?\d+)\s*:\s*(?:/\*\s*(.*?)\s*\*/\s*)?\[(.*?)\]",
        re.DOTALL,
    )
    for entry in entry_pattern.finditer(match.group(1)):
        key = int(entry.group(1))
        label = re.sub(r"\s+", " ", (entry.group(2) or "").strip())
        arrays[key] = _numbers(entry.group(3))
        if label:
            labels[key] = label
    return arrays, labels


def parse_spell_tables(js_text: str, unique_pool_rows: list[dict[str, str]]):
    unique, unique_labels = _object_arrays(js_text, "uniqueSummon")
    terrain, terrain_labels = _object_arrays(js_text, "terrainSummon")
    csv_labels = _pool_lookup(unique_pool_rows)
    unique_names = {
        key: unique_labels.get(key) or csv_labels.get(key) or f"Unique summon pool {key}"
        for key in sorted(set(unique) | set(csv_labels))
    }
    terrain_names = {
        key: terrain_labels.get(key) or f"Terrain summon pool {key}"
        for key in terrain
    }
    return {
        "unique": unique,
        "unique_names": unique_names,
        "terrain": terrain,
        "terrain_names": terrain_names,
        "tartarian": _named_array(js_text, "tartarianGate"),
        "unleash": _named_array(js_text, "unleashImprisonedOnes"),
        "dwarfs": _named_array(js_text, "dwarfs"),
        "yazads": _named_array(js_text, "yazads"),
        "yatas": _named_array(js_text, "yatas"),
        "angelic_host": _named_array(js_text, "angelichost"),
        "horde_from_hell": _named_array(js_text, "hordefromhell"),
        "ghost_ship_armada": _named_array(js_text, "ghostShipArmada"),
    }


def _base_effect_number(effect_number: int) -> int:
    return effect_number - 10000 if effect_number >= 10000 else effect_number


def _spell_common(
    root: dict[str, str],
    root_id: int,
    root_name: str,
    effect_spell_id: int,
    effect: dict[str, str],
    attrs,
    names,
) -> dict[str, object]:
    school = num(root, "school", -1)
    return {
        "spell_id": root_id,
        "effect_spell_id": effect_spell_id,
        "spell": root_name,
        "school": SCHOOLS[school][0],
        "school_slug": SCHOOLS[school][1],
        "level": num(root, "researchlevel"),
        "research": spell_research(root),
        "path": spell_path(root),
        "type": spell_kind(effect),
        "cost": spell_gem_cost(root, effect),
        "availability": spell_availability(root_id, attrs, names),
    }


def _spell_relation(
    common: dict[str, object],
    unit_id: int,
    effect_label: str,
    count_hint: int,
    confidence: str,
    pool: str = "—",
) -> dict[str, object]:
    return {
        **common,
        "kind": "Spell",
        "effect": effect_label,
        "count_hint": max(1, count_hint),
        "confidence": confidence,
        "pool": pool,
        "target_id": unit_id,
    }


def _candidate_pool(
    table: str,
    raw_argument: int,
    tables: dict[str, object],
) -> tuple[str, list[int], str]:
    if table == "unique":
        if raw_argument == -21:
            return (
                "Dwarfs of the Four Directions",
                list(tables["dwarfs"]),
                "spelltables-named-array",
            )
        unique = tables["unique"]
        names = tables["unique_names"]
        return (
            str(names.get(raw_argument) or f"Unique summon pool {raw_argument}"),
            list(unique.get(raw_argument, [])),
            "spelltables-unique-pool",
        )
    if table == "terrain":
        terrain = tables["terrain"]
        names = tables["terrain_names"]
        return (
            str(names.get(raw_argument) or f"Terrain summon pool {raw_argument}"),
            list(terrain.get(raw_argument, [])),
            "spelltables-terrain-pool",
        )
    if table == "tartarian":
        return ("Tartarian Gate candidates", list(tables["tartarian"]), "spelltables-named-array")
    if table == "unleash":
        return (
            "Unleash Imprisoned Ones candidates",
            list(tables["unleash"]),
            "spelltables-named-array",
        )
    return ("", [], "unresolved-pool")


def build_special_spell_relations(
    spell_rows: list[dict[str, str]],
    effect_rows: list[dict[str, str]],
    attribute_rows: list[dict[str, str]],
    unique_pool_rows: list[dict[str, str]],
    terrain_pool_rows: list[dict[str, str]],
    spell_tables_js: str,
    units: dict[int, dict[str, str]],
):
    spells = {num(row, "id"): row for row in spell_rows if row.get("id")}
    effects = effect_map(effect_rows)
    attrs = spell_attributes(attribute_rows)
    names = nation_names()
    tables = parse_spell_tables(spell_tables_js, unique_pool_rows)
    csv_terrain_names = _pool_lookup(terrain_pool_rows)
    for key, value in csv_terrain_names.items():
        tables["terrain_names"].setdefault(key, value)

    candidate_incoming: dict[int, list[dict[str, object]]] = defaultdict(list)
    candidate_relations: list[dict[str, object]] = []
    special_relations: list[dict[str, object]] = []
    random_relations: list[dict[str, object]] = []
    unresolved_special: list[tuple[int, str, int, int]] = []
    unresolved_candidates: list[tuple[int, str, int, int]] = []
    classified_standard: set[tuple[int, int, int]] = set()
    seen: set[tuple[int, int, int, int]] = set()
    seen_candidates: set[tuple[int, int, int]] = set()

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
                base_effect = _base_effect_number(effect_number)
                raw_argument = num(effect, "raw_argument")
                key = (root_id, current_id, effect_number, raw_argument)
                if key not in seen:
                    seen.add(key)
                    common = _spell_common(
                        root,
                        root_id,
                        root_name,
                        current_id,
                        effect,
                        attrs,
                        names,
                    )

                    if effect_number in SUMMON_EFFECTS and raw_argument < 0:
                        if raw_argument in NEGATIVE_MONSTER_POOLS:
                            pool = NEGATIVE_MONSTER_POOLS[raw_argument]
                            confidence = "negative-pool"
                        elif raw_argument <= -1000:
                            pool = f"Montag pool {abs(raw_argument)}"
                            confidence = "montag"
                        else:
                            pool = f"Unmapped negative summon pool {raw_argument}"
                            confidence = "negative-sentinel"
                        random_relations.append(
                            {
                                **common,
                                "kind": "Spell Random Summon",
                                "effect_number": effect_number,
                                "raw_argument": raw_argument,
                                "pool": pool,
                                "confidence": confidence,
                            }
                        )
                        classified_standard.add((root_id, effect_number, raw_argument))

                    direct = DIRECT_SPELL_EFFECTS.get(base_effect)
                    if direct and effect_number not in SUMMON_EFFECTS:
                        label, forced_count = direct
                        if raw_argument > 0 and raw_argument in units:
                            relation = _spell_relation(
                                common,
                                raw_argument,
                                label,
                                forced_count or max(1, num(current, "effects_count", 1)),
                                "spelltables-show-summon",
                            )
                            candidate_key = (root_id, current_id, raw_argument)
                            if candidate_key not in seen_candidates:
                                seen_candidates.add(candidate_key)
                                candidate_incoming[raw_argument].append(relation)
                                candidate_relations.append(relation)
                        elif raw_argument:
                            unresolved_candidates.append(
                                (root_id, root_name, base_effect, raw_argument)
                            )

                    spec = SPECIAL_SPELL_EFFECTS.get(base_effect)
                    if spec:
                        table = str(spec.get("table") or "")
                        pool = str(spec["label"])
                        candidates: list[int] = []
                        confidence = "special-effect-no-fixed-unit"
                        if table:
                            pool, candidates, confidence = _candidate_pool(
                                table,
                                raw_argument,
                                tables,
                            )
                            if not candidates:
                                unresolved_special.append(
                                    (root_id, root_name, base_effect, raw_argument)
                                )
                                if not pool:
                                    pool = f"Unresolved pool {raw_argument}"
                                confidence = "unresolved-pool"

                        resolved_candidates: list[int] = []
                        candidate_names: list[str] = []
                        for unit_id in candidates:
                            if unit_id not in units:
                                unresolved_candidates.append(
                                    (root_id, root_name, base_effect, unit_id)
                                )
                                continue
                            resolved_candidates.append(unit_id)
                            candidate_names.append(
                                units[unit_id].get("name") or f"Unit {unit_id}"
                            )
                            candidate_key = (root_id, current_id, unit_id)
                            if candidate_key in seen_candidates:
                                continue
                            seen_candidates.add(candidate_key)
                            relation = _spell_relation(
                                common,
                                unit_id,
                                f"{spec['category']}: {pool}",
                                1,
                                confidence,
                                pool,
                            )
                            candidate_incoming[unit_id].append(relation)
                            candidate_relations.append(relation)

                        special_relations.append(
                            {
                                **common,
                                "kind": "Spell Special Summon",
                                "category": str(spec["category"]),
                                "effect_number": effect_number,
                                "base_effect_number": base_effect,
                                "raw_argument": raw_argument,
                                "pool": pool,
                                "table": table or "—",
                                "candidates": resolved_candidates,
                                "candidate_names": candidate_names,
                                "confidence": confidence,
                            }
                        )
            next_id = num(current, "next_spell")
            current = spells.get(next_id) if next_id > 0 else None

    return {
        "candidate_incoming": candidate_incoming,
        "candidate_relations": candidate_relations,
        "special_relations": special_relations,
        "random_relations": random_relations,
        "unresolved_special": unresolved_special,
        "unresolved_candidates": unresolved_candidates,
        "classified_standard": classified_standard,
        "unique_pools": tables["unique_names"],
        "unique_pool_units": tables["unique"],
        "terrain_pools": tables["terrain_names"],
        "terrain_pool_units": tables["terrain"],
        "explicit_named_pools": {
            "Tartarian Gate": tables["tartarian"],
            "Unleash Imprisoned Ones": tables["unleash"],
            "Dwarfs of the Four Directions": tables["dwarfs"],
            "Yazads": tables["yazads"],
            "Yatas": tables["yatas"],
            "Angelic Host": tables["angelic_host"],
            "Horde from Hell": tables["horde_from_hell"],
            "Ghost Ship Armada": tables["ghost_ship_armada"],
        },
    }