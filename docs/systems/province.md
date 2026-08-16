---
title: Province（州・領地）
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# Province（州・領地）

Provinceは、単なる地図上の一マスではありません。

> **人口をGold・Resources・Recruitment・Supplyへ変え、Terrain・接続・Dominion・Magic Siteによって価値が変わる、国家運営の最小単位**

です。

一つのProvinceには、

- Population
- Income
- Resources
- Recruitment Points
- Commander Points
- Supplies / Supply Usage
- TerrainとProvince size
- Dominion / Scales
- Unrest
- Province Defence（PD）
- Local recruitment
- Magic Sites
- Fort / Laboratory / Temple
- Strategic connections
- Retreat route
- Corpses

が重なっています。

Provinceを取る目的は、Map上の色を増やすことではありません。

> **Gold、Mage、Gem、兵士、補給、移動、退路、情報、勝利条件のどれを増やすProvinceなのか**

を決めることが重要です。

!!! note "このページの精度範囲"
    本文はDominions 6.35を対象に、現行Manualへの公式導線、公式変更点、ゲーム内Province画面・Message、固定データ、Turn Order、Community testで確認されている主要挙動を実戦向けに整理しています。Map generator、Nation ability、Magic Site、Global、Event、特殊Terrain、別Plane、Siegeには例外があります。数値は計画用の基準として読み、実際のProvince画面とTooltipも確認してください。

---

## 最初に覚える六つ

### 1. Provinceの価値は「現在値」ではなく「毎Turnの流れ」で決まる

Income 120のProvinceは、毎Turn120 Goldを国家へ送り続けられるなら価値があります。

しかし、

- 税収経路が切れている
- Unrestが高い
- Upkeepと防衛費が大きい
- 前線から遠すぎる
- Fortを建てても雇いたいMageがいない

なら、表示値ほど国家を強くしません。

逆にIncome 30でも、

- 国家にないMageを雇える
- 重要Magic Siteがある
- Cave入口を押さえる
- 安全なRetreat routeになる
- Throneへ通じる唯一の接続である

なら、戦争全体を左右します。

### 2. Ownership、Dominion、Informationは別

Provinceを所有していても、敵Dominion下にあることがあります。

敵Provinceでも、自分のDominion、Scout、Spy、Scryingによって情報を得られます。

```text
旗       ＝ 誰がProvinceを所有しているか
Candles  ＝ 誰のDominionがあるか
Scout等  ＝ 何が見えているか
```

を分けます。

### 3. Goldは国家へ運ぶ必要があるが、Resources・Recruitment・SupplyはLocal

Gold Incomeは通常、Owned Provinceを通ってFriendly Fortまで税収経路を引けなければ国庫へ届きません。

一方、Resources、Recruitment Points、Commander Points、Suppliesは、そのProvinceで使うLocal capacityです。

```text
Gold      ：国家資源
Resources ：Local生産力
RP / CP   ：Local雇用枠
Supply    ：Local補給力
```

同じ数字として扱いません。

### 4. ResourcesとRecruitment Pointsは国庫へ貯まらない

ResourcesやRecruitment PointsはGoldやGemのような全国Stockではありません。

そのProvinceのRecruit queueへ毎Turn割り当てられます。費用を満たせないUnitをQueueした場合、完成まで複数Turnかかることはありますが、余ったLocal capacityを別Provinceへ自由に送ることはできません。

### 5. Terrainと接続は、数値と同じくらい重要

Forest、Swamp、Cave、Seaなどは、

- Population
- Resources
- Site frequency
- Population growth
- Map Movement
- Battle terrain
- Local recruitment

を変えます。

さらに、同じIncomeでも、三方向へ接続する中央Provinceと、袋小路のProvinceでは軍事価値が違います。

### 6. Provinceを失う損害はIncomeだけではない

Raid一回で失う可能性があるものは、

- 今TurnのIncome
- 税収経路
- Retreat route
- LabとGem補給
- TempleとDominion
- Local Mage recruitment
- FortへのResources
- Site Search済みのMagic Site
- Blood HunterとPopulation
- Throneへの接続

です。

敵Provinceを評価するときも同じ視点を使います。

---

# ProvinceのLife Cycle

```text
Scout・Scry
      ↓
Independentまたは敵を攻撃
      ↓
占領・PD 1
      ↓
Unrest・接続・Local recruitを確認
      ↓
用途を決める
  ├─ Income / Tax route
  ├─ Resource feeder / Fort
  ├─ Mage / Site
  ├─ Blood
  ├─ Choke / Relay
  └─ Throne / Plane entrance
      ↓
Site Search・Lab・Temple・Fort
      ↓
防衛・Patrol・Reserve Army
      ↓
前線化、または安全な後方経済へ
```

新しく取ったProvinceを「とりあえず所有」したままにせず、役割を決めます。

---

# Province情報はどこまで見えるか

Dominions 6ではHidden MapとFog of Warがあり、Province情報は観測手段によって変わります。

| 状態 | 主に分かること | 注意 |
|---|---|---|
| 未探索 | 見えているMap範囲・Terrainの一部 | Game settingで選択自体できない場合がある |
| 一度Scout済み | Province名と位置を記憶 | Army内容は古くなる |
| 自Dominionのみ | Name、Income、Scales等の一部 | Ownershipや軍勢の詳細は別 |
| Scout | おおよその兵数、主要Unit、建物等 | Scouting能力・偽装で誤差が出る |
| Spy / Scry | より正確な軍勢、Commander、Site等 | 効果ごとに精度・Durationが異なる |
| 自国所有 | Population、Income、Resources、Recruitment等 | Hidden SiteはSite Searchまで不明 |

