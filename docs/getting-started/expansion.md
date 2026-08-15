---
title: 序盤拡張
page_type: guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-15"
---

# 序盤拡張

序盤拡張（Expansion）は、Independent Provinceを占領してGold、Resources、Population、移動経路、Fort候補を増やす段階です。

ただし目的は、最短TurnでProvince数だけを増やすことではありません。

> **補充可能な損失で領土を増やし、次のExpansion Armyと第二Fortを作れる状態を維持すること**

が本当の目的です。

一戦ごとに主力兵とCommanderを失い、Capitalで補充待ちになるなら、Provinceを取っていても成長は止まります。

---

## Expansionの判断式

攻撃前に、次の四つを比較します。

```text
得られるもの
－ 予想損失
－ 次Turnの移動制約
－ 失敗時の損害
```

得られるものはIncomeだけではありません。

- 次のProvinceへの接続
- Choke point
- High Resource
- Fort候補
- Throneへの接近
- 敵Playerより先に確保する境界
- Retreat route

も価値です。

---

## 六段階のExpansion Cycle

## 1. Armyの役割を一文にする

最初に、自軍がどう勝つArmyなのかを書きます。

```text
盾兵で射撃と接敵を受け、高Damage歩兵で敵前衛を削る
```

```text
Sacred cavalryがBless後に一気に接敵し、短時間でRoutさせる
```

```text
Awake Pretenderが通常攻撃を受け止め、Fearと高Damageで崩す
```

役割を説明できないArmyは、配置と補充方針も曖昧になりやすくなります。

## 2. Independentの種類を見る

人数だけで判断しません。

- WeaponとDamage
- Shield
- Protection
- Missile weapon
- Cavalry・Lance
- Size・Trample
- Morale
- Poison・Elemental Damage
- Undead・Demon・Magic Being

を見ます。

偵察情報が足りない場合、Scoutを送る、一Turn待つ、別Provinceへ向かう、より強いArmyを使う、という選択があります。

## 3. 相性を確認する

自軍の攻撃が敵のどの防御層を破るかを考えます。

- 高Protectionへ十分なDamageがあるか
- Shield持ちへ射撃だけで戦おうとしていないか
- 高Defenceへ命中できるか
- PoisonへResistanceがあるか
- Large Unitへ止める手段があるか
- UndeadへPriestや適切なLeadershipがあるか

詳しい防御層は[戦闘ルール](../basics/combat-rules.md)を参照してください。

## 4. 配置と命令を作る

最低限、次を決めます。

- 誰が最初に敵を受けるか
- Damage役がどの敵を狙うか
- Archerがいつ射撃を止めるか
- Commanderをどこへ置くか
- Holdを使うか
- Retreat routeがあるか

同じ兵数でも、前衛とDamage役を混ぜるか分けるかで結果が変わります。

## 5. 損失上限を決める

攻撃前に、失ってよいものと失ってはいけないものを分けます。

### 比較的補充しやすい

- Recruit-anywhereの安価な兵
- 役割を代替できるCommander
- 数Turnで補充可能なChaff

### 失うとExpansion全体が止まりやすい

- 初期Commander
- Rare Mage
- Capital-only Sacred
- Awake Pretender
- Boosterや大量Gemを持つCaster
- 第二Armyを率いる予定のCommander

勝利しても、交換不能なUnitを失ったなら高い勝利です。

## 6. Replayから一つだけ変更する

戦闘後は、全編成を一度に変えません。

- 盾兵を前へ出す
- Damage役を一Squad増やす
- Holdを一回入れる
- Archerの目標を変える
- Commanderを後ろへ下げる

など、一つ変更し、次の結果と比較します。

---

## Independent別の危険信号

次の表は絶対的な強弱表ではありません。同じ名称でも装備や数が異なるため、偵察とReplayを優先してください。

| 相手の特徴 | 主な危険 | 基本的な考え方 | Replayで見るもの |
|---|---|---|---|
| Bow・Sling中心 | 接敵前の損失、Commander被弾 | Shield、散開、素早い接敵、Commander保護 | 誰が射撃を受けたか |
| Crossbow・高威力射撃 | 重装でも大きな損失 | Shield、射線妨害、Flank、短期決着 | Protectionを抜かれたDamage |
| Heavy Infantry | 低Damage攻撃が通らず長期戦 | 高Damage、AP・AN、Strength、Fatigue戦 | 敵HPが減らない原因 |
| Cavalry・Lance | 初回接敵の高Damage | Screen、十分な前衛、Charge後を狙う | 最初の一撃で崩れた場所 |
| Barbarian・高Damage歩兵 | Protectionを越える大打撃 | 射撃、先制、数、短期決着 | 一撃死とRout開始Round |
| Elephant・大型Trampler | Trample、隊列崩壊、Morale | 深さ、Size、集中Damage、逃走時の混乱 | 前衛が押し潰された経路 |
| 高Defence兵 | 攻撃が当たらず消耗 | Attack skill、複数攻撃、拘束、疲労 | Missが続くか |
| Undead | 通常Moraleと異なる挙動、Holy弱点 | Priest、Holy、Undead対策、Leadership | Commander・Leadershipの問題 |
| Poison・毒獣 | 戦闘後も損害が増える | Poison Resistance、遠隔処理、短期戦 | 緑Damageと戦闘後死亡 |
| Amphibious・水域 | 移動可能Unitと装備制限 | 海へ入れる構成を別に用意 | 戦える形態・移動条件 |

---

## Expansion Armyの代表形

