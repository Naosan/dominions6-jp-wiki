from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass

from generate_recruitment_data import num


NEGATIVE_MONSTER_POOLS = {
    -2: "Longdead",
    -3: "Soulless（corpses required）",
    -4: "Ghoul",
    -5: "Random animal",
    -6: "Lesser horror",
    -7: "Horror",
    -8: "Doom Horror",
    -9: "Random bug",
    -10: "Random good crossbreed",
    -11: "Random bad crossbreed",
    -12: "Random crossbreed（3% good）",
    -13: "Random hero",
    -14: "Random dungeon monster",
    -15: "Soulless",
    -16: "Random yazad",
    -17: "Random yata",
    -18: "Soul trap ghost",
    -19: "Lion of strange color",
    -20: "Random bird",
    -21: "Random directional dwarf",
    -22: "Random size 5 elemental",
    -23: "Random scorpion",
    -24: "Lesser horror",
    -25: "Horror",
    -26: "Fayfolk",
}


@dataclass(frozen=True)
class FieldSpec:
    kind: str
    category: str
    timing: str
    amount: str
    condition: str = ""
    companion: str = ""
    note: str = ""


EXACT_TARGET_FIELDS: dict[str, FieldSpec] = {
    "domsummon": FieldSpec(
        "Strategic Spawn", "Dominion", "毎月・friendly dominion内",
        "Dominion strength sided open-ended roll",
        note="Official #domsummon",
    ),
    "domsummon2": FieldSpec(
        "Strategic Spawn", "Dominion", "毎月・friendly dominion内",
        "#domsummonの1/2効率",
        note="Official #domsummon2",
    ),
    "domsummon20": FieldSpec(
        "Strategic Spawn", "Dominion", "毎月・friendly dominion内",
        "#domsummonの1/20効率",
        note="Official #domsummon20",
    ),
    "raredomsummon": FieldSpec(
        "Strategic Spawn", "Dominion", "毎月・friendly dominion内",
        "8%で1体",
        note="Official #raredomsummon",
    ),
    "templetrainer": FieldSpec(
        "Strategic Spawn", "Temple", "Temple provinceでspecial order",
        "1体/turn（同一Temple provinceでは1 Commander）",
        note="Official #templetrainer",
    ),
    "makemonster": FieldSpec(
        "Strategic Spawn", "Special order", "special order・毎月",
        "companion", companion="n_makemonster",
        note="Official #makemonsters1...5",
    ),
    "summon": FieldSpec(
        "Strategic Spawn", "Automatic monthly", "自動・毎月",
        "companion", companion="n_summon",
        note="Official #summon1...5",
    ),
    "summon5": FieldSpec(
        "Strategic Spawn", "Automatic monthly", "自動・毎月",
        "5体",
        note="Inspector field corresponding to monthly summon",
    ),
    "autosum": FieldSpec(
        "Strategic Spawn", "Automatic monthly", "自動・毎月",
        "companion", companion="n_autosum",
        note="Inspector/internal automatic summon field",
    ),
    "coldsummon": FieldSpec(
        "Strategic Spawn", "Scale-conditioned", "毎月",
        "1体（抽出表示）", condition="Cold条件",
        note="Inspector/internal scale-conditioned summon field",
    ),
    "turmoilsummon": FieldSpec(
        "Strategic Spawn", "Scale-conditioned", "毎月",
        "1体（抽出表示）", condition="Turmoil条件",
        note="Inspector/internal scale-conditioned summon field",
    ),
    "ownsmonrec": FieldSpec(
        "Recruit Unlock", "Recruit condition", "Ownerがsource Unitを所有",
        "Recruit解禁", condition="source Unitを所有",
        note="Inspector field #ownsmonrec",
    ),
    "monpresentrec": FieldSpec(
        "Recruit Unlock", "Recruit condition", "source Unitがprovinceに存在",
        "Recruit解禁", condition="source Unitがprovinceに存在",
        note="Inspector field #monpresentrec",
    ),
    "slaver": FieldSpec(
        "Slave Capture", "Strategic order", "毎月",
        "1d6+4 open-ended（slaverbonusで修正）",
        note="Official #slaver",
    ),
    "mummify": FieldSpec(
        "Conversion", "Mummification", "mummify処理",
        "指定Unitへ変換",
        note="Inspector mummify target",
    ),
    "mummification": FieldSpec(
        "Conversion", "Mummification", "partner mummification",
        "指定Unitへ変換",
        note="Inspector mummification partner",
    ),
    "twiceborn": FieldSpec(
        "Conversion", "Twiceborn", "Twiceborn ritual後の復活",
        "指定Unitへ変換",
        note="Official #twiceborn",
    ),
    "lich": FieldSpec(
        "Conversion", "Lich transformation", "Lich化",
        "指定Unitへ変換",
        note="Official #lich",
    ),
    "animatemnr": FieldSpec(
        "Conversion", "Animate", "Animate Tree等の処理",
        "指定Unitへ変換",
        note="Official #animated / Inspector animatemnr",
    ),
    "raiseshape": FieldSpec(
        "Conversion", "Raise", "Raise処理",
        "指定Unitへ変換",
        note="Inspector raiseshape",
    ),
}