!!! warning "古いScout情報"
    一度見たProvince名は残りますが、兵数、Commander、Fort、PD、Gem、Scriptは毎Turn変化します。戦争前のScout情報を最新情報だと思い込まないでください。

## 敵が隠す情報

- Stealthy Unit
- Glamourによる偽装
- Obfuscate
- Fort内部Army
- Hidden Magic Site
- Gem所持
- Battle Script
- 同Turnの増援

は通常のScoutだけでは完全に把握できません。

> **偵察は正解を得る作業ではなく、外したときの被害を減らす作業**

です。

---

# Province画面の主要Stats

| Stat | 何を表すか | 主な用途 |
|---|---|---|
| Terrain | 地形と環境Tag | Population、Resources、Movement、Site、Battle |
| Population | 課税・徴募される住民 | Income、Recruitment、Supply、PD上限 |
| Income | 今TurnのGold収入 | Recruitment、Building、Upkeep、PD |
| Resources | 武器・Armor等のLocal生産力 | Troop recruitment |
| Recruitment Points | Troop用のLocal雇用枠 | 大量Recruit、低Resource兵 |
| Commander Points | Commander用のLocal雇用枠 | Mage、Priest、Commander |
| Supplies | ProvinceがArmyへ供給できる量 | Starvation回避 |
| Supply Usage | 現在いるUnitの必要量 | Army規模の上限 |
| Unrest | 統治混乱 | Income、Resources、Recruitment、Blood Hunt |
| Defence | Province Defence Level | Raider・Event・Scoutへの防衛 |
| Corpses | 埋葬されていない死体 | Reanimation、Ritual、特殊能力 |
| Dominion / Scales | 現地の宗教・環境 | Economy、Supply、Event、Combat、能力 |
| Buildings / Sites | Fort、Lab、Temple、発見Site | 生産・魔法・勝利条件 |

数字を一つずつ見るのではなく、**何が現在のBottleneckか**を探します。

---

# TerrainとProvince size

TerrainはProvinceの初期Population、Resources、成長傾向、Site frequency、Map Movement costへ影響します。

以下は現行Community tableを日本語化した基礎傾向です。Map generator、Mountain・River等のModifier、Site、Nation ability、Scaleによって最終値は変わります。

| Terrain | Population傾向 | Resources傾向 | 基礎Map Move半Step | Site傾向 | Population growth補正 |
|---|---|---|---:|---|---:|
| Plains | 標準 | 標準 | 3 | 標準 | 0.0% |
| Forest | 低い | 高い | 5 | 多い | -0.2% |
| Swamp | とても低い | 標準 | 7 | 多い | -0.4% |
| Waste | 極めて低い | 標準 | 5 | 非常に多い | -0.6% |
| Highlands | 低い | 高い | 6 | 多い | -0.2% |
| Farm | とても高い | 低い | 3 | 少ない | +0.4% |
| Cave | 低い | 標準 | 4 | 標準 | -0.2% |
| Cave Forest | 高い | 標準 | 6 | 多い | +0.2% |
| Crystal Cave | 極めて低い | 高い | 6 | 非常に多い | -0.6% |
| Drip Cave | 低い | 非常に高い | 7 | 標準 | -0.2% |
| Flooded Cave | 低い | 標準 | 5 | 標準 | -0.2% |
| Sea | 低い | 標準 | 5 | 標準 | -0.2% |
| Deep Sea | とても低い | 高い | 5 | 多い | -0.4% |
| Gorge | 低い | 高い | 5 | 非常に多い | -0.4% |
| Kelp Forest | 高い | 標準 | 5 | 標準 | +0.2% |
| Void | 極めて低い | 標準 | 7 | 非常に多い | 0.0% |

## Map Movementは半Stepで考える

UnitはProvince中心から境界へ出て、次のProvince中心へ入ると考えます。

```text
出発Provinceを出るCost
＋
到着Provinceへ入るCost
```

が基本です。複数Provinceを移動する場合、中間Provinceの出入りも支払います。

Forest Survival、Mountain Survival、Swamp Survival、Wasteland Survival等は該当Terrainの負担を軽減し、Starvation時に誰が影響を受けるかにも関係します。

## Mountain Modifier

Map上のMountain borderに接するProvinceは、Populationを減らす代わりにResourcesとSite frequencyを増やす傾向があります。

Farm＋Mountainのような組合せは、GoldとResourcesを両方得られる重要Fort候補になることがあります。

## River Modifier

RiverはPopulationと成長傾向を上げる一方、

- 通常Movement
- 冬季凍結
- Retreat
- River crossing能力

へ影響します。

## Coastal

Water Provinceと接続するLand ProvinceはCoastal扱いになり、

- Sailing
- Amphibious invasion
- Coastal Event・Ritual
- Underwaterとの増援

の対象になります。

## Province size

ProvinceにはSmall、Standard、Large、Capital等のsizeがあり、Population密度の適正値が異なります。

同じTerrainでも、Small ProvinceとLarge Provinceでは、長期Population growthと経済上限が違います。

## Dom6ではTerrainが変化する

Dominions 6では、極端なDominion Scaleや高位Ritual等によってTerrainが変わる場合があります。

したがってTerrainは完全な固定値ではありません。

---

# Population

PopulationはProvince経済の土台です。

主に、

- Income
- Recruitment Points
- Supplies
- Province Defence上限
- Blood Hunt
- Event
- Long-term growth

へ影響します。

## Incomeの基礎

概念的には、Population 100人ごとに基礎Income 1 Goldを生みます。

