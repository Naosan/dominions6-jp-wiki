from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

from combat_data_common import num
from recruitment_loadouts import (
    armor_summary,
    equipment_profile,
    unit_armor_ids,
    unit_weapon_ids,
    weapon_summary,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "data" / "equipment-usage"
WEAPON_OUT = OUT / "weapons"
ARMOR_OUT = OUT / "armor"
PROFILE_OUT = OUT / "profiles"

ERA_ORDER = {"EA": 0, "MA": 1, "LA": 2}
MAP_SPECS = (
    ("ft", "Fort troop", "Troop"),
    ("fl", "Fort commander", "Commander"),
    ("nt", "Fort不要・地形・外国 troop", "Troop"),
    ("nl", "Fort不要・地形・外国 commander", "Commander"),
    ("ct", "Coastal troop", "Troop"),
    ("cl", "Coastal commander", "Commander"),
)
ARMOR_TYPES = {4: "盾", 5: "胴鎧", 6: "兜", 8: "Misc防具"}


def esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def cap(row: dict[str, str]) -> bool:
    return row.get("capitalhome") not in (None, "", "0", "0.0")


def recruit_page_link(nation: dict[str, object], depth: str = "../../") -> str:
    return f"{depth}recruitment/{nation['dir']}/{nation['slug']}.md"


def collect_recruits(
    nation_rows: list[dict[str, object]],
    units: dict[int, dict[str, str]],
    maps,
) -> list[dict[str, object]]:
    nation_by_id = {int(nation["id"]): nation for nation in nation_rows}
    merged: dict[tuple[int, int], dict[str, object]] = {}

    for map_key, source_label, role in MAP_SPECS:
        for nation_id, unit_ids in maps[map_key].items():
            nation = nation_by_id.get(int(nation_id))
            if nation is None:
                continue
            for unit_id in unit_ids:
                row = units.get(int(unit_id))
                if row is None:
                    raise KeyError(f"mapped unit {unit_id} missing from BaseU")
                key = (int(nation_id), int(unit_id))
                record = merged.setdefault(
                    key,
                    {
                        "nation": nation,
                        "row": row,
                        "sources": set(),
                        "roles": set(),
                    },
                )
                record["sources"].add(source_label)
                record["roles"].add(role)

    return sorted(
        merged.values(),
        key=lambda record: (
            ERA_ORDER.get(str(record["nation"]["code"]), 9),
            int(record["nation"]["id"]),
            str(record["row"].get("name") or ""),
            int(record["row"]["id"]),
        ),
    )


def use_record(
    recruit: dict[str, object],
    holder: dict[str, str],
    holder_kind: str,
    count: int,
) -> dict[str, object]:
    return {
        "nation": recruit["nation"],
        "recruit": recruit["row"],
        "holder": holder,
        "holder_kind": holder_kind,
        "sources": sorted(recruit["sources"]),
        "roles": sorted(recruit["roles"]),
        "count": count,
    }


def collect_usage(
    recruits: list[dict[str, object]],
    units: dict[int, dict[str, str]],
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
):
    weapon_users: dict[int, list[dict[str, object]]] = defaultdict(list)
    armor_users: dict[int, list[dict[str, object]]] = defaultdict(list)

    for recruit in recruits:
        rider = recruit["row"]
        holders: list[tuple[str, dict[str, str]]] = [("Unit", rider)]
        mount_id = num(rider, "mountmnr")
        if mount_id:
            mount = units.get(mount_id)
            if mount is None:
                raise KeyError(f"mount {mount_id} missing for unit {rider['id']}")
            holders.append(("Mount", mount))

        for holder_kind, holder in holders:
            for weapon_id, count in Counter(unit_weapon_ids(holder)).items():
                if weapon_id not in weapons:
                    raise KeyError(f"weapon {weapon_id} missing for holder {holder['id']}")
                weapon_users[weapon_id].append(use_record(recruit, holder, holder_kind, count))
            for armor_id, count in Counter(unit_armor_ids(holder)).items():
                if armor_id not in armors:
                    raise KeyError(f"armor {armor_id} missing for holder {holder['id']}")
                armor_users[armor_id].append(use_record(recruit, holder, holder_kind, count))

    return weapon_users, armor_users


def usage_sort_key(use: dict[str, object]):
    nation = use["nation"]
    recruit = use["recruit"]
    holder = use["holder"]
    return (
        ERA_ORDER.get(str(nation["code"]), 9),
        int(nation["id"]),
        str(recruit.get("name") or ""),
        int(recruit["id"]),
        0 if use["holder_kind"] == "Unit" else 1,
        str(holder.get("name") or ""),
        int(holder["id"]),
    )


def usage_table(users: list[dict[str, object]]) -> str:
    if not users:
        return "Recruit可能UnitおよびそのMountによる使用例はありません。\n"
    out = [
        "| Era | Nation | Recruit | ID | Holder | Recruit source | Cap-only | Count |",
        "|---|---|---|---:|---|---|---|---:|",
    ]
    for use in sorted(users, key=usage_sort_key):
        nation = use["nation"]
        recruit = use["recruit"]
        holder = use["holder"]
        nation_label = f"{nation['code']} {nation['name']}"
        nation_link = recruit_page_link(nation)
        holder_text = "Unit"
        if use["holder_kind"] == "Mount":
            holder_text = f"Mount: {holder.get('name') or '(unnamed)'} #{holder['id']}"
        out.append(
            "| {era} | [{nation}]({link}) | {recruit} | {unit_id} | {holder} | "
            "{source} | {cap} | {count} |".format(
                era=nation["code"],
                nation=esc(nation_label),
                link=nation_link,
                recruit=esc(recruit.get("name") or "(unnamed)"),
                unit_id=recruit["id"],
                holder=esc(holder_text),
                source=esc(", ".join(use["sources"])),
                cap="Yes" if cap(recruit) else "No",
                count=use["count"],
            )
        )
    return "\n".join(out) + "\n"


def compact_weapon(item: dict[str, object]) -> str:
    reach = f"Range {item['range']}" if item["class"] == "射撃" else f"Len {item['length']}"
    props = [str(value) for value in item.get("properties", [])]
    types = [str(value) for value in item.get("types", [])]
    key: list[str] = []
    for value in types + props:
        if value in (
            "Slash",
            "Pierce",
            "Blunt",
            "Fire",
            "Cold",
            "Shock",
            "Poison",
            "Acid",
            "両手",
            "AP",
            "AN",
            "Charge",
            "Heavy Charge",
            "盾無視",
            "Defence Negate",
            "MR Negates",
            "Soul Slay",
            "Magic weapon",
            "Nonmagical",
        ) and value not in key:
            key.append(value)
    return f"Dmg {item['damage']}; {reach}; {', '.join(key[:8]) or '—'}"


def compact_armor(item: dict[str, object]) -> str:
    armor_type = int(item["type"])
    if armor_type == 4:
        return f"Shield Prot {item['shield']}; Parry {item['parry']}; Def {int(item['defense']):+d}"
    if armor_type == 5:
        return f"Body Prot {item['body']}; Def {int(item['defense']):+d}; Enc {item['enc']}"
    if armor_type == 6:
        return f"Head Prot {item['head']}; Def {int(item['defense']):+d}; Enc {item['enc']}"
    return f"Body {item['body']}; Head {item['head']}; Enc {item['enc']}"


def detail_header(title: str, commit: str) -> str:
    safe_title = title.replace("\\", "\\\\").replace('"', '\\"')
    return (
        "---\n"
        f'title: "{safe_title}"\n'
        "status: generated\n"
        'verified_version: "6.35"\n'
        f'generated_from: "dom6inspector {commit}"\n'
        "---\n\n"
    )


def unique_nations(users: list[dict[str, object]]) -> int:
    return len({int(use["nation"]["id"]) for use in users})


def unique_recruits(users: list[dict[str, object]]) -> int:
    return len(
        {
            (int(use["nation"]["id"]), int(use["recruit"]["id"]))
            for use in users
        }
    )


def write_weapon_pages(
    weapons: dict[int, dict[str, object]],
    users_by_id: dict[int, list[dict[str, object]]],
    commit: str,
) -> None:
    WEAPON_OUT.mkdir(parents=True, exist_ok=True)
    index = [
        detail_header("Weapon使用者逆引き", commit).rstrip(),
        "",
        "# Weapon使用者逆引き",
        "",
        "全Weapon recordについて、使用するRecruit可能UnitとそのMountを逆引きします。",
        "",
        "| Weapon | ID | Class | Data | Recruit | Nations | Details |",
        "|---|---:|---|---|---:|---:|---|",
    ]

    for weapon_id, item in sorted(weapons.items(), key=lambda pair: (str(pair[1]["name"]), pair[0])):
        users = users_by_id.get(weapon_id, [])
        title = f"{item['name']} #{weapon_id} 使用者"
        page = [
            detail_header(title, commit),
            f"# {title}\n",
            "## Weapon record\n",
            weapon_summary(item) + "\n",
            "## Recruit可能Unit・Mount\n",
            usage_table(users),
            "\n## 読み方\n",
            "- **Holder = Unit** はRecruit本体が装備するWeapon。",
            "- **Holder = Mount** はそのRecruitが騎乗するMount側の攻撃。",
            "- Countは同じHolderが同一Weapon IDを複数参照する場合の数。",
            "- 最終Damage、二刀流Penalty、攻撃順、Bless、Buffは含まない。",
            "",
            "[Weapon使用者索引へ戻る](index.md) · [Weapon data](../../combat/weapons/index.md)",
            "",
        ]
        (WEAPON_OUT / f"{weapon_id}.md").write_text("\n".join(page), encoding="utf-8")
        index.append(
            f"| [{esc(item['name'])}]({weapon_id}.md) | {weapon_id} | {item['class']} | "
            f"{esc(compact_weapon(item))} | {unique_recruits(users)} | "
            f"{unique_nations(users)} | [表示]({weapon_id}.md) |"
        )

    (WEAPON_OUT / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")


def write_armor_pages(
    armors: dict[int, dict[str, object]],
    users_by_id: dict[int, list[dict[str, object]]],
    commit: str,
) -> None:
    ARMOR_OUT.mkdir(parents=True, exist_ok=True)
    index = [
        detail_header("Armor使用者逆引き", commit).rstrip(),
        "",
        "# Armor使用者逆引き",
        "",
        "全Armor recordについて、使用するRecruit可能UnitとそのMountを逆引きします。",
        "",
        "| Armor | ID | Type | Data | Recruit | Nations | Details |",
        "|---|---:|---|---|---:|---:|---|",
    ]

    for armor_id, item in sorted(armors.items(), key=lambda pair: (str(pair[1]["name"]), pair[0])):
        users = users_by_id.get(armor_id, [])
        title = f"{item['name']} #{armor_id} 使用者"
        page = [
            detail_header(title, commit),
            f"# {title}\n",
            "## Armor record\n",
            armor_summary(item) + "\n",
            "## Recruit可能Unit・Mount\n",
            usage_table(users),
            "\n## 読み方\n",
            "- Unit本体とMountのArmor / Bardingを分離して表示する。",
            "- Shield Protection、Parry、通常Defenceは別の値。",
            "- UnitのNatural Protection、Bless、Buff、Mountとの合算は含まない。",
            "",
            "[Armor使用者索引へ戻る](index.md) · [Armor data](../../combat/armor/index.md)",
            "",
        ]
        (ARMOR_OUT / f"{armor_id}.md").write_text("\n".join(page), encoding="utf-8")
        index.append(
            f"| [{esc(item['name'])}]({armor_id}.md) | {armor_id} | "
            f"{ARMOR_TYPES.get(int(item['type']), item['type'])} | "
            f"{esc(compact_armor(item))} | {unique_recruits(users)} | "
            f"{unique_nations(users)} | [表示]({armor_id}.md) |"
        )

    (ARMOR_OUT / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")


def direct_weapons(
    recruit: dict[str, object],
    weapons: dict[int, dict[str, object]],
) -> list[dict[str, object]]:
    return [
        weapons[weapon_id]
        for weapon_id in unit_weapon_ids(recruit["row"])
        if weapon_id in weapons
    ]


def direct_armors(
    recruit: dict[str, object],
    armors: dict[int, dict[str, object]],
) -> list[dict[str, object]]:
    return [
        armors[armor_id]
        for armor_id in unit_armor_ids(recruit["row"])
        if armor_id in armors
    ]


def profile_details(
    recruit: dict[str, object],
    key: str,
    units: dict[int, dict[str, str]],
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
) -> str:
    weapon_rows = direct_weapons(recruit, weapons)
    armor_rows = direct_armors(recruit, armors)
    if key == "shield":
        return "; ".join(
            f"{item['name']} #{item['id']} (Prot {item['shield']}, Parry {item['parry']})"
            for item in armor_rows
            if int(item["type"]) == 4
        )
    if key == "mounted":
        mount_id = num(recruit["row"], "mountmnr")
        if mount_id and mount_id in units:
            mount = units[mount_id]
            return f"{mount.get('name') or '(unnamed)'} #{mount_id}"
        return "Mounted flag"
    labels = {
        "two-handed": "両手",
        "ap": "AP",
        "an": "AN",
        "charge": "Charge",
    }
    if key == "ranged":
        selected = [item for item in weapon_rows if item["class"] == "射撃"]
    else:
        label = labels[key]
        selected = [item for item in weapon_rows if label in item.get("properties", [])]
    return "; ".join(f"{item['name']} #{item['id']}" for item in selected)


def profile_match(
    recruit: dict[str, object],
    key: str,
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
) -> bool:
    profile = equipment_profile(recruit["row"], weapons, armors)
    mapping = {
        "shield": "盾持ち",
        "two-handed": "両手武器",
        "ranged": "射撃",
        "ap": "AP",
        "an": "AN",
        "charge": "Charge",
        "mounted": "騎乗",
    }
    return mapping[key] in profile


def recruit_profile_table(
    recruits: list[dict[str, object]],
    key: str,
    units: dict[int, dict[str, str]],
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
) -> str:
    selected = [record for record in recruits if profile_match(record, key, weapons, armors)]
    if not selected:
        return "該当Recruitなし。\n"
    out = [
        "| Era | Nation | Recruit | ID | Role | Source | Cap-only | Equipment |",
        "|---|---|---|---:|---|---|---|---|",
    ]
    for record in selected:
        nation = record["nation"]
        row = record["row"]
        out.append(
            f"| {nation['code']} | "
            f"[{esc(nation['code'])} {esc(nation['name'])}]({recruit_page_link(nation)}) | "
            f"{esc(row.get('name') or '(unnamed)')} | {row['id']} | "
            f"{esc(', '.join(sorted(record['roles'])))} | "
            f"{esc(', '.join(sorted(record['sources'])))} | "
            f"{'Yes' if cap(row) else 'No'} | "
            f"{esc(profile_details(record, key, units, weapons, armors) or '—')} |"
        )
    return "\n".join(out) + "\n"


def write_profile_pages(
    recruits: list[dict[str, object]],
    units: dict[int, dict[str, str]],
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
    commit: str,
) -> dict[str, int]:
    PROFILE_OUT.mkdir(parents=True, exist_ok=True)
    specs = (
        ("shield", "盾を持つRecruit", "Shield recordを直接装備するRecruitです。"),
        ("two-handed", "両手武器Recruit", "Two-handed propertyを持つWeaponを直接装備するRecruitです。"),
        ("ranged", "射撃Recruit", "射撃Weaponを直接装備するRecruitです。"),
        ("ap", "AP武器Recruit", "Armor Piercing Weaponを直接装備するRecruitです。"),
        ("an", "AN武器Recruit", "Armor Negating Weaponを直接装備するRecruitです。"),
        ("charge", "Charge武器Recruit", "Charge Weaponを直接装備するRecruitです。"),
        ("mounted", "騎乗Recruit", "Mount recordまたはMounted flagを持つRecruitです。"),
    )
    counts: dict[str, int] = {}
    index = [
        detail_header("Recruit装備Profile逆引き", commit).rstrip(),
        "",
        "# Recruit装備Profile逆引き",
        "",
        "| Profile | Recruit数 | Page |",
        "|---|---:|---|",
    ]
    for key, title, intro in specs:
        selected_count = sum(
            1 for record in recruits if profile_match(record, key, weapons, armors)
        )
        counts[key] = selected_count
        content = (
            detail_header(title, commit)
            + f"# {title}\n\n{intro}\n\n"
            + "!!! info \"Profileの範囲\"\n"
            + "    Recruit本体の直接装備を基準にする。Mount側の攻撃・Bardingは個別Weapon / Armor使用者ページで確認する。\n\n"
            + recruit_profile_table(recruits, key, units, weapons, armors)
            + "\n[Profile索引へ戻る](index.md) · [国家別比較](../nations.md)\n"
        )
        (PROFILE_OUT / f"{key}.md").write_text(content, encoding="utf-8")
        index.append(f"| [{title}]({key}.md) | {selected_count} | [表示]({key}.md) |")
    (PROFILE_OUT / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    return counts


def write_nation_matrix(
    recruits: list[dict[str, object]],
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
    commit: str,
) -> None:
    by_nation: dict[int, list[dict[str, object]]] = defaultdict(list)
    for recruit in recruits:
        by_nation[int(recruit["nation"]["id"])].append(recruit)

    lines = [
        detail_header("国家別Recruit装備Profile", commit).rstrip(),
        "",
        "# 国家別Recruit装備Profile",
        "",
        "各国家のRecruit recordを、装備Profile別に数えます。同名Unitが複数Recruit条件を持つ場合は一つにまとめます。",
        "",
        "| Era | Nation | Recruit | 盾 | 両手 | 射撃 | AP | AN | Charge | Mounted |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for nation_id, nation_recruits in sorted(
        by_nation.items(),
        key=lambda pair: (
            ERA_ORDER.get(str(pair[1][0]["nation"]["code"]), 9),
            pair[0],
        ),
    ):
        nation = nation_recruits[0]["nation"]
        counts = {
            key: sum(
                1
                for recruit in nation_recruits
                if profile_match(recruit, key, weapons, armors)
            )
            for key in ("shield", "two-handed", "ranged", "ap", "an", "charge", "mounted")
        }
        lines.append(
            f"| {nation['code']} | "
            f"[{esc(nation['name'])}]({recruit_page_link(nation, '../')}) | "
            f"{len(nation_recruits)} | {counts['shield']} | {counts['two-handed']} | "
            f"{counts['ranged']} | {counts['ap']} | {counts['an']} | "
            f"{counts['charge']} | {counts['mounted']} |"
        )
    lines.extend(
        [
            "",
            "## 注意",
            "",
            "- ProfileはWeapon / Armor recordに基づく機械分類で、強さのTier表ではない。",
            "- APやANを持っていてもDamage、Attack、射程、Costが不十分な場合がある。",
            "- Mount側の攻撃属性はこの表へ含めず、個別使用者ページで分離する。",
            "",
            "[装備使用者索引へ戻る](index.md)",
            "",
        ]
    )
    (OUT / "nations.md").write_text("\n".join(lines), encoding="utf-8")


def write_root_index(
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
    weapon_users: dict[int, list[dict[str, object]]],
    armor_users: dict[int, list[dict[str, object]]],
    recruits: list[dict[str, object]],
    profile_counts: dict[str, int],
    commit: str,
) -> None:
    used_weapons = sum(1 for weapon_id in weapons if weapon_users.get(weapon_id))
    used_armors = sum(1 for armor_id in armors if armor_users.get(armor_id))
    content = f'''---
title: "装備使用者逆引き"
status: generated
verified_version: "6.35"
generated_from: "dom6inspector {commit}"
---

# 装備使用者逆引き

Weapon・Armorから、それを使用するvanilla国家のRecruit可能UnitとMountを逆引きします。

## 索引

- [Weapon使用者](weapons/index.md)
- [Armor使用者](armor/index.md)
- [Recruit装備Profile](profiles/index.md)
- [国家別Profile比較](nations.md)
- [Unit装備・Mountの読み方](../unit-loadouts.md)

## 登録範囲

| 項目 | 件数 |
|---|---:|
| Recruit relation | {len(recruits)} |
| 全Weapon record | {len(weapons)} |
| Recruit / Mountが使用するWeapon | {used_weapons} |
| 全Armor record | {len(armors)} |
| Recruit / Mountが使用するArmor | {used_armors} |

## Profile早見表

| Profile | Recruit数 | Page |
|---|---:|---|
| 盾 | {profile_counts['shield']} | [表示](profiles/shield.md) |
| 両手 | {profile_counts['two-handed']} | [表示](profiles/two-handed.md) |
| 射撃 | {profile_counts['ranged']} | [表示](profiles/ranged.md) |
| AP | {profile_counts['ap']} | [表示](profiles/ap.md) |
| AN | {profile_counts['an']} | [表示](profiles/an.md) |
| Charge | {profile_counts['charge']} | [表示](profiles/charge.md) |
| Mounted | {profile_counts['mounted']} | [表示](profiles/mounted.md) |

!!! note "逆引きの範囲"
    Fort、Capital、Fort不要・地形・外国、Coastal Recruitを対象にします。Hero、Event、Freespawn、召喚、Site限定Unitは含みません。

!!! warning "事実索引と攻略評価"
    「その武器を使える」ことと「その兵が強い」ことは同じではありません。Strength、Attack、Cost、Recruitment制限、Bless、Buff、敵の防御層を国家攻略と戦闘記事で確認してください。
'''
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.md").write_text(content, encoding="utf-8")


def write_equipment_usage_indexes(
    nation_rows: list[dict[str, object]],
    units: dict[int, dict[str, str]],
    maps,
    weapons: dict[int, dict[str, object]],
    armors: dict[int, dict[str, object]],
    commit: str,
) -> dict[str, int]:
    recruits = collect_recruits(nation_rows, units, maps)
    weapon_users, armor_users = collect_usage(recruits, units, weapons, armors)

    write_weapon_pages(weapons, weapon_users, commit)
    write_armor_pages(armors, armor_users, commit)
    profile_counts = write_profile_pages(recruits, units, weapons, armors, commit)
    write_nation_matrix(recruits, weapons, armors, commit)
    write_root_index(
        weapons,
        armors,
        weapon_users,
        armor_users,
        recruits,
        profile_counts,
        commit,
    )

    return {
        "recruits": len(recruits),
        "weapon_records": len(weapons),
        "used_weapons": sum(1 for weapon_id in weapons if weapon_users.get(weapon_id)),
        "weapon_relations": sum(len(users) for users in weapon_users.values()),
        "armor_records": len(armors),
        "used_armors": sum(1 for armor_id in armors if armor_users.get(armor_id)),
        "armor_relations": sum(len(users) for users in armor_users.values()),
        **{f"profile_{key}": value for key, value in profile_counts.items()},
    }
