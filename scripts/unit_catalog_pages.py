from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from generate_recruitment_data import fixed_text, num, random_text, yes
from recruitment_loadouts import (
    armor_summary,
    equipment_profile,
    grouped_summaries,
    mount_summary,
    unit_armor_ids,
    unit_weapon_ids,
    weapon_summary,
)

UNIT_TAG_FIELDS = (
    ("holy", "Sacred"),
    ("undead", "Undead"),
    ("demon", "Demon"),
    ("magicbeing", "Magic Being"),
    ("inanimate", "Lifeless"),
    ("stonebeing", "Stone Being"),
    ("animal", "Animal"),
    ("female", "Female"),
    ("mounted", "Mounted"),
    ("flying", "Flying"),
    ("float", "Floating"),
    ("aquatic", "Aquatic"),
    ("amphibian", "Amphibious"),
    ("pooramphibian", "Poor Amphibian"),
    ("immobile", "Immobile"),
    ("spy", "Spy"),
    ("assassin", "Assassin"),
    ("immortal", "Immortal"),
    ("domimmortal", "Dominion Immortal"),
    ("noheal", "Cannot Heal"),
    ("neednoteat", "Need Not Eat"),
    ("undisciplined", "Undisciplined"),
    ("slave", "Slave"),
    ("ethereal", "Ethereal"),
    ("trample", "Trample"),
    ("stormimmune", "Storm Immune"),
    ("spiritsight", "Spirit Sight"),
    ("truesight", "True Sight"),
    ("blind", "Blind"),
    ("plant", "Plant"),
    ("glamour", "Glamour"),
    ("mindvessel", "Mind Vessel"),
    ("stunimmunity", "Stun Immune"),
    ("petrificationimmune", "Petrification Immune"),
)

VALUED_TAG_FIELDS = (
    ("stealthy", "Stealth"),
    ("heal", "Healer"),
    ("formationfighter", "Formation Fighter"),
    ("bodyguard", "Bodyguard"),
    ("standard", "Standard"),
    ("inspirational", "Inspirational"),
    ("taskmaster", "Taskmaster"),
    ("beastmaster", "Beastmaster"),
    ("awe", "Awe"),
    ("fear", "Fear"),
    ("berserk", "Berserker"),
    ("regeneration", "Regeneration"),
    ("reinvigoration", "Reinvigoration"),
    ("darkvision", "Darkvision"),
    ("fireres", "Fire Resistance"),
    ("coldres", "Cold Resistance"),
    ("shockres", "Shock Resistance"),
    ("poisonres", "Poison Resistance"),
    ("acidres", "Acid Resistance"),
    ("patrolbonus", "Patrol Bonus"),
    ("siegebonus", "Siege Bonus"),
    ("castledef", "Castle Defence"),
    ("supplybonus", "Supply Bonus"),
    ("forgebonus", "Forge Bonus"),
    ("douse", "Blood Search"),
    ("researchbonus", "Research Bonus"),
)


def esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def yaml_string(value: object) -> str:
    return json.dumps(str(value), ensure_ascii=False)


def unit_filename(unit_id: int) -> str:
    return f"{unit_id:04d}.md"


def unit_link(unit_id: int, name: str, prefix: str = "by-id") -> str:
    return f"[{esc(name)}]({prefix}/{unit_filename(unit_id)})"


def sibling_unit_link(unit_id: int, name: str) -> str:
    return f"[{esc(name)}]({unit_filename(unit_id)})"


def unit_role(row: dict[str, str]) -> str:
    magic = fixed_text(row) != "—" or random_text(row) != "—"
    commander = any(num(row, key) for key in ("leader", "undeadleader", "magicleader"))
    if magic and commander:
        return "Mage Commander"
    if magic:
        return "Mage"
    if commander or num(row, "holy"):
        return "Commander"
    return "Troop"


def all_tags(row: dict[str, str]) -> list[str]:
    out = [label for key, label in UNIT_TAG_FIELDS if yes(row, key)]
    if num(row, "mor") == 50 and "Mindless" not in out:
        out.append("Mindless")
    for key, label in VALUED_TAG_FIELDS:
        value = num(row, key)
        if value:
            out.append(f"{label} {value:+d}")
    if num(row, "rt") == 2:
        out.append("Slow to recruit")
    if yes(row, "latehero"):
        out.append("Late Hero")
    if yes(row, "unique"):
        out.append("Unique")
    return out


