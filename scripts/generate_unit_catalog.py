#!/usr/bin/env python3
"""Generate the Dominions 6 all-Unit catalog and confirmed source indexes."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import unit_catalog_pages
from unit_catalog_candidate_pages import install_candidate_pages
from unit_catalog_candidate_quality import write_quality_report
from unit_catalog_event_pages import install_event_pages
from unit_catalog_generation_pages import install_generation_pages
from unit_catalog_roles import install_role_resolver
from unit_catalog_special_integration import load_unit_catalog
from unit_catalog_special_pages import install_special_pages

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "data" / "units"


def validate(stats: dict[str, int], data) -> None:
    checks = (
        ("units", 4000),
        ("unit_pages", 4000),
        ("recruit_relations", 1200),
        ("hero_relations", 50),
        ("pretender_relations", 500),
        ("spell_relations", 75),
        ("site_relations", 50),
        ("mount_units", 50),
        ("mount_relations", 100),
        ("shape_relations", 100),
        ("unit_generation_relations", 20),
        ("strategic_spawn_relations", 5),
        ("battle_spawn_relations", 5),
        ("generation_abilities", 5),
        ("nation_generation_abilities", 5),
        ("event_unit_relations", 50),
        ("event_spawn_relations", 25),
        ("event_transform_relations", 5),
        ("event_combat_relations", 5),
        ("event_random_references", 25),
        ("mercenary_companies", 50),
        ("mercenary_relations", 75),
        ("items_with_unit_relations", 5),
        ("item_unit_relations", 5),
        ("item_units", 5),
        ("spell_random_references", 5),
        ("special_spell_relations", 5),
        ("special_unique_pool_entries", 20),
        ("terrain_pool_entries", 3),
        ("spell_candidate_relations", 25),
        ("special_candidate_units", 25),
        ("arena_items", 1),
    )
    for key, minimum in checks:
        if stats.get(key, 0) < minimum:
            raise ValueError(
                f"Unit catalog appears incomplete: {key}={stats.get(key, 0)} < {minimum}"
            )
    if stats["unit_pages"] != stats["units"]:
        raise ValueError(
            f"Unit page count mismatch: pages={stats['unit_pages']} records={stats['units']}"
        )
    for key in (
        "unresolved_event_targets",
        "unresolved_mercenary_targets",
        "unresolved_item_targets",
        "unresolved_special_spell_pools",
        "unresolved_special_candidates",
    ):
        if stats.get(key, 0) != 0:
            raise ValueError(f"Unit source integrity failure: {key}={stats[key]}")
    if data["unresolved_spells"]:
        raise ValueError(
            f"Unit source integrity failure: unresolved_spells={len(data['unresolved_spells'])}"
        )


def _insert_after(path: Path, anchor: str, additions: list[str]) -> None:
    if not path.exists():
        raise FileNotFoundError(f"generated index not found: {path}")
    text = path.read_text(encoding="utf-8")
    first = additions[0]
    if first in text:
        return
    if anchor not in text:
        raise ValueError(f"generated index anchor not found in {path}: {anchor}")
    text = text.replace(anchor, anchor + "\n" + "\n".join(additions), 1)
    path.write_text(text, encoding="utf-8")


def patch_generated_indexes(stats: dict[str, int]) -> None:
    _insert_after(
        ROOT / "docs" / "data" / "spells" / "index.md",
        "- [National / Realm restricted Spell](national.md)",
        [
            f"- [Spell Random summon pool](../units/spell-random-summons.md) — {stats['spell_random_references']} references",
            f"- [Wish・Unique・Terrain特殊召喚](../units/special-summons.md) — {stats['special_spell_relations']} Spell relations / {stats['spell_candidate_relations']} candidate links",
        ],
    )
    _insert_after(
        ROOT / "docs" / "data" / "items" / "index.md",
        "- [Utility Item](utility.md)",
        [
            f"- [Arena関連Magic Item](arena.md) — {stats['arena_items']} items",
            f"- [Magic ItemによるUnit生成・変身](../units/item-unit-sources.md) — {stats['item_unit_relations']} relations",
            f"- [Item Random summon・未解決Target](../units/item-random.md) — {stats['item_random_references']} random references",
        ],
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    data = load_unit_catalog(args.refresh, args.offline)
    install_role_resolver(unit_catalog_pages, data)
    install_generation_pages(unit_catalog_pages, data)
    install_event_pages(unit_catalog_pages, data)
    install_special_pages(unit_catalog_pages, data)
    install_candidate_pages(unit_catalog_pages, data)
    stats = unit_catalog_pages.write_unit_catalog(data, OUT)
    patch_generated_indexes(stats)
    write_quality_report(data, OUT, stats)
    validate(stats, data)

    print(f"source commit: {data['commit']}")
    for key, value in stats.items():
        print(f"{key}: {value}")
    category_counts = Counter(
        str(relation.get("category") or "—")
        for relation in data["spell_special_relations"]
    )
    print(
        "special Spell categories: "
        + ", ".join(f"{name}={count}" for name, count in sorted(category_counts.items()))
    )
    print(f"random Unit-generation references: {len(data['unit_generation_random_targets'])}")
    print(f"unresolved Unit-generation references: {len(data['unit_generation_unresolved'])}")
    print(f"unresolved nation-generation references: {len(data['nation_generation_unresolved'])}")
    print(f"Event random-pool references: {len(data['event_random_targets'])}")
    print(f"unresolved Event Unit references: {len(data['event_unresolved'])}")
    for event_id, event_name, field, raw_target in data["event_unresolved"]:
        print(
            "unresolved Event target: "
            f"event={event_id} name={event_name!r} field={field} raw={raw_target}"
        )
    print(f"unresolved Mercenary Unit references: {len(data['mercenary_unresolved'])}")
    for mercenary_id, company, role, raw_target in data["mercenary_unresolved"]:
        print(
            "unresolved Mercenary target: "
            f"mercenary={mercenary_id} company={company!r} role={role} raw={raw_target}"
        )
    print(f"Item random-pool references: {len(data['item_random_targets'])}")
    print(f"unresolved Item Unit references: {len(data['item_unresolved'])}")
    for item_id, item_name, field, raw_target in data["item_unresolved"]:
        print(
            "unresolved Item target: "
            f"item={item_id} name={item_name!r} field={field} raw={raw_target}"
        )
    print(f"Spell random-pool references: {len(data['spell_random_targets'])}")
    print(f"special Spell summon relations: {len(data['spell_special_relations'])}")
    print(f"explicit special Spell candidate relations: {len(data['spell_candidate_relations'])}")
    print(f"unresolved special Spell pools: {len(data['special_spell_unresolved'])}")
    for spell_id, spell_name, effect_number, raw_argument in data["special_spell_unresolved"]:
        print(
            "unresolved special Spell pool: "
            f"spell={spell_id} name={spell_name!r} effect={effect_number} raw={raw_argument}"
        )
    print(f"unresolved special Spell candidate Units: {len(data['special_candidate_unresolved'])}")
    for spell_id, spell_name, effect_number, unit_id in data["special_candidate_unresolved"]:
        print(
            "unresolved special Spell candidate: "
            f"spell={spell_id} name={spell_name!r} effect={effect_number} unit={unit_id}"
        )
    print(f"unresolved spell summon references: {len(data['unresolved_spells'])}")
    for spell_id, spell_name, effect_number, raw_argument in data["unresolved_spells"]:
        print(
            "unresolved standard Spell target: "
            f"spell={spell_id} name={spell_name!r} effect={effect_number} raw={raw_argument}"
        )
    print(f"unresolved Magic Site Unit references: {len(data['unresolved_sites'])}")
    print(f"unresolved Shape references: {len(data['unresolved_shapes'])}")


if __name__ == "__main__":
    main()