from __future__ import annotations

import math
from collections import Counter, defaultdict

from combat_data_common import ARMOR_OUT, COMMIT, TYPE_NAMES, TYPE_SLUGS, clean_label, esc, num
from combat_data_weapons import ATTRIBUTE_LABELS


def parse_armor_attributes(rows, attribute_names):
    out = defaultdict(list)
    for row in rows:
        aid, attr = num(row, "armor_number"), num(row, "attribute")
        if not aid or not attr:
            continue
        label = ATTRIBUTE_LABELS.get(attr) or clean_label(attribute_names.get(attr, ""))
        if label and "unknown attribute" not in label.lower():
            out[aid].append((attr, num(row, "raw_value"), label))
    return out


def parse_armors(rows, protections, attrs):
    zones = defaultdict(dict)
    for row in protections:
        zones[num(row, "armor_number")][num(row, "zone_number")] = num(row, "protection")
    out = []
    for row in rows:
        aid, atype = num(row, "id"), num(row, "type")
        if not aid or atype not in TYPE_NAMES:
            continue
        z = zones.get(aid, {})
        head, torso, upper, lower = z.get(1, 0), z.get(2, 0), z.get(3, 0), z.get(4, 0)
        shield, general = z.get(5, 0), z.get(6, 0)
        body = math.floor((torso + (upper + lower) / 2) / 2) if torso else 0
        body, head = body + general, head + general
        raw_def, enc = num(row, "def"), num(row, "enc")
        magic = any(attr == 557 for attr, _raw, _label in attrs.get(aid, []))
        parry, defense, move = "—", raw_def, "—"
        if atype == 4:
            parry, defense = raw_def + enc, -enc
        elif atype == 5:
            move = min(max(enc - (1 if magic else 0), 0) * 2, 6)
            for attr, raw, _label in attrs.get(aid, []):
                if attr == 582 and raw != -99:
                    move = raw
        labels = []
        for _attr, raw, label in attrs.get(aid, []):
            if raw not in (0, 1, -99):
                label = f"{label} {raw}"
            if label not in labels:
                labels.append(label)
        out.append({"id": aid, "name": row.get("name") or "(unnamed)", "type": atype,
                    "body": body or "—", "head": head or "—", "shield": shield or "—",
                    "parry": parry, "defense": defense, "enc": enc, "move": move,
                    "rcost": num(row, "rcost"), "attributes": labels})
    return sorted(out, key=lambda x: (x["type"], x["id"]))


def table(items, atype: int) -> str:
    if atype == 4:
        out = ["| Shield | ID | Shield Prot | Parry | Def penalty | Enc | Res | Attributes |",
               "|---|---:|---:|---:|---:|---:|---:|---|"]
        for x in items:
            out.append(f"| {esc(x['name'])} | {x['id']} | {x['shield']} | {x['parry']} | {x['defense']:+d} | {x['enc']} | {x['rcost']} | {esc(', '.join(x['attributes']) or '—')} |")
    elif atype == 5:
        out = ["| Armor | ID | Body Prot | Def | Enc | Map move penalty | Res | Attributes |",
               "|---|---:|---:|---:|---:|---:|---:|---|"]
        for x in items:
            out.append(f"| {esc(x['name'])} | {x['id']} | {x['body']} | {x['defense']:+d} | {x['enc']} | {x['move']} | {x['rcost']} | {esc(', '.join(x['attributes']) or '—')} |")
    elif atype == 6:
        out = ["| Helmet | ID | Head Prot | Def | Enc | Res | Attributes |",
               "|---|---:|---:|---:|---:|---:|---|"]
        for x in items:
            out.append(f"| {esc(x['name'])} | {x['id']} | {x['head']} | {x['defense']:+d} | {x['enc']} | {x['rcost']} | {esc(', '.join(x['attributes']) or '—')} |")
    else:
        out = ["| Armor | ID | Body Prot | Head Prot | Def | Enc | Res | Attributes |",
               "|---|---:|---:|---:|---:|---:|---:|---|"]
        for x in items:
            out.append(f"| {esc(x['name'])} | {x['id']} | {x['body']} | {x['head']} | {x['defense']:+d} | {x['enc']} | {x['rcost']} | {esc(', '.join(x['attributes']) or '—')} |")
    return "\n".join(out) + "\n"


def page(title, intro, items, atype):
    note = ""
    if atype == 4:
        note = """\n## Shieldの値\n\n- **Parry**は盾で攻撃を受ける能力。\n- **Def penalty**は盾の重さによる通常Defenceへの不利。\n- Shield Hit時はShield Protectionが関与する。\n"""
    elif atype == 5:
        note = """\n## Body Protection\n\nTorso / Upper / Lower zoneからInspectorと同じ式で表示用Body Protectionを算出しています。Natural Protection、Helmet、Shield、Buffは含みません。\n"""
    return f'''---
title: "{title}"
status: generated
verified_version: "6.35"
generated_from: "dom6inspector {COMMIT}"
---

# {title}

{intro}

!!! info "自動生成データ"
    防具単体の値です。UnitのNatural Protection、Mount、Bless、魔法Buff等は含みません。

{table(items, atype)}
{note}
[防具データ索引へ戻る](index.md) · [戦闘ルール](../../../basics/combat-rules.md) · [武器と盾](../../../basics/weapons-and-shields.md)
'''


def write_armor_pages(armors):
    ARMOR_OUT.mkdir(parents=True, exist_ok=True)
    specs = (
        (4, "盾データ", "Shield Protection、Parry、Defence penalty、Encumbranceを比較します。"),
        (5, "胴鎧データ", "Body Protection、Defence、Encumbrance、Map move penaltyを比較します。"),
        (6, "兜データ", "Head Protection、Defence、Encumbranceを比較します。"),
        (8, "Misc防具データ", "General Protection等を持つMisc armor recordです。"),
    )
    counts = Counter(x["type"] for x in armors)
    for atype, title, intro in specs:
        items = [x for x in armors if x["type"] == atype]
        (ARMOR_OUT / f"{TYPE_SLUGS[atype]}.md").write_text(page(title, intro, items, atype), encoding="utf-8")
    (ARMOR_OUT / "index.md").write_text(f'''---
title: "防具データ索引"
status: generated
verified_version: "6.35"
generated_from: "dom6inspector {COMMIT}"
---

# 防具データ索引

| 区分 | 件数 | ページ |
|---|---:|---|
| 盾 | {counts[4]} | [盾](shields.md) |
| 胴鎧 | {counts[5]} | [胴鎧](body-armor.md) |
| 兜 | {counts[6]} | [兜](helmets.md) |
| Misc防具 | {counts[8]} | [Misc防具](misc-armor.md) |

防具表は装備単体の値です。高ProtectionでもAN、Poison、Fatigue、MR攻撃等には別対策が必要です。

[戦闘ルール](../../../basics/combat-rules.md) · [武器と盾](../../../basics/weapons-and-shields.md)
''', encoding="utf-8")
    return dict(counts)
