from __future__ import annotations

from collections import Counter

from generate_nation_site_search_data import random_feasible
from generate_recruitment_data import fixed, randoms


def _dominates(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    return all(a >= b for a, b in zip(left, right)) and any(
        a > b for a, b in zip(left, right)
    )


def _pareto(states: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
    values = sorted(states, key=lambda state: (-sum(state), state), reverse=False)
    frontier: list[tuple[int, ...]] = []
    for state in values:
        if any(_dominates(other, state) or other == state for other in frontier):
            continue
        frontier = [other for other in frontier if not _dominates(state, other)]
        frontier.append(state)
    return set(frontier)


def possible_random_outcomes(row, path_order) -> list[dict[str, int]]:
    """Enumerate Pareto-maximal simultaneous random outcomes.

    Per-path theoretical maxima cannot safely be combined for a crosspath
    requirement. Every positive-chance pick is assigned to exactly one path in
    its pool, matching the feasibility model already used by Site Search.
    """
    base = tuple(int(fixed(row).get(path, 0)) for path in path_order)
    states: set[tuple[int, ...]] = {base}
    for count, chance, level, pool in randoms(row):
        if chance <= 0:
            continue
        for _pick in range(count):
            next_states: set[tuple[int, ...]] = set()
            for state in states:
                for path in pool:
                    if path not in path_order:
                        continue
                    index = path_order.index(path)
                    updated = list(state)
                    updated[index] += level
                    next_states.add(tuple(updated))
            if next_states:
                states = _pareto(next_states)
    output = [
        {
            path: state[index]
            for index, path in enumerate(path_order)
            if state[index] > 0
        }
        for state in states
    ]
    output.sort(key=lambda levels: (-sum(levels.values()), tuple(sorted(levels.items()))))
    return output or [dict(fixed(row))]


def install(generator) -> None:
    original_best_booster_routes = generator.best_booster_routes

    def exact_best_booster_routes(
        nation_id,
        candidates,
        boosters,
        *,
        possible=False,
    ):
        if not possible:
            return original_best_booster_routes(
                nation_id,
                candidates,
                boosters,
                possible=False,
            )

        allowed = generator.allowed_boosters(boosters, nation_id)
        cache = {}
        best = {}
        stats = {"route_states": 0, "loadouts": 0, "candidate_searches": 0}
        for candidate in candidates:
            for base in possible_random_outcomes(candidate["row"], generator.PATH_ORDER):
                signature = tuple(sorted(base.items()))
                if signature not in cache:
                    cache[signature] = generator.route_search(base, allowed)
                    stats["route_states"] += int(cache[signature]["states"])
                    stats["loadouts"] += int(cache[signature]["loadouts"])
                    stats["candidate_searches"] += 1
                result = cache[signature]
                for path, route in result["best_by_path"].items():
                    entry = {
                        **route,
                        "candidate": candidate,
                        "possible": True,
                        "base_outcome": base,
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

    def caster_can_meet(caster, requirements, possible):
        if not possible:
            return generator.meets(caster["guaranteed"], requirements)
        candidate = {
            "row": caster["row"],
            "guaranteed": caster["guaranteed"],
        }
        return random_feasible(candidate, requirements)

    def exact_fixed_summon_chain(
        nation_id,
        candidates,
        groups,
        *,
        possible=False,
    ):
        available = [
            group
            for group in groups
            if generator.summon_group_available(group, nation_id)
        ]
        reachable = {}
        for candidate in candidates:
            record = generator.caster_record(candidate, possible=possible)
            existing = reachable.get(record["id"])
            if existing is None or sum(record["levels"].values()) > sum(existing["levels"].values()):
                reachable[record["id"]] = record

        new_relations = []
        depth_counts = Counter()
        used_groups = set()

        for depth in range(1, generator.MAX_SUMMON_DEPTH + 1):
            additions = []
            pending_ids = set()
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
                    if caster_can_meet(caster, group["requirements"], possible)
                ]
                if not operators:
                    continue
                operator = operators[0]
                for target in group["targets"]:
                    target_id = int(target["id"])
                    if target_id in reachable or target_id in pending_ids:
                        continue
                    relation_key = (
                        int(group["spell_id"]),
                        int(operator["id"]),
                        target_id,
                    )
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
                        "target_magic": dict(
                            target["possible"] if possible else target["guaranteed"]
                        ),
                        "availability": (
                            "National" if group["national_ids"] else "Generic"
                        ),
                        "route": tuple(operator["route"]),
                        "possible": possible,
                    }
                    full_route = tuple(operator["route"]) + (step,)
                    additions.append(
                        generator.target_caster_record(
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

        max_levels_out = {path: 0 for path in generator.PATH_ORDER}
        for record in reachable.values():
            for path, level in record["levels"].items():
                max_levels_out[path] = max(max_levels_out[path], int(level))

        frontier = 0
        for group in available:
            if any(
                caster_can_meet(caster, group["requirements"], possible)
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

    generator.best_booster_routes = exact_best_booster_routes
    generator.fixed_summon_chain = exact_fixed_summon_chain
