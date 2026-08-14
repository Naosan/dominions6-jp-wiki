#!/usr/bin/env python3
"""Generate Dominions 6 spell and magic-item reference pages.

The generator uses a pinned Dominions 6.35 snapshot from larzm42/dom6inspector.
Generated pages are factual indexes. Strategy and recommendations remain in the
hand-written pages under docs/magic/ and docs/items/.

Run from the repository root:
    python scripts/generate_spell_item_data.py
    python scripts/generate_spell_item_data.py --refresh
    python scripts/generate_spell_item_data.py --offline
"""
from __future__ import annotations

import argparse
import csv
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPELL_OUT = ROOT / "docs" / "data" / "spells"
ITEM_OUT = ROOT / "docs" / "data" / "items"
CATALOG = ROOT / "data" / "nations.tsv"

COMMIT = "cfac4311bc0b58053b8dead7bffbc036ba9bd5dc"
BASE = f"https://raw.githubusercontent.com/larzm42/dom6inspector/{COMMIT}/gamedata"
CACHE = ROOT / ".cache" / "dom6inspector" / COMMIT
FILES = (
    "spells.csv",
    "effects_spells.csv",
    "attributes_by_spell.csv",
    "BaseI.csv",
    "weapons.csv",
    "armors.csv",
)

SCHOOLS = {
    0: ("Conjuration", "conjuration"),
    1: ("Alteration", "alteration"),
    2: ("Evocation", "evocation"),
    3: ("Construction", "construction"),
    4: ("Enchantment", "enchantment"),
    5: ("Thaumaturgy", "thaumaturgy"),
    6: ("Blood Magic", "blood-magic"),
    7: ("Divine", "divine"),
}
PATHS = {
    0: ("F", "Fire", "fire"),
    1: ("A", "Air", "air"),
    2: ("W", "Water", "water"),
    3: ("E", "Earth", "earth"),
    4: ("S", "Astral", "astral"),
    5: ("D", "Death", "death"),
    6: ("N", "Nature", "nature"),
    7: ("G", "Glamour", "glamour"),
    8: ("B", "Blood", "blood"),
    9: ("H", "Holy", "holy"),
}
ITEM_TYPES = {
    "1-h wpn": ("片手武器", "one-handed-weapons"),
    "2-h wpn": ("両手武器", "two-handed-weapons"),
    "missile": ("射撃武器", "missile-weapons"),
    "shield": ("盾", "shields"),
    "armor": ("鎧", "armor"),
    "helm": ("兜", "helmets"),
    "boots": ("靴", "boots"),
    "misc": ("Miscellaneous", "miscellaneous"),
    "crown": ("Crown", "crowns"),
    "barding": ("Barding", "barding"),
}
FORGE_COST = {1: 5, 2: 10, 3: 15, 4: 25, 5: 40, 6: 60, 7: 80, 8: 100, 9: 120}
EFFECT_NAMES = {
    1: "Summon",
    2: "Damage",
    3: "Stun damage",
    7: "Poison damage",
    13: "Healing",
    20: "Blink",
    24: "Holy damage",
    28: "Enslave",
    29: "Charm",
    31: "Summon independent",
    43: "Border summon",
    73: "Anti-magic damage",
    103: "Drain life",
    10001: "Summon",
    10019: "Teleport",
    10021: "Summon commander",
    10035: "Crossbreed",
    10037: "Farsummon",
    10038: "Independent farsummon",
    10039: "Gift of Reason",
    10050: "Assassination",
    10063: "Build fort",
    10077: "Army teleport",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="redownload pinned CSV files")
    parser.add_argument("--offline", action="store_true", help="use cache only")
    return parser.parse_args()


def tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def num(row: dict[str, str], key: str, default: int = 0) -> int:
    try:
        return int(float(row.get(key) or default))
    except (TypeError, ValueError):
        return default


def yes(row: dict[str, str], key: str) -> bool:
    return row.get(key) not in (None, "", "0", "0.0")


def esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def source(name: str, refresh: bool, offline: bool) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / name
    if path.exists() and path.stat().st_size > 0 and not refresh:
        return path
    if offline:
        raise FileNotFoundError(f"offline cache missing: {path}")

    request = urllib.request.Request(
        f"{BASE}/{name}",
        headers={"User-Agent": "dominions6-jp-wiki/1.0"},
    )
    error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                data = response.read()
            if not data:
                raise RuntimeError("empty download")
            path.write_bytes(data)
            return path
        except (urllib.error.URLError, TimeoutError, RuntimeError) as exc:
            error = exc
            time.sleep(2**attempt)
    raise RuntimeError(f"download failed: {name}: {error}")


def nation_names() -> dict[int, str]:
    if not CATALOG.exists():
        return {}
    out: dict[int, str] = {}
    for row in tsv(CATALOG):
        era = row.get("era", "")
        code = {"1": "EA", "2": "MA", "3": "LA", "EA": "EA", "MA": "MA", "LA": "LA"}.get(era, era)
        out[int(row["id"])] = f"{code} {row['name']}"
    return out


def path_code(value: object) -> str:
    try:
        return PATHS[int(value)][0]
    except (KeyError, TypeError, ValueError):
        return ""


def spell_path(row: dict[str, str]) -> str:
    parts: list[str] = []
    for pkey, lkey in (("path1", "pathlevel1"), ("path2", "pathlevel2")):
        code = path_code(row.get(pkey))
        level = num(row, lkey)
        if code and level:
            parts.append(f"{code}{level}")
    return "".join(parts) or "—"


def spell_research(row: dict[str, str]) -> str:
    school = num(row, "school", -1)
    title = SCHOOLS.get(school, (f"School {school}", ""))[0]
    if school == 7:
        return title
    return f"{title} {num(row, 'researchlevel')}"


def effect_map(rows: list[dict[str, str]]) -> dict[int, dict[str, str]]:
    out: dict[int, dict[str, str]] = {}
    for row in rows:
        if row.get("record_id"):
            out[int(row["record_id"])] = row
    return out


def spell_attributes(rows: list[dict[str, str]]) -> dict[int, list[tuple[int, int]]]:
    out: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for row in rows:
        if not row.get("spell_number") or not row.get("attribute"):
            continue
        out[int(row["spell_number"])].append((num(row, "attribute"), num(row, "raw_value")))
    return out


def spell_kind(effect: dict[str, str] | None) -> str:
    return "Ritual" if effect and num(effect, "ritual") == 1 else "Combat"


def spell_gem_cost(row: dict[str, str], effect: dict[str, str] | None) -> str:
    cost = num(row, "gemcost")
    if spell_kind(effect) == "Ritual" and cost == 0:
        cost = num(row, "fatiguecost") // 100
    if cost <= 0:
        return "—"
    code = path_code(row.get("path1")) or "?"
    return f"{cost}{code}"


def spell_fatigue(row: dict[str, str], effect: dict[str, str] | None) -> str:
    if spell_kind(effect) == "Ritual":
        return "—"
    base = num(row, "fatiguecost")
    gems = num(row, "gemcost")
    total = base + gems * 100
    return str(total) if total else "0"


def range_text(row: dict[str, str], effect: dict[str, str] | None) -> str:
    if not effect or spell_kind(effect) == "Ritual":
        return "—"
    base = num(effect, "range_base")
    per = num(effect, "range_per_level")
    if base == 0 and per == 0:
        return "Caster / special"
    if per:
        actual = base + num(row, "pathlevel1") * per
        return f"{actual} ({base}+{per}/lvl)"
    return str(base)


def area_text(effect: dict[str, str] | None) -> str:
    if not effect or spell_kind(effect) == "Ritual":
        return "—"
    battlefield = num(effect, "area_battlefield_pct")
    if battlefield:
        return f"{battlefield}% BF"
    base = num(effect, "area_base")
    per = num(effect, "area_per_level") % 10
    if base == 0 and per == 0:
        if num(effect, "range_base") == 0:
            return "Caster / special"
        return "1 / special"
    if per:
        return f"{base}+{per}/lvl"
    return str(base)


