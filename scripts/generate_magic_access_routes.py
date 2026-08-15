#!/usr/bin/env python3
"""Generate nation-level Magic Access route profiles.

The route layer connects four deliberately separate mechanisms:

- self-forged path-booster chains for strategic magic,
- fixed-target recursive mage summon chains,
- Communion / Sabbath battle-only path reach,
- remaining strategic path gaps that may require Empowerment or external access.

Generated data is conservative:
- booster chains use one native mage as a single forger,
- standard humanoid slot capacities are assumed,
- recursive summons use fixed targets and stop at depth three,
- candidate pools are not propagated,
- Communion / Sabbath never count toward Ritual or Forge access.
"""
from __future__ import annotations

import argparse
import itertools
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Iterable

from generate_extended_magic_access_data import (
    build_summon_groups,
    spell_link as extended_spell_link,
)
from generate_nation_site_search_data import (
    ARCANE_PATHS,
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
)
from generate_recruitment_data import (
    COMMIT,
    esc,
    num,
    random_text,
    tsv,
    yes,
)
from generate_spell_item_data import (
    FORGE_COST,
    ITEM_TYPES,
    SCHOOLS,
    item_gem_cost,
    item_requirement,
)
from unit_catalog_special_integration import load_unit_catalog

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "data" / "magic-access-routes"

MAX_FORGES = 3
MAX_SUMMON_DEPTH = 3
COMMUNION_BREAKPOINTS = ((2, 1), (4, 2), (8, 3), (16, 4), (32, 5))

SLOT_CAPACITY = {
    "hand": 2,
    "head": 1,
    "body": 1,
    "boots": 1,
    "misc": 2,
}
ITEM_SLOT_USAGE = {
    "1-h wpn": {"hand": 1},
    "shield": {"hand": 1},
    "2-h wpn": {"hand": 2},
    "missile": {"hand": 2},
    "armor": {"body": 1},
    "helm": {"head": 1},
    "crown": {"head": 1},
    "boots": {"boots": 1},
    "misc": {"misc": 1},
    "barding": {"barding": 1},
}


def path_requirements(row: dict[str, str]) -> dict[str, int]:
    requirements: dict[str, int] = {}
    for path_key, level_key in (
        ("mainpath", "mainlevel"),
        ("secondarypath", "secondarylevel"),
    ):
        path = (row.get(path_key) or "").strip()
        level = num(row, level_key)
        if path in PATH_ORDER and level > 0:
            requirements[path] = max(requirements.get(path, 0), level)
    return requirements


def path_boosts(row: dict[str, str]) -> dict[str, int]:
    return {
        path: num(row, path)
        for path in PATH_ORDER
        if num(row, path) > 0
    }


def restriction_ids(row: dict[str, str]) -> set[int]:
    return {
        num(row, f"restricted{index}")
        for index in range(1, 7)
        if num(row, f"restricted{index}") > 0
    }


def slot_usage(item_type: str) -> dict[str, int]:
    return dict(ITEM_SLOT_USAGE.get(item_type, {}))


def loadout_compatible(items: Iterable[dict[str, object]]) -> bool:
    used: dict[str, int] = defaultdict(int)
    for item in items:
        usage = item["slot_usage"]
        if "barding" in usage:
            return False
        for slot, amount in usage.items():
            used[slot] += int(amount)
            if used[slot] > SLOT_CAPACITY.get(slot, 0):
                return False
    return True


def add_levels(base: dict[str, int], items: Iterable[dict[str, object]]) -> dict[str, int]:
    levels = dict(base)
    for item in items:
        for path, bonus in item["boosts"].items():
            levels[path] = levels.get(path, 0) + int(bonus)
    return {path: level for path, level in levels.items() if level > 0}


def meets(levels: dict[str, int], requirements: dict[str, int]) -> bool:
    return all(levels.get(path, 0) >= level for path, level in requirements.items())


def load_boosters(data) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    forgeable: list[dict[str, object]] = []
    unforgeable: list[dict[str, object]] = []
    rows = tsv(data["paths"]["BaseI.csv"])
    for row in rows:
        name = (row.get("name") or "").strip()
        item_type = (row.get("type") or "").strip()
        boosts = path_boosts(row)
        const = num(row, "constlevel")
        if not name or not boosts or item_type not in ITEM_TYPES or const <= 0:
            continue
        record = {
            "id": num(row, "id"),
            "name": name,
            "row": row,
            "type": item_type,
            "type_title": ITEM_TYPES[item_type][0],
            "type_slug": ITEM_TYPES[item_type][1],
            "const": const,
            "construction": "Unforgeable" if const == 12 else f"Construction {const}",
            "requirements": path_requirements(row),
            "requirement_text": item_requirement(row),
            "cost": item_gem_cost(row),
            "boosts": boosts,
            "boost_text": level_text(boosts),
            "restrictions": restriction_ids(row),
            "slot_usage": slot_usage(item_type),
            "slot": "/".join(slot_usage(item_type)) or "special",
            "standard_slot": "barding" not in slot_usage(item_type),
            "matrix": bool(num(row, "comslave")) or "matrix" in name.lower(),
        }
        if const == 12:
            unforgeable.append(record)
        else:
            forgeable.append(record)
    key = lambda item: (
        int(item["const"]),
        str(item["type_title"]),
        str(item["name"]),
        int(item["id"]),
    )
    forgeable.sort(key=key)
    unforgeable.sort(key=key)
    return forgeable, unforgeable


def allowed_boosters(
    boosters: list[dict[str, object]],
    nation_id: int,
) -> list[dict[str, object]]:
    return [
        item
        for item in boosters
        if item["standard_slot"]
        and (
            not item["restrictions"]
            or nation_id in item["restrictions"]
        )
    ]


def compatible_loadouts(
    owned_ids: frozenset[int],
    item_by_id: dict[int, dict[str, object]],
) -> list[tuple[tuple[int, ...], dict[str, int]]]:
    item_ids = sorted(owned_ids)
    output: list[tuple[tuple[int, ...], dict[str, int]]] = []
    for size in range(len(item_ids) + 1):
        for subset in itertools.combinations(item_ids, size):
            items = [item_by_id[item_id] for item_id in subset]
            if loadout_compatible(items):
                output.append((subset, {}))
    return output


