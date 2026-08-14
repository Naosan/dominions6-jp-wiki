from __future__ import annotations

from pathlib import Path


def write_quality_report(data, out: Path, stats: dict[str, int]) -> Path:
    lines = [
        "---",
        'title: "Unit索引データ品質"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        "---",
        "",
        "# Unit索引データ品質",
        "",
        "自動生成で採用した関係数と、固定Unit IDへ解決できなかった参照を記録します。未解決は推測で補完しません。",
        "",
        "## Coverage",
        "",
        "| 項目 | 件数 |",
        "|---|---:|",
    ]
    for key, label in (
        ("units", "BaseU Unit records"),
        ("unit_pages", "Generated Unit pages"),
        ("acquired_units", "確認済み直接入手経路を持つUnit"),
        ("recruit_relations", "Recruit relations"),
        ("hero_relations", "Hero relations"),
        ("pretender_relations", "Pretender relations"),
        ("spell_relations", "Fixed Spell summon relations"),
        ("site_relations", "Magic Site Unit relations"),
        ("mount_relations", "Rider–Mount relations"),
        ("shape_relations", "Direct Shape relations"),
        ("related_only", "Mount / Shapeとしてのみ確認"),
        ("unclassified", "現在の索引で入手経路未分類"),
    ):
        lines.append(f"| {label} | {stats[key]} |")

    lines.extend(
        [
            "",
            "## Unresolved Spell summon references",
            "",
            "固定Unit IDへ解決できなかったSummon effectです。負値pool、特殊effect、内部sentinel等の可能性があるためUnitへ結び付けません。",
            "",
            "| Root Spell ID | Spell | Effect | Raw argument |",
            "|---:|---|---:|---:|",
        ]
    )
    if data["unresolved_spells"]:
        for spell_id, spell, effect, raw in data["unresolved_spells"]:
            lines.append(f"| {spell_id} | {str(spell).replace('|', '\\|')} | {effect} | {raw} |")
    else:
        lines.append("| — | 解決不能参照なし | — | — |")

    lines.extend(
        [
            "",
            "## Unresolved Magic Site Unit references",
            "",
            "| Site ID | Site | Field | Raw argument |",
            "|---:|---|---|---:|",
        ]
    )
    if data["unresolved_sites"]:
        for site_id, site, field, raw in data["unresolved_sites"]:
            lines.append(f"| {site_id} | {str(site).replace('|', '\\|')} | `{field}` | {raw} |")
    else:
        lines.append("| — | 解決不能参照なし | — | — |")

    lines.extend(
        [
            "",
            "## Unresolved Shape references",
            "",
            "| Source ID | Source | Field | Target ID |",
            "|---:|---|---|---:|",
        ]
    )
    if data["unresolved_shapes"]:
        for source_id, source, field, target_id in data["unresolved_shapes"]:
            lines.append(f"| {source_id} | {str(source).replace('|', '\\|')} | `{field}` | {target_id} |")
    else:
        lines.append("| — | 解決不能参照なし | — | — |")

    lines.extend(
        [
            "",
            "## 解釈方針",
            "",
            "- 未解決参照を名前から推測してUnitへ結び付けない。",
            "- `unclassified`は入手不能を意味しない。Event、Freespawn、Random pool、Wish、Transformation等の未索引経路を含み得る。",
            "- Patch更新時は件数差だけでなく、未解決参照の増減とID変更を確認する。",
            "- 最終的な入手条件と挙動はゲーム内表示・実機テストを優先する。",
            "",
            "[Unit総合索引へ戻る](index.md)",
            "",
        ]
    )
    path = out / "data-quality.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path
