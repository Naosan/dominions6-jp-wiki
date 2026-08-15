---
title: 最初の戦争
page_type: guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-15"
---

# 最初の戦争

最初の対Player戦は、Armyを敵領へ動かしたTurnから始まるのではありません。

> **目的、情報、Research、Army、Gem、Siege、退却先を揃えた時点で始まっています。**

初戦争で最も多い失敗は、Field Battleに勝つ方法だけを考え、Fort攻略、増援、補給、敵の第二Armyを考えていないことです。

このページでは、特定国家のRush Buildではなく、どの国家でも使える戦争準備の型を扱います。

---

## 戦争を始める前の五つの問い

## 1. 何を取れば戦争目的を達成するか

目的は具体的なMap上の対象へします。

- Border Fort
- Capital
- Throne
- High-income地域
- Plane entrance
- 重要Magic Site
- 敵の主力Army
- 敵のMage生産拠点

「相手を弱らせる」では、どこで止まるか決まりません。

良い目的の例：

```text
Border Fortを取り、相手のRecruit-anywhere Mage生産を一拠点止める
```

```text
Throneと周辺二Provinceを確保し、Fortを建てて防衛線にする
```

```text
敵主力を自国Fort前で迎撃し、消耗後に反攻する
```

## 2. 何で主戦闘に勝つか

勝利条件を一文にします。

```text
盾兵で接敵を受け、Strength Buff後の高Damage兵で重装歩兵を破る
```

```text
Chaffで時間を作り、MageのAoE Spellで密集Squadを削る
```

```text
Shock Resistanceを展開し、敵Air Mageの主力Spellを無力化して通常兵で押す
```

この一文に対応するResearch、Mage、Gem、Squad、Scriptが揃っていなければ、戦争計画はまだ完成していません。

## 3. 敵は何でこちらを止めるか

自分の強みだけでなく、相手の最短Counterを考えます。

- ProtectionへAP・AN・Poison
- SacredへAnti-SacredとBless無効化
- Mage密集へAssassin、Raid、遠隔攻撃
- Elemental DamageへResistance
- MR攻撃へAntimagic・Mindless
- GiantへFatigue、Soul attack、Chaff
- ArcherへShield、Storm、Flank

Counterを一つ見たら終わるArmyではなく、第二のDamage typeまたは戦い方を用意します。

## 4. Field Battle後にFortを取れるか

Army戦に勝っても、壁を破れなければ敵生産は止まりません。

- Siege力
- Supply
- 敵Relief Army
- Storm用兵力
- Gem補給
- Reinforcementの距離
- 自軍後方のRaid対策

を確認します。

## 5. 負けた場合に何が残るか

全Armyを一戦へ賭けないようにします。

- Retreat Province
- 第二Commander
- Capital defence
- 後方Mage
- 予備Gem
- 次のResearch Breakpoint
- 外交上の退路

一戦の敗北が即国家崩壊になる構成は、勝率だけでなく損失の大きさが危険です。

---

## Intelligence Checklist

戦争準備はScoutから始まります。

### Map情報

- Fortの位置と種類
- Province接続
- Choke point
- Throne
- Lab・Temple
- Supplyの厳しい地形
- 敵の退却先
- 自軍の退却先

### Army情報

- 主力兵と装備
- Squad数とFormation
- Commander数
- Mage数
- SacredとBless
- Flying、Stealth、Sailing、Magic Phase movement
- Siege Unit

### Magic情報

- 敵国家のNative Path
- 既に見えたSpell
- Research Timingの推定
- Gemを持つCaster
- BoosterらしいItem
- Battlefield Enchantment
- Elemental Resistance
- MR攻撃

### 経済情報

- Fort数
- Capital-only依存
- 新設Fort
- Expansion速度
- Raidへ弱い後方

完全な情報は得られません。大切なのは、未知を既知のように扱わないことです。

```text
確認済み
推定
不明
```

の三段階に分けます。

---

## 開戦準備表