def stats_table(row: dict[str, str]) -> str:
    fields = (
        ("Role", unit_role(row)),
        ("Size", row.get("size") or "—"),
        ("HP", row.get("hp") or "—"),
        ("Protection", row.get("prot") or "—"),
        ("Magic Resistance", row.get("mr") or "—"),
        ("Morale", row.get("mor") or "—"),
        ("Strength", row.get("str") or "—"),
        ("Attack Skill", row.get("att") or "—"),
        ("Defence Skill", row.get("def") or "—"),
        ("Precision", row.get("prec") or "—"),
        ("Encumbrance", row.get("enc") or "—"),
        ("Map Move", row.get("mapmove") or "—"),
        ("Action Points", row.get("ap") or "—"),
        ("Leadership N/U/M", f"{row.get('leader') or '—'}/{row.get('undeadleader') or '—'}/{row.get('magicleader') or '—'}"),
        ("Start / Max age", f"{row.get('startage') or '—'} / {row.get('maxage') or '—'}"),
    )
    out = ["| 項目 | 値 |", "|---|---|"]
    out.extend(f"| {label} | {esc(value)} |" for label, value in fields)
    return "\n".join(out) + "\n"


def magic_section(row: dict[str, str]) -> str:
    guaranteed = fixed_text(row)
    random = random_text(row)
    if guaranteed == "—" and random == "—" and not num(row, "researchbonus"):
        return "## Magic\n\n固定Path・Random Path・Research Bonusは確認されていません。\n"
    return f"""## Magic

| 項目 | 内容 |
|---|---|
| Guaranteed | {esc(guaranteed)} |
| Random | {esc(random)} |
| Research Bonus | {num(row, 'researchbonus') or '—'} |
| Forge Bonus | {num(row, 'forgebonus') or '—'} |
| Blood Search Bonus | {num(row, 'douse') or '—'} |

Random表記はRecruitデータと同じ形式です。実際に得られる組み合わせはRandom groupごとに判定されます。
"""


def equipment_section(row, units, weapons, armors) -> str:
    weapon_lines = grouped_summaries(
        unit_weapon_ids(row), weapons, weapon_summary, "Unknown weapon"
    )
    armor_lines = grouped_summaries(
        unit_armor_ids(row), armors, armor_summary, "Unknown armor"
    )
    profile = equipment_profile(row, weapons, armors)
    lines = ["## 装備・Mount", ""]
    lines.append("### Weapons")
    lines.append("")
    lines.extend(f"- {line}" for line in weapon_lines)
    if not weapon_lines:
        lines.append("- 装備Weaponなし")
    lines.extend(["", "### Armor", ""])
    lines.extend(f"- {line}" for line in armor_lines)
    if not armor_lines:
        lines.append("- 装備Armorなし")
    lines.extend(["", "### Mount", "", mount_summary(row, units, weapons, armors)])
    lines.extend(["", "### Equipment profile", "", ", ".join(profile) or "—", ""])
    lines.append(
        "Weapon・Armor欄はrecord単体の値です。最終Damage、Natural Protection、Bless、Buff、二刀流処理、形態変化は別途考慮します。"
    )
    return "\n".join(lines) + "\n"


def nation_link(relation: dict[str, object]) -> str:
    return f"[{relation['era']} {esc(relation['nation'])}](../../../nations/{relation['directory']}/{relation['slug']}.md)"


def recruit_table(relations: list[dict[str, object]]) -> str:
    out = [
        "| Nation | Role | Source | Capital-only | Data |",
        "|---|---|---|---|---|",
    ]
    for relation in sorted(relations, key=lambda item: (str(item["era"]), str(item["nation"]), str(item["source"]))):
        data_link = f"[Recruit](../../recruitment/{relation['directory']}/{relation['slug']}.md)"
        out.append(
            f"| {nation_link(relation)} | {relation['role']} | {esc(relation['source'])} | "
            f"{'Yes' if relation['capital_only'] else 'No'} | {data_link} |"
        )
    return "\n".join(out) + "\n"


def hero_table(relations: list[dict[str, object]]) -> str:
    out = ["| Nation | Type | Slot |", "|---|---|---|"]
    for relation in sorted(relations, key=lambda item: (str(item["era"]), str(item["nation"]), str(item["slot"]))):
        out.append(
            f"| {nation_link(relation)} | {relation['hero_type']} | `{relation['slot']}` |"
        )
    return "\n".join(out) + "\n"


