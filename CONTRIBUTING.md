# Contributing to Dominions 6 日本語攻略Wiki

このリポジトリでは、手書き攻略記事とDom6 Inspector由来の自動生成データを分離しています。変更前に、対象がどちらの層に属するかを確認してください。

## 開発環境

Python 3.12を使用します。

```bash
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### macOS / Linux

```bash
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## BuildとPreview

通常の生成と静的Site build:

```bash
python scripts/build_wiki.py
```

生成後にLocal serverを起動:

```bash
python scripts/build_wiki.py --serve
```

既存Cacheだけを使う場合:

```bash
python scripts/build_wiki.py --offline
```

Dom6 Inspectorの固定Snapshotを再取得する場合:

```bash
python scripts/build_wiki.py --refresh
```

生成だけを行い、Zensical buildを省略する場合:

```bash
python scripts/build_wiki.py --generate-only
```

個別Generatorを直接実行することもできますが、Pull Requestを提出する前には共有Pipelineを実行してください。LocalとGitHub Actionsは同じ`build_wiki.py`を使用します。

## TestとAudit

ValidatorのUnit test:

```bash
python -m unittest discover -s tests -v
```

Wiki全体の構造Audit:

```bash
python scripts/audit_wiki.py --report build/wiki-audit.json
```

生成Dataの基準Revision差分と、手書き記事の検証Version:

```bash
python scripts/report_patch_impact.py \
  --report build/patch-impact.json
```

Pull Requestでは、基準Branchに同じBuild基盤が存在するとき、Temporary worktreeで基準Revisionも生成します。生成Page数、Markdown table row数、Byte数、Page fingerprintをDataset単位で比較し、追加・削除・内容変更を区別します。また、固定Game Versionより古い`verified_version`を持つ手書き記事をWarningとして列挙します。

Defaultでは次をErrorとして扱います。

- 閉じられていないFront Matter
- 不正な`status`または`last_verified`
- 存在しない内部Link
- 存在しないNavigation target

既存記事を段階的に整備できるよう、Status不足、Version不足、孤立Page、古い検証VersionはDefaultではWarningです。対象Sectionの整備が完了した後は、次のStrict modeを使えます。

```bash
python scripts/audit_wiki.py \
  --strict-metadata \
  --fail-on-orphans
python scripts/report_patch_impact.py --fail-on-stale
```

## 手書き記事

手書き記事は`docs/`配下へ置きます。記事のFront Matterには、少なくとも`title`と`status`を記録してください。

```yaml
---
title: 記事名
page_type: guide
status: draft
verified_version: "6.35"
last_verified: "2026-08-15"
---
```

数値や挙動を検証していない記事では、確認していないVersionや日付を記録しないでください。

### Status

| Status | 用途 |
|---|---|
| `stub` | 自動生成または入口だけのPage |
| `draft` | 本文はあるが構成・検証が未完 |
| `reviewed` | 読者向け記事としてReview済み |
| `verified` | 重要な数値・挙動を記載Versionで検証済み |
| `needs-update` | Patch等により再確認が必要 |

### 記述順

仕様記事では、可能な限り次の順に整理します。

1. 仕様
2. 条件と例外
3. 具体例
4. 攻略上の意味
5. Counter
6. 関連データ
7. 未検証事項

国家攻略では能力値を重複掲載しすぎず、Recruit、Mage access、Magic Access routeなどの生成データへLinkしてください。

## 自動生成Page

`docs/data/`以下の大半はGeneratorが作成します。生成結果を直接修正すると次回Buildで失われるため、原則として次のいずれかを変更してください。

- 対応する`generate_*.py`または`run_*.py`
- 入力となる固定Data
- 生成後の安全なPatch処理
- 手書きのGuideまたは攻略記事

未解決のMonster Number、Montag、Event target、Location bitなどを、名前や説明文だけから単一Recordへ推測で接続しないでください。解決できない情報はData qualityへ残します。

## Pull Request checklist

- [ ] 変更の目的が利用者の具体的な問いと結び付いている
- [ ] 仕様、攻略評価、生成データの役割を混ぜていない
- [ ] 新しいPageがNavigationまたは関連記事から到達できる
- [ ] `python -m unittest discover -s tests -v`が成功する
- [ ] `python scripts/build_wiki.py`が成功する
- [ ] `python scripts/audit_wiki.py`がError 0で終了する
- [ ] `build/patch-impact.json`のDataset差分と検証Version警告を確認した
- [ ] 数値や挙動を変更した場合、根拠と対象Versionを記録した
- [ ] 自動生成結果ではなくGenerator側を修正した

詳細な優先順位と完成条件は、[開発方針と完成条件](docs/reference/development-policy.md)を参照してください。