```text
基礎税収 ≒ floor(Population / 100)
```

ここへSite・Event、Fort Administration、Scales、Unrest、Nation ability等が加わります。

## Populationが減る主な原因

- PatrolによるUnrest鎮圧
- Pillage
- Blood Hunt関連の損耗
- Battle・Massacre
- Disease・Reaper・Population Killer
- Death Dominion
- Event
- Ritual・Global
- Popkill NationのDominion

Populationを短期資源へ変換する戦術は強力ですが、将来のIncome、Recruitment、Supply、PD上限を失います。

## Populationが増える主な要素

- Growth Scale
- TerrainのPopulation growth補正
- RiverやProvince size
- Site・Global・Event
- 特殊National effect

ただし人口密度がTerrain・Province sizeの適正値を超えるほど、自然成長は鈍くなります。

## PDとUnrestの上限

PopulationはProvince DefenceとUnrestの上限にも関係します。

概念的には、Population 10人ごとに上限1を与え、

- PDは最大100
- Unrestは最大500

でCapされます。

低Population Provinceでは、Goldがあっても高PDを購入できません。

---

# Incomeと税収経路

Incomeは、Mage、兵士、Fort、Lab、Temple、Upkeep、Mercenary、PDを支える国家資源です。

## 概念式

完全な処理には複数回の丸めと特殊効果がありますが、判断用には、

```text
Population由来Income
＋ Site / Event
× Fort Administration
× 経済Scales
÷ Unrest補正
```

と考えます。

Unrestの影響は後述します。

## 税収はFortへ通じる必要がある

通常、Province Incomeは、Owned Provinceだけを通る切れていない経路でFriendly Fortへ到達できなければ国庫へ入りません。

```text
孤立Province
  └─ 敵Provinceで遮断
        └─ Friendly Fortへ到達不能
              ＝ Tax incomeなし
```

そのためRaidは、占領した一ProvinceのIncome以上の損害を与えることがあります。

### 税収経路を切る価値

- 深部の高Income群を孤立させる
- Fort ringの接続を切る
- Cave・Sea入口を奪う
- Bridge Provinceを取る
- 敵の新占領地をFortから隔離する

と、複数ProvinceのGoldを同時に止められます。

## Tax Collector

Tax Collector能力を持つCommanderは、Fortへ税収経路を引けないProvinceでもIncomeを国庫へ送れる場合があります。

ただし、

- Commanderが生存しているか
- Provinceを所有しているか
- Siege・Event・特殊National rule

は別に確認します。

Sailing Nation等には海を越えたIncome routeの特殊規則がある場合があります。

## Gem incomeとGold incomeを混同しない

Magic SiteのGem incomeは、Population taxをFriendly Fortへ運ぶ仕組みとは別です。

> **Gold税収経路が切れたから、すべてのGem incomeも同じ理由で停止する**

とは考えません。

Siege中のSite、Lab、Gem回収の特殊処理は[Fort・Siege・Storm](forts.md)を確認してください。

---

# Resources

Resourcesは武器、Armor、Mount装備等を作るLocal生産力です。

Goldが余っていてもResourcesが足りなければ、重装兵や騎兵を十分に雇えません。

## Potential Resourcesと表示Resources

FortのないProvinceは、通常、そのProvinceが持つResource potentialの一部だけをLocal recruitmentへ使います。

概念的には、非Fort ProvinceはPotentialの約半分を使い、Fortを建てると自ProvinceのPotentialをより完全に利用できます。

## FortによるResource draw

FortはAdministrationに応じて隣接ProvinceからResourcesを引き込みます。

主な制限は、

- Adjacent Provinceを自国が所有している
- Land FortはSea Provinceから引けない
- Sea FortはLand Provinceから引けない
- Enemy Provinceから引けない
- FortのあるAdjacent Provinceからは通常引けない

です。

```text
Unforted resource Province
       ↓ Adminでdraw
Resource Fort
       ↓
Heavy Infantry / Cavalry / Giantを生産
```

## Fortを建てない価値

High Resource ProvinceをすべてFort化すると、既存FortがそこからResourcesを引けなくなることがあります。

そのため、

- Troop production Fort
- Resource feeder Province
- Mage-only Fort

を分けます。

## Fort間競合

複数Fortが同じUnforted ProvinceからResourcesを引くと、有限のPotentialを奪い合います。

Capital周辺へFortを密集させた結果、Capital-only重装兵の生産数が落ちる場合があります。

## Resourcesは全国Stockではない

今Turn余ったResourcesを来Turnへ全国備蓄したり、離れたFortへ送ったりはできません。

ただしRecruit queue内のUnitは、ResourcesやRecruitment Points不足により複数Turnかけて完成する場合があります。

---

# Recruitment PointsとCommander Points

## Recruitment Points（RP）

Troopを雇うためのLocal manpowerです。

主にPopulation、Terrain、Building、Unrest、Site、National abilityの影響を受けます。

### RPがBottleneckになる国家

- 低Resourceの軽歩兵を大量に雇う
- Archer・Slingerを大量生産する
- ChaffをSiege用に集める
- Sacredや特殊UnitのRP Costが高い

場合、GoldとResourcesが余っていてもRPで止まります。

## Commander Points（CP）

Commander、Mage、Priest用の別Queueです。

Troop用RPとは共有しません。

FortのないProvinceにも通常1 CPがあり、多くの一般Commanderを雇えます。Fort level・upgradeはCPを追加し、Mage生産数を増やします。

Mageが2 CP以上を必要とする場合、低Level Fortでは一人のRecruitに複数Turnかかることがあります。

