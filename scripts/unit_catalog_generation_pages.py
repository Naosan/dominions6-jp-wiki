from __future__ import annotations

from collections import defaultdict
from pathlib import Path


BASE_ACQUISITION_KINDS = {"Recruit", "Hero", "Pretender", "Spell", "Magic Site"}
UNIT_GENERATION_KINDS = {
    "Strategic Spawn",
    "Battle Spawn",
    "Recruit Unlock",
    "Slave Capture",
    "Conversion",
}
RELATION_PAGE_CONFIG = (
    (
        "strategic-spawns.md",
        "Strategic summon・Freespawn",
        {"Strategic Spawn", "Slave Capture"},
        "Unit自身のDominion召喚、毎月自動召喚、Temple summon、special order、scale条件召喚、slave captureを整理します。",
    ),
    (
        "battle-spawns.md",
        "Battle summon",
        {"Battle Spawn"},
        "戦闘開始時または各Combat roundにUnit自身が生成する召喚を整理します。",
    ),
    (
        "recruit-unlocks.md",
        "Unit条件Recruit",
        {"Recruit Unlock"},
        "`ownsmonrec`と`monpresentrec`によって解禁されるRecruit関係を整理します。",
    ),
    (
        "conversions.md",
        "変換・復活・Raise関係",
        {"Conversion"},
        "Mummification、Twiceborn、Lich化、Animate、Raise等の固定Unit変換先を整理します。",
    ),
)


def _esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def _unit_link(module, unit_id: int, name: str, *, sibling: bool = False) -> str:
    if sibling:
        return module.sibling_unit_link(unit_id, name)
    return module.unit_link(unit_id, name)


def _target_cell(module, relation: dict[str, object], *, sibling: bool = False) -> str:
    target_id = int(relation.get("target_id") or 0)
    target = str(relation.get("target") or "—")
    if target_id > 0:
        return _unit_link(module, target_id, target, sibling=sibling)
    return _esc(target)


def _unit_generation_table(module, relations: list[dict[str, object]], *, incoming: bool) -> str:
    if not relations:
        return ""
    if incoming:
        out = [
            "| Source Unit | Relation | Field | Timing | Amount | Condition | Confidence |",
            "|---|---|---|---|---|---|---|",
        ]
        for relation in sorted(
            relations,
            key=lambda item: (
                str(item.get("kind", "")),
                str(item.get("source", "")),
                str(item.get("field", "")),
            ),
        ):
            source_id = int(relation["source_id"])
            source = module.sibling_unit_link(source_id, str(relation["source"]))
            out.append(
                f"| {source} | {_esc(relation['kind'])} / {_esc(relation['category'])} | "
                f"`{_esc(relation['field'])}` | {_esc(relation['timing'])} | "
                f"{_esc(relation['amount'])} | {_esc(relation.get('condition') or '—')} | "
                f"{_esc(relation['confidence'])} |"
            )
        return "\n".join(out) + "\n"

    out = [
        "| Relation | Field | Target / pool | Timing | Amount | Condition | Confidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for relation in sorted(
        relations,
        key=lambda item: (
            str(item.get("kind", "")),
            str(item.get("field", "")),
            int(item.get("raw_target") or 0),
        ),
    ):
        out.append(
            f"| {_esc(relation['kind'])} / {_esc(relation['category'])} | "
            f"`{_esc(relation['field'])}` | {_target_cell(module, relation, sibling=True)} | "
            f"{_esc(relation['timing'])} | {_esc(relation['amount'])} | "
            f"{_esc(relation.get('condition') or '—')} | {_esc(relation['confidence'])} |"
        )
    return "\n".join(out) + "\n"


