from __future__ import annotations

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


SPECIAL_SPELL_EFFECTS: dict[int, dict[str, str | None]] = {
    34: {"category": "Wish", "label": "Wish", "table": None},
    35: {"category": "Procedural summon", "label": "Cross Breeding", "table": None},
    68: {"category": "Procedural summon", "label": "Summon Animals", "table": None},
    76: {"category": "Procedural summon", "label": "Tartarian Gate", "table": None},
    89: {"category": "Unique summon pool", "label": "Unique commander", "table": "unique"},
    93: {"category": "Unique summon pool", "label": "Unique unit", "table": "unique"},
    98: {"category": "Procedural summon", "label": "Winged Monkeys", "table": None},
    100: {"category": "Terrain summon pool", "label": "Terrain-specific ritual summon", "table": "terrain"},
    114: {"category": "Procedural summon", "label": "Awaken Treelord", "table": None},
    120: {"category": "Procedural summon", "label": "Unleash Imprisoned Ones", "table": None},
    127: {"category": "Procedural summon", "label": "Infernal Breeding", "table": None},
    137: {"category": "Conditional summon", "label": "Summon if not dead", "table": None},
    141: {"category": "Procedural summon", "label": "Call the Birds of Splendour", "table": None},
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


def build_special_spell_relations(
    spell_rows: list[dict[str, str]],
    effect_rows: list[dict[str, str]],
    attribute_rows: list[dict[str, str]],
    unique_pool_rows: list[dict[str, str]],
    terrain_pool_rows: list[dict[str, str]],
):
    spells = {num(row, "id"): row for row in spell_rows if row.get("id")}
    effects = effect_map(effect_rows)
    attrs = spell_attributes(attribute_rows)
    names = nation_names()
    unique_pools = _pool_lookup(unique_pool_rows)
    terrain_pools = _pool_lookup(terrain_pool_rows)
    special_relations: list[dict[str, object]] = []
    random_relations: list[dict[str, object]] = []
    unresolved_special: list[tuple[int, str, int, int]] = []
    classified_standard: set[tuple[int, int, int]] = set()
    seen: set[tuple[int, int, int, int]] = set()

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

                    spec = SPECIAL_SPELL_EFFECTS.get(base_effect)
                    if spec:
                        table = spec.get("table")
                        pool = str(spec["label"])
                        confidence = "special-effect-no-fixed-unit"
                        if table == "unique":
                            pool = unique_pools.get(raw_argument, "")
                            confidence = "special-unique-table"
                        elif table == "terrain":
                            pool = terrain_pools.get(raw_argument, "")
                            confidence = "terrain-summon-table"
                        if table and not pool:
                            unresolved_special.append(
                                (root_id, root_name, base_effect, raw_argument)
                            )
                            pool = f"Unresolved pool {raw_argument}"
                            confidence = "unresolved-pool"
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
                                "confidence": confidence,
                            }
                        )
            next_id = num(current, "next_spell")
            current = spells.get(next_id) if next_id > 0 else None

    return {
        "special_relations": special_relations,
        "random_relations": random_relations,
        "unresolved_special": unresolved_special,
        "classified_standard": classified_standard,
        "unique_pools": unique_pools,
        "terrain_pools": terrain_pools,
    }
