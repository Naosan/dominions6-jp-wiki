#!/usr/bin/env python3
"""Generate nation-level Site Search capability profiles.

The generator combines recruitable commander records with the pinned
Dominions 6.35 Site Search spell data. It deliberately separates guaranteed
fixed access from random-assisted theoretical access.

Run from the repository root:
    python scripts/generate_nation_site_search_data.py
    python scripts/generate_nation_site_search_data.py --refresh
    python scripts/generate_nation_site_search_data.py --offline
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

from generate_recruitment_data import (
    COMMIT,
    cap,
    esc,
    fixed,
    mapping,
    nations,
    num,
    randoms,
    random_text,
    rows,
    source,
    tsv,
    unit_data,
    yes,
)
from generate_site_search_data import build_search_spell_rows
from generate_spell_item_data import (
    PATHS as SPELL_PATHS,
    SCHOOLS,
    spell_gem_cost,
    spell_path,
    spell_research,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "data" / "site-search"
RECRUIT_OUT = ROOT / "docs" / "data" / "recruitment"
MAGE_ACCESS = ROOT / "docs" / "data" / "mage-access.md"
SITE_INDEX = ROOT / "docs" / "data" / "sites" / "index.md"
SPELL_SEARCH_INDEX = ROOT / "docs" / "data" / "spells" / "site-search.md"

FILES = (
    "BaseU.csv",
    "fort_leader_types_by_nation.csv",
    "nonfort_leader_types_by_nation.csv",
    "coast_leader_types_by_nation.csv",
    "spells.csv",
    "effects_spells.csv",
)

PATH_ORDER = tuple("FAWESDNGBH")
ARCANE_PATHS = tuple("FAWESDNGB")
PATH_NAMES = {
    code: name for _number, (code, name, _slug) in SPELL_PATHS.items()
}
SOURCE_ORDER = {
    "Any fort": 0,
    "Fort不要 / terrain": 1,
    "Coastal": 2,
    "Capital-only": 3,
}


def front_matter(title: str) -> list[str]:
    safe = title.replace('"', '\\"')
    return [
        "---",
        f'title: "{safe}"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {COMMIT}"',
        "---",
        "",
    ]


def map_move(row: dict[str, str]) -> int:
    for key in ("mapmove", "mapmov", "map_move"):
        value = num(row, key)
        if value:
            return value
    return 0


def research_value(row: dict[str, str]) -> int:
    return num(row, "researchbonus")


def slow_to_recruit(row: dict[str, str]) -> bool:
    return num(row, "rt") == 2 or yes(row, "slowrec")


def deterministic_levels(row: dict[str, str]) -> dict[str, int]:
    """Guaranteed paths, including 100% single-path random groups."""
    levels = dict(fixed(row))
    for count, chance, level, pool in randoms(row):
        if chance == 100 and len(pool) == 1:
            path = pool[0]
            levels[path] = levels.get(path, 0) + count * level
    return {path: level for path, level in levels.items() if level > 0}


def possible_levels(row: dict[str, str]) -> dict[str, int]:
    """Theoretical maximum per path; simultaneous maxima are not implied."""
    levels = dict(fixed(row))
    for count, _chance, level, pool in randoms(row):
        for path in pool:
            levels[path] = levels.get(path, 0) + count * level
    return {path: level for path, level in levels.items() if level > 0}


def level_text(levels: dict[str, int], paths: Iterable[str] = PATH_ORDER) -> str:
    return " ".join(f"{path}{levels[path]}" for path in paths if levels.get(path, 0)) or "—"


def random_pool_paths(row: dict[str, str]) -> set[str]:
    return {path for _count, _chance, _level, pool in randoms(row) for path in pool}


def source_text(sources: set[str]) -> str:
    return ", ".join(sorted(sources, key=lambda value: SOURCE_ORDER.get(value, 99)))


def constraints(row: dict[str, str], sources: set[str]) -> str:
    out: list[str] = []
    if sources == {"Capital-only"}:
        out.append("Capital-only")
    if slow_to_recruit(row):
        out.append("Slow to recruit")
    if "Fort不要 / terrain" in sources:
        out.append("Terrain / non-fort")
    if "Coastal" in sources:
        out.append("Coastal")
    if num(row, "stealthy"):
        out.append(f"Stealth {num(row, 'stealthy'):+d}")
    if yes(row, "flying"):
        out.append("Flying")
    if yes(row, "aquatic"):
        out.append("Aquatic")
    elif yes(row, "amphibian"):
        out.append("Amphibious")
    elif yes(row, "pooramphibian"):
        out.append("Poor Amphibian")
    return ", ".join(out) or "—"


def candidate_record(
    row: dict[str, str],
    sources: set[str],
) -> dict[str, object]:
    guaranteed = deterministic_levels(row)
    possible = possible_levels(row)
    guaranteed_paths = {path for path in PATH_ORDER if guaranteed.get(path, 0)}
    possible_paths = {
        path for path in PATH_ORDER if possible.get(path, 0) or path in random_pool_paths(row)
    }
    return {
        "row": row,
        "id": num(row, "id"),
        "name": (row.get("name") or "(unnamed)").strip(),
        "sources": sources,
        "source_text": source_text(sources),
        "guaranteed": guaranteed,
        "possible": possible,
        "guaranteed_paths": guaranteed_paths,
        "possible_paths": possible_paths,
        "guaranteed_breadth": len(guaranteed_paths),
        "possible_breadth": len(possible_paths),
        "arcane_breadth": len(guaranteed_paths & set(ARCANE_PATHS)),
        "potential_arcane_breadth": len(possible_paths & set(ARCANE_PATHS)),
        "depth_sum": sum(min(level, 6) for level in guaranteed.values()),
        "mapmove": map_move(row),
        "research": research_value(row),
        "random_text": random_text(row),
        "constraints": constraints(row, sources),
        "any_fort": "Any fort" in sources,
        "capital_only": sources == {"Capital-only"},
    }


def collect_candidates(
    nation_id: int,
    maps: dict[str, dict[int, list[int]]],
    units: dict[int, dict[str, str]],
) -> list[dict[str, object]]:
    sources_by_unit: dict[int, set[str]] = defaultdict(set)

    for unit_id in maps["fl"].get(nation_id, []):
        row = units.get(unit_id)
        if row is None:
            raise KeyError(f"mapped commander {unit_id} missing from BaseU")
        sources_by_unit[unit_id].add("Capital-only" if cap(row) else "Any fort")
    for unit_id in maps["nl"].get(nation_id, []):
        sources_by_unit[unit_id].add("Fort不要 / terrain")
    for unit_id in maps["cl"].get(nation_id, []):
        sources_by_unit[unit_id].add("Coastal")

    output: list[dict[str, object]] = []
    for unit_id, sources in sorted(sources_by_unit.items()):
        row = units.get(unit_id)
        if row is None:
            raise KeyError(f"mapped commander {unit_id} missing from BaseU")
        if not (fixed(row) or randoms(row) or yes(row, "researchbonus")):
            continue
        output.append(candidate_record(row, sources))
    return output


def broad_sort_key(candidate: dict[str, object]) -> tuple[object, ...]:
    return (
        -int(candidate["guaranteed_breadth"]),
        -int(candidate["possible_breadth"]),
        -int(candidate["depth_sum"]),
        0 if bool(candidate["any_fort"]) else 1,
        1 if bool(candidate["capital_only"]) else 0,
        1 if slow_to_recruit(candidate["row"]) else 0,
        -int(candidate["mapmove"]),
        str(candidate["name"]),
        int(candidate["id"]),
    )


def broad_candidates(candidates: list[dict[str, object]]) -> list[dict[str, object]]:
    selected = [
        candidate
        for candidate in candidates
        if int(candidate["guaranteed_breadth"]) >= 2
        or int(candidate["possible_breadth"]) >= 3
    ]
    return sorted(selected, key=broad_sort_key)


def requirement_levels(row: dict[str, str]) -> dict[str, int]:
    requirements: dict[str, int] = {}
    for pkey, lkey in (("path1", "pathlevel1"), ("path2", "pathlevel2")):
        path_number = num(row, pkey, -1)
        level = num(row, lkey)
        if path_number in SPELL_PATHS and level > 0:
            code = SPELL_PATHS[path_number][0]
            requirements[code] = max(requirements.get(code, 0), level)
    return requirements


def fixed_meets(candidate: dict[str, object], requirements: dict[str, int]) -> bool:
    guaranteed = candidate["guaranteed"]
    return all(int(guaranteed.get(path, 0)) >= level for path, level in requirements.items())


def random_feasible(candidate: dict[str, object], requirements: dict[str, int]) -> bool:
    """Whether some outcome of the random picks can meet all requirements.

    This is a feasibility test, not a probability calculation. Each random pick
    is allowed to land on one path in its pool. Chance values only determine how
    likely the outcome is, not whether it is possible.
    """
    if fixed_meets(candidate, requirements):
        return True

    base = fixed(candidate["row"])
    required_paths = tuple(sorted(requirements))
    deficits = tuple(
        max(0, requirements[path] - int(base.get(path, 0)))
        for path in required_paths
    )
    if not any(deficits):
        return True

    states: set[tuple[int, ...]] = {(0,) * len(required_paths)}
    for count, _chance, level, pool in randoms(candidate["row"]):
        for _pick in range(count):
            next_states = set(states)
            for state in states:
                for path in pool:
                    if path not in required_paths:
                        continue
                    index = required_paths.index(path)
                    updated = list(state)
                    updated[index] = min(deficits[index], updated[index] + level)
                    next_states.add(tuple(updated))
            states = next_states
    return deficits in states


def remote_access(
    candidates: list[dict[str, object]],
    spells: list[dict[str, object]],
) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for item in spells:
        row = item["row"]
        requirements = requirement_levels(row)
        native = [
            candidate for candidate in candidates if fixed_meets(candidate, requirements)
        ]
        possible = [
            candidate
            for candidate in candidates
            if not fixed_meets(candidate, requirements)
            and random_feasible(candidate, requirements)
        ]
        output.append(
            {
                **item,
                "requirements": requirements,
                "native": sorted(native, key=broad_sort_key),
                "possible": sorted(possible, key=broad_sort_key),
            }
        )
    return output


def max_levels(
    candidates: list[dict[str, object]],
    *,
    key: str = "guaranteed",
) -> dict[str, int]:
    result = {path: 0 for path in PATH_ORDER}
    for candidate in candidates:
        levels = candidate[key]
        for path in PATH_ORDER:
            result[path] = max(result[path], int(levels.get(path, 0)))
    return result


def per_path_candidates(
    candidates: list[dict[str, object]],
    path: str,
    *,
    possible: bool = False,
) -> list[dict[str, object]]:
    key = "possible" if possible else "guaranteed"
    maximum = max((int(candidate[key].get(path, 0)) for candidate in candidates), default=0)
    if maximum <= 0:
        return []
    selected = [
        candidate
        for candidate in candidates
        if int(candidate[key].get(path, 0)) == maximum
    ]
    return sorted(selected, key=broad_sort_key)


def path_union(candidates: list[dict[str, object]], key: str) -> set[str]:
    result: set[str] = set()
    for candidate in candidates:
        result.update(candidate[key])
    return result


def capital_additions(
    candidates: list[dict[str, object]],
) -> dict[str, int]:
    capital = [candidate for candidate in candidates if candidate["capital_only"]]
    other = [candidate for candidate in candidates if not candidate["capital_only"]]
    capital_max = max_levels(capital)
    other_max = max_levels(other)
    return {
        path: level
        for path, level in capital_max.items()
        if level > other_max.get(path, 0)
    }


def profile_tags(
    candidates: list[dict[str, object]],
    remote: list[dict[str, object]],
) -> list[str]:
    tags: list[str] = []
    best_breadth = max(
        (int(candidate["guaranteed_breadth"]) for candidate in candidates),
        default=0,
    )
    fixed_union = path_union(candidates, "guaranteed")
    max_fixed = max(max_levels(candidates).values(), default=0)
    cap_add = capital_additions(candidates)
    local = any(
        "Fort不要 / terrain" in candidate["sources"]
        or "Coastal" in candidate["sources"]
        for candidate in candidates
    )
    native_standard = sum(
        bool(item["native"]) and item["kind"] == "Single Path" for item in remote
    )

    if best_breadth >= 4:
        tags.append("Wide rover")
    elif best_breadth >= 3:
        tags.append("Broad rover")
    elif len(fixed_union) >= 6:
        tags.append("Distributed coverage")
    if max_fixed >= 4:
        tags.append("Deep L4+")
    elif max_fixed >= 3:
        tags.append("Deep L3")
    if native_standard >= 7:
        tags.append("Remote-rich")
    elif native_standard >= 4:
        tags.append("Remote-ready")
    if cap_add:
        tags.append("Capital adds paths")
    if local:
        tags.append("Local / coastal access")
    if "H" in fixed_union:
        tags.append("Holy manual")
    return tags or ["Limited native coverage"]


def nation_profile(
    nation: dict[str, object],
    candidates: list[dict[str, object]],
    spells: list[dict[str, object]],
) -> dict[str, object]:
    guaranteed = max_levels(candidates, key="guaranteed")
    possible = max_levels(candidates, key="possible")
    any_fort = [candidate for candidate in candidates if candidate["any_fort"]]
    capital = [candidate for candidate in candidates if candidate["capital_only"]]
    local = [candidate for candidate in candidates if not candidate["capital_only"] and not candidate["any_fort"]]
    remote = remote_access(candidates, spells)
    rovers = broad_candidates(candidates)
    native_standard = sum(
        bool(item["native"]) and item["kind"] == "Single Path" for item in remote
    )
    native_special = sum(
        bool(item["native"]) and item["kind"] == "Special" for item in remote
    )
    possible_standard = sum(
        bool(item["possible"]) and item["kind"] == "Single Path" for item in remote
    )
    possible_special = sum(
        bool(item["possible"]) and item["kind"] == "Special" for item in remote
    )

    return {
        "nation": nation,
        "candidates": candidates,
        "rovers": rovers,
        "remote": remote,
        "guaranteed": guaranteed,
        "possible": possible,
        "any_fort_levels": max_levels(any_fort),
        "capital_levels": max_levels(capital),
        "local_levels": max_levels(local),
        "guaranteed_union": path_union(candidates, "guaranteed"),
        "possible_union": path_union(candidates, "possible_paths"),
        "capital_additions": capital_additions(candidates),
        "tags": profile_tags(candidates, remote),
        "native_standard": native_standard,
        "native_special": native_special,
        "possible_standard": possible_standard,
        "possible_special": possible_special,
    }


def render_candidate_cell(
    candidates: list[dict[str, object]],
    limit: int = 3,
) -> str:
    if not candidates:
        return "—"
    values = [
        f"{candidate['name']} #{candidate['id']} ({candidate['source_text']})"
        for candidate in candidates[:limit]
    ]
    if len(candidates) > limit:
        values.append(f"ほか{len(candidates) - limit}")
    return "; ".join(values)


def rover_status(candidate: dict[str, object]) -> str:
    guaranteed = int(candidate["guaranteed_breadth"])
    possible = int(candidate["possible_breadth"])
    if guaranteed >= 4:
        return "Guaranteed wide"
    if guaranteed >= 3:
        return "Guaranteed broad"
    if guaranteed == 2:
        return "Guaranteed dual"
    if possible >= 4:
        return "Random-assisted wide"
    return "Random-assisted"


def nation_page(profile: dict[str, object]) -> str:
    nation = profile["nation"]
    candidates = profile["candidates"]
    rovers = profile["rovers"]
    remote = profile["remote"]

    lines = front_matter(f"{nation['code']} {nation['name']} Site Search能力")
    lines.extend(
        [
            f"# {nation['code']} {nation['name']} — Site Search能力",
            "",
            f"> **{nation['epithet']}**",
            "",
            f"[Recruitデータ](../../recruitment/{nation['dir']}/{nation['slug']}.md) · "
            f"[国家攻略](../../../nations/{nation['dir']}/{nation['slug']}.md) · "
            "[Site Search完全ガイド](../../../magic/site-search.md) · "
            "[運用Playbook](../../../magic/site-search-playbook.md)",
            "",
            '!!! info "自動生成された探索能力Profile"',
            "    Recruitable commanderの固定Path、100%単一Path random、通常Random pool、Recruit source、Remote Search Spell要求を結合します。Tier表ではなく、探索計画の素材です。",
            "",
            "## 概要",
            "",
            "| 項目 | 内容 |",
            "|---|---|",
            f"| Recruitable Mage record | {len(candidates)} |",
            f"| 全Recruitの保証Path最大 | {esc(level_text(profile['guaranteed']))} |",
            f"| Random込み理論最大 | {esc(level_text(profile['possible']))} |",
            f"| Any-fort保証最大 | {esc(level_text(profile['any_fort_levels']))} |",
            f"| Broad Rover候補 | {len(rovers)} |",
            f"| Native Remote Search | 標準 {profile['native_standard']}/9・特殊 {profile['native_special']}/3 |",
            f"| Random-assisted Remote | 標準 {profile['possible_standard']}/9・特殊 {profile['possible_special']}/3 |",
            f"| Capital追加 | {esc(level_text(profile['capital_additions']))} |",
            f"| Profile | {esc(', '.join(profile['tags']))} |",
            "",
            "## Manual Search coverage",
            "",
            "| Path | Any-fort保証 | Capital保証 | Local / Coastal保証 | 全Recruit保証 | Random込み理論最大 | 最良保証候補 |",
            "|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    for path in PATH_ORDER:
        guaranteed_candidates = per_path_candidates(candidates, path)
        lines.append(
            f"| {path} — {PATH_NAMES[path]} | "
            f"{profile['any_fort_levels'].get(path, 0) or '—'} | "
            f"{profile['capital_levels'].get(path, 0) or '—'} | "
            f"{profile['local_levels'].get(path, 0) or '—'} | "
            f"{profile['guaranteed'].get(path, 0) or '—'} | "
            f"{profile['possible'].get(path, 0) or '—'} | "
            f"{esc(render_candidate_cell(guaranteed_candidates))} |"
        )

    lines.extend(
        [
            "",
            "### Coverageの読み方",
            "",
            "- **保証**には固定Pathと、100%・候補Pathが一つだけのrandom groupを含めます。",
            "- **Random込み理論最大**は、各Pathへrandom pickが最大限偏った場合です。異なるPathの最大値を同時に得られるとは限りません。",
            "- Any-fort、Capital、Local / CoastalはRecruit source別です。同じUnitが複数sourceへ現れる場合があります。",
            "",
            "## Broad Rover候補",
            "",
            "| Mage | ID | Recruit source | Status | Guaranteed | Random | 保証幅 | 理論幅 | Map Move | Research bonus | 制約 |",
            "|---|---:|---|---|---|---|---:|---:|---:|---:|---|",
        ]
    )
    for candidate in rovers:
        lines.append(
            f"| {esc(candidate['name'])} | {candidate['id']} | {esc(candidate['source_text'])} | "
            f"{rover_status(candidate)} | {esc(level_text(candidate['guaranteed']))} | "
            f"{esc(candidate['random_text'])} | {candidate['guaranteed_breadth']} | "
            f"{candidate['possible_breadth']} | {candidate['mapmove'] or '—'} | "
            f"{candidate['research'] or '—'} | {esc(candidate['constraints'])} |"
        )
    if not rovers:
        lines.append("| — | — | — | 明確なmulti-Path候補なし | — | — | — | — | — | — | — |")

    lines.extend(
        [
            "",
            "Broad Roverの候補判定は、保証二Path以上、またはRandom込み三Path以上です。研究価値、Gold、Commander Point、Pathの戦闘価値は順位へ直接換算していません。",
            "",
            "## Deep Specialist",
            "",
            "| Path | 保証最大 | 保証候補 | Random込み理論最大 | 理論候補 |",
            "|---|---:|---|---:|---|",
        ]
    )
    for path in PATH_ORDER:
        guaranteed_candidates = per_path_candidates(candidates, path)
        possible_candidates = per_path_candidates(candidates, path, possible=True)
        lines.append(
            f"| {path} — {PATH_NAMES[path]} | {profile['guaranteed'].get(path, 0) or '—'} | "
            f"{esc(render_candidate_cell(guaranteed_candidates))} | "
            f"{profile['possible'].get(path, 0) or '—'} | "
            f"{esc(render_candidate_cell(possible_candidates))} |"
        )

    lines.extend(
        [
            "",
            "## Remote Search operator",
            "",
            "| Spell | Kind | Research | Req | Cost | Scope | Guaranteed operator | Random-assisted possible |",
            "|---|---|---|---|---|---|---|---|",
        ]
    )
    for item in remote:
        row = item["row"]
        effect = item["effect"]
        lines.append(
            f"| {esc(row.get('name') or '(unnamed)')} | {esc(item['kind'])} | "
            f"{esc(spell_research(row))} | {esc(spell_path(row))} | "
            f"{esc(spell_gem_cost(row, effect))} | {esc(item['scope'])} | "
            f"{esc(render_candidate_cell(item['native']))} | "
            f"{esc(render_candidate_cell(item['possible']))} |"
        )

    lines.extend(
        [
            "",
            "### Remote accessの意味",
            "",
            "- **Guaranteed operator**はRecruit直後の保証Pathだけで要求を満たします。Booster、Empowerment、Communion、Hero、Summon Mageは含みません。",
            "- **Random-assisted possible**は、random pickのある結果で要求を満たせることだけを示し、出現確率は計算しません。",
            "- SpellのResearch、Gem / Blood Slave、Ritual range、敵Province制限、海・Cave条件は別の制約です。",
            "",
            "## この国家で計画するとき",
            "",
            "1. Any-fort保証Pathから、量産可能なSearch coverageを決める。",
            "2. Capital追加Pathが国家戦略上重要なら、首都Mageを何Turn探索へ出せるか計算する。",
            "3. Broad Rover候補はExpansion後方の一本道へ置き、往復を避ける。",
            "4. Deep Specialistは全領土ではなく、Fort候補・Throne・Cave・Sea・主力Gem Pathへ限定する。",
            "5. Remote Searchは保証operatorを優先し、Random個体を国家計画の前提にしすぎない。",
            "",
            "## 限界",
            "",
            "- Gold cost、Commander Point、Researchの最終値、Map terrain cost、Old Age、Stealth発見Riskは完全評価していません。",
            "- Randomの同時成立確率は計算しません。`possible`は理論上の実現可能性です。",
            "- Booster、Pretender、Hero、召喚Mage、Magic Site Mage、Mercenary、Communion / Sabbathは別レイヤーです。",
            "- Manual Searchの最終挙動、Holy Search、Remote target制限はゲーム内表示を優先してください。",
            "",
            "## 関連ページ",
            "",
            "- [全国家Site Search能力](../index.md)",
            "- [Path coverage比較](../path-coverage.md)",
            "- [Broad Rover候補](../broad-rovers.md)",
            "- [Deep Specialist比較](../deep-specialists.md)",
            "- [Remote Search access](../remote-access.md)",
            "- [Search Level分布](../../sites/search-levels.md)",
            "- [Remote Site Search Spell](../../spells/site-search.md)",
            "",
        ]
    )
    return "\n".join(lines)


def index_page(profiles: list[dict[str, object]]) -> str:
    lines = front_matter("国家別Site Search能力")
    lines.extend(
        [
            "# 国家別Site Search能力",
            "",
            "全103国家のRecruitable Mageから、Manual Search coverage、Broad Rover候補、Deep Specialist、Remote Search operatorを比較します。",
            "",
            "- [Site Search完全ガイド](../../magic/site-search.md)",
            "- [Site Search運用Playbook](../../magic/site-search-playbook.md)",
            "- [Path coverage比較](path-coverage.md)",
            "- [Broad Rover候補](broad-rovers.md)",
            "- [Deep Specialist比較](deep-specialists.md)",
            "- [Remote Search access](remote-access.md)",
            "- [データ品質・判定基準](data-quality.md)",
            "",
            '!!! warning "Tier表ではありません"',
            "    Path幅が広いMageでも高価・首都限定・高Researchなら探索へ出しにくく、Path幅が狭い国家でも安価なMage量産やRemote Searchで十分な場合があります。",
            "",
        ]
    )

    for era in ("EA", "MA", "LA"):
        selected = [profile for profile in profiles if profile["nation"]["code"] == era]
        lines.extend(
            [
                f"## {era}",
                "",
                "| Nation | Any-fort保証 | 全保証 | Random込み | Broad Rover | Deepest | Native remote | Capital追加 | Profile | Detail |",
                "|---|---|---|---|---|---|---|---|---|---|",
            ]
        )
        for profile in selected:
            rovers = profile["rovers"]
            rover = (
                f"{rovers[0]['name']} ({rovers[0]['guaranteed_breadth']}/{rovers[0]['possible_breadth']})"
                if rovers
                else "—"
            )
            maximum = max(profile["guaranteed"].values(), default=0)
            deepest = " ".join(
                path
                for path in PATH_ORDER
                if profile["guaranteed"].get(path, 0) == maximum and maximum > 0
            )
            deepest_text = f"{deepest}{maximum}" if maximum else "—"
            remote_text = (
                f"{profile['native_standard']}/9 + {profile['native_special']}/3"
            )
            nation = profile["nation"]
            lines.append(
                f"| {esc(nation['name'])} | {esc(level_text(profile['any_fort_levels']))} | "
                f"{esc(level_text(profile['guaranteed']))} | {esc(level_text(profile['possible']))} | "
                f"{esc(rover)} | {esc(deepest_text)} | {remote_text} | "
                f"{esc(level_text(profile['capital_additions']))} | "
                f"{esc(', '.join(profile['tags']))} | "
                f"[表示]({nation['dir']}/{nation['slug']}.md) |"
            )
        lines.append("")

    lines.extend(
        [
            "## 表の読み方",
            "",
            "- **Any-fort保証**は各Fortで繰り返し雇えるMageの保証Path最大。",
            "- **全保証**はCapital、Fort不要・地形、Coastalを含むRecruitable Mage全体。",
            "- **Random込み**は各Pathの理論最大で、同時成立を意味しない。",
            "- **Broad Rover**の括弧は保証Path幅 / Random込み理論幅。",
            "- **Native remote**は標準単一Path9種 + 特殊3種のうち、保証PathでCast可能な数。",
            "- **Capital追加**はCapital-only Mageが、Capital以外のRecruit accessより高くするPath。",
            "",
        ]
    )
    return "\n".join(lines)


def path_coverage_page(profiles: list[dict[str, object]]) -> str:
    lines = front_matter("国家別Site Search Path coverage")
    lines.extend(
        [
            "# 国家別Site Search Path coverage",
            "",
            "各Pathの保証最大 / Random込み理論最大を比較します。`2/4*`は保証L2、Randomが最大限偏った場合L4を意味します。",
            "",
            "[国家別Site Search能力へ戻る](index.md)",
            "",
        ]
    )
    for era in ("EA", "MA", "LA"):
        lines.extend(
            [
                f"## {era}",
                "",
                "| Nation | " + " | ".join(PATH_ORDER) + " |",
                "|---|" + "---:|" * len(PATH_ORDER),
            ]
        )
        for profile in [item for item in profiles if item["nation"]["code"] == era]:
            cells: list[str] = []
            for path in PATH_ORDER:
                guaranteed = int(profile["guaranteed"].get(path, 0))
                possible = int(profile["possible"].get(path, 0))
                if possible <= 0:
                    cells.append("—")
                elif possible == guaranteed:
                    cells.append(str(guaranteed))
                else:
                    cells.append(f"{guaranteed or '—'}/{possible}*")
            nation = profile["nation"]
            lines.append(
                f"| [{esc(nation['name'])}]({nation['dir']}/{nation['slug']}.md) | "
                + " | ".join(cells)
                + " |"
            )
        lines.append("")
    lines.extend(
        [
            "## 注意",
            "",
            "- Pathごとの理論最大は別々のrandom結果を仮定するため、同じ個体で同時に達成できない場合があります。",
            "- 100%・単一候補Pathのrandom groupは保証値へ加算します。",
            "- Hero、Pretender、召喚Mage、Site Mage、Boosterは含みません。",
            "",
        ]
    )
    return "\n".join(lines)


def broad_rover_page(profiles: list[dict[str, object]]) -> str:
    rows_out: list[tuple[dict[str, object], dict[str, object]]] = []
    for profile in profiles:
        for candidate in profile["rovers"]:
            if int(candidate["guaranteed_breadth"]) >= 3 or int(candidate["possible_breadth"]) >= 4:
                rows_out.append((profile, candidate))
    rows_out.sort(
        key=lambda pair: (
            -int(pair[1]["guaranteed_breadth"]),
            -int(pair[1]["possible_breadth"]),
            0 if pair[1]["any_fort"] else 1,
            pair[0]["nation"]["code"],
            pair[0]["nation"]["name"],
            pair[1]["name"],
        )
    )

    lines = front_matter("全国家Broad Rover候補")
    lines.extend(
        [
            "# 全国家Broad Rover候補",
            "",
            "保証三Path以上、またはRandom込み四Path以上のRecruitable Mageを抽出します。",
            "",
            "[国家別Site Search能力へ戻る](index.md)",
            "",
            f"候補Relation: **{len(rows_out)}**",
            "",
            "| Nation | Mage | ID | Source | Guaranteed | Random | 保証幅 | 理論幅 | Move | Research bonus | 制約 |",
            "|---|---|---:|---|---|---|---:|---:|---:|---:|---|",
        ]
    )
    for profile, candidate in rows_out:
        nation = profile["nation"]
        lines.append(
            f"| [{nation['code']} {esc(nation['name'])}]({nation['dir']}/{nation['slug']}.md) | "
            f"{esc(candidate['name'])} | {candidate['id']} | {esc(candidate['source_text'])} | "
            f"{esc(level_text(candidate['guaranteed']))} | {esc(candidate['random_text'])} | "
            f"{candidate['guaranteed_breadth']} | {candidate['possible_breadth']} | "
            f"{candidate['mapmove'] or '—'} | {candidate['research'] or '—'} | "
            f"{esc(candidate['constraints'])} |"
        )
    if not rows_out:
        lines.append("| — | — | — | — | — | — | — | — | — | — | — |")
    lines.extend(
        [
            "",
            "Path幅だけでSearcherの採用価値は決まりません。Capital-only、高Research、Slow-to-recruitなら機会費用が高くなります。",
            "",
        ]
    )
    return "\n".join(lines)


def deep_specialist_page(profiles: list[dict[str, object]]) -> str:
    lines = front_matter("全国家Deep Specialist比較")
    lines.extend(
        [
            "# 全国家Deep Specialist比較",
            "",
            "各Pathについて保証L3以上を持つ国家・Recruitable Mageを抽出します。RandomだけでL3へ届く候補は各国家詳細で確認します。",
            "",
            "[国家別Site Search能力へ戻る](index.md)",
            "",
        ]
    )
    for path in PATH_ORDER:
        entries: list[tuple[dict[str, object], list[dict[str, object]]]] = []
        for profile in profiles:
            maximum = int(profile["guaranteed"].get(path, 0))
            if maximum < 3:
                continue
            entries.append((profile, per_path_candidates(profile["candidates"], path)))
        entries.sort(
            key=lambda pair: (
                -int(pair[0]["guaranteed"].get(path, 0)),
                pair[0]["nation"]["code"],
                pair[0]["nation"]["name"],
            )
        )
        lines.extend(
            [
                f"## {path} — {PATH_NAMES[path]}（{len(entries)}国家）",
                "",
                "| Nation | 保証最大 | Candidate | Recruit source | Capital追加 |",
                "|---|---:|---|---|---|",
            ]
        )
        for profile, candidates in entries:
            nation = profile["nation"]
            source_labels = sorted(
                {candidate["source_text"] for candidate in candidates}
            )
            lines.append(
                f"| [{nation['code']} {esc(nation['name'])}]({nation['dir']}/{nation['slug']}.md) | "
                f"{profile['guaranteed'][path]} | {esc(render_candidate_cell(candidates))} | "
                f"{esc('; '.join(source_labels))} | "
                f"{'Yes' if path in profile['capital_additions'] else '—'} |"
            )
        if not entries:
            lines.append("| — | — | — | — | — |")
        lines.append("")
    return "\n".join(lines)


def remote_access_page(
    profiles: list[dict[str, object]],
    spells: list[dict[str, object]],
) -> str:
    lines = front_matter("国家別Remote Site Search access")
    lines.extend(
        [
            "# 国家別Remote Site Search access",
            "",
            "各Remote Site Search Spellについて、保証PathでCastできる国家とRandom-assistedで理論上可能な国家を分けます。",
            "",
            "[国家別Site Search能力へ戻る](index.md)",
            "",
        ]
    )
    for spell_index, spell in enumerate(spells):
        row = spell["row"]
        native_profiles: list[dict[str, object]] = []
        possible_profiles: list[dict[str, object]] = []
        native_any_fort = 0
        for profile in profiles:
            access = profile["remote"][spell_index]
            if access["native"]:
                native_profiles.append(profile)
                if any(candidate["any_fort"] for candidate in access["native"]):
                    native_any_fort += 1
            elif access["possible"]:
                possible_profiles.append(profile)
        native_profiles.sort(key=lambda value: (value["nation"]["code"], value["nation"]["name"]))
        possible_profiles.sort(key=lambda value: (value["nation"]["code"], value["nation"]["name"]))

        lines.extend(
            [
                f"## {esc(row.get('name') or '(unnamed)')}",
                "",
                "| 項目 | 内容 |",
                "|---|---|",
                f"| Kind | {esc(spell['kind'])} |",
                f"| Research | {esc(spell_research(row))} |",
                f"| Req | {esc(spell_path(row))} |",
                f"| Cost | {esc(spell_gem_cost(row, spell['effect']))} |",
                f"| Scope | {esc(spell['scope'])} |",
                f"| Native nation | {len(native_profiles)}（Any-fort operatorあり {native_any_fort}） |",
                f"| Random-assisted nation | {len(possible_profiles)} |",
                "",
                "### Native",
                "",
                ", ".join(
                    f"[{profile['nation']['code']} {esc(profile['nation']['name'])}]"
                    f"({profile['nation']['dir']}/{profile['nation']['slug']}.md)"
                    for profile in native_profiles
                )
                or "該当国家なし。",
                "",
                "### Random-assisted possible",
                "",
                ", ".join(
                    f"[{profile['nation']['code']} {esc(profile['nation']['name'])}]"
                    f"({profile['nation']['dir']}/{profile['nation']['slug']}.md)"
                    for profile in possible_profiles
                )
                or "該当国家なし。",
                "",
            ]
        )
    lines.extend(
        [
            "## 注意",
            "",
            "- NativeはRecruitable Mageの保証Pathだけを使用します。",
            "- Random-assistedは確率を計算せず、あるrandom結果で要求を満たせるかだけを判定します。",
            "- Booster、Empowerment、Communion、Hero、Pretender、召喚Mageは含みません。",
            "",
        ]
    )
    return "\n".join(lines)


def data_quality_page(
    profiles: list[dict[str, object]],
    spells: list[dict[str, object]],
) -> str:
    candidates = [candidate for profile in profiles for candidate in profile["candidates"]]
    rover_relations = [candidate for profile in profiles for candidate in profile["rovers"]]
    unique_mages = {int(candidate["id"]) for candidate in candidates}
    source_counts: Counter[str] = Counter()
    for candidate in candidates:
        for source_name in candidate["sources"]:
            source_counts[source_name] += 1
    native_relations = sum(
        bool(item["native"])
        for profile in profiles
        for item in profile["remote"]
    )
    possible_relations = sum(
        bool(item["possible"])
        for profile in profiles
        for item in profile["remote"]
    )
    no_mages = [
        profile for profile in profiles if not profile["candidates"]
    ]
    single = [spell for spell in spells if spell["kind"] == "Single Path"]
    special = [spell for spell in spells if spell["kind"] == "Special"]

    lines = front_matter("国家別Site Search能力データ品質")
    lines.extend(
        [
            "# 国家別Site Search能力データ品質",
            "",
            "| 検査・集計 | 値 |",
            "|---|---:|",
            f"| 国家 | {len(profiles)} |",
            f"| Nation–Mage relation | {len(candidates)} |",
            f"| 固有Mage Unit record | {len(unique_mages)} |",
            f"| Broad Rover候補Relation | {len(rover_relations)} |",
            f"| Any-fort Mage relation | {source_counts['Any fort']} |",
            f"| Capital-only Mage relation | {source_counts['Capital-only']} |",
            f"| Fort不要 / terrain Mage relation | {source_counts['Fort不要 / terrain']} |",
            f"| Coastal Mage relation | {source_counts['Coastal']} |",
            f"| Single-Path Remote Search Spell | {len(single)} |",
            f"| Special Remote Search Spell | {len(special)} |",
            f"| Nation–Spell native access relation | {native_relations} |",
            f"| Nation–Spell random-assisted relation | {possible_relations} |",
            f"| Recruitable Mage recordなしの国家 | {len(no_mages)} |",
            "",
            "## 判定境界",
            "",
            "### 保証Path",
            "",
            "- BaseUの固定Path。",
            "- 100%かつ候補Pathが一つだけのrandom groupは、実質的に保証されるため加算。",
            "- 100%でも複数候補Pathから選ぶrandomは、どのPathになるか保証されないためRandom側。",
            "",
            "### Random込み理論最大",
            "",
            "- 各random pickが特定Pathへ最大限偏った場合。",
            "- Path別最大値を同じ個体で同時に得られるとは限らない。",
            "- Remote SpellのRandom-assisted判定では、要求Pathを同時に満たすrandom割当が存在するかを状態探索する。",
            "- 確率は計算しない。",
            "",
            "### Recruit source",
            "",
            "- Fort mappingの`capitalhome`なし：Any fort。",
            "- Fort mappingの`capitalhome`あり：Capital-only。",
            "- nonfort mapping：Fort不要 / terrain。",
            "- coast mapping：Coastal。",
            "",
            "### 含まないもの",
            "",
            "- Hero、Pretender、召喚Mage、Magic Site Mage、Mercenary。",
            "- Booster、Empowerment、Communion / Sabbath。",
            "- Gold、Commander Point、最終Research、Old Age、Map terrain cost。",
            "- Searcher死亡Risk、外交、前線までの距離。",
            "",
            "## 検証",
            "",
            f"- 標準Remote Search Path coverage: **{''.join(sorted({next(iter(requirement_levels(spell['row'])), '?') for spell in single})) or '—'}**",
            f"- 期待する標準Path: **{''.join(ARCANE_PATHS)}**",
            f"- 特殊Search: **{', '.join(str(spell['row'].get('name') or '') for spell in special)}**",
            "",
        ]
    )
    if no_mages:
        lines.extend(
            [
                "### Recruitable Mage recordなし",
                "",
                ", ".join(
                    f"{profile['nation']['code']} {profile['nation']['name']}"
                    for profile in no_mages
                ),
                "",
            ]
        )
    return "\n".join(lines)


def _insert_after(path: Path, anchor: str, additions: list[str]) -> None:
    if not path.exists():
        raise FileNotFoundError(f"generated page missing: {path}")
    text = path.read_text(encoding="utf-8")
    missing = [addition for addition in additions if addition not in text]
    if not missing:
        return
    if anchor not in text:
        raise ValueError(f"anchor not found in {path}: {anchor}")
    text = text.replace(anchor, anchor + "\n" + "\n".join(missing), 1)
    path.write_text(text, encoding="utf-8")


def patch_generated_pages(profiles: list[dict[str, object]]) -> None:
    _insert_after(
        RECRUIT_OUT / "index.md",
        "- [Mage access早見表](../mage-access.md)",
        ["- [国家別Site Search能力](../site-search/index.md)"],
    )
    _insert_after(
        MAGE_ACCESS,
        "- [国家Recruitデータ](recruitment/index.md)",
        ["- [国家別Site Search能力](site-search/index.md)"],
    )
    _insert_after(
        SITE_INDEX,
        "- [Site Search運用Playbook](../../magic/site-search-playbook.md)",
        ["- [国家別Site Search能力](../site-search/index.md)"],
    )
    _insert_after(
        SPELL_SEARCH_INDEX,
        "- [Site Search運用Playbook](../../magic/site-search-playbook.md)",
        ["- [国家別Site Search能力](../site-search/index.md)"],
    )

    for profile in profiles:
        nation = profile["nation"]
        path = RECRUIT_OUT / nation["dir"] / f"{nation['slug']}.md"
        if not path.exists():
            raise FileNotFoundError(f"recruit page missing: {path}")
        text = path.read_text(encoding="utf-8")
        label = f"[Site Search能力](../../site-search/{nation['dir']}/{nation['slug']}.md)"
        if label in text:
            continue
        anchor = f"[国家攻略ページへ戻る](../../../nations/{nation['dir']}/{nation['slug']}.md)"
        if anchor not in text:
            raise ValueError(f"nation page anchor missing: {path}")
        text = text.replace(anchor, anchor + f" · {label}", 1)
        path.write_text(text, encoding="utf-8")


def validate(
    profiles: list[dict[str, object]],
    spells: list[dict[str, object]],
    errors: list[str],
) -> None:
    if len(profiles) != 103:
        raise ValueError(f"nation profile count mismatch: {len(profiles)}")
    if len({int(profile["nation"]["id"]) for profile in profiles}) != len(profiles):
        raise ValueError("duplicate nation profile ID")
    standard = [spell for spell in spells if spell["kind"] == "Single Path"]
    special = [spell for spell in spells if spell["kind"] == "Special"]
    if len(standard) != 9:
        raise ValueError(f"single-Path Site Search count mismatch: {len(standard)}")
    if len(special) != 3:
        raise ValueError(f"special Site Search count mismatch: {len(special)}")
    standard_paths = {
        next(iter(requirement_levels(spell["row"])), "")
        for spell in standard
    }
    if standard_paths != set(ARCANE_PATHS):
        raise ValueError(
            f"remote Path coverage mismatch: found={sorted(standard_paths)} "
            f"expected={list(ARCANE_PATHS)}"
        )
    if errors:
        raise ValueError("; ".join(errors))


def write_pages(profiles: list[dict[str, object]], spells: list[dict[str, object]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for profile in profiles:
        nation = profile["nation"]
        path = OUT / nation["dir"] / f"{nation['slug']}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(nation_page(profile), encoding="utf-8")

    (OUT / "index.md").write_text(index_page(profiles), encoding="utf-8")
    (OUT / "path-coverage.md").write_text(
        path_coverage_page(profiles), encoding="utf-8"
    )
    (OUT / "broad-rovers.md").write_text(
        broad_rover_page(profiles), encoding="utf-8"
    )
    (OUT / "deep-specialists.md").write_text(
        deep_specialist_page(profiles), encoding="utf-8"
    )
    (OUT / "remote-access.md").write_text(
        remote_access_page(profiles, spells), encoding="utf-8"
    )
    (OUT / "data-quality.md").write_text(
        data_quality_page(profiles, spells), encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    paths = {name: source(name, args.refresh, args.offline) for name in FILES}
    nation_rows = nations()
    units = unit_data(paths["BaseU.csv"])
    maps = {
        "fl": mapping(paths["fort_leader_types_by_nation.csv"]),
        "nl": mapping(paths["nonfort_leader_types_by_nation.csv"]),
        "cl": mapping(paths["coast_leader_types_by_nation.csv"]),
    }
    search_spells, errors = build_search_spell_rows(
        tsv(paths["spells.csv"]),
        tsv(paths["effects_spells.csv"]),
    )

    profiles = []
    for nation in nation_rows:
        candidates = collect_candidates(int(nation["id"]), maps, units)
        profiles.append(nation_profile(nation, candidates, search_spells))

    validate(profiles, search_spells, errors)
    write_pages(profiles, search_spells)
    patch_generated_pages(profiles)

    all_candidates = [
        candidate for profile in profiles for candidate in profile["candidates"]
    ]
    print(f"source commit: {COMMIT}")
    print(f"nation profiles: {len(profiles)}")
    print(f"nation-mage relations: {len(all_candidates)}")
    print(f"unique mage units: {len({candidate['id'] for candidate in all_candidates})}")
    print(
        "Broad Rover relations: "
        f"{sum(len(profile['rovers']) for profile in profiles)}"
    )
    print(
        "native remote nation-spell relations: "
        f"{sum(bool(item['native']) for profile in profiles for item in profile['remote'])}"
    )
    print(
        "random-assisted remote nation-spell relations: "
        f"{sum(bool(item['possible']) for profile in profiles for item in profile['remote'])}"
    )
    print(f"nation detail pages: {len(list(OUT.glob('*/*.md')))}")


if __name__ == "__main__":
    main()
