---
title: Artifact・Unique Item攻略
status: expanding
verified_version: "6.35"
last_verified: "2026-08-19"
---

# Artifact・Unique Item攻略

Dominions 6のArtifactを理解するときは、まず**Forge可能なConstruction 9 Artifact**と、**通常ForgeできないItem class**を分けます。

公式Main Manualでは、Construction / research level 9でForgeできるItemをArtifactと呼び、同じArtifactは世界に一つだけ存在できます。

一方、Modding Manualの`constlevel`には、

- 11 — unforgeable item
- 13 — unforgeable unique artifact
- 15 — unforgeable unique per nation artifact

という別の取得classもあります。

したがってこのWikiでは、曖昧な「Artifact」という一語だけで分類せず、

> **Forgeable Artifact（C9）**
>
> **Unforgeable Item（constlevel 11 / 13 / 15）**

として取得経路を明示します。

正確な6.35データは、

- [Forgeable Artifact一覧 — Construction 9](../data/items/artifacts.md)
- [Unforgeable Item一覧](../data/items/unforgeable.md)
- [Magic Item Weapon profile](../data/items/weapon-profiles.md)
- [Magic Item Armor profile](../data/items/armor-profiles.md)
- [Item Spell・自動効果](../data/items/active-effects.md)
- [Summon・Retinue Item](../data/items/summoning-effects.md)
- [Item副作用・装備制限](../data/items/risk-restrictions.md)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)

で確認します。

---

# Forgeable Artifact — Construction 9

Main Manualが通常のArtifactとして説明しているのがConstruction 9 Itemです。

特徴は、

- Construction 9が必要
- Forge要求Pathが必要
- Gem / Blood Slaveが必要
- unique
- 同じArtifactが既に存在している間はForgeできない
- yearningによるCost軽減がある

ことです。

通常Itemのように「後でGemが貯まったら作ればよい」とは限りません。

```text
C9へ到達
→ Forge Pathを完成
→ Gemを準備
→ Enemyより先に確保
→ Carrierを守る
```

という**Artifact race**になります。

---

# Unforgeable Item — constlevel 11 / 13 / 15

こちらは通常の`Forge Item` orderでは作れません。

6.35の固定データでは、Modding Manualのclassに合わせて、

| constlevel | Wiki表示 | 意味 |
|---:|---|---|
| 11 | Unforgeable | 通常Forge不可 |
| 13 | Unforgeable unique artifact | Forge不可・unique |
| 15 | Unforgeable unique per nation artifact | Forge不可・国家単位unique |

として索引化します。

重要なのは、**Construction 9を研究しても取得できない**ことです。

入手経路はItemごとに、

- Event
- Arena
- 国家固有
- 特殊生成
- その他のゲーム内取得

を確認します。

[Arena関連Magic Item](../data/items/arena.md)や[Magic ItemによるUnit生成・変身](../data/units/item-unit-sources.md)も併用してください。

---

# 「Artifact」と「Unforgeable」を混ぜない

`unforgeable unique artifact`という技術用語があるため、

> Artifact = 必ずForge可能

とも、

> Artifact = Unforgeable

とも言い切れません。

攻略上は**取得方法**で分けるのが安全です。

```text
C9でForgeする？
├─ Yes → Forgeable Artifact / Artifact race / Yearning
└─ No  → Unforgeable class / 入手イベントや特殊条件を調べる
```

---

# Uniqueとは何か

Forgeable C9 Artifactは同じものが同時に世界に一つしか存在できません。

そのため、

- 自分がC9へ到達した
- 要求Pathがある
- Gemもある

だけでは不十分です。

既に他国がそのArtifactを所有しているならForgeできません。

通常Itemとの最大の違いは、**研究と資源だけでなく先着権が価値になる**ことです。

---

# Artifact raceの六つの条件

Forgeable Artifactを確保するには、少なくとも次が必要です。

1. Construction 9
2. Forge要求Path
3. Booster / Summon / Pretender等のPath route
4. 必要Gem
5. Forge担当Mageの一Turn
6. Artifactがまだ世界に存在していないこと

C9完成後に1～5を準備し始めると遅い場合があります。

---

# C9より先にBooster chainを作る

欲しいArtifactが高Path・複合Pathなら、研究完成前にForge Mageを作ります。

```text
Native Mage
→ Booster 1
→ Booster 2
→ Summoned Mage / Pretender
→ Artifact要求Path
```

C9完成Turnに`Forge Item`を選べる状態が理想です。

- [Magic Path Booster](boosters.md)
- [Magic Path Boosting](../magic/boosting.md)
- [Magic Access Route](../magic/magic-access-routes.md)

を使って事前計画します。

---

# Yearning

Forgeable Artifactには`yearning`があります。

Main Manualでは、**yearning状態のArtifactは通常Costの半額でForge**できます。

