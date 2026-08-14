from __future__ import annotations

from collections import defaultdict

from generate_recruitment_data import num
from unit_catalog_generation import NATION_GENERATION_COMMANDS, _target_text


# attribute_keys.csv still labels these records as unknown in the pinned
# Dominions 6.35 extraction.  The mapping below is deliberately limited to
# vanilla attributes whose command can be identified from the nations carrying
# them and the command/nation combinations documented by Illwinter.
#
# Keep the raw attribute number in every generated relation: these are
# snapshot-specific IDs and must be revalidated when the pinned data changes.
VERIFIED_VANILLA_NATION_ATTRIBUTES: dict[int, str] = {
    69: "manikinreanim",       # MA Asphodel
    205: "undeadreanim",       # EA Therodos, MA Ermor, LA Lemuria
    210: "priestreanim",       # nations with priest reanimation
    324: "guardspirit",        # fixed/negative Monster Number target
    694: "autoundead",         # MA Ermor, LA Lemuria
    697: "tombwyrmreanim",     # LA C'tis
    698: "horsereanim",        # MA Ermor, MA Sceleria
    699: "wightreanim",        # MA Ermor
    700: "supayareanim",       # MA Nazca
    701: "greekreanim",        # EA Therodos
    702: "ghostreanim",        # LA Lemuria
}


def augment_nation_generation(
    existing: dict[str, object],
    attribute_rows: list[dict[str, str]],
    nation_rows: list[dict[str, object]],
    units: dict[int, dict[str, str]],
) -> dict[str, object]:
    abilities = list(existing.get("abilities", []))
    incoming: dict[int, list[dict[str, object]]] = defaultdict(list)
    for unit_id, relations in dict(existing.get("incoming", {})).items():
        incoming[int(unit_id)].extend(relations)
    unresolved = list(existing.get("unresolved", []))
    commands = dict(existing.get("attribute_commands", {}))
    commands.update(VERIFIED_VANILLA_NATION_ATTRIBUTES)

    nations = {int(row["id"]): row for row in nation_rows}
    seen = {
        (
            int(relation["nation_id"]),
            int(relation["attribute"]),
            int(relation["raw_value"]),
        )
        for relation in abilities
    }

    for row in attribute_rows:
        nation_id = num(row, "nation_number")
        attribute = num(row, "attribute")
        raw = num(row, "raw_value")
        command = VERIFIED_VANILLA_NATION_ATTRIBUTES.get(attribute, "")
        if command not in NATION_GENERATION_COMMANDS or nation_id not in nations:
            continue
        key = (nation_id, attribute, raw)
        if key in seen:
            continue
        seen.add(key)

        nation = nations[nation_id]
        category, description = NATION_GENERATION_COMMANDS[command]
        relation: dict[str, object] = {
            "kind": "Nation Spawn" if command == "guardspirit" else "Nation Ability",
            "category": category,
            "command": command,
            "attribute": attribute,
            "raw_value": raw,
            "nation_id": nation_id,
            "nation": nation["name"],
            "era": nation["code"],
            "directory": nation["dir"],
            "slug": nation["slug"],
            "description": description,
            "target_id": 0,
            "target": "—",
            "confidence": "verified-vanilla-attribute",
        }

        if command == "guardspirit":
            target, target_confidence = _target_text(raw, units)
            relation["target"] = target
            relation["confidence"] = (
                "verified-vanilla-attribute / " + target_confidence
            )
            if raw in units:
                relation["target_id"] = raw
                incoming[raw].append(relation)
            elif target_confidence == "unresolved":
                unresolved.append(
                    (nation_id, str(nation["name"]), command, raw)
                )

        abilities.append(relation)

    abilities.sort(
        key=lambda relation: (
            str(relation["era"]),
            str(relation["nation"]),
            str(relation["command"]),
            int(relation["raw_value"]),
        )
    )
    return {
        "abilities": abilities,
        "incoming": incoming,
        "unresolved": unresolved,
        "attribute_commands": commands,
    }