| 分野 | 最低限の確認 | 未完成なら起きること |
|---|---|---|
| 目的 | 取るFort・Throne・Armyが明確 | 勝っても戦争が終わらない |
| Scout | 敵主力と経路を一度以上確認 | 想定外のArmyへ正面衝突 |
| Research | 使用SpellとCasterが決定 | 研究済みでも誰も使えない |
| Army | 前衛・Damage・Commanderの役割 | 接敵順が崩れる |
| Script | Mage、Squad、Gemを確認 | AI任せで勝利条件が発動しない |
| Resistance | 敵主力Damageへの対策 | Army全体が一Damage typeで崩壊 |
| Siege | 壁を破る能力と時間 | Field Battle後に停滞 |
| Supply | 長期包囲を維持できる | Disease・Starvation・戦力低下 |
| Reinforcement | 次の兵とMageの到着経路 | 勝利後に前線が空になる |
| Retreat | 安全な自領へ逃げられる | Routが大量死へ変わる |
| Defence | 自国後方の最低限の守り | 主力前進中にRaidされる |

---

## 戦争計画を五文で書く

複雑な計画を作る前に、五文へ圧縮します。

```text
目的：Border Fortを取る。
敵主力：高Protection歩兵とAir Mage。
勝利条件：Shock Resistance後、高Damage兵で歩兵を破る。
進行：Scoutで主力位置を確認し、二方向のRaid後に本隊で包囲する。
撤退条件：Resistanceが間に合わない、または敵第二Armyが合流したら自国Fortへ戻る。
```

五文にできない場合、目的または手段が曖昧です。

---

## 開戦の段階

## 1. 接触前

- Scoutを先行
- Rally pointを決める
- GemとItemを移す
- CommanderへArmyを割り当てる
- 研究完了Turnを確認
- 敵へ見せたくないCasterを隠す
- 後方ProvinceのRaid対策を置く

この段階でArmyを一か所へ集めすぎると、開戦意図が見えます。逆に分散しすぎると、一Turnで集結できません。

## 2. Border戦

最初のProvinceを取ることより、敵主力の反応を見ることが重要です。

- どの方向へ集結するか
- Mageを何人出すか
- Raidを返してくるか
- Fortへ退くか
- 主力Spellを見せるか

小さな戦闘で情報を取れれば、本戦のRiskを下げられます。

## 3. Main Battle

Main Battleでは、兵数より**勝利条件の発動順**を確認します。

例：

```text
Screenが接敵
→ Buffが完了
→ Damage役が接敵
→ Mageが主力Spell
→ Enemy Commander / Mageを崩す
```

配置がずれると、Buff前に前衛が死ぬ、Damage役がScreenに詰まる、Mageが射撃を受ける、といった事故が起きます。

## 4. Siege

主戦闘に勝った直後が最も危険です。

- 自軍も損耗している
- Gemを使っている
- 敵はFort内で補充できる
- Relief Armyが近づく
- 後方がRaidされる

ためです。

Fortへ何人残し、誰が次のProvinceを取り、誰がGemを補給するかを決めます。

## 5. Stormまたは撤退

壁を破ったから即Stormする必要はありません。

- Defender
- Castle guard
- Mage Script
- Battlefield effect
- 自軍の疲労と補充
- Relief Armyの到着

を比較します。

目標Fortを取る価値より、Storm損失が高いなら包囲継続や別目標も選択肢です。

---

## Armyを役割へ分ける

## Screen / Line holder

最初に敵を受け、MageとDamage役の時間を作ります。

- Shield
- Protection
- Defence
- Morale
- Formation
- 数

を見ます。

## Damage dealer

敵の主防御を破ります。

- 高Damage
- AP・AN
- Multiple attacks
- Strength Buff
- Poison・Elemental
- MR攻撃

のどれを使うかを明確にします。

## Mage core

全Mageを同じScriptにしません。

- Resistance
- Army Buff
- Damage
- Summon / Chaff
- Control
- Battlefield Enchantment
- Emergency spell

へ役割分担します。

## Commander protection

Commander死亡は、Leadership、Script、Retreat、Magicを同時に失わせます。

- 後方配置
- Bodyguard
- Flank対策
- Archer対策
- Flying / Attack Rear対策

を用意します。

## Raider

Main Armyと別に、敵のIncome、Lab、Temple、Reinforcement routeを狙います。