ABILITY_FIELDS: dict[str, tuple[str, str, str]] = {
    "reanimator": ("Reanimation", "Passive corpse reanimation", "自動で毎Turnこの数のcorpseをreanimate"),
    "preanimator": ("Reanimation", "Priest reanimation", "Priestとしてundeadをraise可能"),
    "dreanimator": ("Reanimation", "Death reanimation", "Death-based reanimation能力"),
    "raiseonkill": ("Reanimation", "Raise on kill", "倒した相手をSoullessとしてraiseする確率"),
    "onisummon": ("Freespawn", "Oni attraction", "Unrest/Turmoilに応じたKo-Oni attraction chance modifier"),
    "ivylord": ("Summon bonus", "Ivy Lord", "Vine Man系召喚への追加数"),
    "dragonlord": ("Summon bonus", "Dragon Lord", "Drake系召喚への追加数"),
    "lamialord": ("Summon bonus", "Lamia Lord", "Lamia系召喚への追加数"),
    "corpselord": ("Summon bonus", "Corpse Lord", "Corpse Man生成への追加数"),
    "faysummon": ("Summon bonus", "Fay summon bonus", "Fayfolk系召喚への追加数"),
    "fireelementals": ("Summon bonus", "Fire elemental bonus", "召喚Fire ElementalのSize bonus"),
    "airelementals": ("Summon bonus", "Air elemental bonus", "召喚Air ElementalのSize bonus"),
    "waterelementals": ("Summon bonus", "Water elemental bonus", "召喚Water ElementalのSize bonus"),
    "earthelementals": ("Summon bonus", "Earth elemental bonus", "召喚Earth ElementalのSize bonus"),
}


NATION_GENERATION_COMMANDS: dict[str, tuple[str, str]] = {
    "autoundead": ("Dominion Freespawn", "DominionがUndeadを自動生成"),
    "guardspirit": ("Battle summon", "Priestが戦闘時にGuardian Spiritを得る可能性"),
    "priestreanim": ("Reanimation", "全Priestがreanimpriest相当"),
    "undeadreanim": ("Reanimation", "全Undead Priestがreanimpriest相当"),
    "horsereanim": ("Reanimation", "H3+ PriestがLongdead Horsemanをreanimate"),
    "wightreanim": ("Reanimation", "H4+ PriestがLictorをreanimate"),
    "tombwyrmreanim": ("Reanimation", "C'tis系特殊Undeadをreanimate"),
    "manikinreanim": ("Reanimation", "Carrion Beast系をreanimate"),
    "supayareanim": ("Reanimation", "Supaya系をreanimate"),
    "greekreanim": ("Reanimation", "Greek Ghost系をreanimate"),
    "ghostreanim": ("Reanimation", "Ghost系をreanimate"),
}


def _value(row: dict[str, str], field: str) -> int:
    return num(row, field)


def _companion_amount(row: dict[str, str], spec: FieldSpec) -> str:
    if spec.amount != "companion":
        return spec.amount
    value = _value(row, spec.companion)
    return f"{value}体" if value > 0 else "1体（companion countなし）"


def _battle_spec(field: str) -> FieldSpec | None:
    match = re.fullmatch(r"batstartsum(?P<amount>[1-5]|1d3|[1-9]d6)(?:_\d+)?", field)
    if match:
        amount = match.group("amount")
        return FieldSpec(
            "Battle Spawn", "Battle start", "戦闘開始時", f"{amount}体",
            note="Official #batstartsum command",
        )
    match = re.fullmatch(r"battlesum(?P<amount>[1-5]|1d2|1d3|warm)(?:_\d+)?", field)
    if match:
        amount = match.group("amount")
        if amount in {"1", "2", "3", "4", "5"}:
            text = f"0–{amount}体/round"
        elif amount == "1d2":
            text = "1–2体/round"
        elif amount == "1d3":
            text = "1–3体/round"
        else:
            text = "1–4−Cold scale体/round（最低・上限は公式説明参照）"
        return FieldSpec(
            "Battle Spawn", "Per-round battle summon", "各Combat round", text,
            condition="Warm/Cold scale" if amount == "warm" else "",
            note="Official #battlesum command",
        )
    return None


