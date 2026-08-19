---
title: Artifact・Unique Item攻略
status: expanding
verified_version: "6.35"
last_verified: "2026-08-19"
---

# Artifact・Unique Item攻略

Artifactは「高級Magic Item」の別名ではありません。

Dominions 6では、**Construction 9でForgeするItemがArtifactで、同じArtifactは世界に一つしか存在できません。**

したがってArtifactは、

```text
Construction 9へ到達する
→ 必要Pathへ届く
→ Gemを確保する
→ まだ存在していないArtifactをForgeする
→ Carrierを守る
```

という**先着競争**です。

さらにArtifactには`yearning`があり、ゲーム進行によってForge Costが半額になることがあります。

正確な6.35の要求Path・通常Cost・Slot・効果は、

- [Artifact一覧 — Construction 9](../data/items/artifacts.md)
- [Magic Item Weapon profile](../data/items/weapon-profiles.md)
- [Magic Item Armor profile](../data/items/armor-profiles.md)
- [Item Spell・自動効果](../data/items/active-effects.md)
- [Summon・Retinue Item](../data/items/summoning-effects.md)
- [Item副作用・装備制限](../data/items/risk-restrictions.md)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)

を使います。

---

# ArtifactとUnforgeable Itemは別

ここは用語上かなり重要です。

## Artifact

Dominions 6 Manualでは、**research / Construction level 9のforgeable Item**をArtifactと呼びます。

- Forgeできる
- Construction 9が必要
- unique
- 同じArtifactが既に存在している間はForgeできない
- yearning対象になる

という性質があります。

## Unforgeable Item

通常の`Forge Item`では作れないItemです。

入手経路はItemごとに異なり、

- Event
- Arena
- 特殊生成
- 国家固有
- その他のゲーム内入手手段

を確認します。

[Unforgeable Item一覧](../data/items/unforgeable.md)と[Arena関連Magic Item](../data/items/arena.md)を参照してください。

> **Artifact = Unforgeableではありません。**

ArtifactはC9でForgeするunique Itemです。

---

# Uniqueとは何か

Artifactは世界に同じものが同時に一つしか存在できません。

つまり、自分が必要PathとGemを持っていても、他Playerが既にそのArtifactを所有していれば作れません。

このため通常Itemとは価値計算が変わります。

通常Itemなら、

```text
欲しい
→ Gemを貯める
→ 後から作る
```

でよいことが多いですが、Artifactでは、

```text
欲しい
→ Enemyも欲しいか
→ C9到達Timing
→ Forge可能Mage
→ Gem在庫
→ 先に作れるか
```

まで考えます。

---

# Artifact race

Artifact争いはResearch競争だけではありません。

必要なのは、

1. Construction 9
2. Forge Path
3. Booster
4. Gem
5. Forge Mageの一Turn
6. Artifactがまだ存在していないこと

です。

一つでも欠けると先着できません。

---

# C9へ到達するだけでは足りない

よくある失敗は、Construction 9を研究してからForge準備を始めることです。

例えば欲しいArtifactが高い複合Pathを要求するなら、C9完成前に、

```text
Native Mage
→ Booster 1
→ Booster 2
→ Summoned Mage / Pretender
→ 最終Forge Path
```

を作っておきます。

C9完成TurnにForge orderを出せる状態が理想です。

[Magic Path Booster](boosters.md)と[Magic Access Route](../magic/magic-access-routes.md)を使います。

---

# Yearning

Artifactには`yearning`という特殊なForge Cost軽減があります。

公式Manualでは、yearning状態になったArtifactは**通常Costの半額でForge**できます。

ただしyearningは静的なItem能力ではなく、ゲーム進行中に発生する状態です。

そのため自動生成Item表のGem欄には反映されません。

最終Costは必ずゲーム内Forge画面で確認します。

---

# Yearningが始まり得る条件

公式Manualでは、少なくとも次のいずれかが発生するとArtifactがyearningを開始する可能性が生じます。

- 少なくとも一国がConstruction 9を研究した
- Global Enchantment `Forge of the Ancients` が発動した
- `Throne of Creation` がClaimされた
- `Throne of the Artificer` がClaimされた

各条件はyearning rateを50%ずつ増加させます。

Manualの例では、条件が一つだけ成立している場合、Artifactがyearningを開始する確率は**毎月50%**です。

---

# Yearningをどう使うか

Yearningを待つとGemを大きく節約できます。

一方で待っている間にEnemyが先にForgeするRiskがあります。

したがって判断は、

```text
今すぐ通常Costで確保する価値
vs
Yearningを待って節約する価値
vs
Enemyに取られるRisk
```