## 四つのBottleneck

| 症状 | 足りない可能性 |
|---|---|
| Queueへ追加できない | Gold |
| 重装兵だけ完成しない | Resources |
| 安価な兵を大量に作れない | Recruitment Points |
| Mageが毎Turn完成しない | Commander Points |

Recruitment画面では、単にGold総額を見るのではなく、四つを分けます。

---

# Local recruitmentとPoptype

FortのないProvinceでは、Independent population typeに応じたLocal UnitとCommanderを雇えます。

重要なLocal recruitは、

- Scout
- Priest
- N1 / S1 / D1等のIndependent Mage
- Crossbow / Archer
- Heavy Cavalry
- Amphibious Commander
- Sailing Commander
- Terrain Survival持ち
- Patrol・Pillage・Siege担当

です。

能力値が低いMageでも、国家にないMagic Pathへ入る入口として大きな価値があります。

## Poptypeが決めるもの

- Independent時の守備兵
- Non-Fort Local recruitment
- Non-Fort Province Defence

FortがあるProvinceのPDは、原則として所有NationのNational PDへ変わります。

## Fortを建ててもLocal valueは消えない

FortはNational recruitmentを追加しますが、Local Commander、Site recruit、Terrain recruit等が同時に価値を持つ場合があります。

Fort候補を選ぶときは、IncomeとResourcesだけでなく、毎Turn雇えるCommanderとMageを確認します。

---

# SuppliesとSupply Usage

SuppliesはArmyを維持するLocal補給力です。

Armyは一か月分の食料を全国Stockから持ち運ぶのではなく、基本的に到着Provinceと周辺FortのSupplyへ依存します。

## Supplyを決める主な要素

- Population
- Growth / Death等のScales
- Terrain
- Friendly Fort
- Site
- Supply Bonus Unit・Item
- National effect
- Siege状態

## Supply Usage

UnitごとにSupply Usageがあります。

- 普通のHuman troop
- Giant
- Gluttonous Unit
- Animal
- Need Not Eat
- Supply Bonus持ち

で負担が大きく異なります。

Supply BonusがSupply Usageを上回る場合、Province画面のUsageが負になることもあります。

## Starvation

Supply不足が起きると、TroopはStarving状態になり、Moraleが低下します。連続したSupply不足はDiseaseへつながります。

Terrain Survivalは、該当Terrainで誰がStarvationの影響を受けるかを改善します。

## 大軍の補給計画

```text
Army Supply Usage
≤
目的ProvinceのSupply
＋ Fort・Item・MageのSupply Bonus
```

を確認します。

不足する場合は、

- Armyを複数Provinceへ分ける
- Supply Itemを持たせる
- Nature Mageを同行させる
- Fortを中継する
- 高Supply経路を選ぶ
- Need Not Eat Summonへ置き換える
- Siege期間を短くする

ことで対処します。

Siege内部のSupply storageは通常Provinceとは別なので、[Fort・Siege・Storm](forts.md)を参照してください。

---

# Unrest

Unrestは、Provinceの住民が統治・徴税・徴募へ抵抗している度合いです。

## 主な悪影響

- Income低下
- Resources低下
- Recruitment Points低下
- Commander Points低下
- Blood Hunt成功率低下
- Patrol効率低下
- Event・Rebellion Risk

## 数値の目安

現行の一般式を計画用に単純化すると、

```text
Income比率    ≒ 1 / (1 + 0.02 × Unrest)
Resources比率 ≒ 1 / (1 + 0.01 × Unrest)
RP / CP比率   ≒ max(0, 1 - 0.01 × Unrest)
```

です。

| Unrest | Income目安 | Resources目安 | RP / CP目安 |
|---:|---:|---:|---:|
| 0 | 100% | 100% | 100% |
| 25 | 66.7% | 80.0% | 75% |
| 50 | 50.0% | 66.7% | 50% |
| 75 | 40.0% | 57.1% | 25% |
| 100 | 33.3% | 50.0% | 0% |

Unrest 100ではRecruitment capacityが実質0になるため、新規Unit・Commanderの完成を期待できません。

## Unrestの主な原因

- 占領直後
- Blood Hunt
- Pillage・Raid
- SpyのInstill Uprising
- Battle・Event
- Enemy Ritual
- Causes Unrest能力
- Hostile Dominion
- Site・Global

## 下げる方法

- 自然減少
- Order Scale
- Friendly Dominion
- Province Defenceの一定Level
- Patrol
- Reduces Unrest能力
- Event・Spell・Site

## PatrolのTiming

Income処理は、Patrolによる能動的なUnrest低下より先です。

```text
このTurnのIncome計算
→ Unrest減少
→ 次TurnのIncomeが改善
```

したがって、今Turn大量Patrolしたからといって、同じHostの税収が回復するわけではありません。

## PatrolとPopulation

Active PatrolはUnrestを減らす一方、住民を殺してPopulationを減らします。

Blood economyでは、

```text
Slave income
－ PatrolによるPopulation損失
－ UnrestによるGold・RP損失
```

を一つの収支として見ます。

---

# Province Defence（PD）

Province DefenceはGoldで購入するLocal防衛です。

所有権を失うまで毎回再生成され、通常のUnitのようにMap上を移動したり、Afflictionを蓄積したりはしません。

## PD Cost

通常、次の1 Levelに上げるCostは、そのLevelと同じGoldです。

PD 0からNまでの累計は、

```text
N × (N + 1) / 2
```

です。

