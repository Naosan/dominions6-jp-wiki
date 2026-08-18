---
title: MA Caelum
page_type: nation-guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-19"
nation_id: 71
era: "MA"
epithet: "Reign of the Seraphim"
---

# MA Caelum — Reign of the Seraphim

MA Caelumは、**Flying Unitを広い範囲から集中し、Air・Water・Stormで射撃と戦場条件を制御する国家**です。

国家の中心は、

> **多くのFlying兵**
> ＋ **Ice weapon・Ice armor**
> ＋ **A3W2H2まで保証されるHigh Seraph**
> ＋ **Archer・Lance・Heavy Ice Infantry・MammothのCombined Arms**
> ＋ **StormとAir Magicによる戦場再設定**

です。

CaelumはMap上で速く、山・森・River等を越えて局地的多数を作れます。しかし、

- 多くの兵が低HP
- 軽装兵は射撃・AoEで減る
- Stormは自軍飛行・射撃も止め得る
- MammothはMorale・MR・Controlに弱い
- High SeraphがSlow recruitment
- Earth・Nature・Glamour・Bloodが不足

という制約があります。

> **Caelumの強さは「全部飛べること」ではなく、「敵より一Turn早く、必要なBattleへ必要な役割を集めること」です。**

- [自動生成Recruitデータ](../../data/recruitment/ma/caelum.md)
- [国家別Site Search能力](../../data/site-search/ma/caelum.md)
- [Extended Magic Access](../../data/extended-magic-access/ma/caelum.md)
- [Magic Access Route](../../data/magic-access-routes/ma/caelum.md)
- [Flying・Storm・Air機動戦](../../systems/flying-storm.md)
- [Pretender設計サンプル](../../pretender/samples.md)

!!! note "このページの精度範囲"
    本文はDominions 6.35の固定データ、ゲーム内Nation・Unit・Spell・Item表示、公式Documentation、現行Inspector、現行Community資料を照合し、実戦判断へ再構成しています。Ice armor、Temperature、Storm、Mount、Flying、Random Path、National Summon、Patch、MODには例外があります。正確なCost・Protection・Path・Spellはゲーム内表示と上記自動生成データを優先してください。

!!! warning "Mammoth RiderとFlying"
    RecruitデータのRider側にFlying属性が表示される場合がありますが、Dominions 6ではRiderとMountが別Statsです。Mammothを含むArmyのStrategic Move・Battle moveはMap ArrowとUnit詳細を正本にしてください。

---

# 一言でいうと

```text
Flying兵でExpansion
→ Fortを広い範囲へ配置
→ High Seraphを継続生産
→ Archer・Lance・Iceclad・Mammothを役割分担
→ Air・Waterで敵射撃と高Protectionへ回答
→ Flying Armyを一つのBattleへ集中
→ Stormあり・なしを敵別に切り替える
```

国家です。

Caelumでよくある誤解は、

```text
Flyingだから敵後方へAttack Rearすれば勝てる
```

です。

実際には、

```text
後方へ飛ぶ
→ Bodyguard・Rear guardへ孤立
→ 軽装兵が集中攻撃
→ Rout
```

が起こります。

FlyingはTargetとTimingを設計して初めて強くなります。

---

# 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | Middle Age |
| Nation ID | 71 |
| Epithet | Reign of the Seraphim |
| Preferred Temperature | Cold寄り |
| 軍事の中心 | Flying infantry、Archer、Storm Guard、Iceclad、Mammoth |
| 保証Magic | A3、W2、H2 |
| Random Magic | High SeraphのA/W/S/D、SeraphineのFire |
| Mage | Spire Horn Seraph、Ice Crafter、Caelian Seraph、Seraphine、High Seraph |
| 戦略能力 | Flying、高Map Move、Mountain network、Air・Water Magic |
| 操作量 | 中～高。Army集中、Storm、Random Mage、射撃・飛行Timing |
| 主な弱点 | 低HP、射撃、AoE、Fire・Heat、MR、Morale、Missing Path |

## Recruit概要

### Any-fort Mage

```text
Spire Horn Seraph  A1
Ice Crafter        W1
Caelian Seraph     A2 W1
Seraphine          H1 + 20% F1
High Seraph        A3 W2 H2 + A/W/S/D Random
```

High SeraphはSlow to recruitです。

### Troop

```text
Spire Horn Militia
Spire Horn Warrior
Spire Horn Archer
Storm Guard
Airya Light Infantry
Airya Infantry
Iceclad
Mammoth Rider
```

---

# 国家エンジン

```text
Flying Expansionで地形を越える
        ↓
Fort候補とMountain・Cold適地を確保
        ↓
複数FortからMage・兵を生産
        ↓
Flying Armyを必要戦線へ集中
        ↓
Air・Water・StormでBattle条件を設定
        ↓
Mammoth・Lance・Archer・Mageで役割分担
        ↓
Fort・Throneを取り、次の集中拠点を増やす
```