def pretender_table(relations: list[dict[str, object]]) -> str:
    out = ["| Nation | Nation ID |", "|---|---:|"]
    for relation in sorted(relations, key=lambda item: (str(item["era"]), str(item["nation"]))):
        out.append(f"| {nation_link(relation)} | {relation['nation_id']} |")
    return "\n".join(out) + "\n"


def spell_table(relations: list[dict[str, object]]) -> str:
    out = [
        "| Spell | ID | Research | Req | Type | Effect | Count hint | Availability |",
        "|---|---:|---|---|---|---|---:|---|",
    ]
    for relation in sorted(relations, key=lambda item: (str(item["school"]), int(item["level"]), str(item["spell"]))):
        spell_link = f"[{esc(relation['spell'])}](../../spells/by-school/{relation['school_slug']}.md)"
        out.append(
            f"| {spell_link} | {relation['spell_id']} | {esc(relation['research'])} | "
            f"{relation['path']} | {relation['type']} | {esc(relation['effect'])} | "
            f"{relation['count_hint']} | {esc(relation['availability'])} |"
        )
    return "\n".join(out) + "\n"


def site_table(relations: list[dict[str, object]]) -> str:
    out = [
        "| Magic Site | ID | Path | Source slot | Role | Count hint |",
        "|---|---:|---|---|---|---:|",
    ]
    for relation in sorted(relations, key=lambda item: (str(item["path"]), str(item["site"]), str(item["field"]))):
        out.append(
            f"| {esc(relation['site'])} | {relation['site_id']} | {esc(relation['path'])} | "
            f"{esc(relation['source'])} (`{relation['field']}`) | {relation['role']} | {relation['count_hint']} |"
        )
    return "\n".join(out) + "\n"


def acquisition_section(relations: list[dict[str, object]]) -> str:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for relation in relations:
        grouped[str(relation["kind"])].append(relation)
    lines = ["## 確認済みの入手・利用経路", ""]
    if not grouped:
        lines.append(
            "現在の索引ソースでは、通常Recruit・Hero・Pretender・Spell・Magic Siteからの直接入手経路を確認できません。MountやShapeとしてのみ参照される場合は次節に表示します。"
        )
        return "\n".join(lines) + "\n"
    renderers = (
        ("Recruit", "通常Recruit", recruit_table),
        ("Hero", "Hero", hero_table),
        ("Pretender", "Pretender chassis", pretender_table),
        ("Spell", "Spell summon", spell_table),
        ("Magic Site", "Magic Site", site_table),
    )
    for key, title, renderer in renderers:
        if grouped.get(key):
            lines.extend([f"### {title}", "", renderer(grouped[key])])
    return "\n".join(lines).rstrip() + "\n"


def relation_section(unit_id: int, data) -> str:
    units = data["units"]
    outgoing = data["shape_outgoing"].get(unit_id, [])
    incoming = data["shape_incoming"].get(unit_id, [])
    riders = data["riders_by_mount"].get(unit_id, [])
    lines = ["## Unit間の関係", ""]
    if riders:
        lines.extend(["### Mountとして使用", ""])
        for rider in sorted(riders, key=lambda item: (str(item["rider"]), int(item["rider_id"]))):
            lines.append(f"- {sibling_unit_link(int(rider['rider_id']), str(rider['rider']))}")
        lines.append("")
    if outgoing:
        lines.extend(["### このUnitから変化するShape", ""])
        for relation in sorted(outgoing, key=lambda item: (str(item["label"]), int(item["target_id"]))):
            lines.append(
                f"- **{relation['label']}** (`{relation['field']}`) → "
                f"{sibling_unit_link(int(relation['target_id']), str(relation['target']))}"
            )
        lines.append("")
    if incoming:
        lines.extend(["### このUnitへ変化するShape", ""])
        for relation in sorted(incoming, key=lambda item: (str(item["label"]), int(item["source_id"]))):
            lines.append(
                f"- {sibling_unit_link(int(relation['source_id']), str(relation['source']))} "
                f"→ **{relation['label']}** (`{relation['field']}`)"
            )
        lines.append("")
    if not riders and not outgoing and not incoming:
        lines.append("現在のBaseU直接参照では、MountまたはShape関係を確認できません。")
    return "\n".join(lines) + "\n"


