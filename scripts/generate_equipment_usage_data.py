#!/usr/bin/env python3
"""Generate reverse indexes from weapons and armor to recruitable users."""
from __future__ import annotations

import argparse

from generate_recruitment_data import FILES, mapping, nations, source, unit_data
from recruitment_loadouts import equipment_indexes
from recruitment_usage_indexes import write_equipment_usage_indexes

COMMIT = "cfac4311bc0b58053b8dead7bffbc036ba9bd5dc"
MAP_FILES = {
    "ft": "fort_troop_types_by_nation.csv",
    "fl": "fort_leader_types_by_nation.csv",
    "nt": "nonfort_troop_types_by_nation.csv",
    "nl": "nonfort_leader_types_by_nation.csv",
    "ct": "coast_troop_types_by_nation.csv",
    "cl": "coast_leader_types_by_nation.csv",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    paths = {name: source(name, args.refresh, args.offline) for name in FILES}
    nation_rows = nations()
    units = unit_data(paths["BaseU.csv"])
    weapons, armors = equipment_indexes(paths)
    maps = {key: mapping(paths[filename]) for key, filename in MAP_FILES.items()}

    stats = write_equipment_usage_indexes(
        nation_rows,
        units,
        maps,
        weapons,
        armors,
        COMMIT,
    )

    if stats["recruits"] < 1200:
        raise ValueError(f"recruit relation data appears incomplete: {stats['recruits']}")
    if stats["used_weapons"] < 300:
        raise ValueError(f"weapon usage data appears incomplete: {stats['used_weapons']}")
    if stats["used_armors"] < 100:
        raise ValueError(f"armor usage data appears incomplete: {stats['used_armors']}")

    print(f"source commit: {COMMIT}")
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
