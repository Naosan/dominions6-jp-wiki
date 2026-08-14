from __future__ import annotations

from collections import defaultdict
from pathlib import Path


def _esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def _item_link(relation: dict[str, object], *, from_unit_page: bool) -> str:
    prefix = "../" if from_unit_page else ""
    return (
        f"[{_esc(relation['item'])}]({prefix}item-unit-sources.md#item-{int(relation['item_id'])})"
    )


def _target_cell(module, relation: dict[str, object], *, sibling: bool = False) -> str:
    target_id = int(relation.get("target_id") or 0)
    target = str(relation.get("target") or "—")
    if target_id > 0:
        return (
            module.sibling_unit_link(target_id, target)
            if sibling
            else module.unit_link(target_id, target)
        )
    return _esc(target)


def _item_unit_table(relations: list[dict[str, object]]) -> str:
    out = [
        "| Item | Relation | Field | Amount | Timing | Owner | Lifetime |",
        "|---|---|---|---|---|---|---|",
    ]
    for relation in sorted(
        relations,
        key=lambda item: (int(item["item_id"]), str(item["field"])),
    ):
        out.append(
            f"| {_item_link(relation, from_unit_page=True)} | "
            f"{_esc(relation['kind'])} / {_esc(relation['category'])} | "
            f"`{_esc(relation['field'])}` | {_esc(relation['amount'])} | "
            f"{_esc(relation['timing'])} | {_esc(relation['owner'])} | "
            f"{_esc(relation['lifetime'])} |"
        )
    return "\n".join(out) + "\n"


def _special_stats(data) -> dict[str, int]:
    return {
        "items_with_unit_relations": int(data["items_with_unit_relations"]),
        "item_unit_relations": len(data["item_relations"]),
        "item_units": len(data["item_incoming"]),
        "item_random_references": len(data["item_random_targets"]),
        "unresolved_item_targets": len(data["item_unresolved"]),
        "spell_random_references": len(data["spell_random_targets"]),
        "special_spell_relations": len(data["spell_special_relations"]),
        "special_unique_pool_entries": len(data["special_unique_pools"]),
        "terrain_pool_entries": len(data["terrain_summon_pools"]),
        "unresolved_special_spell_pools": len(data["special_spell_unresolved"]),
        "arena_items": len(data["arena_items"]),
    }


