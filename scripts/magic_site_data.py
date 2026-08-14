from __future__ import annotations

import re
from collections import Counter, defaultdict
from typing import Iterable

from generate_recruitment_data import num


PATH_ORDER = (
    ("Fire", "F", "fire"),
    ("Air", "A", "air"),
    ("Water", "W", "water"),
    ("Earth", "E", "earth"),
    ("Astral", "S", "astral"),
    ("Death", "D", "death"),
    ("Nature", "N", "nature"),
    ("Glamour", "G", "glamour"),
    ("Blood", "B", "blood"),
    ("Holy", "H", "holy"),
)
PATH_BY_NAME = {name: (code, slug) for name, code, slug in PATH_ORDER}
PATH_BY_CODE = {code: name for name, code, _slug in PATH_ORDER}
GEM_CODES = tuple(code for _name, code, _slug in PATH_ORDER if code != "H")
CLAIM_GEM_CODES = GEM_CODES

NATION_SITE_ATTRIBUTES = {
    25: "Start Site",
    52: "Start Site",
    100: "Start Site",
    631: "Future Site",
}

SITE_EVENT_REQUIREMENTS = {
    "site": "Requires site",
    "foundsite": "Requires discovered site",
    "hiddensite": "Requires hidden site",
    "nearbysite": "Requires nearby site",
}
SITE_EVENT_EFFECTS = {
    "newsite": "Creates site",
}

SITE_UNIT_FIELD_SPECS: dict[str, dict[str, str]] = {}
for index in range(1, 6):
    SITE_UNIT_FIELD_SPECS[f"hmon{index}"] = {
        "group": "Recruit",
        "category": "Home troop recruit",
        "role": "Troop",
    }
    SITE_UNIT_FIELD_SPECS[f"hcom{index}"] = {
        "group": "Recruit",
        "category": "Home commander recruit",
        "role": "Commander",
    }
    SITE_UNIT_FIELD_SPECS[f"mon{index}"] = {
        "group": "Recruit",
        "category": "Site troop recruit",
        "role": "Troop",
    }
    SITE_UNIT_FIELD_SPECS[f"com{index}"] = {
        "group": "Recruit",
        "category": "Site commander recruit",
        "role": "Commander",
    }
for index in range(1, 5):
    SITE_UNIT_FIELD_SPECS[f"sum{index}"] = {
        "group": "Summon",
        "category": "Site summon",
        "role": "Summon",
    }
SITE_UNIT_FIELD_SPECS.update(
    {
        "natmon": {
            "group": "Recruit",
            "category": "National site troop",
            "role": "Troop",
        },
        "natcom": {
            "group": "Recruit",
            "category": "National site commander",
            "role": "Commander",
        },
        "provdef1": {
            "group": "Province Defence",
            "category": "Extra province defence unit",
            "role": "Troop",
        },
        "provdef2": {
            "group": "Province Defence",
            "category": "Extra province defence unit",
            "role": "Troop",
        },
        "provdefcom": {
            "group": "Province Defence",
            "category": "Extra province defence commander",
            "role": "Commander",
        },
    }
)

