from __future__ import annotations

from pathlib import Path

from unit_catalog_quality import write_quality_report as write_base_quality_report


def _escape(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def _coverage_rows(stats: dict[str, int]) -> str:
    rows = []
    for key, label in (
        ("unit_generation_sources", "Unit records with fixed generation / conversion fields"),
        ("unit_generation_relations", "Unit generation / conversion relations"),
        ("strategic_spawn_relations", "Strategic summon / Freespawn relations"),
        ("battle_spawn_relations", "Battle summon relations"),
        ("recruit_unlock_relations", "Unit-dependent recruit unlock relations"),
        ("conversion_relations", "Fixed conversion / resurrection relations"),
        ("generation_ability_units", "Units with non-target generation abilities"),
        ("generation_abilities", "Reanimation / Freespawn / summon-bonus abilities"),
        ("nation_generation_abilities", "Nation generation / Reanimation abilities"),
        ("nation_spawn_relations", "Nation ability relations resolved to fixed Unit IDs"),
        ("random_spawn_references", "Negative Monster Number / Montag references"),
        ("unresolved_unit_generation", "Unresolved positive Unit-generation targets"),
    ):
        rows.append(f"| {label} | {stats.get(key, 0)} |")
    return "\n".join(rows)


def write_quality_report(data, out: Path, stats: dict[str, int]) -> Path:
    path = write_base_quality_report(data, out, stats)
    text = path.read_text(encoding="utf-8")

    anchor = f"| 現在の索引で入手経路未分類 | {stats['unclassified']} |"
    if anchor in text:
        text = text.replace(anchor, anchor + "\n" + _coverage_rows(stats), 1)

    sections = [
        "## Random summon / pool references",
        "",
        "負のMonster NumberまたはMontag poolを参照する生成関係です。単一の固定Unit IDへは結び付けません。",
        "",
        "| Source ID | Source | Field | Raw target | Pool | Relation |",
        "|---:|---|---|---:|---|---|",
    ]
    random_rows = data.get("unit_generation_random_targets", [])
    if random_rows:
        for relation in sorted(
            random_rows,
            key=lambda item: (str(item["source"]), str(item["field"]), int(item["raw_target"])),
        ):
            sections.append(
                f"| {relation['source_id']} | {_escape(relation['source'])} | "
                f"`{_escape(relation['field'])}` | {relation['raw_target']} | "
                f"{_escape(relation['target'])} | {_escape(relation['kind'])} |"
            )
    else:
        sections.append("| — | — | — | — | 該当なし | — |")

    sections.extend(
        [
            "",
            "## Unresolved Unit-generation targets",
            "",
            "正値TargetがBaseUの固定Unit IDへ解決できなかった関係です。推測で補完しません。",
            "",
            "| Source ID | Source | Field | Raw target | Relation |",
            "|---:|---|---|---:|---|",
        ]
    )
    unresolved = data.get("unit_generation_unresolved", [])
    if unresolved:
        for source_id, source, field, raw_target, kind in unresolved:
            sections.append(
                f"| {source_id} | {_escape(source)} | `{_escape(field)}` | "
                f"{raw_target} | {_escape(kind)} |"
            )
    else:
        sections.append("| — | — | — | — | 解決不能参照なし |")

    sections.extend(
        [
            "",
            "## Unresolved nation-generation targets",
            "",
            "| Nation ID | Nation | Command | Raw target |",
            "|---:|---|---|---:|",
        ]
    )
    nation_unresolved = data.get("nation_generation_unresolved", [])
    if nation_unresolved:
        for nation_id, nation, command, raw_target in nation_unresolved:
            sections.append(
                f"| {nation_id} | {_escape(nation)} | `#{_escape(command)}` | {raw_target} |"
            )
    else:
        sections.append("| — | — | — | 解決不能参照なし |")

    sections.extend(
        [
            "",
            "## Recognized BaseU generation fields",
            "",
            "| Field | Relations |",
            "|---|---:|",
        ]
    )
    field_counts = data.get("unit_generation_field_counts", {})
    if field_counts:
        for field, count in sorted(field_counts.items()):
            sections.append(f"| `{_escape(field)}` | {count} |")
    else:
        sections.append("| — | 0 |")

    insertion = "\n".join(sections) + "\n\n"
    marker = "## 解釈方針"
    if marker in text:
        text = text.replace(marker, insertion + marker, 1)
    else:
        text += "\n" + insertion

    text = text.replace(
        "`unclassified`は入手不能を意味しない。Event、Freespawn、Random pool、Wish、Transformation等の未索引経路を含み得る。",
        "`unclassified`は入手不能を意味しない。Unit / Nation生成能力を追加分類した後も、Event、Wish、Random table、hard-coded Reanimation結果、Scenario等の未索引経路を含み得る。",
    )
    path.write_text(text, encoding="utf-8")
    return path
