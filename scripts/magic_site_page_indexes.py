from __future__ import annotations

from magic_site_data import PATH_ORDER
from magic_site_page_common import (
    compact_site_table,
    esc,
    front_matter,
    nation_link,
    short,
    site_link,
    summary_effects,
    unit_link,
)


def index_page(data, commit: str) -> str:
    stats = data["stats"]
    lines = front_matter("Magic Site総合索引", commit)
    lines.extend(
        [
            "# Magic Site総合索引",
            "",
            "Dominions 6.35対応の`MagicSites.csv`を、Path、Level、Rarity、Terrain、Gem income、Recruit、Summon、研究・Ritual bonus、Event relationから参照する索引です。",
            "",
            f"- Site record: **{stats['sites']}**",
            f"- Monthly gem incomeを持つSite: **{stats['monthly_gem_sites']}** / 合計 **{stats['monthly_gem_total']} gems**",
            f"- Claim時Gemを持つSite: **{stats['claim_gem_sites']}** / 合計 **{stats['claim_gem_total']} gems**",
            f"- Site–Unit relation: **{stats['site_unit_relations']}**",
            f"- Nation start / future Site relation: **{stats['start_site_relations']} / {stats['future_site_relations']}**",
            f"- Event relation: **{stats['site_event_relations']}**",
            f"- Throne: **{stats['throne_sites']}**",
            "",
            "## 索引",
            "",
            "- [全Magic Site](all.md)",
            "- [Gem income](gem-income.md)",
            "- [Recruit Unit・Commander](recruitment.md)",
            "- [Site summon](summons.md)",
            "- [Research・Ritual bonus](research.md)",
            "- [Economy・Fort・Lab](economy.md)",
            "- [Enter・Active effect](enter-effects.md)",
            "- [国家開始Site・Future Site](national.md)",
            "- [Terrain・Location](terrain.md)",
            "- [Throne](thrones.md)",
            "- [Site Event relation](events.md)",
            "- [データ品質](data-quality.md)",
            "",
            "## Path別",
            "",
            "| Path | Site数 | 一覧 |",
            "|---|---:|---|",
        ]
    )
    for path_name, code, slug in PATH_ORDER:
        count = data["path_counts"].get(path_name, 0)
        lines.append(f"| {code} — {path_name} | {count} | [{path_name} Site](by-path/{slug}.md) |")
    unknown_paths = [
        (path, count)
        for path, count in sorted(data["path_counts"].items())
        if path not in {name for name, _code, _slug in PATH_ORDER}
    ]
    for path, count in unknown_paths:
        slug = next(site["path_slug"] for site in data["sites"] if site["path"] == path)
        lines.append(f"| {esc(path)} | {count} | [{esc(path)} Site](by-path/{slug}.md) |")
    lines.extend(
        [
            "",
            "## 読み方",
            "",
            "- **Level**はSite searchに関係する抽出Levelです。",
            "- **Rarity**はraw codeであり、そのまま出現確率の百分率ではありません。",
            "- **Terrain**は`loc` bitfieldを`site_terrain_types.csv`で展開します。`Unique`は地形ではなく配置Flagです。",
            "- **Gems when claimed**は通常の毎月Gem incomeと分離します。",
            "- **Recruit / Summon / PD**は正の固定Unit IDだけをUnitページへ接続します。",
            "- **Event relation**はEvent requirementの`site` / `foundsite` / `hiddensite` / `nearbysite`と、effectの`newsite`を対象にします。",
            "",
            "!!! warning \"Site効果の最終確認\"",
            "    Capital placement、Throne claim、Hidden Site、Event chain、Entering Site、Adventure、Void Gate、National recruit、Research bonusの適用条件は複雑です。最終的な表示と挙動はゲーム内Site詳細・実機確認を優先してください。",
            "",
        ]
    )
    return "\n".join(lines)


def simple_listing_page(title: str, intro: str, sites: list[dict[str, object]], commit: str) -> str:
    return "\n".join(
        front_matter(title, commit)
        + [
            f"# {title}",
            "",
            intro,
            "",
            f"該当Site: **{len(sites)}**",
            "",
            "[Magic Site総合索引へ戻る](index.md)",
            "",
            compact_site_table(sites).rstrip(),
            "",
        ]
    )


def relation_listing_page(
    title: str,
    intro: str,
    relations: list[tuple[dict[str, object], dict[str, object]]],
    commit: str,
) -> str:
    lines = front_matter(title, commit)
    lines.extend(
        [
            f"# {title}",
            "",
            intro,
            "",
            f"Relation: **{len(relations)}**",
            "",
            "| Site | Site ID | Relation | Role | Unit | Unit ID | Amount | Field |",
            "|---|---:|---|---|---|---:|---|---|",
        ]
    )
    for site, relation in relations:
        lines.append(
            f"| {site_link(site)} | {site['id']} | {esc(relation['category'])} | "
            f"{esc(relation['role'])} | {unit_link(int(relation['unit_id']), str(relation['unit']))} | "
            f"{relation['unit_id']} | {esc(relation['amount'])} | `{esc(relation['field'])}` |"
        )
    if not relations:
        lines.append("| — | — | 該当Relationなし | — | — | — | — | — |")
    lines.extend(["", "[Magic Site総合索引へ戻る](index.md)", ""])
    return "\n".join(lines)


