---
title: MA Atlantis
page_type: nation-guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
nation_id: 88
era: "MA"
epithet: "Kings of the Deep"
---

# MA Atlantis — Kings of the Deep

MA Atlantisは、**AmphibiousなCoral兵で海を取り、Any-fortのKing of the Deepを増やし、Water MagicとCoastal Recruitを使って陸上戦へ移行するUnderwater国家**です。

国家の中心は、

> **Coral weaponの追加Poison**
> ＋ **Coral armorのPoison Barbs**
> ＋ **Shield Infantry・Shambler・Lobsterの役割分担**
> ＋ **深いWater MagicとFire / Earth / Astral Random**
> ＋ **海から陸へ出るLandfall計画**

です。

MA Atlantisは、海中だけで完結する国家ではありません。

海を制圧しても、

- 陸上Throne
- Enemy Capital
- 多くの外交相手
- High-income Land Province

へ届かなければ勝利条件が遠くなります。

したがって国家計画は、

```text
海中Expansion
→ Water Mage量産
→ Coast確保
→ Landfall
→ 陸上Fort・Lab・Recruit network
```

まで一続きです。

- [自動生成Recruitデータ](../../data/recruitment/ma/atlantis.md)
- [国家別Site Search能力](../../data/site-search/ma/atlantis.md)
- [Extended Magic Access](../../data/extended-magic-access/ma/atlantis.md)
- [Magic Access Route](../../data/magic-access-routes/ma/atlantis.md)
- [海・Underwater・Amphibious攻略](../../systems/underwater.md)
- [Pretender設計サンプル](../../pretender/samples.md)

!!! note "このページの精度範囲"
    本文はDominions 6.35の固定Roster、Coastal Recruit、Start Site Mage、Weapon / Armor record、ゲーム内表示、現行Inspector、Community referenceを照合した運用記事です。海陸でのWeapon・Spell使用可否、Poor Amphibian penalty、Fort条件、Random Pathはゲーム内popupを優先してください。

---

# 一言でいうと

```text
Coral Shield兵で前線を作る
→ Glaive・Shambler・PoisonでDamage
→ King of the Deepを各Fortで増やす
→ Water GemとSea Siteを確保
→ Coastへ上陸
→ Coastal MageとLand Recruitを取り込む
```

国家です。

MA Atlantisの強みは、

> Water Pathが高い

だけではありません。

```text
海陸を同じ国家兵が移動できる
＋
Water MageをFortごとに増やせる
＋
Poisonを通常武器へ付けられる
```

ことです。

---

# 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | Middle Age |
| Nation ID | 88 |
| Epithet | Kings of the Deep |
| 国家環境 | Underwater開始、Amphibious Roster |
| 一般兵 | Size 3 Atlantian、Shield・Coral weapon・Poison Barbs |
| 大型兵 | Shambler、War Shambler、Lobster Rider |
| Any-fort Mage | King of the Deep、Mage of the Deep、Coral Queen |
| Coastal Mage | Initiate / Witness of the Deep等 |
| Start Site Mage | Deep Seer W3S2H1 |
| 主要Magic | Water、Random Fire / Earth / Astral、Holy |
| 欠けるPath | Air、Death、Nature、Glamour、Blood |
| 操作量 | 中～高。海陸Army、Coast、Random Mage、Landfall管理 |
| 主な弱点 | Poison Resistance、低Defence・Precision、Missing Path、Landfall Timing |

---

# 国家固有の戦い方

## Coral Weapon

Atlantian兵のCoral weaponは、通常Damageに加えてWeak Poisonを与えます。

攻略上は、

```text
最初の一撃で倒す
```

より、

```text
接触し続ける
→ Poisonを蓄積
→ 数Round後に敵が崩れる
```

Damageです。

したがって、

- Shield
- HP
- Formation
- Mage support

で前線を維持する価値があります。

## Poison Barbs

Coral armorを着た兵は、近接攻撃者へPoison Barbsを返す場合があります。

多段攻撃・低Poison Resistance兵は、Atlantianを殴るほど消耗します。

ただし、

- 射撃
- Spell
- 高Poison Resistance
- Undead / Inanimate

には効率が下がります。

## Amphibious

国家兵の多くが海陸を移動できます。

しかし海・陸で、

