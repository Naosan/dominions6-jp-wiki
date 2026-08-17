---
title: 召喚・Global・遠隔Ritual
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
---

# 召喚・Global・遠隔Ritual

戦略魔法は、強いSpellを一回唱えることではありません。

> **Research、Magic Access、Gem income、Lab、Caster、Target、継続費、敵Counterを一つの生産計画へ接続すること**

です。

このページでは、[LA Bogarus — Age of Heroes](../nations/la/bogarus.md)を主要例として、

- Unit・Mage summon
- Global Enchantment
- Remote attack
- Remote summon
- Terrain・Province操作
- Monthly Ritual
- Dispel・Overcast
- Recursive Magic Access

を整理します。

!!! warning "数値とTiming"
    Ritualの正確なResearch、Path、Gem、Range、Plane、Target条件、Unique状態はPatchで変わります。現在のSpell description、Ritual画面、Messageを正本にしてください。

---

## 最初に覚える十項目

| 項目 | 最初の理解 |
|---|---|
| Ritual | Labから戦略Mapを対象に唱えるMagic |
| Summon | Unit・Commander・MageをGem等から生産するRitual |
| Remote attack | 離れたProvinceへ攻撃・Event・Battleを発生させるRitual |
| Global | 世界全体へ継続効果を与え、共有Slotを使うSpell |
| Monthly order | 条件を満たす間、同じRitual・Forgeを繰り返す命令 |
| Access chain | Booster・Summon Mage・Empowermentで次のPathへ到達する経路 |
| Overcast | 最低Costより多くGemを投入し、Global競争等を強化する考え方 |
| Dispel | 敵Globalを除去する戦略 |
| Magic Phase | RitualやMagic Movementが通常Movementより前に処理されるPhase |
| Caster security | Ritual casterをAssassination・Raid・Lab喪失から守ること |

---

# 戦略魔法の四層

## 1. Research

Spellが解禁されているか。

## 2. Access

誰が必要Pathへ届くか。

- Native Mage
- Booster
- Communionは戦闘のみ
- Summon Mage
- Pretender
- Hero
- Empowerment
- Item

を分けます。

## 3. Economy

Gem・Blood Slaveを一回だけでなく継続供給できるか。

## 4. Operations

- Lab
- Target
- Range
- Plane
- Monthly order
- Caster保護
- Message確認

を管理できるか。

四層の一つでも欠けると、Research済みでも国家戦略になりません。

---

# Ritual計画表

RitualをResearchする前に、次を書きます。

```text
Ritual：
目的：
Research：
Caster：
Base Path：
Booster後Path：
一回Cost：
月間Cost：
使用開始Turn：
Target：
Range：
Plane：
必要Lab：
敵Counter：
停止条件：
```

## 目的を具体化する

悪い例：

```text
強いSummonを使う
```

良い例：

```text
N2 Mageを召喚し、
Poison ResistanceとNature Boosterを国家へ追加する
```

```text
敵Border FortへRemote attackを三Turn連続し、
PatrolとGemを後方へ拘束する
```

---

# Summonの分類

## 兵を召喚する

GoldではなくGemをArmyへ変換します。

評価するものは、

```text
Gem cost
Unit数
HP・Protection・MR
Leadership
Supply
Upkeep
Siege
Damage type
召喚Caster turn
```

です。

## Commanderを召喚する

Commander不足、Leadership、Scout、Priest等を補います。

## Mageを召喚する

最も重要な召喚の一つです。

Mage summonは、

```text
Gem
→ 新Path
→ Booster
→ さらに上位Summon
→ Global・Forge・Battle Magic
```

というAccess chainを開きます。

## Unique summon

Unique Unitは世界に一体だけ等の制約を持つ場合があります。

競争相手、既存状態、死亡後の再召喚可否を確認します。

## Random / Candidate pool

召喚結果が複数候補から決まる場合、欲しいPathを必ず得るとは限りません。

```text
期待値
≠
保証
```

です。

---

# Summon Mageの価値

Mageを召喚するときは、そのMage本人のPathだけでなく、次を見るべきです。

```text
ForgeできるBooster：
次にCastできるSummon：
Site Search：
Global：
Remote Ritual：
Battlefield spell：
Priest level：
Leadership：
```

## Pathを一段開く

Native 0のPathを1得るだけで、

- Site Search
- Low-level Booster
- Crosspath Item
- Resistance
- Summon chain

が開く場合があります。

## 高Pathだけを求めない

高PathMageでも、

- Gem incomeがない
- BoosterをForgeできない
- Spell Researchが遠い
- Uniqueで失えない
- 戦場へ出せない

なら、国家へすぐ貢献しません。

---

# Access chain

## Strategic AccessとBattle Access

