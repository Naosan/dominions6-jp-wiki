#!/usr/bin/env python3
"""Generate Dominions 6 nation index pages and missing nation stubs.

The source catalog is data/nations.tsv. Existing pages are never overwritten
unless they are generated stubs containing `status: stub`.

Run from the repository root:
    python scripts/generate_nation_catalog.py
"""

from __future__ import annotations

import csv
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "nations.tsv"
DOCS = ROOT / "docs" / "nations"

ERA = {
    "1": ("EA", "ea", "Early Age"),
    "2": ("MA", "ma", "Middle Age"),
    "3": ("LA", "la", "Late Age"),
}

STATUS_LABELS = {
    "stub": "骨組み",
    "draft": "下書き",
    "review": "攻略あり",
    "verified": "検証済み",
}


def slugify(name: str) -> str:
    value = unicodedata.normalize("NFKD", name)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.lower().replace("&", " and ")
    value = re.sub(r"['’]", "", value)
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def read_rows() -> list[dict[str, str]]:
    with DATA.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    for row in rows:
        code, directory, era_name = ERA[row["era"]]
        row["era_code"] = code
        row["era_dir"] = directory
        row["era_name"] = era_name
        row["slug"] = slugify(row["name"])
    return rows


def page_path(row: dict[str, str]) -> Path:
    return DOCS / row["era_dir"] / f'{row["slug"]}.md'


def frontmatter_status(path: Path) -> str:
    if not path.exists():
        return "stub"
    head = path.read_text(encoding="utf-8")[:1000]
    match = re.search(r"(?m)^status:\s*[\"']?([^\"'\n]+)", head)
    return match.group(1).strip() if match else "draft"


def is_generated_stub(path: Path) -> bool:
    return not path.exists() or frontmatter_status(path) == "stub"


def stub(row: dict[str, str]) -> str:
    title = f'{row["era_code"]} {row["name"]}'
    create_url = (
        "https://github.com/Naosan/dominions6-jp-wiki/new/main/"
        f'docs/nations/{row["era_dir"]}?filename={row["slug"]}.md'
    )
    return f"""---
title: {quote(title)}
status: stub
verified_version: "6.35"
last_verified: "2026-08-14"
nation_id: {row["id"]}
era: {quote(row["era_code"])}
epithet: {quote(row["epithet"])}
---

# {title} — {row["epithet"]}

!!! info "記事状態: 骨組み"
    国家名・時代・Epithet・Nation IDは現行のvanillaデータで確認済みです。兵種、Mage、Pretender、Research、対人戦評価は順次追加します。

[GitHubでこの国家記事を作成する]({create_url})

## 一言でいうと

*執筆中。*

## 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | {row["era_name"]}（{row["era_code"]}） |
| 国家名 | {row["name"]} |
| Epithet | {row["epithet"]} |
| Nation ID | {row["id"]} |
| 略称 | {row["abbreviation"]} |
| 確認バージョン | Dominions 6.35 |

Nation IDはMOD・Inspector・データ照合用の識別番号であり、強さの順位ではありません。

## 国家の特徴

### 強み

*執筆中。*

### 弱み

*執筆中。*

## 兵士

### 主力兵

*執筆中。*

### Sacred

*執筆中。*

### 特殊・外国Recruit

*執筆中。*

## Commander / Mage

*執筆中。*

## Magic Path

| Path | Recruit-anywhere | Capital-only | Random / 条件付き |
|---|---:|---:|---|
| Fire | — | — | — |
| Air | — | — | — |
| Water | — | — | — |
| Earth | — | — | — |
| Astral | — | — | — |
| Death | — | — | — |
| Nature | — | — | — |
| Glamour | — | — | — |
| Blood | — | — | — |
| Holy | — | — | — |

## Pretender方針

*執筆中。*

## 序盤拡張

*執筆中。*

## Researchルート

### 最初のBreakpoint

*執筆中。*

### 第一戦争

*執筆中。*

### 中盤以降

*執筆中。*

## 重要Spell・召喚

*執筆中。*

## 重要Magic Item

*執筆中。*

## Army構成・Battle Script

*執筆中。*

## Counterされるもの

*執筆中。*

## 対人戦

*執筆中。*

## 情報源・検証

- Dominions 6 ゲーム内Nation Overview
- Dominions 6 Manual / Change log
- Dominions 6 Mod Inspectorのvanilla nation data
- Battle Replay・実機テスト

!!! warning
    旧作の国家ページは設計思想の参考にはなりますが、Dom6ではMagic Path、兵数、Spell、騎乗、戦場地形などが変更されています。数値をそのまま移植しないでください。
"""


def index(rows: list[dict[str, str]], era: str) -> str:
    code, _directory, era_name = ERA[era]
    selected = [row for row in rows if row["era"] == era]
    out = [
        "---",
        f'title: "{era_name} 国家一覧"',
        "status: catalog",
        'verified_version: "6.35"',
        'last_verified: "2026-08-14"',
        "---",
        "",
        f"# {era_name}（{code}）国家一覧",
        "",
        f"Dominions 6.35のvanilla国家を、現行のnation dataに基づいて整理しています。{era_name}には**{len(selected)}国家**あります。",
        "",
        "- [国家ページの読み方](../how-to-read.md)",
        "- [国家選択ガイド](../choose-a-nation.md)",
        "",
        "## 国家一覧",
        "",
        "| ID | 国家 | Epithet | 記事状態 |",
        "|---:|---|---|---|",
    ]
    for row in selected:
        status = frontmatter_status(page_path(row))
        label = STATUS_LABELS.get(status, status)
        out.append(
            f'| {row["id"]} | [{code} {row["name"]}]({row["slug"]}.md) | '
            f'{row["epithet"]} | {label} |'
        )
    out.extend(
        [
            "",
            "## 記事状態について",
            "",
            "- **骨組み**: 公式名称・Epithet・Nation IDと共通見出しを登録済み。",
            "- **下書き**: 兵種・Mage・Researchなどの主要項目を執筆中。",
            "- **攻略あり**: 実戦的な運用方針まで記述済み。Patch確認は継続する。",
            "- **検証済み**: 記載バージョンで数値・挙動の確認を終えた記事。",
            "",
            "!!! note \"国家数とPatch\"",
            "    新国家が追加されることがあります。国家数、名称、EpithetはPatch更新時にデータと照合します。",
            "",
        ]
    )
    return "\n".join(out)


def main() -> None:
    rows = read_rows()
    created = 0
    skipped = 0

    for row in rows:
        path = page_path(row)
        path.parent.mkdir(parents=True, exist_ok=True)
        if is_generated_stub(path):
            path.write_text(stub(row), encoding="utf-8")
            created += 1
        else:
            skipped += 1

    for era, (_code, directory, _name) in ERA.items():
        (DOCS / directory / "index.md").write_text(index(rows, era), encoding="utf-8")

    print(f"generated/updated stubs: {created}")
    print(f"preserved authored pages: {skipped}")


if __name__ == "__main__":
    main()