def national_page(data, commit: str) -> str:
    lines = front_matter("国家開始Site・Future Site", commit)
    lines.extend(
        [
            "# 国家開始Site・Future Site",
            "",
            "`attributes_by_nation.csv`のCapital Site属性とFuture Site属性を、Magic Site recordへ接続します。",
            "",
            "| Nation | Relation | Site | Site ID | Attribute | Gems / effects |",
            "|---|---|---|---:|---:|---|",
        ]
    )
    rows = []
    for site in data["sites"]:
        for relation in site["nation_relations"]:
            rows.append((site, relation))
    for site, relation in sorted(
        rows,
        key=lambda pair: (str(pair[1]["era"]), str(pair[1]["nation"]), str(pair[1]["kind"]), int(pair[0]["id"])),
    ):
        lines.append(
            f"| {nation_link(relation)} | {esc(relation['kind'])} | {site_link(site)} | "
            f"{site['id']} | {relation['attribute']} | {esc(summary_effects(site))} |"
        )
    if not rows:
        lines.append("| — | — | 該当Relationなし | — | — | — |")
    lines.extend(
        [
            "",
            "`Start Site`はInspectorがCapital Siteとして扱う属性25 / 52 / 100、`Future Site`は属性631です。国家内部処理やScenario追加Siteはこの表だけでは確定しません。",
            "",
            "[Magic Site総合索引へ戻る](index.md)",
            "",
        ]
    )
    return "\n".join(lines)


def terrain_page(data, commit: str) -> str:
    lines = front_matter("Magic Site Terrain・Location", commit)
    lines.extend(
        [
            "# Magic Site Terrain・Location",
            "",
            "`loc` bitfieldを`site_terrain_types.csv`で展開します。複数Terrain bitを持つSiteは複数節に現れます。",
            "",
            "| Terrain / flag | Site数 | Bit value |",
            "|---|---:|---:|",
        ]
    )
    for bit, label in data["terrain_lookup"].items():
        lines.append(f"| {esc(label)} | {data['terrain_counts'].get(label, 0)} | {bit} |")
    unspecified = [site for site in data["sites"] if not site["location_labels"]]
    lines.append(f"| Unspecified / special placement | {len(unspecified)} | 0 |")
    lines.append("")

    for bit, label in data["terrain_lookup"].items():
        selected = [site for site in data["sites"] if label in site["location_labels"]]
        lines.extend([f"## {label}", "", compact_site_table(selected).rstrip(), ""])
    lines.extend(
        [
            "## Unspecified / special placement",
            "",
            compact_site_table(unspecified).rstrip(),
            "",
            "`Unique`は通常TerrainではなくSite配置Flagです。`loc = 0`を『すべての地形へ通常出現する』とは解釈していません。",
            "",
            "[Magic Site総合索引へ戻る](index.md)",
            "",
        ]
    )
    return "\n".join(lines)


def event_page(data, commit: str) -> str:
    lines = front_matter("Magic Site Event relation", commit)
    lines.extend(
        [
            "# Magic Site Event relation",
            "",
            "Event requirementがSiteを要求する関係と、Event effectがSiteを生成する関係を整理します。",
            "",
            "| Site | Site ID | Event | Event ID | Relation | Field | Rarity | Description | Confidence |",
            "|---|---:|---|---:|---|---|---:|---|---|",
        ]
    )
    relations = []
    for site in data["sites"]:
        for relation in site["event_relations"]:
            relations.append((site, relation))
    for site, relation in sorted(
        relations,
        key=lambda pair: (int(pair[1]["event_id"]), int(pair[0]["id"]), str(pair[1]["field"])),
    ):
        lines.append(
            f"| {site_link(site)} | {site['id']} | {esc(relation['event'])} | "
            f"{relation['event_id']} | {esc(relation['relation'])} | `{esc(relation['field'])}` | "
            f"{relation['rarity']} | {esc(short(relation['description'], 160) or '—')} | "
            f"{esc(relation['confidence'])} |"
        )
    if not relations:
        lines.append("| — | — | — | — | 該当Relationなし | — | — | — | — |")
    lines.extend(
        [
            "",
            "Description内の`[Site Name]`によるRelationは、明示Site IDより低いConfidenceで表示します。Event chain全体の結果、発生順、所有者、Hidden / Found状態の変化はEvent本文と実機挙動を優先します。",
            "",
            "[Magic Site総合索引へ戻る](index.md)",
            "",
        ]
    )
    return "\n".join(lines)