です。

---

# すぐForgeするArtifact

次のような場合はyearning待ちより先着を優先しやすくなります。

- 勝ち筋の中心になる
- Enemyが同じPathを持つ
- EnemyもC9へ近い
- Artifactで次のGlobal / Army / SCが完成する
- Throne戦が数Turn以内
- Gem在庫に余裕がある

重要なのは「高性能だから」ではなく、**失うと代替がないか**です。

---

# Yearningを待ちやすいArtifact

逆に、

- 今すぐ使うCarrierがいない
- Enemyが要求Pathへ届きにくい
- Gemが戦争用に必要
- 複数Artifactを連続Forgeしたい
- まだC9到達国が少ない

なら待つ価値があります。

ただし完全な情報は得られません。

MultiplayerではEnemyのResearch・Pretender・Booster chainを推測します。

---

# Artifact優先順位を固定Tierにしない

Artifactは一律Tier化しにくいItemです。

同じArtifactでも、

- Nation
- Pretender
- Native magic
- Gem income
- Carrier
- Enemy composition
- Map
- Throne状況
- 残りTurn

で価値が変わります。

評価軸を使います。

| 軸 | 質問 |
|---|---|
| Access | 新しいPath / Spell / Ritualを開くか |
| Army | 一人ではなくArmy全体へ影響するか |
| Economy | Gem / Gold / Research / Unit生成を生むか |
| Mobility | Raid / Teleport / Sailing等を変えるか |
| Combat | SC / Thug / Anti-SC能力を作るか |
| Unique | 他Itemで代替できるか |
| Timing | 今の戦争に間に合うか |
| Risk | Carrier死亡時の損失が大きいか |

---

# ArtifactをPath accessとして見る

Artifactの中には、単なる戦闘装備ではなくMagic economyを変えるものがあります。

その場合、

```text
Artifact
→ Path access
→ Forge / Ritual
→ Summon Mage
→ 次のMagic diversity
```

という連鎖を評価します。

一戦で何Damage増えるかより、国家全体のMagic ceilingが変わる方が重要なことがあります。

---

# ArtifactをArmy effectとして見る

Start battle effect、Battlefield condition、Summon、Leadership等を持つArtifactはCarrier一人のStatsだけでは評価できません。

[Item固有効果・Weapon proc・副作用](effects-and-procs.md)で、

- Item本体
- Weapon / Armor
- Start battle
- Auto combat
- Summon
- 副作用

を分解して確認します。

---

# ArtifactをSC装備として見る

ArtifactをSCへ全部積めば強い、とは限りません。

Artifactはuniqueなので、Carrier死亡時の機会損失が通常Itemより大きくなります。

SCへ渡す前に、

```text
このArtifactでしか解決できない弱点か？
```

を確認します。

通常C5/C7 Itemで任務を満たせるなら、Artifactを後方Casterや別Commanderへ残せる場合があります。

---

# Carrier Risk

Artifactを持つCommanderはEnemyから見ても高価値Targetです。

警戒するもの：

- Assassination
- Remote attack
- Magic Duel
- Soul Slay / Control
- AN burst
- Fatigue kill
- Retreat blocking
- Teleport interception
- Horror / special effect

Artifactそのものだけでなく、Carrierの価値も計算します。

---

# Artifactを後方Mageへ持たせる場合

Forge / Ritual / Global用Artifactなら、前線に出す必要がないことがあります。

- Capital後方
- Safe Fort
- Lab
- Patrol
- Anti-assassin Bodyguard
- Retreat route

を用意します。

F8のMagic item overviewで所在を定期確認します。

---

# Artifactを前線へ持たせる場合

戦闘効果が目的ならRiskを受け入れます。

その代わり、

- MR
- Elemental Resistance
- Bodyguard
- Gem
- Retreat
- Scout情報

をArtifact以外の安価な手段で補います。

「Artifactが強いから裸Carrierでも強い」と考えないことが重要です。

---

# 敵がArtifactを持ったとき

Counterは同じArtifactを作ることではありません。

すでに存在しているなら同じArtifactをForgeできないため、**別Counterを作る必要があります。**

まず効果を分解します。

```text
Weaponが強い？
Start battleが強い？
Path Boosterが強い？
Summon economyが強い？
Mobilityが強い？
SC sustainが強い？
```

その発生源を狙います。

---

# Counter：Carrierを殺す

Artifactの効果が一人のCarrierへ集中しているなら、Army全体を正面から倒す必要はありません。

- Assassin
- Remote
- Magic phase interception
- Precision / Commander snipe
- MR attack
- Anti-SC specialist

