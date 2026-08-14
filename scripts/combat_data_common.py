from __future__ import annotations

import argparse
import csv
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "data" / "combat"
WEAPON_OUT = OUT / "weapons"
ARMOR_OUT = OUT / "armor"
COMMIT = "cfac4311bc0b58053b8dead7bffbc036ba9bd5dc"
BASE = f"https://raw.githubusercontent.com/larzm42/dom6inspector/{COMMIT}/gamedata"
CACHE = ROOT / ".cache" / "dom6inspector" / COMMIT
FILES = (
    "weapons.csv", "effects_weapons.csv", "effect_modifier_bits.csv",
    "effects_info.csv", "special_damage_types.csv",
    "attributes_by_weapon.csv", "attribute_keys.csv", "armors.csv",
    "protections_by_armor.csv", "attributes_by_armor.csv",
)
TYPE_NAMES = {4: "盾", 5: "胴鎧", 6: "兜", 8: "Misc防具"}
TYPE_SLUGS = {4: "shields", 5: "body-armor", 6: "helmets", 8: "misc-armor"}
BITS = {
    "strength": 1, "two_handed": 2, "fire": 32,
    "armor_piercing": 64, "armor_negating": 128,
    "soul_slaying": 256, "cold": 512, "shock": 2048,
    "mr_negates": 4096, "poison": 8192, "ignore_shield": 16384,
    "sacred_only": 32768, "mindless_immune": 131072,
    "enemy_only": 262144, "undead_immune": 524288,
    "defense_negate": 1048576, "nonmagical": 2097152,
    "underwater_ok": 8388608, "mr_negates_easily": 16777216,
    "iron": 67108864, "intrinsic": 134217728,
    "charge": 2147483648, "beam": 4294967296,
    "false_damage": 17179869184, "heavy_charge": 68719476736,
    "cannot_repel": 137438953472, "piercing": 274877906944,
    "blunt": 549755813888, "slashing": 1099511627776,
    "acid": 2199023255552, "size_or_strength_negates": 4398046511104,
    "hard_mr_negates": 17592186044416,
    "cannot_be_repelled": 35184372088832, "hit_head": 562949953421312,
    "true_damage": 18014398509481984, "internal_damage": 36028797018963968,
    "magic_damage": 72057594037927936, "half_strength": 288230376151711744,
    "extra_effect": 576460752303423488,
    "extra_effect_on_damage": 1152921504606846976,
    "mr_half_damage": 2305843009213693952,
    "third_strength": 4611686018427387904,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    return parser.parse_args()


def tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def num(row: dict[str, str], key: str, default: int = 0) -> int:
    try:
        return int(float(row.get(key) or default))
    except (TypeError, ValueError):
        return default


def esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def clean_label(value: str) -> str:
    return re.sub(r"\s*\{.*?\}\s*", "", value or "").replace("<", "").replace(">", "").strip()


def source(name: str, refresh: bool, offline: bool) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / name
    if path.exists() and path.stat().st_size and not refresh:
        return path
    if offline:
        raise FileNotFoundError(f"offline cache missing: {path}")
    request = urllib.request.Request(
        f"{BASE}/{name}", headers={"User-Agent": "dominions6-jp-wiki/1.0"}
    )
    error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                data = response.read()
            if not data:
                raise RuntimeError("empty download")
            path.write_bytes(data)
            return path
        except (urllib.error.URLError, TimeoutError, RuntimeError) as exc:
            error = exc
            time.sleep(2**attempt)
    raise RuntimeError(f"download failed: {name}: {error}")


def has(mask: int, key: str) -> bool:
    return bool(mask & BITS[key])
