#!/usr/bin/env python3
"""Validate equipment and mount references used by recruitable vanilla units."""
from __future__ import annotations

import argparse
from collections import defaultdict

from generate_recruitment_data import FILES, mapping, source, unit_data
from recruitment_loadouts import equipment_indexes, unit_armor_ids, unit_weapon_ids

MAP_FILES = (
    "fort_troop_types_by_nation.csv",
    "fort_leader_types_by_nation.csv",
    "nonfort_troop_types_by_nation.csv",
    "nonfort_leader_types_by_nation.csv",
    "coast_troop_types_by_nation.csv",
    "coast_leader_types_by_nation.csv",
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    paths = {name: source(name, args.refresh, args.offline) for name in FILES}
    units = unit_data(paths["BaseU.csv"])
    weapons, armors = equipment_indexes(paths)

    recruit_ids: set[int] = set()
    for filename in MAP_FILES:
        mapped = mapping(paths[filename])
        for unit_ids in mapped.values():
            recruit_ids.update(unit_ids)

    selected_ids = set(recruit_ids)
    for unit_id in list(recruit_ids):
        mount_id = int(float(units[unit_id].get("mountmnr") or 0))
        if mount_id:
            selected_ids.add(mount_id)

    missing_weapons = defaultdict(list)
    missing_armors = defaultdict(list)
    missing_mounts = defaultdict(list)

    for unit_id in sorted(selected_ids):
        row = units.get(unit_id)
        if row is None:
            continue
        label = f"{row.get('name') or '(unnamed)'} #{unit_id}"
        for weapon_id in unit_weapon_ids(row):
            if weapon_id not in weapons:
                missing_weapons[weapon_id].append(label)
        for armor_id in unit_armor_ids(row):
            if armor_id not in armors:
                missing_armors[armor_id].append(label)
        mount_id = int(float(row.get("mountmnr") or 0))
        if mount_id and mount_id not in units:
            missing_mounts[mount_id].append(label)

    print(f"recruit unit records checked: {len(recruit_ids)}")
    print(f"recruit units plus mounts checked: {len(selected_ids)}")
    print(f"weapon records available: {len(weapons)}")
    print(f"armor records available: {len(armors)}")

    problems = False
    for title, values in (
        ("unresolved weapon refs", missing_weapons),
        ("unresolved armor refs", missing_armors),
        ("unresolved mount refs", missing_mounts),
    ):
        if not values:
            print(f"{title}: none")
            continue
        problems = True
        print(f"{title}:")
        for record_id, users in sorted(values.items()):
            print(f"  {record_id}: {', '.join(users)}")

    if problems:
        raise SystemExit("recruit equipment reference validation failed")


if __name__ == "__main__":
    main()
