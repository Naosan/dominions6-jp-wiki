---
title: EA Mictlan
page_type: nation-guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
nation_id: 25
era: "EA"
epithet: "Reign of Blood"
---

# EA Mictlan — Reign of Blood

EA Mictlanは、**Sacred expansion、Restricted Dominion、Blood Sacrifice、安価なBlood Hunter、四系統の首都Priestを、一つの国家Engineとして回すBlood国家**です。

国家の中心は、

> **Jaguar Warriorと人間兵によるExpansion**
> ＋ **Mictlan PriestによるBlood HuntとBlood Sacrifice**
> ＋ **Sun・Rain・Moon・Land PriestのCrosspath**
> ＋ **Nahualliから始まるAstral・Nature・召喚Access**

です。

Mictlanは、単にBlood Spellが使える国家ではありません。

Blood Slaveは、

- Ritual
- Sabbath
- Demon summon
- Forge
- Blood Sacrifice

へ使われます。

さらに通常のDominion spreadが制限されるため、Blood economyを作らないことは、Late-game火力を捨てるだけではなく、**宗教Networkそのものを放棄すること**です。

- [自動生成Recruitデータ](../../data/recruitment/ea/mictlan.md)
- [国家別Site Search能力](../../data/site-search/ea/mictlan.md)
- [Extended Magic Access](../../data/extended-magic-access/ea/mictlan.md)
- [Magic Access Route](../../data/magic-access-routes/ea/mictlan.md)
- [Blood Economy・Blood Hunt・Blood Sacrifice](../../magic/blood-economy.md)
- [Pretender設計サンプル](../../pretender/samples.md)

!!! note "このページの精度範囲"
    本文はDominions 6.35の固定Roster、Start Site Mage、National rule、ゲーム内表示、現行Inspector、Community referenceを照合した運用記事です。Blood Hunt式、Bless cost、Fort、Holy Point、Random Path、Map、Pretenderで最適解は変わります。正確なUnit cost・Recruit limit・Spell requirementはゲーム内表示と自動生成データを優先してください。

---

# 一言でいうと

```text
Jaguar Warriorと人間兵でExpansion
→ Mictlan Priestを各Fortで量産
→ 後方でBlood Hunt
→ TempleへSlaveを運びBlood Sacrifice
→ 首都高位PriestへSlaveを集約
→ Blood Ritual・Sabbath・Crosspathへ変換
```

する国家です。

Mictlanで最も重要な資源は、Blood Slave単体ではありません。

```text
Population
＋ Hunter turn
＋ Patrol
＋ Temple
＋ Priest turn
＋ 輸送経路
```

が揃ったBlood Networkです。

---

# 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | Early Age |
| Nation ID | 25 |
| Epithet | Reign of Blood |
| 一般兵 | Sling・Javelin・Shieldを持つ安価な人間兵 |
| Sacred | Jaguar Warrior、Moon Warrior等のSacred・特殊兵 |
| Any-fort Mage | Mictlan Priest B1H1、Nahualli S1N2 |
| 首都Site Mage | Fire / Water / Astral / Nature＋Blood＋Holy |
| 国家宗教 | Restricted Dominion、Blood Sacrificeが必須級 |
| 主要Magic | Blood、Fire、Water、Astral、Nature、Holy |
| 欠けやすいPath | Air、Earth、Death、Glamour |
| 操作量 | 非常に高い。Hunt、Patrol、Sacrifice、輸送、Sabbath |
| 主な弱点 | 軽装、射撃、重装敵、Anti-Sacred、Hunter拠点Raid |

---

# 国家固有Rule

## Restricted Dominion

EA Mictlanは、通常国家と同じ方法ではDominionが十分に広がりません。

- Home Province
- Temple
- Prophet
- PriestのPreach
- Pretenderのpassive spread

に制限があります。

実戦上は、

```text
Templeを建てる
→ Priestを置く
→ Blood Slaveを運ぶ
→ Blood Sacrificeする
```

ことがDominion運用の中心です。

Blood Sacrificeを忘れると、

- Sacred Recruit
- Bless運用
- Scales
- Pretender安全圏
- Dominion kill耐性

が崩れます。

## Bless Point Bonus

MictlanはPretender designでBlessへ向く国家能力を持ちます。

しかし、

> Bless Pointが多いのでHeavy Bless一択

ではありません。

