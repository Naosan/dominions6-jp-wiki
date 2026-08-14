---
title: Scales
status: expanding
verified_version: "6.35"
last_verified: "2026-08-14"
---

# Scales

ScalesはPretender designで設定し、自国Dominionを通じてProvinceへ広がる国家環境です。

Scalesは「余ったDesign Pointを入れる場所」ではありません。

- Gold
- Resources
- Population
- Supply
- Research
- Magic Resistance
- Random Event
- Temperature
- 国家固有能力

を毎Turn変える長期投資です。

---

# 六つのScale軸

- Order / Turmoil
- Productivity / Sloth
- Heat / Cold
- Growth / Death
- Luck / Misfortune
- Magic / Drain

Dom6では国家・Pretenderによって通常範囲を超えるExtreme Scaleを選べる場合があり、追加効果が発生します。

---

# Order / Turmoil

## Order

主な価値：

- 安定Income
- Unrest抑制
- Mage / Fort economy
- Blood Hunt後の回復補助

### 向く国家

- Gold-heavy Mage
- 高Upkeep Army
- Fortを多く建てる
- Random Eventへ依存しない

## Turmoil

主な価値：

- Design Point
- Event frequency
- 一部国家のFreespawn / Chaos能力
- Luckとの組み合わせ

### 向く国家

- TurmoilからUnit・Gem・Eventを得る
- Gold依存が低い
- Summon / Blood中心
- Luckが高い

### Risk

- Income低下
- Unrest
- Fort / Mage生産の遅れ

OrderとLuck、TurmoilとMisfortuneを個別に見ず、Event economy全体で評価します。

---

# Productivity / Sloth

## Productivity

主な価値：

- Resources
- 重装兵・Cavalry・Giantの生産
- Supply / Incomeへの補助

### 最重要になりやすい国家

- Resource costが高い
- Capitalで複数Expansion Armyを作る
- Fort Resource bonusを持つ
- Armorが国家の強み

## Sloth

主な価値：

- Design Point

### 許容しやすい国家

- Low-resource Sacred
- Light infantry / Archer
- Summon Army
- Mage中心
- Capital-only兵を少数だけ使う

### Risk

Goldがあっても兵士を雇えません。Recruit画面でGoldとResourcesのどちらが余るかTestします。

---

# Heat / Cold

国家にはPreferred Temperatureがあります。

そこから外れるとIncome・Supply等へPenaltyを受けます。

## 設計時の問い

- 国家のPreferred Temperatureは何か
- Heat / Cold Auraを使うか
- Cold Blooded Unitが多いか
- Fire / Water battle planと合うか
- Enemy DominionへTemperatureを押し付けたいか
- Seasonal変化へ耐えられるか

TemperatureはDesign Point源として選びやすい一方、長期Incomeへ毎Turn影響します。

---

# Growth / Death

## Growth

主な価値：

- Population増加
- 長期Income
- Supply
- Blood Hunt基盤
- 老齢・Diseaseへの間接耐性

### 向く国家

- 長期戦
- Blood
- Gold-heavy
- High Population map
- Living Mageが多い

## Death

主な価値：

- Design Point
- 一部Undead / Death国家能力

### Risk

- Population減少
- Income低下
- Supply低下
- Blood economy悪化
- 長期Gameで累積損失

Death Scaleは序盤の表示Incomeだけでなく、Turn 30～60のPopulationを考えます。

---

# Luck / Misfortune

## Luck

主な価値：

- 良いRandom Event
- Gem / Gold / Hero等の期待
- TurmoilとのEvent頻度相乗

## Misfortune

主な価値：

- Design Point

### Risk

- Gold loss
- Unrest
- Disease / Commander loss
- Province damage
- Bad event chain

### 評価

Randomなので一Gameの結果だけで判断しません。

国家固有Event、Turmoil、Order、Fort数、Misfortune耐性を見ます。

---

# Magic / Drain

## Magic

主な価値：

- Research
- Spell Fatigue
- Magic environment

### 向く国家

- Mage数が多い
- Cheap researcher
- Early research breakpoint
- Communion
- 高Fatigue Spell

## Drain

主な価値：

- Design Point
- MR等への影響
- 一部国家・Mundane Researcherとの相性

### 許容しやすい国家

- Mundane Researcher
- Research bonus Unit
- Early兵士Rush
- Mage数が少ない

