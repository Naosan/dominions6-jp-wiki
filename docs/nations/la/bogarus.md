---
title: LA Bogarus
page_type: nation-guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-19"
nation_id: 116
era: "LA"
epithet: "Age of Heroes"
---

# LA Bogarus — Age of Heroes

LA Bogarusは、**平凡な人間兵を、非常に多様なMage、早いResearch、Communion・Sabbath、召喚・Global・遠隔Ritualで国家戦力へ変えるLate-game Magic国家**です。

国家の中心は、

> **役割の異なる多数のAny-fort Mage**
> ＋ **Astral CommunionとBlood Sabbath**
> ＋ **Fire・Air・Earth・Death・Blood・Holyの横断**
> ＋ **Staretsと国家召喚による戦略Access**
> ＋ **Research速度を実際の戦争へ変換するTiming**

です。

BogarusはSpell一覧を見ると万能に見えます。しかし、

- 通常兵が弱い
- Expansionが不安定
- Mageが脆い
- 多数のMage typeを分類する必要がある
- Gold・Commander Pointが不足
- Water・NatureはStarets Random依存、Glamourは自然には不足
- Communion・Blood・Ritualが同じMage turnを奪う

という制約があります。

> **Bogarusの上達は、すべての研究を進めることではなく、次の戦争に必要なSpellだけへ最短で到達し、その後に戦略魔法へPivotすることです。**

- [自動生成Recruitデータ](../../data/recruitment/la/bogarus.md)
- [国家別Site Search能力](../../data/site-search/la/bogarus.md)
- [Extended Magic Access](../../data/extended-magic-access/la/bogarus.md)
- [Magic Access Route](../../data/magic-access-routes/la/bogarus.md)
- [召喚・Global・遠隔Ritual](../../magic/strategic-rituals.md)
- [Communion](../../magic/communions.md)
- [Pretender設計サンプル](../../pretender/samples.md)

!!! note "このページの精度範囲"
    本文はDominions 6.35の固定データ、ゲーム内Nation・Unit・Spell・Item表示、公式Documentation、現行Inspector、現行Community資料を照合し、実戦判断へ再構成しています。Mage Cost、Research bonus、Unrest、Seduction、National Summon、Hero、Random Path、Patch、MODには例外があります。正確な数値とSpell条件はゲーム内表示と上記自動生成データを優先してください。

!!! warning "BogarusのMageは同じ資源を奪い合う"
    Researcher、Communion Master、Sabbath、Blood Hunter、Ritual caster、Site Searcherは同じCommander Point・Gold・Mage turnを使います。すべてを同時に最大化できるとは考えないでください。

---

# 一言でいうと

```text
最低限の兵でExpansion
→ Fortを増やしMageを量産
→ MageをPathとRoleで分類
→ 第一Research BreakpointでFirst war
→ Communionを小さく安全に使う
→ Research優位を維持
→ Summon Mage・Global・RemoteへPivot
→ Bloodは用途と輸送が完成してから拡張
```

国家です。

Bogarusは、

```text
Mageが多い
＝ すぐ強い
```

ではありません。

```text
Research
→ Spell
→ Caster
→ Gem / Slave
→ Script
→ Battle
```

までつながって初めて強くなります。

---

# 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | Late Age |
| Nation ID | 116 |
| Epithet | Age of Heroes |
| 軍事の中心 | Peshtsi、Druzhina、Khlyst、Mage |
| Any-fort Magic | F1、A2、E1、S2、D1、B2、H2 |
| Start Site | Starets、Eparch |
| Magicの軸 | Astral Communion、Air、Fire、Earth、Death、Blood、Holy |
| 主な不足 | Glamour。Water・NatureはStarets Random依存 |
| 戦略能力 | Fast research、Communion、Sabbath、召喚、遠隔、Hero |
| 操作量 | 非常に高い。Mage分類、Script、Gem、Blood、Ritual、Fort |
| 主な弱点 | 弱い通常兵、Mage assassination、Gold、Raid、Magic Duel、早期Rush |

