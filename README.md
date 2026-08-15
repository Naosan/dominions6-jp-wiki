# Dominions 6 日本語攻略Wiki

**Dominions 6 - Rise of the Pantokrator**の日本語攻略・仕様・データWikiです。

公開Site: <https://naosan.github.io/dominions6-jp-wiki/>

## 開発方針

このWikiは、単にData Pageを増やすのではなく、次を同時に満たすことを目標にしています。

- Unit、Spell、Item、Siteなどの事実を再生成できる
- CombatやMagicの仕様と、攻略上の評価を区別できる
- 初心者が国家選択から最初の戦争まで辿れる
- 記事の状態、対象Version、未検証事項を確認できる
- Patch後に差分を確認しながら更新できる

詳細は[開発方針と完成条件](docs/reference/development-policy.md)を参照してください。

## Localで確認する

Python 3.12を使用します。依存Packageは`requirements.txt`へ固定しています。

```bash
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/build_wiki.py --serve
```

### macOS / Linux

```bash
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/build_wiki.py --serve
```

Browserで`http://localhost:8000`を開きます。

### Build mode

```bash
# 全Dataを生成して静的SiteをBuild
python scripts/build_wiki.py

# Cacheだけを使用し、Networkへ接続しない
python scripts/build_wiki.py --offline

# 固定SourceからCacheを再取得
python scripts/build_wiki.py --refresh

# Markdown生成だけを実行
python scripts/build_wiki.py --generate-only
```

`scripts/build_wiki.py`がLocalとGitHub Actionsで共有する正式なPipelineです。生成Stepを追加・削除する場合は、WorkflowへCommandを重複記述せず、このFileを更新します。

## Testと品質Audit

```bash
python -m unittest discover -s tests -v
python scripts/audit_wiki.py --report build/wiki-audit.json
```

Auditは、Front Matter、内部Link、Zensical Navigation、記事Status、孤立Pageを検査します。Defaultでは構造的な破損をErrorとし、既存記事を段階的に整備できるようMetadata不足と孤立PageはWarningとして集計します。

## GitHub Pagesへの公開

`main`へPushすると、GitHub Actionsが次を実行します。

1. 固定したPythonとZensicalをInstall
2. Wiki toolのUnit test
3. 国家一覧と未執筆Stubを生成
4. Recruit、Mage access、Unit装備を生成
5. Recruit装備参照を検証
6. Weapon・Armorから使用者を逆引き
7. SpellとMagic Item索引を生成
8. Weapon、Armor、Damage property索引を生成
9. 全Unitと入手経路を生成
10. 全Magic Siteと関連Dataを生成
11. Site Search参照を生成
12. 国家別Site Search能力を生成
13. Extended Magic Accessを生成
14. Magic Access routeを生成
15. Zensicalで静的SiteをBuild
16. 内部Link、Navigation、MetadataをAudit
17. GitHub PagesへDeploy

Pull Requestと`main`以外のBranchでも、同じBuildとAuditを実行します。

## 記事を書く

手書き記事は`docs/`配下のMarkdownです。

```text
docs/
  basics/weapons-and-shields.md
  magic/site-search.md
  magic/site-search-playbook.md
  magic/paths/earth.md
  nations/ma/ulm.md
```

記事にはFront Matterを付けます。

```yaml
---
title: 記事名
page_type: guide
status: draft
verified_version: "6.35"
last_verified: "2026-08-15"
---
```

数値や挙動を確認していない場合は、確認していないVersionや日付を記録しません。Statusの意味、生成Pageの扱い、Pull Request checklistは[CONTRIBUTING.md](CONTRIBUTING.md)にまとめています。

国家の自動生成Stubは、同じPathに手書き記事が存在すると上書きされません。`status: stub`を`status: draft`などへ変更すると、執筆済み記事として保護されます。

## Data生成

個別Generatorは調査やDebug用に直接実行できます。通常のBuildでは`scripts/build_wiki.py`を使用してください。

### 国家Catalog

```bash
python scripts/generate_nation_catalog.py
```

入力: `data/nations.tsv`