ECONOMY_FIELDS = (
    ("gold", "Gold generation"),
    ("bringgold", "Mine gold / turn"),
    ("res", "Resource generation"),
    ("bringres", "Mine resource production"),
    ("provinc", "Province income modifier"),
    ("sup", "Supply bonus"),
    ("unr", "Unrest modifier"),
    ("recpoints", "Recruitment points"),
    ("recpointpercent", "Recruitment point modifier"),
    ("recpointpercentcmd", "Commander recruitment point modifier"),
    ("addtolimitedrecruitment", "Limited recruitment allowance"),
    ("popgrowth", "Population growth"),
)
FACILITY_FIELDS = (
    ("lab", "Creates laboratory"),
    ("fort", "Creates fort"),
    ("temple", "Creates temple"),
)
SCALE_FIELDS = (
    ("scale1", "Scale increase 1"),
    ("scale2", "Scale increase 2"),
    ("turmoil", "Turmoil / Order modifier"),
    ("sloth", "Sloth / Productivity modifier"),
    ("cold", "Cold / Heat modifier"),
    ("death", "Death / Growth modifier"),
    ("misfortune", "Misfortune / Luck modifier"),
    ("drain", "Drain / Magic modifier"),
    ("domspread", "Dominion spread"),
    ("domconflict", "Dominion conflict bonus"),
    ("maximizeorder", "Set Order to maximum"),
    ("throneclustering", "Throne clustering"),
)
RESEARCH_FIELDS = (
    ("conj", "Conjuration bonus"),
    ("alter", "Alteration bonus"),
    ("evo", "Evocation bonus"),
    ("const", "Construction bonus"),
    ("ench", "Enchantment bonus"),
    ("thau", "Thaumaturgy bonus"),
    ("blood", "Blood Magic bonus"),
    ("rituallevelmodifier", "Ritual level modifier"),
    ("callgodbonus", "Call God bonus"),
    ("magicresistancebonus", "Magic resistance bonus"),
)
ENTER_EFFECT_FIELDS = (
    ("exp", "Enter to gain experience"),
    ("heal", "Healing"),
    ("disease", "Spreads disease"),
    ("curse", "Curse chance"),
    ("horror", "Horror mark chance"),
    ("holyfire", "Holy fire"),
    ("holypow", "Holy power"),
    ("scry", "Enter to scry"),
    ("scryrange", "Scrying range"),
    ("adventure", "Adventure chance"),
    ("voidgate", "Summon void creatures"),
    ("reveal", "Reveals score graphs"),
    ("other", "Other extracted effect"),
)
PROVINCE_BONUS_FIELDS = (
    ("fireres", "Fire resistance"),
    ("coldres", "Cold resistance"),
    ("shockres", "Shock resistance"),
    ("poisonres", "Poison resistance"),
    ("str", "Strength"),
    ("prec", "Precision"),
    ("mor", "Morale"),
    ("undying", "Undying"),
    ("att", "Attack"),
    ("def", "Defence"),
    ("darkvision", "Darkvision"),
    ("aawe", "Animal awe"),
    ("awe", "Awe"),
    ("reinvigoration", "Reinvigoration"),
    ("airshield", "Air shield"),
    ("mr", "Magic resistance"),
    ("ageratereduction", "Age rate reduction"),
    ("agingpercent", "Aging rate"),
    ("unaging", "Unaging"),
    ("dragonlord", "Dragon lord bonus"),
    ("corpselord", "Corpse construction bonus"),
    ("ivylord", "Vine creature bonus"),
    ("pdconscript", "Dominion PD conscription"),
)
DEFENDER_FIELDS = (
    ("wilddefenders", "Wild defenders"),
    ("evil", "Evil defenders"),
    ("scorch", "Scorching desert damage"),
)

FIELD_GROUPS = (
    ("economy", "Economy・Recruitment infrastructure", ECONOMY_FIELDS + FACILITY_FIELDS),
    ("scales", "Scales・Dominion", SCALE_FIELDS),
    ("research", "Research・Ritual bonuses", RESEARCH_FIELDS),
    ("enter", "Enter・Active effects", ENTER_EFFECT_FIELDS),
    ("bonuses", "Province・Unit bonuses", PROVINCE_BONUS_FIELDS + DEFENDER_FIELDS),
)

BASE_SITE_FIELDS = {
    "id",
    "name",
    "rarity",
    "loc",
    "level",
    "path",
    "sprite",
    "end",
    "nationalrecruits",
    "rit",
    "ritrng",
}
KNOWN_SITE_FIELDS = set(BASE_SITE_FIELDS)
KNOWN_SITE_FIELDS.update(GEM_CODES)
KNOWN_SITE_FIELDS.update(f"{code}2" for code in CLAIM_GEM_CODES)
KNOWN_SITE_FIELDS.update(SITE_UNIT_FIELD_SPECS)
KNOWN_SITE_FIELDS.update(f"n_sum{index}" for index in range(1, 5))
for _group_key, _group_title, fields in FIELD_GROUPS:
    KNOWN_SITE_FIELDS.update(key for key, _label in fields)