Communion・SabbathのPath上昇はBattle中です。

```text
CommunionでS5
≠
S5 RitualをLabでCastできる
```

です。

Ritual・Forgeには、

- Native Path
- Booster
- Summon Mage
- Pretender
- Hero
- Empowerment

を使います。

## Chainを書き出す

```text
Native Mage：
→ Booster A
→ Booster B
→ Summon Mage
→ 新MageがBooster C
→ Global
```

と書きます。

## Single point of failure

Chainが一人のRare Mageへ依存する場合、

- Assassination
- Disease
- Raid
- Lab喪失
- Arena
- Battle死亡

で国家計画が止まります。

可能なら複数Caster、複数Lab、予備Boosterを用意します。

---

# Global Enchantment

Globalは世界全体へ継続効果を与え、限られた共有Slotを使います。

## Cast前の確認

```text
効果：
自国が得る利益：
敵国が得る利益：
維持条件：
Caster：
追加Gem：
Dispel対策：
敵がSlotを埋めた場合：
```

## Overcast

最低CostよりGemを多く投入することで、Global競争やDispel耐性へ影響する場合があります。

しかし、

```text
多く投入した
＝ 絶対安全
```

ではありません。

敵Gem、Caster、協力国、Unique effectを考えます。

## Timing

早いGlobalは長く利益を得ますが、

- Gem備蓄が減る
- First war用Gemがなくなる
- 敵全員に脅威を知らせる
- Dispel標的になる

Riskがあります。

## Global casterの保護

Global casterは、

- Booster
- Gem
- Unique Item
- 高Path
- Ritual turn

を集中させています。

Capitalだけへ全員を集めず、Fort、Bodyguard、Patrol、Anti-remoteを使います。

---

# Dispel

敵Globalを放置すると、毎Turn差が広がる場合があります。

Dispel判断は、

```text
敵Globalが一Turnに生む価値
× 残りTurn
```

と、

```text
Dispel Gem
＋ Caster turn
＋ 失敗Risk
```

を比較します。

## 外交

Globalは複数国へ影響します。

一国で全Costを負担せず、

- Gem共同出資
- Caster提供
- Dispel Timing
- Global後のSlot

を交渉できます。

---

# Remote attack

Remote attackは、通常Armyを送らず遠方Provinceへ圧力をかけます。

## 目的

- Mageを殺す
- Commanderを削る
- PDを試す
- Unrestを上げる
- Lab・Templeを脅かす
- Gemを防衛へ使わせる
- Scout情報を得る
- Fort reliefを遅らせる

## Intel

Target前に、

```text
Province Defence：
Fort：
Mage：
Resistance：
Dominion：
Terrain：
Retreat：
Anti-remote：
```

を確認します。

## MessageとReplay

Remote attackはMessage・Battle Replay・Eventを生成する場合があります。

結果から、

- 敵Mage
- Resistance
- PD
- Patrol
- Counter
- 再攻撃価値

を読みます。

## 同じTargetへ繰り返さない

敵は一回目の後に、

- Resistance
- Patrol
- Mage
- Gem
- Fort
- Decoy

を用意します。

第二Targetや別Damage typeへ切り替えます。

---

# Remote summon・Army insertion

遠方へUnitを召喚するRitualは、

- Raid
- Retreat route切断
- Siege reinforcement
- Throne contest
- Scout

へ使えます。

ただし、

- Leadership
- Supply
- Retreat
- Target ownership
- Battle Timing

を確認します。

召喚された兵だけが孤立し、次Turnに全滅するならGem効率が悪い場合があります。

---

# Terrain・Province操作

Ritualには、

- Terrain変更
- Fort・Lab
- Weather
- Dominion
- Population
- Income
- Site

へ影響するものがあります。

効果がBattleに直結しなくても、

```text
移動Cost
Recruit
Supply
Site Search
Fort network
Retreat route
```

を変える場合があります。

Dom6ではBattlefield Terrainや複数Planeもあるため、Target条件を旧作知識だけで判断しません。

---

# Monthly Ritual

## 利点

- 操作量を減らす
- 同じSummonを継続生産する
- Site Searchを繰り返す
- Gemを毎TurnArmyへ変換する

## 停止原因

- Gem不足
- Boosterを外した
- Lab喪失
- Target無効
- Range外
- Plane条件
- Unique既存
- 別Orderで上書き
- Caster死亡・Disease

Monthly orderが止まったらMessageとCommander Orderを確認します。

## 予算

Monthly orderを複数設定すると、気付かないうちにGemが枯れます。

```text
開始Gem：
月間Income：
月間固定消費：
First war reserve：
Global reserve：
残余：
```

を管理します。

---

