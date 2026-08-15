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
python scripts/generate_magic_site_data.py
python scripts/generate_site_search_data.py --offline
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
python scripts/generate_magic_site_data.py
python scripts/generate_site_search_data.py --offline
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
11. Unit / NationのStrategic summon、Battle summon、Recruit unlock、Conversion、Reanimation、Freespawnを生成
12. EventのUnit生成・変身・暗殺参加者とMercenary rosterを生成
13. Magic Itemの固定Unit summon、Retinue、Battle summon、変身・Raise・Encounterを生成
14. SpellのNegative summon pool、Wish、Unique summon、Terrain-specific summon等を生成
15. Arena関連Magic Itemを生成
16. 全1,253 Magic SiteページとGem・Recruit・Summon・Event横断索引を生成
17. Site Level分布とRemote Site Search Spell索引を生成
18. Zensicalで静的サイトを構築
19. GitHub Pagesへ公開

## 記事を書く

手書き記事は `docs/` 配下のMarkdownです。

```text
docs/
  basics/weapons-and-shields.md
  magic/site-search.md
  magic/site-search-playbook.md
  magic/paths/earth.md
  nations/ma/ulm.md
```

国家の自動生成Stubは、同じPathに手書き記事が存在すると上書きされません。Front Matterの `status: stub` を `status: draft` などへ変更すると、執筆済み記事として保護されます。

## データ生成

### 国家カタログ

```bash
python scripts/generate_nation_catalog.py
```

入力: `data/nations.tsv`

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

### 装備使用者逆引き

```bash
python scripts/generate_equipment_usage_data.py --offline
```

生成先: `docs/data/equipment-usage/`

Hero、Event、Freespawn、召喚、Site限定UnitはこのRecruit逆引きの対象外です。これらはUnit総合索引で別レイヤーとして扱います。

### Spell / Magic Item

```bash
python scripts/generate_spell_item_data.py
```

生成先:

```text
docs/data/spells/
docs/data/items/
```

### Weapon / Armor / Damage property

```bash
python scripts/generate_combat_data.py
```

生成先: `docs/data/combat/`

### Unit総合索引

```bash
python scripts/generate_unit_catalog.py
```

生成先:

```text
docs/data/units/
├ index.md
├ all/
├ by-id/
├ pretenders.md
├ heroes.md
├ spell-summons.md
├ spell-random-summons.md
├ special-summons.md
├ magic-sites.md
├ event-spawns.md
├ event-transforms.md
├ event-combat.md
├ event-random.md
├ mercenaries.md
├ item-unit-sources.md
├ item-random.md
├ strategic-spawns.md
├ battle-spawns.md
├ recruit-unlocks.md
├ conversions.md
├ reanimation.md
├ nation-generation.md
├ random-summons.md
├ mounts.md
├ shapes.md
├ unclassified.md
└ data-quality.md

docs/data/items/
└ arena.md
```

Unit総合索引はBaseUの全4,091 recordを個別ページ化し、次の明示的な参照を結合します。

- 国家Recruit mapping
- `attributes_by_nation.csv`の`hero1..6` / `multihero1..2`
- `pretender_types_by_nation.csv`
- Research可能Spellの固定Unit summon effect
- `MagicSites.csv`のUnit参照
- `events.csv`のCommander・Troop生成、変身、暗殺・随伴Unit
- `Mercenary.csv`のCommander・Troop roster
- `BaseI.csv`の`sumrit`、`sumauto`、`sumbat`、`retinue`、`summoner1d6`、`summoner2d6`
- `BaseI.csv`の`batstartsum2`、`batstartsum3`、`batstartsum5d6`
- `BaseI.csv`の`transformwearer`、`raiseshape`、`defender`
- `domsummon`、`makemonster`、`summon`、`autosum`
- `batstartsum*`、`battlesum*`
- `ownsmonrec`、`monpresentrec`
- `mummify`、`twiceborn`、`lich`、`animatemnr`、`raiseshape`
- Nation attributeが明示するGuardian Spirit、Freespawn、Reanimation
- `mountmnr`
- BaseUのShape参照とXP / HP threshold型の形態変化

Eventについては、Effectの`nation -1`をRandom enemy、`nation -2`をProvince ownerとして保持し、`tempunits 1`をTemporaryとして分離します。Eventに登場するUnitを自動的に恒久加入扱いにはしません。

Mercenaryについては、Commander、Troop、初期人数、Era mask、最低入札額、XP、補充率、開始Itemを索引化します。

