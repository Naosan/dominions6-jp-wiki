---
title: 情報源
last_verified: "2026-08-14"
---

# 情報源

攻略記事を書く際の主要な参照先です。

## 優先順位

1. Dominions 6 ゲーム内表示・実機挙動
2. Illwinter公式Manual・Change log・Patch notes
3. ゲームデータ抽出
4. Community Wiki・Guide
5. Battle Replay・Test game・対戦知見

## 公式資料

- Illwinter Game Design公式サイト
- Dominions 6 Manual
- Dominions 6 Change log / Steam公式Announcement
- Dominions 6 Modding Manual

## データ索引

- Dominions 6 Mod Inspector
- Inspectorのvanilla CSV data
- ゲーム内Unit / Spell / Item popup

### 国家カタログ

国家名、Epithet、Nation ID、Eraは、Mod Inspectorの `gamedata/nations.csv` と照合し、リポジトリ内の `data/nations.tsv` にスナップショットとして保存します。

現在の登録数:

- Early Age: 35
- Middle Age: 37
- Late Age: 31
- 合計: 103

### Recruit・Commander・Mage索引

Recruit索引は、Dominions 6.35対応のDom6 Inspector commit
`cfac4311bc0b58053b8dead7bffbc036ba9bd5dc` を固定データ源として生成します。

主に利用するファイル:

- `gamedata/BaseU.csv`
- `gamedata/fort_troop_types_by_nation.csv`
- `gamedata/fort_leader_types_by_nation.csv`
- `gamedata/nonfort_troop_types_by_nation.csv`
- `gamedata/nonfort_leader_types_by_nation.csv`
- `gamedata/coast_troop_types_by_nation.csv`
- `gamedata/coast_leader_types_by_nation.csv`

生成物には、Unit ID、基礎能力値、固定Magic Path、Random Path、Sacred・Flying・Stealthyなどの主要タグを掲載します。

!!! warning "自動生成データの限界"
    - Costは自動計算、Mount、形態変化、特殊Recruit条件などが複雑なため、現段階の索引では表示しません。
    - `Fort`、`Capital-only`、`Foreign / Terrain`、`Coast`は抽出データの分類に従いますが、国家固有イベントや特殊Site Recruitは別途確認が必要です。
    - Random Pathは抽出されたchance / repeats / level / maskを読みやすい表記へ変換しています。最終確認はゲーム内Nation Overviewを優先します。

!!! warning "抽出データの扱い"
    Inspectorは非常に有用ですが、抽出・表示上の不具合があり得ます。最終的な数値・挙動はゲーム内表示と実機テストを優先します。

## Community資料

- illwiki Dominions 6
- 旧Dominions日本語Wiki
- プレイヤーGuide、動画、対戦記録

Community資料は戦術の発見に有用ですが、Dom4 / Dom5の数値やResearch LevelをDom6へそのまま移植しません。

## 出典の書き方

重要な数値・Research Level・Path要求など、Patchで変わりやすい情報には次を残します。

- 確認Version
- 確認日
- ゲーム内か外部データか
- 必要なら検証方法

攻略評価では、前提となるMap、相手、研究時期、Gem消費、Scriptも併記します。
