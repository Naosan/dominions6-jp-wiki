---
title: "国家攻略テンプレート"
status: template
last_verified: "2026-08-14"
---

# 国家攻略テンプレート

新しい国家ページを作るときにコピーします。**仕様・攻略評価・検証状況を分離**してください。

```markdown
---
title: "MA Example"
status: draft
verified_version: "6.35"
last_verified: "YYYY-MM-DD"
nation_id: 000
era: "MA"
epithet: "Official Epithet"
authors:
  - "Name"
---

# MA Example — Official Epithet

!!! info "記事状態"
    主要項目を執筆中。未検証箇所を明記する。

## 一言でいうと

国家の勝ち筋と最大の制約を一～二文で書く。

## 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | Middle Age |
| Nation ID | 000 |
| 得意Path |  |
| 主な制約 |  |
| 国家固有要素 |  |

## 強み

## 弱み

## 国家固有ルール

Dominion効果、特殊Fort、外国Recruit、Reanimation、Blood Sacrificeなど。

## 兵士

### 主力兵

| Unit | Gold | Res | RP | 役割 | 評価 |
|---|---:|---:|---:|---|---|

### Sacred

### 射撃・騎兵・特殊兵

### 外国Recruit / Terrain Recruit

## Commander / Mage

| Commander | 雇用場所 | CP | 固定Path | Random | 主な役割 |
|---|---|---:|---|---|---|

### Recruit-anywhere Mage

### Capital-only Mage

### Priest / Prophet候補

### Rare Randomの扱い

## Magic Access

| Path | 確実な到達点 | Booster後 | Communion等 | 主な用途 |
|---|---:|---:|---:|---|

## Pretender方針

### Awake Expander

### Scales

### Bless

### Rainbow / Diversity

設計例には必ず「何を買い、何を諦めるか」を書く。

## 序盤拡張

### 標準Expansion Army

### Indie別の注意

### 二軍・三軍への分割

## Economy / Fort計画

Gold、Resources、Recruitment Points、Commander Points、第二Fort建設地。

## Researchルート

### 最初のBreakpoint

### 第一戦争

### 中盤

### 終盤

研究レベルは記載バージョンで再確認する。

## 重要Spell・召喚

| Spell | School | Level | Path | 用途 | 注意 |
|---|---|---:|---|---|---|

## 重要Magic Item

| Item | Construction | Path | 用途 | 誰に持たせるか |
|---|---:|---|---|---|

## Army構成

### 前衛

### Damage dealer

### Mage

### 側面・後衛警戒

## Battle Script

```text
Spell 1
Spell 2
Spell 3
Cast Spells
```

Scriptの目的と、失敗条件を書く。

## Raid / Siege / Map Control

## Counterされるもの

| 相手の手段 | なぜ弱いか | 対応 |
|---|---|---|

## 対主要Archetype

### 高Protection

### 高Defence / Glamour

### Giant

### Undead / Demon

### Poison / Foul Vapors

### MR攻撃

## Multiplayer

Timing、外交、脅威認識、公開情報と隠したい情報。

## よくある失敗

## 情報源・検証

- ゲーム内Nation Overview
- Unit / Spell / Item popup
- Battle Replay
- 公式Manual / Change log
- 現行Mod Inspector

## 更新履歴

| 日付 | Version | 内容 |
|---|---|---|
| YYYY-MM-DD | 6.xx | 初版 |
```

## 記事状態

| Status | 意味 |
|---|---|
| `stub` | 公式メタデータと見出しのみ |
| `draft` | 主要項目を執筆中 |
| `review` | 実戦記事あり、検証待ち |
| `verified` | 記載Versionで検証済み |

## 執筆時の禁止事項

- Dom4 / Dom5の数値を未確認で移植しない
- Rare Randomを確定Accessとして書かない
- Capital-onlyとRecruit-anywhereを混同しない
- Magic WeaponとArmor Negatingを混同しない
- 単一のPretender例を唯一の正解として書かない
- Tier評価だけで理由を省略しない