## 盾兵＋Damage役

最も理解しやすい構成です。

- 盾兵：射撃と最初の接敵を受ける
- Damage役：高Strength、高Damage、長武器、複数攻撃等で敵を倒す
- Commander：後方でLeadershipを維持する

弱点は、盾兵とDamage役が同時に疲れ、長期戦へ入ることです。

## Archer中心

接敵前に敵を減らします。

- 軽装・密集した敵へ強い
- 高Protection・Shieldへ効率が落ちる
- Friendly Fireが起こる
- Commanderが射線に入る

という特徴があります。

敵が接敵した後も射撃を続けるか、Attack orderへ切り替えるかを考えます。

## Cavalry・高機動

短時間で接敵し、FlankまたはChargeを利用します。

初撃後の継続Damage、Mountを失った後の性能、補充Costまで見ます。最初のChargeだけで敵を崩せない相手へは損失が増えます。

## Sacred Expansion

Bless込みで評価します。

- ProphetまたはPriestが間に合うか
- Bless前に接敵しないか
- Sacredの補充速度
- Capital-onlyか
- Incarnate Blessが有効か

を確認します。

強力でも、少数しか補充できないSacredを毎戦失うと中盤の主力が消えます。

## Awake Expander

Pretender本人でProvinceを取ります。

- Fatigue
- Poison
- Elemental Damage
- Magic Weapon
- Affliction
- Retreat route
- Dominion依存

を毎戦確認します。

一度勝った構成でもDRNや敵種類で事故が起こります。同じIndependent類型へ複数回Testし、HPとFatigueに余裕があるかを見ます。

## Mage支援Expansion

低Level Buff、Summon、Evocation等を早期に使う構成です。

Mageを前線へ出すことでResearchが減るため、得られる低損失Expansionと比較します。Gemを使う場合は、そのProvinceの価値とGem消費も記録します。

---

## 第二・第三Expansion Army

Expansion速度は、一Armyの強さだけでなく、独立して安全に動けるArmy数で決まります。

第二Armyを作るときは、次を揃えます。

- Commander
- 必要Leadership
- 前衛
- Damage役
- PriestまたはMage
- 補充経路
- 安全な標的

第一Armyから兵を分ける場合、両方が不完全にならないようにします。

### 良い分割

- 一方はArcherへ強い盾中心
- 一方はHeavy Infantryへ強い高Damage中心
- Pretenderは危険標的、国家兵は安全標的

### 悪い分割

- Commanderだけ増やし、どちらも敵を倒せない
- Bless役が一人しかいないのにSacredを二分する
- 退路を考えず反対方向へ伸ばす
- 補充不能な精鋭を両Armyで少しずつ失う

---

## Provinceの選び方

## Income

Mageと兵士を雇うGoldを増やします。ただし高Incomeだけを追い、地理的に孤立すると守りにくくなります。

## Resources

重装兵や高Resource兵を生産するFort候補になります。

## 接続

次のExpansion先、Choke point、敵との境界を決めます。弱いProvinceでも重要な橋になる場合があります。

## Terrain

Movement、Supply、Fort、Magic Site、国家能力へ影響します。

## Throne

勝利条件と効果を持ちますが、守備が通常Independentより強いことがあります。序盤に無理に攻める必要はありません。

## Retreat route

負けたときに自領へ逃げられるかを見ます。敵領に囲まれたProvinceへの攻撃は、Routが全滅へ変わりやすくなります。

---

## いつExpansionを止めるか

Independentが残っていても、次の状況では集結を優先します。

- 敵Playerが近い
- Border Fortが建ち始めた
- 主力Armyが分散している
- 最初のResearch Breakpointへ到達した
- Expansion先が高Riskだけになった
- 敵のRushが見えた
- ThroneやChoke pointを守る必要がある

Expansionを続けることと、戦争準備を遅らせることは同じではありません。安全な後方Expansionは継続しつつ、前線Armyだけを集める選択もあります。

---

## よくある失敗

### 人数だけで攻撃先を選ぶ

少数CavalryやBarbarianが、多数の軽歩兵より危険な場合があります。

### 勝ったので同じArmyで連戦する

損失、Affliction、Commander、次の敵構成を見ていません。

### Commanderを前へ置く

Armyは残っているのにLeadershipを失い、Routまたは行動不能になります。

### 全Unitを一Squadにする

盾、Damage、射撃、Flankの役割が混ざり、狙った接敵順になりません。

### Capital-only Unitを消耗品として使う

補充上限があり、第一戦争までに数が戻りません。

### Province数だけを競う

Fort、Mage、Researchへ変換できず、広いだけの国家になります。

### 負けたArmyを同じ相手へ送り直す

原因を変えず、補充兵だけを追加しています。

---

## Expansion記録Template

```text
Turn：
攻撃Province：
Independentの種類・推定数：
自軍構成：
配置・命令：
勝敗：
主な損失：
最初に崩れた場所：
Damage type：
Routの有無：
次回変えること一つ：
```

数戦分を残すと、その国家で安全な標的と危険な標的が見えてきます。

---

## 関連ページ

- [最初の12ターン](first-12-turns.md)
- [最初の戦争](first-war.md)
- [Battle Replayの読み方](battle-replay.md)
- [命令とBattle Script](../basics/orders.md)
- [戦闘ルール](../basics/combat-rules.md)
- [国家ページの読み方](../nations/how-to-read.md)
- [Unit装備・Mountの読み方](../data/unit-loadouts.md)

## 主な参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
