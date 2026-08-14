from __future__ import annotations

import re
from collections import defaultdict

from generate_recruitment_data import num
from unit_catalog_generation import NEGATIVE_MONSTER_POOLS


EVENT_RARITY = {
    0: "Always",
    1: "Common bad",
    2: "Uncommon bad",
    -1: "Common good",
    -2: "Uncommon good",
    10: "Always global",
    11: "Common global",
    12: "Uncommon global",
    13: "Immediate global",
}


EXACT_EVENT_EFFECTS: dict[str, tuple[str, str, str]] = {
    "com": ("Event Spawn", "Commander", "1"),
    "stealthcom": ("Event Spawn", "Stealth commander", "1"),
    "assassin": ("Event Combat", "Assassin attacker", "1"),
    "transform": ("Event Transform", "Transform", "1 target"),
    "forcetransform": ("Event Transform", "Forced transform", "1 target"),
    "assfollower1": ("Event Combat", "Assassin follower", "1"),
    "assfollower1d3": ("Event Combat", "Assassin follower", "1d3"),
    "assfollower2": ("Event Combat", "Assassin follower", "2"),
    "assfollower3": ("Event Combat", "Assassin follower", "3"),
}


def split_event_tokens(raw: str) -> list[tuple[str, list[str]]]:
    out: list[tuple[str, list[str]]] = []
    for token in (raw or "").split("|"):
        token = token.strip()
        if not token:
            continue
        parts = token.split()
        out.append((parts[0], parts[1:]))
    return out


def _integer(value: object, default: int = 0) -> int:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return default


def _effect_spec(field: str) -> tuple[str, str, str] | None:
    if field in EXACT_EVENT_EFFECTS:
        return EXACT_EVENT_EFFECTS[field]

    commander = re.fullmatch(r"(?P<count>\d+)com", field)
    if commander:
        return ("Event Spawn", "Commander", commander.group("count"))

    troops = re.fullmatch(r"(?P<amount>\d+(?:d\d+)?)units?", field)
    if troops:
        return ("Event Spawn", "Troop", troops.group("amount"))
    return None


def _target_text(raw_target: int, units: dict[int, dict[str, str]]) -> tuple[str, str]:
    if raw_target in units:
        return (units[raw_target].get("name") or "(unnamed)", "fixed-unit")
    if raw_target in NEGATIVE_MONSTER_POOLS:
        return (NEGATIVE_MONSTER_POOLS[raw_target], "negative-pool")
    if raw_target <= -1000:
        return (f"Montag pool {abs(raw_target)}", "montag")
    return (f"Unresolved target {raw_target}", "unresolved")


def _owner_text(raw_owner: int | None, nations: dict[int, dict[str, object]]) -> str:
    if raw_owner is None:
        return "Event recipient / current owner"
    if raw_owner == -2:
        return "Province owner"
    if raw_owner == -1:
        return "Random enemy"
    nation = nations.get(raw_owner)
    if nation:
        return f"{nation['code']} {nation['name']} (Nation {raw_owner})"
    return f"Nation {raw_owner}"


def _temporary_text(tokens: list[tuple[str, list[str]]]) -> str:
    values = [values[0] for key, values in tokens if key == "tempunits" and values]
    if not values:
        return "Default / normally permanent"
    return "Temporary" if _integer(values[-1]) else "Permanent"