def _field_spec(field: str) -> FieldSpec | None:
    return EXACT_TARGET_FIELDS.get(field) or _battle_spec(field)


def _target_text(raw_target: int, units: dict[int, dict[str, str]]) -> tuple[str, str]:
    if raw_target in units:
        return (units[raw_target].get("name") or "(unnamed)", "fixed-unit")
    if raw_target in NEGATIVE_MONSTER_POOLS:
        return (NEGATIVE_MONSTER_POOLS[raw_target], "negative-pool")
    if raw_target <= -1000:
        return (f"Montag pool {abs(raw_target)}", "montag")
    return (f"Unresolved target {raw_target}", "unresolved")


def build_unit_generation(units: dict[int, dict[str, str]]):
    outgoing: dict[int, list[dict[str, object]]] = defaultdict(list)
    incoming: dict[int, list[dict[str, object]]] = defaultdict(list)
    abilities: dict[int, list[dict[str, object]]] = defaultdict(list)
    unresolved: list[tuple[int, str, str, int, str]] = []
    random_targets: list[dict[str, object]] = []
    field_counts: dict[str, int] = defaultdict(int)
    seen: set[tuple[int, str, int]] = set()

    for source_id, row in units.items():
        source_name = row.get("name") or "(unnamed)"
        for field, raw in row.items():
            if raw in (None, "", "0", "0.0"):
                continue
            spec = _field_spec(field)
            if spec is None:
                continue
            raw_target = _value(row, field)
            if raw_target == 0:
                continue
            key = (source_id, field, raw_target)
            if key in seen:
                continue
            seen.add(key)
            field_counts[field] += 1
            target_name, confidence = _target_text(raw_target, units)
            relation = {
                "kind": spec.kind,
                "category": spec.category,
                "source_id": source_id,
                "source": source_name,
                "target_id": raw_target if raw_target in units else 0,
                "target": target_name,
                "raw_target": raw_target,
                "field": field,
                "timing": spec.timing,
                "amount": _companion_amount(row, spec),
                "condition": spec.condition,
                "note": spec.note,
                "confidence": confidence,
            }
            if field == "slaver" and _value(row, "slaverbonus"):
                relation["amount"] = f"1d6+4 open-ended; modifier {_value(row, 'slaverbonus'):+d}"
            outgoing[source_id].append(relation)
            if raw_target in units:
                incoming[raw_target].append(relation)
            elif confidence in {"negative-pool", "montag"}:
                random_targets.append(relation)
            else:
                unresolved.append((source_id, source_name, field, raw_target, spec.kind))

        for field, (category, label, description) in ABILITY_FIELDS.items():
            value = _value(row, field)
            if value == 0:
                continue
            abilities[source_id].append(
                {
                    "category": category,
                    "field": field,
                    "label": label,
                    "value": value,
                    "description": description,
                }
            )

    return {
        "outgoing": outgoing,
        "incoming": incoming,
        "abilities": abilities,
        "random_targets": random_targets,
        "unresolved": unresolved,
        "field_counts": dict(sorted(field_counts.items())),
    }


DIRECT_SHAPE_FIELDS: dict[str, str] = {
    "firstshape": "Natural Shape",
    "secondshape": "Wounded Shape",
    "shapechange": "Shape Change",
    "secondtmpshape": "Dying / Temporary Shape",
    "landshape": "Land Shape",
    "watershape": "Water Shape",
    "forestshape": "Forest Shape",
    "plainshape": "Normal / Plain Shape",
    "prophetshape": "Prophet Shape",
    "homeshape": "Home Province Shape",
    "foreignshape": "Foreign Province Shape",
    "domshape": "Friendly Dominion Shape",
    "notdomshape": "Outside Friendly Dominion Shape",
    "springshape": "Spring Shape",
    "summershape": "Summer Shape",
    "autumnshape": "Autumn Shape",
    "wintershape": "Winter Shape",
    "battleshape": "Battle Shape",
    "worldshape": "World / Non-battle Shape",
    "twiceborn": "Twiceborn Shape",
    "lich": "Lich Shape",
    "animatemnr": "Animated Shape",
    "raiseshape": "Raised Shape",
}