## Any-fort Mage

```text
Exarch          H2
Skopets         H1 + 20% B1
Fivefold Angel  B2 H2
Occultist       S1 D1 B1
Kalendologist   S2
Astrapelagist   A2 S1
Master of Names S2 + F/A/B Random
Alchemist       F1 E1 S1
```

## Start Site

```text
Eparch   H3
Starets  F2 E1 S1 D2 + 100% A/W/E/S/N/D Random + 10% second Random
```

Start Site recruitは供給拠点とCommander Pointを確認します。

---

# 国家エンジン

```text
慎重なExpansion
        ↓
Fort・Labを増やす
        ↓
安価なResearcherを継続生産
        ↓
Mage typeをRole別に分類
        ↓
第一BreakpointでFirst war
        ↓
Communion / Battlefield Magicで兵を補う
        ↓
Research優位をSummon・Global・Remoteへ変換
        ↓
新Path・Gem・Commanderを獲得
        ↓
さらに上位の戦略魔法へ到達
```

止まりやすい場所は、

1. Expansionで通常兵を失いFort資金が遅れる
2. Mage種類が多く、Recruit方針が毎Turn変わる
3. Communionを大きくしすぎSlaveを失う
4. Bloodへ早くPivotしResearchが止まる
5. Researchは高いがGem・Caster・Targetがない
6. Mage FortをRaid・Assassinで失う

です。

---

# 強み

## 1. 多数のAny-fort Mage

一つのFortで複数Pathへアクセスできます。

- Fire
- Air
- Earth
- Astral
- Death
- Blood
- Holy

を分業できます。

## 2. Research

Kalendologist等の研究者により、Research Breakpointへ早く到達できます。

ただしResearchを戦争へ変換しなければ、領土差を取り戻せません。

## 3. Communion

多数のAstral MageをCommunion Master / Slaveへできます。

- Fire
- Air
- Earth
- Astral
- Death
- Blood

のBattle Pathを上げられます。

## 4. Sabbath

Occultist、Fivefold Angel等でBlood Sabbathへ入れます。

Blood Spellだけでなく、Blood SlaveをCommunion資源として使います。

## 5. Holy Access

H2をAny-fortで得られ、H3 Start Siteもあります。

- Smite
- Banish
- Bless
- Preach
- Throne
- Undead Counter

へ強いです。

## 6. Strategic Magic

BogarusはResearch速度とMage diversityにより、

- Summon
- Global
- Remote attack
- Blood
- Site Search
- Booster

へ早くPivotできます。

---

# 弱み

## 1. 通常兵が平凡

Voi・PeshtsiはLAの魔法戦に対し、そのままでは弱いです。

## 2. Expansion

高性能Sacred・Giant・Heavy Infantry国家より損失が出やすいです。

## 3. Mageが脆い

多くのMageは低HP・低Protectionです。

- Archer
- Assassin
- Flying Raider
- Remote attack
- AoE

へ弱いです。

## 4. Gold・Commander Point

Mage種類が多く、すべて雇いたくなりますが、Fortごとに一人しか選べない場合があります。

## 5. Water・Natureの供給とGlamour不足

Water・NatureはStaretsのRandomで得られますが、Start Site供給とRandom rollに依存します。

安定して必要数を揃えたい場合や高Pathへ伸ばしたい場合は、Pretender・Summon・Site・Boosterで別Routeを用意します。Glamourは自然には不足します。

## 6. 操作量

Communion、Blood、Ritual、Script、Gem、Fortを毎Turn管理します。

---

# 兵士

# Voi Spearman

Spear、Javelin、Shieldの安価兵です。

- Chaff
- Screen
- Siege
- Patrol
- Expansion補助

へ使います。

Morale・Combat statsが低いため、主力決戦兵ではありません。

---

# Voi Axeman

AxeとShieldを持つDamage寄りの安価兵です。

高Protectionへ少し有利ですが、命中・生存はMage supportが必要です。

---

# Voi Archer

Short Bowの安価Archerです。

- Chaff射撃
- Flaming等のBuff
- Siege
- PD補助