def _write_item_sources(module, out: Path, data) -> Path:
    lines = [
        "---",
        'title: "Magic ItemによるUnit生成・変身"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        "---",
        "",
        "# Magic ItemによるUnit生成・変身",
        "",
        "Magic Item recordが固定Unit IDを直接参照する召喚、Retinue、Battle summon、変身、Raise、敵対Encounterを整理します。",
        "",
        "| Item | ID | Type | Construction | Forge req | Relation | Field | Target | Amount | Timing | Owner / lifetime | Confidence |",
        "|---|---:|---|---|---|---|---|---|---|---|---|---|",
    ]
    anchored: set[int] = set()
    for relation in sorted(
        data["item_relations"],
        key=lambda item: (int(item["item_id"]), str(item["field"])),
    ):
        item_id = int(relation["item_id"])
        anchor = ""
        if item_id not in anchored:
            anchor = f'<a id="item-{item_id}"></a>'
            anchored.add(item_id)
        target = _target_cell(module, relation)
        owner_lifetime = f"{relation['owner']}; {relation['lifetime']}"
        lines.append(
            f"| {anchor}{_esc(relation['item'])} | {item_id} | {_esc(relation['item_type'])} | "
            f"{_esc(relation['construction'])} | {_esc(relation['forge_path'])} | "
            f"{_esc(relation['kind'])} / {_esc(relation['category'])} | "
            f"`{_esc(relation['field'])}` | {target} | {_esc(relation['amount'])} | "
            f"{_esc(relation['timing'])} | {_esc(owner_lifetime)} | {_esc(relation['confidence'])} |"
        )
    if not data["item_relations"]:
        lines.append("| — | — | — | — | — | 該当Relationなし | — | — | — | — | — | — |")
    lines.extend(
        [
            "",
            "`sumrit / sumauto / sumbat`等は抽出Field名を保持しています。具体的なCommand、使用回数、持続、死亡時処理はItemごとのゲーム内説明を優先します。",
            "",
            "敵対Encounterは出現経路であり、Unitの所有権を得ることを意味しません。",
            "",
            "[Unit総合索引へ戻る](index.md)",
            "",
        ]
    )
    path = out / "item-unit-sources.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _write_item_random(module, out: Path, data) -> Path:
    lines = [
        "---",
        'title: "Item Random summon・未解決Target"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        "---",
        "",
        "# Item Random summon・未解決Target",
        "",
        "Magic ItemのUnit参照がNegative Monster Number、Montag、その他の負値を使う場合、単一Unitへは結び付けません。",
        "",
        "## Random pool / sentinel",
        "",
        "| Item | Field | Raw target | Pool / sentinel | Relation | Amount |",
        "|---|---|---:|---|---|---|",
    ]
    for relation in sorted(
        data["item_random_targets"],
        key=lambda item: (int(item["item_id"]), str(item["field"]), int(item["raw_target"])),
    ):
        lines.append(
            f"| {_item_link(relation, from_unit_page=False)} | `{_esc(relation['field'])}` | "
            f"{relation['raw_target']} | {_esc(relation['target'])} | "
            f"{_esc(relation['category'])} | {_esc(relation['amount'])} |"
        )
    if not data["item_random_targets"]:
        lines.append("| — | — | — | 該当なし | — | — |")

    lines.extend(
        [
            "",
            "## 解決不能な正値Target",
            "",
            "| Item ID | Item | Field | Raw target |",
            "|---:|---|---|---:|",
        ]
    )
    for item_id, item_name, field, raw_target in data["item_unresolved"]:
        lines.append(f"| {item_id} | {_esc(item_name)} | `{_esc(field)}` | {raw_target} |")
    if not data["item_unresolved"]:
        lines.append("| — | — | — | 解決不能参照なし |")
    lines.extend(["", "[Unit索引データ品質](data-quality.md)", ""])
    path = out / "item-random.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _spell_link(relation: dict[str, object]) -> str:
    return (
        f"[{_esc(relation['spell'])}](../spells/by-school/{_esc(relation['school_slug'])}.md)"
    )