def spell_effect(effect: dict[str, str] | None) -> str:
    if not effect:
        return "—"
    number = num(effect, "effect_number")
    return EFFECT_NAMES.get(number, f"Effect {number}")


def spell_availability(spell_id: int, attrs: dict[int, list[tuple[int, int]]], nations: dict[int, str]) -> str:
    values = attrs.get(spell_id, [])
    national = [raw for attribute, raw in values if attribute == 278]
    realm = any(attribute == 602 for attribute, _ in values)
    parts: list[str] = []
    if national:
        labels = [nations.get(nation_id, f"Nation {nation_id}") for nation_id in national]
        parts.append("National: " + ", ".join(labels))
    if realm:
        parts.append("Realm restricted")
    return "; ".join(parts) or "Generic"


def spell_notes(row: dict[str, str], effect: dict[str, str] | None, availability: str) -> str:
    notes: list[str] = []
    if effect and num(effect, "area_battlefield_pct"):
        notes.append("Battlefield")
    if availability != "Generic":
        notes.append(availability)
    if num(row, "school") == 6:
        notes.append("Blood")
    if num(row, "school") == 7:
        notes.append("Divine")
    return ", ".join(notes) or "—"


def spell_rows(paths: dict[str, Path]) -> list[dict[str, object]]:
    effects = effect_map(tsv(paths["effects_spells.csv"]))
    attrs = spell_attributes(tsv(paths["attributes_by_spell.csv"]))
    nations = nation_names()
    output: list[dict[str, object]] = []

    for row in tsv(paths["spells.csv"]):
        school = num(row, "school", -1)
        if school not in SCHOOLS:
            continue
        name = (row.get("name") or "").strip()
        if not name or name in {"Nothing", "..."}:
            continue
        spell_id = num(row, "id")
        effect = effects.get(num(row, "effect_record_id"))
        availability = spell_availability(spell_id, attrs, nations)
        output.append(
            {
                "id": spell_id,
                "name": name,
                "school": school,
                "level": num(row, "researchlevel"),
                "research": spell_research(row),
                "path": spell_path(row),
                "path_numbers": tuple(
                    number
                    for number in (num(row, "path1", -1), num(row, "path2", -1))
                    if number in PATHS
                ),
                "kind": spell_kind(effect),
                "cost": spell_gem_cost(row, effect),
                "fatigue": spell_fatigue(row, effect),
                "range": range_text(row, effect),
                "area": area_text(effect),
                "effect": spell_effect(effect),
                "availability": availability,
                "notes": spell_notes(row, effect, availability),
            }
        )
    output.sort(key=lambda spell: (int(spell["school"]), int(spell["level"]), str(spell["name"]), int(spell["id"])))
    if len(output) < 500:
        raise ValueError(f"researchable spell set looks incomplete: {len(output)}")
    return output


def spell_table(spells: list[dict[str, object]], *, compact: bool = False) -> str:
    if not spells:
        return "該当Spellなし。\n"
    if compact:
        out = [
            "| Spell | ID | Research | Req | Type | Cost | Effect / Note |",
            "|---|---:|---|---|---|---|---|",
        ]
        for spell in spells:
            note = str(spell["effect"])
            if spell["notes"] != "—":
                note += f"; {spell['notes']}"
            out.append(
                f"| {esc(spell['name'])} | {spell['id']} | {esc(spell['research'])} | "
                f"{spell['path']} | {spell['kind']} | {spell['cost']} | {esc(note)} |"
            )
        return "\n".join(out) + "\n"

    out = [
        "| Spell | ID | Type | Lv | Req | Cost | Fatigue | Range | AoE | Effect | Availability |",
        "|---|---:|---|---:|---|---|---:|---|---|---|---|",
    ]
    for spell in spells:
        out.append(
            f"| {esc(spell['name'])} | {spell['id']} | {spell['kind']} | {spell['level']} | "
            f"{spell['path']} | {spell['cost']} | {spell['fatigue']} | {spell['range']} | "
            f"{spell['area']} | {esc(spell['effect'])} | {esc(spell['availability'])} |"
        )
    return "\n".join(out) + "\n"