def route_search(
    base_levels: dict[str, int],
    boosters: list[dict[str, object]],
) -> dict[str, object]:
    item_by_id = {int(item["id"]): item for item in boosters}
    start = frozenset()
    queue: deque[frozenset[int]] = deque([start])
    depth = {start: 0}
    route: dict[frozenset[int], tuple[int, ...]] = {start: ()}
    reachable_items: set[int] = set()
    evaluated_loadouts: dict[frozenset[int], list[tuple[tuple[int, ...], dict[str, int]]]] = {}

    def states_for(owned: frozenset[int]):
        if owned in evaluated_loadouts:
            return evaluated_loadouts[owned]
        states: list[tuple[tuple[int, ...], dict[str, int]]] = []
        for subset, _unused in compatible_loadouts(owned, item_by_id):
            levels = add_levels(base_levels, (item_by_id[item_id] for item_id in subset))
            states.append((subset, levels))
        evaluated_loadouts[owned] = states
        return states

    while queue:
        owned = queue.popleft()
        current_depth = depth[owned]
        if current_depth >= MAX_FORGES:
            continue
        states = states_for(owned)
        for item in boosters:
            item_id = int(item["id"])
            if item_id in owned:
                continue
            if not any(meets(levels, item["requirements"]) for _subset, levels in states):
                continue
            new_owned = frozenset(set(owned) | {item_id})
            reachable_items.add(item_id)
            if new_owned in depth:
                continue
            depth[new_owned] = current_depth + 1
            route[new_owned] = route[owned] + (item_id,)
            queue.append(new_owned)

    best_by_path: dict[str, dict[str, object]] = {}
    state_count = len(depth)
    loadout_count = 0
    for owned in depth:
        forged_route = route[owned]
        for subset, levels in states_for(owned):
            loadout_count += 1
            for path in PATH_ORDER:
                level = int(levels.get(path, 0))
                base = int(base_levels.get(path, 0))
                if level <= base:
                    continue
                candidate = {
                    "path": path,
                    "level": level,
                    "base": base,
                    "route_ids": forged_route,
                    "equipped_ids": subset,
                    "forge_count": len(forged_route),
                    "max_const": max(
                        (int(item_by_id[item_id]["const"]) for item_id in forged_route),
                        default=0,
                    ),
                    "route_cost": " + ".join(
                        str(item_by_id[item_id]["cost"])
                        for item_id in forged_route
                    ) or "—",
                }
                old = best_by_path.get(path)
                score = (
                    level,
                    -len(forged_route),
                    -candidate["max_const"],
                    -len(subset),
                )
                old_score = (
                    int(old["level"]),
                    -int(old["forge_count"]),
                    -int(old["max_const"]),
                    -len(old["equipped_ids"]),
                ) if old else None
                if old is None or score > old_score:
                    best_by_path[path] = candidate

    return {
        "best_by_path": best_by_path,
        "reachable_item_ids": reachable_items,
        "states": state_count,
        "loadouts": loadout_count,
        "item_by_id": item_by_id,
    }


def route_item_names(route: dict[str, object], item_by_id) -> str:
    values = [item_by_id[item_id]["name"] for item_id in route["route_ids"]]
    return " → ".join(values) or "—"


def equipped_item_names(route: dict[str, object], item_by_id) -> str:
    values = [item_by_id[item_id]["name"] for item_id in route["equipped_ids"]]
    return ", ".join(values) or "—"


def candidate_base(candidate: dict[str, object], possible: bool = False) -> dict[str, int]:
    return dict(candidate["possible"] if possible else candidate["guaranteed"])


def best_booster_routes(
    nation_id: int,
    candidates: list[dict[str, object]],
    boosters: list[dict[str, object]],
    *,
    possible: bool = False,
) -> tuple[dict[str, dict[str, object]], dict[str, int]]:
    allowed = allowed_boosters(boosters, nation_id)
    cache: dict[tuple[tuple[str, int], ...], dict[str, object]] = {}
    best: dict[str, dict[str, object]] = {}
    stats = {"route_states": 0, "loadouts": 0, "candidate_searches": 0}
    for candidate in candidates:
        base = candidate_base(candidate, possible=possible)
        signature = tuple(sorted(base.items()))
        if signature not in cache:
            cache[signature] = route_search(base, allowed)
            stats["route_states"] += int(cache[signature]["states"])
            stats["loadouts"] += int(cache[signature]["loadouts"])
            stats["candidate_searches"] += 1
        result = cache[signature]
        for path, route in result["best_by_path"].items():
            entry = {
                **route,
                "candidate": candidate,
                "possible": possible,
                "item_by_id": result["item_by_id"],
            }
            old = best.get(path)
            score = (
                int(entry["level"]),
                -int(entry["forge_count"]),
                0 if candidate.get("any_fort") else -1,
                -int(entry["max_const"]),
            )
            old_score = (
                int(old["level"]),
                -int(old["forge_count"]),
                0 if old["candidate"].get("any_fort") else -1,
                -int(old["max_const"]),
            ) if old else None
            if old is None or score > old_score:
                best[path] = entry
    return best, stats


def summon_group_available(group: dict[str, object], nation_id: int) -> bool:
    national_ids = set(group["national_ids"])
    if national_ids and nation_id not in national_ids:
        return False
    if bool(group["realm_restricted"]) and not national_ids:
        return False
    return not bool(group["candidate"])


def caster_record(
    candidate: dict[str, object],
    *,
    depth: int = 0,
    route: tuple[dict[str, object], ...] = (),
    possible: bool = False,
) -> dict[str, object]:
    return {
        "id": int(candidate["id"]),
        "name": str(candidate["name"]),
        "row": candidate["row"],
        "guaranteed": dict(candidate["guaranteed"]),
        "possible": dict(candidate["possible"]),
        "levels": dict(candidate["possible"] if possible else candidate["guaranteed"]),
        "depth": depth,
        "route": route,
        "native": depth == 0,
        "random_mode": possible,
    }


def target_caster_record(
    target: dict[str, object],
    *,
    depth: int,
    route: tuple[dict[str, object], ...],
    possible: bool,
) -> dict[str, object]:
    return {
        "id": int(target["id"]),
        "name": str(target["name"]),
        "row": target["row"],
        "guaranteed": dict(target["guaranteed"]),
        "possible": dict(target["possible"]),
        "levels": dict(target["possible"] if possible else target["guaranteed"]),
        "depth": depth,
        "route": route,
        "native": False,
        "random_mode": possible,
    }