def _write_spell_random(out: Path, data) -> Path:
    lines = [
        "---",
        'title: "Spell Random summon pool"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        "---",
        "",
        "# Spell Random summon pool",
        "",
        "通常のSummon effectが負のMonster NumberまたはMontagを参照するSpellを整理します。固定Unit IDではないため、候補集合として表示します。",
        "",
        "| Spell | ID | Research | Req | Type | Effect # | Raw argument | Pool | Availability | Confidence |",
        "|---|---:|---|---|---|---:|---:|---|---|---|",
    ]
    for relation in sorted(
        data["spell_random_targets"],
        key=lambda item: (str(item["school"]), int(item["level"]), str(item["spell"])),
    ):
        lines.append(
            f"| {_spell_link(relation)} | {relation['spell_id']} | {_esc(relation['research'])} | "
            f"{_esc(relation['path'])} | {_esc(relation['type'])} | {relation['effect_number']} | "
            f"{relation['raw_argument']} | {_esc(relation['pool'])} | "
            f"{_esc(relation['availability'])} | {_esc(relation['confidence'])} |"
        )
    if not data["spell_random_targets"]:
        lines.append("| — | — | — | — | — | — | — | 該当なし | — | — |")

    lines.extend(
        [
            "",
            "## なお未解決のSpell summon参照",
            "",
            "| Spell ID | Spell | Effect # | Raw argument |",
            "|---:|---|---:|---:|",
        ]
    )
    for spell_id, spell_name, effect_number, raw_argument in data["unresolved_spells"]:
        lines.append(
            f"| {spell_id} | {_esc(spell_name)} | {effect_number} | {raw_argument} |"
        )
    if not data["unresolved_spells"]:
        lines.append("| — | — | — | 解決不能参照なし |")
    lines.extend(["", "[Spell summon Unit](spell-summons.md)", ""])
    path = out / "spell-random-summons.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _write_special_summons(out: Path, data) -> Path:
    lines = [
        "---",
        'title: "Wish・Unique・Terrain特殊召喚"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        "---",
        "",
        "# Wish・Unique・Terrain特殊召喚",
        "",
        "固定Unit IDではなく、専用pool、terrain rule、procedural table、特殊内部処理を使うSpellを分離します。",
        "",
        "## Spell",
        "",
        "| Spell | ID | Research | Req | Type | Category | Effect # | Raw argument | Pool / mechanism | Table | Availability | Confidence |",
        "|---|---:|---|---|---|---|---:|---:|---|---|---|---|",
    ]
    for relation in sorted(
        data["spell_special_relations"],
        key=lambda item: (str(item["school"]), int(item["level"]), str(item["spell"])),
    ):
        lines.append(
            f"| {_spell_link(relation)} | {relation['spell_id']} | {_esc(relation['research'])} | "
            f"{_esc(relation['path'])} | {_esc(relation['type'])} | {_esc(relation['category'])} | "
            f"{relation['base_effect_number']} | {relation['raw_argument']} | {_esc(relation['pool'])} | "
            f"{_esc(relation['table'])} | {_esc(relation['availability'])} | {_esc(relation['confidence'])} |"
        )
    if not data["spell_special_relations"]:
        lines.append("| — | — | — | — | — | 該当なし | — | — | — | — | — | — |")

    lines.extend(
        [
            "",
            "## Special unique summon table",
            "",
            "| Number | Pool name |",
            "|---:|---|",
        ]
    )
    for number, name in sorted(data["special_unique_pools"].items()):
        lines.append(f"| {number} | {_esc(name)} |")
    if not data["special_unique_pools"]:
        lines.append("| — | 該当なし |")

    lines.extend(
        [
            "",
            "## Terrain-specific summon table",
            "",
            "| Number | Pool name |",
            "|---:|---|",
        ]
    )
    for number, name in sorted(data["terrain_summon_pools"].items()):
        lines.append(f"| {number} | {_esc(name)} |")
    if not data["terrain_summon_pools"]:
        lines.append("| — | 該当なし |")

    lines.extend(
        [
            "",
            "## 解釈上の注意",
            "",
            "- Unique summon tableの番号は候補群の名称であり、単一Unit IDではありません。",
            "- Terrain-specific summonは地形やSpell固有処理によって結果が変わります。",
            "- WishはEffect record上も通常の固定Unit summonではありません。この索引から全Wish結果を逆算しません。",
            "- Cross Breeding、Tartarian Gate等も専用処理を持つため、説明文や名前から固定Unitへ推測で接続しません。",
            "",
            "[Unit総合索引へ戻る](index.md)",
            "",
        ]
    )
    if data["special_spell_unresolved"]:
        lines.extend(
            [
                "## 解決不能な特殊pool番号",
                "",
                "| Spell ID | Spell | Effect # | Raw argument |",
                "|---:|---|---:|---:|",
            ]
        )
        for spell_id, spell_name, effect_number, raw_argument in data["special_spell_unresolved"]:
            lines.append(
                f"| {spell_id} | {_esc(spell_name)} | {effect_number} | {raw_argument} |"
            )
        lines.append("")
    path = out / "special-summons.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _write_arena_items(out: Path, data) -> Path:
    item_out = out.parent / "items"
    item_out.mkdir(parents=True, exist_ok=True)
    lines = [
        "---",
        'title: "Arena関連Magic Item"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        "---",
        "",
        "# Arena関連Magic Item",
        "",
        "BaseIの`arenareward`または`mustfightinarena`を持つItemを整理します。値の詳細な意味と実際のArena進行はゲーム内挙動を優先します。",
        "",
        "| Item | ID | Type | Construction | Forge req | Arena reward | Must fight in Arena |",
        "|---|---:|---|---|---|---:|---:|",
    ]
    for item in sorted(data["arena_items"], key=lambda row: int(row["item_id"])):
        lines.append(
            f"| {_esc(item['item'])} | {item['item_id']} | {_esc(item['item_type'])} | "
            f"{_esc(item['construction'])} | {_esc(item['forge_path'])} | "
            f"{item['arena_reward']} | {item['must_fight']} |"
        )
    if not data["arena_items"]:
        lines.append("| — | — | — | — | — | — | — |")
    lines.extend(
        [
            "",
            "Arena報酬の選出条件、勝者への付与、既存Itemとの重複、Event chainはこのFlag表だけでは決まりません。",
            "",
            "[Magic Itemデータ索引へ戻る](index.md)",
            "",
        ]
    )
    path = item_out / "arena.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _write_pages(module, out: Path, data) -> None:
    _write_item_sources(module, out, data)
    _write_item_random(module, out, data)
    _write_spell_random(out, data)
    _write_special_summons(out, data)
    _write_arena_items(out, data)


