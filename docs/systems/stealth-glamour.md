---
title: Stealth・Glamour・特殊作戦
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
---

# Stealth・Glamour・特殊作戦

DominionsのStealthは、単に「敵から見えない」能力ではありません。

> **敵が守るべき場所を増やし、Main Armyの進路を曖昧にし、情報差を戦力差へ変える仕組み**

です。

Glamour国家ではさらに、

- 戦略Map上の不確実性
- 高Defence・Illusion系の戦闘性能
- Glamour MagicによるLuck・Dream・Perception操作
- Stealthy CommanderとSacred Raider
- 敵Scout報告の不完全さ

を一つの作戦へ組み合わせます。

このページでは、[EA Vanheim — Age of Vanir](../nations/ea/vanheim.md)を主要例として、Stealth、Glamour、Patrol、Assassination、Raid、情報戦を整理します。

!!! warning "Glamourという語は三つの意味で使われる"
    `Glamour`という語は、Unitの特殊能力、Magic Path、Illusion・Dream系Spell群を指す場合があります。本文では文脈を分けます。正確な現在値・Spell効果・判定はUnit popup、Spell description、Map画面の`?`を優先してください。

---

## 最初に覚える十項目

| 項目 | 最初の理解 |
|---|---|
| Stealth | 敵Provinceへ通常移動とは別の形で潜入・移動する能力 |
| Sneak | Stealthy Commanderが敵に見つからないよう移動するOrder |
| Glamour trait | Unitの知覚・Illusion系防御に関係する特殊能力 |
| Glamour Path | Dream、Luck、Illusion、Mind、Perceptionを扱うMagic Path |
| Patrol | Stealth Unitを発見し、Unrestも下げるOrder |
| Spy | 情報取得やUnrest操作を得意とするStealth Commander |
| Assassin | Movement前後の特殊Timingで敵Commanderを狙う能力 |
| Raider | 小規模部隊で後方Province・Tax route・Labを脅かす役割 |
| Scout report | 敵Armyの全構成を常に正確に表示するものではない |
| True Sight等 | Glamour・Illusion系の防御へ対抗する重要能力 |

---

# 三つのLayerを分ける

## 1. Strategic Stealth

Map上で、

- 敵領へ潜入する
- Armyの存在を隠す
- Scout・Spyを送る
- Raidの出発点を隠す
- 複数方向から同時に現れる

ためのLayerです。

これはBattle中のDefenceやIllusionとは別です。

## 2. UnitのGlamour

Glamoured Unitは、通常の人間兵とは異なる知覚・Illusion系の防御を持ちます。

ただし、

```text
Glamourを持つ
≠
すべての攻撃を回避する
≠
True Sight以外には無敵
≠
MR attackやAoEにも強い
```

ではありません。

敵の、

- True Sight
- Mindless
- AoE
- Magic Weapon
- MR attack
- Fatigue
- Poison・Elemental damage

を確認します。

## 3. Glamour Magic

Glamour Pathは、Dominions 6で独立したMagic Pathです。

主な役割は、

- Luck・Fortune
- Illusion
- Dream
- Perception
- Mind・Moraleへの干渉
- Battlefield control
- Stealth・偵察支援
- Glamour Gemを使うRitual・Item

です。

Path記事は[Magic Path: Glamour](../magic/paths/glamour.md)を参照してください。

---

# Stealth値をどう読むか

Stealth値は高いほど発見されにくくなりますが、結果はStealth値だけでは決まりません。

見るものは、

```text
Stealth側
- CommanderのStealth
- 同行UnitのStealth
- Army size
- 特殊能力・Spell・Item
- 移動Order

Detection側
- Patrol人数
- Patrol Bonus
- Province Defence
- Scout・Spy
- Fort・Temple等の重要度
- Event・Spell
```

です。

## Army全体は最も弱い構成要素に影響される

Stealthy Commanderへ通常兵を混ぜると、Army全体が意図どおり潜伏できない場合があります。

出発前に、

- Commander
- 全Squad
- Bodyguard
- Summon
- Slave
- Escort
- Mount
- Magic Being

のStealth表示を確認します。

```text
Stealth Commander
＋ 非Stealth兵
＝ Stealth Armyとは限らない
```

です。

## Scout reportと実数

敵Scout報告は、Stealth、Glamour、Obfuscation、情報不足等により不完全になる場合があります。

報告を見るときは、

```text
見えているArmy
＋
見えていないStealth Army
＋
到着予定Army
＋
Magic Phase移動
```

を仮定します。

---

# Sneakと通常移動

## 通常Move

敵Provinceへ通常Moveすると、通常の侵攻として扱われます。

## Sneak

Stealthy CommanderはSneakで敵Provinceへ移動できます。

Sneakは、

- Provinceを占領しない
- 敵Armyと通常Battleを起こさない
- 発見された場合は危険
- 次TurnのRaid・Assassination・情報取得の準備になる

という性質を持ちます。

!!! note "現在画面のOrderを優先"
    Unit・Commanderによって使用可能Orderが異なります。Map画面でCommanderを選び、`?`とOrder一覧を確認してください。