これはBaseIに固定されたItem能力ではなく、進行中のゲーム状態です。

そのため、

- Wikiのgenerated Gem欄
- 固定6.35 BaseI

にはyearning後の価格を入れません。

**現在のForge Costはゲーム内Forge画面をsource of truth**とします。

---

# Yearningが始まり得る条件

Main Manualは、少なくとも次のイベントのどれかが起きるとArtifactがyearningし始める可能性が生じると説明しています。

- 少なくとも一国がConstruction 9を研究した
- Global Enchantment `Forge of the Ancients` が発動した
- `Throne of Creation` がClaimされた
- `Throne of the Artificer` がClaimされた

各イベントはyearning rateを50%増加させます。

Manualの例では、一条件だけ成立している場合は**毎月50%**でArtifactがyearningを開始します。

---

# Yearningは「半額だから待つ」だけではない

Yearningを待つ利点は大きなGem節約です。

しかし待機中にEnemyがForgeすれば、そのArtifact自体を失います。

判断は、

```text
通常Costで今すぐ確保する価値
vs
Yearningで節約する価値
vs
Enemyに先着されるRisk
```

です。

---

# すぐForgeしやすい状況

- Artifactが勝ち筋の中心
- 代替Itemがない
- Enemyも同じForge Pathへ届く
- EnemyもC9へ近い
- Throne決戦が近い
- ArtifactでGlobal / Army / SCが即完成する
- 現在Gemで支払っても戦争資源が残る

こういう場合、半額待ちより**確保**が優先されます。

---

# Yearningを待ちやすい状況

- 今すぐCarrierがいない
- Enemyが要求Pathへ届きにくい
- Gemを目先の戦争に使う必要がある
- 複数Artifactを計画している
- そのArtifactに通常Itemで代替がある

ただしMultiplayerではEnemyのResearchやBooster chainは完全には見えません。

待つこと自体がRiskです。

---

# Artifactを固定Tierにしない

同じArtifactでも価値はNation・Map・Enemy・Timingで変わります。

| 評価軸 | 質問 |
|---|---|
| Access | 新しいPath / Spell / Ritualを開くか |
| Army | 一人ではなくArmy全体へ影響するか |
| Economy | Gem / Gold / Research / Unit生成を生むか |
| Mobility | Raid / Teleport / Strategic moveを変えるか |
| Combat | SC / Thug / Anti-SC能力を作るか |
| Unique | 通常Itemで代替できるか |
| Timing | 今の戦争・Throne raceに間に合うか |
| Carrier | 誰に持たせ、失ってよいか |

「有名ArtifactだからForge」ではなく、この表で評価します。

---

# Magic accessとしてのArtifact

Path Booster系Artifactは一人のStats強化ではなく国家のMagic ceilingを変えます。

```text
Artifact
→ 新しいPath
→ Forge / Ritual
→ Summoned Mage
→ 次のMagic diversity
```

へ繋がるなら、戦闘Item以上の価値があります。

---

# Battlefield effectとしてのArtifact

Start battle spell、Auto combat、Summon等を持つItemはCarrier一人のStatsだけでは評価できません。

[Item固有効果・Weapon proc・副作用](effects-and-procs.md)で、

- Item本体
- Weapon / Armor
- Secondary
- Start battle
- Auto combat
- Summon
- Risk / restriction

を分解してください。

---

# SC装備としてのArtifact

ArtifactをSCへ積めば強いとは限りません。

unique Itemを一人に集中すると、

- Carrier死亡
- MR attack
- Assassination
- Retreat不能

で国家全体の資産をまとめて失います。

通常C5/C7 Itemで任務を達成できるなら、Artifactを別のCasterや戦略用途へ残す方がよい場合があります。

---

# Carrier Risk

Artifact carrierは高価値Targetです。

警戒するもの：

- Assassination
- Remote attack
- Magic phase interception
- Magic Duel
- Soul Slay / Charm / Control
- AN burst
- Fatigue kill
- Retreat blocking

Item価格だけでなく、Rare Mage・Hero・Pretender本人の価値も含めます。

---

# 後方Artifact carrier

Forge / Ritual / Global用途なら前線へ出す必要がありません。

- Safe Fort
- Lab
- Patrol
- Bodyguard
- Retreat route

を用意します。

F8のMagic item overviewで所在を確認し、前線Mageへ付けっぱなしにしません。

---

# 前線Artifact carrier

戦闘効果が目的ならRiskを受け入れます。

その代わり、Artifact以外で、

- MR
- Elemental Resistance
- Reinvigoration
- Bodyguard
- Retreat

を補います。

Artifact一個でCarrierの全弱点が消えるわけではありません。

---

# Counter：敵のArtifactを分解する

同じArtifactが既に存在するなら、自分は同じものをForgeして対抗できません。

まず敵Artifactの価値の発生源を見ます。