def spell_index(spells: list[dict[str, object]]) -> str:
    school_counts = Counter(int(spell["school"]) for spell in spells)
    type_counts = Counter(str(spell["kind"]) for spell in spells)
    lines = [
        "---",
        'title: "Spellデータ索引"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {COMMIT}"',
        "---",
        "",
        "# Spellデータ索引",
        "",
        "Research可能なSpellをSchool・Magic Path・National restrictionから参照する自動生成索引です。",
        "",
        f"- 登録Spell: **{len(spells)}**",
        f"- Combat: **{type_counts['Combat']}**",
        f"- Ritual: **{type_counts['Ritual']}**",
        "",
        "## Research School",
        "",
        "| School | Spell数 | 一覧 |",
        "|---|---:|---|",
    ]
    for number, (name, slug) in SCHOOLS.items():
        lines.append(f"| {name} | {school_counts[number]} | [{name}](by-school/{slug}.md) |")
    lines += [
        "",
        "## Magic Path",
        "",
        "| Path | 一覧 |",
        "|---|---|",
    ]
    for _number, (code, name, slug) in PATHS.items():
        lines.append(f"| {code} — {name} | [{name} Spell](by-path/{slug}.md) |")
    lines += [
        "",
        "## 特殊索引",
        "",
        "- [National / Realm restricted Spell](national.md)",
        "",
        "## 表の読み方",
        "",
        "- **Req**: Spellの要求Path。`F3A1`ならFire 3・Air 1。",
        "- **Cost**: 戦闘GemまたはRitual Gem / Blood Slave。主Pathの記号を付ける。",
        "- **Fatigue**: Combat Spellの基礎FatigueとGem相当分を合算した抽出上の値。",
        "- **Range / AoE**: 単純な数式で表せないSpellは`special`と表示する。",
        "- **Availability**: National / Realm restriction。Hero・Event等のCaster条件は含まない。",
        "",
        "!!! warning \"自動生成値の限界\"",
        "    Range、AoE、Fatigue、複合効果はSpell固有処理で変わることがあります。最終確認はゲーム内Spell詳細を優先してください。",
        "",
        "## 関連攻略",
        "",
        "- [魔法の基本](../../magic/index.md)",
        "- [Researchと研究ルート](../../magic/research.md)",
        "- [Magic Path総論](../../magic/paths/index.md)",
        "",
    ]
    return "\n".join(lines)


def school_page(number: int, spells: list[dict[str, object]]) -> str:
    title, _slug = SCHOOLS[number]
    selected = [spell for spell in spells if int(spell["school"]) == number]
    lines = [
        "---",
        f'title: "{title} Spell一覧"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {COMMIT}"',
        "---",
        "",
        f"# {title} Spell一覧",
        "",
        f"{title}に属するResearch可能Spellは**{len(selected)}**件です。",
        "",
        "[Spellデータ索引へ戻る](../index.md)",
        "",
    ]
    if number == 7:
        lines.append(spell_table(selected))
    else:
        for level in sorted({int(spell["level"]) for spell in selected}):
            level_spells = [spell for spell in selected if int(spell["level"]) == level]
            lines += [f"## Research Level {level}", "", spell_table(level_spells)]
    return "\n".join(lines)


def path_page(number: int, spells: list[dict[str, object]]) -> str:
    code, title, _slug = PATHS[number]
    selected = [spell for spell in spells if number in spell["path_numbers"]]
    lines = [
        "---",
        f'title: "{title} Spell索引"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {COMMIT}"',
        "---",
        "",
        f"# {code} — {title} Spell索引",
        "",
        f"{title}を要求するResearch可能Spellは**{len(selected)}**件です。主Path・副Pathの両方を含みます。",
        "",
        f"- [{title} Path攻略](../../../magic/paths/{PATHS[number][2]}.md)",
        "- [Spellデータ索引へ戻る](../index.md)",
        "",
    ]
    for school in SCHOOLS:
        group = [spell for spell in selected if int(spell["school"]) == school]
        if not group:
            continue
        lines += [f"## {SCHOOLS[school][0]}", "", spell_table(group, compact=True)]
    return "\n".join(lines)


