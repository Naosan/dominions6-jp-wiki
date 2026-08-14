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
python scripts/generate_spell_item_data.py
zensical serve
```

### macOS / Linux

```bash
source .venv/bin/activate
pip install zensical
python scripts/generate_nation_catalog.py
python scripts/generate_recruitment_data.py
python scripts/generate_spell_item_data.py
zensical serve
```

ブラウザで `http://localhost:8000` を開きます。

## 公開

`main` ブランチへpushすると、GitHub Actionsが次を自動実行します。

1. 103国家の一覧と未執筆Stubを生成
2. Dom6 Inspector 6.35 snapshotからRecruit / Mage access索引を生成
3. SpellのSchool / Path / National索引を生成
4. Magic ItemのSlot / Booster / Research / Resistance索引を生成
5. Zensicalで静的サイトを構築
6. GitHub Pagesへ公開

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

### Recruit / Mage access

```bash
python scripts/generate_recruitment_data.py
```

生成ページ:

```text
docs/data/recruitment/
docs/data/mage-access.md
```

### Spell / Magic Item

```bash
python scripts/generate_spell_item_data.py
```

生成ページ:

```text
docs/data/spells/
docs/data/items/
```

生成元はDom6 InspectorのDominions 6.35対応Commitへ固定しています。ダウンロード済みデータは `.cache/dom6inspector/` に保存されます。

```bash
# 強制的に再取得
python scripts/generate_recruitment_data.py --refresh
python scripts/generate_spell_item_data.py --refresh

# Networkを使用せずCacheのみで生成
python scripts/generate_recruitment_data.py --offline
python scripts/generate_spell_item_data.py --offline
```

自動生成ページは攻略評価ではなく、現行データを確認するための索引です。戦術、研究順、Pretender、Script、Counterは手書き記事で扱います。