Magic Itemについては、固定Unit IDへ解決できる召喚・Retinue・Battle summon・変身・Raise・敵対EncounterだけをUnitページへ接続します。Item固有の使用回数、発動条件、持続時間はゲーム内説明を優先します。

Spellについては、通常の固定Unit summonに加えて、Negative Monster Number、Montag、`special_unique_summons.csv`、`terrain_specific_summons.csv`を候補集合として索引化します。Wish、Cross Breeding、Tartarian Gate等の特殊処理を、名前や説明文から単一Unitへ推測で接続しません。

負のMonster NumberとMontagはRandom poolとして表示し、固定Unitへは結び付けません。Reanimation結果などhard-codedな生成先を安全に対応付けられない場合も、能力Flagと品質レポートへ残します。

### Magic Site総合索引

```bash
python scripts/generate_magic_site_data.py
```

生成先:

```text
docs/data/sites/
├ index.md
├ all.md
├ by-id/              # 全1,253 Site個別ページ
├ by-path/            # F / A / W / E / S / D / N / G / B / H
├ gem-income.md
├ recruitment.md
├ summons.md
├ research.md
├ economy.md
├ enter-effects.md
├ national.md
├ terrain.md
├ thrones.md
├ events.md
└ data-quality.md
```

Magic Site索引は次の明示データを結合します。

- `MagicSites.csv`の全1,253 record
- Path、Site level、raw Rarity、`loc` bitfield
- 毎月のGem incomeとClaim時Gemを別Fieldとして保持
- `mon*` / `com*` / `hmon*` / `hcom*` / `natmon` / `natcom`
- `sum1..4` / `n_sum1..4`
- Site固有のProvince Defence追加Unit
- Gold、Resource、Supply、Unrest、Recruitment Point、Population
- Fort、Laboratory、Research School bonus、Ritual range
- Scales、Dominion、Entering Site、Scry、Adventure、Void Gate
- Nation属性が明示するStart Site / Future Site
- Event requirementの`site` / `foundsite` / `hiddensite` / `nearbysite`
- Event effectの`newsite`

正のUnit IDはBaseUに存在する場合だけ接続し、raw Rarityを出現確率の百分率へ変換しません。`loc = 0`は「全地形へ通常出現」と断定せず、未知のLocation bitも消さずに品質レポートへ残します。同名Siteは同一視せず、異なるSite IDのrecordとして保持します。

### Site Search参照

```bash
python scripts/generate_site_search_data.py --offline
```

生成先:

```text
docs/data/sites/search-levels.md
docs/data/spells/site-search.md
```

Site Search参照は次を生成します。

- Path別のSearch Level分布
- raw Rarity 0–2 SiteのL1 / L2 / L3 / L4累積record数
- Level 4以上の通常・特殊Site一覧
- effect 48とPath argumentによる九Pathの単一Path Remote Search抽出
- `Mirror of Earth's Memories`、`Voice of Tiamat`、`Acashic Knowledge`の特殊Search分離
- Research、要求Path、Gem / Blood Slave Cost、Search scope
- Holy専用Remote Searchが現行Researchable setにないことの整合性確認

手書き攻略は次です。

```text
docs/magic/site-search.md
docs/magic/site-search-playbook.md
```

生成データはSite recordとSpellの事実、手書き記事はManual / Remoteの選択、Searcherの機会費用、Search Route、戦争前の中止条件を扱います。

## データ更新

生成元はDom6 InspectorのDominions 6.35対応Commitへ固定しています。ダウンロード済みデータは `.cache/dom6inspector/` に保存されます。

```bash
# 強制的に再取得
python scripts/generate_recruitment_data.py --refresh
python scripts/generate_equipment_usage_data.py --refresh
python scripts/generate_spell_item_data.py --refresh
python scripts/generate_combat_data.py --refresh
python scripts/generate_unit_catalog.py --refresh
python scripts/generate_magic_site_data.py --refresh
python scripts/generate_site_search_data.py --refresh

# Networkを使用せずCacheのみで生成
python scripts/generate_recruitment_data.py --offline
python scripts/generate_equipment_usage_data.py --offline
python scripts/generate_spell_item_data.py --offline
python scripts/generate_combat_data.py --offline
python scripts/generate_unit_catalog.py --offline
python scripts/generate_magic_site_data.py --offline
python scripts/generate_site_search_data.py --offline
```

自動生成ページは攻略評価ではなく、現行データを確認するための索引です。戦術、研究順、Pretender、Script、Counterは手書き記事で扱います。