def national_spell_page(spells: list[dict[str, object]]) -> str:
    selected = [spell for spell in spells if spell["availability"] != "Generic"]
    return "\n".join(
        [
            "---",
            'title: "National・Realm restricted Spell"',
            "status: generated",
            'verified_version: "6.35"',
            f'generated_from: "dom6inspector {COMMIT}"',
            "---",
            "",
            "# National・Realm restricted Spell",
            "",
            "国家またはRealmによる利用制限が抽出されたSpellの索引です。",
            "",
            "[Spellデータ索引へ戻る](index.md)",
            "",
            spell_table(selected),
            "",
            "!!! note",
            "    国家固有Spellでも、召喚CommanderやPretenderのPathが不足すれば使用できません。逆に、Realm条件や国家固有の取得方法は表だけでは完全に表せない場合があります。",
            "",
        ]
    )


def item_requirement(row: dict[str, str]) -> str:
    parts: list[str] = []
    main = (row.get("mainpath") or "").strip()
    secondary = (row.get("secondarypath") or "").strip()
    if main and num(row, "mainlevel"):
        parts.append(f"{main}{num(row, 'mainlevel')}")
    if secondary and num(row, "secondarylevel"):
        parts.append(f"{secondary}{num(row, 'secondarylevel')}")
    return "".join(parts) or "—"


def item_gem_cost(row: dict[str, str]) -> str:
    if num(row, "constlevel") == 12:
        return "—"
    parts: list[str] = []
    for path_key, level_key, modifier_key in (
        ("mainpath", "mainlevel", "itemcost1"),
        ("secondarypath", "secondarylevel", "itemcost2"),
    ):
        path = (row.get(path_key) or "").strip()
        level = num(row, level_key)
        if not path or level <= 0 or level not in FORGE_COST:
            continue
        multiplier = 1 + num(row, modifier_key) / 100
        cost = round(FORGE_COST[level] * multiplier)
        parts.append(f"{cost}{path}")
    return " + ".join(parts) or "—"


def item_boosters(row: dict[str, str]) -> str:
    parts = [f"{code}+{num(row, code)}" for code in "FAWESDNGBH" if num(row, code) > 0]
    return " ".join(parts) or "—"


def item_restriction(row: dict[str, str], nations: dict[int, str]) -> str:
    ids: list[int] = []
    for index in range(1, 7):
        nation_id = num(row, f"restricted{index}")
        if nation_id:
            ids.append(nation_id)
    if not ids:
        return "Generic"
    return ", ".join(nations.get(nation_id, f"Nation {nation_id}") for nation_id in ids)


def signed(label: str, value: int) -> str:
    return f"{label} {value:+d}"


def item_traits(row: dict[str, str]) -> list[str]:
    traits: list[str] = []
    numeric = (
        ("shockres", "SR"),
        ("fireres", "FR"),
        ("coldres", "CR"),
        ("poisonres", "PR"),
        ("acidres", "AR"),
        ("mr", "MR"),
        ("reinvigoration", "Reinvig"),
        ("researchbonus", "Research"),
        ("douse", "Blood Search"),
        ("forge", "Forge"),
        ("fixforge", "Forge"),
        ("ldr-n", "Leadership"),
        ("ldr-u", "Undead Ldr"),
        ("ldr-m", "Magic Ldr"),
        ("inspirational", "Inspirational"),
        ("patrolbonus", "Patrol"),
        ("siegebonus", "Siege"),
        ("castledef", "Castle Def"),
        ("supplybonus", "Supply"),
        ("mapmovebonus", "Map Move"),
        ("stealth", "Stealth"),
        ("hp", "HP"),
        ("protf", "Prot"),
        ("str", "Str"),
        ("att", "Att"),
        ("def", "Def"),
        ("prec", "Prec"),
        ("enc", "Enc"),
    )
    for key, label in numeric:
        value = num(row, key)
        if value:
            traits.append(signed(label, value))
    flags = (
        ("quick", "Quickness"),
        ("eth", "Ethereal"),
        ("luck", "Luck"),
        ("twistfate", "Twist Fate"),
        ("airshield", "Air Shield"),
        ("antimagic", "Antimagic"),
        ("truesight", "True Sight"),
        ("spiritsight", "Spirit Sight"),
        ("waterbreathing", "Water Breathing"),
        ("giftofwater", "Gift of Water Breathing"),
        ("fly", "Flying"),
        ("float", "Floating"),
        ("invisibility", "Invisible"),
        ("regeneration", "Regeneration"),
        ("limitedregeneration", "Limited Regeneration"),
        ("fireshield", "Fire Shield"),
        ("banefireshield", "Bane Fire Shield"),
        ("invulnerable", "Invulnerability"),
        ("soulvortex", "Soul Vortex"),
        ("fastcasting", "Fast Casting"),
        ("masterritualist", "Master Ritualist"),
        ("bloodsearcher", "Blood Searcher"),
        ("extraarms", "Extra Arms"),
        ("dancingweapon", "Dancing Weapon"),
        ("singleuse", "Single use"),
        ("crown", "Artifact / Crown"),
    )
    for key, label in flags:
        if yes(row, key):
            traits.append(label)
    return traits[:12]


