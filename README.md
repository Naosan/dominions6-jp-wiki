# Dominions 6 日本語攻略Wiki

Dominions 6 - Rise of the Pantokrator の日本語攻略Wikiです。

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
zensical serve
```

### macOS / Linux

```bash
source .venv/bin/activate
pip install zensical
python scripts/generate_nation_catalog.py
zensical serve
```

ブラウザで `http://localhost:8000` を開きます。

## 公開

`main` ブランチへpushするとGitHub Actionsが次を実行します。

1. Zensicalをインストール
2. `data/nations.tsv` から不足している国家ページの骨組みを生成
3. Wikiをビルド
4. GitHub Pagesへ公開

## 記事を書く

記事は `docs/` 配下のMarkdownです。

```text
docs/
  basics/weapons-and-shields.md
  magic/paths/earth.md
  nations/ma/ulm.md
```

## 国家カタログ

現行vanilla国家のメタデータは `data/nations.tsv` で管理します。

```bash
python scripts/generate_nation_catalog.py
```

このスクリプトは以下を生成します。

- EA / MA / LAの国家一覧
- まだ手書き記事がない国家のstubページ

`status: draft` 以上の手書き記事は上書きしません。新国家追加時は `data/nations.tsv` を更新してから再生成してください。

## 記事状態

- `stub`: 公式メタデータと見出しのみ
- `draft`: 執筆中
- `review`: 実戦記事あり、検証待ち
- `verified`: 記載Versionで検証済み
