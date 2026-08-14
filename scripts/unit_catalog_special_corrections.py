from __future__ import annotations

from generate_recruitment_data import num, tsv
from generate_spell_item_data import effect_map
from unit_catalog_generation import NEGATIVE_MONSTER_POOLS
from unit_catalog_special_data import (
    DIRECT_SPELL_EFFECTS,
    _base_effect_number,
    _spell_common,
    _spell_relation,
)


def _append_unique(mapping, key: int, relation: dict[str, object]) -> None:
    values = mapping.setdefault(key, [])
    marker = (
        int(relation.get("spell_id") or 0),
        int(relation.get("effect_spell_id") or 0),
        int(relation.get("target_id") or 0),
        str(relation.get("effect") or ""),
    )
    for existing in values:
        existing_marker = (
            int(existing.get("spell_id") or 0),
            int(existing.get("effect_spell_id") or 0),
            int(existing.get("target_id") or 0),
            str(existing.get("effect") or ""),
        )
        if existing_marker == marker:
            return
    values.append(relation)


def _add_candidate(
    data,
    common: dict[str, object],
    unit_id: int,
    effect_label: str,
    confidence: str,
    pool: str,
    count_hint: int = 1,
) -> None:
    if unit_id not in data["units"]:
        data["special_candidate_unresolved"].append(
            (
                int(common["spell_id"]),
                str(common["spell"]),
                int(common["effect_spell_id"]),
                unit_id,
            )
        )
        return
    marker = (
        int(common["spell_id"]),
        int(common["effect_spell_id"]),
        unit_id,
        effect_label,
    )
    for existing in data["spell_candidate_relations"]:
        existing_marker = (
            int(existing.get("spell_id") or 0),
            int(existing.get("effect_spell_id") or 0),
            int(existing.get("target_id") or 0),
            str(existing.get("effect") or ""),
        )
        if existing_marker == marker:
            return
    relation = _spell_relation(
        common,
        unit_id,
        effect_label,
        count_hint,
        confidence,
        pool,
    )
    data["spell_candidate_relations"].append(relation)
    _append_unique(data["spell_candidate_incoming"], unit_id, relation)
    _append_unique(data["spell_summons"], unit_id, relation)
    _append_unique(data["acquisitions"], unit_id, relation)


def _add_summary(
    data,
    common: dict[str, object],
    category: str,
    effect_number: int,
    raw_argument: int,
    pool: str,
    table: str,
    candidates: list[int],
    confidence: str,
) -> None:
    marker = (
        int(common["spell_id"]),
        int(common["effect_spell_id"]),
        effect_number,
        raw_argument,
        pool,
    )
    for existing in data["spell_special_relations"]:
        existing_marker = (
            int(existing.get("spell_id") or 0),
            int(existing.get("effect_spell_id") or 0),
            int(existing.get("base_effect_number") or 0),
            int(existing.get("raw_argument") or 0),
            str(existing.get("pool") or ""),
        )
        if existing_marker == marker:
            return
    data["spell_special_relations"].append(
        {
            **common,
            "kind": "Spell Special Summon",
            "category": category,
            "effect_number": effect_number,
            "base_effect_number": effect_number,
            "raw_argument": raw_argument,
            "pool": pool,
            "table": table,
            "candidates": candidates,
            "candidate_names": [
                data["units"][unit_id].get("name") or f"Unit {unit_id}"
                for unit_id in candidates
                if unit_id in data["units"]
            ],
            "confidence": confidence,
        }
    )


def _add_random(
    data,
    common: dict[str, object],
    effect_number: int,
    raw_argument: int,
) -> None:
    if raw_argument in NEGATIVE_MONSTER_POOLS:
        pool = NEGATIVE_MONSTER_POOLS[raw_argument]
        confidence = "negative-pool"
    elif raw_argument <= -1000:
        pool = f"Montag pool {abs(raw_argument)}"
        confidence = "montag"
    else:
        pool = f"Unmapped negative summon pool {raw_argument}"
        confidence = "negative-sentinel"
    marker = (
        int(common["spell_id"]),
        int(common["effect_spell_id"]),
        effect_number,
        raw_argument,
    )
    for existing in data["spell_random_targets"]:
        existing_marker = (
            int(existing.get("spell_id") or 0),
            int(existing.get("effect_spell_id") or 0),
            int(existing.get("effect_number") or 0),
            int(existing.get("raw_argument") or 0),
        )
        if existing_marker == marker:
            return
    data["spell_random_targets"].append(
        {
            **common,
            "kind": "Spell Random Summon",
            "effect_number": effect_number,
            "raw_argument": raw_argument,
            "pool": pool,
            "confidence": confidence,
        }
    )


