---
title: "Lightless Lantern"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 399
---

# Lightless Lantern

**Research Bonus +12を一人のMageへ与える代わりに、BearerをVeilの向こうのHorrorsへ露出させ得るConstruction 7の高出力Research Item。**

Lightless Lanternは、Owl Quillより数字が大きいResearch装備というだけではありません。攻略上は、**遅いResearch解禁、高い一枠出力、Horror-related risk、Carrier価値をまとめて管理するItem**として評価します。

- [Dominions 6.35固定データ — Item 399](../../data/items/by-id/399.md)
- [Magic Item攻略辞典](index.md)
- [Owl Quill](owl-quill.md)
- [Research Item](../research-items.md)

---

# まず何ができるか

6.35固定データでは、Lightless LanternはConstruction 7、Forge要求**F1**のMiscellaneous Itemで、装備者へ、

- **Research Bonus +12**
- **Darkvision 100**

を与えます。

Item descriptionでは、hidden lightが魔法研究の秘密を明らかにする一方、そのdark lightがBearerをVeilの向こうに潜むHorrorsへ見つけさせる可能性があると説明されています。

このためItemの中心は、

```text
高いResearch収入
と
Horror-related risk
```

の交換です。

Darkvisionは付随機能ですが、通常の後方Research運用では使わないことも多くあります。

---

# +12は毎Turn積み上がる収入

Lightless Lanternを装備したMageが研究を続ける限り、Research Bonus +12は毎Turn積み上がります。

価値は、

```text
一Turnの+12
×
安全にResearchできたTurn数
```

で増えます。

したがって、

- 研究終了まで何Turn残っているか
- CarrierがResearch以外へ動員されないか
- LabがRaidされないか
- Lanternを失わず使い続けられるか
- Horror-related riskでCarrier運用が中断しないか

が重要です。

一、二Turnだけ装備して前線へ出るMageでは、高出力を回収する前に運用が終わります。

---

# Construction 7到達後というTiming

Lightless LanternはConstruction 7 Itemです。

つまり使い始める前に、

- Construction 7までResearchする
- F1 MageのForge turnを使う
- Fire Gemを支払う
- ItemをResearcherへ配送する

必要があります。

すでにゲーム終盤で主要研究が終わりかけている場合、+12を回収できるTurnが足りません。

逆に、C7到達後にも、

- High-level Battlefield magic
- Ritual
- Artifact access
- 複数Schoolの仕上げ

が大量に残っているなら、一枠の継続収入が大きくなります。

**表示Bonusの大きさではなく、解禁後に何Turn使えるか**を見ます。

---

# Owl Quillとの違い

[Owl Quill](owl-quill.md)は、Construction 1、A1でForgeでき、Research Bonus +6を与えます。

Lightless Lanternは、C7・F1でResearch Bonus +12です。

整理すると、

```text
Owl Quill
→ 早い
→ 一枠+6
→ 低いResearch thresholdから量産可能

Lightless Lantern
→ 遅い
→ 一枠+12
→ Horror-related riskを持つ
```

です。

Lightless Lanternは一枠の出力が高いため、

- Mage数が少ない
- Misc Slot数が限られる
- 高価値Researcherへ出力を集中したい

時に有利です。

ただしHorror-related riskがCarrier価値と結びつくため、単純な上位互換として扱いません。

---

# CarrierはResearch能力だけで選ばない

Research Itemは、Research値の高いMageへ付けたくなります。

しかしLightless Lanternでは、Carrierを失った時のCostも考えます。

高Riskなのは、

- 唯一の高Path Mage
- Rare Crosspathを持つMage
- Pretender
- Hero
- Booster chainの中核
- Global / Ritual担当
- 代替不可能なForge Mage

です。

Lanternの+12はCarrierの基礎Researchへ比例せず、Itemから固定で加算されます。

したがって、装備可能で安全に研究を続けられるなら、**比較的交換可能なMageへ持たせてCarrier Riskを抑える**判断があります。

---

# 一枠出力を集中する利点

Lightless Lanternの+12は、Owl Quill二つ分のResearch Bonusを一つのMisc Slotへまとめます。

これにより、

- Mage数が少なくても高い追加Researchを得る
- Item配送先を減らす
- 一人のResearcherで出力を集約する
- Misc Slotが一つしか空いていないMageを使う

ことができます。

ただし集中はRiskも集中します。

```text
一人へLanternを集中
→ 管理は簡単
→ Carrier loss時のResearch損失が大きい

複数の低出力Itemへ分散
→ 管理は増える
→ 単一事故の損失を抑えやすい
```

という違いがあります。

---

# Horror-related riskをResearch計画へ入れる

Item descriptionは、Lanternのdark lightがBearerをHorrorsへ露出させ得ると警告しています。

固定tableと短いdescriptionだけでは、

- Riskがいつ増えるか
- どの表示へ現れるか
- Itemを外した後に何が残るか
- Horror attackがどの条件で起こるか
- 複数Lanternでどう重なるか

の全挙動を安全に断定できません。

そのため攻略上は、

```text
Research +12は確定収入
Horror-related effectはCarrier Risk
```

として分け、Test gameと実際のUnit statusで確認します。

Riskを数値化できないから無視するのではなく、**代替可能なCarrier、後方防衛、Item回収計画**で吸収します。

---

# Darkvision 100の位置付け

Lightless LanternはDarkvision 100も与えます。

暗闇のBattlefieldへCarrierを出す場合、視界Penaltyを避ける助けになり得ます。

しかし通常、Lantern Carrierは後方LabでResearchを続ける方がItem出力を回収しやすい役割です。

Darkvisionを使うために前線へ出すと、

