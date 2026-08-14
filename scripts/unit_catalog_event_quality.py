from __future__ import annotations

from pathlib import Path

from unit_catalog_generation_quality import write_quality_report as write_generation_quality_report


def _esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def _coverage_rows(stats: dict[str, int]) -> str:
    rows = []
    for key, label in (
        ("events_with_unit_effects", "Events with recognized Unit effects"),
        ("event_unit_relations", "Event Unit / transform / combat relations"),
        ("event_spawn_relations", "Event permanent/default spawn relations"),
        ("event_transform_relations", "Event transform relations"),
        ("event_combat_relations", "Event assassin / combat participant relations"),
        ("event_units", "Unique Unit records referenced by Events"),
        ("event_random_references", "Event Negative Monster Number / Montag references"),
        ("unresolved_event_targets", "Unresolved positive Event Unit targets"),
        ("mercenary_companies", "Mercenary companies"),
        ("mercenary_relations", "Mercenary commander / troop relations"),
        ("mercenary_units", "Unique Unit records used by Mercenaries"),
        ("unresolved_mercenary_targets", "Unresolved Mercenary Unit targets"),
    ):
        rows.append(f"| {label} | {stats.get(key, 0)} |")
    return "\n".join(rows)


def write_quality_report(data, out: Path, stats: dict[str, int]) -> Path:
    path = write_generation_quality_report(data, out, stats)
    text = path.read_text(encoding="utf-8")

    anchor = f"| 現在の索引で入手経路未分類 | {stats['unclassified']} |"
    if anchor in text:
        text = text.replace(anchor, anchor + "\n" + _coverage_rows(stats), 1)

    sections = [
        "## Event Random pool references",
        "",
        "Event effectの負値Targetは、単一UnitではなくNegative Monster NumberまたはMontag poolとして保持します。",
        "",
        "| Event ID | Event | Effect | Raw target | Pool | Role |",
        "|---:|---|---|---:|---|---|",
    ]
    if data["event_random_targets"]:
        for relation in sorted(
            data["event_random_targets"],
            key=lambda item: (int(item["event_id"]), str(item["field"]), int(item["raw_target"])),
        ):
            sections.append(
                f"| {relation['event_id']} | {_esc(relation['event'])} | `{_esc(relation['field'])}` | "
                f"{relation['raw_target']} | {_esc(relation['target'])} | {_esc(relation['category'])} |"
            )
    else:
        sections.append("| — | — | — | — | 該当なし | — |")

    sections.extend(
        [
            "",
            "## Unresolved Event Unit targets",
            "",
            "| Event ID | Event | Effect | Raw target |",
            "|---:|---|---|---:|",
        ]
    )
    if data["event_unresolved"]:
        for event_id, event_name, field, raw_target in data["event_unresolved"]:
            sections.append(
                f"| {event_id} | {_esc(event_name)} | `{_esc(field)}` | {raw_target} |"
            )
    else:
        sections.append("| — | — | — | 解決不能参照なし |")

    sections.extend(
        [
            "",
            "## Recognized Event Unit effect fields",
            "",
            "| Effect field | Relations |",
            "|---|---:|",
        ]
    )
    if data["event_field_counts"]:
        for field, count in sorted(data["event_field_counts"].items()):
            sections.append(f"| `{_esc(field)}` | {count} |")
    else:
        sections.append("| — | 0 |")

    sections.extend(
        [
            "",
            "## Unresolved Mercenary Unit targets",
            "",
            "| Mercenary ID | Company | Role | Raw target |",
            "|---:|---|---|---:|",
        ]
    )
    if data["mercenary_unresolved"]:
        for mercenary_id, company, role, raw_target in data["mercenary_unresolved"]:
            sections.append(
                f"| {mercenary_id} | {_esc(company)} | {_esc(role)} | {raw_target} |"
            )
    else:
        sections.append("| — | — | — | 解決不能参照なし |")

    insertion = "\n".join(sections) + "\n\n"
    marker = "## 解釈方針"
    if marker in text:
        text = text.replace(marker, insertion + marker, 1)
    else:
        text += "\n" + insertion

    text = text.replace(
        "`unclassified`は入手不能を意味しない。Unit / Nation生成能力を追加分類した後も、Event、Wish、Random table、hard-coded Reanimation結果、Scenario等の未索引経路を含み得る。",
        "`unclassified`は入手不能を意味しない。EventとMercenaryを追加分類した後も、Wish、Random table、hard-coded Reanimation結果、Adventure、Scenario等の未索引経路を含み得る。",
    )
    path.write_text(text, encoding="utf-8")
    return path
