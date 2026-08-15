---
title: 初心者ガイド
page_type: guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-15"
---

# 初心者ガイド

Dominions 6は、最初から全Unit・全Spell・全ルールを覚えて遊ぶゲームではありません。

最初のゲームで身につけたいのは、次の一周です。

> **偵察する → 編成する → 命令する → 戦う → Replayを見る → 一つ直す**

この一周を回せるようになれば、国家やMagic Pathが変わっても自分で学習を続けられます。

!!! note "このガイドの範囲"
    ここで示すのは、陸上の一般的な国家を使った初回プレイ向けの標準手順です。Awake Expander、Blood、Underwater、Undead、極端なSacred国家などは一部の優先順位が変わります。国家固有記事がある場合は、そちらを優先してください。

## 最初のゲーム設定

学習を目的にするなら、最初の一戦は複雑さを減らします。

- Vanillaで始め、MODは後回しにする
- 陸上国家を選ぶ
- AIの強さは標準以下でもよい
- Mapを極端に大きくしない
- 勝敗より、最初の戦争までの流れを一度経験する

最初からMultiplayerを遊んでも構いませんが、その場合は外交、時間制限、予測不能なCounterが加わります。まずSingle PlayerでArmy Setup、Research、Fort建設、Battle Replayを触っておくと理解しやすくなります。

---

## 学習ルート

次の順に読むと、国家選択から最初の戦争と敗戦分析まで一続きになります。

| 段階 | 読むページ | 解決する問い |
|---|---|---|
| 1 | [国家選択ガイド](../nations/choose-a-nation.md) | どの国家なら何を学びやすいか |
| 2 | [Pretender God](../pretender/index.md) | 国家に足りない役割をどう補うか |
| 3 | [最初の12ターン](first-12-turns.md) | 毎Turn何を確認し、何を準備するか |
| 4 | [序盤拡張](expansion.md) | Independent Provinceを低損失で取るにはどうするか |
| 5 | [Researchと研究ルート](../magic/research.md) | 最初の戦争へ何を研究するか |
| 6 | [Forts](../systems/forts.md) | 第二生産拠点をいつ、どこへ作るか |
| 7 | [最初の戦争](first-war.md) | 敵領へ入る前に何を揃えるか |
| 8 | [Battle Replayの読み方](battle-replay.md) | 勝敗を次の編成へどう変換するか |

補助として、[初心者向けTips](beginner-tips.md)、[命令とBattle Script](../basics/orders.md)、[戦闘ルール](../basics/combat-rules.md)を使います。

---

## 一Turnの基本手順

Dominionsでは、Turn終了前に全てを完璧にする必要はありません。代わりに、毎Turn同じ順で確認すると見落としが減ります。

### 1. Messageを読む

最初に、戦闘、Event、Site発見、建設完了、Commander死亡などを確認します。

重要なのは、結果だけでなく「前Turnに出したどの命令が、どう解決されたか」を結び付けることです。

### 2. Battle Replayを見る

勝った戦闘も見ます。

- 想定したSquadが最初に敵を受けたか
- Commanderが危険な位置にいなかったか
- 予定したSpellが発動したか
- 不要な損失が出ていないか
- RoutしたUnitがいないか

勝利は、Scriptが正しかった証明ではありません。相手が弱かっただけの場合もあります。

### 3. Strategic Mapを確認する

- 新しく見えたIndependentと敵領
- 空いたProvince
- 敵Armyの移動候補
- Fort、Throne、Choke point
- 自軍の退却先

を見ます。

### 4. Recruitを決める

兵士だけでなく、CommanderとMageの生産を確認します。

多くの国家では、Fort数とCommander Pointが将来のResearch量・Battle Mage数を決めます。目先の兵士を一体増やすために、毎Turn雇えるMageを止めていないかを確認します。

### 5. Researchを確認する

Research Schoolを漫然と均等に上げず、次のBreakpointを一つ決めます。

```text
誰が使うか
＋ 何を倒すか
＋ 何Gem必要か
＋ 何Turn頃に使うか
```

まで答えられる研究を優先します。

### 6. Army Setupと命令を確認する

- Squadの位置
- Formation
- Attack order
- Holdの有無
- Mage Script
- Gem
- Bodyguard
- Retreat route

を確認します。

「前Turnと同じだから大丈夫」ではなく、敵と地形が変わったらScriptも見直します。

### 7. Gold・Gem・建設を確認する

- 次TurnのMage雇用費
- 第二Fort資金
- Lab・Temple
- Gemを持たせるCaster
- Forge予定

を確認します。

GoldやGemを残すこと自体は失敗ではありません。目的なく眠らせることと、数Turn後の投資のために確保することを区別します。

### 8. End Turn前の最終確認

最後に、動いていないCommanderへ理由があるか確認します。

Research、Preach、Site Search、Build、Forge、Patrol、Scout、Army移動など、何らかの役割を与えます。ただし、敵の攻撃を予測して意図的に待機することも立派な命令です。

---

## 最初のゲームの成功条件

初回プレイでは、勝利だけを成功条件にしません。次のうち複数を達成できれば、Wikiを使って自力で改善できる段階へ進んでいます。

- 二つ目のExpansion Armyを作った
- 第二Fortを建設し、Mage生産を増やした
- 最初のResearch Breakpointを目的付きで選んだ
- Squadごとに役割と命令を分けた
- Mageへ五つのScriptを設定した
- 敵のProtection、MR、Resistanceのいずれかを見てCounterを変えた
- 負けたBattle Replayから最初の崩壊原因を説明できた
- 次の戦闘で変更点を一つだけ試した

---

## 今は覚えなくてよいもの

最初から次を網羅する必要はありません。

- 全Spell名とResearch Level
- 全Pretender Chassis
- 全Item Recipe
- 全特殊能力の内部数式
- 全国家のMatchup
- Late-game Globalの細部

必要になったときにWikiで調べます。Dominionsの上達は暗記量だけでなく、**問題を正しい索引へ分解する能力**です。

---

## 困ったときの入口

| 症状 | 最初に確認するページ |
|---|---|
| Independentに毎回大損する | [序盤拡張](expansion.md) |
| 何をResearchすべきか分からない | [Researchと研究ルート](../magic/research.md) |
| Mageが予定したSpellを使わない | [命令とBattle Script](../basics/orders.md) |
| 重装兵を倒せない | [戦闘ルール](../basics/combat-rules.md) |
| Goldが足りず国力が伸びない | [Forts](../systems/forts.md) |
| 敵へ攻める時期が分からない | [最初の戦争](first-war.md) |
| 負けた理由を説明できない | [Battle Replayの読み方](battle-replay.md) |
| 国家のRosterを読めない | [国家ページの読み方](../nations/how-to-read.md) |

---

## 次に読む

まず[最初の12ターン](first-12-turns.md)を開き、実際のゲームと並べて使ってください。

## 主な参照先

- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
