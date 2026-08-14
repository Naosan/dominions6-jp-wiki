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
- [Unit装備・Mountの読み方](unit-loadouts.md)
- [国家攻略一覧](../nations/index.md)

各国家Recruitページでは、Unitの基礎能力に加えてWeapon、Armor、Mount recordを結合して表示します。

## 装備使用者逆引き

- [装備使用者逆引き](equipment-usage/index.md)
- [Weapon使用者](equipment-usage/weapons/index.md)
- [Armor使用者](equipment-usage/armor/index.md)
- [国家別Recruit装備Profile](equipment-usage/nations.md)
- [盾を持つRecruit](equipment-usage/profiles/shield.md)
- [両手武器Recruit](equipment-usage/profiles/two-handed.md)
- [射撃Recruit](equipment-usage/profiles/ranged.md)
- [AP武器Recruit](equipment-usage/profiles/ap.md)
- [AN武器Recruit](equipment-usage/profiles/an.md)
- [Charge武器Recruit](equipment-usage/profiles/charge.md)
- [騎乗Recruit](equipment-usage/profiles/mounted.md)

Weapon・Armorから使用国家とRecruitを逆引きできます。Mount側の攻撃・BardingはRider本体と分離して追跡します。

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

## Combat data

- [Combat data索引](combat/index.md)
- [近接武器](combat/weapons/melee.md)
- [射撃武器](combat/weapons/ranged.md)
- [AP・AN武器](combat/weapons/ap-an.md)
- [Elemental・Poison・Acid武器](combat/weapons/elemental.md)
- [盾](combat/armor/shields.md)
- [胴鎧](combat/armor/body-armor.md)
- [兜](combat/armor/helmets.md)
- [Weapon property・Damage type](combat/weapon-properties.md)
- [特殊Damage・状態効果](combat/special-damage.md)

Weapon / Armor recordを攻略記事から分離し、Damage、Attack / Precision、Defence、Length / Range、AP / AN、Shield Protection、Parry、Encumbrance等を確認できます。

## 自動生成と攻略本文の違い

### 自動生成データ

- Nation IDとRecruit roster
- Unit / Commanderの基本値
- Unitが参照するWeapon、Armor、Mount record
- Weapon / Armorから見た使用国家・Recruitの逆引き
- RiderとMountの別Stats・別攻撃Profile
- 固定Magic PathとRandom Path pool
- SpellのSchool、要求Path、Gem Cost、Range、AoE
- ItemのConstruction、要求Path、基礎Gem Cost、Booster、主要効果
- Weapon / Armorの基礎値、Damage modifier、部位Protection
- Capital-only、National restrictionなどのデータ属性

### 人が執筆する攻略

- どの兵、Spell、Item、Weaponを主力にするか
- Expansion時の必要人数
- Pretender設計
- Research Breakpoint
- Battle Script
- Counterと外交・Timing

数値一覧だけでは強さは判断できません。自動生成データは**事実確認の土台**、攻略記事は**そのデータの解釈**として分離します。

## データ更新方針

現在はDominions 6.35対応のDom6 Inspector snapshotを固定して生成します。Patchが更新された場合は生成元Commitを更新し、次を差分確認します。

- 国家の追加・削除・改名
- Recruit roster、Weapon / Armor / Mount参照、Magic Path
- Equipment使用者とProfile分類
- SpellのSchool、Research level、Path、Cost
- ItemのConstruction、Path、Cost、効果
- WeaponのDamage、Length、AP / AN、modifier
- ArmorのProtection、Parry、Encumbrance
- Unit / Spell / Item / Weapon / Armor ID

!!! warning "抽出データの限界"
    Inspectorの抽出値とゲーム内最終表示が異なる可能性があります。複合Spell、特殊Range / AoE、Itemの発動効果、WeaponのSecondary effect、Mounted combat、最終Forge Costはゲーム内表示と実機テストを優先します。