| PD | PD 0からの累計Gold |
|---:|---:|
| 1 | 1 |
| 6 | 21 |
| 10 | 55 |
| 15 | 120 |
| 20 | 210 |
| 30 | 465 |

通常、Provinceを占領するとPD 1を得るため、実際の追加支払額は現在Levelとの差になります。

Friendly Civilization、Defence Organizer、National rule等はCostや効果を変える場合があります。

## PD上限

PDは最大100ですが、Populationが少ないProvinceでは、

```text
Population / 10
```

がより低い上限になります。

## Non-Fort PDとFort PD

- Fortなし：Local population typeのPD
- Fortあり：所有NationのNational PD

が基本です。

同じNationでも、Fortの有無によってPD構成が大きく変わります。

## 重要な一般Threshold

現行Community referenceでは、一般に次の機能があります。

- PD 1：Commanderと少数Troop、攻撃情報を得る
- 一定PD：一部の悪Eventを抑止
- PD 15：Stealth detection用のPatrol Strengthが発生
- PD 20：追加Commanderと追加Troop
- 10 PDごと：毎TurnのUnrestを追加で1減らす

Eventの対象やNational PD構成は個別差が大きいため、現在のUIとReplayで確認します。

## PDの役割

- Scout captureを防ぐ
- 軽Raiderを止める
- Enemy compositionをBattle Reportで確認する
- Retreat先を保持する
- Stealth detectionを補助する
- Gem baitとして敵Scriptを使わせる
- Defending ArmyのScreenを増やす
- Fort完成・Reliefまで時間を買う

## PD dump

主戦闘直前にPDへ大量投資し、実Armyの前衛・Screenとして使う戦術です。

PDはArmy Rout計算で通常Unitより軽く扱われるため、適切なPD構成では大量Screenとして機能することがあります。

ただし、

- 固定構成でCounterされる
- Goldを回収できない
- Mage・Itemを持てない
- 高級ThugやAoEに弱い場合がある
- Provinceを失うと投資が消える

ため、敵編成を見て使います。

## 高PDはArmyの代わりではない

PD 20へ210 Goldを使うなら、

- Fort建設
- Mage一人
- Mobile reserve
- Scout網
- Gem用Lab

との比較が必要です。

> **PDは動けないArmyです。移動できないこと自体が最大のCostです。**

---

# DominionとScales

Provinceには現在のDominion strengthとScalesがあります。

Pretender作成時に選んだScaleと、各Provinceで現在表示されるScaleは必ずしも同じではありません。

- Enemy Dominion
- Global
- Site
- Event
- Extreme Scale
- Terrain

によってLocal stateが変化します。

## Provinceへ影響する主なScale

| Scale | 主な影響 |
|---|---|
| Order / Turmoil | Income、Unrest、Event、能力 |
| Productivity / Sloth | Resources、Income、能力 |
| Heat / Cold | Income、Supply、能力、Season |
| Growth / Death | Population、Supply、Income、Aging |
| Luck / Misfortune | Event |
| Magic / Drain | Research、MR、Event、特殊効果 |

Extreme Scaleは通常の数値変化だけでなく、特殊EventやTerrain変化を起こす場合があります。

詳しくは[Dominion](dominion.md)と[PretenderのScales](../pretender/scales.md)を参照してください。

---

# Magic Sites

Magic SiteはProvince価値を大きく変えます。

## 主なSite効果

- Gem income
- Gold・Resources・Supply
- Research Bonus
- Forge・Ritual discount
- Mage・Unit recruitment
- Summon・特殊Order
- Fort type・Wall defender
- Scale・Dominion
- Unrest・Disease・Horror
- Plane入口
- Throne effect

Income 20のWasteが、国家にないMageを雇えるSite一つで最重要Provinceになることがあります。

## Public SiteとHidden Site

Throneや一部の特徴的SiteはScoutでも見えます。

Hidden SiteはSite Searchまで分かりません。

Site level 0は占領時に自動発見され、より高LevelのSiteは対応PathとSearch levelが必要です。

Site levelとGem income量は同じ概念ではありません。

## TerrainとSite frequency

一般に、

- Waste
- Swamp
- Highlands
- Forest
- Deep Sea
- Crystal Cave
- Gorge
- Void

はSiteが多く、Farmは少ない傾向があります。

ただし「ForestはNatureだけ」のように一Pathへ決めつけません。複数PathでSearchします。

## Site Searchの優先順位

1. 新しく取った安全なProvince
2. Site frequencyの高いTerrain
3. 異常なHeat・Cold・Scale・UnrestがあるProvince
4. Fort候補
5. 国家に不足するGem Path
6. Throne・Cave・Sea・Void
7. 戦争で失う前の前線Province

通常の開始Capitalには初期未発見Siteがないため、序盤のManual Search優先度は低いです。Eventで後からSiteが追加された場合は別です。

## 生成データ

- [Magic Siteデータ索引](../data/sites/index.md)
- [Terrain別Site](../data/sites/terrain.md)
- [Gem income Site](../data/sites/gem-income.md)
- [Recruitment Site](../data/sites/recruitment.md)
- [Economy Site](../data/sites/economy.md)
- [Site Search](../magic/site-search.md)
- [Site Search実戦手順](../magic/site-search-playbook.md)

を使って、仕様と運用を分けて確認します。

---

# Corpses

CorpsesはPopulationとは別のProvince resourceです。

Battle、Event、Population death等で増え、

- Soulless等のReanimation
- Raven Feast
- Corpse Eater
- National reanimation
- 特殊Ritual・Site

に使われます。

## 攻略上の意味

大規模Battle後のProvinceは、

- Corpse利用
- Disease
- Unrest
- Population loss
- Retreat route

