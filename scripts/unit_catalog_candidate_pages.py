from __future__ import annotations

from pathlib import Path


def _esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def _candidate_stats(data) -> dict[str, int]:
    unique_candidates = {
        unit_id
        for values in data["special_unique_pool_units"].values()
        for unit_id in values
    }
    terrain_candidates = {
        unit_id
        for values in data["terrain_summon_pool_units"].values()
        for unit_id in values
    }
    named_candidates = {
        unit_id
        for values in data["explicit_named_summon_pools"].values()
        for unit_id in values
    }
    return {
        "spell_candidate_relations": len(data["spell_candidate_relations"]),
        "special_candidate_units": len(data["spell_candidate_incoming"]),
        "unresolved_special_candidates": len(data["special_candidate_unresolved"]),
        "unique_pool_candidates": len(unique_candidates),
        "terrain_pool_candidates": len(terrain_candidates),
        "named_pool_candidates": len(named_candidates),
    }


def _unit_links(module, unit_ids: list[int], data) -> str:
    links: list[str] = []
    for unit_id in unit_ids:
        row = data["units"].get(unit_id)
        if not row:
            links.append(f"Unresolved Unit {unit_id}")
            continue
        links.append(module.unit_link(unit_id, row.get("name") or f"Unit {unit_id}"))
    return ", ".join(links) or "—"


def _spell_link(relation: dict[str, object]) -> str:
    name = _esc(relation["spell"])
    slug = _esc(relation["school_slug"])
    return f"[{name}](../spells/by-school/{slug}.md)"


