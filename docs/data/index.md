---
title: データ索引
status: guide
verified_version: "6.35"
last_verified: "2026-08-14"
---

# データ索引

攻略本文とは別に、現行のvanillaデータから機械的に生成した参照ページをまとめます。

## 国家・Recruitデータ

- [国家Recruitデータ](recruitment/index.md)
- [Mage access早見表](mage-access.md)
- [国家攻略一覧](../nations/index.md)

## Spellデータ

- [Spellデータ索引](spells/index.md)
- Research School別
  - [Conjuration](spells/by-school/conjuration.md)
  - [Alteration](spells/by-school/alteration.md)
  - [Evocation](spells/by-school/evocation.md)
  - [Construction](spells/by-school/construction.md)
  - [Enchantment](spells/by-school/enchantment.md)
  - [Thaumaturgy](spells/by-school/thaumaturgy.md)
  - [Blood Magic](spells/by-school/blood-magic.md)
  - [Divine](spells/by-school/divine.md)
- [National / Realm restricted Spell](spells/national.md)

各Magic PathからもSpellを引けます。主Pathと副Pathの両方を対象にしています。

## Magic Itemデータ

- [Magic Itemデータ索引](items/index.md)
- [Magic Path Booster](items/boosters.md)
- [Research Item](items/research.md)
- [Resistance / MR Item](items/resistance.md)
- [Utility Item](items/utility.md)
- [Unforgeable / Artifact](items/unforgeable.md)

Slot別ページでは片手武器、両手武器、盾、鎧、兜、靴、Miscellaneous、Crown、BardingをConstruction順に比較できます。

## 自動生成と攻略本文の違い

### 自動生成データ

- Nation IDとRecruit roster
- Unit / Commanderの基本値
- 固定Magic PathとRandom Path pool
- SpellのSchool、要求Path、Gem Cost、Range、AoE
- ItemのConstruction、要求Path、基礎Gem Cost、Booster、主要効果
- Capital-only、National restrictionなどのデータ属性

### 人が執筆する攻略

- どの兵、Spell、Itemを主力にするか
- Expansion時の必要人数
- Pretender設計
- Research Breakpoint
- Battle Script
- Counterと外交・Timing

数値一覧だけでは強さは判断できません。自動生成データは**事実確認の土台**、攻略記事は**そのデータの解釈**として分離します。

## データ更新方針

現在はDominions 6.35対応のDom6 Inspector snapshotを固定して生成します。Patchが更新された場合は生成元Commitを更新し、次を差分確認します。

- 国家の追加・削除・改名
- Recruit rosterとMagic Path
- SpellのSchool、Research level、Path、Cost
- ItemのConstruction、Path、Cost、効果
- Unit / Spell / Item ID

!!! warning "抽出データの限界"
    Inspectorの抽出値とゲーム内最終表示が異なる可能性があります。複合Spell、特殊Range / AoE、Itemの発動効果、最終Forge Costはゲーム内表示と実機テストを優先します。
