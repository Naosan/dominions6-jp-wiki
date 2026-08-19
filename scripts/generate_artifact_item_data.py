#!/usr/bin/env python3
"""Separate forgeable Construction 9 artifacts from unforgeable Item records.

Dominions 6 calls research-level / Construction 9 forgeable items artifacts.
They are unique while unforgeable Item records are a separate acquisition class.
This supplemental generator runs after the normal Item/effect generators so it
can normalize the generated terminology without duplicating the core item parser.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import generate_spell_item_data as core

ARTIFACT_CONST = 9
UNFORGEABLE_CONST = 12
START = "<!-- artifact-item-index:start -->"
END = "<!-- artifact-item-index:end -->"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    return parser.parse_args()


def artifact_items(items: list[dict[str, object]]) -> list[dict[str, object]]:
    return [item for item in items if int(item["const"]) == ARTIFACT_CONST]


def unforgeable_items(items: list[dict[str, object]]) -> list[dict[str, object]]:
    return [item for item in items if int(item["const"]) == UNFORGEABLE_CONST]


def artifact_page(items: list[dict[str, object]]) -> str:
    selected = artifact_items(items)
    return "\n".join(
        [
            "---",
            'title: "Artifact一覧 — Construction 9"',
            "status: generated",
            'verified_version: "6.35"',
            f'generated_from: "dom6inspector {core.COMMIT}"',
            "---",
            "",
            "# Artifact一覧 — Construction 9",
            "",
            f"Construction 9のforgeable Artifactは**{len(selected)}**件です。Dominions 6ではArtifactはuniqueで、同じArtifactが既に存在する間は再Forgeできません。",
            "",
            "このページは6.35固定データの事実索引です。Yearning、Artifact race、Booster chain、Carrier riskは[Artifact・Unique Item攻略](../../items/artifacts.md)を参照してください。",
            "",
            "[Magic Itemデータ索引へ戻る](index.md)",
            "",
            core.item_table(selected),
            "",
            "!!! note \"Yearning\"",
            "    Yearning状態はBaseIの静的Item recordではなくゲーム進行中の状態です。この表のGem欄は通常の基礎Forge Costで、Yearningによる半額化は反映しません。ゲーム内Forge画面を確認してください。",
            "",
        ]
    )


def index_block(artifact_count: int, unforgeable_count: int) -> str:
    return "\n".join(
        [
            START,
            "## Artifact / Unforgeable",
            "",
            f"- [Artifact — Construction 9](artifacts.md) — {artifact_count} items / unique",
            f"- [Unforgeable Item](unforgeable.md) — {unforgeable_count} items / 通常Forge不可",
            "- [Artifact・Unique Item攻略](../../items/artifacts.md)",
            "",
            "Artifactと通常Forge不可Itemは別カテゴリとして扱います。",
            END,
            "",
        ]
    )


def patch_index(artifact_count: int, unforgeable_count: int) -> None:
    path = core.ITEM_OUT / "index.md"
    text = path.read_text(encoding="utf-8")
    # Remove the old combined terminology emitted by the core generator.
    text = text.replace("- [Unforgeable / Artifact](unforgeable.md)\n", "")
    block = index_block(artifact_count, unforgeable_count)
    if START in text and END in text:
        before, rest = text.split(START, 1)
        _old, after = rest.split(END, 1)
        text = before + block.rstrip() + after
    else:
        anchor = "\n## 表の読み方"
        if anchor not in text:
            raise ValueError("Magic Item index insertion anchor not found")
        text = text.replace(anchor, "\n" + block + "## 表の読み方", 1)
    path.write_text(text, encoding="utf-8")


def normalize_unforgeable_page() -> None:
    path = core.ITEM_OUT / "unforgeable.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace('title: "Unforgeable・Artifact一覧"', 'title: "Unforgeable Item一覧"')
    text = text.replace("# Unforgeable・Artifact一覧", "# Unforgeable Item一覧")
    text = text.replace(
        "通常のConstruction研究とForge Itemでは作成できないItemです。入手法はArtifact、Event、Arena、国家固有などItemごとに異なります。",
        "通常のConstruction研究とForge Itemでは作成できないItemです。入手法はEvent、Arena、国家固有、特殊生成などItemごとに異なります。",
    )
    path.write_text(text, encoding="utf-8")


def normalize_generated_item_labels() -> int:
    changed = 0
    for path in core.ITEM_OUT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        new = text.replace("Unforgeable / Artifact", "Unforgeable")
        # BaseI's `crown` flag means crown; it is not the Artifact marker.
        new = new.replace("Artifact / Crown", "Crown")
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    return changed


def write_pages(items: list[dict[str, object]]) -> tuple[int, int, int]:
    artifacts = artifact_items(items)
    unforgeable = unforgeable_items(items)
    (core.ITEM_OUT / "artifacts.md").write_text(artifact_page(items), encoding="utf-8")
    normalize_unforgeable_page()
    patch_index(len(artifacts), len(unforgeable))
    normalized = normalize_generated_item_labels()
    return len(artifacts), len(unforgeable), normalized


def main() -> None:
    args = parse_args()
    names = ("BaseI.csv", "weapons.csv", "armors.csv")
    paths = {name: core.source(name, args.refresh, args.offline) for name in names}
    items = core.item_rows(paths)
    artifacts, unforgeable, normalized = write_pages(items)
    print(f"generated forgeable artifacts (Construction 9): {artifacts}")
    print(f"indexed unforgeable items: {unforgeable}")
    print(f"normalized generated Item pages: {normalized}")


if __name__ == "__main__":
    main()
