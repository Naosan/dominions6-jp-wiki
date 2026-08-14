from __future__ import annotations

from collections import defaultdict

from magic_site_data import FIELD_GROUPS, format_gems, present
from magic_site_page_common import (
    esc,
    event_relations_table,
    field_table,
    front_matter,
    nation_relations_table,
    unit_relations_table,
)


def site_page(site: dict[str, object], commit: str) -> str:
    raw = site["raw"]
    lines = front_matter(str(site["name"]), commit)
    lines.extend(
        [
            f"# {site['name']}",
            "",
            f"Magic Site ID **{site['id']}** の自動生成ページです。抽出値と明示Relationを掲載し、発見確率や最終的なゲーム内挙動を推測で補完しません。",
            "",
            "## 基本情報",
            "",
            "| 項目 | 値 |",
            "|---|---|",
            f"| Site ID | {site['id']} |",
            f"| Path | {esc(site['path'])} |",
            f"| Site level | {site['level']} |",
            f"| Rarity code | {site['rarity']} |",
            f"| Category | {esc(', '.join(site['categories']))} |",
            f"| Location bitfield | {site['location_raw']} |",
            f"| Allowed terrain / flags | {esc(site['location_text'])} |",
            "",
            "Rarityは抽出されたraw codeです。通常Siteの発見率を、その数値だけから直接の百分率へ換算していません。",
            "",
            "## 国家との関係",
            "",
            nation_relations_table(site, from_site_page=True).rstrip(),
            "",
        ]
    )
    if int(site.get("national_recruits_id") or 0) > 0:
        lines.extend(
            [
                f"`nationalrecruits`はNation ID **{site['national_recruits_id']}** を参照します。個別Recruit欄のNation restrictionを確認してください。",
                "",
            ]
        )

    lines.extend(
        [
            "## Gem income",
            "",
            "| Timing | Gems | Total |",
            "|---|---|---:|",
            f"| Monthly / normal income | {format_gems(site['monthly_gems'])} | {sum(site['monthly_gems'].values())} |",
            f"| When claimed | {format_gems(site['claim_gems'])} | {sum(site['claim_gems'].values())} |",
            "",
        ]
    )

    if present(raw.get("rit")) or present(raw.get("ritrng")):
        lines.extend(
            [
                "## Ritual range",
                "",
                "| Path | Range bonus | Source fields |",
                "|---|---|---|",
                f"| {esc(raw.get('rit') or '—')} | {esc(raw.get('ritrng') or '—')} | `rit`, `ritrng` |",
                "",
            ]
        )

    for _key, title, fields in FIELD_GROUPS:
        lines.extend([f"## {title}", "", field_table(site, fields).rstrip(), ""])

    relations_by_group: dict[str, list[dict[str, object]]] = defaultdict(list)
    for relation in site["unit_relations"]:
        relations_by_group[str(relation["group"])].append(relation)
    lines.extend(
        [
            "## Recruit・Summon・Province Defence",
            "",
        ]
    )
    for group in ("Recruit", "Summon", "Province Defence"):
        lines.extend(
            [
                f"### {group}",
                "",
                unit_relations_table(
                    relations_by_group.get(group, []), from_site_page=True
                ).rstrip(),
                "",
            ]
        )

    lines.extend(
        [
            "## Event relation",
            "",
            event_relations_table(site).rstrip(),
            "",
            "## 解釈上の注意",
            "",
            "- `mon*` / `com*` / `hmon*` / `hcom*`はSite recordの明示Unit参照です。国家・地形・Fort・形態による実際のRecruit可否はゲーム内表示を優先します。",
            "- `sum*`のAmountはInspector表示と同様に、`n_sum*`が1より大きい場合を`1–N`として保持します。確率分布はこの表だけでは確定しません。",
            "- EventのSite名一致は、説明文中の`[Site Name]`を使う場合があります。数値ID参照より信頼度を一段下げて表示します。",
            "- Gem、Research bonus、Scale、Province bonusはSiteが存在・発見・Claimされた時点や所有状態によって適用条件が異なる場合があります。",
            "",
            "[Magic Site総合索引へ戻る](../index.md)",
            "",
        ]
    )
    return "\n".join(lines)