def _nation_spawn_table(module, relations: list[dict[str, object]]) -> str:
    out = [
        "| Nation | Command | Category | Description | Raw / target |",
        "|---|---|---|---|---|",
    ]
    for relation in sorted(
        relations,
        key=lambda item: (str(item["era"]), str(item["nation"]), str(item["command"])),
    ):
        nation = module.nation_link(relation)
        target_id = int(relation.get("target_id") or 0)
        if target_id:
            target = module.sibling_unit_link(target_id, str(relation["target"]))
        else:
            target = _esc(relation.get("raw_value") or "—")
        out.append(
            f"| {nation} | `#{_esc(relation['command'])}` | {_esc(relation['category'])} | "
            f"{_esc(relation['description'])} | {target} |"
        )
    return "\n".join(out) + "\n"


def _ability_table(abilities: list[dict[str, object]]) -> str:
    out = [
        "| Category | Ability | Field | Value | Meaning |",
        "|---|---|---|---:|---|",
    ]
    for ability in sorted(
        abilities,
        key=lambda item: (str(item["category"]), str(item["label"]), str(item["field"])),
    ):
        out.append(
            f"| {_esc(ability['category'])} | {_esc(ability['label'])} | "
            f"`{_esc(ability['field'])}` | {ability['value']} | {_esc(ability['description'])} |"
        )
    return "\n".join(out) + "\n"


def _producer_section(module, unit_id: int, data) -> str:
    outgoing = data["unit_generation_outgoing"].get(unit_id, [])
    abilities = data["unit_generation_abilities"].get(unit_id, [])
    if not outgoing and not abilities:
        return ""
    lines = ["## 生成・召喚・変換能力", ""]
    if outgoing:
        lines.extend(
            [
                "### 固定Target / Random pool参照",
                "",
                _unit_generation_table(module, outgoing, incoming=False),
                "",
            ]
        )
    if abilities:
        lines.extend(["### Targetを直接指定しない能力", "", _ability_table(abilities), ""])
    lines.extend(
        [
            "負のTargetは公式Negative Monster NumberまたはMontag poolです。特定Unit IDへは結び付けません。",
            "",
        ]
    )
    return "\n".join(lines)


def _incoming_generation_section(module, relations: list[dict[str, object]]) -> str:
    unit_relations = [relation for relation in relations if relation["kind"] in UNIT_GENERATION_KINDS]
    nation_relations = [relation for relation in relations if relation["kind"] == "Nation Spawn"]
    if not unit_relations and not nation_relations:
        return ""
    lines = ["### Unit / Nation能力による入手・変換", ""]
    if unit_relations:
        lines.extend([_unit_generation_table(module, unit_relations, incoming=True), ""])
    if nation_relations:
        lines.extend([_nation_spawn_table(module, nation_relations), ""])
    return "\n".join(lines)


def _generation_stats(data) -> dict[str, int]:
    outgoing = [
        relation
        for relations in data["unit_generation_outgoing"].values()
        for relation in relations
    ]
    abilities = [
        ability
        for values in data["unit_generation_abilities"].values()
        for ability in values
    ]
    counts = defaultdict(int)
    for relation in outgoing:
        counts[str(relation["kind"])] += 1
    return {
        "unit_generation_sources": len(data["unit_generation_outgoing"]),
        "unit_generation_relations": len(outgoing),
        "strategic_spawn_relations": counts["Strategic Spawn"] + counts["Slave Capture"],
        "battle_spawn_relations": counts["Battle Spawn"],
        "recruit_unlock_relations": counts["Recruit Unlock"],
        "conversion_relations": counts["Conversion"],
        "random_spawn_references": len(data["unit_generation_random_targets"]),
        "unresolved_unit_generation": len(data["unit_generation_unresolved"]),
        "generation_ability_units": len(data["unit_generation_abilities"]),
        "generation_abilities": len(abilities),
        "nation_generation_abilities": len(data["nation_generation"]),
        "nation_spawn_relations": sum(
            len(values) for values in data["nation_generation_incoming"].values()
        ),
    }


