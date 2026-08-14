# Dominions 6 日本語攻略Wiki

Dominions 6 - Rise of the Pantokrator の日本語攻略・仕様・データWikiです。

公開サイト:

- https://naosan.github.io/dominions6-jp-wiki/

## ローカルで確認する

```bash
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
pip install zensical
python scripts/generate_nation_catalog.py
python scripts/generate_recruitment_data.py
python scripts/generate_equipment_usage_data.py --offline
python scripts/generate_spell_item_data.py
python scripts/generate_combat_data.py
python scripts/generate_unit_catalog.py
zensical serve
```

### macOS / Linux

```bash
source .venv/bin/activate
pip install zensical
python scripts/generate_nation_catalog.py
python scripts/generate_recruitment_data.py
python scripts/generate_equipment_usage_data.py --offline
python scripts/generate_spell_item_data.py
python scripts/generate_combat_data.py
python scripts/generate_unit_catalog.py
zensical serve
```

ブラウザで `http://localhost:8000` を開きます。

## 公開

`main` ブランチへpushすると、GitHub Actionsが次を自動実行します。

1. 103国家の一覧と未執筆Stubを生成
2. Dom6 Inspector 6.35 snapshotからRecruit / Mage access索引を生成
3. Recruit UnitへWeapon / Armor / Mount recordを結合
4. Weapon / ArmorからRecruit・Mountを逆引きする使用者索引を生成
5. 盾・両手・射撃・AP・AN・Charge・Mountedの横断Profileを生成
6. SpellのSchool / Path / National索引を生成
7. Magic ItemのSlot / Booster / Research / Resistance索引を生成
8. Weapon / Armor / Damage property索引を生成
9. BaseUの全4,091 Unitページと入手経路索引を生成
10. Hero、Pretender、Spell summon、Magic Site、Mount、Shapeの関係を生成
11. Zensicalで静的サイトを構築
12. GitHub Pagesへ公開

## 記事を書く

手書き記事は `docs/` 配下のMarkdownです。

```text
docs/
  basics/weapons-and-shields.md
  magic/paths/earth.md
  nations/ma/ulm.md
```

国家の自動生成Stubは、同じPathに手書き記事が存在すると上書きされません。Front Matterの `status: stub` を `status: draft` などへ変更すると、執筆済み記事として保護されます。

## データ生成

### 国家カタログ

```bash
python scripts/generate_nation_catalog.py
```

入力:

```text
data/nations.tsv
```

### Recruit / Mage access / Unit loadout

```bash
python scripts/generate_recruitment_data.py
```

生成ページ:

```text
docs/data/recruitment/
docs/data/mage-access.md
```

国家別Recruitページでは、`BaseU.csv`の`wpn1..7`、`armor1..4`、`mountmnr`をWeapon / Armor / Mount recordへ結合します。

表示する主な内容:

- Unit基礎能力
- 固定Magic PathとRandom Path
- WeaponのDamage、Attack / Precision、Length / Range、Damage type、AP / AN
- Shield Protection、Parry、Body / Head Protection、Encumbrance
- Riderとは別のMount HP・Protection・攻撃・防具
- 盾持ち、両手、射撃、Charge等の簡易Profile

自動表は最終Damage、二刀流処理、Shape Change、Gold Costを完全には再構成しません。戦術評価は手書き攻略で扱います。

### 装備使用者逆引き

```bash
python scripts/generate_equipment_usage_data.py --offline
```

`generate_recruitment_data.py`が取得した固定スナップショットを再利用し、次を生成します。

```text
docs/data/equipment-usage/
├ index.md
├ nations.md
├ weapons/
├ armor/
└ profiles/
```

- 全Weapon / Armor recordの個別使用者ページ
- Recruit本体とMountの使用を分離した逆引き
- 国家別の装備Profile比較
- 盾、両手、射撃、AP、AN、Charge、Mountedの横断一覧

Hero、Event、Freespawn、召喚、Site限定UnitはこのRecruit逆引きの対象外です。これらはUnit総合索引で別レイヤーとして扱います。

### Spell / Magic Item

```bash
python scripts/generate_spell_item_data.py
```

生成ページ:

```text
docs/data/spells/
docs/data/items/
```

### Weapon / Armor / Damage property

```bash
python scripts/generate_combat_data.py
```

生成ページ:

```text
docs/data/combat/
```

武器は近接・射撃・AP/AN・属性・特殊効果へ、防具は盾・胴鎧・兜へ分類します。Weapon modifier bitと特殊Damage bitの技術索引も生成します。

### Unit総合索引

初回はPretender、Hero、Magic Site等の追加CSVを取得するためNetworkを使用します。

```bash
python scripts/generate_unit_catalog.py
```

生成ページ:

```text
docs/data/units/
├ index.md
├ all/
├ by-id/
├ pretenders.md
├ heroes.md
├ spell-summons.md
├ magic-sites.md
├ mounts.md
├ shapes.md
├ unclassified.md
└ data-quality.md
```

Unit総合索引はBaseUの全4,091 recordを個別ページ化し、次の明示的な参照を結合します。

- 国家Recruit mapping
- `attributes_by_nation.csv`の`hero1..6` / `multihero1..2`
- `pretender_types_by_nation.csv`
- Research可能Spellの固定Unit summon effect
- `MagicSites.csv`のUnit参照
- `mountmnr`
- BaseUの直接Shape参照

Event、Freespawn、Random summon pool、Wish、Transformation等を安全に対応付けられない場合は、推測せず`unclassified.md`と`data-quality.md`へ残します。

生成元はDom6 InspectorのDominions 6.35対応Commitへ固定しています。ダウンロード済みデータは `.cache/dom6inspector/` に保存されます。

```bash
# 強制的に再取得
python scripts/generate_recruitment_data.py --refresh
python scripts/generate_equipment_usage_data.py --refresh
python scripts/generate_spell_item_data.py --refresh
python scripts/generate_combat_data.py --refresh
python scripts/generate_unit_catalog.py --refresh

# Networkを使用せずCacheのみで生成
python scripts/generate_recruitment_data.py --offline
python scripts/generate_equipment_usage_data.py --offline
python scripts/generate_spell_item_data.py --offline
python scripts/generate_combat_data.py --offline
python scripts/generate_unit_catalog.py --offline
```

自動生成ページは攻略評価ではなく、現行データを確認するための索引です。戦術、研究順、Pretender、Script、Counterは手書き記事で扱います。