```text
Weapon性能？
Secondary？
Start battle？
Path Booster？
Summon economy？
Mobility？
SC sustain？
```

そして別軸からCounterします。

---

# Counter：Carrierを狙う

効果がCarrierへ集中するならArmy全体を倒す必要はありません。

- Assassin
- Commander snipe
- Remote
- MR attack
- Anti-SC specialist

でCarrierを狙います。

ただしStart battle effectのように、戦闘開始時点で既に価値を発揮する効果は、戦闘中にCarrierを倒しても「発動前へ巻き戻る」わけではありません。

---

# Counter：Slotを狙う

Artifactも装備Slotを使います。

EnemyがArtifactを装備した結果、

- MR
- Elemental Resistance
- Reinvigoration
- Shield
- Mobility

のどれかが不足している場合があります。

Artifactそのものを正面突破するより、**そのItemのために空いた弱点**を攻めます。

---

# Counter：C9完成前に戦う

C9研究は大きなResearch投資です。

相手がConstructionへ深く進んだということは、同じResearchをBattle magicへ使っていない可能性があります。

Artifact完成前のTiming windowを狙います。

---

# Counter：Gem economyを攻撃する

C9・PathがあってもGemがなければForgeできません。

- Gem Site Raid
- Forge hub attack
- Booster carrier assassination
- BattleでGemを吐かせる
- Globalへの圧力

でArtifact準備を遅らせます。

---

# ArtifactとDiplomacy

Multiplayerでは次の情報がArtifact raceの手掛かりになります。

- C9到達が見える動き
- Forge of the Ancients
- Throne of Creation / Artificer
- 高Path Pretender
- Boosterを積んだMage
- Battle Replayで確認したArtifact

これらからEnemyのResearch・Forge routeを推測します。

---

# C9研究前チェック

```text
欲しいForgeable Artifact：
何が勝ち筋になる：
要求Path：
Forge可能Mage：
必要Booster：
通常Gem Cost：
現在Gem：
Enemyも狙えるか：
Yearningを待つか：
Carrier：
Carrier防御：
代替C5/C7 Item：
C9研究で遅れるBattle Spell：
```

これを埋められないなら、C9を「強いItemがあるから」で研究するのは危険です。

---

# Forge開始Turnを準備する

C9完成前に、

- BoosterをTreasuryへ置く
- Forge MageをLabへ戻す
- Gemを集める
- Carrierを決める
- 不要なMonthly Forgeを止める
- F8でItem所在を確認する

ところまで済ませます。

C9完成後に準備を始める一TurnがArtifact raceでは大きな差になります。

---

# Unforgeable Itemの評価

UnforgeableはResearch raceではなく**入手経路**から評価します。

```text
Item
→ 何から入手するか
→ 再現可能か
→ unique classか
→ Carrierを選べるか
→ Timingを操作できるか
```

偶然Eventで得るItemを国家標準buildの前提にしないことも重要です。

---

# Arena Item

Arena報酬はForge economyとは違います。

```text
参加Commanderを失うRisk
vs
勝利報酬
vs
Championを他任務から外すTurn
```

で判断します。

[Arena関連Magic Item](../data/items/arena.md)を参照してください。

---

# よくある失敗

## C9 ArtifactとUnforgeableを同じ一覧にする

取得方法が違うため、戦略判断を誤ります。

## constlevel 11 / 13 / 15をConstruction研究で解禁すると考える

これらは通常Forge不可classです。

## C9へ着いてからBoosterを作る

Enemyに先着されます。

## Yearningを必ず待つ

Gemを節約してもArtifactそのものをEnemyに取られれば失敗です。

## Yearningを一切待たない

競争が薄いArtifactへ毎回通常Costを払い、戦争Gemを失う場合があります。

## Artifactを一人へ集中する

一回のCounterで国家全体のunique資産を失います。

## generated Gem欄を現在価格だと思う

Yearningはgame stateなので、最終価格はForge画面を確認します。

---

# Test Game

PretenderやBooster chainをArtifact前提で設計する場合は、Test Gameで、

- C9到達Timing
- Booster chain
- Forge Path
- Gem income
- Carrier Slot
- Forge画面
- Yearning前後の価格

を確認します。

複合Path Artifactは一段不足するだけで計画全体が止まります。

---

## 関連ページ

- [Magic Item総論](index.md)
- [Forge計画とConstruction Breakpoint](forge-planning.md)
- [用途別Magic Item辞典](purpose-dictionary.md)
- [Item固有効果・Weapon proc・副作用](effects-and-procs.md)
- [Magic Path Booster](boosters.md)
- [Magic Path Boosting](../magic/boosting.md)
- [Gem economy](../magic/gems.md)
- [Strategic Ritual](../magic/strategic-rituals.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Modding Manual](https://www.illwinter.com/dom6/dom6modman.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
