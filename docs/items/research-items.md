---
title: Research Item
status: expanding
verified_version: "6.35"
last_verified: "2026-08-14"
---

# Research Item

Research Itemは、Mage一人の毎Turn Researchを増やす装備です。

Owl Quill、Skull Mentor、Lightless Lantern等が代表例ですが、Construction level、要求Path、Research bonus、副作用は現行ゲームデータを確認してください。

重要なのは「Research bonusが大きいか」ではなく、**作成に使った研究・Gem・Forge turnを何Turnで回収できるか**です。

---

# Research Itemの価値

Research Itemは次の変換を行います。

```text
Gem + Forge turn
→ 毎TurnのResearch
→ 早いBreakpoint
→ 戦争Timing・Global先着・Legendary Spell
```

作った瞬間にはArmyが強くなりません。将来の研究到達Turnを早めます。

---

# 回収Turn

概念的には次で考えます。

```text
回収Turn
≈
（Item解禁までの追加研究 + ForgeしたMageが失う研究 + Gem価値）
÷ Itemの毎Turn Research bonus
```

厳密な共通換算はありませんが、比較には使えます。

## 例

- Research +6 Item
- ForgeしたMageのResearch 10
- Forgeに一Turn

なら、まず失った10 Researchを約2Turnで回収します。

しかし実際には、Item解禁へ寄り道したSchool、Gem、Carrier死亡Riskもあります。

---

# 作るべき時期

## 作りやすい状況

- 国境が安定している
- 最初の軍事Breakpointへ到達済み
- Forge Bonusがある
- 対応Gem incomeが多い
- Cheap researcherが多い
- ゲームが長く続く
- 次の大研究目標まで距離がある

## 作りにくい状況

- 数Turn以内に戦争
- Battle Spellが不足
- Gemを戦争で使う
- 前線Fortしかない
- Researcherが少ない
- Game終了が近い

「研究加速Itemを作れば研究が速い」は正しいですが、**作るために戦争Spellが遅れて敗北する**なら失敗です。

---

# 代表的なResearch Itemの役割

!!! note
    以下は役割の分類です。数値・Construction level・Pathはゲーム内またはMod Inspectorで確認してください。

## Owl Quill型

- 低～中Construction
- Air access
- 比較的早く作れる
- 一個あたりのResearch bonusは中程度

Air Gemが余り、A1 Forge accessがある国家でResearch economyを始めやすくなります。

## Skull Mentor型

- Death access
- 高いResearch bonus
- Horror / Disease / Curse等の副作用を持つ場合がある

Carrier選びと使用期間を考えます。Old Age Mageへ副作用Itemを集中させると研究者を失います。

## Lightless Lantern型

- Fire access
- 高いResearch bonus
- Horror関連Risk
- 中～高Construction

Fire Mageを量産でき、Forge Bonusを持つ国家で大量生産しやすい一方、解禁が遅い場合があります。

## Artifact / Unique Research Item

非常に高いResearchや特殊能力を持ちますが、一つしか存在せず、Carrier死亡Riskが高いです。

---

# Carrierの選び方

## Cheap Researcher

基本候補です。Itemを持つことで、Gold / Commander PointあたりのResearchが増えます。

## Mundane Researcher

Magic / Drainの影響やItem相性が国家固有で異なります。研究値計算を確認します。

## Rare Path Mage

Research Itemを持たせるよりForge / Ritualへ使う方が価値が高い場合があります。

## Old Age Mage

副作用Item、Disease、Horror、老齢を重ねると損失が増えます。

## 前線Battle Mage

研究Itemを装備したまま前線へ出すと、

- Itemを失う
- Resistance Slotが足りない
- Battle Scriptに不要

となります。Labへ戻すか後方研究者へ渡します。

---

# 大量生産の基盤

## Forge Bonus

Item一個あたりのGem costを下げ、回収Turnを短くします。

## Forge discount Item

Dwarven Hammer等のdiscount Itemを何個作るか計算します。

Research Itemを20個作る計画なら価値が高く、3個だけならHammer作成Costを回収できない場合があります。

## Gem Site

対応Gem incomeが少ない場合、Research Itemを作りすぎるとBattle Magic、Booster、Summonが止まります。

## Safe Fort

研究Itemは前線から離れたFortへ集めます。

- Fort
- Lab
- 防衛Army
- Raid警戒
- Retreat route

を用意します。

---

# Research ItemとFort

Fortを一つ増やすと、

- Mage recruitment
- Commander Point
- Laboratory
- Safe research space
- Item carrier数

が増えます。

Research Itemだけ増やしてResearcherが足りない場合、先にFortを増やす方がよいことがあります。

---

# Research ItemとScales

Magic / Drain、Order / Turmoil、Gold income、Growth等がResearcher数と効率へ影響します。

Research ItemはScalesの代替ではなく、国家経済の上に積む追加投資です。

---

# Timingによる価値

## Early game

低級Research Itemがすぐ解禁でき、最初の戦争を遅らせないなら有効です。

## Mid game

最初のBreakpoint後、Constructionへ進み、中盤～終盤研究を加速する代表時期です。

## Late game

Legendary Spell、Global、High summon競争に価値があります。

ただし残りTurnが少ない場合、Itemより即時Battle Spell・SummonへGemを使います。

---

# 研究加速の代替

Research Itemだけが方法ではありません。

- Fortを増やす
- Cheap Mageを追加
- Research bonus Site
- Magic Scale
- National ability
- Summoned researcher
- Enemy research Fortの奪取
- Battle Mageを研究へ戻す
- 不要なForge / Ritualを止める

最も安い方法を選びます。

---

# よくある失敗

## Constructionへ直行

Item解禁前に最初の戦争へ負けます。

## 全Gemを研究へ変換

Battlefield spell、Resistance、Boosterが不足します。

## 前線へItemを置く

Raid一回で研究経済を失います。

## Carrier副作用を見ない

Horror、Disease、Curse、Aging等で研究者が死亡します。

## Late gameに大量生産

回収前にゲームが終わります。

## Forge turnを無料だと思う

ForgeしたMageはそのTurn研究していません。

---

# 生産計画テンプレート

```text
研究目標：
必要Research：
現在の毎Turn Research：
Item解禁まで：
Item一個のBonus：
一個のGem cost：
Forge Bonus：
月産数：
Battle用Gem予算：
安全なCarrier数：
回収予定Turn：
```

---

## 関連ページ

- [Magic Item](index.md)
- [Research](../magic/research.md)
- [Gem](../magic/gems.md)
- [Booster](boosters.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