### Recruit・Mage access・Unit装備

```bash
python scripts/generate_recruitment_data.py
python scripts/check_recruitment_equipment_refs.py --offline
```

生成先:

```text
docs/data/recruitment/
docs/data/mage-access.md
docs/data/unit-loadouts.md
```

国家別Recruit Pageでは、`BaseU.csv`のWeapon、Armor、Mount参照を対応Recordへ結合します。

### 装備使用者逆引き

```bash
python scripts/generate_equipment_usage_data.py --offline
```

生成先: `docs/data/equipment-usage/`

RecruitとMountの装備使用者をWeapon・Armor側から逆引きし、Shield、Two-handed、Ranged、AP、AN、Charge、Mountedの横断Profileを生成します。Hero、Event、Freespawn、Summon、Site限定UnitはUnit総合索引で別Layerとして扱います。

### Spell・Magic Item

```bash
python scripts/generate_spell_item_data.py
```

生成先:

```text
docs/data/spells/
docs/data/items/
```

School、Path、National Spell、Item slot、Booster、Research、Resistanceなどを索引化します。

### Weapon・Armor・Damage property

```bash
python scripts/generate_combat_data.py
```

生成先: `docs/data/combat/`

### Unit総合索引

```bash
python scripts/generate_unit_catalog.py
```

生成先: `docs/data/units/`

BaseUの全Unit Recordを個別Page化し、次の明示的な関係を接続します。

- 国家Recruit mapping
- HeroとPretender chassis
- Spell、Magic Site、Event、Mercenary、Magic ItemによるUnit参照
- Strategic summonとBattle summon
- Recruit unlock、Conversion、Reanimation、Freespawn
- MountとShape relation
- Negative Monster Number、Montag、Wish、特殊Summon pool

Eventの相対Nation、Temporary Unit、Random poolなどは意味を保持し、安全な根拠なしに恒久加入や単一Unitへ変換しません。

### Magic Site総合索引

```bash
python scripts/generate_magic_site_data.py
```

生成先: `docs/data/sites/`

全Magic Site Recordを個別Page化し、Path、Level、Rarity、Location bit、Gem income、Recruit、Summon、Economy、Research、Terrain、Throne、Event relationを索引化します。

`loc = 0`や未知のLocation bitを推測で正規化せず、同名Siteも異なるIDのRecordとして保持します。

### Site Search参照

```bash
python scripts/generate_site_search_data.py --offline
python scripts/run_nation_site_search_data.py --offline
```

生成先:

```text
docs/data/sites/search-levels.md
docs/data/spells/site-search.md
docs/data/site-search/
```

Site Level分布、Remote Search Spell、国家別Recruitable MageのNative・Random-assisted到達可能性を生成します。Booster、Communion、Summon、PretenderはこのLayerへ混ぜません。

### Extended Magic Access

```bash
python scripts/run_extended_magic_access_data.py --offline
```

生成先: `docs/data/extended-magic-access/`

通常Recruitに加え、Site Mage、Hero、国家固有の生成経路などを別Layerとして整理します。

### Magic Access route

```bash
python scripts/run_magic_access_routes_safe.py --offline
```

生成先: `docs/data/magic-access-routes/`

Native PathからBooster、再帰Summon、Communion・Sabbathへ到達する経路を生成します。Strategic Map上の到達値とBattle限定到達値を分離し、Random crosspathは同時成立可能な結果だけを使用します。

## Data更新

生成元はDom6 InspectorのDominions 6 6.35対応Snapshotへ固定されています。取得済みDataは`.cache/dom6inspector/`へ保存されます。

```bash
# 全対応GeneratorのCacheを再取得
python scripts/build_wiki.py --refresh

# Networkを使わずCacheだけで生成
python scripts/build_wiki.py --offline
```

Source versionを変更する場合は、生成結果だけでなくData quality、主要件数、手書き記事の`verified_version`も確認してください。

自動生成Pageは攻略評価ではなく、現行Dataを確認する索引です。戦術、Research順、Pretender、Battle Script、Counterは手書き記事で扱います。