def build_event_relations(
    rows: list[dict[str, str]],
    units: dict[int, dict[str, str]],
    nation_rows: list[dict[str, object]],
):
    nations = {int(row["id"]): row for row in nation_rows}
    incoming: dict[int, list[dict[str, object]]] = defaultdict(list)
    relations: list[dict[str, object]] = []
    random_targets: list[dict[str, object]] = []
    unresolved: list[tuple[int, str, str, int]] = []
    field_counts: dict[str, int] = defaultdict(int)
    event_ids: set[int] = set()
    seen: set[tuple[int, str, int, int]] = set()

    for row in rows:
        event_id = num(row, "id", -1)
        if event_id < 0:
            continue
        event_name = (row.get("name") or f"Event {event_id}").strip()
        description = (row.get("description") or "").strip()
        effect_tokens = split_event_tokens(row.get("effects") or "")
        owner_values = [
            _integer(values[0])
            for key, values in effect_tokens
            if key == "nation" and values
        ]
        raw_owner = owner_values[-1] if owner_values else None
        owner = _owner_text(raw_owner, nations)
        temporary = _temporary_text(effect_tokens)
        rarity = num(row, "rarity")
        rarity_text = EVENT_RARITY.get(rarity, str(rarity))
        requirements = (row.get("requirements") or "").strip()

        for position, (field, values) in enumerate(effect_tokens):
            spec = _effect_spec(field)
            if spec is None or not values:
                continue
            raw_target = _integer(values[0])
            if raw_target == 0:
                continue
            key = (event_id, field, raw_target, position)
            if key in seen:
                continue
            seen.add(key)
            kind, category, amount = spec
            target, confidence = _target_text(raw_target, units)
            relation = {
                "kind": kind,
                "category": category,
                "event_id": event_id,
                "event": event_name,
                "description": description,
                "rarity": rarity,
                "rarity_text": rarity_text,
                "requirements": requirements,
                "effects": row.get("effects") or "",
                "field": field,
                "amount": amount,
                "owner": owner,
                "raw_owner": raw_owner,
                "temporary": temporary,
                "target_id": raw_target if raw_target in units else 0,
                "target": target,
                "raw_target": raw_target,
                "confidence": confidence,
            }
            relations.append(relation)
            field_counts[field] += 1
            event_ids.add(event_id)
            if raw_target in units:
                incoming[raw_target].append(relation)
            elif confidence in {"negative-pool", "montag"}:
                random_targets.append(relation)
            else:
                unresolved.append((event_id, event_name, field, raw_target))

    return {
        "incoming": incoming,
        "relations": relations,
        "random_targets": random_targets,
        "unresolved": unresolved,
        "field_counts": dict(sorted(field_counts.items())),
        "events_with_unit_effects": len(event_ids),
    }


def _era_mask(mask: int) -> str:
    eras = []
    if mask & 1:
        eras.append("EA")
    if mask & 2:
        eras.append("MA")
    if mask & 4:
        eras.append("LA")
    return "/".join(eras) or "—"


def build_mercenary_relations(
    rows: list[dict[str, str]],
    units: dict[int, dict[str, str]],
):
    incoming: dict[int, list[dict[str, object]]] = defaultdict(list)
    relations: list[dict[str, object]] = []
    unresolved: list[tuple[int, str, str, int]] = []
    companies: set[int] = set()

    for row in rows:
        mercenary_id = num(row, "id", -1)
        if mercenary_id < 0:
            continue
        company = (row.get("name") or f"Mercenary {mercenary_id}").strip()
        boss = (row.get("bossname") or "").strip()
        common = {
            "kind": "Mercenary",
            "mercenary_id": mercenary_id,
            "company": company,
            "boss": boss,
            "level": num(row, "level"),
            "minmen": num(row, "minmen"),
            "minpay": num(row, "minpay"),
            "xp": num(row, "xp"),
            "recruit_rate": num(row, "recrate"),
            "random_equipment": num(row, "randequip"),
            "item1": (row.get("item1") or "").strip(),
            "item2": (row.get("item2") or "").strip(),
            "era": _era_mask(num(row, "eramask")),
            "confidence": "explicit-mercenary-table",
        }

        candidates = (
            ("Commander", num(row, "com"), 1),
            ("Troop", num(row, "unit"), num(row, "nrunits")),
        )
        for role, unit_id, count in candidates:
            if unit_id <= 0 or (role == "Troop" and count <= 0):
                continue
            relation = dict(common)
            relation.update(
                {
                    "category": role,
                    "target_id": unit_id if unit_id in units else 0,
                    "target": units.get(unit_id, {}).get("name") or f"Unresolved target {unit_id}",
                    "raw_target": unit_id,
                    "count": count,
                }
            )
            relations.append(relation)
            companies.add(mercenary_id)
            if unit_id in units:
                incoming[unit_id].append(relation)
            else:
                unresolved.append((mercenary_id, company, role, unit_id))

    return {
        "incoming": incoming,
        "relations": relations,
        "unresolved": unresolved,
        "companies": len(companies),
    }