def levels_meet(levels: dict[str, int], requirements: dict[str, int]) -> bool:
    return all(levels.get(path, 0) >= level for path, level in requirements.items())


def fixed_summon_chain(
    nation_id: int,
    candidates: list[dict[str, object]],
    groups: list[dict[str, object]],
    *,
    possible: bool = False,
) -> dict[str, object]:
    available = [
        group
        for group in groups
        if summon_group_available(group, nation_id)
    ]
    reachable: dict[int, dict[str, object]] = {}
    for candidate in candidates:
        record = caster_record(candidate, possible=possible)
        existing = reachable.get(record["id"])
        if existing is None or sum(record["levels"].values()) > sum(existing["levels"].values()):
            reachable[record["id"]] = record

    new_relations: list[dict[str, object]] = []
    depth_counts: Counter[int] = Counter()
    used_groups: set[tuple[int, int, int]] = set()

    for depth in range(1, MAX_SUMMON_DEPTH + 1):
        additions: list[dict[str, object]] = []
        pending_ids: set[int] = set()
        casters = sorted(
            reachable.values(),
            key=lambda item: (
                int(item["depth"]),
                str(item["name"]),
                int(item["id"]),
            ),
        )
        for group in available:
            operators = [
                caster
                for caster in casters
                if levels_meet(caster["levels"], group["requirements"])
            ]
            if not operators:
                continue
            operator = operators[0]
            for target in group["targets"]:
                target_id = int(target["id"])
                if target_id in reachable or target_id in pending_ids:
                    continue
                relation_key = (int(group["spell_id"]), int(operator["id"]), target_id)
                if relation_key in used_groups:
                    continue
                used_groups.add(relation_key)
                step = {
                    "depth": depth,
                    "spell_id": int(group["spell_id"]),
                    "spell": str(group["spell"]),
                    "school": str(group["school"]),
                    "school_slug": str(group["school_slug"]),
                    "research": str(group["research"]),
                    "path": str(group["path"]),
                    "cost": str(group["cost"]),
                    "requirements": dict(group["requirements"]),
                    "caster_id": int(operator["id"]),
                    "caster": str(operator["name"]),
                    "target_id": target_id,
                    "target": str(target["name"]),
                    "target_magic": dict(target["possible"] if possible else target["guaranteed"]),
                    "availability": (
                        "National" if group["national_ids"] else "Generic"
                    ),
                    "route": tuple(operator["route"]),
                    "possible": possible,
                }
                full_route = tuple(operator["route"]) + (step,)
                additions.append(
                    target_caster_record(
                        target,
                        depth=depth,
                        route=full_route,
                        possible=possible,
                    )
                )
                pending_ids.add(target_id)
                new_relations.append(step)
                depth_counts[depth] += 1
        if not additions:
            break
        for record in additions:
            reachable.setdefault(int(record["id"]), record)

    max_levels_out = {path: 0 for path in PATH_ORDER}
    for record in reachable.values():
        for path, level in record["levels"].items():
            max_levels_out[path] = max(max_levels_out[path], int(level))

    frontier = 0
    for group in available:
        if any(
            levels_meet(caster["levels"], group["requirements"])
            for caster in reachable.values()
        ):
            for target in group["targets"]:
                if int(target["id"]) not in reachable:
                    frontier += 1

    return {
        "reachable": reachable,
        "relations": new_relations,
        "depth_counts": dict(depth_counts),
        "max_levels": max_levels_out,
        "frontier": frontier,
    }


def candidate_pool_opportunities(
    nation_id: int,
    candidates: list[dict[str, object]],
    groups: list[dict[str, object]],
) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for group in groups:
        if not group["candidate"]:
            continue
        national_ids = set(group["national_ids"])
        if national_ids and nation_id not in national_ids:
            continue
        if bool(group["realm_restricted"]) and not national_ids:
            continue
        guaranteed = [
            candidate
            for candidate in candidates
            if fixed_meets(candidate, group["requirements"])
        ]
        possible = [
            candidate
            for candidate in candidates
            if not fixed_meets(candidate, group["requirements"])
            and random_feasible(candidate, group["requirements"])
        ]
        if not guaranteed and not possible:
            continue
        output.append(
            {
                **group,
                "guaranteed_operators": sorted(guaranteed, key=broad_sort_key),
                "possible_operators": sorted(possible, key=broad_sort_key),
            }
        )
    return output


def boosted_master_levels(levels: dict[str, int], bonus: int) -> dict[str, int]:
    return {
        path: level + bonus
        for path, level in levels.items()
        if path in ARCANE_PATHS and level > 0
    }


def communion_profile(
    candidates: list[dict[str, object]],
    path: str,
    label: str,
) -> dict[str, object]:
    guaranteed = [
        candidate
        for candidate in candidates
        if int(candidate["guaranteed"].get(path, 0)) >= 1
    ]
    possible = [
        candidate
        for candidate in candidates
        if int(candidate["guaranteed"].get(path, 0)) < 1
        and int(candidate["possible"].get(path, 0)) >= 1
    ]
    breakpoints: list[dict[str, object]] = []
    for slaves, bonus in COMMUNION_BREAKPOINTS:
        best_levels = {arcane: 0 for arcane in ARCANE_PATHS}
        best_masters: dict[str, dict[str, object]] = {}
        for candidate in guaranteed:
            levels = boosted_master_levels(candidate["guaranteed"], bonus)
            for arcane, level in levels.items():
                if level > best_levels[arcane]:
                    best_levels[arcane] = level
                    best_masters[arcane] = candidate
        breakpoints.append(
            {
                "slaves": slaves,
                "bonus": bonus,
                "levels": best_levels,
                "masters": best_masters,
            }
        )
    return {
        "label": label,
        "path": path,
        "guaranteed": guaranteed,
        "possible": possible,
        "breakpoints": breakpoints,
    }


def strategic_union(*levels_sets: dict[str, int]) -> dict[str, int]:
    result = {path: 0 for path in PATH_ORDER}
    for levels in levels_sets:
        for path, level in levels.items():
            result[path] = max(result[path], int(level))
    return result


