---
title: データ索引
status: guide
verified_version: "6.35"
---

# データ索引

攻略本文とは別に、現行のvanillaデータから機械的に生成した参照ページをまとめます。

## 国家データ

- [国家Recruitデータ](recruitment/index.md)
- [Mage access早見表](mage-access.md)
- [国家攻略一覧](../nations/index.md)

## 自動生成と攻略本文の違い

### 自動生成データ

- Nation ID
- Recruit可能なUnit / Commander
- 固定Magic Path
- Random Path pool
- HP、Protection、MRなどの基本値
- Capital-onlyなどのデータ属性

### 人が執筆する攻略

- どの兵を主力にするか
- Expansion時の必要人数
- Pretender設計
- Research Breakpoint
- Battle Script
- Counterと外交・Timing

数値一覧だけでは国家の強さは判断できません。自動生成データは**事実確認の土台**、国家攻略は**そのデータの解釈**として分離します。

## データ更新方針

現在はDominions 6.35対応のDom6 Inspector snapshotを固定して生成します。Patchが更新された場合は、生成元Commitを更新し、次を差分確認します。

- 国家の追加・削除・改名
- Recruit roster
- Magic PathとRandom
- Unit ID
- 能力値・特殊能力

!!! note
    Inspectorの抽出値とゲーム内最終表示が異なる可能性があります。重要なCost、Spell requirement、特殊挙動はゲーム内表示と実機テストを優先します。