def item_base(row: dict[str, str], weapons: dict[int, dict[str, str]], armors: dict[int, dict[str, str]]) -> str:
    if num(row, "weapon") in weapons:
        weapon = weapons[num(row, "weapon")]
        bits = [weapon.get("name") or f"Weapon {weapon['id']}"]
        for key, label in (("att", "Att"), ("def", "Def"), ("len", "Len"), ("nratt", "Atk#")):
            if weapon.get(key) not in (None, "", "0"):
                bits.append(f"{label} {weapon[key]}")
        return ", ".join(bits)
    if num(row, "armor") in armors:
        armor = armors[num(row, "armor")]
        bits = [armor.get("name") or f"Armor {armor['id']}"]
        for key, label in (("def", "Def"), ("enc", "Enc")):
            if armor.get(key) not in (None, "", "0"):
                bits.append(f"{label} {armor[key]}")
        return ", ".join(bits)
    return "—"


def item_rows(paths: dict[str, Path]) -> list[dict[str, object]]:
    nations = nation_names()
    weapons = {num(row, "id"): row for row in tsv(paths["weapons.csv"]) if row.get("id")}
    armors = {num(row, "id"): row for row in tsv(paths["armors.csv"]) if row.get("id")}
    output: list[dict[str, object]] = []

    for row in tsv(paths["BaseI.csv"]):
        name = (row.get("name") or "").strip()
        item_type = (row.get("type") or "").strip()
        if not name or item_type not in ITEM_TYPES:
            continue
        const = num(row, "constlevel")
        if const <= 0:
            continue
        traits = item_traits(row)
        output.append(
            {
                "id": num(row, "id"),
                "name": name,
                "type": item_type,
                "type_title": ITEM_TYPES[item_type][0],
                "type_slug": ITEM_TYPES[item_type][1],
                "construction": "Unforgeable" if const == 12 else f"Construction {const}",
                "const": const,
                "path": item_requirement(row),
                "cost": item_gem_cost(row),
                "boosters": item_boosters(row),
                "base": item_base(row, weapons, armors),
                "traits": traits,
                "traits_text": ", ".join(traits) or "—",
                "restriction": item_restriction(row, nations),
                "research": num(row, "researchbonus"),
                "has_resistance": any(num(row, key) for key in ("shockres", "fireres", "coldres", "poisonres", "acidres", "mr")) or yes(row, "antimagic"),
                "has_utility": any(
                    num(row, key)
                    for key in (
                        "reinvigoration",
                        "douse",
                        "forge",
                        "fixforge",
                        "ldr-n",
                        "ldr-u",
                        "ldr-m",
                        "patrolbonus",
                        "siegebonus",
                        "castledef",
                        "supplybonus",
                        "mapmovebonus",
                        "stealth",
                    )
                )
                or any(yes(row, key) for key in ("fly", "float", "waterbreathing", "giftofwater", "invisibility", "truesight", "spiritsight", "fastcasting", "masterritualist")),
            }
        )
    output.sort(key=lambda item: (int(item["const"]), str(item["type_title"]), str(item["name"]), int(item["id"])))
    if len(output) < 250:
        raise ValueError(f"magic item set looks incomplete: {len(output)}")
    return output