- Jaguar Warrior供給
- Holy Point
- Capital依存
- MageとFortのGold
- Blood economy開始Turn

を含めて比較します。

## Blood Sacrifice

PriestがTempleでSlaveを消費し、Dominion checkを発生させます。

これは、

```text
Blood Slave
＋ Priest turn
＋ Temple
＋ 輸送
```

を宗教圧力へ変えるOrderです。

## Slaver

Tribal King等はSlaver能力でSlaveを得る手段を持ちます。

Slave兵は、

- Screen
- Patrol
- Siege
- Arrow受け
- 高価なSacredの損失分担

へ使います。

---

# 国家Engine

```text
ExpansionでPopulationのあるProvinceを取る
        ↓
Fort・Temple・Labを増やす
        ↓
Mictlan Priestを量産
        ↓
Blood Hunt / Blood Sacrifice / Researchへ分配
        ↓
首都PriestとNahualliへSlaveを集約
        ↓
Sabbath・Summon・Ritual
        ↓
さらにFort・Hunter・Dominionを増やす
```

## 第一の詰まり：Commander Point

Mictlan Priestは、

- Hunter
- Sacrificer
- Researcher
- Battle support

を一体で担当します。

各Fortで毎Turn、

```text
次の一人を
Huntへ送るか
Templeへ送るか
Researchへ残すか
```

を決めます。

## 第二の詰まり：Unrest

Hunterを増やすだけでは、

- Income
- Recruitment
- Commander Points
- Blood Hunt効率

が崩れます。

PatrolとProvince rotationが必要です。

## 第三の詰まり：首都Queue

首都Siteの高位Priestは強力ですが、同じ首都生産枠で競合します。

Fire、Water、Astral、Natureのどれを何Turn生産するかを、Research planから逆算します。

---

# 兵士

## Warrior系

Mictlan Warriorは装備差で役割が変わります。

### Sling＋Spear＋Shield

- 安価な射撃
- Shield Screen
- 接敵後のSpear
- Archer・Light Infantryへの圧力

低Precisionと低Damageを、数と長射程で補います。

### Armored Sling Warrior

軽装版より生存性がありますが、ResourceとGoldを使います。

射撃が通らない敵へ大量生産しないようにします。

### Javelin＋Spear＋Shield

接敵直前のBurstとShield Screenです。

Ammoが少ないため、長時間射撃するUnitではありません。

### Mace＋Javelin＋Shield

高ArmorへSpearよりBluntが有効な場合があります。

敵Protection・Shield・Sizeで選びます。

## Feathered Warrior

基本人間兵よりAttack・Defence・Moraleが高い中核です。

- Expansionの安定
- Screen兼Damage
- Javelin
- First warの一般兵

へ使います。

Sacredだけに依存せず、Feathered Warrior等で前線を支えます。

## Moon Warrior

高MR・Moraleと両手Obsidian weaponを持つDamage役です。

Shieldがないため、

```text
Shield Warriorが先に接敵
→ Moon Warriorが後から入る
```

配置にします。

## Jaguar Warrior

Jaguar WarriorはSacredの主力です。

評価するときは、

- Gold / Resource
- Holy Point / Recruit limit
- BlessなしStats
- 変身・第二形態
- 射撃への弱さ
- Anti-Sacred
- 補充速度

を見ます。

### 役割

- Expansion
- Shock troop
- Fast kill
- Mageへ時間を与える
- Blessを国家全体へ変換

### 弱点

- 軽装
- 射撃
- 高Protection
- Fatigue
- Anti-Sacred
- Capital・Temple圧力

Heavy Blessだけでなく、通常WarriorをScreenへ入れます。

---

# Commander / Mage

## Scout

Blood Hunter Province、Temple、Border、敵Priestを監視します。

Blood国家では後方Scoutが特に重要です。

## Tribal King

- 通常Leadership
- Slaver
- Expansion・Patrol指揮
- Siege

へ使います。

高価なPriestを通常Army transportへ使わないためのCommanderです。

## Mictlan Priest

```text
B1 H1
＋10%でF/W/S/Nから+1
```

Any-fortで量産できる国家基盤です。

### 役割分類

```text
標準B1H1
→ Blood Hunt / Blood Sacrifice

F / W / S / N Random
→ Site Search、Crosspath、Battle support、将来Booster
```

Random個体を通常Hunterへ埋めず、色分けします。