- Missile Weapon
- Precision
- Spell
- Poor Amphibian
- Retreat

が同じとは限りません。

[Underwater攻略](../../systems/underwater.md)のChecklistを使います。

---

# 国家Engine

```text
Sea Provinceを安全に取る
        ↓
FortとKing of the Deepを増やす
        ↓
Water Site SearchとGem income
        ↓
Water booster・Elemental・Army support
        ↓
Coastを選びLandfall
        ↓
Land Fort・Coastal Mage・Independent Recruit
        ↓
陸上勝利条件へ参加
```

## 第一の詰まり：Coast

海中で領土が広くても、上陸可能なCoastが敵Fortや外交で塞がれると陸へ出られません。

早いTurnから、

- Coastの所有者
- Fort建設
- Throne
- Retreat route
- Sea接続

を確認します。

## 第二の詰まり：Mage Random

King of the Deepは、

```text
W3
＋100%でF/W/E/Sから+2
＋10%追加Random
```

を持ちます。

個体によって役割が大きく違います。

## 第三の詰まり：Missing Path

Waterは深い一方、Air・Death・Nature・Glamour・Bloodへ自然には届きません。

Pretender・Hero・Site Mage・Summonを早く計画します。

---

# 兵士

## Atlantian Militia

- 安価
- 低Morale
- 低Attack / Defence
- Coral Spear

を持つ数合わせです。

Patrol、Siege、Arrow受け等へ使います。

## Atlantian Shield Bearer

Turtle Shell Shieldを持つScreenです。

- 最初の接敵
- Javelin・射撃受け
- Poison接触時間の確保
- MageへのRound提供

へ使います。

Armorが薄いため、高Damage・AoEには弱いです。

## Atlantian Light Infantry

Coral Cuirassを持ち、Shieldなしです。

Shield Bearerの後ろでDamageを補います。

## Atlantian Infantry

Coral Cuirass、Cap、Turtle Shell Shieldを持つ標準前衛です。

- Shield
- Armor
- Coral Spear
- Poison Barbs

をまとめて持ち、国家の安定したLine holderです。

## Reef Warrior

Coral Spear、Poisoned Javelin、Shieldを持つElite寄りです。

Javelinは陸上と水中で使用可否が異なるため、Battle Replayで確認します。

Landfall直後の短距離射撃として価値があります。

## Coral Guard：Shield

重いCoral armorとShieldを持つElite Screenです。

- Morale
- HP
- Protection
- Poison Barbs

で前線を支えます。

## Coral Guard：Glaive

Coral Glaiveの高Damageを持つDamage役です。

Shieldがないため、Shield Guardの後ろへ配置します。

```text
Shield Coral Guard
→ 敵を固定

Glaive Coral Guard
→ 高Damage＋Poisonで処理
```

の分業です。

## Shambler

Size 4、高HP・Strengthの大型兵です。

裸のShamblerは複数Clawを持ちますが、防御が低いため、安価な高HP Chaffとして使います。

## Shambler Guard

ShieldとArmorを持つ大型Screenです。

- HP
- Shield
- Blunt weapon
- Size

を活かします。

## War Shambler

高StrengthでCoral GlaiveとShieldを同時に持つDamage兼Screenです。

一体は強い一方、Size 4でSquareを多く使います。

前線幅と補充Costを確認します。

## Lobster Rider

巨大Lobsterへ騎乗する高Protection Mountです。

- 高Mount HP
- 高Protection
- Pincher
- Shield rider

を持ちます。

しかし、

- Mount MR
- 低Defence
- Size
- Map Move
- Poison / MR攻撃

を確認します。

---

# Commander / Mage

## Scout

Amphibious ScoutでSea routeとCoastを確認します。

Landfall候補、敵Water Breathing、Coast Fortを優先Scoutします。

## Shambler Chief

通常Army Commanderです。

高価なKing of the DeepをTransportへ使わず、兵の輸送とExpansionへ使います。

## Consort

H1、Sacred、AmphibiousのCommanderです。

- Bless
- Temple
- Army leadership
- Prophet候補

へ使います。

## Coral Queen

```text
H3
```

をAny-fortで得られる高位Priestです。

- Throne Claim
- Bless
- Dominion
- Anti-undead
- Army leadership

へ使います。