def source_labels(unit_id: int, data) -> list[str]:
    labels: list[str] = []
    for relation in data["acquisitions"].get(unit_id, []):
        label = str(relation["kind"])
        if label not in labels:
            labels.append(label)
    if data["riders_by_mount"].get(unit_id):
        labels.append("Mount")
    if data["shape_outgoing"].get(unit_id) or data["shape_incoming"].get(unit_id):
        labels.append("Shape")
    return labels


def unit_page(unit_id: int, row: dict[str, str], data) -> str:
    name = row.get("name") or "(unnamed)"
    tags = all_tags(row)
    sources = source_labels(unit_id, data)
    front = f"""---
title: {yaml_string(f'{name} #{unit_id}')}
status: generated
verified_version: "6.35"
unit_id: {unit_id}
generated_from: {yaml_string('dom6inspector ' + data['commit'])}
---

# {esc(name)} — Unit #{unit_id}

[Unit総合索引へ戻る](../index.md) · [全Unit一覧](../all/index.md) · [Unit装備・Mountの読み方](../../unit-loadouts.md)

!!! info "自動生成Unit record"
    BaseU recordと確認済みの取得関係を結合した参照ページです。最終Cost、AI評価、実戦Tier、全Shape処理を自動採点するものではありません。

## 分類

| 項目 | 内容 |
|---|---|
| Role | {unit_role(row)} |
| Tags | {esc(', '.join(tags) or '—')} |
| Indexed sources | {esc(', '.join(sources) or '未確認')} |

## 基本能力

{stats_table(row)}
"""
    return (
        front
        + "\n"
        + magic_section(row)
        + "\n"
        + equipment_section(row, data["units"], data["weapons"], data["armors"])
        + "\n"
        + acquisition_section(data["acquisitions"].get(unit_id, []))
        + "\n"
        + relation_section(unit_id, data)
        + f"""
## データ上の注意

- Unit recordの`Prot`と、Armor recordのBody / Head / Shield Protectionは別の表示です。
- Spell summonのCount hintはeffect chain上の値で、Caster level、特殊条件、確率選択を完全には再現しません。
- Magic Siteの`hmon` / `hcom` / `sum`等は抽出列名を保った分類です。実際の出現・Recruit条件はゲーム内Site詳細を優先します。
- Hero、Pretender、Spell、Siteが同じUnitを共有する場合、複数経路をすべて表示します。
- Shape relationはBaseUの直接参照のみです。イベント、Battle開始時変身、一時効果の全挙動を保証しません。

## 出典

- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- Data snapshot: `{data['commit']}`（Dominions 6.35）
"""
    )


def unit_overview_row(unit_id: int, row: dict[str, str], data, prefix: str = "../by-id") -> str:
    magic = fixed_text(row)
    if random_text(row) != "—":
        magic += ("; " if magic != "—" else "") + random_text(row)
    return (
        f"| {unit_id} | {unit_link(unit_id, row.get('name') or '(unnamed)', prefix)} | "
        f"{unit_role(row)} | {row.get('size') or '—'} | {row.get('hp') or '—'} | "
        f"{row.get('prot') or '—'} | {row.get('mr') or '—'} | {esc(magic)} | "
        f"{esc(', '.join(source_labels(unit_id, data)) or '—')} |"
    )