## Nahualli

```text
S1 N2
＋10%でS/D/N/Bから+1
```

- Research
- Nature Site Search
- Astral Remote Search
- Contact Couatl
- Nature booster
- Sabbath / Communion bridge

へ使います。

NahualliはBlood Hunterより、国家Magic Accessを広げる役です。

---

# 首都Site Mage

## High Priest of the Sun

```text
F2 B3 H3
```

- Fire Battle Magic
- High Blood ritual
- Sabbath Master
- Blood Sacrifice
- Fire / Blood booster

へ使います。

国家の最も重要なCasterの一つです。

## Rain Priest

```text
W2 B2 H2
```

- Water support
- Rain / Cold / Quickness
- Water Site Search
- Sabbath
- Tlaloque routeの入口

です。

## Moon Priest

```text
S2 B2 H2
```

- Astral support
- Communion / Sabbath
- Antimagic
- MR attack
- Astral booster

へ使います。

Magic Duelを意識して分散します。

## Priest King

```text
N2 B2 H2
```

- Nature support
- Poison Resistance
- Regeneration
- Contact Couatl
- Blood / Nature ritual

へ使います。

## 首都Queueを研究から逆算

```text
First warでFire AoEが必要
→ Sun Priestを先に生産

Poison / Sustainが必要
→ Priest King

Astral defence / MR attackが必要
→ Moon Priest

Quickness / Water supportが必要
→ Rain Priest
```

とします。

全種類を一人ずつ揃えるだけで数Turn使うため、目的を決めます。

---

# Pretender方針

## Heavy Bless

### 買うもの

- Jaguar WarriorのExpansion
- First warのSacred火力
- Sacred Priest / Commanderへの副次効果

### 代償

- Scales
- Dominion
- Awake状態
- Missing Path
- Blood economy用Gold

### Test

```text
IncarnateなしでExpansion可能か
毎Turn何体のJaguarを得るか
通常兵とMage生産が止まらないか
Anti-Sacredへ第二Armyがあるか
```

## Light Bless＋Scales

Jaguar Warriorの致命的弱点だけを補い、

- Fort
- Mictlan Priest
- 首都Mage
- Patrol
- Growth

へPointを残します。

Blood economyはPopulationを使うため、GrowthとGoldは長期価値を持ちます。

## Awake Expander

国家兵Expansionが不安定なMapで、Pretenderが別方向を取ります。

ただしBlood economy、Bless、Missing Pathへ使えるPointが減ります。

## Rainbow / Missing Path

Air・Earth・Death・Glamour等を補います。

特に、

- Shock Resistance
- Earth Protection
- Death summon
- Booster crosspath

を開けます。

Bloodは国家側で得られるため、PretenderのPathをBloodだけへ過剰投資しない案もあります。

## Dominion

Restricted Dominion国家なので、低Dominionは通常国家以上のRiskです。

Blood SacrificeのSlave・Priest turn・Temple costを含めてDesignします。

---

# Expansion

## Jaguar Expansion

Jaguar Warriorを中心に、

- Shield Warrior
- Tribal King
- Priest / Bless

を組みます。

### 確認する相手

- Archer
- Heavy Infantry
- Cavalry
- Barbarian
- Poison
- Undead
- Elephant

Heavy Blessが一種類のIndieだけに強くならないようにします。

## Mass Warrior Expansion

安価なWarriorを数で出し、Sling・Javelinで接敵前に削ります。

Jaguar supplyをFirst warへ残せます。

## ScreenとDamageを分ける

```text
Shield Warrior：前
Jaguar / Moon：少し後ろ
Slinger：後方
```

にします。

## Slaver

Tribal KingのSlaverで得たSlave兵を、

- Arrow受け
- PD処理
- Patrol
- Siege

へ使います。

高価なJaguarの損失を減らします。

---

# Economy / Fort計画

## Populationを守る

Blood HuntとPatrolはPopulationを消耗します。

Populationは、

- Income
- Blood Hunt
- Supply
- Recruit

の基盤です。

## 第二Fort

第二Fortは、

- Mictlan Priest生産
- Hunter supply
- Temple・Sacrifice node
- Patrol拠点
- Blood route

です。

兵士よりCommander Pointの価値が高いFortです。

## Hunt Province

```text
安全な後方
Populationがある
Labまたは輸送路がある
Patrol担当を置ける
Fort資金を壊さない
```