def apply_special_corrections(data) -> None:
    """Apply display-logic corrections confirmed by SpellTables.js.

    The generic effects-info label for effect 34 is not used as Wish here.
    SpellTables.js renders Wish at effect 25 and explicitly expands several
    negative and named summon pools.
    """
    data["spell_special_relations"] = [
        relation
        for relation in data["spell_special_relations"]
        if int(relation.get("base_effect_number") or 0) != 34
    ]
    data["special_candidate_unresolved"] = []

    spell_rows = tsv(data["paths"]["spells.csv"])
    effects = effect_map(tsv(data["paths"]["effects_spells.csv"]))
    spells = {num(row, "id"): row for row in spell_rows if row.get("id")}

    # Existing helpers already built the metadata objects used by the pages.
    from generate_spell_item_data import nation_names, spell_attributes

    attrs = spell_attributes(tsv(data["paths"]["attributes_by_spell.csv"]))
    names = nation_names()

    named_negative = {
        -16: ("Yazads", list(data["explicit_named_summon_pools"].get("Yazads", []))),
        -17: ("Yatas", list(data["explicit_named_summon_pools"].get("Yatas", []))),
        -21: (
            "Dwarfs of the Four Directions",
            list(data["explicit_named_summon_pools"].get("Dwarfs of the Four Directions", [])),
        ),
    }

    for root in spell_rows:
        school = num(root, "school", -1)
        root_id = num(root, "id")
        root_name = (root.get("name") or "").strip()
        if school < 0 or not root_name or root_name in {"Nothing", "..."}:
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
                common = _spell_common(
                    root,
                    root_id,
                    root_name,
                    current_id,
                    effect,
                    attrs,
                    names,
                )

                if base_effect == 25:
                    _add_summary(
                        data,
                        common,
                        "Wish",
                        25,
                        raw_argument,
                        "Wish",
                        "—",
                        [],
                        "spelltables-effect-lookup",
                    )

                if base_effect in DIRECT_SPELL_EFFECTS and raw_argument < 0:
                    if raw_argument in named_negative and named_negative[raw_argument][1]:
                        pool, candidates = named_negative[raw_argument]
                        _add_summary(
                            data,
                            common,
                            "Explicit candidate pool",
                            base_effect,
                            raw_argument,
                            pool,
                            "SpellTables named array",
                            candidates,
                            "spelltables-named-array",
                        )
                        for unit_id in candidates:
                            _add_candidate(
                                data,
                                common,
                                unit_id,
                                f"Explicit candidate pool: {pool}",
                                "spelltables-named-array",
                                pool,
                            )
                    else:
                        _add_random(data, common, effect_number, raw_argument)

                if base_effect == 37 and current_id == 380 and raw_argument == 543:
                    pool = "Angelic Host"
                    candidates = list(data["explicit_named_summon_pools"].get(pool, []))
                    _add_summary(
                        data,
                        common,
                        "Explicit candidate pool",
                        base_effect,
                        raw_argument,
                        pool,
                        "SpellTables named array",
                        candidates,
                        "spelltables-spell-id-special-case",
                    )
                    for unit_id in candidates:
                        _add_candidate(
                            data,
                            common,
                            unit_id,
                            f"Explicit candidate pool: {pool}",
                            "spelltables-spell-id-special-case",
                            pool,
                        )

                if base_effect == 37 and current_id == 1081 and raw_argument == 303:
                    pool = "Horde from Hell"
                    candidates = list(data["explicit_named_summon_pools"].get(pool, []))
                    _add_summary(
                        data,
                        common,
                        "Explicit candidate pool",
                        base_effect,
                        raw_argument,
                        pool,
                        "SpellTables named array",
                        candidates,
                        "spelltables-spell-id-special-case",
                    )
                    for unit_id in candidates:
                        _add_candidate(
                            data,
                            common,
                            unit_id,
                            f"Explicit candidate pool: {pool}",
                            "spelltables-spell-id-special-case",
                            pool,
                        )

                if base_effect == 81 and num(current, "damage") == 43:
                    pool = "Ghost Ship Armada"
                    candidates = list(data["explicit_named_summon_pools"].get(pool, []))
                    _add_summary(
                        data,
                        common,
                        "Explicit candidate pool",
                        base_effect,
                        raw_argument,
                        pool,
                        "SpellTables named array",
                        candidates,
                        "spelltables-damage-special-case",
                    )
                    for unit_id in candidates:
                        _add_candidate(
                            data,
                            common,
                            unit_id,
                            f"Explicit candidate pool: {pool}",
                            "spelltables-damage-special-case",
                            pool,
                        )
            next_id = num(current, "next_spell")
            current = spells.get(next_id) if next_id > 0 else None
