from __future__ import annotations

from pathlib import Path


def _site_link(module, site_id: int, name: str, *, from_unit_page: bool) -> str:
    prefix = "../../sites/by-id" if from_unit_page else "../sites/by-id"
    return f"[{module.esc(name)}]({prefix}/{site_id:04d}.md)"


def install_site_links(module) -> None:
    def site_table(relations: list[dict[str, object]]) -> str:
        out = [
            "| Magic Site | ID | Path | Source slot | Role | Count hint |",
            "|---|---:|---|---|---|---:|",
        ]
        for relation in sorted(
            relations,
            key=lambda item: (
                str(item["path"]),
                str(item["site"]),
                str(item["field"]),
            ),
        ):
            site_id = int(relation["site_id"])
            out.append(
                f"| {_site_link(module, site_id, str(relation['site']), from_unit_page=True)} | "
                f"{site_id} | {module.esc(relation['path'])} | "
                f"{module.esc(relation['source'])} (`{relation['field']}`) | "
                f"{relation['role']} | {relation['count_hint']} |"
            )
        return "\n".join(out) + "\n"

    def write_magic_sites(out: Path, data) -> Path:
        lines = [
            "---",
            'title: "Magic Site Unit索引"',
            "status: generated",
            'verified_version: "6.35"',
            "---",
            "",
            "# Magic Site Unit索引",
            "",
            "MagicSites.csvの`mon/com/hmon/hcom/sum/natmon/natcom`列からUnit参照を抽出します。列名を保った事実索引であり、発見条件や国家制限の全挙動はゲーム内Site詳細を優先します。",
            "",
            "- [Magic Site総合索引](../sites/index.md)",
            "- [Magic Site Recruit](../sites/recruitment.md)",
            "- [Magic Site Summon](../sites/summons.md)",
            "",
            "| Path | Site | ID | Source slot | Role | Count hint | Unit | Unit ID |",
            "|---|---|---:|---|---|---:|---|---:|",
        ]
        relations = module.flatten_relations(data["sites"])
        for unit_id, relation in sorted(
            relations,
            key=lambda item: (
                str(item[1]["path"]),
                str(item[1]["site"]),
                str(item[1]["field"]),
                item[0],
            ),
        ):
            row = data["units"][unit_id]
            site_id = int(relation["site_id"])
            lines.append(
                f"| {module.esc(relation['path'])} | "
                f"{_site_link(module, site_id, str(relation['site']), from_unit_page=False)} | "
                f"{site_id} | {module.esc(relation['source'])} (`{relation['field']}`) | "
                f"{relation['role']} | {relation['count_hint']} | "
                f"{module.unit_link(unit_id, row.get('name') or '(unnamed)')} | {unit_id} |"
            )
        path = out / "magic-sites.md"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return path

    module.site_table = site_table
    module.write_magic_sites = write_magic_sites
