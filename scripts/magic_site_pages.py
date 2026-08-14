from __future__ import annotations

from pathlib import Path

from magic_site_data import (
    ECONOMY_FIELDS,
    ENTER_EFFECT_FIELDS,
    FACILITY_FIELDS,
    RESEARCH_FIELDS,
    present,
)
from magic_site_page_common import (
    _has_fields,
    compact_site_table,
    front_matter,
    site_filename,
)
from magic_site_page_detail import site_page
from magic_site_page_indexes import (
    event_page,
    index_page,
    national_page,
    relation_listing_page,
    simple_listing_page,
    terrain_page,
)
from magic_site_page_quality import quality_page


def write_magic_site_catalog(data, out: Path, commit: str) -> dict[str, int]:
    out.mkdir(parents=True, exist_ok=True)
    by_id = out / "by-id"
    by_path = out / "by-path"
    by_id.mkdir(parents=True, exist_ok=True)
    by_path.mkdir(parents=True, exist_ok=True)

    for site in data["sites"]:
        (by_id / site_filename(int(site["id"]))).write_text(
            site_page(site, commit), encoding="utf-8"
        )

    (out / "index.md").write_text(index_page(data, commit), encoding="utf-8")
    (out / "all.md").write_text(
        simple_listing_page(
            "全Magic Site一覧",
            "MagicSites.csvの全recordをID順に掲載します。",
            data["sites"],
            commit,
        ),
        encoding="utf-8",
    )

    actual_paths = sorted({str(site["path"]) for site in data["sites"]})
    for path in actual_paths:
        selected = [site for site in data["sites"] if site["path"] == path]
        slug = selected[0]["path_slug"]
        (by_path / f"{slug}.md").write_text(
            "\n".join(
                front_matter(f"{path} Magic Site", commit)
                + [
                    f"# {path} Magic Site",
                    "",
                    f"Pathが**{path}**のSiteは**{len(selected)}**件です。",
                    "",
                    "[Magic Site総合索引へ戻る](../index.md)",
                    "",
                    compact_site_table(selected, prefix="../by-id").rstrip(),
                    "",
                ]
            ),
            encoding="utf-8",
        )

    gem_sites = [site for site in data["sites"] if site["monthly_gems"] or site["claim_gems"]]
    (out / "gem-income.md").write_text(
        simple_listing_page(
            "Magic Site Gem income",
            "毎月のGem incomeとClaim時Gemを分離して掲載します。",
            gem_sites,
            commit,
        ),
        encoding="utf-8",
    )

    recruit_relations = []
    summon_relations = []
    for site in data["sites"]:
        for relation in site["unit_relations"]:
            if relation["group"] == "Recruit":
                recruit_relations.append((site, relation))
            elif relation["group"] == "Summon":
                summon_relations.append((site, relation))
    (out / "recruitment.md").write_text(
        relation_listing_page(
            "Magic Site Recruit Unit・Commander",
            "Site recordの`mon*` / `com*` / `hmon*` / `hcom*` / `natmon` / `natcom`をUnitへ接続します。",
            recruit_relations,
            commit,
        ),
        encoding="utf-8",
    )
    (out / "summons.md").write_text(
        relation_listing_page(
            "Magic Site Summon",
            "Site recordの`sum1..4`を固定Unitへ接続します。Amountは`n_sum*`に基づくInspector表示上の範囲です。",
            summon_relations,
            commit,
        ),
        encoding="utf-8",
    )

    research_sites = [
        site
        for site in data["sites"]
        if _has_fields(site, RESEARCH_FIELDS)
        or present(site["raw"].get("rit"))
        or present(site["raw"].get("ritrng"))
    ]
    economy_sites = [
        site
        for site in data["sites"]
        if _has_fields(site, ECONOMY_FIELDS + FACILITY_FIELDS)
    ]
    enter_sites = [site for site in data["sites"] if _has_fields(site, ENTER_EFFECT_FIELDS)]
    throne_sites = [site for site in data["sites"] if int(site["rarity"]) >= 11]

    (out / "research.md").write_text(
        simple_listing_page(
            "Magic Site Research・Ritual bonus",
            "Research School bonus、Ritual range、Ritual level modifier、Call God bonus等を持つSiteです。",
            research_sites,
            commit,
        ),
        encoding="utf-8",
    )
    (out / "economy.md").write_text(
        simple_listing_page(
            "Magic Site Economy・Fort・Lab",
            "Gold、Resource、Supply、Unrest、Recruitment Point、Population、Fort、Lab等の抽出値を持つSiteです。",
            economy_sites,
            commit,
        ),
        encoding="utf-8",
    )
    (out / "enter-effects.md").write_text(
        simple_listing_page(
            "Magic Site Enter・Active effect",
            "Experience、Healing、Disease、Curse、Horror Mark、Scry、Adventure、Void Gate等の能動・侵入関連値を持つSiteです。",
            enter_sites,
            commit,
        ),
        encoding="utf-8",
    )
    (out / "thrones.md").write_text(
        simple_listing_page(
            "Throne Magic Site",
            "Inspectorの分類と同様にRarity code 11以上をThroneとして一覧化します。",
            throne_sites,
            commit,
        ),
        encoding="utf-8",
    )
    (out / "national.md").write_text(national_page(data, commit), encoding="utf-8")
    (out / "terrain.md").write_text(terrain_page(data, commit), encoding="utf-8")
    (out / "events.md").write_text(event_page(data, commit), encoding="utf-8")

    stats = dict(data["stats"])
    stats.update(
        {
            "site_pages": len(list(by_id.glob("*.md"))),
            "path_pages": len(list(by_path.glob("*.md"))),
            "generated_site_index_pages": len(list(out.glob("*.md"))),
        }
    )
    (out / "data-quality.md").write_text(
        quality_page(data, stats, commit), encoding="utf-8"
    )
    return stats