def profile_for_nation(
    nation: dict[str, object],
    data,
    boosters: list[dict[str, object]],
    unforgeable: list[dict[str, object]],
    summon_groups: list[dict[str, object]],
) -> tuple[dict[str, object], dict[str, int]]:
    nation_id = int(nation["id"])
    candidates = collect_candidates(nation_id, data["maps"], data["units"])
    native = max_levels(candidates, key="guaranteed")
    native_possible = max_levels(candidates, key="possible")
    booster, booster_stats = best_booster_routes(
        nation_id,
        candidates,
        boosters,
        possible=False,
    )
    booster_possible, booster_possible_stats = best_booster_routes(
        nation_id,
        candidates,
        boosters,
        possible=True,
    )
    booster_max = dict(native)
    booster_possible_max = dict(native_possible)
    for path, route in booster.items():
        booster_max[path] = max(booster_max.get(path, 0), int(route["level"]))
    for path, route in booster_possible.items():
        booster_possible_max[path] = max(
            booster_possible_max.get(path, 0),
            int(route["level"]),
        )

    fixed_chain = fixed_summon_chain(
        nation_id,
        candidates,
        summon_groups,
        possible=False,
    )
    possible_chain = fixed_summon_chain(
        nation_id,
        candidates,
        summon_groups,
        possible=True,
    )
    candidate_pools = candidate_pool_opportunities(
        nation_id,
        candidates,
        summon_groups,
    )
    communion = communion_profile(candidates, "S", "Communion")
    sabbath = communion_profile(candidates, "B", "Sabbath")

    planned = strategic_union(native, booster_max, fixed_chain["max_levels"])
    conditional = strategic_union(
        native_possible,
        booster_possible_max,
        possible_chain["max_levels"],
    )
    gaps = [
        path
        for path in ARCANE_PATHS
        if int(planned.get(path, 0)) <= 0
    ]
    new_paths = [
        path
        for path in ARCANE_PATHS
        if int(native.get(path, 0)) <= 0 and int(planned.get(path, 0)) > 0
    ]

    allowed_unforgeable = [
        item
        for item in unforgeable
        if not item["restrictions"] or nation_id in item["restrictions"]
    ]
    matrix_items = [
        item
        for item in allowed_boosters(boosters, nation_id) + allowed_unforgeable
        if item["matrix"]
    ]

    return {
        "nation": nation,
        "candidates": candidates,
        "native": native,
        "native_possible": native_possible,
        "booster": booster,
        "booster_possible": booster_possible,
        "booster_max": booster_max,
        "booster_possible_max": booster_possible_max,
        "fixed_chain": fixed_chain,
        "possible_chain": possible_chain,
        "candidate_pools": candidate_pools,
        "communion": communion,
        "sabbath": sabbath,
        "planned": planned,
        "conditional": conditional,
        "gaps": gaps,
        "new_paths": new_paths,
        "matrix_items": matrix_items,
    }, {
        **booster_stats,
        "possible_route_states": booster_possible_stats["route_states"],
        "possible_loadouts": booster_possible_stats["loadouts"],
        "possible_candidate_searches": booster_possible_stats["candidate_searches"],
    }


def unit_link(unit_id: int, name: str, *, detail: bool = False) -> str:
    prefix = "../../units/by-id" if detail else "../units/by-id"
    return f"[{esc(name)}]({prefix}/{unit_id:04d}.md)"


def spell_link(step: dict[str, object], *, detail: bool = False) -> str:
    prefix = "../../spells/by-school" if detail else "../spells/by-school"
    return f"[{esc(step['spell'])}]({prefix}/{step['school_slug']}.md)"


def candidate_names(candidates: list[dict[str, object]], limit: int = 3) -> str:
    values = [
        f"{candidate['name']} #{candidate['id']}"
        for candidate in candidates[:limit]
    ]
    if len(candidates) > limit:
        values.append(f"ほか{len(candidates) - limit}")
    return "; ".join(values) or "—"


def render_route_step(step: dict[str, object]) -> str:
    return (
        f"{step['spell']} → {step['target']} #{step['target_id']}"
    )


def render_chain_route(step: dict[str, object]) -> str:
    prior = [render_route_step(item) for item in step.get("route") or ()]
    prior.append(render_route_step(step))
    return " / ".join(prior)


def path_master_text(
    masters: dict[str, dict[str, object]],
    levels: dict[str, int],
) -> str:
    values: list[str] = []
    for path in ARCANE_PATHS:
        if levels.get(path, 0):
            master = masters.get(path)
            name = f"{master['name']} #{master['id']}" if master else "—"
            values.append(f"{path}{levels[path]}: {name}")
    return "; ".join(values) or "—"