へ使います。

敵Storm・Arrow defence・High Protectionへ弱いです。

---

# Peshtsi Spearman

Scale armor、Kite Shield、Spearを持つScreenです。

BogarusのMageへRoundを渡します。

---

# Peshtsi Axeman

重めのArmorとAxeを持ちます。

ScreenよりDamageへ寄せます。

---

# Peshtsi City Guard

Sword、Heavy Shield、Castle Defenceを持ちます。

- Fort防衛
- Mage Fort保護
- Storm defence

へ向きます。

---

# Grid Druzhina

Composite Bowを持つHorse Archerです。

- Mobility
- Archer
- Flank
- Raid
- Buff carrier

へ使います。

---

# Malaia Druzhina

Lance、Heavy cavalryです。

- Charge
- Expansion
- Flank
- Commander assassination pressure

へ使います。

高価で、MageとGold競合します。

---

# Khlyst

Sacred・Stealthを持つ安価な特殊兵です。

通常Battle statsは高くありません。

役割は、

- Bless carrier
- Stealth pressure
- Unrest・特殊作戦
- Chaff
- Ritual・Battle synergy

です。

Heavy Blessで主力Eliteへ変えるより、供給量・Holy Point・国家計画を確認します。

---

# Commander・Mage

# Exarch

H2 Priestです。

- Banish
- Smite
- Bless
- Preach
- Throne
- Undead Counter

へ使います。

---

# Skopets

H1＋20% B1、Stealthを持ちます。

B1個体は、

- Blood Hunt
- Sabbath
- Site Search
- Special operation

へ使います。

---

# Fivefold Angel

B2H2、Spy、Stealthです。

- Blood Master
- Sabbath
- Blood Sacrifice系宗教
- Spy
- Stealth operation
- High Holy

へ使います。

高価なRoleが多いため、前線で簡単に失わないでください。

---

# Occultist

S1D1B1です。

Bogarusの重要なCrosspath Mageです。

- Communion
- Sabbath
- Death
- Blood
- Astral
- Remote・Ritual

へ使えます。

---

# Kalendologist

S2です。

- Research
- Communion
- Astral battle
- Site Search
- Summon・Ritual

へ使います。

量産できるS2はBogarusの中核です。

---

# Astrapelagist

A2S1です。

- Air battle
- Communion Master / Slave
- Storm
- Lightning
- Air Booster
- Magic Phase

へ使います。

---

# Master of Names

S2＋F/A/B Randomです。

Recruit後に、

```text
Fire
Air
Blood
```

へ分類します。

Random個体はAccess chain・Battle roleが変わります。

---

# Alchemist

F1E1S1です。

- Fire
- Earth
- Astral
- Communion
- Forge
- Alchemy・Economy
- Resistance

へ使います。

高価な場合、全Fortで量産せず必要数を決めます。

---

# Starets

F2E1S1D2＋100% A/W/E/S/N/D Random＋10% A/W/E/S/N/D second Randomです。

Bogarusの戦略Magic中核です。

- Fire
- Earth
- Death
- Astral
- Air / Water / Nature Random
- 追加Earth / Astral / Death Random
- Communion
- Summon
- Global
- Booster

へつながります。

Start Site供給なので、失うと補充が難しい場合があります。Water・Nature個体や高Path化するRandom個体は、通常のBattle Mageとして使い潰さず役割を分けます。

---

# Eparch

H3です。

- High Holy
- Smite
- Banish
- Throne
- Preach
- Religious pressure

へ使います。

---

# Expansion

## 基本

BogarusはMageが揃う前の通常兵が弱いため、Expansion計画が重要です。

```text
Peshtsi Screen
＋ Druzhina Damage / Archer
＋ Commander
＋ 必要ならPretender
```

を使います。

## Awake Expander

危険なCapital周辺をPretenderで取り、Fort・Researchを早める案があります。

## Cavalry

Malaia Druzhinaは強いChargeを持ちますが、高価です。

損失がFort・Mageを遅らせます。