def item_table(items: list[dict[str, object]]) -> str:
    if not items:
        return "該当Itemなし。\n"
    out = [
        "| Item | ID | Research | Req | Gem | Booster | Base equipment | Effects | Restriction |",
        "|---|---:|---|---|---|---|---|---|---|",
    ]
    for item in items:
        out.append(
            f"| {esc(item['name'])} | {item['id']} | {item['construction']} | {item['path']} | "
            f"{item['cost']} | {item['boosters']} | {esc(item['base'])} | "
            f"{esc(item['traits_text'])} | {esc(item['restriction'])} |"
        )
    return "\n".join(out) + "\n"


def item_index(items: list[dict[str, object]]) -> str:
    type_counts = Counter(str(item["type"]) for item in items)
    lines = [
        "---",
        'title: "Magic Itemデータ索引"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {COMMIT}"',
        "---",
        "",
        "# Magic Itemデータ索引",
        "",
        "Magic ItemをSlot、Construction、要求Path、Gem Cost、Booster、主要効果から参照する自動生成索引です。",
        "",
        f"- 登録Item: **{len(items)}**",
        "",
        "## Slot / Type",
        "",
        "| Type | Item数 | 一覧 |",
        "|---|---:|---|",
    ]
    for item_type, (title, slug) in ITEM_TYPES.items():
        lines.append(f"| {title} | {type_counts[item_type]} | [{title}](by-type/{slug}.md) |")
    lines += [
        "",
        "## 目的別",
        "",
        "- [Magic Path Booster](boosters.md)",
        "- [Research Item](research.md)",
        "- [Resistance / MR Item](resistance.md)",
        "- [Utility Item](utility.md)",
        "- [Unforgeable / Artifact](unforgeable.md)",
        "",
        "## 表の読み方",
        "",
        "- **Research**: Forgeに必要なConstruction level。`Unforgeable`は通常鍛造不可。",
        "- **Req**: 鍛造者の要求Path。",
        "- **Gem**: Forge Bonusや国家割引を適用する前の基礎Gem Cost。",
        "- **Booster**: 装備時のMagic Path上昇。",
        "- **Base equipment**: Itemが参照する武器・防具の基本データ。",
        "- **Effects**: 抽出できる主要能力。全効果の文章説明ではない。",
        "",
        "!!! warning \"Costと効果\"",
        "    実際の鍛造CostはForge Bonus、Dwarven Hammer、国家割引などで変わります。特殊効果、武器のDamage Type、発動Spellはゲーム内Item詳細を優先してください。",
        "",
        "## 関連攻略",
        "",
        "- [Magic Item総論](../../items/index.md)",
        "- [Magic Path Booster攻略](../../items/boosters.md)",
        "- [Research Item攻略](../../items/research-items.md)",
        "- [Thug装備](../../items/thug-equipment.md)",
        "",
    ]
    return "\n".join(lines)


def item_type_page(item_type: str, items: list[dict[str, object]]) -> str:
    title, _slug = ITEM_TYPES[item_type]
    selected = [item for item in items if item["type"] == item_type]
    lines = [
        "---",
        f'title: "{title} Item一覧"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {COMMIT}"',
        "---",
        "",
        f"# {title} Item一覧",
        "",
        f"{title}に分類されるMagic Itemは**{len(selected)}**件です。",
        "",
        "[Magic Itemデータ索引へ戻る](../index.md)",
        "",
    ]
    for const in sorted({int(item["const"]) for item in selected}):
        group = [item for item in selected if int(item["const"]) == const]
        heading = "Unforgeable / Artifact" if const == 12 else f"Construction {const}"
        lines += [f"## {heading}", "", item_table(group)]
    return "\n".join(lines)