def nation_page(profile: dict[str, object]) -> str:
    nation = profile["nation"]
    native = profile["native"]
    lines = front_matter(f"{nation['code']} {nation['name']} Magic Access到達経路")
    lines.extend(
        [
            f"# {nation['code']} {nation['name']} — Magic Access到達経路",
            "",
            f"> **{nation['epithet']}**",
            "",
            f"[Recruitデータ](../../recruitment/{nation['dir']}/{nation['slug']}.md) · "
            f"[Site Search能力](../../site-search/{nation['dir']}/{nation['slug']}.md) · "
            f"[拡張Magic Access](../../extended-magic-access/{nation['dir']}/{nation['slug']}.md) · "
            f"[国家攻略](../../../nations/{nation['dir']}/{nation['slug']}.md) · "
            "[経路の読み方](../../../magic/magic-access-routes.md)",
            "",
            '!!! warning "戦略Pathと戦闘Pathは別"',
            "    Booster・召喚・EmpowermentはRitual / Forgeへ使える戦略Accessです。Communion / Sabbathは戦闘中だけの到達値で、召喚RitualやForgeへは加算しません。",
            "",
            "## 概要",
            "",
            "| Layer | 最大Path / 状態 | 備考 |",
            "|---|---|---|",
            f"| Native保証 | {esc(level_text(native))} | 通常Recruit Mage |",
            f"| Single-forger Booster | {esc(level_text(profile['booster_max']))} | 最大{MAX_FORGES}段・標準Slot仮定 |",
            f"| Fixed summon chain | {esc(level_text(profile['fixed_chain']['max_levels']))} | 固定Target・最大{MAX_SUMMON_DEPTH}段 |",
            f"| Planned strategic total | {esc(level_text(profile['planned']))} | Native / Booster / Fixed summonの最大をLayer別に統合 |",
            f"| Conditional total | {esc(level_text(profile['conditional']))} | Random-assistedを含む理論上限 |",
            f"| 新規Path | {esc(' '.join(profile['new_paths']) or '—')} | Native 0から計画的に開くPath |",
            f"| Empowerment gap | {esc(' '.join(profile['gaps']) or 'なし')} | 自動の計画経路で残るArcane Path |",
            "",
            "## Booster best route",
            "",
            "| Path | Start Mage | Base | Reach | Forge route | Final equipment | Max Construction | Base Gem cost |",
            "|---|---|---|---:|---|---|---|---|",
        ]
    )
    for path in PATH_ORDER:
        route = profile["booster"].get(path)
        if not route:
            continue
        candidate = route["candidate"]
        item_by_id = route["item_by_id"]
        lines.append(
            f"| {path} — {PATH_NAMES[path]} | "
            f"{esc(candidate['name'])} #{candidate['id']} | "
            f"{esc(level_text(candidate['guaranteed']))} | {route['level']} | "
            f"{esc(route_item_names(route, item_by_id))} | "
            f"{esc(equipped_item_names(route, item_by_id))} | "
            f"{route['max_const'] or '—'} | {esc(route['route_cost'])} |"
        )
    if not profile["booster"]:
        lines.append("| — | — | — | — | Boosterによる保証Path増加なし | — | — | — |")
    lines.extend(
        [
            "",
            "### Random-assisted Booster route",
            "",
            "| Path | Start Mage | Reach | Forge route | Final equipment |",
            "|---|---|---:|---|---|",
        ]
    )
    conditional_rows = 0
    for path in PATH_ORDER:
        route = profile["booster_possible"].get(path)
        guaranteed = profile["booster"].get(path)
        if not route or guaranteed and int(route["level"]) <= int(guaranteed["level"]):
            continue
        conditional_rows += 1
        candidate = route["candidate"]
        item_by_id = route["item_by_id"]
        lines.append(
            f"| {path} — {PATH_NAMES[path]} | "
            f"{esc(candidate['name'])} #{candidate['id']} ({esc(random_text(candidate['row']))}) | "
            f"{route['level']} | {esc(route_item_names(route, item_by_id))} | "
            f"{esc(equipped_item_names(route, item_by_id))} |"
        )
    if not conditional_rows:
        lines.append("| — | — | — | 保証Routeを超えるRandom-assisted Routeなし | — |")

    lines.extend(
        [
            "",
            "## Fixed recursive Mage summon chain",
            "",
            "| Depth | Spell | Caster | Target Mage | Target magic | Route | Research / Cost |",
            "|---:|---|---|---|---|---|---|",
        ]
    )
    for step in profile["fixed_chain"]["relations"]:
        target = profile["fixed_chain"]["reachable"].get(int(step["target_id"]))
        target_magic = level_text(target["levels"]) if target else level_text(step["target_magic"])
        lines.append(
            f"| {step['depth']} | {spell_link(step, detail=True)} | "
            f"{unit_link(int(step['caster_id']), str(step['caster']), detail=True)} | "
            f"{unit_link(int(step['target_id']), str(step['target']), detail=True)} | "
            f"{esc(target_magic)} | {esc(render_chain_route(step))} | "
            f"{esc(step['research'])} / {esc(step['cost'])} |"
        )
    if not profile["fixed_chain"]["relations"]:
        lines.append("| — | — | — | — | — | 固定Targetの再帰Mage summonなし | — |")

    lines.extend(
        [
            "",
            "### Random-assisted summon chain",
            "",
            "| Depth | Spell | Caster | Target Mage | Target magic | Route |",
            "|---:|---|---|---|---|---|",
        ]
    )
    fixed_targets = {
        int(step["target_id"])
        for step in profile["fixed_chain"]["relations"]
    }
    possible_rows = 0
    for step in profile["possible_chain"]["relations"]:
        if int(step["target_id"]) in fixed_targets:
            continue
        possible_rows += 1
        target = profile["possible_chain"]["reachable"].get(int(step["target_id"]))
        target_magic = level_text(target["levels"]) if target else level_text(step["target_magic"])
        lines.append(
            f"| {step['depth']} | {spell_link(step, detail=True)} | "
            f"{unit_link(int(step['caster_id']), str(step['caster']), detail=True)} | "
            f"{unit_link(int(step['target_id']), str(step['target']), detail=True)} | "
            f"{esc(target_magic)} | {esc(render_chain_route(step))} |"
        )
    if not possible_rows:
        lines.append("| — | — | — | — | — | 保証Chainを超えるRandom-assisted targetなし |")

    lines.extend(
        [
            "",
            "### Candidate-pool opportunities",
            "",
            "| Spell | Req | Caster | Pool | Mage candidates |",
            "|---|---|---|---|---|",
        ]
    )
    for group in profile["candidate_pools"]:
        operators = group["guaranteed_operators"] or group["possible_operators"]
        targets = "; ".join(
            f"{target['name']} #{target['id']}: {level_text(target['possible'])}"
            for target in group["targets"][:5]
        )
        if len(group["targets"]) > 5:
            targets += f"; ほか{len(group['targets']) - 5}"
        lines.append(
            f"| {extended_spell_link(group, detail=True)} | {esc(group['path'])} | "
            f"{esc(candidate_names(operators))} | {esc(group['pool'])} | {esc(targets)} |"
        )
    if not profile["candidate_pools"]:
        lines.append("| — | — | — | — | Native casterで利用できるMage候補poolなし |")

    lines.extend(
        [
            "",
            "## Communion / Sabbath battle reach",
            "",
            "| Structure | Native slave-capable types | Random-assisted types | Slaves | Bonus | Battle Path max | Best masters |",
            "|---|---:|---:|---:|---:|---|---|",
        ]
    )
    for structure in (profile["communion"], profile["sabbath"]):
        if not structure["guaranteed"]:
            lines.append(
                f"| {structure['label']} | 0 | {len(structure['possible'])} | — | — | — | Native保証{structure['path']}1なし |"
            )
            continue
        for breakpoint in structure["breakpoints"]:
            lines.append(
                f"| {structure['label']} | {len(structure['guaranteed'])} | "
                f"{len(structure['possible'])} | {breakpoint['slaves']} | "
                f"+{breakpoint['bonus']} | {esc(level_text(breakpoint['levels']))} | "
                f"{esc(path_master_text(breakpoint['masters'], breakpoint['levels']))} |"
            )

    lines.extend(
        [
            "",
            "## Matrix / Communion関連Item",
            "",
            "| Item | Type | Research | Req | Booster |",
            "|---|---|---|---|---|",
        ]
    )
    for item in profile["matrix_items"]:
        lines.append(
            f"| {esc(item['name'])} | {esc(item['type_title'])} | "
            f"{esc(item['construction'])} | {esc(item['requirement_text'])} | "
            f"{esc(item['boost_text'])} |"
        )
    if not profile["matrix_items"]:
        lines.append("| — | — | — | — | 国家制限内のMatrix候補なし |")

    lines.extend(
        [
            "",
            "## Empowerment gap",
            "",
            f"Planned strategic routeで未到達のArcane Path: **{esc(' '.join(profile['gaps']) or 'なし')}**",
            "",
            "この欄はEmpowermentの推奨ではありません。Pretender、Hero、Start Site、一般Site Mage、国家全体のBooster分業、Event等も比較してください。",
            "",
            "## 計算上の限界",
            "",
            "- Boosterは通常Recruit Mage一体が最大三段をSelf-forgeする保守的な計算です。別MageがForgeして渡す分業は含みません。",
            "- Boosterの標準Slot計算はUnit固有の手・頭・Misc数、装備不可、Size / Strength制限を完全には再現しません。",
            "- Forge Bonus、Gem割引、国家Rebate、Artifact競合をRoute順位へ反映しません。",
            "- 固定召喚Chainは最大三段。Candidate pool、Wish、procedural summonは再帰へ投入しません。",
            "- Communion / SabbathはPath到達だけを表示し、Fatigue安全性とMaster数を評価しません。",
            "- Empowerment costは固定表示せず、ゲーム内画面を優先します。",
            "",
        ]
    )
    return "\n".join(lines)


