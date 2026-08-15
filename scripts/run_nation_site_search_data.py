#!/usr/bin/env python3
"""Run the nation Site Search generator with atomic multi-line patching.

The underlying generator patches generated indexes and zensical.toml after all
source pages exist. A patch block must be inserted as a complete unit; checking
individual lines is unsafe because common TOML closing lines already occur in
the configuration.
"""
from __future__ import annotations

from pathlib import Path

import generate_nation_site_search_data as generator


def atomic_insert_after(path: Path, anchor: str, additions: list[str]) -> None:
    if not path.exists():
        raise FileNotFoundError(f"generated page missing: {path}")
    text = path.read_text(encoding="utf-8")
    if additions and additions[0] in text:
        return
    if anchor not in text:
        raise ValueError(f"anchor not found in {path}: {anchor}")
    text = text.replace(anchor, anchor + "\n" + "\n".join(additions), 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    generator._insert_after = atomic_insert_after
    generator.main()


if __name__ == "__main__":
    main()