Slow to recruitのため、Commander queueを占有します。

## Mage of the Deep

```text
W2
＋100%でF/W/E/Sから+1
```

を持つ中位Mageです。

Kingより安価・早いなら、

- Research
- Site Search
- Battle support
- Low-level Elemental / Astral

へ使います。

## King of the Deep

```text
W3
＋100%でF/W/E/Sから+2
＋10%追加Random
```

国家の主要Mageです。

### W5型

- 高位Water
- Booster chain
- Water Elemental
- Large battlefield Water spell
- Queen of Elemental Water

へ使います。

### F2型

- Acid
- Fire / Water crosspath
- Flame Spirit route
- Anti-chaff

へ使います。

### E2型

- Earth Boots
- Protection
- Maws / Earth support
- Elemental Earth route

へ使います。

### S2型

- Astral support
- MR attack
- Booster
- Teleport / Returning
- Magic Duel管理

へ使います。

### Rare追加Random

F3、W6、E3、S3等へ届く個体は国家技術です。

通常Battleへ使い捨てず、名前・番号で管理します。

## Deep Seer

Start Siteから得る、

```text
W3 S2 H1
```

Mageです。

- Astralが確定
- Water・Astral crosspath
- Research
- Site Search
- MR support

へ使います。

---

# Coastal Recruit

Land Coastでは、

- Atlantian Light Infantry
- Soldier of the Deep
- Shambler Chief
- Initiate of the Deep W1
- Witness of the Deep W2S1

等を得ます。

## Witness of the Deep

Land側でWater・Astralを供給する重要Mageです。

- Coast FortのResearch
- Water support
- Astral defence
- Landfall Army

へ使います。

## Poor Amphibian

Soldier・Initiate等はPoor Amphibianの場合があります。

陸上StatsとFatigueを確認し、海中Mageと同じScriptを貼りません。

---

# Pretender方針

## Scales＋Missing Path

国家兵とWater Mageが強いため、

- Productivity
- Gold
- Growth
- Magic

を残しながら、Air・Nature・Death等をPretenderへ持たせます。

### 向く場合

- Sea Expansionが国家兵で安定
- Landfall前にMageを増やしたい
- Missing Pathを中盤へ使う

## Awake Expander

危険なSea IndieをPretenderが取り、国家兵を別方向へ回します。

Test対象は、

- Poison
- Large Aquatic
- Mind blast / MR
- High Protection
- Swarm

です。

## Rainbow / Landfall Support

Pretenderで、

- Air：Shock、Storm、Cloud movement
- Nature：Poison Resistance、Regeneration、Supply
- Death：Summon、Darkness、Undead
- Glamour：Stealth、Illusion

を開きます。

Waterは国家側が深いため、Pretender Waterを過剰に上げる必要があるか比較します。

## Heavy Bless

Sacred兵の供給と性能が国家全体を支えるかをTestします。

Coral Queen等Sacred CommanderへのBless価値もありますが、通常AtlantianとMageが国家Engineの中心です。

---

# Sea Expansion

## 基本Army

```text
Shield Infantry
＋ Damage Infantry / Shambler
＋ Shambler Chief
```

で組みます。

## Poisonを時間Damageとして使う

一撃で倒せない敵でも、前線を維持すればPoisonが働きます。

反対に、Atlantianが短時間で崩れるとPoisonが発動する前に負けます。

## Darkvision

深海で敵がDarkvisionを持たない場合、命中差を利用できます。

敵もDeep raceなら優位はありません。

## Large Unit

Shambler・Lobsterを多く入れるとSquareが詰まります。

```text
Shield Size 3
＋ 少数Size 4 Damage
```

で前線密度を調整します。

---

# Landfall

## Coastを選ぶ

```text
Seaからの接続数
敵Fort
Income
Coastal Recruit
Retreat route
Throne
次のLand Fort位置
```

を見ます。

## 上陸Army

```text
Atlantian Infantry：Screen
Coral Glaive / War Shambler：Damage
Reef Warrior：Land Javelin
King / Witness：Support
Coral Queen：Bless・Dominion
```

へ分けます。

## 海側予備を残す

全ArmyをLandへ出すと、海中FortとRetreat routeが空きます。

```text
Landfall Army
＋ Sea reserve
＋ Coastal reinforcement
```

にします。

