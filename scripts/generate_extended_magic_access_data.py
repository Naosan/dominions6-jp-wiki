#!/usr/bin/env python3
"""Generate nation-level extended Magic Access profiles.

This layer deliberately sits above normal recruit access. It separates:

- nation start/future Site mages,
- national Hero mages,
- Pretender chassis base paths,
- one-step mage summons castable by native recruit mages.

The generator does not recursively chain summoned mages, assume Hero arrival,
or treat Pretender design as an in-game recruit. Generated pages are factual
planning aids, not a tier list.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

from generate_nation_site_search_data import (
    PATH_NAMES,
    PATH_ORDER,
    broad_sort_key,
    collect_candidates,
    deterministic_levels,
    fixed_meets,
    front_matter,
    level_text,
    max_levels,
    possible_levels,
    random_feasible,
    requirement_levels,
)
from generate_recruitment_data import (
    COMMIT,
    esc,
    fixed,
    mage,
    num,
    random_text,
    randoms,
    tsv,
    yes,
)
from generate_spell_item_data import (
    SCHOOLS,
    spell_attributes,
    spell_gem_cost,
    spell_path,
    spell_research,
)
from magic_site_data import NATION_SITE_ATTRIBUTES
from unit_catalog_special_integration import load_unit_catalog

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "data" / "extended-magic-access"
CONFIG = ROOT / "zensical.toml"
DATA_INDEX = ROOT / "docs" / "data" / "index.md"
MAGE_ACCESS = ROOT / "docs" / "data" / "mage-access.md"
SITE_SEARCH_INDEX = ROOT / "docs" / "data" / "site-search" / "index.md"
SITE_SEARCH_GUIDE = ROOT / "docs" / "magic" / "site-search.md"
SITE_SEARCH_PLAYBOOK = ROOT / "docs" / "magic" / "site-search-playbook.md"
GUIDE = ROOT / "docs" / "magic" / "extended-magic-access.md"
RECRUIT_ROOT = ROOT / "docs" / "data" / "recruitment"
SITE_SEARCH_ROOT = ROOT / "docs" / "data" / "site-search"

PATH_SET = set(PATH_ORDER)


def unit_has_magic(row: dict[str, str]) -> bool:
    return bool(fixed(row) or randoms(row))


def unit_role(row: dict[str, str]) -> str:
    commander = any(num(row, key) for key in ("leader", "undeadleader", "magicleader"))
    if unit_has_magic(row) and commander:
        return "Mage Commander"
    if unit_has_magic(row):
        return "Mage"
    if commander or num(row, "holy"):
        return "Commander"
    return "Troop"


def unit_record(
    unit_id: int,
    row: dict[str, str],
    *,
    layer: str,
    source: str,
    metadata: dict[str, object] | None = None,
) -> dict[str, object]:
    guaranteed = deterministic_levels(row)
    possible = possible_levels(row)
    return {
        "id": unit_id,
        "name": (row.get("name") or f"Unit {unit_id}").strip(),
        "row": row,
        "layer": layer,
        "source": source,
        "guaranteed": guaranteed,
        "possible": possible,
        "random": random_text(row),
        "role": unit_role(row),
        "mapmove": num(row, "mapmove"),
        "research": num(row, "researchbonus"),
        "latehero": yes(row, "latehero"),
        "unique": yes(row, "unique"),
        **(metadata or {}),
    }


def records_max(
    records: Iterable[dict[str, object]],
    *,
    key: str = "guaranteed",
) -> dict[str, int]:
    result = {path: 0 for path in PATH_ORDER}
    for record in records:
        levels = record.get(key) or {}
        for path in PATH_ORDER:
            result[path] = max(result[path], int(levels.get(path, 0)))
    return result


def flatten_targets(groups: Iterable[dict[str, object]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    seen: set[tuple[int, str]] = set()
    for group in groups:
        for target in group.get("targets") or []:
            key = (int(target["id"]), str(group.get("access") or ""))
            if key in seen:
                continue
            seen.add(key)
            output.append(target)
    return output


def gain_map(layer: dict[str, int], native: dict[str, int]) -> dict[str, int]:
    return {
        path: level
        for path, level in layer.items()
        if level > int(native.get(path, 0))
    }


def gain_text(layer: dict[str, int], native: dict[str, int]) -> str:
    parts: list[str] = []
    for path in PATH_ORDER:
        level = int(layer.get(path, 0))
        old = int(native.get(path, 0))
        if level <= old:
            continue
        if old:
            parts.append(f"{path}{level}（native {path}{old}）")
        else:
            parts.append(f"{path}{level}（new）")
    return " ".join(parts) or "—"


def level_cell(levels: dict[str, int]) -> str:
    return level_text(levels)


def unit_link(record: dict[str, object], *, detail: bool = False) -> str:
    prefix = "../../units/by-id" if detail else "../units/by-id"
    return f"[{esc(record['name'])}]({prefix}/{int(record['id']):04d}.md)"


def site_link(site_id: int, site_name: str, *, detail: bool = False) -> str:
    prefix = "../../sites/by-id" if detail else "../sites/by-id"
    return f"[{esc(site_name)}]({prefix}/{site_id:04d}.md)"


def spell_link(group: dict[str, object], *, detail: bool = False) -> str:
    prefix = "../../spells/by-school" if detail else "../spells/by-school"
    return (
        f"[{esc(group['spell'])}]"
        f"({prefix}/{group['school_slug']}.md)"
    )


def reverse_hero_records(data) -> dict[int, list[dict[str, object]]]:
    output: dict[int, list[dict[str, object]]] = defaultdict(list)
    seen: set[tuple[int, int, str]] = set()
    for unit_id, relations in data["heroes"].items():
        row = data["units"].get(unit_id)
        if row is None or not unit_has_magic(row):
            continue
        for relation in relations:
            nation_id = int(relation["nation_id"])
            key = (nation_id, unit_id, str(relation["slot"]))
            if key in seen:
                continue
            seen.add(key)
            output[nation_id].append(
                unit_record(
                    unit_id,
                    row,
                    layer="Hero",
                    source=str(relation["hero_type"]),
                    metadata={
                        "hero_type": relation["hero_type"],
                        "slot": relation["slot"],
                    },
                )
            )
    for records in output.values():
        records.sort(key=lambda item: (str(item["hero_type"]), str(item["slot"]), str(item["name"])))
    return output


def reverse_pretender_records(data) -> dict[int, list[dict[str, object]]]:
    output: dict[int, list[dict[str, object]]] = defaultdict(list)
    seen: set[tuple[int, int]] = set()
    for unit_id, relations in data["pretenders"].items():
        row = data["units"].get(unit_id)
        if row is None:
            continue
        for relation in relations:
            nation_id = int(relation["nation_id"])
            key = (nation_id, unit_id)
            if key in seen:
                continue
            seen.add(key)
            output[nation_id].append(
                unit_record(
                    unit_id,
                    row,
                    layer="Pretender",
                    source="Pretender design",
                    metadata={
                        "pathcost": row.get("pathcost") or "—",
                        "startdom": row.get("startdom") or "—",
                        "minimprisonment": row.get("minimprisonment") or "—",
                        "size": row.get("size") or "—",
                        "hp": row.get("hp") or "—",
                        "prot": row.get("prot") or "—",
                        "immobile": yes(row, "immobile"),
                    },
                )
            )
    for records in output.values():
        records.sort(
            key=lambda item: (
                0 if item["guaranteed"] else 1,
                str(item["name"]),
                int(item["id"]),
            )
        )
    return output


def start_site_records(data) -> tuple[
    dict[int, list[dict[str, object]]],
    list[tuple[int, int]],
]:
    sites_by_id = {
        num(row, "id"): row
        for row in tsv(data["paths"]["MagicSites.csv"])
        if num(row, "id") > 0
    }
    site_mages: dict[int, list[tuple[int, dict[str, object]]]] = defaultdict(list)
    for unit_id, relations in data["sites"].items():
        row = data["units"].get(unit_id)
        if row is None or not unit_has_magic(row):
            continue
        for relation in relations:
            if relation.get("role") != "Commander":
                continue
            site_mages[int(relation["site_id"])].append((unit_id, relation))

    output: dict[int, list[dict[str, object]]] = defaultdict(list)
    unresolved: list[tuple[int, int]] = []
    seen: set[tuple[int, int, int, str]] = set()
    for attr in tsv(data["paths"]["attributes_by_nation.csv"]):
        nation_id = num(attr, "nation_number")
        attribute = num(attr, "attribute")
        site_id = num(attr, "raw_value")
        site_kind = NATION_SITE_ATTRIBUTES.get(attribute)
        if site_kind is None or nation_id <= 0 or site_id <= 0:
            continue
        site_row = sites_by_id.get(site_id)
        if site_row is None:
            unresolved.append((nation_id, site_id))
            continue
        restriction = num(site_row, "nationalrecruits")
        if restriction > 0 and restriction != nation_id:
            continue
        for unit_id, relation in site_mages.get(site_id, []):
            key = (nation_id, site_id, unit_id, str(relation.get("field") or ""))
            if key in seen:
                continue
            seen.add(key)
            output[nation_id].append(
                unit_record(
                    unit_id,
                    data["units"][unit_id],
                    layer=site_kind,
                    source=str(relation.get("source") or "Magic Site commander"),
                    metadata={
                        "site_id": site_id,
                        "site": site_row.get("name") or f"Site {site_id}",
                        "site_kind": site_kind,
                        "site_path": site_row.get("path") or "—",
                        "site_level": num(site_row, "level"),
                        "site_field": relation.get("field") or "—",
                    },
                )
            )
    for records in output.values():
        records.sort(
            key=lambda item: (
                0 if item["site_kind"] == "Start Site" else 1,
                str(item["site"]),
                str(item["name"]),
                int(item["id"]),
            )
        )
    return output, unresolved


def spell_scope(attribute_rows: list[dict[str, str]]) -> tuple[
    dict[int, set[int]],
    set[int],
]:
    national: dict[int, set[int]] = defaultdict(set)
    realm: set[int] = set()
    attrs = spell_attributes(attribute_rows)
    for spell_id, values in attrs.items():
        for attribute, raw_value in values:
            if attribute == 278 and raw_value > 0:
                national[spell_id].add(raw_value)
            elif attribute == 602:
                realm.add(spell_id)
    return national, realm


def build_summon_groups(data) -> tuple[list[dict[str, object]], dict[str, int]]:
    spell_rows = {
        num(row, "id"): row
        for row in tsv(data["paths"]["spells.csv"])
        if num(row, "id") > 0
    }
    national, realm = spell_scope(tsv(data["paths"]["attributes_by_spell.csv"]))
    grouped: dict[tuple[int, str, bool], dict[str, object]] = {}
    excluded_independent = 0
    unresolved_spells = 0

    for unit_id, relations in data["spell_summons"].items():
        row = data["units"].get(unit_id)
        if row is None or not unit_has_magic(row):
            continue
        for relation in relations:
            if relation.get("kind") != "Spell" or relation.get("type") != "Ritual":
                continue
            effect_label = str(relation.get("effect") or "")
            if "independent" in effect_label.lower():
                excluded_independent += 1
                continue
            spell_id = int(relation.get("spell_id") or 0)
            spell_row = spell_rows.get(spell_id)
            if spell_row is None:
                unresolved_spells += 1
                continue
            pool = str(relation.get("pool") or "—")
            candidate = pool not in {"", "—"}
            key = (spell_id, pool, candidate)
            group = grouped.setdefault(
                key,
                {
                    "spell_id": spell_id,
                    "spell": relation.get("spell") or spell_row.get("name") or f"Spell {spell_id}",
                    "school": relation.get("school") or SCHOOLS.get(num(spell_row, "school"), ("—", "index"))[0],
                    "school_slug": relation.get("school_slug") or SCHOOLS.get(num(spell_row, "school"), ("—", "index"))[1],
                    "research": relation.get("research") or spell_research(spell_row),
                    "path": relation.get("path") or spell_path(spell_row),
                    "cost": relation.get("cost") or "—",
                    "effect": effect_label or "Summon",
                    "pool": pool,
                    "candidate": candidate,
                    "confidence": relation.get("confidence") or "explicit-spell-unit",
                    "requirements": requirement_levels(spell_row),
                    "spell_row": spell_row,
                    "national_ids": national.get(spell_id, set()),
                    "realm_restricted": spell_id in realm,
                    "targets": {},
                },
            )
            group["targets"][unit_id] = unit_record(
                unit_id,
                row,
                layer="Spell summon candidate" if candidate else "Spell summon",
                source=str(group["spell"]),
                metadata={
                    "pool": pool,
                    "confidence": group["confidence"],
                },
            )

    output: list[dict[str, object]] = []
    for group in grouped.values():
        group["targets"] = sorted(
            group["targets"].values(),
            key=lambda item: (str(item["name"]), int(item["id"])),
        )
        output.append(group)
    output.sort(
        key=lambda item: (
            num(item["spell_row"], "school"),
            num(item["spell_row"], "researchlevel"),
            str(item["spell"]),
            bool(item["candidate"]),
            str(item["pool"]),
        )
    )
    return output, {
        "summon_mage_groups": len(output),
        "excluded_independent_summons": excluded_independent,
        "unresolved_summon_spells": unresolved_spells,
    }


def candidate_names(candidates: list[dict[str, object]], limit: int = 3) -> str:
    if not candidates:
        return "—"
    values = [f"{item['name']} #{item['id']}" for item in candidates[:limit]]
    if len(candidates) > limit:
        values.append(f"ほか{len(candidates) - limit}")
    return "; ".join(values)


def summon_access_for_nation(
    nation_id: int,
    native_candidates: list[dict[str, object]],
    groups: list[dict[str, object]],
) -> tuple[list[dict[str, object]], int]:
    output: list[dict[str, object]] = []
    realm_unassigned = 0
    for group in groups:
        national_ids = set(group["national_ids"])
        realm_restricted = bool(group["realm_restricted"])
        if national_ids and nation_id not in national_ids:
            continue
        if realm_restricted and not national_ids:
            realm_unassigned += 1
            continue

        requirements = group["requirements"]
        guaranteed_ops = [
            candidate
            for candidate in native_candidates
            if fixed_meets(candidate, requirements)
        ]
        possible_ops = [
            candidate
            for candidate in native_candidates
            if not fixed_meets(candidate, requirements)
            and random_feasible(candidate, requirements)
        ]
        if guaranteed_ops:
            access = "Native guaranteed caster"
            operators = sorted(guaranteed_ops, key=broad_sort_key)
        elif possible_ops:
            access = "Native random-assisted caster"
            operators = sorted(possible_ops, key=broad_sort_key)
        elif national_ids:
            access = "National spell; no native caster"
            operators = []
        else:
            continue
        if realm_restricted:
            access += "; Realm condition"

        output.append(
            {
                **group,
                "access": access,
                "operators": operators,
                "availability": (
                    "National" if national_ids else "Generic"
                ) + (" + Realm" if realm_restricted else ""),
            }
        )
    return output, realm_unassigned


def summon_layer_max(
    groups: list[dict[str, object]],
    *,
    access_prefix: str,
    candidate: bool,
) -> dict[str, int]:
    selected = [
        group
        for group in groups
        if str(group["access"]).startswith(access_prefix)
        and bool(group["candidate"]) == candidate
    ]
    return records_max(flatten_targets(selected))


def nation_profile(
    nation: dict[str, object],
    data,
    hero_by_nation: dict[int, list[dict[str, object]]],
    pretender_by_nation: dict[int, list[dict[str, object]]],
    site_by_nation: dict[int, list[dict[str, object]]],
    summon_groups: list[dict[str, object]],
) -> tuple[dict[str, object], int]:
    nation_id = int(nation["id"])
    native_candidates = collect_candidates(nation_id, data["maps"], data["units"])
    native = max_levels(native_candidates, key="guaranteed")
    native_possible = max_levels(native_candidates, key="possible")
    heroes = hero_by_nation.get(nation_id, [])
    pretenders = pretender_by_nation.get(nation_id, [])
    sites = site_by_nation.get(nation_id, [])
    start_sites = [record for record in sites if record["site_kind"] == "Start Site"]
    future_sites = [record for record in sites if record["site_kind"] == "Future Site"]
    summons, realm_unassigned = summon_access_for_nation(
        nation_id,
        native_candidates,
        summon_groups,
    )

    summon_fixed = summon_layer_max(
        summons,
        access_prefix="Native guaranteed caster",
        candidate=False,
    )
    summon_random_operator = summon_layer_max(
        summons,
        access_prefix="Native random-assisted caster",
        candidate=False,
    )
    summon_candidate = records_max(
        flatten_targets([group for group in summons if group["candidate"]])
    )

    return {
        "nation": nation,
        "native_candidates": native_candidates,
        "native": native,
        "native_possible": native_possible,
        "heroes": heroes,
        "hero_max": records_max(heroes),
        "hero_possible": records_max(heroes, key="possible"),
        "pretenders": pretenders,
        "pretender_base_max": records_max(pretenders),
        "pretender_possible": records_max(pretenders, key="possible"),
        "start_sites": start_sites,
        "start_site_max": records_max(start_sites),
        "start_site_possible": records_max(start_sites, key="possible"),
        "future_sites": future_sites,
        "future_site_max": records_max(future_sites),
        "summons": summons,
        "summon_fixed": summon_fixed,
        "summon_random_operator": summon_random_operator,
        "summon_candidate": summon_candidate,
        "start_gain": gain_map(records_max(start_sites), native),
        "future_gain": gain_map(records_max(future_sites), native),
        "hero_gain": gain_map(records_max(heroes), native),
        "summon_gain": gain_map(summon_fixed, native),
        "summon_random_gain": gain_map(summon_random_operator, native),
        "candidate_gain": gain_map(summon_candidate, native),
        "pretender_base_gain": gain_map(records_max(pretenders), native),
    }, realm_unassigned


def render_unit_magic(record: dict[str, object]) -> str:
    text = level_text(record["guaranteed"])
    if record["random"] != "—":
        text += f"; {record['random']}"
    return text


def render_targets(group: dict[str, object], *, detail: bool = False, limit: int = 5) -> str:
    values: list[str] = []
    for target in group["targets"][:limit]:
        values.append(f"{unit_link(target, detail=detail)}: {esc(render_unit_magic(target))}")
    if len(group["targets"]) > limit:
        values.append(f"ほか{len(group['targets']) - limit}")
    return "; ".join(values) or "—"


def nation_page(profile: dict[str, object]) -> str:
    nation = profile["nation"]
    native = profile["native"]
    lines = front_matter(f"{nation['code']} {nation['name']} 拡張Magic Access")
    lines.extend(
        [
            f"# {nation['code']} {nation['name']} — 拡張Magic Access",
            "",
            f"> **{nation['epithet']}**",
            "",
            f"[通常Recruit](../../recruitment/{nation['dir']}/{nation['slug']}.md) · "
            f"[Site Search能力](../../site-search/{nation['dir']}/{nation['slug']}.md) · "
            f"[国家攻略](../../../nations/{nation['dir']}/{nation['slug']}.md) · "
            "[拡張Accessの読み方](../../../magic/extended-magic-access.md)",
            "",
            '!!! warning "Layerの確度を混同しない"',
            "    Start Site recruit、Hero、Pretender、召喚Mageは利用Timingと確度が異なります。下表の最大値を、一人のMageや同一Turnに同時取得できる値とは解釈しません。",
            "",
            "## 概要",
            "",
            "| Layer | 関係数 | 最大Path | Nativeからの増分 | 確度・Timing |",
            "|---|---:|---|---|---|",
            f"| 通常Recruit | {len(profile['native_candidates'])} | {esc(level_cell(native))} | baseline | ゲーム内Recruit条件 |",
            f"| Nation Start Site mage | {len(profile['start_sites'])} | {esc(level_cell(profile['start_site_max']))} | {esc(gain_text(profile['start_site_max'], native))} | Start Siteは国家属性で明示。実際のRecruit施設条件は別 |",
            f"| Future Site mage | {len(profile['future_sites'])} | {esc(level_cell(profile['future_site_max']))} | {esc(gain_text(profile['future_site_max'], native))} | Future Siteの出現Timing・条件が必要 |",
            f"| Hero mage | {len(profile['heroes'])} | {esc(level_cell(profile['hero_max']))} | {esc(gain_text(profile['hero_max'], native))} | 出現は保証されない |",
            f"| Direct fixed summon | {sum(not group['candidate'] and group['operators'] for group in profile['summons'])} | {esc(level_cell(profile['summon_fixed']))} | {esc(gain_text(profile['summon_fixed'], native))} | Research・Gem・Casterが必要 |",
            f"| Candidate-pool summon | {sum(group['candidate'] and group['operators'] for group in profile['summons'])} | {esc(level_cell(profile['summon_candidate']))} | {esc(gain_text(profile['summon_candidate'], native))} | 候補集合であり結果不確定 |",
            f"| Pretender chassis | {len(profile['pretenders'])} | {esc(level_cell(profile['pretender_base_max']))} | {esc(gain_text(profile['pretender_base_max'], native))} | ゲーム開始前に一体を設計 |",
            "",
            "## Path別Layer比較",
            "",
            "| Path | Native保証 | Start Site | Future Site | Hero | Fixed summon | Random-caster summon | Candidate pool | Pretender base |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for path in PATH_ORDER:
        lines.append(
            f"| {path} — {PATH_NAMES[path]} | "
            f"{native.get(path, 0) or '—'} | "
            f"{profile['start_site_max'].get(path, 0) or '—'} | "
            f"{profile['future_site_max'].get(path, 0) or '—'} | "
            f"{profile['hero_max'].get(path, 0) or '—'} | "
            f"{profile['summon_fixed'].get(path, 0) or '—'} | "
            f"{profile['summon_random_operator'].get(path, 0) or '—'} | "
            f"{profile['summon_candidate'].get(path, 0) or '—'} | "
            f"{profile['pretender_base_max'].get(path, 0) or '—'} |"
        )

    lines.extend(
        [
            "",
            "## Nation Start / Future Site mage",
            "",
            "| Site | Kind | Site Path/Lv | Mage | ID | Magic | Slot | Native重複 |",
            "|---|---|---|---|---:|---|---|---|",
        ]
    )
    native_ids = {int(candidate["id"]) for candidate in profile["native_candidates"]}
    for record in profile["start_sites"] + profile["future_sites"]:
        lines.append(
            f"| {site_link(int(record['site_id']), str(record['site']), detail=True)} | "
            f"{record['site_kind']} | {esc(record['site_path'])} {record['site_level']} | "
            f"{unit_link(record, detail=True)} | {record['id']} | "
            f"{esc(render_unit_magic(record))} | `{esc(record['site_field'])}` | "
            f"{'Yes' if int(record['id']) in native_ids else '—'} |"
        )
    if not profile["start_sites"] and not profile["future_sites"]:
        lines.append("| — | — | — | — | — | — | — | 該当なし |")

    lines.extend(
        [
            "",
            "## Hero mage",
            "",
            "| Hero | ID | Type | Slot | Magic | Late Hero | Nativeからの増分 |",
            "|---|---:|---|---|---|---|---|",
        ]
    )
    for record in profile["heroes"]:
        lines.append(
            f"| {unit_link(record, detail=True)} | {record['id']} | "
            f"{esc(record['hero_type'])} | `{esc(record['slot'])}` | "
            f"{esc(render_unit_magic(record))} | {'Yes' if record['latehero'] else '—'} | "
            f"{esc(gain_text(record['guaranteed'], native))} |"
        )
    if not profile["heroes"]:
        lines.append("| — | — | — | — | — | — | Mage Heroなし |")

    accessible = [group for group in profile["summons"] if group["operators"]]
    blocked = [group for group in profile["summons"] if not group["operators"]]
    lines.extend(
        [
            "",
            "## Native recruitからの一段召喚Mage",
            "",
            "| Spell | Research | Req | Cost | Access | Type | Native caster | Mage target | Path gain |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
    )
    for group in accessible:
        target_max = records_max(group["targets"])
        lines.append(
            f"| {spell_link(group, detail=True)} | {esc(group['research'])} | "
            f"{esc(group['path'])} | {esc(group['cost'])} | {esc(group['access'])} | "
            f"{'Candidate pool' if group['candidate'] else 'Fixed target'} | "
            f"{esc(candidate_names(group['operators']))} | {render_targets(group, detail=True)} | "
            f"{esc(gain_text(target_max, native))} |"
        )
    if not accessible:
        lines.append("| — | — | — | — | — | — | — | — | Native casterによる一段Mage召喚なし |")

    if blocked:
        lines.extend(
            [
                "",
                "### National SpellだがNative casterなし",
                "",
                "| Spell | Research | Req | Target mage | 備考 |",
                "|---|---|---|---|---|",
            ]
        )
        for group in blocked:
            lines.append(
                f"| {spell_link(group, detail=True)} | {esc(group['research'])} | "
                f"{esc(group['path'])} | {render_targets(group, detail=True)} | "
                f"{esc(group['access'])} |"
            )

    lines.extend(
        [
            "",
            "## Pretender chassis",
            "",
            "| Chassis | ID | Base magic | Path cost | Start Dom | Min imprison | Size / HP / Prot | Notes |",
            "|---|---:|---|---:|---:|---:|---|---|",
        ]
    )
    for record in profile["pretenders"]:
        notes: list[str] = []
        if record["immobile"]:
            notes.append("Immobile")
        if not record["guaranteed"] and record["random"] == "—":
            notes.append("No base path")
        lines.append(
            f"| {unit_link(record, detail=True)} | {record['id']} | "
            f"{esc(render_unit_magic(record))} | {esc(record['pathcost'])} | "
            f"{esc(record['startdom'])} | {esc(record['minimprisonment'])} | "
            f"{esc(record['size'])} / {esc(record['hp'])} / {esc(record['prot'])} | "
            f"{esc(', '.join(notes) or '—')} |"
        )
    if not profile["pretenders"]:
        lines.append("| — | — | — | — | — | — | — | Chassis mappingなし |")

    lines.extend(
        [
            "",
            "## 解釈上の注意",
            "",
            "- Heroは国家固有でも、必要Turnまでに出現する保証はありません。",
            "- Pretender欄はChassisの基礎値です。最終Pathは設計Point、Awake / Dormant / Imprisoned、Scales、Blessとの交換条件で決まります。",
            "- Fixed summonでも、Research、Gem、Lab、Casterの生存、Unique状態などが必要です。",
            "- Candidate poolは候補集合です。表にあるMageを一回のCastで必ず得るとは限りません。",
            "- 召喚判定は通常Recruit MageだけをCasterに使う一段計算です。Booster、Communion、Hero、Pretender、Start Site Mage、召喚Mageによる再帰的な連鎖は含みません。",
            "- Realm restricted Spellは国家Realmとの対応データを安全に再構成できないため、National IDで明示されたもの以外は国家へ割り当てません。",
            "- 一般Magic Siteで偶然見つかるMageは国家固有Accessではないため、[Site Recruit索引](../../sites/recruitment.md)で別に扱います。",
            "",
        ]
    )
    return "\n".join(lines)


def index_page(profiles: list[dict[str, object]]) -> str:
    lines = front_matter("国家別拡張Magic Access")
    lines.extend(
        [
            "# 国家別拡張Magic Access",
            "",
            "通常RecruitのMage rosterへ、Start Site、Future Site、Hero、Pretender、Native casterによる一段Mage召喚を重ねます。",
            "",
            "- [拡張Magic Accessの読み方](../../magic/extended-magic-access.md)",
            "- [Path gain比較](path-gains.md)",
            "- [Nation Start / Future Site mage](start-sites.md)",
            "- [Hero mage](heroes.md)",
            "- [一段召喚Mage](summon-mages.md)",
            "- [Pretender base magic](pretenders.md)",
            "- [データ品質・境界](data-quality.md)",
            "",
            '!!! warning "最大値の足し算は禁止"',
            "    Hero、Pretender、Start Site、召喚は同じ確度・Timingではありません。各列はLayer別の最大であり、同じ個体や同じTurnに共存する能力を表しません。",
            "",
        ]
    )
    for era in ("EA", "MA", "LA"):
        lines.extend(
            [
                f"## {era}",
                "",
                "| Nation | Native | Start Site gain | Hero potential | Fixed summon gain | Candidate gain | Pretender base gain | Detail |",
                "|---|---|---|---|---|---|---|---|",
            ]
        )
        for profile in [item for item in profiles if item["nation"]["code"] == era]:
            nation = profile["nation"]
            lines.append(
                f"| {esc(nation['name'])} | {esc(level_cell(profile['native']))} | "
                f"{esc(gain_text(profile['start_site_max'], profile['native']))} | "
                f"{esc(gain_text(profile['hero_max'], profile['native']))} | "
                f"{esc(gain_text(profile['summon_fixed'], profile['native']))} | "
                f"{esc(gain_text(profile['summon_candidate'], profile['native']))} | "
                f"{esc(gain_text(profile['pretender_base_max'], profile['native']))} | "
                f"[表示]({nation['dir']}/{nation['slug']}.md) |"
            )
        lines.append("")
    return "\n".join(lines)


def path_gains_page(profiles: list[dict[str, object]]) -> str:
    lines = front_matter("拡張Magic Access Path gain比較")
    lines.extend(
        [
            "# 拡張Magic Access Path gain比較",
            "",
            "通常Recruitの保証最大を超えるPathだけをLayer別に表示します。`new`はNative保証が0のPathです。",
            "",
            "[国家別拡張Magic Accessへ戻る](index.md)",
            "",
        ]
    )
    for path in PATH_ORDER:
        entries: list[tuple[dict[str, object], list[str]]] = []
        for profile in profiles:
            native = int(profile["native"].get(path, 0))
            sources: list[str] = []
            for label, key in (
                ("Start Site", "start_site_max"),
                ("Future Site", "future_site_max"),
                ("Hero", "hero_max"),
                ("Fixed summon", "summon_fixed"),
                ("Random-caster summon", "summon_random_operator"),
                ("Candidate pool", "summon_candidate"),
                ("Pretender base", "pretender_base_max"),
            ):
                level = int(profile[key].get(path, 0))
                if level > native:
                    sources.append(f"{label} {path}{level}")
            if sources:
                entries.append((profile, sources))
        lines.extend(
            [
                f"## {path} — {PATH_NAMES[path]}（{len(entries)}国家）",
                "",
                "| Nation | Native | 拡張Layer |",
                "|---|---:|---|",
            ]
        )
        for profile, sources in entries:
            nation = profile["nation"]
            lines.append(
                f"| [{nation['code']} {esc(nation['name'])}]({nation['dir']}/{nation['slug']}.md) | "
                f"{profile['native'].get(path, 0) or '—'} | {esc('; '.join(sources))} |"
            )
        if not entries:
            lines.append("| — | — | 該当なし |")
        lines.append("")
    return "\n".join(lines)


def start_sites_page(profiles: list[dict[str, object]]) -> str:
    records: list[tuple[dict[str, object], dict[str, object]]] = []
    for profile in profiles:
        for record in profile["start_sites"] + profile["future_sites"]:
            records.append((profile, record))
    lines = front_matter("国家Start / Future Site mage")
    lines.extend(
        [
            "# 国家Start / Future Site mage",
            "",
            "国家属性が明示するStart Site・Future Siteと、そのSite recordが参照するMage Commanderを結合します。",
            "",
            f"Relation: **{len(records)}**",
            "",
            "| Nation | Site | Kind | Mage | ID | Magic | Slot |",
            "|---|---|---|---|---:|---|---|",
        ]
    )
    for profile, record in records:
        nation = profile["nation"]
        lines.append(
            f"| [{nation['code']} {esc(nation['name'])}]({nation['dir']}/{nation['slug']}.md) | "
            f"{site_link(int(record['site_id']), str(record['site']))} | {record['site_kind']} | "
            f"{unit_link(record)} | {record['id']} | {esc(render_unit_magic(record))} | "
            f"`{esc(record['site_field'])}` |"
        )
    if not records:
        lines.append("| — | — | — | — | — | — | — |")
    lines.extend(
        [
            "",
            "Start Siteが国家に保証されても、Commanderの実際のRecruitにはFort、Lab、Temple、Recruit Point、国家制限などが関係する場合があります。Future Siteはさらに出現Timing・条件を確認してください。",
            "",
        ]
    )
    return "\n".join(lines)


def heroes_page(profiles: list[dict[str, object]]) -> str:
    records: list[tuple[dict[str, object], dict[str, object]]] = []
    for profile in profiles:
        for record in profile["heroes"]:
            records.append((profile, record))
    lines = front_matter("国家Hero mage")
    lines.extend(
        [
            "# 国家Hero mage",
            "",
            "国家Hero mappingのうち、固定PathまたはRandom Pathを持つUnitを抽出します。",
            "",
            f"Relation: **{len(records)}**",
            "",
            "| Nation | Hero | ID | Type | Slot | Magic | Late Hero | Native gain |",
            "|---|---|---:|---|---|---|---|---|",
        ]
    )
    for profile, record in records:
        nation = profile["nation"]
        lines.append(
            f"| [{nation['code']} {esc(nation['name'])}]({nation['dir']}/{nation['slug']}.md) | "
            f"{unit_link(record)} | {record['id']} | {esc(record['hero_type'])} | "
            f"`{esc(record['slot'])}` | {esc(render_unit_magic(record))} | "
            f"{'Yes' if record['latehero'] else '—'} | "
            f"{esc(gain_text(record['guaranteed'], profile['native']))} |"
        )
    if not records:
        lines.append("| — | — | — | — | — | — | — | — |")
    lines.extend(["", "Heroは出現を国家計画の必須前提にしないでください。", ""])
    return "\n".join(lines)


def summons_page(profiles: list[dict[str, object]]) -> str:
    relations: list[tuple[dict[str, object], dict[str, object]]] = []
    for profile in profiles:
        for group in profile["summons"]:
            relations.append((profile, group))
    lines = front_matter("国家別一段召喚Mage")
    lines.extend(
        [
            "# 国家別一段召喚Mage",
            "",
            "通常Recruit MageだけをCasterに使い、一回のSpell summonで得られるMageを国家別に整理します。再帰的な召喚Chainは計算しません。",
            "",
            f"Nation–Spell relation: **{len(relations)}**",
            "",
            "| Nation | Spell | Research | Req | Access | Type | Operator | Mage target | Native gain |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
    )
    for profile, group in relations:
        nation = profile["nation"]
        target_max = records_max(group["targets"])
        lines.append(
            f"| [{nation['code']} {esc(nation['name'])}]({nation['dir']}/{nation['slug']}.md) | "
            f"{spell_link(group)} | {esc(group['research'])} | {esc(group['path'])} | "
            f"{esc(group['access'])} | {'Candidate pool' if group['candidate'] else 'Fixed'} | "
            f"{esc(candidate_names(group['operators']))} | {render_targets(group)} | "
            f"{esc(gain_text(target_max, profile['native']))} |"
        )
    if not relations:
        lines.append("| — | — | — | — | — | — | — | — | — |")
    lines.extend(
        [
            "",
            "- `National spell; no native caster`はSpell自体が国家に紐付くものの、通常Recruit Mageだけでは要求Pathを満たさない関係です。",
            "- Candidate poolは候補Unitの一覧であり、結果保証ではありません。",
            "- Booster、Communion、Pretender、Hero、Start Site Mage、召喚Mageによる追加到達は含みません。",
            "",
        ]
    )
    return "\n".join(lines)


def pretenders_page(profiles: list[dict[str, object]]) -> str:
    lines = front_matter("国家別Pretender base magic")
    lines.extend(
        [
            "# 国家別Pretender base magic",
            "",
            "各国家が選べるPretender chassisの基礎Pathを比較します。最終設計PathやBlessの強さを評価するTier表ではありません。",
            "",
            "| Nation | Chassis数 | Base magic最大 | Random込み理論最大 | Path cost範囲 | Detail |",
            "|---|---:|---|---|---|---|",
        ]
    )
    for profile in profiles:
        nation = profile["nation"]
        numeric_costs = [
            int(str(record["pathcost"]))
            for record in profile["pretenders"]
            if str(record["pathcost"]).lstrip("-").isdigit()
        ]
        cost_range = (
            f"{min(numeric_costs)}–{max(numeric_costs)}" if numeric_costs else "—"
        )
        lines.append(
            f"| {nation['code']} {esc(nation['name'])} | {len(profile['pretenders'])} | "
            f"{esc(level_cell(profile['pretender_base_max']))} | "
            f"{esc(level_cell(profile['pretender_possible']))} | {cost_range} | "
            f"[表示]({nation['dir']}/{nation['slug']}.md#pretender-chassis) |"
        )
    lines.extend(
        [
            "",
            "Chassisの基礎Pathが0でも、Pretender designでPathを購入できる場合があります。購入可否・費用・最終Design Pointはゲーム内Pretender画面を優先してください。",
            "",
        ]
    )
    return "\n".join(lines)


def quality_page(stats: dict[str, int], unresolved_sites: list[tuple[int, int]]) -> str:
    lines = front_matter("拡張Magic Accessデータ品質")
    lines.extend(
        [
            "# 拡張Magic Accessデータ品質・境界",
            "",
            "## 生成件数",
            "",
            "| 項目 | 件数 |",
            "|---|---:|",
        ]
    )
    for key in sorted(stats):
        lines.append(f"| `{key}` | {stats[key]} |")
    lines.extend(
        [
            "",
            "## Access Layerの意味",
            "",
            "| Layer | 何を確認したか | 国家計画での確度 |",
            "|---|---|---|",
            "| Native recruit | Fort / non-fort / coastal commander mapping | 最も再現性が高い基礎 |",
            "| Start Site | 国家属性→Site ID→Commander recruit field | 国家固有だが施設条件は別 |",
            "| Future Site | 国家属性→Future Site | Timing・発生条件が必要 |",
            "| Hero | 国家Hero slot→Unit ID | 出現Turn・出現自体が不確定 |",
            "| Pretender | 国家→Chassis mapping | ゲーム開始前に一体を選ぶ |",
            "| Fixed summon | Spell→固定Mage Unit | Research・Gem・Casterが必要 |",
            "| Candidate summon | Spell→候補集合内Mage | 候補であり結果不確定 |",
            "",
            "## 意図的に含めないもの",
            "",
            "- Booster、Empowerment、Communion / SabbathによるCaster到達。",
            "- Hero、Pretender、Start Site Mage、召喚MageをCasterにした再帰的Summon chain。",
            "- 一般Magic Siteを偶然発見して得る非国家固有Mage。",
            "- Mercenary・Event加入Mage。",
            "- Realmだけで制限され、国家Realm対応を安全に決められないSpell。",
            "- Gold cost、Commander Point、Research機会費用、Unique生存状態。",
            "",
            "## 未解決参照",
            "",
        ]
    )
    if unresolved_sites:
        lines.extend(["| Nation ID | Site ID |", "|---:|---:|"])
        for nation_id, site_id in unresolved_sites:
            lines.append(f"| {nation_id} | {site_id} |")
    else:
        lines.append("Start / Future Site参照の未解決IDはありません。")
    lines.append("")
    return "\n".join(lines)


def _insert_after(path: Path, anchor: str, additions: list[str]) -> bool:
    if not path.exists():
        raise FileNotFoundError(f"required generated page missing: {path}")
    text = path.read_text(encoding="utf-8")
    if additions and additions[0] in text:
        return False
    if anchor not in text:
        raise ValueError(f"anchor not found in {path}: {anchor!r}")
    path.write_text(
        text.replace(anchor, anchor + "\n" + "\n".join(additions), 1),
        encoding="utf-8",
    )
    return True


def patch_navigation_and_indexes(profiles: list[dict[str, object]]) -> dict[str, int]:
    changes = Counter()
    changes["navigation"] += _insert_after(
        CONFIG,
        '    "data/site-search/data-quality.md",',
        [
            '    "data/extended-magic-access/index.md",',
            '    "data/extended-magic-access/path-gains.md",',
            '    "data/extended-magic-access/start-sites.md",',
            '    "data/extended-magic-access/heroes.md",',
            '    "data/extended-magic-access/summon-mages.md",',
            '    "data/extended-magic-access/pretenders.md",',
            '    "data/extended-magic-access/data-quality.md",',
        ],
    )
    changes["data_index"] += _insert_after(
        DATA_INDEX,
        "- [国家別Site Search能力](site-search/index.md)",
        ["- [国家別拡張Magic Access](extended-magic-access/index.md)"],
    )
    changes["mage_access"] += _insert_after(
        MAGE_ACCESS,
        "- [国家別Site Search能力](site-search/index.md)",
        ["- [国家別拡張Magic Access](extended-magic-access/index.md)"],
    )
    changes["site_search_index"] += _insert_after(
        SITE_SEARCH_INDEX,
        "- [データ品質・判定基準](data-quality.md)",
        ["- [国家別拡張Magic Access](../extended-magic-access/index.md)"],
    )
    changes["guide"] += _insert_after(
        SITE_SEARCH_GUIDE,
        "- [国家別Site Search能力](../data/site-search/index.md)",
        ["- [国家別拡張Magic Access](../data/extended-magic-access/index.md)"],
    )
    changes["playbook"] += _insert_after(
        SITE_SEARCH_PLAYBOOK,
        "- [国家別Site Search能力](../data/site-search/index.md)",
        ["- [国家別拡張Magic Access](../data/extended-magic-access/index.md)"],
    )

    for profile in profiles:
        nation = profile["nation"]
        detail_link = (
            f"[拡張Magic Access]"
            f"(../../extended-magic-access/{nation['dir']}/{nation['slug']}.md)"
        )
        recruit_path = RECRUIT_ROOT / str(nation["dir"]) / f"{nation['slug']}.md"
        site_path = SITE_SEARCH_ROOT / str(nation["dir"]) / f"{nation['slug']}.md"
        changes["recruit_pages"] += _insert_after(
            recruit_path,
            f"[Site Search能力](../../site-search/{nation['dir']}/{nation['slug']}.md)",
            [f" · {detail_link}"],
        )
        changes["site_search_pages"] += _insert_after(
            site_path,
            f"[Recruitデータ](../../recruitment/{nation['dir']}/{nation['slug']}.md)",
            [f" · {detail_link}"],
        )
    return dict(changes)


def validate(
    profiles: list[dict[str, object]],
    stats: dict[str, int],
    unresolved_sites: list[tuple[int, int]],
) -> None:
    if len(profiles) != 103:
        raise ValueError(f"nation profile count mismatch: {len(profiles)}")
    if stats["hero_mage_relations"] < 25:
        raise ValueError("Hero mage relation set appears incomplete")
    if stats["pretender_relations"] < 500:
        raise ValueError("Pretender relation set appears incomplete")
    if stats["start_future_site_mage_relations"] < 10:
        raise ValueError("Start / Future Site mage relation set appears incomplete")
    if stats["summon_mage_groups"] < 20:
        raise ValueError("Summon mage group set appears incomplete")
    if stats["unresolved_summon_spells"]:
        raise ValueError(
            f"unresolved summon Spell rows: {stats['unresolved_summon_spells']}"
        )
    if unresolved_sites:
        raise ValueError(f"unresolved national Site IDs: {len(unresolved_sites)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    data = load_unit_catalog(args.refresh, args.offline)
    heroes = reverse_hero_records(data)
    pretenders = reverse_pretender_records(data)
    sites, unresolved_sites = start_site_records(data)
    summon_groups, summon_stats = build_summon_groups(data)

    profiles: list[dict[str, object]] = []
    realm_unassigned_total = 0
    for nation in data["nations"]:
        profile, realm_unassigned = nation_profile(
            nation,
            data,
            heroes,
            pretenders,
            sites,
            summon_groups,
        )
        profiles.append(profile)
        realm_unassigned_total += realm_unassigned
    profiles.sort(key=lambda item: (item["nation"]["code"], int(item["nation"]["id"])))

    OUT.mkdir(parents=True, exist_ok=True)
    for era in ("ea", "ma", "la"):
        (OUT / era).mkdir(parents=True, exist_ok=True)
    for profile in profiles:
        nation = profile["nation"]
        path = OUT / str(nation["dir"]) / f"{nation['slug']}.md"
        path.write_text(nation_page(profile), encoding="utf-8")

    stats = {
        "nation_profiles": len(profiles),
        "nation_detail_pages": len(profiles),
        "hero_mage_relations": sum(len(profile["heroes"]) for profile in profiles),
        "pretender_relations": sum(len(profile["pretenders"]) for profile in profiles),
        "start_site_mage_relations": sum(len(profile["start_sites"]) for profile in profiles),
        "future_site_mage_relations": sum(len(profile["future_sites"]) for profile in profiles),
        "start_future_site_mage_relations": sum(
            len(profile["start_sites"]) + len(profile["future_sites"])
            for profile in profiles
        ),
        "nation_summon_relations": sum(len(profile["summons"]) for profile in profiles),
        "native_guaranteed_summon_relations": sum(
            str(group["access"]).startswith("Native guaranteed caster")
            for profile in profiles
            for group in profile["summons"]
        ),
        "native_random_summon_relations": sum(
            str(group["access"]).startswith("Native random-assisted caster")
            for profile in profiles
            for group in profile["summons"]
        ),
        "national_blocked_summon_relations": sum(
            str(group["access"]).startswith("National spell; no native caster")
            for profile in profiles
            for group in profile["summons"]
        ),
        "candidate_pool_relations": sum(
            bool(group["candidate"])
            for profile in profiles
            for group in profile["summons"]
        ),
        "realm_unassigned_nation_spell_checks": realm_unassigned_total,
        **summon_stats,
    }

    (OUT / "index.md").write_text(index_page(profiles), encoding="utf-8")
    (OUT / "path-gains.md").write_text(path_gains_page(profiles), encoding="utf-8")
    (OUT / "start-sites.md").write_text(start_sites_page(profiles), encoding="utf-8")
    (OUT / "heroes.md").write_text(heroes_page(profiles), encoding="utf-8")
    (OUT / "summon-mages.md").write_text(summons_page(profiles), encoding="utf-8")
    (OUT / "pretenders.md").write_text(pretenders_page(profiles), encoding="utf-8")
    (OUT / "data-quality.md").write_text(
        quality_page(stats, unresolved_sites),
        encoding="utf-8",
    )

    validate(profiles, stats, unresolved_sites)
    patch_counts = patch_navigation_and_indexes(profiles)

    print(f"source commit: {COMMIT}")
    for key, value in stats.items():
        print(f"{key}: {value}")
    for key, value in patch_counts.items():
        print(f"patched_{key}: {value}")


if __name__ == "__main__":
    main()