場所を選びます。

## Temple Network

Restricted Dominionのため、Templeは宗教建物であると同時に国家生存設備です。

Border、Capital、Throne、Plane入口へ優先します。

---

# Blood Economy

## 初期段階

```text
少数Mictlan PriestをHunterへ
→ Unrestと平均Slaveを記録
→ Patrolを追加
→ TempleへSacrifice Priestを置く
→ Research用途ができたらHunterを増やす
```

最初から全PriestをHuntへ置きません。

## 分業

```text
Hunter
Sacrificer
Researcher
Frontline support
Transport
```

を名前・番号で分けます。

## Slave reserve

```text
Dominion維持用
First war Battle用
Ritual用
緊急用
```

へ分けます。

全Slaveを大型Summonへ使い、Border Dominionが消える失敗を避けます。

詳しくは[Blood Economy](../../magic/blood-economy.md)を参照してください。

---

# Magic Access

## Fire

High Priest of the Sunが軸です。

- Fire resistance
- Fire AoE
- Fire Elemental
- Heat
- Blood crosspath

へ使います。

敵Fire Resistanceには通常物理・Astral・Blood summonを用意します。

## Water

Rain Priestが、

- Quickness
- Cold
- Water Elemental
- Rain
- Water summon

を担当します。

## Astral

Moon PriestとNahualliが、

- Antimagic
- MR attack
- Communion / Sabbath
- Site Search
- Booster

へ使えます。

## Nature

Priest KingとNahualliが、

- Poison Resistance
- Regeneration
- Relief
- Summon
- Contact Couatl

へ進みます。

## Blood

Mictlan Priestを量産でき、高位首都PriestをSabbath Master・Ritualへ使えます。

## Missing Path

Air、Earth、Death、Glamourは、Pretender、Hero、Summon、Empowerment等から補います。

Hero accessを保証計画にしません。

---

# Research方針

## Blood Magic

- Blood economyの実戦利用
- Demon / National summon
- Sabbath
- Remote pressure
- High Blood ritual

へ進みます。

## Conjuration

- Contact Couatl
- Elemental
- Tlaloque route
- Nature summon

へつながります。

Contact CouatlはNahualliから、S3N3H2のCasterへアクセスする重要経路です。

## Construction

- Jade Knife
- Blood booster
- Nature / Astral booster
- Resistance Item
- Hunter・Transport保護

へ使います。

## Thaumaturgy

- Site Search
- Astral・MR
- Dominion・Control

へ進みます。

## Enchantment / Alteration

- Resistance
- Regeneration
- Quickness
- Army support

で軽装兵を中盤へ残します。

---

# First War

## 勝利条件

Mictlanは、

```text
Blessed Jaguarで早く前衛を破る
＋
Fire / Water / Nature / Astral support
＋
Blood Slaveを必要箇所へ投入
```

して勝ちます。

## 目的

- Hunterに適したPopulation
- Border Fort
- Temple route
- Throne
- Enemy Capital圧力

を優先します。

## Hunterを守る

Main Armyを前へ出すと、後方HunterがRaidに弱くなります。

```text
Scout
＋ PD
＋ Patrol
＋ Mobile reserve
```

を残します。

## Slaveを全部持ち込まない

Battle Mageへ必要数だけ渡します。

輸送Commander一人へ国家在庫を集中しません。

---

# Battle Script

## Jaguar Army

```text
Priest：Bless
Shield Warrior：Hold and Attack
Jaguar：Hold / Attack Closest または適切Target
Slinger：Fire appropriate target
```

接敵Timingと射撃被害をReplayで確認します。

## Sun Priest

```text
Path / defence
→ Fire resistance / Army support
→ Fire or Blood damage
→ Cast Spells
```

敵Fire Resistanceを確認します。

## Rain Priest

```text
Water boost
→ Quickness / defence / cold support
→ Elemental or control
```

## Moon Priest

```text
Astral defence
→ Antimagic / MR attack
→ Sabbath plan
```

## Sabbath

```text
必要Spell
→ 必要Path
→ 最小Slave数
→ Master数
→ Slave保護
```

の順で作ります。

---

# Counterされるもの

