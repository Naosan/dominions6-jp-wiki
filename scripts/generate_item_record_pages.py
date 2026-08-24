#!/usr/bin/env python3
"""Generate lightweight per-Item record pages and link generated Item tables.

The existing Item generators are optimized for cross-cutting indexes.  This
supplement creates one compact page per Magic Item so a reader can move from an
Item name to its forge/acquisition facts and then into the specialized Weapon,
Armor, effect, summon, risk, and strategy indexes without duplicating those
large tables on every page.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import generate_item_effect_data as effect_data
import generate_spell_item_data as core

ITEM_OUT = core.ITEM_OUT
BY_ID = ITEM_OUT / "by-id"
STRATEGY_DIR = core.ROOT / "docs" / "items" / "encyclopedia"
START = "<!-- item-record-index:start -->"
END = "<!-- item-record-index:end -->"
ITEM_ID_RE = re.compile(r"(?m)^item_id:\s*([0-9]+)\s*$")
UNFORGEABLE_CLASSES = {
    11: "Unforgeable item",
    13: "Unforgeable unique artifact",
    15: "Unforgeable unique per-nation artifact",
}
FORGE_LEVELS = {1, 3, 5, 7, 9}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    return parser.parse_args()


def normalized_traits(item: dict[str, object]) -> str:
    """Keep the old core parser's crown label from leaking into new records."""
    text = str(item.get("traits_text") or "—")
    return text.replace("Artifact / Crown", "Crown")


def acquisition_label(item: dict[str, object]) -> str:
    const = int(item["const"])
    if const == 9:
        return "Construction 9 Artifact (forgeable / unique)"
    if const in UNFORGEABLE_CLASSES:
        return UNFORGEABLE_CLASSES[const]
    return str(item["construction"])


def display_cost(item: dict[str, object]) -> str:
    """Never present an unforgeable class as having a normal Forge cost."""
    if int(item["const"]) in UNFORGEABLE_CLASSES:
        return "—"
    return str(item["cost"])


def strategy_pages(strategy_dir: Path = STRATEGY_DIR) -> dict[int, Path]:
    """Map hand-written per-Item strategy pages to their stable Item IDs."""
    pages: dict[int, Path] = {}
    if not strategy_dir.exists():
        return pages
    for path in sorted(strategy_dir.glob("*.md")):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        match = ITEM_ID_RE.search(text)
        if match is None:
            raise ValueError(f"Magic Item strategy page is missing item_id: {path}")
        item_id = int(match.group(1))
        if item_id in pages:
            raise ValueError(
                f"duplicate Magic Item strategy item_id {item_id}: {pages[item_id]} and {path}"
            )
        pages[item_id] = path
    return pages


def relative_link(target: Path, from_path: Path) -> str:
    return os.path.relpath(target, start=from_path.parent).replace(os.sep, "/")


def special_features(raw: dict[str, str]) -> list[str]:
    features: list[str] = []
    for specs in (
        effect_data.DIRECT_EFFECT_FIELDS,
        effect_data.SUMMON_FIELDS,
        effect_data.RISK_RESTRICTION_FIELDS,
    ):
        features.extend(effect_data.explicit_features(raw, specs))
    return features


def related_links(item: dict[str, object], raw: dict[str, str]) -> list[str]:
    links = [
        f"[Slot / Type一覧](../by-type/{item['type_slug']}.md)",
    ]
    const = int(item["const"])
    if const in FORGE_LEVELS:
        links.append(f"[Construction {const} Item](../by-construction/c{const}.md)")
    if const == 9:
        links.append("[Artifact一覧](../artifacts.md)")
    if const in UNFORGEABLE_CLASSES:
        links.append("[Unforgeable Item一覧](../unforgeable.md)")
    if str(item["boosters"]) != "—":
        links.append("[Magic Path Booster一覧](../boosters.md)")
    if int(item["research"]) != 0:
        links.append("[Research Item一覧](../research.md)")
    if bool(item["has_resistance"]):
        links.append("[Resistance / MR Item一覧](../resistance.md)")
    if bool(item["has_utility"]):
        links.append("[Utility Item一覧](../utility.md)")
    if core.num(raw, "weapon"):
        links.append("[Magic Item Weapon profile](../weapon-profiles.md)")
    if core.num(raw, "armor"):
        links.append("[Magic Item Armor profile](../armor-profiles.md)")
    if effect_data.explicit_features(raw, effect_data.DIRECT_EFFECT_FIELDS):
        links.append("[Item Spell・自動効果](../active-effects.md)")
    if effect_data.explicit_features(raw, effect_data.SUMMON_FIELDS):
        links.append("[Summon・Retinue効果](../summoning-effects.md)")
    if effect_data.explicit_features(raw, effect_data.RISK_RESTRICTION_FIELDS):
        links.append("[副作用・装備制限](../risk-restrictions.md)")
    if effect_data.raw_value(raw, "mustfightinarena") or effect_data.raw_value(raw, "arenareward"):
        links.append("[Arena関連Magic Item](../arena.md)")
    return links