をまとめて確認します。

Corpsesを利用しない国家にとっても、敵がDeath economyへ変換する可能性があります。

---

# Fort・Laboratory・Temple

BuildingはProvinceの役割を変えます。

## Fort

Fortは、

- National recruitment
- Commander Points
- Resource concentration
- Income bonus
- Supply storage
- Retreat point
- Siege delay

を追加します。

Fortがあるだけで隣接Enemy movementを自動停止させるZone of Controlにはなりません。

詳しくは[Fort・Siege・Storm](forts.md)を参照してください。

## Laboratory

Labは、

- Mage recruitment
- Research
- Forge
- Ritual
- Gem・Item inventory
- Magic reinforcement

の拠点です。

Frontline Labは便利ですが、Raiderに奪われると敵のGem補給・Ritual拠点にもなり得ます。

## Temple

Templeは、

- Dominion spread
- Priest・Sacred recruitment
- Preach
- Blood Sacrifice可能性
- Throne claim支援
- National ability

へ関係します。

Enemy Dominionの強い前線やThroneでは、Templeは単なるRecruitment条件ではなく防衛施設です。

## Building完成Timing

通常Buildingの完成はMovement・Battleより後です。

```text
敵が侵攻
→ Field Battle
→ 後でBuilding完成判定
```

となるため、完成予定Turnに攻撃されるProvinceは、未完成状態で守る必要があります。

---

# Strategic connections

Province connectionは、Army movement以外にも国家全体を決めます。

## 接続が使われるもの

- Friendly / Hostile Movement
- Tax route
- Resource draw
- Retreat
- Fort relief
- Siege包囲
- Sailing・Amphibious invasion
- Cave・Void・Plane移動
- Scout・Raid network

## Choke pointの判定

接続数が少ないだけではChokeではありません。

次へYesが多いほど価値があります。

- 無視すると税収経路が切れるか
- 無視するとRetreat routeが危険か
- Fort内部からBreak Siegeされるか
- 後方からRelief Armyが来るか
- Throne・Lab・Siteを守るか
- Sea・Cave・Void入口か
- 敵が迂回すると大きく遠回りするか

Fort自体ではなく、**無視した代償**がChokeを作ります。

## Friendly Movementと防衛合流

Friendly Province間のMovementはEnemy Provinceへの侵攻より先に処理されます。

そのため中央Provinceへ複数方向からDefenderを合流させ、その後侵攻Armyを迎えられます。

詳しくは[ターン処理順](../reference/turn-resolution.md)を参照してください。

---

# Retreat route

ArmyがRoutして戦場端へ到達しても、安全なProvinceへ退却できなければ失われます。

## 安全性を上げるもの

- 同Province内のFriendly Fort
- Friendly adjacent Province
- 複数方向の退路
- CommanderのMorale
- Terrain Survival
- 退路Provinceの所有維持

## 危険な状況

- Enemy territory深部
- 袋小路
- River・Sea・Plane connection
- Adjacent Provinceを同Turnに奪われる
- Fort storm defence
- Encirclement
- Third-party ownership

> **Battleに勝てるかだけでなく、負けた場合に何人残るか**

を侵攻前に確認します。

Retreatの細部は[戦闘ルール](../basics/combat-rules.md)と[命令とBattle Script](../basics/orders.md)を参照してください。

---

# Provinceの役割分類

## Gold Province

特徴：

- Farm・Plains
- High Population
- Low Unrest
- Tax routeが安全

主な用途：

- Mage upkeep
- Building
- PD
- Mercenary

Fortを建てる場合はMage productionとCommander Pointsを重視します。

## Resource Fort候補

特徴：

- Highlands・Mountain・Drip Cave
- High Resources
- 周辺にUnforted Resource Province
- Troop production需要

主な用途：

- Heavy Infantry
- Cavalry
- Giant
- Resource-heavy Sacred

## Resource feeder

Fortを建てず、隣接Resource FortへPotentialを供給するProvinceです。

Local recruitが不要なら、Fort化しないこと自体が役割になります。

## Mage・Recruitment Province

特徴：

- Useful independent Mage
- Priest・Scout
- Amphibious・Sailing Commander
- Magic Site recruit

Incomeが低くてもLabやFortの価値があります。

## Gem・Site Province

特徴：

- High gem income
- Discount
- Unique summon
- Scale・Global anchor

PD、Fort、Scout、Reserve Armyで守ります。

## Blood Province

特徴：

- High Population
- Safe rear area
- Patrolを置ける
- Transport routeが安全

Hunter、Patroller、Slave輸送、Unrest、Populationを一体管理します。

## Choke・Relay Province

特徴：

- 接続が少ない
- 前線までの中間点
- Retreat・Gem補給・Reliefに有効

Incomeより位置価値が中心です。

## Throne・Plane entrance

勝利条件または別戦域への入口です。

Fort、Temple、Priest、Anti-assassination、Anti-teleport、Reserve Armyまで含めて守ります。

## Buffer Province

低Incomeで失っても致命傷が少ないProvinceです。

- Scout網
- Raid warning
- Retreat route
- 敵のMovement消費
- Counter-raid誘導

に使います。

---

# 新しく取ったProvinceで行うこと

## Capture直後Checklist

1. **PD 1があるか**
2. **Unrestはいくつか**
3. **Incomeは税収経路へ接続しているか**
4. **Local Commander・Mageは何か**
5. **TerrainとProvince sizeは何か**
6. **ResourcesとRPはどちらがBottleneckか**
7. **SupplyはExpansion Armyを支えられるか**
8. **Retreat routeは何本か**
9. **Fort・Lab・Temple・Public Siteがあるか**
10. **Site Searchを誰がいつ行うか**
11. **Enemy最短到達Turnはいくつか**
12. **このProvinceの役割は何か**