## 潜入後に何をするか

潜入は目的ではありません。

```text
潜入
→ Scout
→ Spy
→ Assassination
→ Raid
→ Attack Current Province
→ Temple・Labへの圧力
→ Main Armyのための情報取得
```

へ接続します。

「潜入できたが、何Turnも何もしない」なら、そのCommander turnをResearch・Site Search・Army supportへ使う方がよい場合があります。

---

# Stealth Raiderの設計

Stealth Raiderは、Main Armyの小型版ではありません。

## 役割

- 低PD Provinceを取る
- Tax routeを切る
- Lab・Templeを脅かす
- Scoutを排除する
- Fort建設を止める
- 敵Reserveを後退させる
- Retreat routeを切る
- Main Armyの進行方向を隠す

ための部隊です。

## 最小構成

```text
Stealth Commander
＋ PDを抜ける最小兵数
＋ 必要ならPriest / Mage
＋ 安全な退却先
```

です。

兵を増やすほどBattleには強くなりますが、

- 発見されやすくなる
- Supplyを使う
- Main Armyが弱くなる
- 一度の迎撃で損失が増える

という代償があります。

## Targetの選び方

Province Incomeだけを見ません。

優先度が高いものは、

- Tax route中継
- Border Lab
- Temple
- Fort建設中
- Throneの隣接
- Cave・Sea・Plane入口
- 敵ArmyのRetreat route
- Mage輸送路
- Blood Hunt拠点

です。

## Raid後に保持するか

Raidの価値は永久占領だけではありません。

```text
一Turn占領
→ Income停止
→ Recruit停止
→ Commander移動を強制
→ Main Armyを分割
```

でも十分な場合があります。

保持できないProvinceへ高価なStealth Sacredを残し続けないでください。

---

# 正面ArmyとStealth Army

Glamour国家では、すべてをStealthへ寄せると失敗しやすくなります。

## 正面Armyの仕事

- Fortを包囲する
- Throneを守る
- 敵Main Armyを拘束する
- Relief Armyを止める
- SupplyとGemを集約する

## Stealth Armyの仕事

- Mapの別方向へ圧力をかける
- 敵Reserveを引き離す
- 情報を取る
- 戦場を選ぶ
- Main Armyの進行を隠す

```text
正面Armyが敵を固定
＋
Stealth Armyが後方へ入る
```

ことで価値が増します。

Stealth Armyだけが多数いても、敵Main Armyを止める場所がなければ、CapitalやThroneを直接失うことがあります。

---

# Glamour兵の戦闘

## Defenceだけを見ない

高Defence兵は通常攻撃へ強い一方、

- Harassment
- 多数攻撃
- AoE
- Fatigue
- Entangle・Web
- MR attack
- True Sight
- Mindless attacker

で崩れます。

Battle Replayでは、

```text
最初は回避している
→ 接敵人数が増える
→ HarassmentでDefence低下
→ Fatigue蓄積
→ 急に被弾が増える
```

流れを確認します。

## ProtectionとHP

Glamoured Elf系兵は、Defenceが高くてもHP・ProtectionがGiantほど高いとは限りません。

一度当たった攻撃が重い場合があります。

```text
当てさせない防御
＋
当たった後の防御
```

を分けて評価します。

## Magic WeaponとTrue Sight

敵がMagic WeaponやTrue Sightを用意した場合、Glamourの一部Layerが弱くなる可能性があります。

そのときは、

- 通常兵
- Shield兵
- Summon
- Elemental Resistance
- MR
- Fatigue攻撃
- Raid

へ戦い方を切り替えます。

---

# Glamour Magicの運用

## 何を解決するか先に書く

```text
Spell：
Research：
Caster：
Gem：
Target：
解決する問題：
Counterされた場合：
```

を決めます。

Glamourは選択肢が多いため、

> Glamour Spellを使いたい

だけではResearch計画になりません。

## Army support

Glamour Mageは、

- Luck
- Defence
- Illusion
- Morale
- Perception
- Enemy control

を担当できます。

しかし高価なStealth Mageを前線へ出すと、

- Research
- Site Search
- Ritual
- Raid command
- Sacred leadership

を同時に失うRiskがあります。

## Ritual

Glamour Ritualは、

- 情報
- Dream
- Stealth
- Remote influence
- Summon
- Global

へ広がります。

正確なSpell、Research、Range、Gemは[Spellデータ](../data/spells/by-path/glamour.md)を確認してください。

---

# PatrolとCounter-Stealth

## Patrolの二つの役割

Patrolは、

1. Unrestを下げる
2. Stealth Unitを発見する

Orderです。

Blood Hunt拠点やBorder Fortでは両方が重要です。

## Patrol網

すべてのProvinceへ大量兵を置く必要はありません。

```text
Scout
→ 侵入方向を推測

Choke point
→ Patrol

重要Fort
→ Patrol Bonus Unit

後方
→ Mobile Reserve
```

とします。

## PDだけに任せない

高PDでも、Stealth Commanderの発見、Assassin対策、強いRaider迎撃を完全には保証しません。

