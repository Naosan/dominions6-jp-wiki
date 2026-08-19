---
title: Research Item
status: expanding
verified_version: "6.35"
last_verified: "2026-08-19"
---

# Research Item

Research Itemは、装備中のCommanderへResearch bonusを与えるMagic Itemです。

重要なのは「Research bonusが大きいか」だけではありません。

> **Construction研究 + Gem + Forge turn + Carrier + Slot**
> を先払いして、将来のResearchを買う投資です。

現行6.35の全Research Itemと正確な要求Path・Construction・効果は[自動生成Research Item一覧](../data/items/research.md)と[Dom6 Mod Inspector](https://larzm42.github.io/dom6inspector/)で確認してください。このページでは、いつ作るか、どのItemを選ぶか、どこで投資を止めるかを扱います。

---

# Research Itemの価値

Research Itemは次の変換を行います。

```text
Gem + Forge turn
→ 毎TurnのResearch
→ 早いBreakpoint
→ 戦争Timing・Global先着・Legendary Spell
```

作った瞬間にはArmyが強くなりません。価値が出るのは、そのItemが将来の重要な研究到達を実際に早めたときです。

例えば研究到達が1Turn早まった結果、

- 最初の大規模Battle Spellを先に使える
- Counter spellが開戦前に間に合う
- Globalへ先着する
- Constructionの次段階へ早く届く
- Summonから新しいMagic accessを得る

なら、単純なRP以上の価値があります。

---

# まず6.35の代表Itemを区別する

Research Itemは同じ「RP増加Item」ではありません。要求Path、解禁Construction、追加効果、制約が異なります。

| Item | Construction | Forge Req | Research | 重要な追加条件・性質 |
|---|---:|---|---:|---|
| Owl Quill | 3 | A1 | +6 | 早期に作りやすい基本型 |
| Imp Familiar | 3 | B1 | +3 | Cursed、Tainted、No Forge Bonus、Retinueあり |
| Skull Mentor | 5 | D2 | +14 | Research特化。6.35データ上、Curse / Disease / Taintedを持たない |
| Homunculus | 5 | N2 | +11 | Cursed、Retinueあり |
| Dreamstone | 5 | G1 | +9 | MR -2、Glamour Mage限定、non-sleeper不可 |
| Lightless Lantern | 7 | F1 | +12 | Darkvision 100、Tainted |

この表は代表的なGeneric Itemです。国家限定ItemやArtifactにもResearch bonusを持つものがあります。正確な全件は生成一覧を使ってください。

!!! warning "古い攻略の副作用を引き継がない"
    `Skull Mentor`を「Horror / Disease / Curse持ち」と説明する古い知識を6.35へそのまま持ち込まないでください。固定Dom6 InspectorデータではResearch +14のItemで、これらのFlagはありません。一方、`Lightless Lantern`はTainted、`Dreamstone`はMR低下と装備者制限を持ちます。Itemごとに確認します。

---

# 回収Turn

最初に見るのは**ForgeしたMageの一Turn**です。

概念的には、

```text
Forge-turn回収
≈ ForgeしたMageがそのTurn失ったResearch
  ÷ ItemのResearch bonus
```

です。

例えばResearch 10のMageがOwl QuillをForgeすると、そのTurnに失った10 RPだけならResearch +6で約2Turn分です。

しかし本当の投資にはさらに、

- Item解禁のためConstructionへ振ったResearch
- Gem
- Forge Bonusを用意した投資
- Item slot
- Carrierを研究へ固定する機会費用
- 戦争用Gemを使わない機会費用

があります。

そのため、単純に「+14は+6より強い」ではなく、**今あるPathとConstructionから何Turnで量産を開始できるか**で比較します。

---

# Construction breakpointで考える

## Construction 3

Owl Quillのような早期Research Itemへ入れます。

向いているのは、

- A1等の安いForge accessが既にある
- 対応Gemが余る
- 最初の軍事Researchを壊さずC3へ寄れる
- まだゲーム残りTurnが長い

場合です。

C3は「研究経済を今から作るか」を決める早い分岐です。

## Construction 5

Research Itemの選択肢が増えます。Skull Mentor、Homunculus、DreamstoneのようにPath別に性格が変わります。

ここでは、

```text
高Bonusを一個作る
vs
安いItemを多数作る
vs
Booster / Thug装備 / ResistanceへGemを残す
```

を比較します。

特にSkull MentorはResearch +14なので強力ですが、D2 casterのForge turnとDeath Gemを使います。Death GemがSummonや戦争Ritualのボトルネックなら、Research bonusだけでは決まりません。

## Construction 7

Lightless LanternがResearch +12を提供しますが、C7まで来る時点ではゲーム時間が進んでいます。

したがって問題は「強いResearch Itemか」ではなく、

> **これから何Turn研究を続けるか**

です。

C7到達後すぐ大戦争へ入りMageを前線へ出すなら、大量生産してもCarrierが研究しません。

---

# Item別の実戦判断

## Owl Quill

A1・Construction 3・Research +6という早い入口です。

強みは絶対値より**早く量産サイクルへ入れること**です。Air Gemを戦闘で大量消費する予定が薄く、A1 Mageが後方に余るなら研究経済へ変換しやすくなります。

Counterは自分の研究計画そのものです。数Turn後にAir系Battle SpellやAir BoosterへGemが必要なら、Quillを作りすぎないようにします。

## Skull Mentor

D2・Construction 5・Research +14。

Research bonusが大きく、6.35ではSkull Mentor自体にCurse / Disease / Taintedはありません。したがって「危険な研究ItemだからOld Age Mageに押し付ける」という判断は不要です。

本当のCostはDeath GemとD2 Forge turnです。Death GemをSummon、Booster、Remote attackへ回す戦略なら、その競合を評価します。

## Homunculus

N2・Construction 5・Research +11で、CursedかつRetinueを伴います。

単純なRP効率だけでなく、Nature GemをPoison対策、Regeneration、Nature summonへ使う予定との競合を見ます。

## Dreamstone

G1・Construction 5・Research +9。

MR -2に加え、Glamour Mageであること、non-sleeperではないことという装備条件があります。安いGlamour researcherへ自然に載る国家では便利ですが、貴重なGlamour casterしかいない国家ではForge / Ritual / battlefield dutyと競合します。

## Lightless Lantern

F1・Construction 7・Research +12で、Taintedです。

高Construction到達後なので、**残り研究期間**が特に重要です。Fire Gemを戦闘魔法やElemental、Artifact競争へ使う予定も確認します。

Taintedの実際のリスクはゲーム内Item詳細で確認し、単に「Horror / Disease / Curse全部がある」と一括りにしません。

## Imp Familiar

B1・Construction 3・Research +3。

Research bonusは小さい一方、Cursed、Tainted、No Forge Bonus、Retinueという複数の性質があります。Blood SlaveはGemとは経済構造が違うため、Blood economyが既に回っている国家とそうでない国家で価値が大きく変わります。

---

# Carrierの選び方

## Cheap Researcher

基本候補です。Itemを持つことで、Gold / Commander PointあたりのResearchを増やせます。

## Rare Path Mage

Research Itemを持たせても、そのMageがForge / Ritual / Site Searchへ出続けるならItemのRPは発生しません。

「装備できるMage」ではなく、**実際にResearch orderを長期間続けるMage**へ渡します。

## Old Age Mage

Old Age自体と、Item固有のCursed / Tainted / MR penalty等を混同しないようにします。Skull Mentorのように副作用を持たないResearch Itemまで危険物扱いしないことが重要です。

## 前線Battle Mage

研究Itemを装備したまま前線へ出すと、

- そのTurnはResearch bonusを使わない
- 戦闘用Slotが一つ埋まる
- Carrier死亡時にItemを失う可能性がある

ため、出征前にF8のMagic item overview等で装備を確認し、後方研究者へ回せるものは回します。

---

# 大量生産の基盤

## Forge Bonus

Item一個あたりの実コストを下げ、回収を早めます。

ただし生成データの`Gem`欄はForge Bonus・国家割引を入れる前の基礎Costです。最終コストはゲーム内Forge画面を優先してください。

## Forge discount Item

Dwarven Hammer等を先に用意する場合、そのHammer自身のGemとForge turnも投資です。

Research Itemを大量生産するなら回収しやすく、数個しか作らないなら先行投資が重くなることがあります。

## Gem / Slave income

対応資源をResearchへ変換しすぎると、

- Battlefield spell
- Booster
- Summon
- Resistance Item
- Thug / SC装備

が止まります。

Research Item予算を独立して決めます。

## Safe research hub

研究Itemは前線から離れたLabへ集めるのが基本です。ただし一箇所へ過度に集中するとRaidやRemote attack一回の損失が大きくなります。

---

# Research ItemとFort

Research Itemを増やしても、装備してResearchするCommanderがいなければ意味がありません。

Fortを増やすと、

- Mage recruitment
- Commander Point
- Laboratory
- Safe research space
- Item carrier数

が増えます。

したがってResearch economyは、

```text
Researcher生産能力
× 一人あたりResearch
× 実際に研究するTurn数
```

で考えます。

---

# Timingによる価値

## Early game

C3 Research Itemをすぐ解禁でき、最初の戦争を遅らせないなら価値があります。

ただし軍事Breakpointを一つ落としてまでConstructionへ寄ると、研究加速Itemを作る前に戦争で損をします。

## Mid game

最初の軍事Breakpoint後にC5へ進み、Research ItemとBooster・Resistance・Thug装備を同時に選ぶ時期です。

ここでは「研究をさらに加速するか」「今の研究成果をItemで戦力化するか」が中心判断になります。

## Late game

Legendary SpellやGlobal競争へ向けて価値が残る場合があります。

一方、ゲーム終了が近いならResearch Itemの回収期間がありません。即時にArmyを強くするItem、Summon、Battle Gemへ資源を戻します。

---

# Counter：敵のResearch Item経済を見る

敵が大量のResearch Itemを作っているなら、それは「研究が速い」だけでなく、

- Forge turnを後方へ使っている
- 特定Gem / Slaveを研究へ変換している
- Item carrierがLabへ集中している
- Constructionへ研究を振っている

という情報です。

そのため、

- 早い戦争Timingを作る
- Research hubをRaidする
- Remote attack / Assassinで高価なCarrierへ圧力をかける
- 相手がResearchへ使ったGemと競合するPathで戦争を強制する

といったCounterが成立します。

Research Item経済は時間を味方につける投資なので、**相手へ時間を与えないこと**が最も直接的なCounterです。

---

# よくある失敗

## Constructionへ直行する

Item解禁前に最初の戦争へ負けます。

## BonusだけでItemを順位付けする

+14が+6より常に優れるわけではありません。解禁時期、要求Path、資源、Forge turnが違います。

## 古い副作用情報を使う

Skull Mentor、Lightless Lantern等の性質を旧作や古いWikiから流用せず、6.35 Inspectorを確認します。

## 全資源をResearchへ変換する

研究は進んでも、その研究成果を使うGem・Slaveが残りません。

## 前線へResearch Itemを持ち出す

研究していないTurnにはResearch bonusを使いません。戦闘用Slotも失います。

## Late gameに大量生産する

回収前にゲームが終わります。

## Forge turnを無料だと思う

ForgeしたMageはそのTurn研究していません。

---

# 生産計画テンプレート

```text
次の研究目標：
そのBreakpointの価値：
現在の毎Turn Research：
Item解禁までのResearch：
候補Item：
Item一個のResearch bonus：
要求Path：
基礎Cost：
実際のForge Cost：
Forge担当MageのResearch：
月産数：
Battle / Summon用の資源予算：
安全なCarrier数：
Itemを使う予定Turn数：
```

---

## 関連ページ

- [Magic Item](index.md)
- [Forge計画とConstruction breakpoint](forge-planning.md)
- [Research](../magic/research.md)
- [Gem](../magic/gems.md)
- [Booster](boosters.md)
- [自動生成Research Item一覧](../data/items/research.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