ただし、Raid Unitを主戦闘から抜いた結果、本隊が負けるなら逆効果です。

## Siege / Logistics

戦闘能力が低くても、Siege、Supply、Gem輸送、Leadershipを担うUnitが戦争を終わらせます。

---

## Research Timing

Researchは「高いほどよい」のではなく、敵より先に機能する必要があります。

### 早く到達してもArmyがない

Spellを研究したが、Caster、Gem、前衛が足りません。

### Armyが揃っても研究が遅い

通常兵だけで敵のBuff・Evocation・Summonへ突入します。

### Researchを欲張る

複数Schoolを少しずつ上げ、どの勝利条件も完成しません。

戦争前は、第一Breakpointと第二Breakpointを分けます。

```text
第一：開戦に必要
第二：Counterを見た後に必要
```

詳しくは[Researchと研究ルート](../magic/research.md)を参照してください。

---

## GemとItem

Gemは「持たせた」だけでは計画になりません。

- 何Spell用か
- 何Battle分か
- AIが別Spellへ使う可能性
- Retreat時に失うRisk
- 補給Commander

を確認します。

Rare Boosterや大量Gemを一人へ集中させると、AssassinationやRoutで国家のMagic Accessごと失うことがあります。

---

## Retreatと敗北管理

戦闘前に、敗北したArmyがどこへ逃げるか確認します。

- 隣接する自領
- Fort
- Enemy control
- River・Mountain・Plane等の接続
- 包囲状態

退路がない戦闘では、Morale崩壊が通常以上に重い損失になります。

### 撤退条件を決める

- 敵主力が想定より大きい
- 必須Mageが到着しない
- Researchが一Turn遅れる
- Resistanceが不足
- 別Playerの介入
- 自国Capitalが脅かされる

撤退は失敗ではありません。戦争目的を達成できない条件でArmyを温存する判断です。

---

## よくある失敗

### 敵のProvinceを広く取るだけ

FortとArmyを壊しておらず、敵が再集結します。

### 主力ArmyをScoutなしで動かす

相手のCounter Armyへ正面から入ります。

### Mageを一種類のSpellへ統一する

Resistance一つでArmy全体が停止します。

### Field Battleだけを準備する

Siege、Supply、Stormで止まります。

### 勝利後に前進し続ける

Gem、補充、疲労、Commanderを確認せず、Relief Armyに負けます。

### 後方を空にする

Stealth、Flying、Raid、Magic Phase movementで生産地を失います。

### 一度の敗北で全編成を変える

原因が分からないままResearchと生産を捨てます。まず[Battle Replayの読み方](battle-replay.md)で最初の崩壊点を特定します。

### 戦争を終える条件がない

敵Capitalまで進むのか、Border Fortで止まるのか決まっておらず、第三国に利益を取られます。

---

## 戦争終了後

勝敗にかかわらず、次を整理します。

- 目的を達成したか
- 取ったFortを守れるか
- Army損失を何Turnで補充できるか
- 使用したGemとItem
- 敵が見せたCounter
- 次のResearch Breakpoint
- 第三国との国力差
- 休戦・追撃・撤退のどれを選ぶか

勝った戦争で国力を使い切り、第三国へ負けることもあります。領土獲得だけでなく、**戦後に残った生産力・Research・Mage・外交位置**で評価します。

---

## First War Plan Template

```text
敵国家：
戦争目的：
主要目標Province / Fort：
敵主力兵：
敵Mage / Path：
敵の想定Research：
自軍の勝利条件：
第一Research Breakpoint：
第二Research Breakpoint：
必要Mage：
必要Gem：
Main Army：
Raider：
Siege要員：
Rally point：
Retreat Province：
開戦条件：
撤退条件：
戦争終了条件：
```

---

## 関連ページ

- [最初の12ターン](first-12-turns.md)
- [序盤拡張](expansion.md)
- [Battle Replayの読み方](battle-replay.md)
- [命令とBattle Script](../basics/orders.md)
- [戦闘ルール](../basics/combat-rules.md)
- [Researchと研究ルート](../magic/research.md)
- [Forts](../systems/forts.md)
- [Magic Path Boosting](../magic/boosting.md)

## 主な参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