def filtered_item_page(title: str, intro: str, items: list[dict[str, object]]) -> str:
    return "\n".join(
        [
            "---",
            f'title: "{title}"',
            "status: generated",
            'verified_version: "6.35"',
            f'generated_from: "dom6inspector {COMMIT}"',
            "---",
            "",
            f"# {title}",
            "",
            intro,
            "",
            "[Magic Itemデータ索引へ戻る](index.md)",
            "",
            item_table(items),
            "",
        ]
    )


def write_pages(spells: list[dict[str, object]], items: list[dict[str, object]]) -> None:
    (SPELL_OUT / "by-school").mkdir(parents=True, exist_ok=True)
    (SPELL_OUT / "by-path").mkdir(parents=True, exist_ok=True)
    (ITEM_OUT / "by-type").mkdir(parents=True, exist_ok=True)

    (SPELL_OUT / "index.md").write_text(spell_index(spells), encoding="utf-8")
    for number, (_title, slug) in SCHOOLS.items():
        (SPELL_OUT / "by-school" / f"{slug}.md").write_text(school_page(number, spells), encoding="utf-8")
    for number, (_code, _title, slug) in PATHS.items():
        (SPELL_OUT / "by-path" / f"{slug}.md").write_text(path_page(number, spells), encoding="utf-8")
    (SPELL_OUT / "national.md").write_text(national_spell_page(spells), encoding="utf-8")

    (ITEM_OUT / "index.md").write_text(item_index(items), encoding="utf-8")
    for item_type, (_title, slug) in ITEM_TYPES.items():
        (ITEM_OUT / "by-type" / f"{slug}.md").write_text(item_type_page(item_type, items), encoding="utf-8")
    (ITEM_OUT / "boosters.md").write_text(
        filtered_item_page(
            "Magic Path Booster一覧",
            "装備時にMagic Pathを上昇させるItemです。Booster chainの攻略上の意味は手書き記事を参照してください。",
            [item for item in items if item["boosters"] != "—"],
        ),
        encoding="utf-8",
    )
    (ITEM_OUT / "research.md").write_text(
        filtered_item_page(
            "Research Item一覧",
            "Research bonusを持つItemです。Forge turnとGemの回収計算は手書き攻略で扱います。",
            [item for item in items if int(item["research"]) != 0],
        ),
        encoding="utf-8",
    )
    (ITEM_OUT / "resistance.md").write_text(
        filtered_item_page(
            "Resistance・MR Item一覧",
            "Elemental / Poison / Acid resistance、MR、Antimagicを持つItemです。",
            [item for item in items if bool(item["has_resistance"])],
        ),
        encoding="utf-8",
    )
    (ITEM_OUT / "utility.md").write_text(
        filtered_item_page(
            "Utility Item一覧",
            "Reinvigoration、Leadership、Forge、Blood Search、移動、偵察、Siegeなど戦闘外・支援用途を持つItemです。",
            [item for item in items if bool(item["has_utility"])],
        ),
        encoding="utf-8",
    )
    (ITEM_OUT / "unforgeable.md").write_text(
        filtered_item_page(
            "Unforgeable・Artifact一覧",
            "通常のConstruction研究とForge Itemでは作成できないItemです。入手法はArtifact、Event、Arena、国家固有などItemごとに異なります。",
            [item for item in items if int(item["const"]) == 12],
        ),
        encoding="utf-8",
    )


def main() -> None:
    args = parse_args()
    paths = {name: source(name, args.refresh, args.offline) for name in FILES}
    spells = spell_rows(paths)
    items = item_rows(paths)
    write_pages(spells, items)

    school_count = Counter(int(spell["school"]) for spell in spells)
    item_type_count = Counter(str(item["type"]) for item in items)
    print(f"generated spell records: {len(spells)}")
    print("spell schools:", ", ".join(f"{SCHOOLS[key][0]}={school_count[key]}" for key in SCHOOLS))
    print(f"generated item records: {len(items)}")
    print("item types:", ", ".join(f"{ITEM_TYPES[key][0]}={item_type_count[key]}" for key in ITEM_TYPES))


if __name__ == "__main__":
    main()
