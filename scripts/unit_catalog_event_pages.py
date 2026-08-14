from __future__ import annotations

from collections import defaultdict
from pathlib import Path


EVENT_PAGE_CONFIG = (
    (
        "event-spawns.md",
        "Event Unit・Commander生成",
        {"Event Spawn"},
        "Random EventやStory Eventが直接生成するCommander・Troopを整理します。所有者とTemporary指定を必ず併記します。",
    ),
    (
        "event-transforms.md",
        "Event変身・強制変身",
        {"Event Transform"},
        "Event effectの`transform`と`forcetransform`が参照する固定Unit形態を整理します。",
    ),
    (
        "event-combat.md",
        "Event暗殺・戦闘参加Unit",
        {"Event Combat"},
        "Eventが生成するAssassinとAssassination followerを整理します。ここに載るUnitは、通常の恒久加入を意味しません。",
    ),
)


def _esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def _short(value: object, limit: int = 150) -> str:
    text = str(value if value is not None else "").replace("\n", " ").strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def _event_filename(kind: str) -> str:
    if kind == "Event Transform":
        return "event-transforms.md"
    if kind == "Event Combat":
        return "event-combat.md"
    return "event-spawns.md"


def _event_link(relation: dict[str, object], *, from_unit_page: bool) -> str:
    prefix = "../" if from_unit_page else ""
    filename = _event_filename(str(relation["kind"]))
    return (
        f"[{_esc(relation['event'])}]({prefix}{filename}#event-{int(relation['event_id'])})"
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


def _event_unit_table(relations: list[dict[str, object]]) -> str:
    out = [
        "| Event | Effect | Role | Amount | Owner | Unit lifetime | Rarity | Requirements |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for relation in sorted(
        relations,
        key=lambda item: (int(item["event_id"]), str(item["field"]), int(item["raw_target"])),
    ):
        out.append(
            f"| {_event_link(relation, from_unit_page=True)} | `{_esc(relation['field'])}` | "
            f"{_esc(relation['category'])} | {_esc(relation['amount'])} | "
            f"{_esc(relation['owner'])} | {_esc(relation['temporary'])} | "
            f"{_esc(relation['rarity_text'])} | {_esc(_short(str(relation['requirements']).replace('|', '; '), 120) or '—')} |"
        )
    return "\n".join(out) + "\n"


def _mercenary_unit_table(relations: list[dict[str, object]]) -> str:
    out = [
        "| Company | Role | Count | Era | Level | Minimum pay | Boss | Starting items |",
        "|---|---|---:|---|---:|---:|---|---|",
    ]
    for relation in sorted(
        relations,
        key=lambda item: (int(item["mercenary_id"]), str(item["category"])),
    ):
        items = ", ".join(
            item for item in (str(relation.get("item1") or ""), str(relation.get("item2") or "")) if item
        ) or "—"
        out.append(
            f"| [{_esc(relation['company'])}](../mercenaries.md#mercenary-{int(relation['mercenary_id'])}) | "
            f"{_esc(relation['category'])} | {relation['count']} | {_esc(relation['era'])} | "
            f"{relation['level']} | {relation['minpay']} | {_esc(relation['boss'] or '—')} | {_esc(items)} |"
        )
    return "\n".join(out) + "\n"


def _event_stats(data) -> dict[str, int]:
    counts = defaultdict(int)
    for relation in data["event_relations"]:
        counts[str(relation["kind"])] += 1
    return {
        "events_with_unit_effects": int(data["events_with_unit_effects"]),
        "event_unit_relations": len(data["event_relations"]),
        "event_spawn_relations": counts["Event Spawn"],
        "event_transform_relations": counts["Event Transform"],
        "event_combat_relations": counts["Event Combat"],
        "event_units": len(data["event_incoming"]),
        "event_random_references": len(data["event_random_targets"]),
        "unresolved_event_targets": len(data["event_unresolved"]),
        "mercenary_companies": int(data["mercenary_companies"]),
        "mercenary_relations": len(data["mercenary_relations"]),
        "mercenary_units": len(data["mercenary_incoming"]),
        "unresolved_mercenary_targets": len(data["mercenary_unresolved"]),
    }


def _write_event_page(module, out: Path, data, filename: str, title: str, kinds: set[str], description: str) -> Path:
    selected = [relation for relation in data["event_relations"] if relation["kind"] in kinds]
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
        "| Event | ID | Rarity | Effect | Role | Target | Amount | Owner | Lifetime | Requirements | Description |",
        "|---|---:|---|---|---|---|---|---|---|---|---|",
    ]
    anchored: set[int] = set()
    for relation in sorted(
        selected,
        key=lambda item: (int(item["event_id"]), str(item["field"]), int(item["raw_target"])),
    ):
        event_id = int(relation["event_id"])
        anchor = ""
        if event_id not in anchored:
            anchor = f'<a id="event-{event_id}"></a>'
            anchored.add(event_id)
        target = _target_cell(module, relation)
        requirements = _short(str(relation["requirements"]).replace("|", "; "), 140) or "—"
        description_text = _short(relation["description"], 180) or "—"
        lines.append(
            f"| {anchor}{_esc(relation['event'])} | {event_id} | {_esc(relation['rarity_text'])} | "
            f"`{_esc(relation['field'])}` | {_esc(relation['category'])} | {target} | "
            f"{_esc(relation['amount'])} | {_esc(relation['owner'])} | {_esc(relation['temporary'])} | "
            f"{_esc(requirements)} | {_esc(description_text)} |"
        )
    if not selected:
        lines.append("| — | — | — | — | 該当Relationなし | — | — | — | — | — | — |")
    lines.extend(
        [
            "",
            "`nation -1`はRandom enemy、`nation -2`はProvince ownerです。`tempunits 1`は一時Unitであり、恒久加入とは扱いません。",
            "",
            "[Unit総合索引へ戻る](index.md)",
            "",
        ]
    )
    path = out / filename
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _write_event_random(module, out: Path, data) -> Path:
    lines = [
        "---",
        'title: "Event Random pool・未解決Target"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        "---",
        "",
        "# Event Random pool・未解決Target",
        "",
        "Event effectが負のMonster NumberまたはMontagを参照する場合、単一Unitへは結び付けません。",
        "",
        "## Random pool",
        "",
        "| Event | Effect | Raw target | Pool | Role | Amount | Owner |",
        "|---|---|---:|---|---|---|---|",
    ]
    for relation in sorted(
        data["event_random_targets"],
        key=lambda item: (int(item["event_id"]), str(item["field"]), int(item["raw_target"])),
    ):
        lines.append(
            f"| {_event_link(relation, from_unit_page=False)} | `{_esc(relation['field'])}` | "
            f"{relation['raw_target']} | {_esc(relation['target'])} | {_esc(relation['category'])} | "
            f"{_esc(relation['amount'])} | {_esc(relation['owner'])} |"
        )
    if not data["event_random_targets"]:
        lines.append("| — | — | — | 該当なし | — | — | — |")

    lines.extend(
        [
            "",
            "## 解決不能な正値Target",
            "",
            "| Event ID | Event | Effect | Raw target |",
            "|---:|---|---|---:|",
        ]
    )
    for event_id, event_name, field, raw_target in data["event_unresolved"]:
        lines.append(f"| {event_id} | {_esc(event_name)} | `{_esc(field)}` | {raw_target} |")
    if not data["event_unresolved"]:
        lines.append("| — | — | — | 解決不能参照なし |")
    lines.extend(["", "[Unit索引データ品質](data-quality.md)", ""])
    path = out / "event-random.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _write_mercenaries(module, out: Path, data) -> Path:
    grouped: dict[int, list[dict[str, object]]] = defaultdict(list)
    for relation in data["mercenary_relations"]:
        grouped[int(relation["mercenary_id"])].append(relation)
    lines = [
        "---",
        'title: "Mercenary Unit索引"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {data["commit"]}"',
        "---",
        "",
        "# Mercenary Unit索引",
        "",
        "`Mercenary.csv`から、傭兵団のCommander・Troop・初期人数・最低入札額・Era maskを整理します。",
        "",
        "| Company | ID | Era | Boss | Commander | Troop | Men | Level | Min men | Min pay | XP | Rec rate | Starting items |",
        "|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for mercenary_id, relations in sorted(grouped.items()):
        first = relations[0]
        commander = next((relation for relation in relations if relation["category"] == "Commander"), None)
        troop = next((relation for relation in relations if relation["category"] == "Troop"), None)
        commander_cell = _target_cell(module, commander) if commander else "—"
        troop_cell = _target_cell(module, troop) if troop else "—"
        men = int(troop["count"]) if troop else 0
        items = ", ".join(
            item for item in (str(first.get("item1") or ""), str(first.get("item2") or "")) if item
        ) or "—"
        lines.append(
            f"| <a id=\"mercenary-{mercenary_id}\"></a>{_esc(first['company'])} | {mercenary_id} | "
            f"{_esc(first['era'])} | {_esc(first['boss'] or '—')} | {commander_cell} | {troop_cell} | "
            f"{men} | {first['level']} | {first['minmen']} | {first['minpay']} | {first['xp']} | "
            f"{first['recruit_rate']} | {_esc(items)} |"
        )
    lines.extend(
        [
            "",
            "Era maskは1=EA、2=MA、4=LAのbit組み合わせです。傭兵の実際の出現・競売・再雇用状況はゲーム状態に依存します。",
            "",
            "[Unit総合索引へ戻る](index.md)",
            "",
        ]
    )
    path = out / "mercenaries.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _write_pages(module, out: Path, data) -> None:
    for filename, title, kinds, description in EVENT_PAGE_CONFIG:
        _write_event_page(module, out, data, filename, title, kinds, description)
    _write_event_random(module, out, data)
    _write_mercenaries(module, out, data)


def install_event_pages(module, data) -> None:
    original_acquisition_section = module.acquisition_section
    original_source_labels = module.source_labels
    original_write_main_index = module.write_main_index
    original_write_unit_catalog = module.write_unit_catalog

    def acquisition_section(relations: list[dict[str, object]]) -> str:
        base = original_acquisition_section(relations).rstrip()
        events = [relation for relation in relations if str(relation.get("kind", "")).startswith("Event")]
        mercenaries = [relation for relation in relations if relation.get("kind") == "Mercenary"]
        additions: list[str] = []
        if events:
            additions.extend(["### Eventによる出現・変身", "", _event_unit_table(events).rstrip()])
        if mercenaries:
            additions.extend(["", "### Mercenary", "", _mercenary_unit_table(mercenaries).rstrip()])
        if not additions:
            return base + "\n"
        return base + "\n\n" + "\n".join(additions).strip() + "\n"

    def source_labels(unit_id: int, current_data) -> list[str]:
        labels = original_source_labels(unit_id, current_data)
        if current_data["event_incoming"].get(unit_id) and "Event" not in labels:
            labels.append("Event")
        if current_data["mercenary_incoming"].get(unit_id) and "Mercenary" not in labels:
            labels.append("Mercenary")
        return labels

    def write_main_index(out: Path, current_data, stats: dict[str, int]):
        stats.update(_event_stats(current_data))
        path = original_write_main_index(out, current_data, stats)
        text = path.read_text(encoding="utf-8")
        anchor = f"- [Magic Site Unit](magic-sites.md) — {stats['site_relations']} site–unit relations"
        additions = "\n".join(
            [
                f"- [Event Unit・Commander生成](event-spawns.md) — {stats['event_spawn_relations']} relations",
                f"- [Event変身・強制変身](event-transforms.md) — {stats['event_transform_relations']} relations",
                f"- [Event暗殺・戦闘参加Unit](event-combat.md) — {stats['event_combat_relations']} relations",
                f"- [Event Random pool・未解決Target](event-random.md) — {stats['event_random_references']} random references",
                f"- [Mercenary Unit](mercenaries.md) — {stats['mercenary_companies']} companies / {stats['mercenary_relations']} relations",
            ]
        )
        if anchor in text and "event-spawns.md" not in text:
            text = text.replace(anchor, anchor + "\n" + additions, 1)
        text = text.replace(
            "Event、Wish、Random summon table、hard-coded Reanimation結果は、対応を確定できるまで未分類または能力Flagとして残します。",
            "EventとMercenaryの固定Unit参照は索引化済みです。Wish、Random summon table、hard-coded Reanimation結果は、対応を確定できるまで未分類または能力Flagとして残します。",
        )
        path.write_text(text, encoding="utf-8")
        return path

    def write_unit_catalog(current_data, out: Path) -> dict[str, int]:
        stats = original_write_unit_catalog(current_data, out)
        _write_pages(module, out, current_data)
        stats.update(_event_stats(current_data))
        return stats

    module.acquisition_section = acquisition_section
    module.source_labels = source_labels
    module.write_main_index = write_main_index
    module.write_unit_catalog = write_unit_catalog