def write_all_indexes(out: Path, data) -> list[Path]:
    all_dir = out / "all"
    all_dir.mkdir(parents=True, exist_ok=True)
    unit_ids = sorted(data["units"])
    chunks: dict[int, list[int]] = defaultdict(list)
    for unit_id in unit_ids:
        chunks[(unit_id // 1000) * 1000].append(unit_id)
    written: list[Path] = []
    links: list[str] = []
    for start, ids in sorted(chunks.items()):
        end = start + 999
        filename = f"{start:04d}-{end:04d}.md"
        links.append(f"- [{start}–{end}]({filename}) — {len(ids)} records")
        lines = [
            "---",
            f"title: {yaml_string(f'Unit {start}–{end}')}",
            "status: generated",
            'verified_version: "6.35"',
            "---",
            "",
            f"# Unit {start}–{end}",
            "",
            "| ID | Unit | Role | Size | HP | Prot | MR | Magic | Indexed sources |",
            "|---:|---|---|---:|---:|---:|---:|---|---|",
        ]
        for unit_id in ids:
            lines.append(unit_overview_row(unit_id, data["units"][unit_id], data))
        path = all_dir / filename
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        written.append(path)
    index = all_dir / "index.md"
    index.write_text(
        "---\ntitle: \"全Unit一覧\"\nstatus: generated\nverified_version: \"6.35\"\n---\n\n"
        "# 全Unit一覧\n\nBaseUの全Unit recordをID帯ごとに分割しています。\n\n"
        + "\n".join(links)
        + "\n",
        encoding="utf-8",
    )
    written.append(index)
    return written


def flatten_relations(source_map) -> list[tuple[int, dict[str, object]]]:
    return [
        (unit_id, relation)
        for unit_id, relations in source_map.items()
        for relation in relations
    ]


def write_pretenders(out: Path, data) -> Path:
    lines = [
        "---",
        'title: "Pretender chassis索引"',
        "status: generated",
        'verified_version: "6.35"',
        "---",
        "",
        "# Pretender chassis索引",
        "",
        "国家ごとの選択可能Chassisを`pretender_types_by_nation.csv`から逆引きします。",
        "",
    ]
    relations = flatten_relations(data["pretenders"])
    for era in ("EA", "MA", "LA"):
        rows = [(unit_id, relation) for unit_id, relation in relations if relation["era"] == era]
        lines.extend([
            f"## {era}",
            "",
            "| Nation | Chassis | ID | Role | Tags |",
            "|---|---|---:|---|---|",
        ])
        for unit_id, relation in sorted(rows, key=lambda item: (str(item[1]["nation"]), data["units"][item[0]].get("name") or "")):
            row = data["units"][unit_id]
            nation = f"[{era} {esc(relation['nation'])}](../../nations/{relation['directory']}/{relation['slug']}.md)"
            lines.append(
                f"| {nation} | {unit_link(unit_id, row.get('name') or '(unnamed)')} | {unit_id} | "
                f"{unit_role(row)} | {esc(', '.join(all_tags(row)[:8]) or '—')} |"
            )
        lines.append("")
    path = out / "pretenders.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_heroes(out: Path, data) -> Path:
    lines = [
        "---",
        'title: "Hero索引"',
        "status: generated",
        'verified_version: "6.35"',
        "---",
        "",
        "# Hero索引",
        "",
        "国家属性`hero1..hero6`および`multihero1..2`から生成します。",
        "",
    ]
    relations = flatten_relations(data["heroes"])
    for era in ("EA", "MA", "LA"):
        rows = [(unit_id, relation) for unit_id, relation in relations if relation["era"] == era]
        lines.extend([
            f"## {era}",
            "",
            "| Nation | Hero | ID | Type | Slot | Magic |",
            "|---|---|---:|---|---|---|",
        ])
        for unit_id, relation in sorted(rows, key=lambda item: (str(item[1]["nation"]), str(item[1]["slot"]))):
            row = data["units"][unit_id]
            nation = f"[{era} {esc(relation['nation'])}](../../nations/{relation['directory']}/{relation['slug']}.md)"
            magic = fixed_text(row)
            if random_text(row) != "—":
                magic += ("; " if magic != "—" else "") + random_text(row)
            lines.append(
                f"| {nation} | {unit_link(unit_id, row.get('name') or '(unnamed)')} | {unit_id} | "
                f"{relation['hero_type']} | `{relation['slot']}` | {esc(magic)} |"
            )
        lines.append("")
    path = out / "heroes.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_spell_summons(out: Path, data) -> Path:
    lines = [
        "---",
        'title: "Spell summon索引"',
        "status: generated",
        'verified_version: "6.35"',
        "---",
        "",
        "# Spell summon索引",
        "",
        "Research可能Spellのeffect chainから、固定Unit IDを参照する確認済みSummon効果を抽出します。Random poolや負値参照は固定Unitとして掲載しません。",
        "",
        "| Spell | ID | Research | Req | Type | Effect | Count hint | Summoned Unit | Unit ID | Availability |",
        "|---|---:|---|---|---|---|---:|---|---:|---|",
    ]
    relations = flatten_relations(data["spell_summons"])
    for unit_id, relation in sorted(relations, key=lambda item: (str(item[1]["school"]), int(item[1]["level"]), str(item[1]["spell"]), item[0])):
        row = data["units"][unit_id]
        spell = f"[{esc(relation['spell'])}](../spells/by-school/{relation['school_slug']}.md)"
        lines.append(
            f"| {spell} | {relation['spell_id']} | {esc(relation['research'])} | {relation['path']} | "
            f"{relation['type']} | {esc(relation['effect'])} | {relation['count_hint']} | "
            f"{unit_link(unit_id, row.get('name') or '(unnamed)')} | {unit_id} | {esc(relation['availability'])} |"
        )
    path = out / "spell-summons.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


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
        "| Path | Site | ID | Source slot | Role | Count hint | Unit | Unit ID |",
        "|---|---|---:|---|---|---:|---|---:|",
    ]
    relations = flatten_relations(data["sites"])
    for unit_id, relation in sorted(relations, key=lambda item: (str(item[1]["path"]), str(item[1]["site"]), str(item[1]["field"]), item[0])):
        row = data["units"][unit_id]
        lines.append(
            f"| {esc(relation['path'])} | {esc(relation['site'])} | {relation['site_id']} | "
            f"{esc(relation['source'])} (`{relation['field']}`) | {relation['role']} | {relation['count_hint']} | "
            f"{unit_link(unit_id, row.get('name') or '(unnamed)')} | {unit_id} |"
        )
    path = out / "magic-sites.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_mounts(out: Path, data) -> Path:
    lines = [
        "---",
        'title: "Mount Unit索引"',
        "status: generated",
        'verified_version: "6.35"',
        "---",
        "",
        "# Mount Unit索引",
        "",
        "BaseUの`mountmnr`から逆引きしたMount recordです。Riderとは別のHP、Protection、攻撃、防具を持ちます。",
        "",
        "| Mount | ID | Size | HP | Prot | Def | Riders | Rider examples |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for mount_id, riders in sorted(data["riders_by_mount"].items(), key=lambda item: (data["units"][item[0]].get("name") or "", item[0])):
        row = data["units"][mount_id]
        examples = ", ".join(
            unit_link(int(rider["rider_id"]), str(rider["rider"]))
            for rider in sorted(riders, key=lambda value: (str(value["rider"]), int(value["rider_id"])))[:8]
        )
        if len(riders) > 8:
            examples += f" ほか{len(riders) - 8}"
        lines.append(
            f"| {unit_link(mount_id, row.get('name') or '(unnamed)')} | {mount_id} | {row.get('size') or '—'} | "
            f"{row.get('hp') or '—'} | {row.get('prot') or '—'} | {row.get('def') or '—'} | {len(riders)} | {examples} |"
        )
    path = out / "mounts.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_shapes(out: Path, data) -> Path:
    lines = [
        "---",
        'title: "Shape relation索引"',
        "status: generated",
        'verified_version: "6.35"',
        "---",
        "",
        "# Shape relation索引",
        "",
        "BaseUの直接Shape参照を一覧化します。一時変身、イベント変身、Battle effectの全処理を再構成するものではありません。",
        "",
        "| Relation | Field | Source | Source ID | Target | Target ID |",
        "|---|---|---|---:|---|---:|",
    ]
    relations = [relation for values in data["shape_outgoing"].values() for relation in values]
    for relation in sorted(relations, key=lambda item: (str(item["label"]), int(item["source_id"]), int(item["target_id"]))):
        lines.append(
            f"| {relation['label']} | `{relation['field']}` | "
            f"{unit_link(int(relation['source_id']), str(relation['source']))} | {relation['source_id']} | "
            f"{unit_link(int(relation['target_id']), str(relation['target']))} | {relation['target_id']} |"
        )
    path = out / "shapes.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_unclassified(out: Path, data) -> tuple[Path, int, int]:
    related_only: list[int] = []
    unclassified: list[int] = []
    for unit_id in sorted(data["units"]):
        if data["acquisitions"].get(unit_id):
            continue
        if data["riders_by_mount"].get(unit_id) or data["shape_outgoing"].get(unit_id) or data["shape_incoming"].get(unit_id):
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
        "通常Recruit、Hero、Pretender、固定Spell summon、Magic Site Unitのいずれにも対応付かなかったrecordです。未分類は『ゲーム内で入手不能』を意味しません。Event、Freespawn、特殊召喚、内部effect、Transformation等が未索引の場合があります。",
        "",
        f"## Mount・Shapeとしてのみ確認（{len(related_only)}）",
        "",
        "| ID | Unit | Role | Related source |",
        "|---:|---|---|---|",
    ]
    for unit_id in related_only:
        row = data["units"][unit_id]
        lines.append(
            f"| {unit_id} | {unit_link(unit_id, row.get('name') or '(unnamed)')} | {unit_role(row)} | "
            f"{esc(', '.join(source_labels(unit_id, data)))} |"
        )
    lines.extend([
        "",
        f"## 現在の索引では関係未確認（{len(unclassified)}）",
        "",
        "| ID | Unit | Role | Tags |",
        "|---:|---|---|---|",
    ])
    for unit_id in unclassified:
        row = data["units"][unit_id]
        lines.append(
            f"| {unit_id} | {unit_link(unit_id, row.get('name') or '(unnamed)')} | {unit_role(row)} | "
            f"{esc(', '.join(all_tags(row)[:8]) or '—')} |"
        )
    path = out / "unclassified.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path, len(related_only), len(unclassified)


def write_main_index(out: Path, data, stats: dict[str, int]) -> Path:
    path = out / "index.md"
    path.write_text(
        f"""---
title: "Unit総合索引"
status: generated
verified_version: "6.35"
generated_from: "dom6inspector {data['commit']}"
---

# Unit総合索引

BaseUの全 **{stats['units']}** recordを個別ページ化し、確認済みの入手経路とUnit間関係を結合します。

## カテゴリ

- [全Unit一覧](all/index.md)
- [Pretender chassis](pretenders.md) — {stats['pretender_relations']} nation–chassis relations
- [Hero](heroes.md) — {stats['hero_relations']} nation–hero relations
- [Spell summon](spell-summons.md) — {stats['spell_relations']} fixed summon relations
- [Magic Site Unit](magic-sites.md) — {stats['site_relations']} site–unit relations
- [Mount](mounts.md) — {stats['mount_units']} unique Mount records
- [Shape relation](shapes.md) — {stats['shape_relations']} direct shape links
- [入手経路未分類](unclassified.md) — {stats['unclassified']} no confirmed indexed source

## この索引でいう「確認済み」

次の明示的なデータ参照だけを入手経路として採用します。

1. 国家Recruit mapping
2. 国家属性`hero1..6` / `multihero1..2`
3. `pretender_types_by_nation.csv`
4. Research可能Spellの固定Unit summon effect
5. MagicSites.csvのUnit参照

MountとShapeはUnit間関係であり、直接のRecruit経路とは別に扱います。Event、Freespawn、Random summon pool、Wish、Transformation、特殊国家処理は、対応を確定できるまで未分類へ残します。

## 読み方

```text
Unit page
├ 基本能力
├ Magic Path
├ Weapon / Armor / Mount
├ Recruit / Hero / Pretender / Spell / Site
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


def write_unit_catalog(data, out: Path) -> dict[str, int]:
    out.mkdir(parents=True, exist_ok=True)
    by_id = out / "by-id"
    by_id.mkdir(parents=True, exist_ok=True)
    for unit_id, row in sorted(data["units"].items()):
        (by_id / unit_filename(unit_id)).write_text(unit_page(unit_id, row, data), encoding="utf-8")

    write_all_indexes(out, data)
    write_pretenders(out, data)
    write_heroes(out, data)
    write_spell_summons(out, data)
    write_magic_sites(out, data)
    write_mounts(out, data)
    write_shapes(out, data)
    _path, related_only, unclassified = write_unclassified(out, data)

    stats = {
        "units": len(data["units"]),
        "unit_pages": len(list(by_id.glob("*.md"))),
        "acquired_units": len(data["acquisitions"]),
        "recruit_relations": sum(len(values) for values in data["recruit"].values()),
        "hero_relations": sum(len(values) for values in data["heroes"].values()),
        "pretender_relations": sum(len(values) for values in data["pretenders"].values()),
        "spell_relations": sum(len(values) for values in data["spell_summons"].values()),
        "site_relations": sum(len(values) for values in data["sites"].values()),
        "mount_units": len(data["riders_by_mount"]),
        "mount_relations": sum(len(values) for values in data["riders_by_mount"].values()),
        "shape_relations": sum(len(values) for values in data["shape_outgoing"].values()),
        "related_only": related_only,
        "unclassified": unclassified,
    }
    write_main_index(out, data, stats)
    return stats
