from __future__ import annotations

from pathlib import Path

from unit_catalog_special_quality import write_quality_report as write_special_quality_report


def _esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def _coverage_rows(stats: dict[str, int]) -> str:
    rows = []
    for key, label in (
        ("spell_candidate_relations", "Explicit special Spell candidate relations"),
        ("special_candidate_units", "Unique Unit records in explicit special Spell candidates"),
        ("unique_pool_candidates", "Unique summon table candidate Unit records"),
        ("terrain_pool_candidates", "Terrain summon table candidate Unit records"),
        ("named_pool_candidates", "Named SpellTables candidate Unit records"),
        ("unresolved_special_candidates", "Unresolved special Spell candidate Unit IDs"),
    ):
        rows.append(f"| {label} | {stats.get(key, 0)} |")
    return "\n".join(rows)


def write_quality_report(data, out: Path, stats: dict[str, int]) -> Path:
    path = write_special_quality_report(data, out, stats)
    text = path.read_text(encoding="utf-8")

    anchor = f"| 現在の索引で入手経路未分類 | {stats['unclassified']} |"
    if anchor in text:
        text = text.replace(anchor, anchor + "\n" + _coverage_rows(stats), 1)

    sections = [
        "## Explicit special summon candidate source",
        "",
        "候補Unitは固定Dom6 Inspector snapshotの`scripts/DMI/SpellTables.js`に明示された配列から取得します。",
        "",
        "| Source table | Pools | Candidate references |",
        "|---|---:|---:|",
        f"| `MSpell.uniqueSummon` | {len(data['special_unique_pool_units'])} | {sum(len(values) for values in data['special_unique_pool_units'].values())} |",
        f"| `MSpell.terrainSummon` | {len(data['terrain_summon_pool_units'])} | {sum(len(values) for values in data['terrain_summon_pool_units'].values())} |",
        f"| Named arrays | {len(data['explicit_named_summon_pools'])} | {sum(len(values) for values in data['explicit_named_summon_pools'].values())} |",
        "",
        "候補Relationは『そのSpellで候補になり得る』ことを示し、全候補の同時取得や等確率を意味しません。",
        "",
        "## Unresolved special summon candidate Unit IDs",
        "",
        "| Spell ID | Spell | Effect # | Candidate Unit ID |",
        "|---:|---|---:|---:|",
    ]
    if data["special_candidate_unresolved"]:
        for spell_id, spell_name, effect_number, unit_id in data["special_candidate_unresolved"]:
            sections.append(
                f"| {spell_id} | {_esc(spell_name)} | {effect_number} | {unit_id} |"
            )
    else:
        sections.append("| — | — | — | 解決不能候補なし |")

    sections.extend(
        [
            "",
            "## Explicit named summon pools",
            "",
            "| Pool | Candidate Unit IDs |",
            "|---|---|",
        ]
    )
    for name, unit_ids in sorted(data["explicit_named_summon_pools"].items()):
        sections.append(
            f"| {_esc(name)} | {_esc(', '.join(str(unit_id) for unit_id in unit_ids) or '—')} |"
        )
    if not data["explicit_named_summon_pools"]:
        sections.append("| 該当なし | — |")

    insertion = "\n".join(sections) + "\n\n"
    marker = "## 解釈方針"
    if marker in text:
        text = text.replace(marker, insertion + marker, 1)
    else:
        text += "\n" + insertion

    text = text.replace(
        "`unclassified`は入手不能を意味しない。Event、Mercenary、Magic Itemの固定Unit参照を追加分類した後も、Wishの任意結果、hard-coded Reanimation、Scenario等の未索引経路を含み得る。",
        "`unclassified`は入手不能を意味しない。Event、Mercenary、Magic Item、SpellTablesの明示候補を追加分類した後も、Wishの任意入力結果、hard-coded Reanimation、Scenario等の未索引経路を含み得る。",
    )
    path.write_text(text, encoding="utf-8")
    return path
