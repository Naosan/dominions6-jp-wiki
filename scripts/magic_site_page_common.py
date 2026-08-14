from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from magic_site_data import (
    CLAIM_GEM_CODES,
    ECONOMY_FIELDS,
    ENTER_EFFECT_FIELDS,
    FACILITY_FIELDS,
    FIELD_GROUPS,
    GEM_CODES,
    PATH_ORDER,
    PROVINCE_BONUS_FIELDS,
    RESEARCH_FIELDS,
    SCALE_FIELDS,
    DEFENDER_FIELDS,
    format_gems,
    present,
)


def esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def short(value: object, limit: int = 180) -> str:
    text = str(value if value is not None else "").replace("\n", " ").strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def site_filename(site_id: int) -> str:
    return f"{site_id:04d}.md"


def site_link(site: dict[str, object], prefix: str = "by-id") -> str:
    return f"[{esc(site['name'])}]({prefix}/{site_filename(int(site['id']))})"


def unit_link(unit_id: int, name: str, *, from_site_page: bool = False) -> str:
    prefix = "../../units/by-id" if from_site_page else "../units/by-id"
    return f"[{esc(name)}]({prefix}/{unit_id:04d}.md)"


def nation_link(relation: dict[str, object], *, from_site_page: bool = False) -> str:
    prefix = "../../../nations" if from_site_page else "../../nations"
    return (
        f"[{esc(relation['era'])} {esc(relation['nation'])}]"
        f"({prefix}/{relation['directory']}/{relation['slug']}.md)"
    )


def front_matter(title: str, commit: str) -> list[str]:
    safe_title = title.replace('"', '\\"')
    return [
        "---",
        f'title: "{safe_title}"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {commit}"',
        "---",
        "",
    ]


PERCENT_FIELDS = {
    "conj",
    "alter",
    "evo",
    "const",
    "ench",
    "thau",
    "blood",
    "voidgate",
    "curse",
    "horror",
    "holyfire",
    "holypow",
    "adventure",
    "ageratereduction",
    "recpointpercent",
    "recpointpercentcmd",
    "agingpercent",
}
BOOLEAN_FIELDS = {"lab", "temple", "unaging", "maximizeorder"}
REVEAL_VALUES = {
    0: "Mundane score graphs",
    3: "Magic score graphs",
    5: "Dominion score graphs",
    999: "All score graphs",
}
SCALE_DIRECTIONS = {
    "turmoil": ("Turmoil", "Order"),
    "sloth": ("Sloth", "Productivity"),
    "cold": ("Cold", "Heat"),
    "death": ("Death", "Growth"),
    "misfortune": ("Misfortune", "Luck"),
    "drain": ("Drain", "Magic"),
}


def _integer(value: object, default: int = 0) -> int:
    try:
        return int(float(str(value).strip()))
    except (TypeError, ValueError):
        return default


def field_value(raw: dict[str, str], key: str) -> str:
    value = str(raw.get(key) or "").strip()
    if not present(value):
        return "—"
    if key in BOOLEAN_FIELDS:
        return "Yes"
    if key in PERCENT_FIELDS and "%" not in value:
        return f"{value}%"
    if key in SCALE_DIRECTIONS:
        number = _integer(value)
        positive, negative = SCALE_DIRECTIONS[key]
        return f"{positive} +{number}" if number > 0 else f"{negative} +{-number}"
    if key == "reveal":
        return REVEAL_VALUES.get(_integer(value), value)
    if key == "scorch":
        return f"{value} AN fire damage"
    return value


def _has_fields(site: dict[str, object], fields) -> bool:
    raw = site["raw"]
    return any(present(raw.get(key)) for key, _label in fields)


def _has_group(site: dict[str, object], group_key: str) -> bool:
    for key, _title, fields in FIELD_GROUPS:
        if key == group_key:
            return _has_fields(site, fields)
    return False


def summary_effects(site: dict[str, object], limit: int = 5) -> str:
    raw = site["raw"]
    effects: list[str] = []
    if site["monthly_gems"]:
        effects.append(f"Gems {format_gems(site['monthly_gems'])}")
    if site["claim_gems"]:
        effects.append(f"Claim {format_gems(site['claim_gems'])}")
    relation_counts = defaultdict(int)
    for relation in site["unit_relations"]:
        relation_counts[str(relation["group"])] += 1
    if relation_counts["Recruit"]:
        effects.append(f"Recruit {relation_counts['Recruit']}")
    if relation_counts["Summon"]:
        effects.append(f"Summon {relation_counts['Summon']}")
    if relation_counts["Province Defence"]:
        effects.append(f"PD {relation_counts['Province Defence']}")
    for key, label in RESEARCH_FIELDS:
        if present(raw.get(key)):
            effects.append(f"{label} {field_value(raw, key)}")
    if present(raw.get("gold")):
        effects.append(f"Gold {field_value(raw, 'gold')}")
    if present(raw.get("lab")):
        effects.append("Lab")
    if present(raw.get("fort")):
        effects.append("Fort")
    if site["event_relations"]:
        effects.append(f"Events {len(site['event_relations'])}")
    return ", ".join(effects[:limit]) or "—"


