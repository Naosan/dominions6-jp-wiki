---
title: Forts
status: expanding
verified_version: "6.35"
last_verified: "2026-08-14"
---

# Forts

Fortは防壁であると同時に、**Mage・Commander・国家兵を毎Turn生産する国家経済施設**です。

Fort一つの価値は、壁の厚さだけでなく、

- Commander Point
- Recruitment
- Resources
- Laboratory / Temple
- Retreat / reinforcement
- Strategic position
- Siege / Stormまで稼ぐTurn

で決まります。

---

# Fortの主な役割

## Mage生産

多くのNational MageはFortを必要とします。

第二Fortを建てることは、将来の毎Turn ResearchとBattle Mage数を増やすことです。

## 国家兵生産

National Unit、重装兵、Sacred、CommanderのRecruit拠点になります。

## Resourcesの集中

Fortは周辺ProvinceからResourcesを引き込み、重装兵生産を可能にします。

## Laboratory / Templeの防衛

LabとTempleを壁の内側へ置き、Mage、Gem、Item、Dominionを守ります。

## Choke point

Enemy ArmyをFortへ拘束し、別方向のRaid・救援・集結時間を得ます。

## Retreat /補給拠点

Armyの退却先、Gem補給、Item交換、Mage集合地点になります。

---

# Fort建設のTiming

Fortは早いほど長く生産しますが、建設Goldは現在のArmyとExpansionを減らします。

## 早期Fortが向く状況

- 初期Expansionが安定
- 国家兵だけでIndieを取れる
- Cheap Mageを各Fortで量産
- Capital Resourceが不足
- 複数方向へ戦線が伸びる
- 高Income / High Resource候補を確保

## 遅らせる状況

- 目前にRush
- Expansion Armyが一つしかない
- Capital-only Mage / Sacred依存
- Gold不足
- Fort候補が前線で守れない
- Awake Expanderが死亡・停滞

### 判断式

```text
Fort建設で失う現在戦力
<
Fortが完成後に生むMage・兵士・Resources・位置価値
```

---

# Fort建設地

## High Income

MageとCommanderの継続雇用に向きます。

## High Resources

重装兵、Cavalry、Giant Armorへ向きます。

## Choke point

少ない接続で広い後方を守ります。

## Border

侵攻拠点になりますが、完成前に攻撃されるRiskがあります。

## Important Site

Mage recruitment、Forge / Ritual discount、Gem Siteを守ります。

## Throne

Victory PointとThrone effectを守ります。

## Plane entrance

地下・海・別Planeからの侵入を止めます。

---

# Fort type

Fortは国家・Terrain・建設能力によって種類と強化段階が異なります。

主な違い：

- Wall integrity
- Commander Point
- Resources
- Recruitment
- Build time / cost
- Supply
- Special defence

一部CommanderはFort upgradeや特殊Fort建設能力を持ちます。

### 攻略上の意味

- 研究拠点：Commander Point優先
- 前線：WallとChoke優先
- 重装生産：Resources優先
- 後方：安価で早いFortでも十分

すべてを最大Fortへ強化する必要はありません。

---

# Commander Point

Commander Pointは、Fortで一TurnにどのCommanderを何人雇えるかを制限します。

Mage recruitmentがCommander Point 2以上を使う国家では、Fort upgradeの価値が高くなります。

Fort数だけでなく、

```text
毎TurnのCommander Point
÷ Mage一人の必要Point
```

を見ます。

---

# ResourcesとFort

FortはProvinceと隣接地からResourcesを引き込みます。

## Resource Fort

- Mountain / Highland
- Productivity
- Resource bonus Commander / Site
- National fort bonus

を組み合わせます。

## Resource競合

近接したFort同士は同じ周辺ProvinceのResourcesを奪い合う場合があります。

Fortを密集させる場合は、各Fortで本当に兵士を生産するか、Mage専用Fortにするか決めます。

---

# LaboratoryとFort

Labを建てると、

- Mage recruitment
- Research
- Forge
- Ritual
- Gem / Item transfer
- Teleport network

が利用できます。

## 前線Lab

Gem補給とBattle Mage増援に便利ですが、Fortが落ちるとItem・Mageを失います。

## 後方Lab

Research / Forge / Ritualを安全に行います。

Rare MageとBoosterは後方へ置きます。

---

# TempleとFort

TempleをFort内へ置くと、

- Dominion spread
- Priest / Sacred recruitment
- Preach拠点
- Throne防衛

が安定します。

Enemy Dominionが強い前線Fortでは、TempleとPriestがFort defenceの一部になります。

---

# Siege

Enemy FortへArmyがいるとSiegeが始まります。

攻撃側は壁を破壊し、防御側は壁を修復・維持します。

主な要素：

- UnitのStrength / Size
- Siege Bonus
- Castle Defence
- Army数
- Fort wall
- Commander / Site / Spell

## Siege strength

高Strength Giant、Sapper、Siege engine、Siege bonus Unitは少数でも壁を壊します。

## Castle defence