## Land Fort

Coastを取ったら、

- Fort
- Lab
- Temple
- Independent Commander
- Coastal Mage

を作ります。

Landfallの勝利はProvinceを一つ取ることではなく、**陸上生産拠点を完成すること**です。

---

# Magic Access

## Water

国家の確実な軸です。

King of the Deep W3から、

```text
Robe of the Sea
→ Water Bracelet
→ Orb of Elemental Water
```

等で高位Waterへ進めます。

- Water Elemental
- Quickness
- Cold
- Army support
- Sea summon
- Battlefield-wide spell

へ使います。

## Fire Random

Fire型Kingは、

- Acid
- Fire / Water crosspath
- Fire summon
- Anti-chaff

へ使います。

Fire SpellのUnderwater可否を確認します。

## Earth Random

Earth型Kingは、

- Earth Boots
- Protection
- Strength
- Anti-armor
- Earth Elemental

へ使います。

ShamblerとCoral Guardの物理性能を伸ばします。

## Astral Random

Astral型King、Deep Seer、Witnessが、

- MR attack
- Antimagic
- Teleport
- Booster
- Magic Duel

へ使えます。

## Missing Path

Air、Death、Nature、Glamour、BloodはPretender・Hero・Site Mage・Summonへ依存します。

特にNature不足は、

- Poison Resistance
- Regeneration
- Supply
- Disease

で問題になります。

自軍はPoisonを使いますが、敵のPoisonへ自動的に完全耐性があるとは限りません。

---

# Site Search

## Water Search

King・Mage・Deep Seerで高Level Water Siteを探します。

## Astral Search

Deep SeerとWitnessが担当します。

## Random Path

Fire・Earth・Astral型Kingを、

- Manual Search
- Remote Search
- Booster

へ分けます。

Rare Mageを海中Main Armyへ全員入れません。

## Sea Site

Sea-specific Siteは、

- Water Gem
- Recruit
- Summon
- Economy

を大きく変えます。

Sea ProvinceをIncomeだけで評価しません。

---

# Research方針

## Conjuration

- Water Elemental
- Sea King
- Bishop Fish
- Elemental Queen
- Flame Spirit

へつながります。

## Alteration

- Quickness
- Defence
- Protection
- Body buff
- Cold / Water support

へ使います。

## Evocation

- Cold
- Water damage
- Acid
- Astral MR attack

で敵防御を破ります。

## Construction

- Water booster
- Earth / Astral booster
- Water Breathing Item
- Resistance Item
- Thug gear

へ使います。

## Enchantment

- Army-wide support
- Water / Cold battlefield
- Protection
- Resistance

へ進みます。

## Thaumaturgy

- Site Search
- Astral control
- Teleport
- Soul・Mind

へ使います。

---

# First War

## 海中相手

- Darkvision
- Water Mage
- Poison Resistance
- Large Unit
- Mind / MR attack

をScoutします。

## 陸上相手

Landfall TimingとCoast Fortが勝敗を決めます。

### 勝利条件

```text
Shield Coral兵で前線維持
→ PoisonとWater support
→ Glaive / ShamblerでDamage
→ Random Mageで敵Counterへ回答
```

## 攻めるTarget

- Coast Fort
- Land Throne
- Mage Fort
- Nature / Air Site
- Sea accessを持つ敵Commander

です。

---

# Battle Script

## Water support

```text
Water path boost
→ Quickness / defence / protection
→ Water Elemental or cold damage
→ Cast Spells
```

## Earth King

```text
Earthpower
→ Army protection / strength
→ Anti-armor
```

## Astral King / Deep Seer

```text
Astral defence
→ Antimagic / MR attack
→ Returning等の安全策
```

## Fire King

```text
Fire / Water crosspath
→ Acid / anti-chaff
→ 敵Resistanceで第二Spellへ切替
```

## Formation

```text
Shield Atlantian：前
Glaive / War Shambler：後
Mage：中央後方
Lobster：側面または別Squad
```

Large Unitを中央へ詰めすぎません。

---

# Counterされるもの

