from __future__ import annotations

from collections import defaultdict

from generate_recruitment_data import source, tsv
from unit_catalog_event_data import build_event_relations, build_mercenary_relations
from unit_catalog_generation_integration import load_unit_catalog as load_base_unit_catalog


def _merge_acquisitions(base, *extra_sources):
    merged: dict[int, list[dict[str, object]]] = defaultdict(list)
    for unit_id, relations in base.items():
        merged[unit_id].extend(relations)
    for source_map in extra_sources:
        for unit_id, relations in source_map.items():
            merged[unit_id].extend(relations)
    return merged


def _normalize_event_relations(events: dict[str, object]) -> None:
    """Clarify event-only sentinels, ownership and lifetime semantics."""
    sentinel_relations = []
    for relation in events["relations"]:
        kind = relation.get("kind")
        if kind == "Event Combat":
            relation["owner"] = "Event combat side / attacker"
            relation["temporary"] = "Combat participant; no ownership grant"
        elif kind == "Event Transform":
            relation["owner"] = "Selected Event target"
            relation["temporary"] = "Transformation result; see Event chain"

        # Vanilla uses `assassin -1` in several unrelated adventure/site
        # events. The concrete attacker is context-dependent, so raw -1 is an
        # Event sentinel/pool, not a fixed Unit or a standard negative monster
        # number that should be guessed from the surrounding description.
        if int(relation.get("raw_target") or 0) != -1:
            continue
        if relation.get("confidence") != "unresolved":
            continue
        relation["target"] = "Event-defined attacker pool / sentinel (raw -1)"
        relation["confidence"] = "event-sentinel"
        sentinel_relations.append(relation)

    if sentinel_relations:
        events["random_targets"].extend(sentinel_relations)
        events["unresolved"] = [
            entry for entry in events["unresolved"] if int(entry[3]) != -1
        ]


def load_unit_catalog(refresh: bool = False, offline: bool = False):
    data = load_base_unit_catalog(refresh, offline)

    events_path = source("events.csv", refresh, offline)
    mercenaries_path = source("Mercenary.csv", refresh, offline)
    data["paths"]["events.csv"] = events_path
    data["paths"]["Mercenary.csv"] = mercenaries_path

    events = build_event_relations(
        tsv(events_path),
        data["units"],
        data["nations"],
    )
    _normalize_event_relations(events)

    mercenaries = build_mercenary_relations(
        tsv(mercenaries_path),
        data["units"],
    )

    data["event_incoming"] = events["incoming"]
    data["event_relations"] = events["relations"]
    data["event_random_targets"] = events["random_targets"]
    data["event_unresolved"] = events["unresolved"]
    data["event_field_counts"] = events["field_counts"]
    data["events_with_unit_effects"] = events["events_with_unit_effects"]

    data["mercenary_incoming"] = mercenaries["incoming"]
    data["mercenary_relations"] = mercenaries["relations"]
    data["mercenary_unresolved"] = mercenaries["unresolved"]
    data["mercenary_companies"] = mercenaries["companies"]

    # Event combatants are included as confirmed appearance routes, not as a
    # claim that the player permanently controls them. Unit pages preserve
    # owner and lifetime semantics for every Event relation.
    data["acquisitions"] = _merge_acquisitions(
        data["acquisitions"],
        events["incoming"],
        mercenaries["incoming"],
    )
    return data