Engineer、守備Unit、Fort能力等で壁を維持します。

## 攻略上の意味

Army戦で勝ってもSiege力がなければFortを取れません。

侵攻Armyには、

- Siege Unit
- Supply
- Gem補給
- Storm Army
- Enemy relief迎撃

が必要です。

---

# Storm Castle

壁が十分破壊されるとStormできます。

Storm戦では通常のField battleと異なり、狭い進入口・壁・Tower・配置が戦闘へ影響します。

## 攻撃側

- Gateへ集中するUnit
- Flying / Teleport
- AoE
- Siege / Wall crossing
- Assassin / Remote damage
- Mage placement

を準備します。

## 防御側

- Gateに高Protection / Pike
- Archer / Mageを後方へ
- ChokeへAoE
- Castle defence Commander
- Retreat不能Risk

を利用します。

### 注意

Fort内の防御Armyは逃げ場がなく、Routが全滅へつながりやすくなります。

---

# Siege中の状態

Fortが包囲されると、

- 外部Recruitment / Resource
- Income / Supply
- Mage移動
- Lab network
- Dominion
- Disease / Starvation

へ影響が出ます。

Fort内に大軍を詰め込みすぎるとSupply不足になります。

---

# Relief Army

Fort救援では、Fort内Armyと外から来たArmyがTimingを合わせます。

確認：

- Turn処理順
- Break Siege / movement order
- Magic Phase attack
- Enemy reinforcement
- Retreat route
- Commander / Gem

Fort内ArmyだけでStormを受けず、外部ArmyでSiegerへ戦闘を強制します。

---

# Forward Fort

前線Fortの目的：

- Gem / Item補給
- Battle Mage recruitment
- Retreat route
- Enemy movement遮断
- Siegeで敵主力を固定
- Temple / Dominion

## 建てるRisk

- 完成前に奪われる
- Enemyの補給拠点になる
- GoldをArmyから奪う
- Chokeでなければ迂回される

Enemyが奪ったときの価値も考えます。

---

# Rear Fort

後方Fortの目的：

- Safe Research
- Forge / Ritual
- Blood economy
- Rare Mage recruitment
- Reserve Army
- Plane / Coast防衛

PDだけでなく、Raiderを倒せるMobile reserveを置きます。

---

# Fort数と国家設計

## Mage-heavy国家

Fort数がResearch capです。早期に複数Fortを作ります。

## Capital-only依存

Fortを増やしても主力Mage / Sacredが増えない場合、Gold回収が遅くなります。それでもScout、indie Mage、通常兵、Strategic positionには価値があります。

## Summon-heavy国家

FortよりLab networkとGem Siteを優先する場合があります。

## Blood国家

後方Fort / LabがHunter、Patrol、Slave storage、Summonを守ります。

## Giant / Resource-heavy国家

High Resource FortとProductivityが必要です。

---

# Fort defenceの層

Fortを守る方法は壁だけではありません。

1. ScoutでEnemyを発見
2. Choke / Dominionで侵入を遅らせる
3. PDで小Raiderを止める
4. Mobile ArmyでSiegeを破る
5. WallでStormまで時間を稼ぐ
6. Gate defenceでStormを撃退
7. CounterattackでEnemy Retreatを塞ぐ

Fort内へ全軍を閉じ込めるより、外から動けるArmyを残します。

---

# RaidとFort

Enemy Fortを取れなくても、周囲Provinceを奪うことで、

- Resources
- Income
- Supply
- Retreat
- Reinforcement
- Dominion

を削れます。

Fortだけ残して周囲を支配すれば、Enemy Armyを孤立させられます。

逆に自国Fortが包囲されたとき、周辺Provinceを守らないと救援と補給が困難になります。

---

# よくある失敗

## 第二Fortが遅い

Mage数とResearchが頭打ちになります。

## 前線Fortを完成前に失う

BuilderとGoldをEnemyへ渡します。

## FortをIncomeだけで選ぶ

Resources、Choke、Site、Commander Pointを見ます。

## 全Fortを最大強化

Goldを使いすぎます。役割別に必要段階を選びます。

## Siege Unitがいない

Enemy reliefまでに壁を壊せません。

## Fort内へ大軍を詰め込む

Supply不足とRout全滅Riskが増えます。

## Lab / Boosterを前線へ集める

Fort一つの喪失でMagic accessを失います。

## Fortがあるから安全と思う

Magic Phase、Assassin、Remote ritual、Dominion kill、Starvationがあります。

---

# Fort計画テンプレート

```text
Province：
目的：Mage / Resource / Choke / Throne / Site / Blood
Income：
Resources：
Connections：
Enemy到達Turn：
建設Cost / Turn：
Fort type：
Commander Point：
Lab：
Temple：
生産Mage：
生産Unit：
Siege defence：
Relief route：
奪われた場合のRisk：
```

---

## 関連ページ

- [Province](province.md)
- [Dominion](dominion.md)
- [Throne of Ascension](thrones.md)
- [ターン処理順](../reference/turn-resolution.md)
- [Research](../magic/research.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
