#!/usr/bin/env python3
"""Verify source inputs, generate all derived pages, and build/serve the site.

This file is the canonical pipeline used by local development and GitHub
Actions.  External downloads happen only in the source-audit stage; every
subsequent generator consumes the verified cache in offline mode.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REPORT = ROOT / "build" / "source-audit.json"
SITE_REPORT = ROOT / "build" / "site-audit.json"


@dataclass(frozen=True)
class Step:
    """One deterministic pipeline step."""

    label: str
    command: tuple[str, ...]
    supports_offline: bool = False


STEPS: tuple[Step, ...] = (
    Step("国家カタログ", ("scripts/generate_nation_catalog.py",)),
    Step(
        "Recruit・Mage access・Unit装備",
        ("scripts/generate_recruitment_data.py",),
        supports_offline=True,
    ),
    Step(
        "Recruit装備参照の検証",
        ("scripts/check_recruitment_equipment_refs.py",),
        supports_offline=True,
    ),
    Step(
        "装備使用者逆引き",
        ("scripts/generate_equipment_usage_data.py",),
        supports_offline=True,
    ),
    Step(
        "Spell・Magic Item",
        ("scripts/generate_spell_item_data.py",),
        supports_offline=True,
    ),
    Step(
        "Magic Item目的別・Construction索引",
        ("-m", "scripts.generate_item_purpose_data"),
        supports_offline=True,
    ),
    Step(
        "Weapon・Armor・Damage property",
        ("scripts/generate_combat_data.py",),
        supports_offline=True,
    ),
    Step(
        "Unit総合索引",
        ("scripts/generate_unit_catalog.py",),
        supports_offline=True,
    ),
    Step(
        "Magic Site総合索引",
        ("scripts/generate_magic_site_data.py",),
        supports_offline=True,
    ),
    Step(
        "Site Search参照",
        ("scripts/generate_site_search_data.py",),
        supports_offline=True,
    ),
    Step(
        "国家別Site Search能力",
        ("scripts/run_nation_site_search_data.py",),
        supports_offline=True,
    ),
    Step(
        "Extended Magic Access",
        ("scripts/run_extended_magic_access_data.py",),
        supports_offline=True,
    ),
    Step(
        "Magic Access routes",
        ("scripts/run_magic_access_routes_safe.py",),
        supports_offline=True,
    ),
    Step(
        "個別Data recordの軽量Template",
        ("scripts/apply_data_record_templates.py",),
    ),
)


def run(command: Sequence[str]) -> None:
    """Run one command from the repository root and stop on failure."""

    printable = " ".join(command)
    print(f"\n$ {printable}", flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def source_command(*, offline: bool, refresh: bool) -> list[str]:
    command = [
        sys.executable,
        "scripts/audit_sources.py",
        "--report",
        str(SOURCE_REPORT.relative_to(ROOT)),
    ]
    if refresh:
        command.append("--refresh")
    elif offline:
        command.append("--offline")
    return command


def step_command(step: Step) -> list[str]:
    command = [sys.executable, *step.command]
    if step.supports_offline:
        command.append("--offline")
    return command


def site_audit_command() -> list[str]:
    command = [
        sys.executable,
        "scripts/audit_site.py",
        "--report",
        str(SITE_REPORT.relative_to(ROOT)),
    ]
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        command.append("--github-summary")
    return command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Dominions 6日本語Wikiの生成処理を一括実行します。"
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--offline",
        action="store_true",
        help="Networkを使わず、Manifest検証済みCacheだけで全処理を実行します。",
    )
    mode.add_argument(
        "--refresh",
        action="store_true",
        help="Manifestに固定した全Sourceを再取得・検証してから生成します。",
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

    print("\n[Source] Dom6 Inspector snapshotの取得・Checksum検証", flush=True)
    run(source_command(offline=args.offline, refresh=args.refresh))

    for index, step in enumerate(STEPS, start=1):
        print(f"\n[{index}/{len(STEPS)}] {step.label}", flush=True)
        run(step_command(step))

    if args.generate_only:
        print("\n生成処理が完了しました。", flush=True)
        return 0

    if args.serve:
        run(("zensical", "serve"))
    else:
        run(("zensical", "build", "--clean"))
        run(site_audit_command())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