# Inspector accepts these even when the pinned vanilla table does not currently expose them.
KNOWN_SITE_FIELDS.update({"H", "H2", "G2", "hp", "temple"})


def _text(value: object) -> str:
    return str(value if value is not None else "").strip()


def present(value: object) -> bool:
    text = _text(value)
    return text not in {"", "0", "0.0", "0%", "0.0%", "—"}


def integer(value: object, default: int = 0) -> int:
    text = _text(value)
    if not text:
        return default
    try:
        return int(float(text))
    except ValueError:
        return default


def split_tokens(raw: str) -> list[tuple[str, list[str]]]:
    output: list[tuple[str, list[str]]] = []
    for token in (raw or "").split("|"):
        token = token.strip()
        if not token:
            continue
        parts = token.split()
        output.append((parts[0], parts[1:]))
    return output


def path_slug(path: str) -> str:
    if path in PATH_BY_NAME:
        return PATH_BY_NAME[path][1]
    slug = re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-")
    return slug or "unknown"


def gem_values(row: dict[str, str], *, claimed: bool = False) -> dict[str, int]:
    suffix = "2" if claimed else ""
    values: dict[str, int] = {}
    for code in CLAIM_GEM_CODES if claimed else GEM_CODES:
        value = integer(row.get(f"{code}{suffix}"))
        if value:
            values[code] = value
    return values


def format_gems(values: dict[str, int]) -> str:
    return " + ".join(f"{amount}{code}" for code, amount in values.items()) or "—"


def load_terrain_lookup(rows: Iterable[dict[str, str]]) -> dict[int, str]:
    output: dict[int, str] = {}
    for row in rows:
        bit = integer(row.get("bit_value"))
        name = _text(row.get("bit_name"))
        if bit > 0 and name:
            output[bit] = name
    return dict(sorted(output.items()))


def decode_location(raw_location: int, terrain_lookup: dict[int, str]) -> tuple[list[str], int]:
    labels: list[str] = []
    remaining = raw_location
    for bit, label in terrain_lookup.items():
        if raw_location & bit:
            labels.append(label)
            remaining &= ~bit
    return labels, remaining


def _site_name_matches(description: str, sites_by_name: dict[str, list[int]]) -> list[int]:
    matches: list[int] = []
    for name in re.findall(r"\[(.*?)\]", description or ""):
        matches.extend(sites_by_name.get(name.strip(), []))
    return list(dict.fromkeys(matches))


def build_nation_site_relations(
    attribute_rows: list[dict[str, str]],
    sites_by_id: dict[int, dict[str, object]],
    nation_rows: list[dict[str, object]],
):
    nations = {int(row["id"]): row for row in nation_rows}
    by_site: dict[int, list[dict[str, object]]] = defaultdict(list)
    unresolved: list[tuple[int, str, int, int]] = []
    seen: set[tuple[int, int, str, int]] = set()

    for row in attribute_rows:
        nation_id = num(row, "nation_number", -1)
        attribute = num(row, "attribute", -1)
        site_id = num(row, "raw_value", -1)
        kind = NATION_SITE_ATTRIBUTES.get(attribute)
        if kind is None or nation_id not in nations or site_id <= 0:
            continue
        key = (site_id, nation_id, kind, attribute)
        if key in seen:
            continue
        seen.add(key)
        if site_id not in sites_by_id:
            unresolved.append((nation_id, str(nations[nation_id]["name"]), attribute, site_id))
            continue
        nation = nations[nation_id]
        by_site[site_id].append(
            {
                "kind": kind,
                "attribute": attribute,
                "nation_id": nation_id,
                "nation": nation["name"],
                "era": nation["code"],
                "directory": nation["dir"],
                "slug": nation["slug"],
                "confidence": "explicit-nation-attribute",
            }
        )
    return by_site, unresolved


