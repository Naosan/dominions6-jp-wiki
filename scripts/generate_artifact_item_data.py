#!/usr/bin/env python3
"""Separate forgeable Construction 9 artifacts from unforgeable Item records.

Dominions 6 calls Construction 9 forgeable items artifacts. The modding data
also has separate unforgeable classes at constlevel 11, 13, and 15. This
supplemental generator runs after the normal Item/effect generators so the
rendered Wiki uses the correct acquisition terminology without duplicating the
core item parser.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import generate_spell_item_data as core

ARTIFACT_CONST = 9
UNFORGEABLE_LEVELS = {
    11: "Unforgeable",
    13: "Unforgeable unique artifact",
    15: "Unforgeable unique per nation artifact",
}
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
    return [item for item in items if int(item["const"]) in UNFORGEABLE_LEVELS]


def normalized_unforgeable_item(item: dict[str, object]) -> dict[str, object]:
    copy = dict(item)
    level = int(copy["const"])
    copy["construction"] = UNFORGEABLE_LEVELS[level]
    copy["cost"] = "—"
    return copy


def artifact_page(items: list[dict[str, object]]) -> str:
    selected = artifact_items(items)
    return "\n".join(
        [
            "---",
            'title: "Forgeable Artifact一覧 — Construction 9"',
            "status: generated",
            'verified_version: "6.35"',
            f'generated_from: "dom6inspector {core.COMMIT}"',
            "---",
            "",
            "# Forgeable Artifact一覧 — Construction 9",
            "",
            f"Construction 9のforgeable Artifactは**{len(selected)}**件です。Dominions 6 ManualではC9 Artifactはuniqueで、同じArtifactが既に存在する間は再Forgeできません。",
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


def unforgeable_page(items: list[dict[str, object]]) -> str:
    selected = [normalized_unforgeable_item(item) for item in unforgeable_items(items)]
    groups = {
        level: [item for item in selected if int(item["const"]) == level]
        for level in UNFORGEABLE_LEVELS
    }
    lines = [
        "---",
        'title: "Unforgeable Item一覧"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {core.COMMIT}"',
        "---",
        "",
        "# Unforgeable Item一覧",
        "",
        f"通常のForge Item orderでは作成できないItemを**{len(selected)}**件抽出しています。",
        "",
        "- `constlevel 11`: unforgeable item",
        "- `constlevel 13`: unforgeable unique artifact",
        "- `constlevel 15`: unforgeable unique per-nation artifact",
        "",
        "入手法はEvent、Arena、国家固有、特殊生成などItemごとに異なります。Construction 9のforgeable Artifactとは取得経路を分けて考えてください。",
        "",
        "[Magic Itemデータ索引へ戻る](index.md) · [Artifact・Unique Item攻略](../../items/artifacts.md)",
        "",
    ]
    for level, label in UNFORGEABLE_LEVELS.items():
        group = groups[level]
        lines += [f"## {label} — constlevel {level}", "", core.item_table(group)]
    return "\n".join(lines)


def index_block(artifact_count: int, unforgeable_counts: dict[int, int]) -> str:
    unforgeable_total = sum(unforgeable_counts.values())
    subtype = " / ".join(
        f"{level}: {unforgeable_counts[level]}" for level in UNFORGEABLE_LEVELS
    )
    return "\n".join(
        [
            START,
            "## Artifact / Unforgeable",
            "",
            f"- [Forgeable Artifact — Construction 9](artifacts.md) — {artifact_count} items / unique",
            f"- [Unforgeable Item](unforgeable.md) — {unforgeable_total} items (`constlevel` {subtype})",
            "- [Artifact・Unique Item攻略](../../items/artifacts.md)",
            "",
            "Construction 9 Artifactと、constlevel 11 / 13 / 15の通常Forge不可Itemは取得経路を分けて扱います。",
            END,
            "",
        ]
    )


def patch_index(artifact_count: int, unforgeable_counts: dict[int, int]) -> None:
    path = core.ITEM_OUT / "index.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("- [Unforgeable / Artifact](unforgeable.md)\n", "")
    block = index_block(artifact_count, unforgeable_counts)
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


def normalize_generated_item_labels() -> int:
    """Normalize legacy labels/costs in every generated Item table.

    The core generator predates the explicit 11/13/15 unforgeable split. Rows
    in all supplemental indexes have the common sequence
    `Construction N | Req | Gem`, so normalize that sequence after all Item
    generators have run.
    """

    changed = 0
    row_pattern = re.compile(
        r"\| Construction (11|13|15) \| ([^|\n]+?) \| ([^|\n]+?) \|"
    )

    def row_replacement(match: re.Match[str]) -> str:
        level = int(match.group(1))
        req = match.group(2).strip()
        return f"| {UNFORGEABLE_LEVELS[level]} | {req} | — |"

    for path in core.ITEM_OUT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        new = text.replace("Artifact / Crown", "Crown")
        new = new.replace("Unforgeable / Artifact", "Unforgeable")
        for level, label in UNFORGEABLE_LEVELS.items():
            new = new.replace(f"## Construction {level}", f"## {label} — constlevel {level}")
        new = row_pattern.sub(row_replacement, new)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    return changed


def write_pages(items: list[dict[str, object]]) -> tuple[int, dict[int, int], int]:
    artifacts = artifact_items(items)
    unforgeable_counts = {
        level: sum(int(item["const"]) == level for item in items)
        for level in UNFORGEABLE_LEVELS
    }
    (core.ITEM_OUT / "artifacts.md").write_text(artifact_page(items), encoding="utf-8")
    (core.ITEM_OUT / "unforgeable.md").write_text(unforgeable_page(items), encoding="utf-8")
    patch_index(len(artifacts), unforgeable_counts)
    normalized = normalize_generated_item_labels()
    return len(artifacts), unforgeable_counts, normalized


def main() -> None:
    args = parse_args()
    names = ("BaseI.csv", "weapons.csv", "armors.csv")
    paths = {name: core.source(name, args.refresh, args.offline) for name in names}
    items = core.item_rows(paths)
    artifacts, unforgeable_counts, normalized = write_pages(items)
    print(f"generated forgeable artifacts (Construction 9): {artifacts}")
    print(
        "indexed unforgeable items: "
        + ", ".join(f"const{level}={unforgeable_counts[level]}" for level in UNFORGEABLE_LEVELS)
    )
    print(f"normalized generated Item pages: {normalized}")


if __name__ == "__main__":
    main()