止まりやすい場所は、

1. 軽装兵をExpansionで失い続ける
2. High SeraphのSlow recruitmentを考えず戦場へ使い潰す
3. Flying Raidへ偏り、Siege・Fort攻略が遅れる
4. Stormで自軍計画まで壊す
5. Air damageだけへ寄せ、Shock Resistanceで止まる

です。

---

# 強み

## 1. Strategic Flying

多くの兵・CommanderがFlyingを持ちます。

- 山越え
- River越え
- 広域集中
- Raid
- Fort relief
- Retreat route切断
- Mage輸送

へ使えます。

## 2. A3W2H2 High Seraph

High Seraphは保証A3W2H2を持ち、さらにA/W/S/D Randomがあります。

一体で、

- Air battlefield
- Water support
- Priest・Holy support
- Elemental
- Storm
- Site Search
- Booster route
- Random crosspath

へ入れます。

## 3. AirとWaterの組合せ

Airは、

- Lightning
- Wind
- Storm
- Defence
- Projectile control

Waterは、

- Cold
- Quickness
- Elemental
- Fatigue
- Water Booster

を提供します。

## 4. Magic Ice weapon

多くのIce weaponはMagic Weaponです。

- Ethereal
- Magic Being
- 一部特殊防御

へ通常鉄武器より対応しやすくなります。

## 5. Archer・Lance・Heavy兵・Mammoth

単一兵種国家ではありません。

- Archer：射撃
- Lance：Charge
- Storm Guard / Iceclad：重前衛
- Mammoth：Trample
- Mage：Air・Water

を組み合わせます。

---

# 弱み

## 1. 低HP

多くのCaelianはHPが低く、一度当たると死にやすいです。

## 2. 射撃・AoE

Flying・軽装兵は射撃とAoEで数を減らします。

## 3. Stormの両刃

Stormは敵Flying・Archerを止めますが、自軍にも影響します。

## 4. Fire・Heat

Ice armor・Cold適性を持つ国家として、Fire・Heatへ警戒します。

正確なResistanceはUnitごとに確認します。

## 5. High Seraph供給

Slow recruitmentにより、Fort数を増やしても同じ速度で量産できるとは限りません。

## 6. Missing Path

Earth、Nature、Glamour、Bloodが自然には不足します。

Astral・DeathもRandom依存です。

---

# 兵士

# Spire Horn Militia

安価なFlying兵です。

役割は、

- Siege補助
- Patrol
- Chaff
- Arrow受け
- Raider数調整

です。

低Morale・低Combat statsを考慮します。

---

# Spire Horn Warrior

Ice Lance、Shield、Flyingを持ちます。

- Charge
- Screen
- Flying flank
- Expansion

へ使えます。

Leather armorのため、重い射撃・AoEへ弱いです。

---

# Spire Horn Archer

Short BowとFlyingを持つArcherです。

役割は、

- 地形を越える射撃支援
- Raid
- 軽装兵処理
- Flying Armyへの同行

です。

Stormを自軍で使うと射撃計画が弱くなる場合があります。

---

# Storm Guard

Ice Lance、Ice Cuirass、Ice Aegisを持つ重装Flying infantryです。

- 前衛
- Charge
- Archer保護
- Storm計画
- 重要Battle

へ使います。

高価な場合は、全ArmyをStorm Guardだけにせず、安価な兵を混ぜます。

---

# Airya Light Infantry

Ice Lance、Shield、Ice armorを持つFlying兵です。

ChargeとScreenの中間です。

---

# Airya Infantry

Ice Blade、Shield、Ice armorを持つ近接兵です。

継続戦闘へ向きます。

---

# Iceclad

重いIce armorとShieldを持つ精鋭です。

低HPをProtectionで補います。

しかし、

- AP
- AN
- Fire
- Fatigue
- MR attack

へは別の回答が必要です。

---

# Mammoth Rider

Mammothは、

- 高HP
- Trample
- Size
- Mass damage

を提供します。

一方、

- Morale
- MR
- Control
- Friendly Trample
- 狭い地形
- Retreat

へ弱点があります。

MammothだけをExpansionへ送り、Routで大量損失しないようCommander、Formation、Targetを確認します。

---

# Commander

# Caelian Scout

Flying・Stealth Scoutです。

Caelumの機動力を活かすには情報が必要です。

- 敵Army
- PD
- Mage
- Archer
- Storm caster
- Shock Resistance
- Retreat route

を確認します。

---

# Storm General

Flying Army Commanderです。

高Leadershipで広い範囲から兵を集めます。

MageをCommanderへ使わず、Storm Generalに通常兵を任せます。

---

# Airya Noble