def compact_site_table(sites: list[dict[str, object]], *, prefix: str = "by-id") -> str:
    if not sites:
        return "該当Siteなし。\n"
    lines = [
        "| Site | ID | Path | Lv | Rarity | Category | Terrain | Gems / effects |",
        "|---|---:|---|---:|---:|---|---|---|",
    ]
    for site in sites:
        lines.append(
            f"| {site_link(site, prefix)} | {site['id']} | {esc(site['path'])} | "
            f"{site['level']} | {site['rarity']} | {esc(', '.join(site['categories']))} | "
            f"{esc(site['location_text'])} | {esc(summary_effects(site))} |"
        )
    return "\n".join(lines) + "\n"


def field_table(site: dict[str, object], fields) -> str:
    raw = site["raw"]
    selected = [(key, label) for key, label in fields if present(raw.get(key))]
    if not selected:
        return "該当する抽出値なし。\n"
    lines = ["| Effect | Value | Source field |", "|---|---|---|"]
    for key, label in selected:
        lines.append(f"| {esc(label)} | {esc(field_value(raw, key))} | `{key}` |")
    return "\n".join(lines) + "\n"


def nation_relations_table(site: dict[str, object], *, from_site_page: bool = False) -> str:
    relations = site["nation_relations"]
    if not relations:
        return "国家開始Site・Future Siteとしての明示Relationなし。\n"
    lines = ["| Nation | Relation | Attribute |", "|---|---|---:|"]
    for relation in sorted(
        relations,
        key=lambda item: (str(item["kind"]), str(item["era"]), str(item["nation"])),
    ):
        lines.append(
            f"| {nation_link(relation, from_site_page=from_site_page)} | "
            f"{esc(relation['kind'])} | {relation['attribute']} |"
        )
    return "\n".join(lines) + "\n"


def unit_relations_table(
    relations: list[dict[str, object]],
    *,
    from_site_page: bool = False,
) -> str:
    if not relations:
        return "該当Relationなし。\n"
    lines = [
        "| Relation | Role | Unit | ID | Amount | Nation restriction | Field |",
        "|---|---|---|---:|---|---|---|",
    ]
    for relation in sorted(
        relations,
        key=lambda item: (str(item["group"]), str(item["category"]), int(item["unit_id"])),
    ):
        nation = relation.get("national_recruits")
        if nation:
            nation_text = nation_link(
                {
                    "era": nation["code"],
                    "nation": nation["name"],
                    "directory": nation["dir"],
                    "slug": nation["slug"],
                },
                from_site_page=from_site_page,
            )
        elif int(relation.get("national_recruits_id") or 0) > 0:
            nation_text = f"Nation {relation['national_recruits_id']}"
        else:
            nation_text = "—"
        lines.append(
            f"| {esc(relation['category'])} | {esc(relation['role'])} | "
            f"{unit_link(int(relation['unit_id']), str(relation['unit']), from_site_page=from_site_page)} | "
            f"{relation['unit_id']} | {esc(relation['amount'])} | {nation_text} | "
            f"`{esc(relation['field'])}` |"
        )
    return "\n".join(lines) + "\n"


def event_relations_table(site: dict[str, object]) -> str:
    relations = site["event_relations"]
    if not relations:
        return "このSiteを直接参照・生成するEvent relationは確認されていません。\n"
    lines = [
        "| Event | ID | Relation | Field | Rarity | Description | Confidence |",
        "|---|---:|---|---|---:|---|---|",
    ]
    for relation in sorted(
        relations,
        key=lambda item: (int(item["event_id"]), str(item["direction"]), str(item["field"])),
    ):
        lines.append(
            f"| {esc(relation['event'])} | {relation['event_id']} | {esc(relation['relation'])} | "
            f"`{esc(relation['field'])}` | {relation['rarity']} | "
            f"{esc(short(relation['description'], 170) or '—')} | {esc(relation['confidence'])} |"
        )
    return "\n".join(lines) + "\n"