def _write_special_summons(module, out: Path, data) -> Path:
    lines = [
        "---",
        'title: "Wish・Unique・Terrain特殊召喚"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        'candidate_source: "scripts/DMI/SpellTables.js"',
        "---",
        "",
        "# Wish・Unique・Terrain特殊召喚",
        "",
        "通常の固定Unit summonとは異なり、専用pool、terrain rule、procedural table、または特殊内部処理を使うSpellを整理します。",
        "",
        "候補Unitは、固定スナップショットのDom6 InspectorがSpell表示に使用する`SpellTables.js`の明示配列だけを採用します。説明文やUnit名の類似から推測していません。",
        "",
        "## Spell",
        "",
        "| Spell | ID | Research | Req | Type | Category | Effect # | Raw | Pool / mechanism | Candidate Units | Availability | Confidence |",
        "|---|---:|---|---|---|---|---:|---:|---|---|---|---|",
    ]
    for relation in sorted(
        data["spell_special_relations"],
        key=lambda item: (
            str(item["school"]),
            int(item["level"]),
            str(item["spell"]),
            int(item["effect_spell_id"]),
        ),
    ):
        candidates = _unit_links(module, list(relation.get("candidates") or []), data)
        lines.append(
            f"| {_spell_link(relation)} | {relation['spell_id']} | {_esc(relation['research'])} | "
            f"{_esc(relation['path'])} | {_esc(relation['type'])} | {_esc(relation['category'])} | "
            f"{relation['base_effect_number']} | {relation['raw_argument']} | {_esc(relation['pool'])} | "
            f"{candidates} | {_esc(relation['availability'])} | {_esc(relation['confidence'])} |"
        )
    if not data["spell_special_relations"]:
        lines.append("| — | — | — | — | — | 該当なし | — | — | — | — | — | — |")

    lines.extend(
        [
            "",
            "## Special unique summon table",
            "",
            "| Number | Pool name | Candidate Units |",
            "|---:|---|---|",
        ]
    )
    all_unique_keys = sorted(
        set(data["special_unique_pools"]) | set(data["special_unique_pool_units"])
    )
    for number in all_unique_keys:
        name = data["special_unique_pools"].get(number) or f"Unique summon pool {number}"
        candidates = _unit_links(
            module,
            list(data["special_unique_pool_units"].get(number, [])),
            data,
        )
        lines.append(f"| {number} | {_esc(name)} | {candidates} |")
    if not all_unique_keys:
        lines.append("| — | 該当なし | — |")

    lines.extend(
        [
            "",
            "## Terrain-specific summon table",
            "",
            "| Number | Pool name | Candidate Units |",
            "|---:|---|---|",
        ]
    )
    all_terrain_keys = sorted(
        set(data["terrain_summon_pools"]) | set(data["terrain_summon_pool_units"])
    )
    for number in all_terrain_keys:
        name = data["terrain_summon_pools"].get(number) or f"Terrain summon pool {number}"
        candidates = _unit_links(
            module,
            list(data["terrain_summon_pool_units"].get(number, [])),
            data,
        )
        lines.append(f"| {number} | {_esc(name)} | {candidates} |")
    if not all_terrain_keys:
        lines.append("| — | 該当なし | — |")

    lines.extend(
        [
            "",
            "## SpellTablesの明示候補集合",
            "",
            "Unique / Terrain table以外に、Inspectorが名前付き配列として明示している候補集合です。",
            "",
            "| Pool | Candidate Units |",
            "|---|---|",
        ]
    )
    for name, unit_ids in sorted(data["explicit_named_summon_pools"].items()):
        lines.append(f"| {_esc(name)} | {_unit_links(module, list(unit_ids), data)} |")
    if not data["explicit_named_summon_pools"]:
        lines.append("| 該当なし | — |")

    lines.extend(
        [
            "",
            "## 解釈上の注意",
            "",
            "- **Candidate Units**は候補集合であり、1回のCastで全員を得るという意味ではありません。",
            "- Unique summonは既に召喚済みのUnique、死亡状態、Spell固有条件によって結果が変わり得ます。",
            "- Terrain-specific summonは地形やSpell固有処理によって結果が変わります。",
            "- Wishは通常の固定Unit summon effectではありません。この索引からWishの全入力結果を逆算しません。",
            "- Cross Breeding、Summon Animals、Infernal Breeding等はprocedural処理として残し、単一Unitへ接続しません。",
            "- `SpellTables.js`はInspectorの表示ロジックです。最終的なゲーム挙動はゲーム内表示と実機テストを優先します。",
            "",
            "[Spell summon Unit](spell-summons.md)",
            "",
            "[Spell Random summon pool](spell-random-summons.md)",
            "",
            "[Unit総合索引へ戻る](index.md)",
            "",
        ]
    )

    if data["special_spell_unresolved"] or data["special_candidate_unresolved"]:
        lines.extend(
            [
                "## 解決不能参照",
                "",
                "| Spell ID | Spell | Effect # | Raw / candidate Unit | Type |",
                "|---:|---|---:|---:|---|",
            ]
        )
        for spell_id, spell_name, effect_number, raw_argument in data["special_spell_unresolved"]:
            lines.append(
                f"| {spell_id} | {_esc(spell_name)} | {effect_number} | {raw_argument} | pool |"
            )
        for spell_id, spell_name, effect_number, unit_id in data["special_candidate_unresolved"]:
            lines.append(
                f"| {spell_id} | {_esc(spell_name)} | {effect_number} | {unit_id} | candidate Unit |"
            )
        lines.append("")

    path = out / "special-summons.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def install_candidate_pages(module, data) -> None:
    original_write_main_index = module.write_main_index
    original_write_unit_catalog = module.write_unit_catalog

    def write_main_index(out: Path, current_data, stats: dict[str, int]):
        stats.update(_candidate_stats(current_data))
        path = original_write_main_index(out, current_data, stats)
        text = path.read_text(encoding="utf-8")
        old = (
            f"- [Wish・Unique・Terrain特殊召喚](special-summons.md) — "
            f"{stats['special_spell_relations']} Spell relations"
        )
        new = (
            f"- [Wish・Unique・Terrain特殊召喚](special-summons.md) — "
            f"{stats['special_spell_relations']} Spell relations / "
            f"{stats['spell_candidate_relations']} candidate links"
        )
        if old in text:
            text = text.replace(old, new, 1)
        path.write_text(text, encoding="utf-8")
        return path

    def write_unit_catalog(current_data, out: Path) -> dict[str, int]:
        stats = original_write_unit_catalog(current_data, out)
        _write_special_summons(module, out, current_data)
        stats.update(_candidate_stats(current_data))
        return stats

    module.write_main_index = write_main_index
    module.write_unit_catalog = write_unit_catalog
