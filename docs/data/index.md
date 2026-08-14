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

## Unit総合データ

- [Unit総合索引](units/index.md)
- [全Unit一覧](units/all/index.md)
- [Pretender chassis](units/pretenders.md)
- [Hero](units/heroes.md)
- [Spell summon](units/spell-summons.md)
- [Spell Random summon pool](units/spell-random-summons.md)
- [Wish・Unique・Terrain特殊召喚](units/special-summons.md)
- [Magic Site Unit](units/magic-sites.md)
- [Event Unit・Commander生成](units/event-spawns.md)
- [Event変身・強制変身](units/event-transforms.md)
- [Event暗殺・戦闘参加Unit](units/event-combat.md)
- [Event Random pool・未解決Target](units/event-random.md)
- [Mercenary Unit](units/mercenaries.md)
- [Magic ItemによるUnit生成・変身](units/item-unit-sources.md)
- [Item Random summon・未解決Target](units/item-random.md)
- [Strategic summon・Freespawn](units/strategic-spawns.md)
- [Battle summon](units/battle-spawns.md)
- [Unit条件Recruit](units/recruit-unlocks.md)
- [変換・復活・Raise](units/conversions.md)
- [Reanimation・Freespawn・召喚Bonus](units/reanimation.md)
- [国家Freespawn・Reanimation](units/nation-generation.md)
- [Random summon・未解決Target](units/random-summons.md)
- [Mount](units/mounts.md)
- [Shape relation](units/shapes.md)
- [入手経路未分類Unit](units/unclassified.md)
- [Unit索引データ品質](units/data-quality.md)

BaseUの全4,091 Unit recordを個別ページ化し、通常Recruit、Hero、Pretender、固定Spell summon、Magic Site、Event、Mercenary、Magic Item、Unit自身の召喚・変換能力、国家Freespawn・Reanimation能力、Mount、Shapeの関係を結合します。

`domsummon`、`makemonster`、`summon`、`batstartsum`、`battlesum`など、固定Unit IDを参照するUnit生成能力は生成先Unitへ逆引きします。負のMonster NumberやMontagはRandom poolであり、特定Unitへ推測で結び付けません。

Event索引では`nation -1`をRandom enemy、`nation -2`をProvince ownerとして保持し、`tempunits 1`を一時Unitとして区別します。Event戦闘参加者を「プレイヤーが恒久取得するUnit」とは扱いません。

Mercenary索引では、傭兵団のCommander、Troop、初期人数、Era mask、最低入札額、経験値、補充率、開始Itemを確認できます。

Magic Itemでは`sumrit`、`sumauto`、`sumbat`、`retinue`、`batstartsum*`、`transformwearer`、`raiseshape`、`defender`等の明示的なUnit参照を追跡します。Itemによる敵対EncounterやBattle summonは、恒久加入とは別の出現関係として表示します。

Spellについては通常の固定Unit summonに加え、Negative Monster Number、Montag、Unique summon table、Terrain-specific summon table、WishやCross Breedingのような特殊処理を分離しました。候補集合や内部処理を、もっともらしい単一Unitへ置き換えません。

## Magic Site総合データ

- [Magic Site総合索引](sites/index.md)
- [全1,253 Magic Site一覧](sites/all.md)
- Magic Path別Site一覧
  - [Fire](sites/by-path/fire.md)
  - [Air](sites/by-path/air.md)
  - [Water](sites/by-path/water.md)
  - [Earth](sites/by-path/earth.md)
  - [Astral](sites/by-path/astral.md)
  - [Death](sites/by-path/death.md)
  - [Nature](sites/by-path/nature.md)
  - [Glamour](sites/by-path/glamour.md)
  - [Blood](sites/by-path/blood.md)
  - [Holy](sites/by-path/holy.md)
- [Gem income](sites/gem-income.md)
- [Recruit Unit・Commander](sites/recruitment.md)
- [Site summon](sites/summons.md)
- [Research・Ritual bonus](sites/research.md)
- [Economy・Fort・Lab](sites/economy.md)
- [Enter・Active effect](sites/enter-effects.md)
- [国家開始Site・Future Site](sites/national.md)
- [Terrain・Location](sites/terrain.md)
- [Throne](sites/thrones.md)
- [Site Event relation](sites/events.md)
- [Magic Site索引データ品質](sites/data-quality.md)

`MagicSites.csv`の全1,253 recordを個別ページ化します。Path、Site level、raw Rarity、`loc` bitfield、毎月のGem income、Recruit、Summon、Province Defence、Gold・Resource・Supply・Unrest、Fort・Lab、Research School bonus、Ritual range、Scales、Dominion、Entering Site、Scry、Adventure、Void Gateなどを分離して表示します。