def build_extended_shape_relations(units: dict[int, dict[str, str]]):
    outgoing: dict[int, list[dict[str, object]]] = defaultdict(list)
    incoming: dict[int, list[dict[str, object]]] = defaultdict(list)
    unresolved: list[tuple[int, str, str, int]] = []
    seen: set[tuple[int, int, str]] = set()

    def add(source_id: int, field: str, label: str, target_id: int) -> None:
        if target_id <= 0 or target_id == source_id:
            return
        source = units[source_id]
        if target_id not in units:
            unresolved.append((source_id, source.get("name") or "(unnamed)", field, target_id))
            return
        key = (source_id, target_id, field)
        if key in seen:
            return
        seen.add(key)
        relation = {
            "field": field,
            "label": label,
            "source_id": source_id,
            "source": source.get("name") or "(unnamed)",
            "target_id": target_id,
            "target": units[target_id].get("name") or "(unnamed)",
        }
        outgoing[source_id].append(relation)
        incoming[target_id].append(relation)

    for source_id, row in units.items():
        for field, label in DIRECT_SHAPE_FIELDS.items():
            add(source_id, field, label, _value(row, field))

        # xpshape/labxpshape store the XP threshold; the target is xpshapemon
        # or, by the official default rule, the next Unit ID.
        xp_target = _value(row, "xpshapemon") or source_id + 1
        if _value(row, "xpshape") > 0:
            add(source_id, "xpshape", "Experience Shape", xp_target)
        if _value(row, "labxpshape") > 0:
            add(source_id, "labxpshape", "Experience Shape（Lab required）", xp_target)

        # Hydra-style HP thresholds use the adjacent Unit record.
        if _value(row, "growhp") > 0:
            add(source_id, "growhp", "Grow above HP threshold", source_id - 1)
        if _value(row, "shrinkhp") > 0:
            add(source_id, "shrinkhp", "Shrink below HP threshold", source_id + 1)

    return outgoing, incoming, unresolved


def _attribute_command(name: str) -> str:
    match = re.search(r"\{Ntn:\s*#([a-z0-9_]+)", name or "", re.I)
    return match.group(1).lower() if match else ""


def build_nation_generation(
    attribute_rows: list[dict[str, str]],
    key_rows: list[dict[str, str]],
    nation_rows: list[dict[str, object]],
    units: dict[int, dict[str, str]],
):
    commands = {
        num(row, "number"): _attribute_command(row.get("name") or "")
        for row in key_rows
        if _attribute_command(row.get("name") or "")
    }
    nations = {int(row["id"]): row for row in nation_rows}
    abilities: list[dict[str, object]] = []
    incoming: dict[int, list[dict[str, object]]] = defaultdict(list)
    unresolved: list[tuple[int, str, str, int]] = []
    seen: set[tuple[int, int, int]] = set()

    for row in attribute_rows:
        nation_id = num(row, "nation_number")
        attribute = num(row, "attribute")
        raw = num(row, "raw_value")
        command = commands.get(attribute, "")
        if command not in NATION_GENERATION_COMMANDS or nation_id not in nations:
            continue
        key = (nation_id, attribute, raw)
        if key in seen:
            continue
        seen.add(key)
        nation = nations[nation_id]
        category, description = NATION_GENERATION_COMMANDS[command]
        relation = {
            "kind": "Nation Spawn" if command == "guardspirit" else "Nation Ability",
            "category": category,
            "command": command,
            "attribute": attribute,
            "raw_value": raw,
            "nation_id": nation_id,
            "nation": nation["name"],
            "era": nation["code"],
            "directory": nation["dir"],
            "slug": nation["slug"],
            "description": description,
            "target_id": 0,
            "target": "—",
            "confidence": "explicit-attribute",
        }
        if command == "guardspirit":
            target, confidence = _target_text(raw, units)
            relation["target"] = target
            relation["confidence"] = confidence
            if raw in units:
                relation["target_id"] = raw
                incoming[raw].append(relation)
            elif confidence == "unresolved":
                unresolved.append((nation_id, str(nation["name"]), command, raw))
        abilities.append(relation)

    return {
        "abilities": abilities,
        "incoming": incoming,
        "unresolved": unresolved,
        "attribute_commands": commands,
    }