```text
PD
＋ Patrol
＋ Scout
＋ Reserve
＋ Fort
```

を組み合わせます。

## Patrolしすぎる代償

PatrolはPopulationへ損害を与える場合があります。

Blood Provinceや高Income Provinceでは、

```text
Stealth対策
→ Population損失
→ 将来Income低下
```

を確認します。

---

# AssassinとBodyguard

## Assassinの目的

Assassinは、敵Commanderを一人ずつ減らし、

- Leadership
- Priest
- Communion Master
- Rare Path
- Gem carrier
- Siege commander

をArmyから切り離します。

Battleに勝つだけでなく、

> 敵が安全に前進できない状態

を作ります。

## Target

優先度は、

1. Rare Path holder
2. Communion / Sabbathの要
3. Prophet・高位Priest
4. Army Commander
5. Gem carrier
6. Scout・Spy

です。

## Bodyguard

重要CommanderにはBodyguardを付けます。

ただしBodyguardは、

- Assassinの種類
- AoE
- Poison
- Fear
- Ethereal
- Seduction

により有効性が変わります。

ReplayとUnit popupを確認します。

---

# SailingとStealth

Sailingは海・River・Coastを使って移動経路を変える戦略能力です。

Stealthと組み合わさると、

```text
敵が陸路だけを警戒
→ Coastを越えてStealth Armyが出現
```

という情報差を作れます。

ただし、

- CommanderのSailing能力
- 同行兵のSize・人数制限
- 出発・到着Province
- Sea・River接続
- 敵所有権
- Map固有接続

を確認します。

Sailingは瞬間移動ではなく、到着先で通常Battleを起こすMovementです。

---

# Magic Phase移動との違い

Stealth・Sailing・Flyingは通常Movementの経路を変える能力です。

Teleport等のMagic Phase移動は別Timingです。

```text
Magic Phase Battle
→ 通常Movement
→ 通常Field Battle
```

となる場合があるため、

> Teleport MageとStealth Armyが同じProvinceへ向かった

だけでは同じBattleになるとは限りません。

詳細は[ターン処理順](../reference/turn-resolution.md)を参照してください。

---

# 敵がStealth国家の場合

## 最初に守る場所

- Capital
- Mage Fort
- Throne
- Tax route
- Lab・Temple
- Retreat route
- Blood Hunt拠点
- Cave・Sea・Plane入口

です。

低Incomeの袋小路を全部守ろうとすると、Main Armyが分散します。

## Raiderを追わない

敵Raiderの現在地だけを追うと、同時移動ですれ違います。

守るべき場所へ先回りします。

## Enemy planを読む

Stealth国家は、見えているArmyより、

```text
何を隠したいか
```

を見るべきです。

- Fortを狙う準備
- Main Armyの移動
- Blood Sacrifice拠点
- Gem carrier
- Throne rush

を推測します。

---

# Battle Replayで見るもの

```text
Glamourが残っていたRound：
True Sight持ちの敵：
最初に命中した攻撃：
Harassment：
Fatigue：
AoE：
MR check：
Rout開始：
Commander死亡：
```

Stealth作戦はMap上では成功していても、Battleで高価なRaiderを毎回失えば持続しません。

---

# よくある失敗

## 1. すべての兵をStealth Armyへ入れる

Fort・Throneを守る正面Armyがなくなります。

## 2. 高Defenceを無敵と考える

AoE、Fatigue、MR attack、True Sightへ崩れます。

## 3. Raiderを大きくしすぎる

発見・迎撃時の損失が増えます。

## 4. 潜入後の目的がない

Commander turnを失います。

## 5. Scout reportを完全情報と思う

Stealth Army、Magic Phase、到着予定Armyを見落とします。

## 6. AssassinへRare Mageを無防備にする

Bodyguard、Fort、分散を使います。

## 7. Raidと決戦を同じ評価軸で見る

RaidはProvince保持より、敵の行動を強制した価値で評価します。

---

# Test checklist

```text
[ ] Stealth Armyへ非Stealth Unitが混ざっていない
[ ] Raiderの最低勝利条件をPD別にTestした
[ ] Retreat先がある
[ ] Main ArmyとRaiderの役割を分けた
[ ] Scout reportが不完全である前提を持った
[ ] True Sight・Mindless・AoEへの第二案がある
[ ] Patrol拠点を重要Provinceへ絞った
[ ] Rare MageへBodyguardを付けた
[ ] Sailing・Flying・Magic Phaseを別Timingとして扱った
[ ] Raid成功をIncomeだけでなく敵移動で評価した
```

---

# 関連ページ

- [EA Vanheim — Age of Vanir](../nations/ea/vanheim.md)
- [EA Ulm — Enigma of Steel](../nations/ea/ulm.md)
- [Magic Path: Glamour](../magic/paths/glamour.md)
- [命令とBattle Script](../basics/orders.md)
- [最初の戦争・外交・Raid・迎撃Q&A](../getting-started/war-faq.md)
- [ターン処理順](../reference/turn-resolution.md)
- [特殊能力](../reference/special-abilities.md)
