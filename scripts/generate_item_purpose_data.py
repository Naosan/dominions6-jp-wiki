#!/usr/bin/env python3
"""Generate Magic Item construction and purpose reverse indexes.

This is a supplemental generator for the pinned Dominions 6.35 Item data.
It deliberately emits factual candidate sets from explicit BaseI fields; tactical
recommendations stay in the hand-written docs/items/ pages.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from scripts import generate_spell_item_data as core

ITEM_OUT = core.ITEM_OUT
CONSTRUCTION_LEVELS = (1, 3, 5, 7, 9)
WEAPON_TYPES = {"1-h wpn", "2-h wpn", "missile"}
DEFENSIVE_TYPES = {"shield", "armor", "helm", "barding"}

PURPOSES: dict[str, dict[str, object]] = {
    "offense": {
        "title": "攻撃・Weapon支援",
        "intro": "Weapon系Itemと、Attack・Strength・Precision・攻撃Auraや反撃能力など明示的な攻撃支援fieldを持つItemです。",
        "types": WEAPON_TYPES,
        "numeric": (
            ("str", "Str"), ("att", "Att"), ("prec", "Prec"), ("pen", "Pen"),
            ("fear", "Fear"), ("awe", "Awe"), ("chill", "Chill"), ("heat", "Heat"),
            ("berserk", "Berserk"), ("bers", "Berserk"),
        ),
        "flags": (
            ("quick", "Quickness"), ("fireshield", "Fire Shield"),
            ("banefireshield", "Bane Fire Shield"), ("bloodvengeance", "Blood Vengeance"),
            ("curseattacker", "Curse attacker"), ("stunattackers", "Stun attackers"),
            ("dancingweapon", "Dancing Weapon"), ("poisonarmor", "Poison Armor"),
            ("entangle", "Entangle"), ("soulvortex", "Soul Vortex"),
            ("petrification", "Petrification"), ("damagereversal", "Damage Reversal"),
        ),
        "text": (("spelleffect", "Spell effect"), ("itemspell", "Item spell")),
    },
    "defense": {
        "title": "防御・Resistance",
        "intro": "Armor / Shield系Itemと、Protection・HP・MR・Elemental/Poison/Acid Resistance・回避防御を明示的に持つItemです。",
        "types": DEFENSIVE_TYPES,
        "numeric": (
            ("shockres", "SR"), ("fireres", "FR"), ("coldres", "CR"),
            ("poisonres", "PR"), ("acidres", "AR"), ("mr", "MR"),
            ("hp", "HP"), ("protf", "Prot"), ("protb", "Body Prot"),
            ("def", "Def"), ("morale", "Morale"), ("airshield", "Air Shield"),
            ("woundfend", "Wound Fend"),
        ),
        "flags": (
            ("eth", "Ethereal"), ("luck", "Luck"), ("twistfate", "Twist Fate"),
            ("barkskin", "Barkskin"), ("stoneskin", "Stoneskin"), ("ironskin", "Ironskin"),
            ("returning", "Returning"), ("invulnerable", "Invulnerability"),
            ("antimagic", "Antimagic"), ("blur", "Blur"),
        ),
        "text": (),
    },
    "sustain": {
        "title": "Sustain・疲労・回復",
        "intro": "Reinvigoration、Regeneration、Healing、追加Lifeなど長期戦・継戦能力へ直接関係するfieldを持つItemです。",
        "types": set(),
        "numeric": (
            ("reinvigoration", "Reinvig"), ("regeneration", "Regeneration"),
            ("limitedregeneration", "Limited Regen"), ("healer", "Healer"),
            ("autodishealer", "Auto disease healer"), ("hpbonus", "HP bonus"),
            ("slowaging", "Slow aging"), ("agingreductiontoallunits", "Aging reduction"),
        ),
        "flags": (
            ("diseasegrinder", "Disease Grinder"), ("extralife", "Extra Life"),
            ("soulvortex", "Soul Vortex"), ("eatforyouth", "Eat for Youth"),
        ),
        "text": (),
    },
    "mobility": {
        "title": "移動・Flying・水中",
        "intro": "Map movement、Flying、Water Breathing、Swimming、Sailingなど移動範囲を変えるfieldを持つItemです。",
        "types": set(),
        "numeric": (
            ("mapspeed", "Map Speed"), ("mapmovebonus", "Map Move"),
            ("flyingmapmove", "Flying Map Move"), ("flyingmaxtotalsize", "Flying max size"),
            ("sailingshipsize", "Sailing ship size"), ("sailingmaxunitsize", "Sailing max unit size"),
            ("farsail", "Far Sail"), ("swimming", "Swimming"),
        ),
        "flags": (
            ("fly", "Flying"), ("float", "Floating"), ("floating", "Floating"),
            ("waterbreathing", "Water Breathing"), ("giftofwater", "Gift of Water Breathing"),
            ("wintermove", "Winter Move"), ("unhindered", "Unhindered"),
            ("stormimmune", "Storm Immune"),
        ),
        "text": (),
    },
    "mage-support": {
        "title": "Mage・Research・Forge支援",
        "intro": "Magic Path Booster、Research、Forge、Blood Search、casting / ritual補助、temporary gemなどMage economyへ関係するItemです。",
        "types": set(),
        "numeric": (
            ("researchbonus", "Research"), ("forge", "Forge"), ("fixforge", "Forge"),
            ("douse", "Blood Search"), ("bloodsearcher", "Blood Searcher"),
            ("firerange", "Fire Range"), ("airrange", "Air Range"), ("waterrange", "Water Range"),
            ("earthrange", "Earth Range"), ("astralrange", "Astral Range"),
            ("deathrange", "Death Range"), ("naturerange", "Nature Range"),
            ("glamourrange", "Glamour Range"), ("bloodrange", "Blood Range"),
            ("tmpfiregems", "Tmp F gem"), ("tmpairgems", "Tmp A gem"),
            ("tmpwatergems", "Tmp W gem"), ("tmpearthgems", "Tmp E gem"),
            ("tmpastralgems", "Tmp S gem"), ("tmpdeathgems", "Tmp D gem"),
            ("tmpnaturegems", "Tmp N gem"), ("tmpglamourgems", "Tmp G gem"),
        ),
        "flags": (
            ("mastersmith", "Master Smith"), ("masterritualist", "Master Ritualist"),
            ("fastcasting", "Fast Casting"), ("bloodsearcher", "Blood Searcher"),
            ("dreamenhancer", "Dream Enhancer"),
            ("fireempower", "Fire Empower"), ("airempower", "Air Empower"),
            ("waterempower", "Water Empower"), ("earthempower", "Earth Empower"),
        ),
        "text": (
            ("startbattlespell", "Start battle spell"),
            ("autocombatspell", "Auto combat spell"),
            ("ritual", "Ritual"),
        ),
        "boosters": True,
    },
    "operations": {
        "title": "指揮・偵察・Siege・特殊作戦",
        "intro": "Leadership、Stealth、Patrol、Siege、Supply、Assassination / Seductionなど戦闘外の任務へ関係するItemです。",
        "types": set(),
        "numeric": (
            ("ldr-n", "Leadership"), ("ldr-u", "Undead Ldr"), ("ldr-m", "Magic Ldr"),
            ("inspirational", "Inspirational"), ("taskmaster", "Taskmaster"),
            ("stealth", "Stealth"), ("stealthb", "Stealth bonus"),
            ("patrolbonus", "Patrol"), ("siegebonus", "Siege"),
            ("castledef", "Castle Def"), ("supplybonus", "Supply"),
            ("pillagebonus", "Pillage"), ("goldgen", "Gold generation"),
        ),
        "flags": (
            ("invisibility", "Invisible"), ("assassin", "Assassin"),
            ("seduction", "Seduction"), ("scalewalls", "Scale Walls"),
            ("falsesupplies", "False Supplies"),
        ),
        "text": (),
    },
    "vision": {
        "title": "視認・Darkness・偵察",
        "intro": "Darkvision、Spirit Sight、True Sight、Magic Eye、Invisibilityなど視認・偵察へ関係するfieldを持つItemです。",
        "types": set(),
        "numeric": (("darkvision", "Darkvision"), ("magiceye", "Magic Eye")),
        "flags": (
            ("spiritsight", "Spirit Sight"), ("truesight", "True Sight"),
            ("invisibility", "Invisible"), ("unseen", "Unseen"),
            ("allunitslooklikebearertoscouts", "Disguise army"),
        ),
        "text": (),
    },
}

START = "<!-- item-purpose-index:start -->"
END = "<!-- item-purpose-index:end -->"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    return parser.parse_args()


def nonzero(row: dict[str, str], key: str) -> bool:
    return core.num(row, key) != 0


def booster_features(row: dict[str, str]) -> list[str]:
    return [f"{code}+{core.num(row, code)}" for code in "FAWESDNGBH" if core.num(row, code) > 0]


def purpose_features(row: dict[str, str], purpose: str) -> list[str]:
    spec = PURPOSES[purpose]
    features: list[str] = []
    for key, label in spec.get("numeric", ()):
        value = core.num(row, key)
        if value:
            features.append(f"{label} {value:+d}" if value < 0 else f"{label} {value}")
    for key, label in spec.get("flags", ()):
        if core.yes(row, key):
            features.append(label)
    for key, label in spec.get("text", ()):
        value = (row.get(key) or "").strip()
        if value and value != "0":
            features.append(f"{label}: {value}")
    if spec.get("boosters"):
        features.extend(booster_features(row))
    return features


def matches_purpose(row: dict[str, str], purpose: str) -> bool:
    spec = PURPOSES[purpose]
    if (row.get("type") or "").strip() in spec.get("types", set()):
        return True
    return bool(purpose_features(row, purpose))


def purpose_table(items: list[dict[str, object]], raw_by_id: dict[int, dict[str, str]], purpose: str) -> str:
    rows = [item for item in items if matches_purpose(raw_by_id[int(item["id"])], purpose)]
    if not rows:
        return "該当Itemなし。\n"
    out = [
        "| Item | ID | Slot | Research | Req | Gem | Extracted features | Restriction |",
        "|---|---:|---|---|---|---|---|---|",
    ]
    for item in rows:
        raw = raw_by_id[int(item["id"])]
        features = purpose_features(raw, purpose)
        if not features and str(item["type"]) in PURPOSES[purpose].get("types", set()):
            features = ["Slot category"]
        out.append(
            f"| {core.esc(item['name'])} | {item['id']} | {core.esc(item['type_title'])} | "
            f"{item['construction']} | {item['path']} | {item['cost']} | "
            f"{core.esc(', '.join(features) or '—')} | {core.esc(item['restriction'])} |"
        )
    return "\n".join(out) + "\n"


def construction_page(level: int, items: list[dict[str, object]]) -> str:
    selected = [item for item in items if int(item["const"]) == level]
    lines = [
        "---",
        f'title: "Construction {level} Item一覧"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {core.COMMIT}"',
        "---",
        "",
        f"# Construction {level} Item一覧",
        "",
        f"Construction {level}でForge可能なItemは**{len(selected)}**件です。",
        "",
        "このページは事実索引です。研究優先度と実戦評価は[Forge計画](../../../items/forge-planning.md)と[用途別Item辞典](../../../items/purpose-dictionary.md)を参照してください。",
        "",
        "[Magic Itemデータ索引へ戻る](../index.md)",
        "",
    ]
    for item_type, (title, _slug) in core.ITEM_TYPES.items():
        group = [item for item in selected if item["type"] == item_type]
        if group:
            lines += [f"## {title}", "", core.item_table(group)]
    return "\n".join(lines)


def purpose_page(purpose: str, items: list[dict[str, object]], raw_by_id: dict[int, dict[str, str]]) -> str:
    spec = PURPOSES[purpose]
    selected_count = sum(matches_purpose(raw_by_id[int(item["id"])], purpose) for item in items)
    return "\n".join(
        [
            "---",
            f'title: "{spec["title"]} Item索引"',
            "status: generated",
            'verified_version: "6.35"',
            f'generated_from: "dom6inspector {core.COMMIT}"',
            "---",
            "",
            f"# {spec['title']} Item索引",
            "",
            str(spec["intro"]),
            "",
            f"抽出対象は**{selected_count}**件です。同じItemが複数の目的別索引へ重複することがあります。",
            "",
            "!!! warning \"候補集合であってTier表ではない\"",
            "    BaseIの明示fieldから機械抽出しています。発動Spell、Weapon固有Damage、特殊条件、Carrier相性まで完全には表しません。最終確認はゲーム内Item詳細とDom6 Mod Inspectorを優先してください。",
            "",
            "[Magic Itemデータ索引へ戻る](../index.md)",
            "",
            purpose_table(items, raw_by_id, purpose),
        ]
    )


def index_block() -> str:
    construction = "\n".join(
        f"- [Construction {level}](by-construction/c{level}.md)" for level in CONSTRUCTION_LEVELS
    )
    purpose = "\n".join(
        f"- [{spec['title']}](by-purpose/{slug}.md)" for slug, spec in PURPOSES.items()
    )
    return "\n".join(
        [
            START,
            "## Construction別",
            "",
            construction,
            "",
            "## 機能・目的別の機械抽出",
            "",
            purpose,
            "",
            "これらはBaseIの明示fieldから作る候補索引です。実戦での選び方は[用途別Item辞典](../../items/purpose-dictionary.md)を参照してください。",
            END,
            "",
        ]
    )


def patch_item_index() -> None:
    path = ITEM_OUT / "index.md"
    text = path.read_text(encoding="utf-8")
    block = index_block()
    if START in text and END in text:
        before, rest = text.split(START, 1)
        _old, after = rest.split(END, 1)
        text = before + block.rstrip() + after
    else:
        anchor = "\n## 表の読み方"
        if anchor not in text:
            raise ValueError("Magic Item index insertion anchor not found")
        text = text.replace(anchor, "\n" + block + "## 表の読み方", 1)
    path.write_text(text, encoding="utf-8")


def write_pages(items: list[dict[str, object]], raw_by_id: dict[int, dict[str, str]]) -> None:
    construction_dir = ITEM_OUT / "by-construction"
    purpose_dir = ITEM_OUT / "by-purpose"
    construction_dir.mkdir(parents=True, exist_ok=True)
    purpose_dir.mkdir(parents=True, exist_ok=True)
    for level in CONSTRUCTION_LEVELS:
        (construction_dir / f"c{level}.md").write_text(construction_page(level, items), encoding="utf-8")
    for purpose in PURPOSES:
        (purpose_dir / f"{purpose}.md").write_text(purpose_page(purpose, items, raw_by_id), encoding="utf-8")
    patch_item_index()


def main() -> None:
    args = parse_args()
    names = ("BaseI.csv", "weapons.csv", "armors.csv")
    paths = {name: core.source(name, args.refresh, args.offline) for name in names}
    items = core.item_rows(paths)
    raw_by_id = {
        core.num(row, "id"): row
        for row in core.tsv(paths["BaseI.csv"])
        if row.get("id")
    }
    write_pages(items, raw_by_id)
    counts = {
        purpose: sum(matches_purpose(raw_by_id[int(item["id"])], purpose) for item in items)
        for purpose in PURPOSES
    }
    print("generated construction item indexes:", ", ".join(f"C{level}" for level in CONSTRUCTION_LEVELS))
    print("generated purpose item indexes:", ", ".join(f"{key}={value}" for key, value in counts.items()))


if __name__ == "__main__":
    main()