def build_site_unit_relations(
    site_rows: list[dict[str, str]],
    units: dict[int, dict[str, str]],
    nation_rows: list[dict[str, object]],
):
    nations = {int(row["id"]): row for row in nation_rows}
    by_site: dict[int, list[dict[str, object]]] = defaultdict(list)
    unresolved: list[tuple[int, str, str, str]] = []
    unresolved_nations: list[tuple[int, str, int]] = []
    seen: set[tuple[int, str, int]] = set()

    for row in site_rows:
        site_id = num(row, "id", -1)
        if site_id <= 0:
            continue
        site_name = _text(row.get("name")) or f"Site {site_id}"
        national_recruits_id = num(row, "nationalrecruits", 0)
        national_recruits = nations.get(national_recruits_id)
        if national_recruits_id > 0 and national_recruits is None:
            unresolved_nations.append((site_id, site_name, national_recruits_id))

        for field, spec in SITE_UNIT_FIELD_SPECS.items():
            raw_target = _text(row.get(field))
            if not present(raw_target):
                continue
            unit_id = integer(raw_target, -1)
            key = (site_id, field, unit_id)
            if key in seen:
                continue
            seen.add(key)
            if unit_id <= 0 or unit_id not in units:
                unresolved.append((site_id, site_name, field, raw_target))
                continue

            amount = "1"
            if field.startswith("sum"):
                slot = field.removeprefix("sum")
                maximum = max(1, num(row, f"n_sum{slot}", 1))
                amount = "1" if maximum <= 1 else f"1–{maximum}"
            elif field.startswith("provdef"):
                amount = "PD-defined"

            relation = {
                "site_id": site_id,
                "site": site_name,
                "group": spec["group"],
                "category": spec["category"],
                "role": spec["role"],
                "field": field,
                "unit_id": unit_id,
                "unit": units[unit_id].get("name") or "(unnamed)",
                "amount": amount,
                "national_recruits_id": national_recruits_id,
                "national_recruits": national_recruits,
                "confidence": "explicit-site-field",
            }
            by_site[site_id].append(relation)

    return by_site, unresolved, unresolved_nations


def build_site_event_relations(
    event_rows: list[dict[str, str]],
    sites_by_id: dict[int, dict[str, object]],
):
    sites_by_name: dict[str, list[int]] = defaultdict(list)
    for site_id, site in sites_by_id.items():
        sites_by_name[str(site["name"])].append(site_id)

    by_site: dict[int, list[dict[str, object]]] = defaultdict(list)
    unresolved: list[tuple[int, str, str, str]] = []
    seen: set[tuple[int, int, str, str]] = set()

    def add_relation(
        row: dict[str, str],
        event_id: int,
        field: str,
        label: str,
        direction: str,
        values: list[str],
    ) -> None:
        raw_target = values[0] if values else ""
        target_id = integer(raw_target, 0)
        target_ids: list[int] = []
        confidence = "explicit-event-site-id"
        if target_id > 0 and target_id in sites_by_id:
            target_ids = [target_id]
        elif target_id > 0:
            unresolved.append(
                (
                    event_id,
                    _text(row.get("name")) or f"Event {event_id}",
                    field,
                    raw_target,
                )
            )
            return
        else:
            target_ids = _site_name_matches(_text(row.get("description")), sites_by_name)
            confidence = "event-description-site-name"
            if not target_ids:
                # Zero/negative values can be sentinels or random-site selectors.
                if raw_target and target_id == 0 and raw_target not in {"0", "-1"}:
                    unresolved.append(
                        (
                            event_id,
                            _text(row.get("name")) or f"Event {event_id}",
                            field,
                            raw_target,
                        )
                    )
                return

        for site_id in target_ids:
            key = (event_id, site_id, field, direction)
            if key in seen:
                continue
            seen.add(key)
            by_site[site_id].append(
                {
                    "event_id": event_id,
                    "event": _text(row.get("name")) or f"Event {event_id}",
                    "description": _text(row.get("description")),
                    "rarity": num(row, "rarity"),
                    "requirements": _text(row.get("requirements")),
                    "effects": _text(row.get("effects")),
                    "field": field,
                    "relation": label,
                    "direction": direction,
                    "raw_target": raw_target,
                    "confidence": confidence,
                }
            )

    for row in event_rows:
        event_id = num(row, "id", -1)
        if event_id < 0:
            continue
        for field, values in split_tokens(row.get("requirements") or ""):
            if field in SITE_EVENT_REQUIREMENTS:
                add_relation(
                    row,
                    event_id,
                    field,
                    SITE_EVENT_REQUIREMENTS[field],
                    "requirement",
                    values,
                )
        for field, values in split_tokens(row.get("effects") or ""):
            if field in SITE_EVENT_EFFECTS:
                add_relation(
                    row,
                    event_id,
                    field,
                    SITE_EVENT_EFFECTS[field],
                    "effect",
                    values,
                )
    return by_site, unresolved