## Archer

Voi Archer・Grid Druzhinaで接敵前に削ります。

---

# Independent別

## Archer

Peshtsi Shieldを前へ置きます。

## Heavy Infantry

Axe、Lance、Mage supportを使います。

## Barbarian

低HP人間兵へ高Damageが危険です。

## Cavalry

Shield、Spear、Formationを使います。

## Undead

ExarchとH3を使います。

## Elephant

Morale、Spear、Mage、Chaffを用意します。

---

# Expansion評価

```text
Province：
損失Gold：
Druzhina損失：
Fort開始：
Researcher数：
第一Breakpoint：
```

兵損失がResearcher一人分を超えたかを考えます。

---

# Fort・Economy

## Fortを増やす理由

Bogarusの国力はMage数です。

Fortは、

- Commander Point
- Researcher
- Battle Mage
- Priest
- Blood Hunter
- Ritual caster

を増やします。

## Recruit plan

Fortごとに役割を決めます。

```text
Research Fort
Air Fort
Blood Fort
Holy Fort
Front Fort
```

## Gold

Mageを全Fortで毎Turn雇うとGoldが枯れます。

兵・Fort・Lab・Temple・Patrolと競合します。

---

# Pretender

## 1. Awake Expander

Expansion弱点を補います。

## 2. Imprisoned Scales

ResearcherとFortを増やします。

国家兵だけでExpansionできるMap向けです。

## 3. Water・Natureの安定化 / Glamour bridge

StaretsのRandomだけへ依存したくないPathや、自然には不足するGlamourを補います。

- Water battlefield・Summon chain
- NatureのPoison Resistance・Regeneration・Healing
- Glamour utility

へ入ります。

## 4. Global caster

高Pathへ集中し、早いResearchをGlobalへ変換します。

## 5. Defensive Bless

Khlystより、Sacred Mage・PriestへのBless価値も考えます。

---

# Research

## First war

BogarusのFirst war候補は、

- Evocation
- Alteration
- Enchantment
- Thaumaturgy
- Communion

です。

敵に合わせて一つ選びます。

## Evocation

Fire・Air・Death damageを使います。

## Alteration

兵・Cavalry・MageのBuff。

## Enchantment

Army-wide effect、Arrow、Resistance、Battlefield。

## Thaumaturgy

Astral・MR attack・Mind・Remote。

## Construction

Booster、Research Item、Resistance。

## Conjuration

National summon、Mage summon、Elemental、Late-game access。

## Blood

Blood Hunt・Sabbath・Demon・Ritual。

---

# Communion

BogarusはMA Pythiumと異なり、多数PathをCommunionへつなげます。

## 小Communion

```text
2～4 Slave
＋
1～2 Master
```

から始めます。

## 目的

```text
必要Spell：
必要Path：
Master数：
Slave数：
Slave保護：
総Round：
```

を決めます。

## Master過多

Masterが増えるほどSlave Fatigueが増えます。

## Slave分類

高価なRare MageをSlaveへ固定しないでください。

## Magic Duel

S2・高Astral Mageを分散します。

---

# Sabbath

Occultist・Fivefold Angel等でSabbathへ入れます。

SabbathはBlood Slaveを使い、Blood Pathと他Pathを高めます。

ただし、

- Blood Slave supply
- Master数
- Slave protection
- Pain transfer
- Fatigue
- Retreat

を管理します。

---

# Blood pivot

## 早すぎるPivot

Blood Hunterを増やすと、

- Researcherが減る
- Goldが減る
- Patrolが必要
- Unrestが増える
- Slave輸送が必要

です。

## 軽いBlood

少数Hunterで、

- Sabbath
- Utility Ritual
- Booster
- Emergency

を用意します。

## 重いBlood

明確な、

- Demon
- Global
- Remote
- Blood summon
- Blood battle

用途が完成してから増やします。

[Blood Economy](../../magic/blood-economy.md)を参照してください。

---

# Strategic Magic

BogarusのLate-gameは、

```text
Research優位
→ Summon Mage
→ Missing Path
→ Booster
→ Global / Remote
```