def record_page(
    item: dict[str, object],
    raw: dict[str, str],
    strategy_href: str | None = None,
) -> str:
    name = core.esc(item["name"])
    features = special_features(raw)
    links = related_links(item, raw)
    lines = [
        "---",
        f'title: "{str(item["name"]).replace(chr(34), chr(39))}"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {core.COMMIT}"',
        f"item_id: {item['id']}",
        "---",
        "",
        f"# {name}",
        "",
        "Dominions 6.35固定データから生成したMagic Item個別recordです。攻略判断は用途別・任務別・個別攻略記事、特殊効果の詳細は各専門索引へ分離しています。",
        "",
        "| 項目 | 値 |",
        "|---|---|",
        f"| Item ID | {item['id']} |",
        f"| Slot / Type | {core.esc(item['type_title'])} |",
        f"| Research / Acquisition | {core.esc(acquisition_label(item))} |",
        f"| Forge requirement | {core.esc(item['path'])} |",
        f"| Base Gem cost | {core.esc(display_cost(item))} |",
        f"| Magic Path Booster | {core.esc(item['boosters'])} |",
        f"| Base equipment | {core.esc(item['base'])} |",
        f"| 主要Effects | {core.esc(normalized_traits(item))} |",
        f"| Restriction | {core.esc(item['restriction'])} |",
        "",
    ]
    if int(item["const"]) == 9:
        lines += [
            "!!! note \"Artifact / Yearning\"",
            "    Construction 9 Artifactはuniqueです。Yearningはゲーム進行中の状態なので、このrecordのGem costには反映しません。現在の支払額はゲーム内Forge画面を確認してください。",
            "",
        ]
    if int(item["const"]) in UNFORGEABLE_CLASSES:
        lines += [
            "!!! note \"Unforgeable\"",
            "    このItemは通常のForge Itemで作るclassではありません。入手経路はArena、Event、国家固有、特殊生成など個別に確認してください。",
            "",
        ]
    if features:
        lines += [
            "## 明示された特殊field",
            "",
            *[f"- {core.esc(feature)}" for feature in features],
            "",
            "!!! warning \"field名以上の意味を推測しない\"",
            "    発動Timing、対象、回数、召喚Unit等はゲーム内Item詳細とDom6 Mod Inspectorを最終確認してください。",
            "",
        ]
    if strategy_href:
        lines += [
            "## 個別攻略",
            "",
            f"- [このItemの手書き攻略]({strategy_href})",
            "",
            "generated recordは固定値、手書き攻略は用途・Carrier・組み合わせ・Counterを担当します。",
            "",
        ]
    lines += [
        "## 関連データ",
        "",
        *[f"- {link}" for link in links],
        "",
        "## 攻略へ戻る",
        "",
        "- [Magic Item攻略辞典](../../../items/encyclopedia/index.md)",
        "- [用途別Magic Item辞典](../../../items/purpose-dictionary.md)",
        "- [任務別Magic Item Loadout](../../../items/mission-loadouts.md)",
        "- [Item固有効果・Weapon proc・副作用](../../../items/effects-and-procs.md)",
        "- [Magic Item総論](../../../items/index.md)",
        "",
        "!!! note \"Source of truth\"",
        "    このページはpin済みDominions 6.35 Inspector snapshotの事実索引です。Patch後の現在値はゲーム内表示とDom6 Mod Inspectorを優先してください。",
        "",
    ]
    return "\n".join(lines)


def records_index_page(items: list[dict[str, object]]) -> str:
    lines = [
        "---",
        'title: "Magic Item個別record一覧"',
        "status: generated",
        'verified_version: "6.35"',
        f'generated_from: "dom6inspector {core.COMMIT}"',
        "---",
        "",
        "# Magic Item個別record一覧",
        "",
        f"Magic Item **{len(items)}**件を、Item IDごとの軽量recordへまとめています。",
        "",
        "[Magic Itemデータ索引へ戻る](index.md) · [Magic Item攻略辞典](../../items/encyclopedia/index.md)",
        "",
        "| Item | ID | Slot | Research / Acquisition | Req | Gem | 主要Effects |",
        "|---|---:|---|---|---|---|---|",
    ]
    for item in items:
        lines.append(
            f"| [{core.esc(item['name'])}](by-id/{item['id']}.md) | {item['id']} | "
            f"{core.esc(item['type_title'])} | {core.esc(acquisition_label(item))} | "
            f"{core.esc(item['path'])} | {core.esc(display_cost(item))} | {core.esc(normalized_traits(item))} |"
        )
    lines += ["", ""]
    return "\n".join(lines)