重装Commanderです。

重要Flying Army、Bodyguard、Expansion Commanderへ使います。

---

# Spire Horn Seraph

A1 Mageです。

- Air support
- Research
- Low-level Air spell
- Site Search

へ使います。

量産しやすいA1を日常Battle Mageへ回し、High SeraphをRare roleへ残します。

---

# Ice Crafter

W1 Mageです。

- Water support
- Forge
- Site Search
- Cold・Quickness
- Research

へ使います。

Water Bracelet等のBooster routeを確認します。

---

# Caelian Seraph

A2W1です。

Caelumの量産可能なBattle Mage中核です。

- Air spell
- Water spell
- Crosspath
- Storm前後
- Elemental

へ使います。

---

# Seraphine

H1＋20% F1のSacred・Stealth・Flying Priestです。

- Bless
- Preach
- Fire Randomの保存
- Scout・Stealth
- Temple network

へ使います。

F1個体を通常Priestとして失わないでください。

---

# High Seraph

A3W2H2＋A/W/S/D Randomです。

## 分類

```text
A Random
W Random
S Random
D Random
Double Random
```

へ分類します。

## Role

- Storm caster
- Lightning
- Water battlefield
- Priest・Holy support
- Booster
- Summon
- Site Search
- Astral / Death bridge
- Global・Ritual

です。

## Slow recruitment

一Fort一Turnで増える通常Mageと同じ計算をしません。

High Seraphを戦場へ出すときは、

```text
死亡時に次個体が何Turn後か
```

を考えます。

---

# Expansion

## Flying infantry

弱いIndependentへはSpire Horn Warrior・Airya兵で取れます。

高Damage相手には低HPが危険です。

## Mammoth

大量小型兵へ強い一方、MoraleとControlを確認します。

## Archer

接敵前に削りますが、Friendly FireとAmmoを見ます。

## Heavy unit

Storm Guard・Icecladは損失を抑えますが、ResourceとGoldを使います。

---

# Independent別

## Archer

重装・Shieldを前へ置き、Flying軽兵を後ろへ置きます。

## Cavalry

Lance ChargeをShield・重装で受けます。

## Barbarian

高Damage一撃で低HP兵が死にます。

Mammoth、射撃、Mage supportを使います。

## Heavy Infantry

Mammoth、Lightning、Lance、Water supportを使います。

## Undead

Magic Ice weaponとPriestを使います。

## Elephant

Mammoth同士のTrample、Morale、Sizeを確認します。

---

# Expansion評価

```text
Province取得Turn：
Caelian損失：
Mammoth損失：
二軍完成：
High Seraph開始：
Fort資金：
```

Flyingで遠くへ取っても、補給・防衛できなければ過伸展です。

---

# Economy・Fort

## Fort network

Flying nationはFort間距離が広くても集中しやすいです。

Fortの役割：

- High Seraph生産
- Caelian Seraph量産
- Mountain・Cold Recruit
- Flying reserve
- Border relief
- Gem・Item受け渡し

## High Seraph bottleneck

Commander PointとSlow recruitmentを考え、Fortごとに、

```text
High Seraph
vs
Caelian Seraph
vs
Ice Crafter
vs
Commander
```

を決めます。

---

# Pretender

## 1. Imprisoned Scales

Flying兵だけでExpansionできる場合、

- Gold
- Productivity
- Cold
- Growth
- Magic

へ投資します。

## 2. Missing Path bridge

Earth、Nature、Glamour、Bloodを補います。

特に、

- Nature Resistance・Regeneration
- Earth Protection・Booster
- Glamour Luck・Illusion
- Blood late-game

を比較します。

## 3. Astral bridge

High SeraphのAstral Randomだけに依存せず、National SummonやGlobalへつなげます。

## 4. Awake Expander

危険なCapital周辺をPretenderで取り、Flying Armyを別方向へ回します。

---

# Research

## Alteration

- Quickness
- Defence
- Protection
- Elemental adaptation

## Evocation

- Lightning
- Air damage
- Water damage
- Shock pressure

## Enchantment

- Storm
- Arrow defence
- Resistance
- Battlefield effect

## Construction

- Air Booster
- Water Booster
- Resistance Item
- Research Item

## Conjuration

- Elemental
- National summon
- Mage summon
- Air Queen等

## Thaumaturgy

Astral・Death Randomを得た個体のMR attack・Utilityへ使います。

---

# Stormあり・なし

## Stormあり

向く場合：

- 敵Flyingを止める
- 敵Archerを弱める
- Storm Powerを使う
- Lightning plan
- 自軍Storm-immune中心

## Stormなし

向く場合：

- Attack Rear
- 自軍Archer
- Flying集中
- 敵にStorm advantage
- 短期Raid

## Scriptを二つ作る

```text
Plan A：No Storm
Plan B：Storm
```