## 最初の三Turn

```text
Turn 1：所有・PD・Unrest・Recruit・接続を確認
Turn 2：Site Search、Scout、税収経路を整える
Turn 3：Fort / Lab / Temple / Blood / Bufferの役割を確定
```

全Provinceへ同じBuildingを建てる必要はありません。

---

# Province Defenceの設計

Provinceを守る層はPDだけではありません。

```text
Scout・Scry
→ Buffer Province
→ PD
→ Mobile Raider Hunter
→ Fort wall
→ Relief Army
→ Storm defence
```

## 低PDが向くProvince

- 後方で安全
- 価値が低い
- Mobile reserveが近い
- Scout captureだけ防げばよい

## 中PDが向くProvince

- Raider経路
- Fort建設中
- Lab・Temple・Site
- Retreat route
- Blood Province

## 高PD・PD dumpが向くProvince

- 主戦闘が確実
- National PDが強い
- Buff対象として優秀
- Throne・Choke
- 敵Gemを使わせたい
- Defending Armyと組み合わせる

PD単独の勝率ではなく、**敵に何を使わせ、Reliefまで何Round稼ぐか**で評価します。

---

# Raidで狙うProvince

Enemy Main Armyを倒せない場合でも、Province controlで戦争を有利にできます。

## 優先Target

1. **税収経路を切るBridge Province**
2. **Retreat route**
3. **High gem / Unique Site**
4. **Lab・Temple**
5. **Blood Hunter群**
6. **Resource Fortのfeeder**
7. **Fort建設中のProvince**
8. **Cave・Sea・Void入口**
9. **Throne周辺**
10. **Scout networkの中継点**

## Raidの価値を測る

```text
獲得Income
＋ 停止させるEnemy Income
＋ 切断するResource / Retreat / Reinforcement
＋ 破壊するInfrastructure
－ Raider損失Risk
```

で考えます。

Income 20のBridge Provinceが、背後のIncome 400を孤立させるなら最優先Targetです。

---

# 実戦例

## 例1：High Income FarmだがResourcesが低い

状況：

- Populationが高い
- Incomeが高い
- Resourcesが低い
- 安全な後方

判断：

- Mage Fort候補
- Scout・Priest・Commander生産
- Heavy troop生産Fortにはしない
- 隣接High Resource Provinceを別Fortへ集める

> **Gold FortとTroop Fortを分ける。**

## 例2：Highland＋Mountainの低Population Province

状況：

- Incomeは低い
- Resourcesは高い
- 接続3本
- Capital-only重装兵の増援先

判断：

- Resource Fort候補
- Troop productionで回収
- 周辺Resource feederをFort化しすぎない
- Supply不足を確認

## 例3：表示Income 150だが孤立している

状況：

```text
自国Fort ─ 自国Province ─ 敵Raid ─ Income 150 Province
```

結果：

税収経路が切れ、表示上価値があっても国庫へ届きません。

Counter：

- Bridge Province奪回
- 新Fort建設
- Tax Collector配置
- 海越しの特殊Income route確認

## 例4：Blood HuntでUnrest 80

概算：

```text
Income  ≒ 1 / 2.6 ＝ 約38.5%
Resources ≒ 1 / 1.8 ＝ 約55.6%
RP / CP ＝ 約20%
```

同TurnにPatrolしても、そのTurnのIncome処理は先です。

判断：

- Hunter数を分散
- Patrolを増やす
- Population損失を記録
- Mage recruitment ProvinceとBlood Provinceを分ける

## 例5：PD 20でRaiderを止めたい

PD 0からなら210 Goldです。

同じGoldで、

- Mage
- Fort進捗
- Mobile Commander＋Troop
- Scout網

を買える可能性があります。

敵Raiderの構成、National PD、Relief Army到達Turnを見てから投資します。

## 例6：Income 15だがUnique Mage Siteがある

Income表では低価値でも、国家にないAstral Mageを毎Turn雇えるなら、

- Communion
- Booster chain
- Site Search
- Anti-Magic
- Magic Phase

への入口になります。

Fort、Lab、PD、Scoutを優先します。

## 例7：Enemy territoryへ一Province深く侵攻

勝率は高くても、Friendly adjacent Provinceが一つしかありません。

同TurnにそのProvinceをRaiderに取られると、敗戦時のRoutが大量死へ変わります。

侵攻前に、

- 第二Retreat route
- Reserve Army
- PD
- Fort
- Movement order

を確認します。

## 例8：Cave entrance

Incomeは低いが、地上と地下を結ぶ唯一の入口です。

価値は、

- Tax route
- Retreat
- Fort relief
- Resource connection
- Enemy invasion
- Site access

を二Plane間で制御できることにあります。

Fort・Temple・Scout・Mobile reserveの優先度が高くなります。

---

# 症状から原因を探す

| 症状 | 最初に確認するもの |
|---|---|
| 表示Incomeが国庫へ入らない | Friendly Fortへの税収経路 |
| Goldがあるのに重装兵が出ない | Resources |
| 軽兵を大量Recruitできない | Recruitment Points |
| Mageが毎Turn完成しない | Commander Points |
| Fort建設後にCapital Resourcesが下がった | Resource draw競合 |
| 大軍が急に弱くなる | Supply不足・Starvation |
| Blood Hunt後に経済が崩れる | Unrest・Population・Patrol |
| PDがRaidを止めない | PD構成・敵Damage type |
| Site Search成果が少ない | Terrain、Search level、未Search Path |
| Rout後の損失が大きい | Retreat route・Fort・隣接所有 |
| Fortがあるのに敵が迂回する | 実際にはChokeでない |
| 新Building完成Turnに失った | BattleがBuilding completionより先 |
| Provinceを取ったのにMagic diversityが増えない | Local recruitにLab/Fort条件、Site未発見 |

