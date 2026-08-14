---
title: Province
status: expanding
verified_version: "6.35"
last_verified: "2026-08-14"
---

# Province

Provinceは、単なる地図上の一マスではありません。

各Provinceは、

- Income
- Resources
- Population
- Supply
- Terrain
- Dominion / Scales
- Unrest
- Province Defence
- Recruitment
- Magic Site
- Fort / Laboratory / Temple
- Strategic connection

を持つ経済・軍事・魔法の単位です。

Provinceを取る目的は面積を増やすことではなく、**国家のGold・Mage・Gem・移動・勝利条件を増やすこと**です。

---

# Provinceの主要Stats

## Income

毎Turn得られるGoldです。

主に、

- Population
- Terrain
- Scales
- Unrest
- Dominion
- Site / Event
- Tax / pillage等

の影響を受けます。

### 攻略上の意味

- MageとCommanderの継続雇用
- Fort / Lab / Temple建設
- Upkeep
- Mercenary
- Province Defence

を支えます。

高Income Provinceは第二Fort候補ですが、Resourceが低い場合は重装兵生産へ向きません。

---

## Resources

そのProvinceでUnitをRecruitするための生産力です。

Resourceは毎Turn使い切りで、国庫へ貯まりません。

### 影響

- Terrain
- Productivity / Sloth
- Fort
- 隣接ProvinceからのResource draw
- National ability
- Commander / Site bonus

### 攻略上の意味

- 重装歩兵
- Cavalry
- Giant armor
- Siege / Sapper

を何人雇えるか決めます。

Goldが余ってもResourceがなければ兵士は作れません。

---

## Recruitment Points

ProvinceでUnitを雇う上限です。

Resourceが余っていてもRecruitment Pointが不足すれば大量生産できません。

軽装・低Resource Unitを大量生産する国家ではRecruitment Pointが主な制約になります。

---

## Population

Income、Supply、Blood Hunt、Event、Long-term economyの土台です。

Populationは、

- Growth / Death
- Blood Hunt / Patrol
- Pilliage
- Disease / Event
- Global / National effect

で変化します。

### 攻略上の意味

Populationを短期資源へ変換する戦術は強力ですが、長期IncomeとBlood incomeを失います。

---

## Supply

Armyが食料・補給を得られる量です。

Supply不足では、

- Starvation
- Disease
- Morale / Fatigue問題
- Army停滞

が発生します。

### Supplyを増やす

- Nature Mage / Spell
- Supply Item
- Growth
- Friendly Dominion / Scale
- Fort / Site
- Army分散

### 大軍運用

一つの巨大Armyを動かす場合、戦闘力だけでなく通過ProvinceのSupplyを確認します。

---

# Terrain

TerrainはIncome・Resources・Supply・Movement・Recruitment・Siteへ影響します。

主なTerrain：

- Plains
- Forest
- Mountain
- Highland
- Swamp
- Waste
- Farm
- Sea / Deep Sea
- Cave / Underground
- Coast / River等の接続要素

## Farm / Plains

PopulationとIncomeが高い傾向があります。Gold Fort候補です。

## Mountain / Highland

Resourcesが高い傾向があり、重装兵生産・Earth Site・Fort候補です。

## Forest

Nature Site、Forest recruitment、Stealth / Survival、Supplyに関係します。

## Swamp

移動とIncomeに不利な場合がありますが、Nature / Water Siteや特殊Recruitmentを得ます。

## Waste

Population・Supplyが低い一方、Fire / Death等のSite・特殊国家に価値があります。

## Sea

水中適性、Water Breathing、Aquatic Unit、別Recruitmentが必要です。

## Cave / Plane

Dominions 6では複数Planeと地下領域があります。

地上との接続点は戦略的Choke pointになり、Cave適応、Darkvision、Underground recruitmentが重要です。

---

# Strategic movement

Province connectionはArmyの移動、Retreat、Trade、Raid、Fort救援を決めます。

## Choke point

少数の接続しかないProvinceへFortを建てると、防衛線を作れます。

## Retreat route

戦闘に負けたArmyがどこへ逃げるか考えます。

Friendly隣接ProvinceがなければRoutが大量死へ変わります。

## River / Mountain / Sea

Survival、Flying、Sailing、Amphibious、Seasonで移動可否・Costが変わる場合があります。

## Plane connection

地下・異Planeへの入口を失うと、ArmyとGem Siteが分断されます。

---

# Province Defence（PD）

Province DefenceはGoldを投資して得る現地防衛です。

PDは国家・Province・投資値でUnitとCommanderが変わります。

## PDの役割

- Scout / weak Raiderを止める
- Enemyに本隊を使わせる
- Patrol / detection
- Fort救援まで時間を稼ぐ
- Enemy scriptとGemを消費させる
- Retreat routeを確保

## PDへ投資する基準

### 低投資

- Scout対策
- Retreat先
- Important Siteの最低防衛
- Enemy movement detection

### 中投資

- Raiderが頻繁
- Choke point
- Fort建設中
- Lab / Temple / Throne

### 高投資

高PDはArmyの代替ではありません。

- National PDが特に強い
- Throne defenceと合流
- Enemy Gem burn
- Emergency defence