# Magic Phaseと通常Movement

Ritual、Teleport、Remote attack等はMagic Phaseで処理される場合があります。

```text
Magic Phase Battle
→ 通常Movement
→ 通常Field Battle
```

となるため、

> Remote attackと徒歩Armyを同じProvinceへ送った

だけでは同じBattleになるとは限りません。

先発部隊が単独でも役割を果たす設計にします。

詳細は[ターン処理順](../reference/turn-resolution.md)を参照してください。

---

# Gem budget

Gemは用途別に分けます。

```text
Battle reserve
Summon
Booster
Global
Remote attack
Emergency
Dispel
```

一つの大召喚へ全Gemを使うと、First warのBattle Magicが止まります。

## GemをArmyへ変換する時期

早い召喚は長く働きますが、Research・Accessが不足しやすいです。

遅い召喚は効率が高くても、勝敗が決まった後になる場合があります。

```text
召喚完成Turn
→ 前線到着Turn
→ 最初に働くBattle
```

まで計算します。

---

# LA Bogarusでの例

Bogarusは、

- Fire
- Air
- Earth
- Astral
- Death
- Blood
- Holy

を複数Mageへ分散して持ちます。

強みは一人の万能Mageではなく、

```text
研究者を大量生産
→ Breakpointへ早く到達
→ Path別Mageを分類
→ Communion / Sabbath
→ Summon・Global・Remoteへ分岐
```

できることです。

一方、

- 水・Nature・Glamourが不足
- Mageが脆い
- Goldを大量に使う
- BattleとRitualでMage turnが競合

します。

詳しくは[LA Bogarus — Age of Heroes](../nations/la/bogarus.md)を参照してください。

---

# Casterの安全

## Fort

高PathMageをFort内へ置きます。

## Patrol

Assassin・Spy・Stealth Raiderを検出します。

## Bodyguard

Assassinationへ備えます。

## 分散

全BoosterとGemを一人へ集中しません。

## Decoy

敵Remote attackが重要Casterへ集中しないよう、LabとMageを複数拠点へ分けます。

## Disease・Old Age

長期Ritual casterはDisease・Old Ageも確認します。

---

# Counter戦略

## 敵がSummon Armyを増やす

Damage type、MR、Mindless、Undead、Magic Beingを確認します。

## 敵がGlobalを展開

Dispel、外交、Caster assassination、Slot競争を検討します。

## 敵がRemote attack

- Patrol
- Resistance
- Decoy
- Fort
- Anti-remote effect
- Target分散

を使います。

## 敵がAccess chainを作る

Booster holder、Rare Mage、Summon MageをScout・Assassin・Raidで狙います。

---

# Battle ReplayとMessage

戦略魔法はReplayだけでなくMessageも正本です。

```text
Cast成功：
Target：
消費Gem：
召喚数：
Battle：
生存：
敵Counter：
Monthly継続：
```

を記録します。

---

# よくある失敗

## 1. Researchしただけで使えると思う

Access、Gem、Lab、Targetが必要です。

## 2. Communion PathでRitualをCastしようとする

Battle AccessとStrategic Accessは別です。

## 3. Summon Mageの次の仕事がない

新Pathから何を開くか決めます。

## 4. Globalへ全Gemを入れる

Battle reserveとDispel reserveを残します。

## 5. Monthly orderを忘れる

Gemが枯れるまで継続します。

## 6. Casterを一拠点へ集中

Raid・Assassination・Remote attackで国家Engineごと失います。

## 7. Remote attackを同じTargetへ繰り返す

敵Counter後はTarget・Damageを変えます。

## 8. Summon完成Turnだけを見る

前線到着Turnまで計算します。

---

# Test checklist

```text
[ ] Ritualの目的を一文で書いた
[ ] CasterとBooster routeを確認した
[ ] CommunionをStrategic Accessへ数えていない
[ ] 一回Costと月間Costを分けた
[ ] Battle reserveを残した
[ ] Globalの敵利益も確認した
[ ] Dispel・Overcast・外交を考えた
[ ] Remote TargetのPD・ResistanceをScoutした
[ ] Magic Phaseと通常Movementを分けた
[ ] CasterをFort・Patrol・Bodyguardで守った
[ ] Summonの前線到着Turnを計算した
[ ] Monthly order停止条件を確認した
```

---

# 関連ページ

- [LA Bogarus — Age of Heroes](../nations/la/bogarus.md)
- [Research](research.md)
- [Gem](gems.md)
- [Magic Boosting](boosting.md)
- [Communion](communions.md)
- [Site Search](site-search.md)
- [Turn resolution](../reference/turn-resolution.md)
- [Forts](../systems/forts.md)
- [Spellデータ](../data/spells/index.md)