def _write_relation_page(
    module,
    out: Path,
    data,
    filename: str,
    title: str,
    kinds: set[str],
    description: str,
) -> Path:
    selected = [
        relation
        for values in data["unit_generation_outgoing"].values()
        for relation in values
        if relation["kind"] in kinds
    ]
    lines = [
        "---",
        f'title: "{title}"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        "---",
        "",
        f"# {title}",
        "",
        description,
        "",
        "| Source Unit | Source ID | Relation | Field | Target / pool | Timing | Amount | Condition | Confidence |",
        "|---|---:|---|---|---|---|---|---|---|",
    ]
    for relation in sorted(
        selected,
        key=lambda item: (
            str(item["kind"]),
            str(item["category"]),
            str(item["source"]),
            str(item["field"]),
        ),
    ):
        source = module.unit_link(int(relation["source_id"]), str(relation["source"]))
        target = _target_cell(module, relation)
        lines.append(
            f"| {source} | {relation['source_id']} | {_esc(relation['kind'])} / "
            f"{_esc(relation['category'])} | `{_esc(relation['field'])}` | {target} | "
            f"{_esc(relation['timing'])} | {_esc(relation['amount'])} | "
            f"{_esc(relation.get('condition') or '—')} | {_esc(relation['confidence'])} |"
        )
    if not selected:
        lines.append("| — | — | 該当Relationなし | — | — | — | — | — | — |")
    lines.extend(
        [
            "",
            "負値Targetは特定Unitではなく、Negative Monster NumberまたはMontag poolを示します。",
            "",
            "[Unit総合索引へ戻る](index.md)",
            "",
        ]
    )
    path = out / filename
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _write_random_targets(module, out: Path, data) -> Path:
    selected = list(data["unit_generation_random_targets"])
    unresolved = list(data["unit_generation_unresolved"])
    lines = [
        "---",
        'title: "Random summon・未解決Target"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        "---",
        "",
        "# Random summon・未解決Target",
        "",
        "負のMonster NumberとMontag poolは、単一の固定Unit IDとして扱いません。",
        "",
        "## Negative Monster Number / Montag",
        "",
        "| Source Unit | Relation | Field | Raw target | Pool | Timing | Amount |",
        "|---|---|---|---:|---|---|---|",
    ]
    for relation in sorted(
        selected,
        key=lambda item: (str(item["source"]), str(item["field"]), int(item["raw_target"])),
    ):
        source = module.unit_link(int(relation["source_id"]), str(relation["source"]))
        lines.append(
            f"| {source} | {_esc(relation['kind'])} | `{_esc(relation['field'])}` | "
            f"{relation['raw_target']} | {_esc(relation['target'])} | "
            f"{_esc(relation['timing'])} | {_esc(relation['amount'])} |"
        )
    if not selected:
        lines.append("| — | — | — | — | 該当なし | — | — |")

    lines.extend(
        [
            "",
            "## 解決不能な正値Target",
            "",
            "| Source ID | Source Unit | Field | Raw target | Relation |",
            "|---:|---|---|---:|---|",
        ]
    )
    for source_id, source_name, field, raw_target, kind in unresolved:
        lines.append(
            f"| {source_id} | {module.unit_link(source_id, source_name)} | "
            f"`{_esc(field)}` | {raw_target} | {_esc(kind)} |"
        )
    if not unresolved:
        lines.append("| — | — | — | — | 解決不能参照なし |")
    lines.extend(["", "[Unit索引データ品質](data-quality.md)", ""])
    path = out / "random-summons.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _write_reanimation(module, out: Path, data) -> Path:
    unit_rows = [
        (unit_id, ability)
        for unit_id, abilities in data["unit_generation_abilities"].items()
        for ability in abilities
    ]
    nation_rows = [
        relation
        for relation in data["nation_generation"]
        if relation["category"] in {"Reanimation", "Dominion Freespawn"}
    ]
    lines = [
        "---",
        'title: "Reanimation・Freespawn・召喚Bonus"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        "---",
        "",
        "# Reanimation・Freespawn・召喚Bonus",
        "",
        "固定Unit Targetを直接指定しないUnit能力と、国家単位のReanimation / Dominion Freespawnを整理します。",
        "",
        "## Unit能力",
        "",
        "| Unit | ID | Category | Ability | Field | Value | Meaning |",
        "|---|---:|---|---|---|---:|---|",
    ]
    for unit_id, ability in sorted(
        unit_rows,
        key=lambda item: (
            str(item[1]["category"]),
            str(data["units"][item[0]].get("name") or ""),
            str(item[1]["field"]),
        ),
    ):
        row = data["units"][unit_id]
        lines.append(
            f"| {module.unit_link(unit_id, row.get('name') or '(unnamed)')} | {unit_id} | "
            f"{_esc(ability['category'])} | {_esc(ability['label'])} | "
            f"`{_esc(ability['field'])}` | {ability['value']} | "
            f"{_esc(ability['description'])} |"
        )
    if not unit_rows:
        lines.append("| — | — | — | 該当能力なし | — | — | — |")

    lines.extend(
        [
            "",
            "## 国家能力",
            "",
            "| Era | Nation | Command | Category | Description | Raw value |",
            "|---|---|---|---|---|---:|",
        ]
    )
    for relation in sorted(
        nation_rows,
        key=lambda item: (str(item["era"]), str(item["nation"]), str(item["command"])),
    ):
        nation = (
            f"[{relation['era']} {_esc(relation['nation'])}]"
            f"(../../nations/{relation['directory']}/{relation['slug']}.md)"
        )
        lines.append(
            f"| {relation['era']} | {nation} | `#{_esc(relation['command'])}` | "
            f"{_esc(relation['category'])} | {_esc(relation['description'])} | "
            f"{relation['raw_value']} |"
        )
    if not nation_rows:
        lines.append("| — | — | — | — | 該当国家能力なし | — |")
    lines.extend(
        [
            "",
            "Reanimationの具体的な生成Unitは国家・Priest level・corpse・hard-coded nation ruleで変わるため、能力Flagから固定Unitへ推測しません。",
            "",
            "[Unit総合索引へ戻る](index.md)",
            "",
        ]
    )
    path = out / "reanimation.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _write_nation_generation(module, out: Path, data) -> Path:
    lines = [
        "---",
        'title: "国家Freespawn・Reanimation能力"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        "---",
        "",
        "# 国家Freespawn・Reanimation能力",
        "",
        "`attributes_by_nation.csv`と`attribute_keys.csv`の明示Command対応から生成します。",
        "",
        "| Era | Nation | Command | Category | Description | Raw / target | Confidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for relation in sorted(
        data["nation_generation"],
        key=lambda item: (str(item["era"]), str(item["nation"]), str(item["command"])),
    ):
        nation = (
            f"[{relation['era']} {_esc(relation['nation'])}]"
            f"(../../nations/{relation['directory']}/{relation['slug']}.md)"
        )
        target_id = int(relation.get("target_id") or 0)
        target = (
            module.unit_link(target_id, str(relation["target"]))
            if target_id
            else _esc(relation.get("target") if relation.get("target") != "—" else relation["raw_value"])
        )
        lines.append(
            f"| {relation['era']} | {nation} | `#{_esc(relation['command'])}` | "
            f"{_esc(relation['category'])} | {_esc(relation['description'])} | "
            f"{target} | {_esc(relation['confidence'])} |"
        )
    if not data["nation_generation"]:
        lines.append("| — | — | — | — | 該当能力なし | — | — |")
    lines.extend(
        [
            "",
            "Guardian Spiritが負値の場合はMontag / random poolであり、固定Unitへは結び付けません。`autoundead`やReanimation flagも、hard-codedな生成先を推測しません。",
            "",
            "[Unit総合索引へ戻る](index.md)",
            "",
        ]
    )
    path = out / "nation-generation.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _write_generation_pages(module, out: Path, data) -> list[Path]:
    paths = [
        _write_relation_page(module, out, data, filename, title, kinds, description)
        for filename, title, kinds, description in RELATION_PAGE_CONFIG
    ]
    paths.append(_write_random_targets(module, out, data))
    paths.append(_write_reanimation(module, out, data))
    paths.append(_write_nation_generation(module, out, data))
    return paths