def index_page(profiles: list[dict[str, object]]) -> str:
    lines = front_matter("国家別Magic Access到達経路")
    lines.extend(
        [
            "# 国家別Magic Access到達経路",
            "",
            "通常Recruit Mageから、Booster、固定Mage召喚Chain、Communion / Sabbath、Empowerment gapへ進む経路を比較します。",
            "",
            "- [経路の読み方](../../magic/magic-access-routes.md)",
            "- [Booster route](booster-routes.md)",
            "- [再帰Mage summon chain](summon-chains.md)",
            "- [Communion・Sabbath battle reach](communion-sabbath.md)",
            "- [Empowerment gap](empowerment-gaps.md)",
            "- [データ品質・境界](data-quality.md)",
            "",
            '!!! warning "Layerを合成した一体のMageではない"',
            "    Native、Booster、召喚、Communionの最大値は別経路です。特にCommunionは戦闘中だけで、Ritual / Forgeへは使えません。",
            "",
        ]
    )
    for era in ("EA", "MA", "LA"):
        lines.extend(
            [
                f"## {era}",
                "",
                "| Nation | Native | Booster | Fixed summon | Planned | New paths | Communion | Sabbath | Empowerment gap | Detail |",
                "|---|---|---|---|---|---|---|---|---|---|",
            ]
        )
        for profile in [item for item in profiles if item["nation"]["code"] == era]:
            nation = profile["nation"]
            communion = len(profile["communion"]["guaranteed"])
            sabbath = len(profile["sabbath"]["guaranteed"])
            lines.append(
                f"| {esc(nation['name'])} | {esc(level_text(profile['native']))} | "
                f"{esc(level_text(profile['booster_max']))} | "
                f"{esc(level_text(profile['fixed_chain']['max_levels']))} | "
                f"{esc(level_text(profile['planned']))} | "
                f"{esc(' '.join(profile['new_paths']) or '—')} | "
                f"{communion or '—'} | {sabbath or '—'} | "
                f"{esc(' '.join(profile['gaps']) or 'なし')} | "
                f"[表示]({nation['dir']}/{nation['slug']}.md) |"
            )
        lines.append("")
    return "\n".join(lines)


def booster_page(profiles: list[dict[str, object]], boosters, unforgeable) -> str:
    lines = front_matter("全国家Booster route")
    lines.extend(
        [
            "# 全国家Booster route",
            "",
            "通常Recruit Mage一体が、標準Slot仮定で最大三段までSelf-forgeするPath Booster routeです。",
            "",
            "[国家別到達経路へ戻る](index.md)",
            "",
            "## Forgeable Booster Item",
            "",
            "| Item | ID | Type | Research | Req | Gem | Boost | Restriction |",
            "|---|---:|---|---|---|---|---|---|",
        ]
    )
    for item in boosters:
        restriction = (
            ", ".join(map(str, sorted(item["restrictions"])))
            if item["restrictions"]
            else "Generic"
        )
        lines.append(
            f"| {esc(item['name'])} | {item['id']} | {esc(item['type_title'])} | "
            f"{esc(item['construction'])} | {esc(item['requirement_text'])} | "
            f"{esc(item['cost'])} | {esc(item['boost_text'])} | {esc(restriction)} |"
        )
    lines.extend(
        [
            "",
            "## Nation best route",
            "",
            "| Nation | Path | Start Mage | Base | Reach | Forge route | Final equipment |",
            "|---|---|---|---|---:|---|---|",
        ]
    )
    count = 0
    for profile in profiles:
        nation = profile["nation"]
        for path in PATH_ORDER:
            route = profile["booster"].get(path)
            if not route:
                continue
            count += 1
            candidate = route["candidate"]
            item_by_id = route["item_by_id"]
            lines.append(
                f"| [{nation['code']} {esc(nation['name'])}]({nation['dir']}/{nation['slug']}.md) | "
                f"{path} | {esc(candidate['name'])} #{candidate['id']} | "
                f"{esc(level_text(candidate['guaranteed']))} | {route['level']} | "
                f"{esc(route_item_names(route, item_by_id))} | "
                f"{esc(equipped_item_names(route, item_by_id))} |"
            )
    if not count:
        lines.append("| — | — | — | — | — | — | — |")
    lines.extend(
        [
            "",
            "## Unforgeable / Artifact Booster",
            "",
            "| Item | ID | Type | Req | Boost | Restriction |",
            "|---|---:|---|---|---|---|",
        ]
    )
    for item in unforgeable:
        restriction = (
            ", ".join(map(str, sorted(item["restrictions"])))
            if item["restrictions"]
            else "Generic / special acquisition"
        )
        lines.append(
            f"| {esc(item['name'])} | {item['id']} | {esc(item['type_title'])} | "
            f"{esc(item['requirement_text'])} | {esc(item['boost_text'])} | "
            f"{esc(restriction)} |"
        )
    lines.extend(
        [
            "",
            f"Nation route relation: **{count}**",
            "",
            "Item restrictionの数字はNation IDです。実際のForge可否、Artifactの取得、Slot互換性はゲーム内表示を優先します。",
            "",
        ]
    )
    return "\n".join(lines)