def install_special_pages(module, data) -> None:
    original_acquisition_section = module.acquisition_section
    original_source_labels = module.source_labels
    original_write_main_index = module.write_main_index
    original_write_unit_catalog = module.write_unit_catalog

    def acquisition_section(relations: list[dict[str, object]]) -> str:
        base = original_acquisition_section(relations).rstrip()
        item_relations = [
            relation
            for relation in relations
            if str(relation.get("kind", "")).startswith("Item")
        ]
        if not item_relations:
            return base + "\n"
        return (
            base
            + "\n\n### Magic Itemによる生成・変身・出現\n\n"
            + _item_unit_table(item_relations).rstrip()
            + "\n"
        )

    def source_labels(unit_id: int, current_data) -> list[str]:
        labels = original_source_labels(unit_id, current_data)
        if current_data["item_incoming"].get(unit_id) and "Magic Item" not in labels:
            labels.append("Magic Item")
        return labels

    def write_main_index(out: Path, current_data, stats: dict[str, int]):
        stats.update(_special_stats(current_data))
        path = original_write_main_index(out, current_data, stats)
        text = path.read_text(encoding="utf-8")
        anchor = (
            f"- [Mercenary Unit](mercenaries.md) — {stats['mercenary_companies']} companies / "
            f"{stats['mercenary_relations']} relations"
        )
        additions = "\n".join(
            [
                f"- [Magic ItemによるUnit生成・変身](item-unit-sources.md) — {stats['item_unit_relations']} relations",
                f"- [Item Random summon・未解決Target](item-random.md) — {stats['item_random_references']} random references",
                f"- [Spell Random summon pool](spell-random-summons.md) — {stats['spell_random_references']} references",
                f"- [Wish・Unique・Terrain特殊召喚](special-summons.md) — {stats['special_spell_relations']} Spell relations",
            ]
        )
        if anchor in text and "item-unit-sources.md" not in text:
            text = text.replace(anchor, anchor + "\n" + additions, 1)
        text = text.replace(
            "Wish、Random summon table、hard-coded Reanimation結果は、対応を確定できるまで未分類または能力Flagとして残します。",
            "Magic Itemの固定Unit参照とSpellのRandom / special summon poolは索引化済みです。Wishの全結果、hard-coded Reanimation結果等は、対応を確定できるまで専用処理または未分類として残します。",
        )
        path.write_text(text, encoding="utf-8")
        return path

    def write_unit_catalog(current_data, out: Path) -> dict[str, int]:
        stats = original_write_unit_catalog(current_data, out)
        _write_pages(module, out, current_data)
        stats.update(_special_stats(current_data))
        return stats

    module.acquisition_section = acquisition_section
    module.source_labels = source_labels
    module.write_main_index = write_main_index
    module.write_unit_catalog = write_unit_catalog