def install_generation_pages(module, data) -> None:
    original_acquisition_section = module.acquisition_section
    original_relation_section = module.relation_section
    original_source_labels = module.source_labels
    original_write_unit_catalog = module.write_unit_catalog

    def acquisition_section(relations: list[dict[str, object]]) -> str:
        base = [relation for relation in relations if relation["kind"] in BASE_ACQUISITION_KINDS]
        extra = [relation for relation in relations if relation["kind"] not in BASE_ACQUISITION_KINDS]
        if base:
            text = original_acquisition_section(base).rstrip()
        else:
            text = "## 確認済みの入手・利用経路\n"
        addition = _incoming_generation_section(module, extra)
        if addition:
            text += "\n\n" + addition.rstrip()
        if not base and not addition:
            text += (
                "\n現在の索引ソースでは、固定Unit IDへ解決できる直接入手経路を確認できません。"
                "Source側の生成能力やMount・Shape関係は次節に表示します。"
            )
        return text + "\n"

    def relation_section(unit_id: int, current_data) -> str:
        base = original_relation_section(unit_id, current_data).rstrip()
        producer = _producer_section(module, unit_id, current_data).rstrip()
        return base + ("\n\n" + producer if producer else "") + "\n"

    def source_labels(unit_id: int, current_data) -> list[str]:
        labels = original_source_labels(unit_id, current_data)
        if current_data["unit_generation_outgoing"].get(unit_id) and "Producer" not in labels:
            labels.append("Producer")
        if current_data["unit_generation_abilities"].get(unit_id) and "Generation Ability" not in labels:
            labels.append("Generation Ability")
        return labels

    def write_unclassified(out: Path, current_data):
        related_only: list[int] = []
        unclassified: list[int] = []
        for unit_id in sorted(current_data["units"]):
            if current_data["acquisitions"].get(unit_id):
                continue
            related = (
                current_data["riders_by_mount"].get(unit_id)
                or current_data["shape_outgoing"].get(unit_id)
                or current_data["shape_incoming"].get(unit_id)
                or current_data["unit_generation_outgoing"].get(unit_id)
                or current_data["unit_generation_abilities"].get(unit_id)
            )
            if related:
                related_only.append(unit_id)
            else:
                unclassified.append(unit_id)

        lines = [
            "---",
            'title: "入手経路未分類Unit"',
            "status: generated",
            'verified_version: "6.35"',
            "---",
            "",
            "# 入手経路未分類Unit",
            "",
            "通常Recruit、Hero、Pretender、固定Spell summon、Magic Site、Unit生成能力、Nation Guardian Spiritのいずれにも固定入手先として対応付かなかったrecordです。",
            "",
            f"## 関係・生成能力のみ確認（{len(related_only)}）",
            "",
            "| ID | Unit | Role | Related source |",
            "|---:|---|---|---|",
        ]
        for unit_id in related_only:
            row = current_data["units"][unit_id]
            lines.append(
                f"| {unit_id} | {module.unit_link(unit_id, row.get('name') or '(unnamed)')} | "
                f"{module.unit_role(row)} | {_esc(', '.join(module.source_labels(unit_id, current_data)))} |"
            )
        lines.extend(
            [
                "",
                f"## 現在の索引では関係未確認（{len(unclassified)}）",
                "",
                "| ID | Unit | Role | Tags |",
                "|---:|---|---|---|",
            ]
        )
        for unit_id in unclassified:
            row = current_data["units"][unit_id]
            lines.append(
                f"| {unit_id} | {module.unit_link(unit_id, row.get('name') or '(unnamed)')} | "
                f"{module.unit_role(row)} | {_esc(', '.join(module.all_tags(row)[:8]) or '—')} |"
            )
        path = out / "unclassified.md"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return path, len(related_only), len(unclassified)

    def write_main_index(out: Path, current_data, stats: dict[str, int]):
        stats.update(_generation_stats(current_data))
        path = out / "index.md"
        path.write_text(
            f"""---
title: "Unit総合索引"
status: generated
verified_version: "6.35"
generated_from: "dom6inspector {current_data['commit']}"
---

# Unit総合索引

BaseUの全 **{stats['units']}** recordを個別ページ化し、確認済みの入手経路、Unit生成能力、Nation能力、Mount、Shapeを結合します。

## カテゴリ

- [全Unit一覧](all/index.md)
- [Pretender chassis](pretenders.md) — {stats['pretender_relations']} nation–chassis relations
- [Hero](heroes.md) — {stats['hero_relations']} nation–hero relations
- [Spell summon](spell-summons.md) — {stats['spell_relations']} fixed summon relations
- [Magic Site Unit](magic-sites.md) — {stats['site_relations']} site–unit relations
- [Strategic summon・Freespawn](strategic-spawns.md) — {stats['strategic_spawn_relations']} relations
- [Battle summon](battle-spawns.md) — {stats['battle_spawn_relations']} relations
- [Unit条件Recruit](recruit-unlocks.md) — {stats['recruit_unlock_relations']} relations
- [変換・復活・Raise](conversions.md) — {stats['conversion_relations']} relations
- [Reanimation・Freespawn・召喚Bonus](reanimation.md) — {stats['generation_abilities']} Unit abilities
- [国家Freespawn・Reanimation](nation-generation.md) — {stats['nation_generation_abilities']} nation abilities
- [Random summon・未解決Target](random-summons.md) — {stats['random_spawn_references']} random references
- [Mount](mounts.md) — {stats['mount_units']} unique Mount records
- [Shape relation](shapes.md) — {stats['shape_relations']} direct / derived shape links
- [入手経路未分類](unclassified.md) — {stats['unclassified']} no confirmed indexed source

## 「確認済み」に採用する参照

1. 国家Recruit mapping
2. 国家属性`hero1..6` / `multihero1..2`
3. `pretender_types_by_nation.csv`
4. Research可能Spellの固定Unit summon effect
5. MagicSites.csvのUnit参照
6. BaseUのMonster Summoning / Recruit unlock / fixed conversion field
7. Nation attribute keyが明示するGuardian Spirit・Freespawn・Reanimation command
8. BaseUのMount・Shape参照

負のMonster NumberとMontagはRandom poolであり、特定Unitへは結び付けません。Event、Wish、Random summon table、hard-coded Reanimation結果は、対応を確定できるまで未分類または能力Flagとして残します。

## 読み方

```text
Unit page
├ 基本能力
├ Magic Path
├ Weapon / Armor / Mount
├ Recruit / Hero / Pretender / Spell / Site
├ Unit・Nation能力からの生成元
├ Unit自身の召喚・変換・Reanimation能力
└ Shape・Mount reverse relation
```

- [国家Recruitデータ](../recruitment/index.md)
- [Unit装備・Mountの読み方](../unit-loadouts.md)
- [装備使用者逆引き](../equipment-usage/index.md)
- [Spellデータ](../spells/index.md)
- [Combat data](../combat/index.md)

!!! warning "未分類の意味"
    未分類Unitは入手不能と断定できません。現在の固定データ源から安全に対応付けできなかったrecordです。
""",
            encoding="utf-8",
        )
        return path

    def write_unit_catalog(current_data, out: Path) -> dict[str, int]:
        stats = original_write_unit_catalog(current_data, out)
        _write_generation_pages(module, out, current_data)
        stats.update(_generation_stats(current_data))
        return stats

    module.acquisition_section = acquisition_section
    module.relation_section = relation_section
    module.source_labels = source_labels
    module.write_unclassified = write_unclassified
    module.write_main_index = write_main_index
    module.write_unit_catalog = write_unit_catalog