def summon_page(profiles: list[dict[str, object]]) -> str:
    lines = front_matter("全国家再帰Mage summon chain")
    lines.extend(
        [
            "# 全国家再帰Mage summon chain",
            "",
            f"固定TargetのMage召喚を最大{MAX_SUMMON_DEPTH}段まで追跡します。Candidate poolは再帰へ投入しません。",
            "",
            "[国家別到達経路へ戻る](index.md)",
            "",
            "| Nation | Depth | Spell | Caster | Target Mage | Target magic | Route |",
            "|---|---:|---|---|---|---|---|",
        ]
    )
    count = 0
    for profile in profiles:
        nation = profile["nation"]
        for step in profile["fixed_chain"]["relations"]:
            count += 1
            target = profile["fixed_chain"]["reachable"].get(int(step["target_id"]))
            target_magic = level_text(target["levels"]) if target else level_text(step["target_magic"])
            lines.append(
                f"| [{nation['code']} {esc(nation['name'])}]({nation['dir']}/{nation['slug']}.md) | "
                f"{step['depth']} | {spell_link(step)} | "
                f"{unit_link(int(step['caster_id']), str(step['caster']))} | "
                f"{unit_link(int(step['target_id']), str(step['target']))} | "
                f"{esc(target_magic)} | {esc(render_chain_route(step))} |"
            )
    if not count:
        lines.append("| — | — | — | — | — | — | — |")
    lines.extend(
        [
            "",
            f"Fixed chain relation: **{count}**",
            "",
            "Research、Gem、Unique状態、Lab、召喚Turnは経路に含まれますが、Turn数やGem収支の最適化は行いません。",
            "",
        ]
    )
    return "\n".join(lines)


def communion_page(profiles: list[dict[str, object]], matrix_items) -> str:
    lines = front_matter("全国家Communion・Sabbath battle reach")
    lines.extend(
        [
            "# 全国家Communion・Sabbath battle reach",
            "",
            "通常Recruit Mageの保証S1 / B1を使い、Slave数ごとの戦闘中Path最大を計算します。",
            "",
            "[国家別到達経路へ戻る](index.md)",
            "",
            "| Nation | Structure | Slave-capable types | 2 slaves | 4 slaves | 8 slaves | 16 slaves |",
            "|---|---|---:|---|---|---|---|",
        ]
    )
    for profile in profiles:
        nation = profile["nation"]
        for structure in (profile["communion"], profile["sabbath"]):
            bps = structure["breakpoints"]
            values = [
                level_text(item["levels"]) if structure["guaranteed"] else "—"
                for item in bps[:4]
            ]
            lines.append(
                f"| [{nation['code']} {esc(nation['name'])}]({nation['dir']}/{nation['slug']}.md) | "
                f"{structure['label']} | {len(structure['guaranteed']) or '—'} | "
                + " | ".join(esc(value) for value in values)
                + " |"
            )
    lines.extend(
        [
            "",
            "## Matrix / Communion related Item",
            "",
            "| Item | Type | Research | Req | Boost |",
            "|---|---|---|---|---|",
        ]
    )
    for item in matrix_items:
        lines.append(
            f"| {esc(item['name'])} | {esc(item['type_title'])} | "
            f"{esc(item['construction'])} | {esc(item['requirement_text'])} | "
            f"{esc(item['boost_text'])} |"
        )
    if not matrix_items:
        lines.append("| — | — | — | — | — |")
    lines.extend(
        [
            "",
            "Path reachだけの比較です。Fatigue、安全なMaster数、Self-buff共有、Matrix装備者のPath差は[Communion・Sabbath](../../magic/communions.md)で確認してください。",
            "",
        ]
    )
    return "\n".join(lines)


def empowerment_page(profiles: list[dict[str, object]]) -> str:
    lines = front_matter("全国家Empowerment gap")
    lines.extend(
        [
            "# 全国家Empowerment gap",
            "",
            "Native、single-forger Booster、固定Mage召喚Chainを使っても残るArcane Pathを表示します。",
            "",
            "[国家別到達経路へ戻る](index.md)",
            "",
            "| Nation | Native | Planned strategic | New paths | Remaining gaps | Conditional possible |",
            "|---|---|---|---|---|---|",
        ]
    )
    for profile in profiles:
        nation = profile["nation"]
        lines.append(
            f"| [{nation['code']} {esc(nation['name'])}]({nation['dir']}/{nation['slug']}.md) | "
            f"{esc(level_text(profile['native']))} | {esc(level_text(profile['planned']))} | "
            f"{esc(' '.join(profile['new_paths']) or '—')} | "
            f"{esc(' '.join(profile['gaps']) or 'なし')} | "
            f"{esc(level_text(profile['conditional']))} |"
        )
    lines.extend(
        [
            "",
            "GapはEmpowerment推奨ではありません。Pretender、Hero、Start / Future Site、一般Site Mage、国家全体のBooster分業、Event等を先に比較します。",
            "",
        ]
    )
    return "\n".join(lines)


