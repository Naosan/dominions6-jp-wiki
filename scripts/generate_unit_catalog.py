#!/usr/bin/env python3
"""Generate the Dominions 6 all-Unit catalog and confirmed acquisition indexes."""
from __future__ import annotations

import argparse
from pathlib import Path

import unit_catalog_pages
from unit_catalog_quality import write_quality_report
from unit_catalog_roles import install_role_resolver
from unit_catalog_sources import load_unit_catalog

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "data" / "units"


def validate(stats: dict[str, int]) -> None:
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
        ("shape_relations", 50),
    )
    for key, minimum in checks:
        if stats[key] < minimum:
            raise ValueError(f"Unit catalog appears incomplete: {key}={stats[key]} < {minimum}")
    if stats["unit_pages"] != stats["units"]:
        raise ValueError(
            f"Unit page count mismatch: pages={stats['unit_pages']} records={stats['units']}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    data = load_unit_catalog(args.refresh, args.offline)
    install_role_resolver(unit_catalog_pages, data)
    stats = unit_catalog_pages.write_unit_catalog(data, OUT)
    write_quality_report(data, OUT, stats)
    validate(stats)

    print(f"source commit: {data['commit']}")
    for key, value in stats.items():
        print(f"{key}: {value}")
    print(f"unresolved spell summon references: {len(data['unresolved_spells'])}")
    print(f"unresolved Magic Site Unit references: {len(data['unresolved_sites'])}")
    print(f"unresolved Shape references: {len(data['unresolved_shapes'])}")


if __name__ == "__main__":
    main()
