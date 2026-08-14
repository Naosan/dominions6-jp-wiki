#!/usr/bin/env python3
"""Generate comprehensive Dominions 6 Magic Site reference pages."""
from __future__ import annotations

import argparse
from pathlib import Path

from generate_recruitment_data import COMMIT, nations, source, tsv, unit_data
from magic_site_data import build_magic_site_catalog
from magic_site_pages import write_magic_site_catalog

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "data" / "sites"
FILES = (
    "MagicSites.csv",
    "site_terrain_types.csv",
    "BaseU.csv",
    "attributes_by_nation.csv",
    "events.csv",
)


def validate(stats: dict[str, int]) -> None:
    checks = (
        ("sites", 1300),
        ("site_pages", 1300),
        ("path_pages", 10),
        ("monthly_gem_sites", 100),
        ("site_unit_relations", 700),
        ("site_recruit_relations", 500),
        ("site_summon_relations", 10),
        ("start_site_relations", 100),
        ("site_event_relations", 10),
        ("throne_sites", 50),
    )
    for key, minimum in checks:
        if stats.get(key, 0) < minimum:
            raise ValueError(
                f"Magic Site catalog appears incomplete: {key}={stats.get(key, 0)} < {minimum}"
            )
    if stats["site_pages"] != stats["sites"]:
        raise ValueError(
            f"Magic Site page count mismatch: pages={stats['site_pages']} records={stats['sites']}"
        )
    for key in (
        "duplicate_site_ids",
        "missing_site_names",
        "unclassified_site_values",
        "unresolved_site_units",
        "unresolved_nation_sites",
        "unresolved_site_events",
        "unresolved_national_recruit_nations",
    ):
        if stats.get(key, 0) != 0:
            raise ValueError(f"Magic Site integrity failure: {key}={stats[key]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    paths = {name: source(name, args.refresh, args.offline) for name in FILES}
    nation_rows = nations()
    units = unit_data(paths["BaseU.csv"])
    data = build_magic_site_catalog(
        tsv(paths["MagicSites.csv"]),
        tsv(paths["site_terrain_types.csv"]),
        tsv(paths["attributes_by_nation.csv"]),
        tsv(paths["events.csv"]),
        units,
        nation_rows,
    )
    stats = write_magic_site_catalog(data, OUT, COMMIT)
    validate(stats)

    print(f"source commit: {COMMIT}")
    for key, value in stats.items():
        print(f"{key}: {value}")
    print("path distribution:")
    for path, count in sorted(data["path_counts"].items()):
        print(f"  {path}: {count}")
    print("rarity distribution:")
    for rarity, count in data["rarity_counts"].items():
        print(f"  {rarity}: {count}")
    print(f"unknown location bitsets: {len(data['unknown_location_bits'])}")
    for site_id, name, raw_location, remaining in data["unknown_location_bits"][:25]:
        print(
            "unknown Site location bits: "
            f"site={site_id} name={name!r} raw={raw_location} remaining={remaining}"
        )
    print(f"unclassified Site fields: {len(data['unclassified_fields'])}")
    for field, count in data["unclassified_fields"].items():
        print(f"unclassified Site field: field={field!r} count={count}")
    print(f"unresolved Site Unit targets: {len(data['unresolved_units'])}")
    for site_id, site_name, field, raw_target in data["unresolved_units"]:
        print(
            "unresolved Site Unit: "
            f"site={site_id} name={site_name!r} field={field} raw={raw_target!r}"
        )
    print(f"unresolved Nation Site targets: {len(data['unresolved_nation_sites'])}")
    for nation_id, nation_name, attribute, site_id in data["unresolved_nation_sites"]:
        print(
            "unresolved Nation Site: "
            f"nation={nation_id} name={nation_name!r} attribute={attribute} site={site_id}"
        )
    print(f"unresolved Site Event targets: {len(data['unresolved_events'])}")
    for event_id, event_name, field, raw_target in data["unresolved_events"]:
        print(
            "unresolved Site Event: "
            f"event={event_id} name={event_name!r} field={field} raw={raw_target!r}"
        )
    print(
        "unresolved national recruit Nations: "
        f"{len(data['unresolved_national_recruits'])}"
    )
    for site_id, site_name, nation_id in data["unresolved_national_recruits"]:
        print(
            "unresolved Site national recruit Nation: "
            f"site={site_id} name={site_name!r} nation={nation_id}"
        )


if __name__ == "__main__":
    main()