def quality_page(
    profiles: list[dict[str, object]],
    boosters,
    unforgeable,
    summon_groups,
    stats: dict[str, int],
) -> str:
    lines = front_matter("Magic Access到達経路データ品質")
    lines.extend(
        [
            "# Magic Access到達経路データ品質",
            "",
            "| 項目 | 値 |",
            "|---|---:|",
            f"| Nation profile | {len(profiles)} |",
            f"| Forgeable booster | {len(boosters)} |",
            f"| Unforgeable booster | {len(unforgeable)} |",
            f"| Mage summon group | {len(summon_groups)} |",
            f"| Booster route state | {stats['route_states']} |",
            f"| Booster compatible loadout | {stats['loadouts']} |",
            f"| Booster base signature search | {stats['candidate_searches']} |",
            f"| Random-assisted route state | {stats['possible_route_states']} |",
            f"| Fixed summon relation | {stats['fixed_summon_relations']} |",
            f"| Random-assisted summon relation | {stats['possible_summon_relations']} |",
            f"| Candidate-pool nation relation | {stats['candidate_pool_relations']} |",
            f"| Truncated fixed-chain frontier | {stats['fixed_frontier']} |",
            "",
            "## 安全上の境界",
            "",
            "- 国家最大Pathを一体へ合成しない。Booster routeは個別Mageから開始する。",
            "- Forgeable boosterだけをsingle-forger chainへ投入し、Artifact / Unforgeableは別表にする。",
            "- Standard slotを超える組み合わせを除外する。Unit固有Slotは未評価。",
            "- Fixed summonだけを再帰Chainへ投入し、Candidate pool、Wish、procedural summonを除外する。",
            "- Realmのみで制限されたSpellを、国家対応がない状態で推測割当しない。",
            "- Communion / Sabbathは戦闘Pathとしてだけ表示する。",
            "- Empowerment costを自動推測しない。",
            "",
            "## 現在含まれないもの",
            "",
            "- Boosterを別MageがForgeして渡す国家全体の分業",
            "- Forge Bonus・Rebate・HammerによるGem節約",
            "- Combat self-boostとGem boost",
            "- Hero、Pretender、Start Site MageをCasterにした再帰召喚",
            "- Summoned Mageから四段以上のChain",
            "- Matrix Itemを使った非Astral Masterの自動計算",
            "- Unit固有の装備Slot、装備不可、Size / Strength条件",
            "",
        ]
    )
    return "\n".join(lines)


def write_pages(
    profiles: list[dict[str, object]],
    boosters,
    unforgeable,
    summon_groups,
    stats,
) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.md").write_text(index_page(profiles), encoding="utf-8")
    (OUT / "booster-routes.md").write_text(
        booster_page(profiles, boosters, unforgeable),
        encoding="utf-8",
    )
    (OUT / "summon-chains.md").write_text(
        summon_page(profiles),
        encoding="utf-8",
    )
    matrix_items = [
        item
        for item in boosters + unforgeable
        if item["matrix"]
    ]
    (OUT / "communion-sabbath.md").write_text(
        communion_page(profiles, matrix_items),
        encoding="utf-8",
    )
    (OUT / "empowerment-gaps.md").write_text(
        empowerment_page(profiles),
        encoding="utf-8",
    )
    (OUT / "data-quality.md").write_text(
        quality_page(profiles, boosters, unforgeable, summon_groups, stats),
        encoding="utf-8",
    )
    for profile in profiles:
        nation = profile["nation"]
        path = OUT / str(nation["dir"]) / f"{nation['slug']}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(nation_page(profile), encoding="utf-8")


def validate(
    profiles,
    boosters,
    summon_groups,
    stats,
) -> None:
    if len(profiles) != 103:
        raise ValueError(f"nation profile count mismatch: {len(profiles)}")
    if len(boosters) < 10:
        raise ValueError(f"booster set appears incomplete: {len(boosters)}")
    if len(summon_groups) < 50:
        raise ValueError(f"summon group set appears incomplete: {len(summon_groups)}")
    if stats["route_states"] <= 0 or stats["loadouts"] <= 0:
        raise ValueError("booster route search produced no states")
    if stats["fixed_summon_relations"] <= 0:
        raise ValueError("recursive summon search produced no relations")
    for profile in profiles:
        if not profile["candidates"]:
            raise ValueError(
                f"nation has no recruitable mage candidate: {profile['nation']['code']} {profile['nation']['name']}"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    data = load_unit_catalog(args.refresh, args.offline)
    boosters, unforgeable = load_boosters(data)
    summon_groups, summon_stats = build_summon_groups(data)

    profiles: list[dict[str, object]] = []
    stats: Counter[str] = Counter()
    for nation in data["nations"]:
        profile, route_stats = profile_for_nation(
            nation,
            data,
            boosters,
            unforgeable,
            summon_groups,
        )
        profiles.append(profile)
        stats.update(route_stats)
        stats["fixed_summon_relations"] += len(profile["fixed_chain"]["relations"])
        stats["possible_summon_relations"] += len(profile["possible_chain"]["relations"])
        stats["candidate_pool_relations"] += len(profile["candidate_pools"])
        stats["fixed_frontier"] += int(profile["fixed_chain"]["frontier"])

    profiles.sort(
        key=lambda profile: (
            str(profile["nation"]["code"]),
            str(profile["nation"]["name"]),
        )
    )
    validate(profiles, boosters, summon_groups, stats)
    write_pages(profiles, boosters, unforgeable, summon_groups, stats)

    print(f"source commit: {COMMIT}")
    print(f"nation_profiles: {len(profiles)}")
    print(f"nation_detail_pages: {len(profiles)}")
    print(f"forgeable_boosters: {len(boosters)}")
    print(f"unforgeable_boosters: {len(unforgeable)}")
    print(f"summon_mage_groups: {len(summon_groups)}")
    for key in (
        "route_states",
        "loadouts",
        "candidate_searches",
        "possible_route_states",
        "possible_loadouts",
        "possible_candidate_searches",
        "fixed_summon_relations",
        "possible_summon_relations",
        "candidate_pool_relations",
        "fixed_frontier",
    ):
        print(f"{key}: {stats[key]}")
    print(
        "summon source stats: "
        + ", ".join(f"{key}={value}" for key, value in sorted(summon_stats.items()))
    )


if __name__ == "__main__":
    main()