### Risk

- Research遅延
- Battle MageのFatigue
- Pretender / Independent Mageの研究低下

国家Mageだけでなく、PretenderとIndie MageがDrainの影響を受けるか確認します。

---

# Scale優先順位

国家を次の制約で分類します。

## Gold-constrained

優先：Order、Growth

例：高価なMage、Fort、多Upkeep Army。

## Resource-constrained

優先：Productivity

例：重装歩兵、Cavalry、Giant armor。

## Research-constrained

優先：Magic、Order / GrowthでMage数増加

## Sacred-constrained

ScalesよりBless / DominionへPointを回す場合があります。

## Short-game rush

Growthの長期価値が低く、Awake / Bless / Productionを優先する場合があります。

## Blood scaling

Growth、Order、Population、防衛可能な後方を重視します。

## Summon-heavy

Gold / Resource依存が低く、Magic・Luck・Gem economyを重視する場合があります。

---

# ScalesとAwake状態

## Awake

Design Pointが少なくなるため、Scalesを削りやすくなります。

Expanderが取る追加Provinceと、弱いScalesの長期損失を比較します。

## Dormant

ScalesとPretender利用時期の中間です。

## Imprisoned

強Scales・Heavy Blessを取りやすい一方、Pretender / Incarnate Bless / Boosterが遅れます。

---

# Scalesの回収

Scalesの価値は毎Turn・全Provinceへ累積します。

概念的には、

```text
Scales value
≈
一Provinceあたりの毎Turn差
× 自国Dominion下のProvince数
× 残りTurn
```

Early ExpansionでProvince数が多い国家ほどStrong Scalesの回収も大きくなります。

逆に領土が狭いままならScales投資を活かせません。

---

# Enemy DominionとScales

自国Scaleは自国Dominionが届いて初めて機能します。

- Border Province
- Enemy Temple周辺
- Newly conquered land
- Plane entrance

ではEnemy / Neutral Scaleが残ります。

TempleとPreachへGold / Priest turnを使うCostもScales設計に含まれます。

---

# Extreme Scales

Dom6では特定国家・Pretenderが通常範囲を超えたScaleを持てます。

Extreme Scaleは単なる数値延長ではなく、追加の戦略効果を持つ場合があります。

国家攻略では、

- 何が発生するか
- Friendly / Enemy Provinceへどう作用するか
- Pretender Dominionが必要か
- 他Scaleとの組み合わせ

を独立して記述します。

---

# Scale designの手順

## 1. Unit生産Test

Capitalで主力兵を何体雇えるか確認します。

## 2. Mage生産Test

毎TurnMageを雇えるIncomeを確保します。

## 3. Fort timing

第二Fort資金が何Turnに貯まるか確認します。

## 4. Research timing

最初のBreakpointへ何Turnで届くか確認します。

## 5. Population horizon

Turn 30以降のGrowth / Death差を考えます。

## 6. Dominion

Scaleが前線へ届くDominion strengthとTemple計画を確認します。

---

# よくある失敗

## 全Scaleを平均化

国家の主要制約を解決できません。

## Productivityを見ず重装国家

Goldが余りExpansion Armyが完成しません。

## Growthを無料だと思う

短期Gameでは回収前に終わる場合があります。

## Deathを序盤Incomeだけで判断

Population減少が累積します。

## Drainを国家Mageだけで判断

Pretender、Indie、Summon Mageが遅れます。

## Luckを一GameのEventで評価

確率なので複数Testが必要です。

## Scalesは強いがExpansionできない

領土が少なく投資を回収できません。

## Dominionが低くScaleが広がらない

Temple costを含めるとDesign Point節約になっていません。

---

# Scales記録テンプレート

```text
Nation / Age：
Game length想定：
主なGold cost：
主なResource cost：
Mage cost / CP：
Sacred依存：
Blood：
Order / Turmoil：
Productivity / Sloth：
Heat / Cold：
Growth / Death：
Luck / Misfortune：
Magic / Drain：
Dominion：
第二Fort予定Turn：
最初のResearch到達Turn：
交換した役割：Awake / Bless / Magic diversity
```

---

## 関連ページ

- [Pretender God](index.md)
- [Bless](bless.md)
- [Dominion](../systems/dominion.md)
- [Province](../systems/province.md)
- [Research](../magic/research.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
