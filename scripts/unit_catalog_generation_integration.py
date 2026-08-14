from __future__ import annotations

from collections import defaultdict

from generate_recruitment_data import source, tsv
from unit_catalog_generation import (
    build_extended_shape_relations,
    build_nation_generation,
    build_unit_generation,
)
from unit_catalog_nation_generation import augment_nation_generation
from unit_catalog_sources import load_unit_catalog as load_base_unit_catalog


def _merge_acquisitions(base, *extra_sources):
    merged: dict[int, list[dict[str, object]]] = defaultdict(list)
    for unit_id, relations in base.items():
        merged[unit_id].extend(relations)
    for source_map in extra_sources:
        for unit_id, relations in source_map.items():
            merged[unit_id].extend(relations)
    return merged


def load_unit_catalog(refresh: bool = False, offline: bool = False):
    data = load_base_unit_catalog(refresh, offline)

    unit_generation = build_unit_generation(data["units"])

    attribute_keys_path = source("attribute_keys.csv", refresh, offline)
    data["paths"]["attribute_keys.csv"] = attribute_keys_path
    attribute_rows = tsv(data["paths"]["attributes_by_nation.csv"])
    nation_generation = build_nation_generation(
        attribute_rows,
        tsv(attribute_keys_path),
        data["nations"],
        data["units"],
    )
    nation_generation = augment_nation_generation(
        nation_generation,
        attribute_rows,
        data["nations"],
        data["units"],
    )

    shape_outgoing, shape_incoming, unresolved_shapes = build_extended_shape_relations(
        data["units"]
    )

    data["unit_generation_outgoing"] = unit_generation["outgoing"]
    data["unit_generation_incoming"] = unit_generation["incoming"]
    data["unit_generation_abilities"] = unit_generation["abilities"]
    data["unit_generation_random_targets"] = unit_generation["random_targets"]
    data["unit_generation_unresolved"] = unit_generation["unresolved"]
    data["unit_generation_field_counts"] = unit_generation["field_counts"]

    data["nation_generation"] = nation_generation["abilities"]
    data["nation_generation_incoming"] = nation_generation["incoming"]
    data["nation_generation_unresolved"] = nation_generation["unresolved"]
    data["nation_attribute_commands"] = nation_generation["attribute_commands"]

    # Replace the original conservative Shape pass. The extended pass corrects
    # threshold fields such as xpshape and cleanshape, then adds seasonal,
    # dominion, battle/world and adjacent-ID HP transformations.
    data["shape_outgoing"] = shape_outgoing
    data["shape_incoming"] = shape_incoming
    data["unresolved_shapes"] = unresolved_shapes

    data["acquisitions"] = _merge_acquisitions(
        data["acquisitions"],
        unit_generation["incoming"],
        nation_generation["incoming"],
    )
    return data