を保存します。

---

# First war

```text
目的：
敵Archer：
敵Shock Resistance：
敵Flying：
Storm：
正面Army：
Raid Army：
High Seraph数：
Gem：
Retreat：
```

## Army構成

### Screen

Storm Guard、Iceclad、Shield infantry。

### Damage

Lance、Mammoth、Lightning、Elemental。

### Archer

Spire Horn Archer。

### Mage

Caelian Seraph量産、High Seraph中核。

### Reserve

Flying Commanderと兵を一歩後ろへ置きます。

---

# Battle Script

## Caelian Seraph

```text
必要Buff
Air / Water support
Damage
Damage
Hold / retreat
```

## High Seraph

```text
Storm判断
Battlefield spell
Army support
Damage / control
```

High Seraph一人へ全作戦を依存しません。

---

# Counter

## Archer

重装、Shield、Storm、Arrow defence、RaidでCaster・Archerを狙います。

## Fire・Heat

Resistance、Temperature、別兵種、Waterを使います。

## Shock Resistance

Lightning以外へ切り替えます。

- Lance
- Mammoth
- Water
- Cold
- MR attack
- Summon

## Storm

敵Stormで自軍Flyingが止まります。

地上戦用Formation・Scriptを準備します。

## AoE

低HP兵を分散し、Resistanceを使います。

## Morale

Mammothと軽兵のRoutを防ぎます。

## MR attack

High Seraph Random、Antimagic、Caster attackを使います。

---

# Magic Access

## 保証

- A3
- W2
- H2

## Random

High Seraphに、

- A
- W
- S
- D

が出ます。

SeraphineにF1が出ます。

## Booster

WaterはW5まで計画Routeがあります。

AirはRandom個体で高位へ届きます。

## Missing

- Earth
- Nature
- Glamour
- Blood

です。

## National Summon

Caelum系National Spellは、Astral、Fire、Death等の高Pathを要求する場合があります。

Pretenderで入口を用意するとLate-game Accessが大きく変わります。

---

# Strategic Magic

High Seraphは、

- Air Queen
- Sea King
- Hidden in Snow
- Revenant
- Bishop Fish
- National Yazad / Daeva系

への入口になり得ます。

ただしRandom・Booster・Pretenderが必要です。

[召喚・Global・遠隔Ritual](../../magic/strategic-rituals.md)も参照してください。

---

# Multiplayer

## 敵から見たCaelum

- どこへでもFlying concentration
- Archer・Mammoth
- Storm
- Lightning
- High Seraph Random
- Throne relief

を警戒されます。

## 見せる情報

- Border
- Stormの有無
- Formal agreement
- Coast・Mountain interest

## 隠す情報

- Reserve位置
- High Seraph Random
- Gem
- Magic Phase plan
- Raid route
- Pretender Missing Path

## 外交

広い接触面を持ちやすく、複数国から脅威と見られます。

「どこへでも飛べる」能力を乱用すると包囲されます。

---

# よくある失敗

## 1. 全部Attack Rear

後方へ孤立します。

## 2. Stormを自動Script

自軍Flying・Archerも止めます。

## 3. High Seraphを使い潰す

Slow recruitmentで補充できません。

## 4. MammothだけでExpansion

Morale・Controlで事故ります。

## 5. Flyingで過伸展

Fort・Supply・Retreatが追いつきません。

## 6. Lightningだけで戦う

Shock Resistanceで止まります。

## 7. RiderのFlyingだけを見る

MountとArmy全体を確認します。

---

# Test game

```text
Turn：
Expansion方向：
Flying route：
Caelian損失：
Mammoth損失：
第二Fort：
High Seraph数：
Random分類：
第一Research：
StormありBattle：
StormなしBattle：
First war reserve：
Missing Path：
```

---

# End Turn checklist

```text
[ ] Army全体が実際に飛べる
[ ] High Seraph Randomを分類した
[ ] Stormあり・なしを選んだ
[ ] ArcherとFlyingのTimingを合わせた
[ ] MammothのMoraleと退却を確認した
[ ] Shock ResistanceをScoutした
[ ] Flying Reserveを一歩後ろへ置いた
[ ] Fort攻略用Siegeがある
[ ] TemperatureとIce armorを確認した
[ ] High Seraphの代替Casterがいる
```

---

# 関連ページ

- [Flying・Storm・Air機動戦](../../systems/flying-storm.md)
- [Magic Path: Air](../../magic/paths/air.md)
- [Magic Path: Water](../../magic/paths/water.md)
- [召喚・Global・遠隔Ritual](../../magic/strategic-rituals.md)
- [戦闘ルール](../../basics/combat-rules.md)
- [ターン処理順](../../reference/turn-resolution.md)
- [Pretender設計サンプル](../../pretender/samples.md)