---

# よくある誤解

## 「Incomeが高いProvinceが常に最優先」

Throne、Unique Site、Mage、Choke、Retreat routeの方が重要な場合があります。

## 「Resourcesは国全体で共有される」

ResourcesはLocalです。高Resource Fortがあっても、遠いFortの重装兵には使えません。

## 「Resourcesは毎Turn全部消えて何も進捗しない」

全国Stockにはなりませんが、Recruit queueのUnitが複数Turnかけて完成することはあります。

## 「Fortは隣接Enemy Movementを止める」

自動Zone of Controlはありません。Fortを無視した場合の補給・退路・Relief Riskが敵を拘束します。

## 「PDは安いArmy」

低Levelは効率的ですが、高PDの累計Costは急増します。移動できず、Province喪失で投資が消えます。

## 「PatrolしたTurnからIncomeが戻る」

Income処理が先です。PatrolによるUnrest改善は主に次Turnへ効きます。

## 「Gold routeが切れるとGem incomeも同じように止まる」

Gold taxationとMagic SiteのGem処理は別です。Siege・Lab固有処理を混同しないでください。

## 「ForestならNature SiteだけSearchすればよい」

Terrainはfrequencyを変えますが、単一Pathへ限定しません。

## 「一度Scoutすれば情報は最新」

記憶されるのは主にProvince名と位置です。Army、PD、Building、Gem、Scriptは更新されます。

## 「Friendly Provinceが一つあればRoutは安全」

同Turnの所有権変化、Fort storm、River・Sea・Plane、Random retreatで失敗します。

---

# Province評価Template

```text
Province ID / Name：
Owner：
Dominion / Scales：
Information source：Scout / Spy / Scry / Owned

Terrain：
Province size：
Connections：
Sea / Cave / Void / River / Mountain：
Enemy最短到達Turn：

Population：
Income：
Tax route：
Resources：
Recruitment Points：
Commander Points：
Supplies：
Supply Usage：
Unrest：
PD：
Corpses：

Local troops：
Local commanders / Mages：
Public Sites：
Discovered Sites：
Search済Path / Level：

Fort：
Laboratory：
Temple：

Retreat route：
Relief route：
Mobile reserve：
Stealth / Raid risk：

役割：
Gold / Resource Fort / Resource feeder / Mage / Gem / Blood / Choke / Relay / Throne / Buffer

次の一手：
PD / Patrol / Search / Build / Recruit / Scout / Fortify / Abandon
```

---

# 検証が必要なEdge case

この総合記事では、Province運用に必要な主要関係を扱っています。

次は個別のTest pageへ分離する価値があります。

- Income formulaの全丸め順
- 特殊Nationの海越しTax route
- Tax CollectorとSiege・Planeの全例外
- Resource drawのcross-plane connection
- 複数Fort競合の厳密な丸め
- Recruitment PointsとCommander Pointsの進捗保存
- PatrolのDom6正確なUnrest reduction formula
- PDによるEvent preventionの全Threshold
- Scout reportの精度とObfuscate
- Rout・Retreatの全分岐
- Terrain alterationとProvince size
- Siege中のSite・Lab・Gem income

未確認部分を推測で固定せず、Battle Message、Income summary、Recruit queue、Test gameで確認します。

---

## 関連ページ

- [Fort・Siege・Storm](forts.md)
- [Dominion](dominion.md)
- [Throne of Ascension](thrones.md)
- [ターン処理順](../reference/turn-resolution.md)
- [序盤拡張](../getting-started/expansion.md)
- [最初の戦争](../getting-started/first-war.md)
- [戦闘ルール](../basics/combat-rules.md)
- [命令とBattle Script](../basics/orders.md)
- [Battle Replayの読み方](../getting-started/battle-replay.md)
- [GemとBlood Slave](../magic/gems.md)
- [Site Search](../magic/site-search.md)
- [Recruitmentデータ](../data/recruitment/index.md)
- [Magic Siteデータ](../data/sites/index.md)

## 主な情報源

- [Dominions 6公式Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
- [illwiki: Province Attributes](https://illwiki.com/dom5/dom6/province-attributes)
- [illwiki: Population](https://illwiki.com/dom5/dom6/population)
- [illwiki: Unrest](https://illwiki.com/dom5/dom6/unrest)
- [illwiki: Supplies](https://illwiki.com/dom5/dom6/supplies)
- [illwiki: Province Defence](https://illwiki.com/dom5/game-mechanics/province-defence)
- [illwiki: Map Movement](https://illwiki.com/dom5/dom6/map-movement)
- [illwiki: Stealth](https://illwiki.com/dom5/dom6/stealthy)
- Dominions 6.35ゲーム内Province画面、Recruit queue、Income summary、Message、Battle Replay

!!! note "記事状態"
    Provinceの主要Stats、Terrain傾向、税収経路、Resource draw、Recruitment、Supply、Unrest、PD、Site、Connection、Retreatの実戦上の関係を6.35向けにレビューしています。すべての丸め、特殊Nation、Event、Siege、別Planeの内部例外を実験で証明した状態ではないため、記事Statusは`reviewed`です。