です。

## Summon

国家Spell・一般Spellで、

- Holy
- Air
- Water
- Nature
- Death
- Commander

を補います。

ただしNative casterがいないNational Spellもあります。

## Global

Researchが早くても、Gem・Caster・Overcastが必要です。

## Remote

敵Mage Fort、Blood Hunt、PD、Throneへ圧力をかけます。

## Hero

HeroはWater・Natureの追加Accessや高Death等を開く場合がありますが、保証ではありません。

[召喚・Global・遠隔Ritual](../../magic/strategic-rituals.md)を参照してください。

---

# First war

```text
目的：
敵Protection：
敵MR：
敵Resistance：
Research：
Communion：
Master：
Slave：
Gem：
Mage protection：
Retreat：
```

## Army

### Screen

Peshtsi。

### Damage

Druzhina、Axe、Mage。

### Archer

Voi・Grid Druzhina。

### Mage

敵に合わせたPath。

### Holy

Undead・Demon・Sacredへ。

---

# Counter

## Early rush

Mage・Researchが揃う前に攻められます。

Fort、PD、Awake Pretender、Mercenary、外交を使います。

## Flying・Stealth Raider

Mage Fortを守ります。

Patrol、Bodyguard、Reserve、Fortを使います。

## Assassin

Rare MageへBodyguard。

## Magic Duel

Astral Mageを分散し、低価値S Mageを交換要員にします。

## Archer・Remote

Mageを後方配置、Fort、Arrow defence、Decoy Lab。

## Shock / Fire / Poison

Mage別Resistanceを用意します。

## Research denial

Fort・Labを失うと国家Engineが止まります。

---

# Multiplayer

## 敵から見たBogarus

- 早いResearch
- 多Path Communion
- Blood pivot
- Summon・Global
- Remote attack
- Weak early army

を警戒されます。

## 外交

序盤は早期Rush対象になりやすいため、

- Border
- Research timing
- 共同敵
- Gem trade
- NAP

を使います。

## 隠す情報

- Breakpoint
- Mage比率
- Blood pivot
- Starets Random
- Global plan
- Gem stock
- Communion構成

---

# よくある失敗

## 1. すべてのMageを雇う

FortごとのRoleを決めます。

## 2. Researchだけして戦わない

Breakpointで領土差を取ります。

## 3. 大Communionから始める

小CommunionをTestします。

## 4. Bloodへ早くPivot

ResearchとGoldが止まります。

## 5. Mage Fortを無防備

Raid・Assassinで国家Engineを失います。

## 6. Missing PathをHero任せ

Pretender・Summon・Siteを用意します。

## 7. Ritualへ全Gem

First war reserveを残します。

## 8. 通常兵を無価値と思う

MageへRoundを渡すScreenが必要です。

---

# Test game

```text
Turn：
Expansion損失：
第二Fort：
Researcher数：
第一Breakpoint：
First war：
Communion構成：
Slave生存：
Starets数：
Blood開始：
月間Slave：
最初のSummon：
最初のGlobal候補：
Missing Path：
```

---

# End Turn checklist

```text
[ ] 各FortのMage Recruitを決めた
[ ] Communion Master / Slaveを分けた
[ ] Rare MageへBodyguardがある
[ ] Research Breakpointと戦争Turnがつながっている
[ ] Blood Hunterの用途がある
[ ] Monthly RitualのGem予算を確認した
[ ] First war reserveを残した
[ ] Mage FortへReserveが届く
[ ] Magic Duel対象を分散した
[ ] Summon Mageの次の仕事を決めた
```

---

# 関連ページ

- [召喚・Global・遠隔Ritual](../../magic/strategic-rituals.md)
- [Communion](../../magic/communions.md)
- [Blood Economy](../../magic/blood-economy.md)
- [Research](../../magic/research.md)
- [Magic Boosting](../../magic/boosting.md)
- [ターン処理順](../../reference/turn-resolution.md)
- [Pretender設計サンプル](../../pretender/samples.md)
