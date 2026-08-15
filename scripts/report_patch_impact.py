#!/usr/bin/env python3
"""Repository-specific entry point for the patch-impact report.

The core reporter is intentionally reusable.  This layer preserves the Wiki's
legacy template convention while metadata is migrated: pages under
``docs/templates`` or carrying ``status: template`` are authoring scaffolds,
not game-versioned hand-written articles.
"""
from __future__ import annotations

from pathlib import PurePosixPath

try:
    from . import report_patch_impact_core as _core
except ImportError:  # Direct execution: ``python scripts/report_patch_impact.py``
    import report_patch_impact_core as _core


# Re-export the core API so existing tests and imports keep using the public
# ``scripts.report_patch_impact`` module.
for _name in dir(_core):
    if not _name.startswith("_"):
        globals()[_name] = getattr(_core, _name)


_core_verification_inventory = _core.verification_inventory
_CLASSIFIED_VERSION_KEYS = (
    "current",
    "stale",
    "ahead",
    "missing",
    "invalid",
    "needs_update",
)


def _legacy_template(record: dict[str, str]) -> bool:
    path = PurePosixPath(str(record.get("path", "")))
    return record.get("status", "").strip() == "template" or (
        bool(path.parts) and path.parts[0] == "templates"
    )


def verification_inventory(docs, target_version: str) -> dict[str, object]:
    """Exclude authoring templates from the game-version freshness scope."""

    result = _core_verification_inventory(docs, target_version)
    excluded_counted_paths: set[str] = set()
    excluded_paths: set[str] = set()

    for key in _CLASSIFIED_VERSION_KEYS:
        kept: list[dict[str, str]] = []
        for record in result[key]:
            if _legacy_template(record):
                path = record["path"]
                excluded_counted_paths.add(path)
                excluded_paths.add(path)
            else:
                kept.append(record)
        result[key] = kept

    kept_metadata: list[dict[str, str]] = []
    for record in result["metadata_missing"]:
        if _legacy_template(record):
            excluded_paths.add(record["path"])
        else:
            kept_metadata.append(record)
    result["metadata_missing"] = kept_metadata

    result["hand_written_pages"] = max(
        0,
        int(result["hand_written_pages"]) - len(excluded_counted_paths),
    )
    result["excluded_non_game_pages"] = (
        int(result["excluded_non_game_pages"]) + len(excluded_paths)
    )
    return result


# ``main`` resolves this global in the core module at runtime.
_core.verification_inventory = verification_inventory


if __name__ == "__main__":
    raise SystemExit(_core.main())