でCarrier本人を狙います。

ただしArtifactのStart battle effectなど、戦闘開始時点で既に価値を発揮するものは「戦闘中に殺せば止まる」とは限りません。

---

# Counter：Slotを攻める

ArtifactもSlotを使います。

Enemyが強力なArtifactを装備することで、

- MR
- Resistance
- Reinvigoration
- Mobility
- Shield

のどれかを諦めている場合があります。

Artifact名ではなく**空いた弱点**を探します。

---

# Counter：C9前に戦う

Artifact raceへの最も単純なCounterは、相手がC9へ投資している間に戦争を始めることです。

Construction 9へのResearchは、同じ期間に、

- Alteration
- Enchantment
- Evocation
- Thaumaturgy
- Conjuration

へ行かなかったことを意味します。

相手の現時点のBattlefield breakpointが低いなら、Artifact完成前がTiming windowです。

---

# Counter：Gem economyを攻撃する

C9へ到達してもGemがなければArtifactは作れません。

- Gem Site Raid
- Capital / Lab pressure
- Global dispel
- Gem-burning war
- Booster carrier assassination

でForge準備を遅らせます。

---

# ArtifactとDiplomacy

MultiplayerではArtifactの存在が外交情報になります。

例えば、

- 特定Artifactを誰が持っているか
- C9到達国がいるか
- Forge of the Ancientsが出たか
- 関連ThroneがClaimされたか

は、他国のResearch・Magic access・勝ち筋を推測する材料です。

Artifact forgeそのものが見えなくても、Battle ReplayやScoutで装備を確認できます。

---

# C9へ行く前のチェック

```text
欲しいArtifact：
そのArtifactで何が変わる：
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

これを埋められないなら、「Artifactが強そうだからC9」は危険です。

---

# Forge開始Turnの準備

理想はC9完成後に考えるのではなく、その前Turnまでに、

- BoosterをTreasuryへ置く
- Forge MageをLabへ戻す
- Gemを移送する
- Carrierを準備する
- Monthly Forgeを止める
- F8で必要Itemの所在を確認する

ところまで終えることです。

---

# Yearning確認

Yearningは自動生成データだけでは判断できません。

Forge画面で実際のCostを確認します。

通常Costと比べて大きく安くなっていれば、現在のゲーム状態が価格へ反映されています。

WikiのGem欄は静的な6.35基礎データとして使い、**現在ゲームの価格はゲームUIをsource of truth**とします。

---

# Unforgeable Itemの考え方

Unforgeable ItemはC9 raceとは別です。

「Constructionを研究すれば取れる」という前提を持たず、入手経路から考えます。

```text
Item
→ どこから出るか
→ 再現可能か
→ Uniqueか
→ Carrierを選べるか
→ 入手Timingを操作できるか
```

を確認します。

---

# Arena Item

Arena報酬等で得るItemは、Forge economyではなくArena参加Riskとの交換です。

評価は、

```text
参加Commanderを失うRisk
vs
勝利報酬Item
vs
Championを前線から外すTurn
```

になります。

[Arena関連Magic Item](../data/items/arena.md)を参照します。

---

# Event / Special acquisition

Eventや特殊生成Itemは、通常Forgeとは供給の再現性が違います。

偶然得た強力Itemを国家標準buildの前提にしないようにします。

一方、入手した後はF8で管理し、通常Itemと同じように、

- Carrier
- Slot
- Counter
- loss risk

を評価します。

---

# よくある失敗

## ArtifactとUnforgeableを同じ意味で使う

C9 ArtifactはForge可能なunique Itemです。

## C9へ着いてからBoosterを作る

Enemyに先着されます。

## Yearningを必ず待つ

半額を待っている間にArtifact自体を失います。

## Yearningを一切待たない

Enemyが狙えないArtifactへ毎回通常Costを払ってGem economyを消耗します。

## Artifactを全部SCへ積む

国家全体のMagic accessやArmy supportを一人へ集中します。

## CarrierのMRを見ない

高額Itemを一回のControl / Soul attackで失います。

## C9をResearchの終点と思う

Artifactを作るだけで勝つわけではありません。作ったItemをどの勝ち筋へ変換するかが必要です。

---

# Test Game

ArtifactをPretender設計へ組み込む場合はTest Gameで、

- Booster chainが本当に成立するか
- C9到達Timing
- Gem income
- Forge MageのPath
- Yearning前後のForge画面
- Carrier Slot
- Battle script

を確認します。

特に複合Path Artifactは、Pathの一段不足で計画全体が止まります。

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
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