現在の固定スナップショットでは、毎月Gem incomeを持つSiteが1,061件、Site–Unit relationが781件、国家Start Site relationが208件、Future Site relationが3件、Throneが74件あります。Eventとの関係は830件で、Siteを要求するrelation 678件とSiteを生成するrelation 152件を区別します。

Terrainは`site_terrain_types.csv`に定義されたbitだけを展開します。`loc = 0`を「全地形に通常出現」とは扱わず、定義されていないbitは品質レポートへ残します。39種の同名Siteが存在しますが、異なるSite IDは別recordとして保持します。

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
- [Spell Random summon pool](units/spell-random-summons.md)
- [Wish・Unique・Terrain特殊召喚](units/special-summons.md)

各Magic PathからもSpellを引けます。主Pathと副Pathの両方を対象にしています。

## Magic Itemデータ

- [Magic Itemデータ索引](items/index.md)
- [Magic Path Booster](items/boosters.md)
- [Research Item](items/research.md)
- [Resistance / MR Item](items/resistance.md)
- [Utility Item](items/utility.md)
- [Arena関連Magic Item](items/arena.md)
- [Magic ItemによるUnit生成・変身](units/item-unit-sources.md)
- [Item Random summon・未解決Target](units/item-random.md)
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
- BaseUの全Unit recordと確認済み入手・出現経路
- Unit / Commanderの基本値
- Hero、Pretender、Spell summon、Magic Site、Event、Mercenary、Magic Item、Mount、Shape関係
- 全Magic Site record、Path、Level、raw Rarity、Terrain bitfield
- SiteのGem income、Recruit、Summon、PD、Economy、Research、Ritual、Scale、Active effect
- 国家Start Site・Future SiteとEventによるSite requirement・生成relation
- EventのUnit所有者、Temporary指定、発生条件、Rarity
- MercenaryのCommander、Troop、人数、Era、入札・補充情報
- Itemの固定Unit summon、Retinue、Battle summon、Transform、Raise、敵対Encounter
- SpellのNegative Monster Number、Montag、Unique・Terrain pool、特殊召喚処理
- Unit自身のDominion summon、毎月召喚、Battle summon、Recruit unlock、固定変換先
- Reanimation、Oni attraction、召喚数BonusなどTargetを直接指定しない能力
- 国家属性が明示するFreespawn、Guardian Spirit、Reanimation能力
- Unitが参照するWeapon、Armor、Mount record
- Weapon / Armorから見た使用国家・Recruitの逆引き
- RiderとMountの別Stats・別攻撃Profile
- 固定Magic PathとRandom Path pool
- SpellのSchool、要求Path、Gem Cost、Range、AoE
- ItemのConstruction、要求Path、基礎Gem Cost、Booster、主要効果
- Weapon / Armorの基礎値、Damage modifier、部位Protection
- Capital-only、National restrictionなどのデータ属性

### 人が執筆する攻略

- どの兵、召喚、Hero、Pretenderを主力にするか
- Freespawnを国家経済へどう組み込むか
- EventやMercenaryを戦略上どの程度期待してよいか
- Site Searchの優先Path・Timing・探索Mageをどう選ぶか
- SiteのGem、Recruit、研究Bonus、Adventureを戦略へどう組み込むか
- Throneをどの戦力と時期で確保・Claimするか
- Item召喚・Retinue・Arena報酬を実戦でどう評価するか
- Wishや特殊召喚で何を狙うか
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
- Hero、Pretender、Spell summon、Magic Site、Event、Mercenary、Item、Shapeの対応
- Magic Site ID、Path、Level、Rarity、Location bit、Gem income、効果Field
- Site Recruit・Summon・PD Unit参照とNational recruit restriction
- Nation Start Site / Future Site属性
- EventのSite requirement・Site生成effect
- Unit / Nation generation fieldとRandom pool参照
- Event effect command、owner、Temporary指定、Requirement
- Mercenary roster、Era mask、人数・入札・補充情報
- ItemのUnit参照Field、Arena flag、Random target
- Spell effect number、Negative pool、Unique・Terrain table番号
- Equipment使用者とProfile分類
- SpellのSchool、Research level、Path、Cost
- ItemのConstruction、Path、Cost、効果
- WeaponのDamage、Length、AP / AN、modifier
- ArmorのProtection、Parry、Encumbrance
- Unit / Spell / Item / Site / Weapon / Armor ID
- 入手経路未分類件数と未解決参照

!!! warning "抽出データの限界"
    Inspectorの抽出値とゲーム内最終表示が異なる可能性があります。Magic Siteの最終発見率、Hidden / Found状態、Capital配置、Throne claim、National recruit条件、Adventure、Void Gate、未知Location bit、Wishの任意入力結果、Unique pool内の実際の選択、Terrain summonの地形別結果、hard-coded Reanimation、Scenario、複合Event chain、複合Spell、特殊Range / AoE、Itemの発動回数・持続、Mounted combat、最終Forge Costはゲーム内表示と実機テストを優先します。