| 相手の手段 | なぜ危険か | 対応 |
|---|---|---|
| Archer | Jaguar・軽装兵が接敵前に損失 | Shield Screen、Storm、機動 |
| 高Protection | Sling・軽武器が通らない | Moon、Mace、Fire、Blood summon |
| Anti-Sacred | Jaguar交換効率を逆転 | 通常兵、Slave、Mage damage |
| Fire Resistance | Sun Priestの火力低下 | 物理、Astral、Water、Blood |
| Shock | Missing Airで対策不足 | Pretender、Item、Scout、分散 |
| Raider | Hunter・Temple・Labを破壊 | Patrol、Fort、Mobile reserve |
| Dominion pressure | Restricted spreadを突く | Sacrifice reserve、Temple network |
| Magic Duel | Moon Priest等のAstralを狙う | 分散、低S交換、Bodyguard |
| Unrest攻撃 | Blood economyとRecruitを同時停止 | Province分散、Patrol、Rotation |

---

# Siege / Raid

## Siege

Slave兵と安価なWarriorを壁削りへ使い、Jaguar・首都MageをStormへ残します。

## Raid

軽装・Forest Survival・安価Commanderを使い、

- Hunter Province
- Temple
- Tax route
- Lab

を狙います。

## 自国後方防衛

Blood Hunter拠点は敵Raidの最優先Targetです。

Hunter数の多いProvinceへ、

- Scout
- Patrol
- PD
- Retreat route

を置きます。

---

# Multiplayer

## 脅威認識

Mictlanは、

- Heavy Bless
- Blood scaling
- Dominion pressure

を持つため、将来脅威として警戒されます。

## 外交で守るもの

- Hunter Province
- Temple network
- Capital Mage queue
- High Population rear
- Blood route

です。

## Blood trade

Slave、Gem、Item、Boosterを外交資源にできますが、国家宗教維持用Slaveを売りすぎません。

---

# よくある失敗

## Blood Huntを始めるが用途がない

Research、Ritual、Battle planが決まっていません。

## Blood Sacrificeを忘れる

Dominionが広がらず、国家全体が弱くなります。

## 全Mictlan PriestをHunterにする

Sacrifice、Research、Battle supportが止まります。

## Jaguarだけを生産する

Holy Point、Gold、Resource、首都依存でArmy数が増えません。

## Heavy BlessでScalesを削りすぎる

Fort、Mage、Patrol、Blood economyが育ちません。

## 首都Priestを目的なく一人ずつ作る

First warの勝利条件が完成しません。

## Random Mictlan Priestを通常Hunterへ埋める

Rare Site Search・Crosspathを失います。

## Hunter Provinceを一か所へ集中する

Raid一回でBlood economyが止まります。

## Sabbath Masterを増やしすぎる

SlaveへFatigueが集中し、国家Casterを全損します。

---

# Test gameで記録するもの

```text
Pretender方針：
Jaguar / Turn：
第一Expansion開始：
Expansion損失：
第二Fort開始Turn：
Mictlan Priest数：
Hunter開始Turn：
平均Slave / Hunter-turn：
Unrest増加：
Patrol投入：
Temple数：
Sacrifice Priest数：
First war用Slave reserve：
首都Priest生産順：
第一Blood Breakpoint：
Hunter Provinceを守るArmy：
```

---

# 毎Turn Checklist

```text
□ MessageとBlood Hunt結果を確認した
□ Hunter ProvinceのUnrestとPopulationを見た
□ Blood Sacrifice担当を設定した
□ SlaveをTemple・Lab・前線へ分けた
□ Hunter / Sacrificer / Researcherを混同していない
□ 首都Priest queueをResearch planと照合した
□ Jaguarと通常兵の生産比率を確認した
□ Random Priestを分類した
□ Hunter ProvinceへのRaid routeをScoutした
□ Sabbath Slaveの生存条件を確認した
```

---

## 関連ページ

- [Blood Economy・Blood Hunt・Blood Sacrifice](../../magic/blood-economy.md)
- [Blood Path](../../magic/paths/blood.md)
- [Communion・Sabbath](../../magic/communions.md)
- [Dominion](../../systems/dominion.md)
- [Pretender設計サンプル](../../pretender/samples.md)
- [Bless](../../pretender/bless.md)
- [Scales](../../pretender/scales.md)
- [命令とBattle Script](../../basics/orders.md)
- [内政・補給・自動化Q&A](../../getting-started/logistics-faq.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [EA Mictlan community reference](https://illwiki.com/dom5/dom6/mictlan-ea)