- Carrier死亡
- Lantern喪失
- Research中断
- Horror-related riskと戦闘Riskの重複

が発生します。

Darkvisionは有用な副次効果ですが、**Research ItemをCombat Itemへ無理に転用する理由にはしない**方が安全です。

---

# Research hubの防衛

Lanternが増えるほど、一つのLab / Fortへ蓄積する価値も増えます。

敵から見ると、Research hubは、

- Mage
- Lantern
- 他のResearch Item
- Gem
- Booster

を同時に奪えるTargetになります。

Item単体の価値を守るには、

- Scout detection
- PD / Fort defense
- 緊急退避Route
- Itemを持ったMageの分散
- Frontからの距離
- Lab破壊後の移送先

を用意します。

Lightless LanternはResearchを速めますが、Research hubを自動で安全にはしません。

---

# Forge担当と装備担当を分ける

F1 MageがLanternをForgeできても、そのMage自身へ持たせる必要はありません。

Forge担当がRare Fire accessやBattle roleを持つ場合、

```text
Forge MageがLantern作成
→ 安価なResearcherへ受け渡し
→ Forge Mageは次のItem / Battleへ戻る
```

方が価値を分離できます。

一方、配送に複数Turn掛かるなら、完成後すぐ装備できるResearch hubでForgeする方が早く+12を回収します。

Forge locationとCarrier locationをItem単位で計画します。

---

# 量産判断は最後の一個で考える

一個目のLanternが有効でも、十個目が同じ価値とは限りません。

量産するほど、

- Fire Gemを消費する
- Forge Mage turnを消費する
- Carrier数が必要になる
- Horror-related riskを持つMageが増える
- Research終了後の余剰Itemが増える
- 他のFire Item・Battle magicを圧迫する

からです。

各追加Lanternについて、

```text
この一個を作る
vs
Fire Gemを戦争・別Forgeへ回す
vs
Forge MageをResearchへ戻す
```

を比較します。

総数ではなく、**次の一個が何Turn使われるか**で止め時を決めます。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 7へ到達済み
- F1 Forge Mageを確保できる
- まだ大量のResearch目標が残っている
- Lanternを長期間持てるResearcherがいる
- Carrierを比較的代替しやすい
- Research hubを防衛できる
- Fire Gemを戦争・別Forgeから回せる
- Horror-related riskをTestし、許容できる
- Owl Quill等より一枠出力を優先する理由がある
- Item完成後すぐResearchへ投入できる

「Research +12だから常に作る」ではなく、**残りResearch TurnとCarrier Riskを含めて黒字になる時**にForgeします。

---

# Forgeしない・別Itemを選ぶ条件

- 主要Researchがほぼ終了している
- C7到達を他Schoolより優先する理由がない
- Fire GemをBattle magicや重要Weaponへ使う必要がある
- 装備可能なResearcherが全員希少Mage
- Research hubがRaid圏内
- Horror-related riskを許容できない
- Forge Mage turnをResearchへ戻した方が早い
- Owl Quill等の早期Itemで十分
- Lanternを配送する間に戦争Timingを逃す

高出力でも、使えるTurnが短ければ回収できません。

---

# Counter：Research収入とItem在庫を同時に狙う

敵がLightless Lanternを量産している場合、時間が経つほどResearch差が広がります。

Counterは、

- Research hubをScoutで特定する
- Fast RaiderやTeleportでLabを攻撃する
- Fort包囲でMageをResearchから外す
- Carrierを暗殺する
- Item配送路を遮断する
- 戦争Timingを早め、+12の回収Turnを減らす
- 複数Frontを作り、ResearcherをBattleへ動員させる
- Lanternを奪える戦闘を選ぶ

のように、**Research Bonusが積み上がる時間と安全性**を奪います。

Horror-related riskは敵側の不確実性ですが、それだけへ期待せず、こちらからResearch運用を中断させます。

---

# よくある失敗

## +12だけ見てC7 Timingを無視する

解禁が遅く、残りResearch Turnが少なければ回収できません。

## 唯一の高Path Mageへ持たせる

Itemの固定+12のために、代替不能なCarrierへRiskを集中しています。

## Horror-related warningをFlavor textとして無視する

Carrier statusとTest gameで実挙動を確認します。

## Darkvisionを使うため前線へ出す

Research中断とItem loss Riskが大きくなる場合があります。

## 研究終了後も量産を続ける

最後の一個が何Turn使われるかを見ず、Fire GemとForge turnを余剰Itemへ変えています。

---

# Test game checklist

```text
[ ] C7・F1でLightless LanternがForge可能か確認
[ ] Item 399であることを確認
[ ] Research Bonus +12がResearch値へ反映されることを確認
[ ] Darkvision 100がUnit画面へ反映されることを確認
[ ] Lanternなし／ありで月間Research差を確認
[ ] Owl Quillとの一枠出力・解禁Timingを比較
[ ] 実支払Gem costを確認
[ ] Item装備中のHorror-related status変化を記録
[ ] Itemを外した後に残る効果があるか確認
[ ] 複数Turn保有時のEvent / attack / markを確認
[ ] 安価なMageと希少MageでCarrier loss Costを比較
[ ] Research hubがRaidされた時のItem回収経路を確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 399](../../data/items/by-id/399.md)
- [Owl Quill](owl-quill.md)
- [Research Item](../research-items.md)
- [Dwarven Hammer](dwarven-hammer.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- BaseI: C7 / F1 / Research Bonus +12 / Darkvision 100
- Item description: Researchを助けるdark lightと、BearerがHorrorsへ露出し得るwarning
- Horror-related effectの発生Timing、蓄積、Item解除後の残存はゲーム内Unit status・Turn message・Test gameを優先