など明確な理由が必要です。

## PDの弱点

- 固定構成でCounterされる
- 移動できない
- Gold回収不能
- Mage support不足
- 高級Thugへ弱い

ReplayでPD Unitを確認し、敵Thugが何に負けるか把握します。

---

# Unrest

UnrestはIncome、Recruitment、Event、Blood Hunt等へ悪影響を与えます。

主な原因：

- Blood Hunt
- Enemy ritual
- Spy
- Pillage
- Tax / Event
- Battle / Siege
- National effect

## 下げる方法

- Patrol
- Order
- Special unit / Commander
- Event / Spell
- Blood Hunter分散

PatrolはPopulationを減らす可能性があるため、Blood economyでは収入と長期Populationを比較します。

---

# Recruitment

## Local recruitment

Fortがなくても、Independent Commander・兵士を雇えるProvinceがあります。

特に重要：

- N1 / S1 / D1等のindependent Mage
- Priest
- Scout
- Crossbow / Archer
- Heavy cavalry
- Amphibious Commander
- Sailing / Survival持ち

弱いMageでも、国家にないPathの入口として価値があります。

## Fort recruitment

National Unit / Mageの多くはFortを必要とします。

Fort建設は、そのProvinceを国家生産拠点へ変えます。

---

# Magic Site

Magic Siteは隠れている場合があります。

主な効果：

- Gem income
- Mage / Unit recruitment
- Ritual / Forge discount
- Scale
- Disease / Horror / Unrest
- Summon / Special order
- Throne / Global effect

## Site Search

### Manual search

MageがProvinceで対応PathをSearchします。

### Remote search

Ritualで離れたProvinceをSearchします。

### 優先Province

- 首都周辺
- 高Site frequency Terrain
- Fort候補
- 安全な後方
- Path不足Gemの期待地

ただし「ForestはNatureだけ」のように決めつけず、複数PathでSearchします。

## Site connection

Site incomeをLab networkへ回収するため、Friendly Provinceの接続を維持します。

Raidで経路を切られるとGem economyへ影響します。

---

# Fortを建てるProvince

## 高Income Fort

Mage生産とGold economyを重視します。

## 高Resource Fort

重装兵・Cavalry・Giantを生産します。

## Choke Fort

地理的防衛を重視します。

## Forward Fort

侵攻、補給、Lab、Retreat routeを作ります。

## Site Fort

重要Mage recruitment、discount、Gem Siteを守ります。

## Throne Fort

Victory Pointと特殊効果を守ります。

一つのFortで全役割を満たす必要はありません。

---

# Laboratory

Labは、

- Mage recruitment
- Research
- Ritual
- Forge
- Gem / Item管理
- Teleport network

の拠点です。

EnemyにLabを奪われると、Gem・Item補給とRitual networkが崩れます。

Frontline Labは便利ですが、Raid Riskがあります。

---

# Temple

Templeは、

- Dominion spread
- Sacred / Priest recruitment
- Prophet / Preach支援
- Throne / religious defence
- National ability

へ関係します。

Templeをどこへ建てるかはDominion戦とBless運用を決めます。

---

# Raidの価値

Province Raidで得るものはIncomeだけではありません。

- Enemy Gem connectionを切る
- Retreat routeを塞ぐ
- Fort reinforcementを止める
- Blood Hunt Provinceを破壊
- Lab / Templeを奪う
- Enemy主力Armyを分散
- Throneを孤立
- Scout networkを失わせる

敵の大軍を倒せなくても、Province controlで戦争に勝てます。

---

# Province優先度

| 優先 | Province例 | 理由 |
|---|---|---|
| S | Throne / Unique Site / Choke | 勝利条件・国家技術 |
| A | High income / High resource Fort | Mage・Army生産 |
| A | Blood / Gem economy拠点 | 戦略資源 |
| B | Retreat / connection | Army movement |
| B | Useful indie recruitment | Magic diversity |
| C | 低Income・孤立 | Map control、緩衝地帯 |

---

# よくある失敗

## IncomeだけでFortを選ぶ

Resource、Choke、Site、前線距離も見ます。

## 全Provinceへ高PD

Fort・Mage用Goldを失います。

## Site Searchを後回し

中盤Gem incomeとBooster chainが遅れます。

## Labを無防備に増やす

Enemy RaiderへItem・Gem補給拠点を与えます。

## Retreat routeを考えない

勝てない戦闘がArmy全滅になります。

## Blood Provinceを前線にする

Hunter、Population、Slave輸送を同時に失います。

## Plane入口を軽視

地下・海・別Planeから後方へ侵入されます。

---

# Province評価テンプレート

```text
Income：
Resources：
Population：
Supply：
Terrain：
Connections / Choke：
Local recruitment：
Known Sites：
Search済Path：
Dominion / Scales：
Unrest：
PD：
Fort / Lab / Temple：
前線までの距離：
Retreat route：
主な用途：Gold / Resource / Choke / Site / Blood / Throne
```

---

## 関連ページ

- [Forts](forts.md)
- [Dominion](dominion.md)
- [Throne of Ascension](thrones.md)
- [GemとBlood Slave](../magic/gems.md)
- [ターン処理順](../reference/turn-resolution.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
