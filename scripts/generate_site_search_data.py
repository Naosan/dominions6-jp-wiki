#!/usr/bin/env python3
"""Generate Site Search spell and Magic Site level reference pages."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path

from generate_recruitment_data import COMMIT, num, source, tsv
from generate_spell_item_data import (
    PATHS,
    SCHOOLS,
    effect_map,
    esc,
    spell_gem_cost,
    spell_path,
    spell_research,
)
from magic_site_data import (
    PATH_ORDER,
    decode_location,
    format_gems,
    gem_values,
    load_terrain_lookup,
)
from magic_site_page_common import site_filename

ROOT = Path(__file__).resolve().parents[1]
SITE_OUT = ROOT / "docs" / "data" / "sites"
SPELL_OUT = ROOT / "docs" / "data" / "spells"
FILES = (
    "MagicSites.csv",
    "site_terrain_types.csv",
    "spells.csv",
    "effects_spells.csv",
)

# Effect 48 is the single-Path remote Site Search effect. raw_argument is the
# Path number used by the Inspector's PATHS table.
SITE_SEARCH_EFFECT = 48
SPECIAL_SEARCH_SPELLS = {
    "Voice of Tiamat": {
        "scope": "Elemental Site（F/A/W/E）",
        "target": "海Province。Spell説明ではCasterが水中にいる必要がある。",
    },
    "Acashic Knowledge": {
        "scope": "全Magic PathのSite",
        "target": "敵Provinceには使用不可。",
    },
}
TARGET_NOTES = {
    "Augury": "Fire Site。Spell説明上は遠隔Provinceの土を使う占術。",
    "Auspex": "Air Site。敵Provinceには使用不可。",
    "Voice of Apsu": "地上のWater Site。発見情報が対象Province内へ共有される特殊性に注意。",
    "Gnome Lore": "Earth Site。Friendly Provinceを対象とする。",
    "Arcane Probing": "Astral Site。Friendly Provinceのみ。",
    "Dark Knowledge": "Death Site。敵Provinceには使用不可。",
    "Haruspex": "Nature Site。動物の内臓を用いる遠隔占術。",
    "At the End of the Rainbow": "Glamour Site。",
    "Bowl of Blood": "Blood Site。Blood Slaveを消費する。",
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


def spell_link(row: dict[str, str]) -> str:
    school = num(row, "school", -1)
    slug = SCHOOLS.get(school, ("", "index"))[1]
    return f"[{esc(row.get('name') or '(unnamed)')}](by-school/{slug}.md)"


def site_link(row: dict[str, str]) -> str:
    site_id = num(row, "id")
    return f"[{esc(row.get('name') or f'Site {site_id}')}]" f"(by-id/{site_filename(site_id)})"


def location_text(row: dict[str, str], terrain_lookup: dict[int, str]) -> str:
    raw = num(row, "loc")
    labels, remaining = decode_location(raw, terrain_lookup)
    output = list(labels)
    if remaining:
        output.append(f"Unknown bits {remaining}")
    return ", ".join(output) or "Unspecified / special placement"


def _researchable_spells(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    output: dict[str, dict[str, str]] = {}
    for row in rows:
        if num(row, "school", -1) not in SCHOOLS:
            continue
        name = (row.get("name") or "").strip()
        if not name or name in {"Nothing", "..."}:
            continue
        output[name] = row
    return output


def build_search_spell_rows(
    spell_rows: list[dict[str, str]],
    effect_rows: list[dict[str, str]],
) -> tuple[list[dict[str, object]], list[str]]:
    effects = effect_map(effect_rows)
    by_name = _researchable_spells(spell_rows)
    output: list[dict[str, object]] = []
    errors: list[str] = []

    for row in spell_rows:
        if num(row, "school", -1) not in SCHOOLS:
            continue
        effect = effects.get(num(row, "effect_record_id"))
        if not effect or num(effect, "effect_number") != SITE_SEARCH_EFFECT:
            continue
        path_number = num(effect, "raw_argument", -1)
        if path_number not in PATHS:
            errors.append(
                f"Spell {row.get('name')!r} has Site Search effect with unknown Path {path_number}"
            )
            continue
        code, path_name, _slug = PATHS[path_number]
        output.append(
            {
                "row": row,
                "effect": effect,
                "scope": f"{code} — {path_name} Site",
                "target": TARGET_NOTES.get(
                    str(row.get("name") or ""),
                    "単一Pathの全Site。対象制限はゲーム内targeterを優先。",
                ),
                "kind": "Single Path",
                "path_number": path_number,
            }
        )

    for name, spec in SPECIAL_SEARCH_SPELLS.items():
        row = by_name.get(name)
        if row is None:
            errors.append(f"Special Site Search Spell missing: {name}")
            continue
        effect = effects.get(num(row, "effect_record_id"))
        output.append(
            {
                "row": row,
                "effect": effect,
                "scope": spec["scope"],
                "target": spec["target"],
                "kind": "Special",
                "path_number": 99,
            }
        )

    output.sort(
        key=lambda item: (
            0 if item["kind"] == "Single Path" else 1,
            int(item["path_number"]),
            num(item["row"], "school"),
            num(item["row"], "researchlevel"),
            str(item["row"].get("name") or ""),
        )
    )
    return output, errors


def search_spell_page(rows: list[dict[str, object]]) -> str:
    single = [row for row in rows if row["kind"] == "Single Path"]
    special = [row for row in rows if row["kind"] == "Special"]
    lines = front_matter("Remote Site Search Spell")
    lines.extend(
        [
            "# Remote Site Search Spell",
            "",
            "Research可能Spellのうち、Magic Siteを遠隔探索するSpellを抽出します。単一Path探索はSpell effect **48** とPath argumentから機械的に判定し、複数Path・全Path探索は固定スナップショット内の明示Spellを別枠で扱います。",
            "",
            "- [Site Search完全ガイド](../../magic/site-search.md)",
            "- [Site Search運用Playbook](../../magic/site-search-playbook.md)",
            "- [Search Level分布](../sites/search-levels.md)",
            "- [Spellデータ索引](index.md)",
            "",
            "## 単一Path Remote Search",
            "",
            "| Spell | ID | Research | Req | Cost | Search scope | Target・運用上の注意 |",
            "|---|---:|---|---|---|---|---|",
        ]
    )
    for item in single:
        row = item["row"]
        effect = item["effect"]
        lines.append(
            f"| {spell_link(row)} | {num(row, 'id')} | {esc(spell_research(row))} | "
            f"{spell_path(row)} | {spell_gem_cost(row, effect)} | {esc(item['scope'])} | "
            f"{esc(item['target'])} |"
        )
    lines.extend(
        [
            "",
            "## 複数Path・全Path Search",
            "",
            "| Spell | ID | Research | Req | Cost | Search scope | Target・運用上の注意 |",
            "|---|---:|---|---|---|---|---|",
        ]
    )
    for item in special:
        row = item["row"]
        effect = item["effect"]
        lines.append(
            f"| {spell_link(row)} | {num(row, 'id')} | {esc(spell_research(row))} | "
            f"{spell_path(row)} | {spell_gem_cost(row, effect)} | {esc(item['scope'])} | "
            f"{esc(item['target'])} |"
        )
    lines.extend(
        [
            "",
            "## Holy Siteについて",
            "",
            "現行のResearch可能Spell setでは、effect 48のHoly単独Remote Searchを確認していません。Holy SiteはPriestによるManual Search、または全Path探索を含む特殊手段で確認します。",
            "",
            "## 表の限界",
            "",
            "- Remote Searchは対象PathについてSite Levelに依存せず発見する設計ですが、対象Province、海・陸、敵対所有、共有通知、Ritual rangeはSpell固有です。",
            "- Ritual rangeはこのCSV表だけで一貫して再構成できないため掲載していません。ゲーム内Spell詳細を優先してください。",
            "- `Voice of Tiamat`や`Acashic Knowledge`は単一Path effect 48ではなく、特殊な複数Path探索として分離しています。",
            "- `Strands of Arcane Power`のようなGlobal Enchantmentによる継続探索は、この一回型Remote Search表とは別の仕組みです。",
            "",
        ]
    )
    return "\n".join(lines)


def _site_records(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output = [row for row in rows if num(row, "id", -1) > 0]
    output.sort(key=lambda row: num(row, "id"))
    return output


def _count_cell(rows: list[dict[str, str]], search_level: int) -> str:
    total = len(rows)
    if total == 0:
        return "—"
    found = sum(num(row, "level") <= search_level for row in rows)
    return f"{found} ({found / total:.0%})"


def search_level_page(
    site_rows: list[dict[str, str]],
    terrain_rows: list[dict[str, str]],
) -> str:
    sites = _site_records(site_rows)
    terrain_lookup = load_terrain_lookup(terrain_rows)
    ordinary = [row for row in sites if num(row, "rarity") in {0, 1, 2}]
    actual_levels = sorted({num(row, "level") for row in sites})
    max_level = max(actual_levels, default=0)
    path_names = [name for name, _code, _slug in PATH_ORDER]
    extra_paths = sorted(
        {
            (row.get("path") or "Unknown").strip() or "Unknown"
            for row in sites
        }
        - set(path_names)
    )
    path_names.extend(extra_paths)

    lines = front_matter("Magic Site Search Level分布")
    lines.extend(
        [
            "# Magic Site Search Level分布",
            "",
            "`MagicSites.csv`のPath・Level・raw Rarityを集計し、Manual Searchの深さを決めるための参照表にします。これは**Site record候補数の分布**であり、Map上の実際の出現確率や期待Gem incomeそのものではありません。",
            "",
            f"- 全Site record: **{len(sites)}**",
            f"- raw Rarity 0–2のrecord: **{len(ordinary)}**",
            f"- 最大抽出Level: **{max_level}**",
            "",
            "- [Site Search完全ガイド](../../magic/site-search.md)",
            "- [Site Search運用Playbook](../../magic/site-search-playbook.md)",
            "- [Remote Site Search Spell](../spells/site-search.md)",
            "- [Magic Site総合索引](index.md)",
            "",
            "## Search Level別の累積record数",
            "",
            "raw Rarity 0–2のSite recordを対象に、各Pathを指定LevelでManual Searchした場合にLevel条件を満たすrecord数を数えます。",
            "",
            "| Path | Rarity 0–2 | L1以下 | L2以下 | L3以下 | L4以下 | 最大Level |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for path in path_names:
        selected = [row for row in ordinary if (row.get("path") or "Unknown") == path]
        path_max = max((num(row, "level") for row in selected), default=0)
        lines.append(
            f"| {esc(path)} | {len(selected)} | {_count_cell(selected, 1)} | "
            f"{_count_cell(selected, 2)} | {_count_cell(selected, 3)} | "
            f"{_count_cell(selected, 4)} | {path_max} |"
        )

    lines.extend(
        [
            "",
            "## Exact Level分布（全record）",
            "",
            "| Path | " + " | ".join(f"L{level}" for level in actual_levels) + " |",
            "|---|" + "---:|" * len(actual_levels),
        ]
    )
    for path in path_names:
        counts = Counter(
            num(row, "level")
            for row in sites
            if (row.get("path") or "Unknown") == path
        )
        lines.append(
            f"| {esc(path)} | "
            + " | ".join(str(counts.get(level, 0)) for level in actual_levels)
            + " |"
        )

    high_ordinary = [row for row in ordinary if num(row, "level") >= 4]
    high_special = [row for row in sites if num(row, "rarity") >= 5 and num(row, "level") >= 4]

    def append_site_table(title: str, selected: list[dict[str, str]]) -> None:
        lines.extend(
            [
                "",
                f"## {title}（{len(selected)}）",
                "",
                "| Site | ID | Path | Level | Rarity | Terrain / placement | Monthly gems |",
                "|---|---:|---|---:|---:|---|---|",
            ]
        )
        for row in sorted(
            selected,
            key=lambda value: (
                str(value.get("path") or ""),
                num(value, "level"),
                str(value.get("name") or ""),
                num(value, "id"),
            ),
        ):
            lines.append(
                f"| {site_link(row)} | {num(row, 'id')} | {esc(row.get('path') or 'Unknown')} | "
                f"{num(row, 'level')} | {num(row, 'rarity')} | "
                f"{esc(location_text(row, terrain_lookup))} | {format_gems(gem_values(row))} |"
            )
        if not selected:
            lines.append("| — | — | — | — | — | — | — |")

    append_site_table("Rarity 0–2かつLevel 4以上", high_ordinary)
    append_site_table("Rarity 5以上かつLevel 4以上", high_special)

    lines.extend(
        [
            "",
            "## 読み方",
            "",
            "- **Manual Search**では、Mageが持つ各Path Level以上に隠されたSiteは発見できません。Multi-path Mageは一回のSearchで複数Pathを同時に確認できます。",
            "- **Level 0**は通常、Provinceを所有した時点で見えるSiteとして扱われますが、特殊配置・Event・Throneはゲーム内表示を優先してください。",
            "- **Rarity 0–2**は通常Site候補を考えるための便宜的な集計です。RarityはSite Levelや価値のTierではありません。",
            "- **高Level Site**が低Level Siteより必ず高収入・高性能とは限りません。Search Levelを上げる判断は、SearcherのTurn、移動、Gem、残りTurn、特殊Recruitの価値と比較します。",
            "- **Remote Search Spell**は対象PathのLevel条件をまとめて解決できますが、GemとMage turnを消費し、Spell固有の対象制限があります。",
            "",
        ]
    )
    return "\n".join(lines)


def _insert_after(path: Path, anchor: str, additions: list[str]) -> None:
    if not path.exists():
        raise FileNotFoundError(f"generated index not found: {path}")
    text = path.read_text(encoding="utf-8")
    if additions[0] in text:
        return
    if anchor not in text:
        raise ValueError(f"generated index anchor not found in {path}: {anchor}")
    text = text.replace(anchor, anchor + "\n" + "\n".join(additions), 1)
    path.write_text(text, encoding="utf-8")


def patch_indexes() -> None:
    _insert_after(
        SITE_OUT / "index.md",
        "- [全Magic Site](all.md)",
        [
            "- [Search Level分布](search-levels.md)",
            "- [Remote Site Search Spell](../spells/site-search.md)",
            "- [Site Search完全ガイド](../../magic/site-search.md)",
            "- [Site Search運用Playbook](../../magic/site-search-playbook.md)",
        ],
    )
    _insert_after(
        SPELL_OUT / "index.md",
        "- [National / Realm restricted Spell](national.md)",
        [
            "- [Remote Site Search Spell](site-search.md)",
            "- [Site Search完全ガイド](../../magic/site-search.md)",
        ],
    )


def validate(
    site_rows: list[dict[str, str]],
    search_spells: list[dict[str, object]],
    errors: list[str],
) -> None:
    sites = _site_records(site_rows)
    standard = [row for row in search_spells if row["kind"] == "Single Path"]
    special = [row for row in search_spells if row["kind"] == "Special"]
    standard_paths = {int(row["path_number"]) for row in standard}

    if len(sites) < 1200:
        raise ValueError(f"Magic Site set appears incomplete: {len(sites)}")
    if len(standard) < 9:
        raise ValueError(f"Single-Path Site Search Spell set appears incomplete: {len(standard)}")
    if standard_paths != set(range(9)):
        raise ValueError(
            "Single-Path Site Search coverage mismatch: "
            f"found={sorted(standard_paths)} expected={list(range(9))}"
        )
    if len(special) < 2:
        raise ValueError(f"Special Site Search Spell set appears incomplete: {len(special)}")
    if max((num(row, "level") for row in sites), default=0) < 4:
        raise ValueError("Magic Site Level data appears incomplete")
    if errors:
        raise ValueError("; ".join(errors))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    paths = {name: source(name, args.refresh, args.offline) for name in FILES}
    site_rows = tsv(paths["MagicSites.csv"])
    terrain_rows = tsv(paths["site_terrain_types.csv"])
    spells, errors = build_search_spell_rows(
        tsv(paths["spells.csv"]),
        tsv(paths["effects_spells.csv"]),
    )
    validate(site_rows, spells, errors)

    SITE_OUT.mkdir(parents=True, exist_ok=True)
    SPELL_OUT.mkdir(parents=True, exist_ok=True)
    (SITE_OUT / "search-levels.md").write_text(
        search_level_page(site_rows, terrain_rows), encoding="utf-8"
    )
    (SPELL_OUT / "site-search.md").write_text(
        search_spell_page(spells), encoding="utf-8"
    )
    patch_indexes()

    sites = _site_records(site_rows)
    ordinary = [row for row in sites if num(row, "rarity") in {0, 1, 2}]
    print(f"source commit: {COMMIT}")
    print(f"Magic Site records: {len(sites)}")
    print(f"Rarity 0-2 Site records: {len(ordinary)}")
    print(f"maximum Site Level: {max(num(row, 'level') for row in sites)}")
    print(
        "single-Path Site Search Spells: "
        f"{sum(row['kind'] == 'Single Path' for row in spells)}"
    )
    print(
        "special Site Search Spells: "
        f"{sum(row['kind'] == 'Special' for row in spells)}"
    )


if __name__ == "__main__":
    main()
