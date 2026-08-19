---
title: Forge計画とConstruction Breakpoint
status: expanding
verified_version: "6.35"
last_verified: "2026-08-19"
---

# Forge計画とConstruction Breakpoint

Magic Itemは「Constructionを上げれば強い装備が増える」というだけの仕組みではありません。

実戦では、

> **何を作りたいか → 誰がForgeできるか → 何Gem必要か → 何Turn使うか → そのためにConstructionをどこまで上げるか**

の順に考えます。

全Itemの正確な一覧は[Magic Itemデータ索引](../data/items/index.md)と[Dom6 Mod Inspector](https://larzm42.github.io/dom6inspector/)を使い、このページでは研究・Gem・Mage turnをどうForge計画へ変換するかを扱います。

---

# まず操作を覚える

## Forgeする

Magic Itemを作るCommanderは、**自国のLaboratoryがあるProvince**で`Forge Item` orderを選びます。

Forge画面では、

- 現在のConstruction
- ForgeするMageのMagic Path
- 所持しているGem / Blood Slave
- Itemの要求Path
- 実際に支払うCost

を確認します。

Item表だけ見て「作れるはず」と判断せず、最後はゲーム内Forge画面を確認します。

## 同じItemを毎Turn作る

同じCommanderへ同じItemを繰り返しForgeさせたい場合は、Commanderを選択して**Shift + O**でmonthly forgeを設定できます。

Research Itemや量産用装備を作るときに便利ですが、戦争でGem予算が変わっても自動生産を続けるので、毎Turnの資源残量を確認します。

## 作ったItemを探す

- **F7 — Magic item treasury**: Treasuryに保管中のItemを見る
- **F8 — Magic item overview**: Treasuryだけでなく、Commander装備中のItemを含めて所在を確認する

「作ったBoosterがどのMageに付いたままか分からない」という問題はF8で確認します。

---

# Forgeの基礎Gem Cost

Dominions 6では、通常のMagic Itemの基礎Forge Costは要求Magic Path levelから決まります。

| Path level | 基礎Cost |
|---:|---:|
| 1 | 5 |
| 2 | 10 |
| 3 | 15 |
| 4 | 20 |
| 5 | 30 |
| 6 | 40 |
| 7 | 55 |
| 8 | 70 |

複数Pathを要求するItemは、それぞれのPath分の資源を使います。

ただし、これは**基礎値**です。Item固有Cost、Forge Bonus、国家固有の割引などがあるため、最終支払額はゲーム内Forge画面を優先します。

自動生成Item表の`Gem`も、原則としてForge Bonusや国家割引を適用する前の基礎Costを示します。

---

# Constructionは1 / 3 / 5 / 7 / 9で考える

Dom6の通常Forge ItemはConstructionの奇数Breakpointで大きく増えます。

「Constructionを上げる」ではなく、**次のBreakpointで何を解禁したいか**を決めます。

## Construction 1 — 最小の穴埋め

序盤のTrinketが中心です。

用途は、

- 小さなResistance
- 低要求の武器・防具
- Movement / Stealth等のUtility
- 特殊なCarrierを安く補助

です。

C1のItemだけを目的に研究ルートを大きく曲げることは少なく、他の研究の通過点として使うことが多くなります。

## Construction 3 — 早期経済と実用品

ここからForgeが国家運営へ影響し始めます。

代表的な判断は、

- Research Itemを早く量産するか
- 安いResistanceを用意するか
- Raider / Assassinへ最低限の装備を渡すか
- Gemを研究投資せずBattle spellへ残すか

です。

C3へ寄る価値は「Itemが強いか」より、**今から長期間使えるか**で決まります。

## Construction 5 — Booster・Counter・Thug装備の中心

多くの国家で最も重要なForge breakpointの一つです。

この段階では、

- Magic Path Booster
- Research Item
- Elemental / MR / Poison counter
- Reinvigoration
- Mobility
- Thugの武器・防具
- Utility / Retinue /特殊能力Item

が競合します。

C5へ到達したら「全部作る」のではなく、戦略目的を3つ程度に絞ります。

```text
例
1. 次のMagic accessを開くBooster
2. 直近の敵へ必要なResistance
3. 余剰GemをResearch economyへ変換
```

この優先順位なら、Forge turnとGemが散りにくくなります。

## Construction 7 — 高級装備を戦争計画へ組み込む

C7は高性能Itemが増えますが、その分、

- Item一個のGem投資
- Rare MageのForge turn
- Carrier死亡時の損失
- 他Schoolを遅らせたResearch cost

も大きくなります。

C7 Itemは「強いから作る」のではなく、**どのArmy / Commander / Global計画へ投入するか**を先に決めます。

またLate gameに近づくため、Research Itemのような長期回収型と、即時戦力型の価値が逆転しやすくなります。

## Construction 9 — Artifact race

Construction 9のArtifactはUniqueです。同じArtifactは世界に一つしか存在できません。

したがってC9は通常Itemの延長ではなく、

- Artifactへ先着する
- Pretender / high-path Mageで要求Pathへ届く
- Booster chainを事前に作る
- 必要Gemを貯める
- 作成後のCarrierを守る

という**競争**です。

Artifactがyearningしている場合は通常より安くForgeできることがあります。実際のForge画面でCostを確認します。

---

# 「何を作るか」はSlotから逆算する

Itemを名前で選ぶ前にCarrierのSlotを見ます。

例えばThugが必要としているものが、

```text
Magic Weapon
+ MR
+ Reinvigoration
+ Shock Resistance
```

だとしても、必要Itemが全部Misc slotへ集中するなら成立しません。

Forge前に、

```text
Head:
Body:
Weapon 1:
Weapon 2 / Shield:
Boots:
Misc 1:
Misc 2:
Special / Mount:
```

を書き、**空Slotではなく役割**を埋めます。

---

# Forge担当MageのTurnも資源

Mageが一TurnForgeすると、そのTurnは通常、

- Research
- Ritual
- Site Search
- Movement

に使えません。

そのためItem CostはGemだけではありません。

```text
実質Forge投資
=
Gem / Slave
+ Forge担当Mageの1 Turn
+ Constructionへ振ったResearch
+ 装備Slot
+ Carrier risk
```

高Path Mage一人しかいない国家では、そのMageのForge turnが最大のボトルネックになることがあります。

---

# Forge Bonusは「量産数」で評価する

Forge Bonusやdiscount Itemは、一個作るときより**同じ資源を何回使うか**で価値が変わります。

例えばdiscount用Itemを先に作る場合、

```text
discount投資
<
今後のItem一個あたり節約額
× Forge予定数
```

になって初めて経済的に回収します。

ただし実戦では、Gem節約だけでなく、

- Rare Gemを別用途へ残せる
- Booster chainを早く完成できる
- Artifact要求資源を確保できる

ことにも価値があります。

---

# Path accessから逆算する

「C5まで行ったのに欲しいItemを作れない」という場合、多くはConstructionではなくForge Path不足です。

順番は、

```text
欲しいItem
→ 要求Path
→ 現在のMage
→ Boosterで届くか
→ Booster自身を誰が作るか
→ Summon / Indie / Pretender / Empowermentが必要か
```

です。

この連鎖は[Magic Path Booster](boosters.md)と[Magic Path Boosting](../magic/boosting.md)を使って確認します。

---

# 目的別Forge予算

毎Turn余ったGemを適当にForgeへ入れると、国家のMagic economyが読めなくなります。

用途を分けます。

| 予算 | 目的 | 典型的な判断 |
|---|---|---|
| Access | Booster | 次のSpell / Summon / Artifactへ届くか |
| Research | Research Item | 回収Turnが残っているか |
| Counter | Resistance / MR | 直近のEnemyへ必要か |
| Commander | Thug / Raider | Carrierが何戦使えるか |
| Army support | Utility | Supply / Leadership / movement等を解決するか |
| Reserve | 未使用 | Battle Gem / Emergency Forge / Artifactへ残す |

Reserveをゼロにしないことが重要です。

---

# 戦況別の優先順位

## 平時

長期回収型が強くなります。

- Research Item
- Booster chain
- Forge discount基盤
- Strategic mobility
- Artifact準備

を進めやすい時期です。

## 開戦直前

「数Turn後に価値が出るItem」より、最初の2～3戦で効くものを優先します。

- Elemental Resistance
- MR
- Anti-Ethereal / Magic Weapon
- Reinvigoration
- Mobility
- Battlefield caster用Booster

などです。

## 戦争中

Enemyの実際のArmy compositionへ合わせます。

一度作ったテンプレLoadoutを盲目的に量産せず、Battle Replayから負け筋を見て必要ItemだけForgeします。

## 終盤

回収期間が短いため、GemをResearch Itemへ変換する価値が低下しやすくなります。

一方、

- Artifact
- Throne assault用SC / Thug
- Global caster用Booster
- 最終決戦のCounter Item

は一戦でゲームを決めるため、高額でも回収できます。

---

# Counter：敵のItemを見る

Itemは敵の戦略を公開する情報でもあります。

Battle ReplayやScout情報で、

- Boosterがある → 高Path Spellを疑う
- Resistance Itemがある → 自分の主Damageへの対策を疑う
- Reinvigorationが多い → 長期戦Caster / Thugを疑う
- MR Itemが多い → MR-negates攻撃への対策を疑う
- Flying / movement Item → Raiderの到達範囲を広く見る
- Research Itemが多い → 相手が時間をResearchへ投資している

と読みます。

Counterは「さらに高いItemを作る」だけではありません。

- Slotを埋めさせる
- Itemで防げないDamageへ切り替える
- Carrier本人をAssassinate / Snipeする
- Research / Forge hubをRaidする
- Gem incomeを奪う
- Artifact完成前に戦争を始める

など、**Item経済そのものを攻撃**できます。

---

# よくある失敗

## Constructionだけ上げる

欲しいItemをForgeできるPathがありません。

## Forge画面を見ず表のCostだけ使う

Forge Bonus、国家割引、Item固有Costを見落とします。

## 強いItemから順に作る

Carrierと敵が決まっていないためGemが寝ます。

## Shift + Oを放置する

戦争が始まってもResearch Item等を自動生産し続け、Battle Gemがなくなります。

## F8を使わない

重要Boosterが後方Mageや死亡Riskの高いCommanderに付いたままになります。

## Slot競合を後から考える

Forge済みItemがLoadoutへ入りません。

## Carrier riskをGemだけで見る

Rare Mage、Hero、Pretenderを失う方がItemより大きな損失になる場合があります。

---

# Forge計画テンプレート

```text
目的：
次の戦争 / 研究目標：
必要Construction：
Item名：
要求Path：
基礎Cost：
ゲーム内表示Cost：
Forge担当：
Forge担当の代替任務：
Carrier：
使用予定Turn / 戦闘数：
Slot競合：
敵に対して何を解決するか：
失った場合の損失：
同じ資源の代替用途：
量産数：
Shift+Oを使うか：
F8で回収確認するTurn：
```

---

## 関連ページ

- [Magic Item総論](index.md)
- [Magic Path Booster](boosters.md)
- [Research Item](research-items.md)
- [Resistance・Utility Item](resistance-items.md)
- [Thug / Supercombatant装備](thug-equipment.md)
- [Magic Itemデータ索引](../data/items/index.md)
- [Gem economy](../magic/gems.md)
- [Research](../magic/research.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
