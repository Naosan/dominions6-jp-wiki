from __future__ import annotations

import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

from generate_recruitment_data import CACHE, COMMIT, source, tsv
from unit_catalog_event_integration import load_unit_catalog as load_base_unit_catalog
from unit_catalog_special_corrections import apply_special_corrections
from unit_catalog_special_data import (
    build_item_unit_relations,
    build_special_spell_relations,
)

RAW_ROOT = f"https://raw.githubusercontent.com/larzm42/dom6inspector/{COMMIT}"


def _merge_acquisitions(base, *extra_sources):
    merged: dict[int, list[dict[str, object]]] = defaultdict(list)
    for unit_id, relations in base.items():
        merged[unit_id].extend(relations)
    for source_map in extra_sources:
        for unit_id, relations in source_map.items():
            merged[unit_id].extend(relations)
    return merged


def _repository_source(
    repository_path: str,
    refresh: bool,
    offline: bool,
) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    cache_name = repository_path.replace("/", "__")
    path = CACHE / cache_name
    if path.exists() and path.stat().st_size and not refresh:
        return path
    if offline:
        raise FileNotFoundError(f"offline cache missing: {path}")

    request = urllib.request.Request(
        f"{RAW_ROOT}/{repository_path}",
        headers={"User-Agent": "dominions6-jp-wiki/1.0"},
    )
    error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = response.read()
            if not payload:
                raise RuntimeError("empty download")
            path.write_bytes(payload)
            return path
        except (urllib.error.URLError, TimeoutError, RuntimeError) as exc:
            error = exc
            if attempt < 2:
                time.sleep(1 + attempt)
    raise RuntimeError(f"failed to download {repository_path}: {error}")


def load_unit_catalog(refresh: bool = False, offline: bool = False):
    data = load_base_unit_catalog(refresh, offline)

    base_items_path = data["paths"].get("BaseI.csv") or source(
        "BaseI.csv", refresh, offline
    )
    unique_pools_path = source("special_unique_summons.csv", refresh, offline)
    terrain_pools_path = source("terrain_specific_summons.csv", refresh, offline)
    spell_tables_path = _repository_source(
        "scripts/DMI/SpellTables.js",
        refresh,
        offline,
    )
    data["paths"]["BaseI.csv"] = base_items_path
    data["paths"]["special_unique_summons.csv"] = unique_pools_path
    data["paths"]["terrain_specific_summons.csv"] = terrain_pools_path
    data["paths"]["SpellTables.js"] = spell_tables_path

    item_data = build_item_unit_relations(
        tsv(base_items_path),
        data["units"],
    )
    spell_data = build_special_spell_relations(
        tsv(data["paths"]["spells.csv"]),
        tsv(data["paths"]["effects_spells.csv"]),
        tsv(data["paths"]["attributes_by_spell.csv"]),
        tsv(unique_pools_path),
        tsv(terrain_pools_path),
        spell_tables_path.read_text(encoding="utf-8"),
        data["units"],
    )

    data["item_incoming"] = item_data["incoming"]
    data["item_relations"] = item_data["relations"]
    data["item_random_targets"] = item_data["random_targets"]
    data["item_unresolved"] = item_data["unresolved"]
    data["item_field_counts"] = item_data["field_counts"]
    data["items_with_unit_relations"] = item_data["items_with_relations"]
    data["arena_items"] = item_data["arena_items"]

    data["spell_candidate_incoming"] = spell_data["candidate_incoming"]
    data["spell_candidate_relations"] = spell_data["candidate_relations"]
    data["spell_special_relations"] = spell_data["special_relations"]
    data["spell_random_targets"] = spell_data["random_relations"]
    data["special_spell_unresolved"] = spell_data["unresolved_special"]
    data["special_candidate_unresolved"] = spell_data["unresolved_candidates"]
    data["special_unique_pools"] = spell_data["unique_pools"]
    data["special_unique_pool_units"] = spell_data["unique_pool_units"]
    data["terrain_summon_pools"] = spell_data["terrain_pools"]
    data["terrain_summon_pool_units"] = spell_data["terrain_pool_units"]
    data["explicit_named_summon_pools"] = spell_data["explicit_named_pools"]

    classified_standard = spell_data["classified_standard"]
    data["unresolved_spells"] = [
        entry
        for entry in data["unresolved_spells"]
        if (int(entry[0]), int(entry[2]), int(entry[3])) not in classified_standard
    ]

    data["spell_summons"] = _merge_acquisitions(
        data["spell_summons"],
        spell_data["candidate_incoming"],
    )
    data["acquisitions"] = _merge_acquisitions(
        data["acquisitions"],
        spell_data["candidate_incoming"],
        item_data["incoming"],
    )
    apply_special_corrections(data)
    return data