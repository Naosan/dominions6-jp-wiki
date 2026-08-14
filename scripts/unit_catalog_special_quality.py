from __future__ import annotations

from pathlib import Path

from unit_catalog_event_quality import write_quality_report as write_event_quality_report


def _esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def _coverage_rows(stats: dict[str, int]) -> str:
    rows = []
    for key, label in (
        ("items_with_unit_relations", "Magic Items with direct Unit fields"),
        ("item_unit_relations", "Magic Item Unit / transform / encounter relations"),
        ("item_units", "Unique Unit records referenced by Magic Items"),
        ("item_random_references", "Magic Item random-pool / sentinel references"),
        ("unresolved_item_targets", "Unresolved positive Magic Item Unit targets"),
        ("spell_random_references", "Spell Negative Monster Number / Montag references"),
        ("special_spell_relations", "Wish / unique / terrain / procedural Spell relations"),
        ("special_unique_pool_entries", "Special unique summon table entries"),
        ("terrain_pool_entries", "Terrain-specific summon table entries"),
        ("unresolved_special_spell_pools", "Unresolved special summon pool numbers"),
        ("arena_items", "Arena-related Magic Items"),
    ):
        rows.append(f"| {label} | {stats.get(key, 0)} |")
    return "\n".join(rows)


def write_quality_report(data, out: Path, stats: dict[str, int]) -> Path:
    path = write_event_quality_report(data, out, stats)
    text = path.read_text(encoding="utf-8")

    anchor = f"| 現在の索引で入手経路未分類 | {stats['unclassified']} |"
    if anchor in text:
        text = text.replace(anchor, anchor + "\n" + _coverage_rows(stats), 1)

    sections = [
        "## Item random-pool references",
        "",
        "Magic Item fieldが負のMonster Number、Montag、その他の負値を参照する場合、単一Unitへは結び付けません。",
        "",
        "| Item ID | Item | Field | Raw target | Pool / sentinel | Relation |",
        "|---:|---|---|---:|---|---|",
    ]
    if data["item_random_targets"]:
        for relation in sorted(
            data["item_random_targets"],
            key=lambda item: (int(item["item_id"]), str(item["field"]), int(item["raw_target"])),
        ):
            sections.append(
                f"| {relation['item_id']} | {_esc(relation['item'])} | `{_esc(relation['field'])}` | "
                f"{relation['raw_target']} | {_esc(relation['target'])} | {_esc(relation['category'])} |"
            )
    else:
        sections.append("| — | — | — | — | 該当なし | — |")

    sections.extend(
        [
            "",
            "## Unresolved Item Unit targets",
            "",
            "| Item ID | Item | Field | Raw target |",
            "|---:|---|---|---:|",
        ]
    )
    if data["item_unresolved"]:
        for item_id, item_name, field, raw_target in data["item_unresolved"]:
            sections.append(
                f"| {item_id} | {_esc(item_name)} | `{_esc(field)}` | {raw_target} |"
            )
    else:
        sections.append("| — | — | — | 解決不能参照なし |")

    sections.extend(
        [
            "",
            "## Recognized Item Unit fields",
            "",
            "| Item field | Relations |",
            "|---|---:|",
        ]
    )
    if data["item_field_counts"]:
        for field, count in sorted(data["item_field_counts"].items()):
            sections.append(f"| `{_esc(field)}` | {count} |")
    else:
        sections.append("| — | 0 |")

    sections.extend(
        [
            "",
            "## Spell Random summon references",
            "",
            "| Spell ID | Spell | Effect # | Raw argument | Pool | Confidence |",
            "|---:|---|---:|---:|---|---|",
        ]
    )
    if data["spell_random_targets"]:
        for relation in sorted(
            data["spell_random_targets"],
            key=lambda item: (int(item["spell_id"]), int(item["effect_number"]), int(item["raw_argument"])),
        ):
            sections.append(
                f"| {relation['spell_id']} | {_esc(relation['spell'])} | {relation['effect_number']} | "
                f"{relation['raw_argument']} | {_esc(relation['pool'])} | {_esc(relation['confidence'])} |"
            )
    else:
        sections.append("| — | — | — | — | 該当なし | — |")

    sections.extend(
        [
            "",
            "## Unresolved standard Spell summon targets",
            "",
            "| Spell ID | Spell | Effect # | Raw argument |",
            "|---:|---|---:|---:|",
        ]
    )
    if data["unresolved_spells"]:
        for spell_id, spell_name, effect_number, raw_argument in data["unresolved_spells"]:
            sections.append(
                f"| {spell_id} | {_esc(spell_name)} | {effect_number} | {raw_argument} |"
            )
    else:
        sections.append("| — | — | — | 解決不能参照なし |")

    sections.extend(
        [
            "",
            "## Unresolved special summon pools",
            "",
            "| Spell ID | Spell | Effect # | Raw argument |",
            "|---:|---|---:|---:|",
        ]
    )
    if data["special_spell_unresolved"]:
        for spell_id, spell_name, effect_number, raw_argument in data["special_spell_unresolved"]:
            sections.append(
                f"| {spell_id} | {_esc(spell_name)} | {effect_number} | {raw_argument} |"
            )
    else:
        sections.append("| — | — | — | 解決不能poolなし |")

    insertion = "\n".join(sections) + "\n\n"
    marker = "## 解釈方針"
    if marker in text:
        text = text.replace(marker, insertion + marker, 1)
    else:
        text += "\n" + insertion

    text = text.replace(
        "`unclassified`は入手不能を意味しない。EventとMercenaryを追加分類した後も、Wish、Random table、hard-coded Reanimation結果、Adventure、Scenario等の未索引経路を含み得る。",
        "`unclassified`は入手不能を意味しない。Event、Mercenary、Magic Itemの固定Unit参照を追加分類した後も、Wishの任意結果、hard-coded Reanimation、Scenario等の未索引経路を含み得る。",
    )
    path.write_text(text, encoding="utf-8")
    return path