def _categories(
    row: dict[str, str],
    nation_relations: list[dict[str, object]],
    location_labels: list[str],
) -> list[str]:
    categories: list[str] = []
    rarity = num(row, "rarity")
    if rarity >= 11:
        categories.append("Throne")
    if any(relation["kind"] == "Start Site" for relation in nation_relations):
        categories.append("National start site")
    if any(relation["kind"] == "Future Site" for relation in nation_relations):
        categories.append("Future national site")
    if "Unique" in location_labels:
        categories.append("Unique location")
    if rarity <= 4 and not categories:
        categories.append("Normal / random site")
    if not categories:
        categories.append("Special site")
    return categories


def _field_counts(site_rows: list[dict[str, str]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for row in site_rows:
        for key, value in row.items():
            if key not in KNOWN_SITE_FIELDS and present(value):
                counts[key] += 1
    return dict(sorted(counts.items()))


def build_magic_site_catalog(
    site_rows: list[dict[str, str]],
    terrain_rows: list[dict[str, str]],
    attribute_rows: list[dict[str, str]],
    event_rows: list[dict[str, str]],
    units: dict[int, dict[str, str]],
    nation_rows: list[dict[str, object]],
):
    terrain_lookup = load_terrain_lookup(terrain_rows)
    sites_by_id: dict[int, dict[str, object]] = {}
    duplicate_ids: list[int] = []
    missing_names: list[int] = []

    for row in site_rows:
        site_id = num(row, "id", -1)
        if site_id <= 0:
            continue
        if site_id in sites_by_id:
            duplicate_ids.append(site_id)
            continue
        name = _text(row.get("name"))
        if not name:
            name = f"Site {site_id}"
            missing_names.append(site_id)
        sites_by_id[site_id] = {
            "id": site_id,
            "name": name,
            "raw": row,
        }

    nation_relations, unresolved_nation_sites = build_nation_site_relations(
        attribute_rows,
        sites_by_id,
        nation_rows,
    )
    unit_relations, unresolved_units, unresolved_national_recruits = build_site_unit_relations(
        site_rows,
        units,
        nation_rows,
    )
    event_relations, unresolved_events = build_site_event_relations(event_rows, sites_by_id)

    unknown_location_bits: list[tuple[int, str, int, int]] = []
    path_counts: Counter[str] = Counter()
    terrain_counts: Counter[str] = Counter()
    rarity_counts: Counter[int] = Counter()
    name_counts: Counter[str] = Counter()

    for site_id, site in sites_by_id.items():
        row = site["raw"]
        location_raw = num(row, "loc")
        location_labels, remaining = decode_location(location_raw, terrain_lookup)
        display_location_labels = list(location_labels)
        if remaining:
            unknown_location_bits.append((site_id, str(site["name"]), location_raw, remaining))
            display_location_labels.append(f"Unknown bits {remaining}")
        path = _text(row.get("path")) or "Unknown"
        site_nations = nation_relations.get(site_id, [])
        site.update(
            {
                "path": path,
                "path_slug": path_slug(path),
                "level": num(row, "level"),
                "rarity": num(row, "rarity"),
                "location_raw": location_raw,
                "location_labels": location_labels,
                "location_text": ", ".join(display_location_labels) or "Unspecified / special placement",
                "monthly_gems": gem_values(row),
                "claim_gems": gem_values(row, claimed=True),
                "nation_relations": site_nations,
                "unit_relations": unit_relations.get(site_id, []),
                "event_relations": event_relations.get(site_id, []),
                "categories": _categories(row, site_nations, location_labels),
                "national_recruits_id": num(row, "nationalrecruits"),
            }
        )
        path_counts[path] += 1
        rarity_counts[num(row, "rarity")] += 1
        name_counts[str(site["name"])] += 1
        for label in location_labels:
            terrain_counts[label] += 1

    sites = [sites_by_id[site_id] for site_id in sorted(sites_by_id)]
    all_unit_relations = [
        relation for site in sites for relation in site["unit_relations"]
    ]
    all_nation_relations = [
        relation for site in sites for relation in site["nation_relations"]
    ]
    all_event_relations = [
        relation for site in sites for relation in site["event_relations"]
    ]
    unclassified_fields = _field_counts(site_rows)
    duplicate_names = {
        name: count for name, count in sorted(name_counts.items()) if count > 1
    }

    stats = {
        "sites": len(sites),
        "monthly_gem_sites": sum(bool(site["monthly_gems"]) for site in sites),
        "monthly_gem_total": sum(
            sum(site["monthly_gems"].values()) for site in sites
        ),
        "claim_gem_sites": sum(bool(site["claim_gems"]) for site in sites),
        "claim_gem_total": sum(sum(site["claim_gems"].values()) for site in sites),
        "normal_site_records": sum(site["rarity"] <= 4 for site in sites),
        "throne_sites": sum(site["rarity"] >= 11 for site in sites),
        "unique_location_sites": sum("Unique" in site["location_labels"] for site in sites),
        "start_site_relations": sum(
            relation["kind"] == "Start Site" for relation in all_nation_relations
        ),
        "future_site_relations": sum(
            relation["kind"] == "Future Site" for relation in all_nation_relations
        ),
        "site_unit_relations": len(all_unit_relations),
        "site_recruit_relations": sum(
            relation["group"] == "Recruit" for relation in all_unit_relations
        ),
        "site_summon_relations": sum(
            relation["group"] == "Summon" for relation in all_unit_relations
        ),
        "site_pd_relations": sum(
            relation["group"] == "Province Defence" for relation in all_unit_relations
        ),
        "site_event_relations": len(all_event_relations),
        "site_event_requirements": sum(
            relation["direction"] == "requirement" for relation in all_event_relations
        ),
        "site_event_creations": sum(
            relation["direction"] == "effect" for relation in all_event_relations
        ),
        "duplicate_site_ids": len(duplicate_ids),
        "duplicate_site_names": len(duplicate_names),
        "missing_site_names": len(missing_names),
        "unknown_location_bits": len(unknown_location_bits),
        "unclassified_site_fields": len(unclassified_fields),
        "unclassified_site_values": sum(unclassified_fields.values()),
        "unresolved_site_units": len(unresolved_units),
        "unresolved_nation_sites": len(unresolved_nation_sites),
        "unresolved_site_events": len(unresolved_events),
        "unresolved_national_recruit_nations": len(unresolved_national_recruits),
    }

    return {
        "sites": sites,
        "sites_by_id": sites_by_id,
        "terrain_lookup": terrain_lookup,
        "path_counts": dict(path_counts),
        "terrain_counts": dict(terrain_counts),
        "rarity_counts": dict(sorted(rarity_counts.items())),
        "duplicate_ids": duplicate_ids,
        "duplicate_names": duplicate_names,
        "missing_names": missing_names,
        "unknown_location_bits": unknown_location_bits,
        "unclassified_fields": unclassified_fields,
        "unresolved_units": unresolved_units,
        "unresolved_nation_sites": unresolved_nation_sites,
        "unresolved_events": unresolved_events,
        "unresolved_national_recruits": unresolved_national_recruits,
        "stats": stats,
    }
