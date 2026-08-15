#!/usr/bin/env python3
"""Generate all derived Wiki pages, validate source references, and build/serve the site.

This file is the canonical build pipeline used by local development and GitHub Actions.
Keeping the command list here prevents README and workflow definitions from drifting apart.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Step:
    """One deterministic pipeline step."""

    label: str
    command: tuple[str, ...]
    supports_offline: bool = False
    supports_refresh: bool = False
    default_offline: bool = False


STEPS: tuple[Step, ...] = (
    Step("国家カタログ", ("scripts/generate_nation_catalog.py",)),
    Step(
        "Recruit・Mage access・Unit装備",
        ("scripts/generate_recruitment_data.py",),
        supports_offline=True,
        supports_refresh=True,
    ),
    Step(
        "Recruit装備参照の検証",
        ("scripts/check_recruitment_equipment_refs.py",),
        supports_offline=True,
        default_offline=True,
    ),
    Step(
        "装備使用者逆引き",
        ("scripts/generate_equipment_usage_data.py",),
        supports_offline=True,
        supports_refresh=True,
        default_offline=True,
    ),
    Step(
        "Spell・Magic Item",
        ("scripts/generate_spell_item_data.py",),
        supports_offline=True,
        supports_refresh=True,
    ),
    Step(
        "Weapon・Armor・Damage property",
        ("scripts/generate_combat_data.py",),
        supports_offline=True,
        supports_refresh=True,
    ),
    Step(
        "Unit総合索引",
        ("scripts/generate_unit_catalog.py",),
        supports_offline=True,
        supports_refresh=True,
    ),
    Step(
        "Magic Site総合索引",
        ("scripts/generate_magic_site_data.py",),
        supports_offline=True,
        supports_refresh=True,
    ),
    Step(
        "Site Search参照",
        ("scripts/generate_site_search_data.py",),
        supports_offline=True,
        supports_refresh=True,
        default_offline=True,
    ),
    Step(
        "国家別Site Search能力",
        ("scripts/run_nation_site_search_data.py",),
        supports_offline=True,
        supports_refresh=True,
        default_offline=True,
    ),
    Step(
        "Extended Magic Access",
        ("scripts/run_extended_magic_access_data.py",),
        supports_offline=True,
        supports_refresh=True,
        default_offline=True,
    ),
    Step(
        "Magic Access routes",
        ("scripts/run_magic_access_routes_safe.py",),
        supports_offline=True,
        supports_refresh=True,
        default_offline=True,
    ),
)


def run(command: Sequence[str]) -> None:
    """Run one command from the repository root and stop on failure."""

    printable = " ".join(command)
    print(f"\n$ {printable}", flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def step_command(step: Step, *, offline: bool, refresh: bool) -> list[str]:
    command = [sys.executable, *step.command]
    if refresh and step.supports_refresh:
        command.append("--refresh")
    elif step.supports_offline and (offline or step.default_offline):
        command.append("--offline")
    return command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Dominions 6日本語Wikiの生成処理を一括実行します。"
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--offline",
        action="store_true",
        help="Networkを使わず、既存Cacheだけで全生成処理を実行します。",
    )
    mode.add_argument(
        "--refresh",
        action="store_true",
        help="対応GeneratorのCacheを再取得してから生成します。",
    )
    output = parser.add_mutually_exclusive_group()
    output.add_argument(
        "--serve",
        action="store_true",
        help="生成後にzensical serveを実行します。",
    )
    output.add_argument(
        "--generate-only",
        action="store_true",
        help="Markdown生成のみ実行し、Zensical buildを省略します。",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    for index, step in enumerate(STEPS, start=1):
        print(f"\n[{index}/{len(STEPS)}] {step.label}", flush=True)
        run(step_command(step, offline=args.offline, refresh=args.refresh))

    if args.generate_only:
        print("\n生成処理が完了しました。", flush=True)
        return 0

    if args.serve:
        run(("zensical", "serve"))
    else:
        run(("zensical", "build", "--clean"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
