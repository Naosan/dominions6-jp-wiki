from __future__ import annotations

from magic_site_page_common import esc, front_matter


def quality_page(data, stats: dict[str, int], commit: str) -> str:
    lines = front_matter("Magic Site索引データ品質", commit)
    lines.extend(
        [
            "# Magic Site索引データ品質",
            "",
            "## Coverage",
            "",
            "| Metric | Count |",
            "|---|---:|",
        ]
    )
    metrics = (
        ("Site records", "sites"),
        ("Generated Site pages", "site_pages"),
        ("Path pages", "path_pages"),
        ("Monthly gem Sites", "monthly_gem_sites"),
        ("Claim-gem Sites", "claim_gem_sites"),
        ("Nation start Site relations", "start_site_relations"),
        ("Future Site relations", "future_site_relations"),
        ("Site–Unit relations", "site_unit_relations"),
        ("Site recruit relations", "site_recruit_relations"),
        ("Site summon relations", "site_summon_relations"),
        ("Site PD relations", "site_pd_relations"),
        ("Site Event relations", "site_event_relations"),
        ("Thrones", "throne_sites"),
        ("Duplicate Site IDs", "duplicate_site_ids"),
        ("Missing Site names", "missing_site_names"),
        ("Unknown location bitsets", "unknown_location_bits"),
        ("Unclassified non-empty fields", "unclassified_site_values"),
        ("Unresolved Site Unit targets", "unresolved_site_units"),
        ("Unresolved Nation Site targets", "unresolved_nation_sites"),
        ("Unresolved Site Event targets", "unresolved_site_events"),
        ("Unresolved national recruit Nations", "unresolved_national_recruit_nations"),
    )
    for label, key in metrics:
        lines.append(f"| {label} | {stats.get(key, 0)} |")

    lines.extend(["", "## Rarity code distribution", "", "| Rarity | Sites |", "|---:|---:|"])
    for rarity, count in data["rarity_counts"].items():
        lines.append(f"| {rarity} | {count} |")

    lines.extend(["", "## Path distribution", "", "| Path | Sites |", "|---|---:|"])
    for path, count in sorted(data["path_counts"].items()):
        lines.append(f"| {esc(path)} | {count} |")

    lines.extend(["", "## Duplicate names", "", "| Site name | Records |", "|---|---:|"])
    for name, count in data["duplicate_names"].items():
        lines.append(f"| {esc(name)} | {count} |")
    if not data["duplicate_names"]:
        lines.append("| — | 0 |")

    lines.extend(["", "## Unknown location bits", "", "| Site ID | Site | Raw loc | Remaining bits |", "|---:|---|---:|---:|"])
    for site_id, name, raw_loc, remaining in data["unknown_location_bits"]:
        lines.append(f"| {site_id} | {esc(name)} | {raw_loc} | {remaining} |")
    if not data["unknown_location_bits"]:
        lines.append("| — | — | — | 0 |")

    lines.extend(["", "## Unclassified Site fields", "", "| Field | Non-empty values |", "|---|---:|"])
    for field, count in data["unclassified_fields"].items():
        lines.append(f"| `{esc(field)}` | {count} |")
    if not data["unclassified_fields"]:
        lines.append("| — | 0 |")

    lines.extend(["", "## Unresolved Unit targets", "", "| Site ID | Site | Field | Raw target |", "|---:|---|---|---|"])
    for site_id, site_name, field, raw_target in data["unresolved_units"]:
        lines.append(f"| {site_id} | {esc(site_name)} | `{esc(field)}` | {esc(raw_target)} |")
    if not data["unresolved_units"]:
        lines.append("| — | — | — | 解決不能参照なし |")

    lines.extend(["", "## Unresolved Nation Site targets", "", "| Nation ID | Nation | Attribute | Site ID |", "|---:|---|---:|---:|"])
    for nation_id, nation_name, attribute, site_id in data["unresolved_nation_sites"]:
        lines.append(f"| {nation_id} | {esc(nation_name)} | {attribute} | {site_id} |")
    if not data["unresolved_nation_sites"]:
        lines.append("| — | — | — | 解決不能参照なし |")

    lines.extend(["", "## Unresolved Event Site targets", "", "| Event ID | Event | Field | Raw target |", "|---:|---|---|---|"])
    for event_id, event_name, field, raw_target in data["unresolved_events"]:
        lines.append(f"| {event_id} | {esc(event_name)} | `{esc(field)}` | {esc(raw_target)} |")
    if not data["unresolved_events"]:
        lines.append("| — | — | — | 解決不能参照なし |")

    lines.extend(
        [
            "",
            "## 解釈方針",
            "",
            "- Raw Rarityを出現確率へ変換しない。",
            "- `loc = 0`を通常の全Terrain出現と断定しない。",
            "- 正のUnit IDがBaseUへ解決できる場合だけUnitページへ接続する。",
            "- Event説明文のSite名一致は、数値ID参照とConfidenceを分ける。",
            "- 同名Siteは別IDのrecordとして保持する。",
            "- `sum*`、Adventure、Void Gate、National recruit、Throne claim等の最終処理はゲーム内表示を優先する。",
            "",
            "[Magic Site総合索引へ戻る](index.md)",
            "",
        ]
    )
    return "\n".join(lines)