def index_block(count: int) -> str:
    return "\n".join(
        [
            START,
            "## 個別Item record",
            "",
            f"- [Magic Item個別record一覧](records.md) — {count} records",
            "- [Magic Item攻略辞典](../../items/encyclopedia/index.md) — Item名から用途・Carrier・Counterを読む手書き層",
            "",
            "Item名からForge条件、Slot、主要効果、Restrictionを一ページで確認し、個別攻略、Weapon / Armor / Spell / Summon / 副作用などの専門索引へ移動できます。",
            END,
            "",
        ]
    )


def patch_item_index(count: int, item_out: Path = ITEM_OUT) -> None:
    path = item_out / "index.md"
    text = path.read_text(encoding="utf-8")
    block = index_block(count)
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


def item_record_link(item_id: int, from_path: Path, item_out: Path = ITEM_OUT) -> str:
    target = item_out / "by-id" / f"{item_id}.md"
    return relative_link(target, from_path)


def link_generated_item_tables(
    items: list[dict[str, object]],
    item_out: Path = ITEM_OUT,
) -> tuple[int, int]:
    """Link table rows whose first two cells exactly match an Item name and ID."""
    expected = {int(item["id"]): core.esc(item["name"]) for item in items}
    row_re = re.compile(r"^(\|\s*)([^|]+?)(\s*\|\s*)(\d+)(\s*\|.*)$")
    changed_files = 0
    linked_rows = 0
    by_id = item_out / "by-id"
    records = item_out / "records.md"

    for path in sorted(item_out.rglob("*.md")):
        if path == records or by_id in path.parents:
            continue
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        changed = False
        for index, line in enumerate(lines):
            match = row_re.match(line)
            if not match:
                continue
            item_id = int(match.group(4))
            name = match.group(2).strip()
            if item_id not in expected or name != expected[item_id]:
                continue
            target = item_record_link(item_id, path, item_out)
            linked_name = f"[{name}]({target})"
            lines[index] = (
                match.group(1)
                + linked_name
                + match.group(3)
                + match.group(4)
                + match.group(5)
            )
            linked_rows += 1
            changed = True
        if changed:
            path.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")
            changed_files += 1
    return changed_files, linked_rows


def write_records(
    items: list[dict[str, object]],
    raw_by_id: dict[int, dict[str, str]],
    item_out: Path = ITEM_OUT,
    strategy_dir: Path = STRATEGY_DIR,
) -> tuple[int, int]:
    by_id = item_out / "by-id"
    by_id.mkdir(parents=True, exist_ok=True)
    valid_names = {f"{int(item['id'])}.md" for item in items}
    item_ids = {int(item["id"]) for item in items}
    strategies = strategy_pages(strategy_dir)
    unknown_strategy_ids = sorted(set(strategies) - item_ids)
    if unknown_strategy_ids:
        raise ValueError(
            "Magic Item strategy pages reference unknown Item IDs: "
            + ", ".join(str(item_id) for item_id in unknown_strategy_ids)
        )

    removed = 0
    for path in by_id.glob("*.md"):
        if path.name not in valid_names:
            path.unlink()
            removed += 1

    written = 0
    for item in items:
        item_id = int(item["id"])
        raw = raw_by_id.get(item_id)
        if raw is None:
            raise ValueError(f"missing BaseI record for Item {item_id}: {item['name']}")
        target = by_id / f"{item_id}.md"
        strategy_href = (
            relative_link(strategies[item_id], target)
            if item_id in strategies
            else None
        )
        target.write_text(
            record_page(item, raw, strategy_href=strategy_href),
            encoding="utf-8",
        )
        written += 1
    (item_out / "records.md").write_text(records_index_page(items), encoding="utf-8")
    return written, removed


def main() -> None:
    args = parse_args()
    names = ("BaseI.csv", "weapons.csv", "armors.csv")
    paths = {name: core.source(name, args.refresh, args.offline) for name in names}
    items = core.item_rows(paths)
    raw_by_id = {
        core.num(row, "id"): row
        for row in core.tsv(paths["BaseI.csv"])
        if core.num(row, "id")
    }
    if len(items) < 500:
        raise ValueError(f"Magic Item record set appears incomplete: {len(items)}")

    written, removed = write_records(items, raw_by_id)
    patch_item_index(len(items))
    changed_files, linked_rows = link_generated_item_tables(items)

    print(f"generated Magic Item by-id records: {written}")
    print(f"removed stale Magic Item records: {removed}")
    print(f"Item table files linked to by-id records: {changed_files}")
    print(f"Item table rows linked to by-id records: {linked_rows}")


if __name__ == "__main__":
    main()