| 相手の手段 | なぜ危険か | 対応 |
|---|---|---|
| Poison Resistance | Coral weapon・Barbsの価値低下 | 通常Damage、Cold、Earth、Astral |
| High Defence | 低Attack Atlantianが当てにくい | Quickness、拘束、AoE、MR attack |
| Shock | Native Air不足 | Pretender、Item、分散、Scout |
| MR attack | 多くの兵が標準MR | Antimagic、Mindless Summon、Mage kill |
| Archer | 陸上Landfall時に損失 | Shield、Storm、Coast配置 |
| Fire / Cold Resistance | Elemental planを止める | Random Crosspath、物理、Astral |
| Large high-Damage | Size 3前衛を短時間で破る | Shambler、Elemental、control |
| Coast Fort | Landfallを遅延 | 別Coast、Siege準備、外交 |
| Sea invasion | 後方Fort・Gem Siteへ直撃 | Sea reserve、Choke Fort、Scout |

---

# Siege

## 海中Fort

Sea connectionが少ないため、一Fortで進路を止めやすい一方、退却先も少なくなります。

## 壁を削るArmy

Militia・Shambler等で数を用意します。

## Storm Army

- Coral Guard
- War Shambler
- Water Elemental
- King of the Deep
- Coral Queen

を使います。

Poisonだけに依存せず、Fort内Mageを短時間で倒すDamageを用意します。

---

# Multiplayer

## 海の外交

Underwater国家同士では、Sea borderとCoast accessが中心です。

陸上国家とは、

- Coast ownership
- Sea Scout
- Water Breathing
- Landfall
- Throne

を交渉します。

## 孤立Risk

海中で安全でも、陸上外交に参加できないと、Throne raceと共同戦争へ遅れます。

## Sea threat

陸上国家から見て海中Armyは見えにくく、Coastへの奇襲能力が高いと評価されます。

不用意に複数Coastへ圧力をかけると包囲網を作られます。

---

# よくある失敗

## 海を全部取ってから陸へ出る

Land Throne・Fort・外交へ遅れます。

## King of the DeepをRandom分類しない

F / E / S Rare個体を通常W Mageとして失います。

## Poisonだけで敵を倒そうとする

Poison Resistance、Undead、Inanimateへ止まります。

## ShamblerをHPだけで評価する

Size、Defence、MR、前線幅を見落とします。

## Amphibiousなので海陸同じScriptを使う

Weapon・Spell・Precision・Penaltyが違います。

## Landfall後にFortを建てない

補充・Mage・Retreatが細く、海へ押し戻されます。

## 全Water MageをMain Armyへ集める

Site Search、Booster、Sea summon、第二戦線が止まります。

## Missing PathをPretenderで考えない

Shock、Poison Resistance、Disease、Stealth等へ回答できません。

## Coral QueenをH3だけで前線へ出す

Slow recruitmentのThrone・Dominion資源を失います。

---

# Test gameで記録するもの

```text
第一Sea Expansion開始Turn：
Expansion損失：
第二Fort開始Turn：
King of the Deep生産数：
Random分類：F / W / E / S
Water Gem income：
最初のCoast接触Turn：
Landfall候補：
Land Fort開始Turn：
Coastal Mage生産：
First war Spell：
Poison Resistance相手への第二Damage：
Sea reserve規模：
Retreat失敗：
```

---

# 毎Turn Checklist

```text
□ SeaとLandのArmyを別に確認した
□ King / MageのRandomを分類した
□ Coast ownershipとFort建設をScoutした
□ Sea Site Searchを進めた
□ Water GemをBattle・Booster・Summonへ分けた
□ Landfall後のFort・Lab資金を残した
□ ShieldとGlaive役を分けた
□ Poison Resistance相手への第二Damageがある
□ Sea reserveとRetreat routeを残した
□ Underwater用とLand用Scriptを分けた
```

---

## 関連ページ

- [海・Underwater・Amphibious攻略](../../systems/underwater.md)
- [Water](../../magic/paths/water.md)
- [Magic Access到達経路](../../magic/magic-access-routes.md)
- [Forts](../../systems/forts.md)
- [Province](../../systems/province.md)
- [戦闘ルール](../../basics/combat-rules.md)
- [命令とBattle Script](../../basics/orders.md)
- [Pretender設計サンプル](../../pretender/samples.md)
- [Unit装備・Mountの読み方](../../data/unit-loadouts.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [MA Atlantis community reference](https://illwiki.com/dom5/dom6/atlantis-ma)
