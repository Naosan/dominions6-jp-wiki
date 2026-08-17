---
title: EA Abysia
page_type: nation-guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
nation_id: 16
era: "EA"
epithet: "Children of Flame"
---

# EA Abysia — Children of Flame

EA Abysiaは、**重装歩兵とFire Magicだけを前へ押し出す国家ではありません。**

本当の国家エンジンは、

> **HeatとFireへ適応した重装兵**
> ＋ **盾役・高Damage役・Salamanderの分業**
> ＋ **AnathemantによるFire・Earth・Holy**
> ＋ **首都WarlockによるAstral・Blood**
> ＋ **Burning OneとBlood Sacrificeを含むSacred・宗教圧力**

です。

Abysian Infantryは人間より高いHPとStrength、重いArmor、Fire Resistanceを持ち、通常兵同士の正面戦闘に強いです。国家MageもFireを自然に伸ばし、自軍が耐えられるFire環境を戦場へ持ち込めます。

しかし、

- 兵とMageが高価で、ResourceとGoldの両方を使う
- 重装兵が遅く、遠距離攻撃を持たない
- Fire Resistance一つで主力Magicを弱められる
- Mageが短命・老齢になりやすい
- 首都のCommander PointをSacred、Warlock、高位Priestが奪い合う
- Magic diversityが狭く、Fireで解決できない敵への第二案が必要

という制約があります。

> **EA Abysiaの強さは、「Fireを撃つこと」ではなく、「自軍だけがHeat・Fire・重装長期戦へ耐えられる状態を先に作ること」です。**

- [自動生成Recruitデータ](../../data/recruitment/ea/abysia.md)
- [国家別Site Search能力](../../data/site-search/ea/abysia.md)
- [Extended Magic Access](../../data/extended-magic-access/ea/abysia.md)
- [Magic Access Route](../../data/magic-access-routes/ea/abysia.md)
- [Pretender設計サンプル](../../pretender/samples.md)

!!! note "このページの精度範囲"
    本文はDominions 6.35の固定データ、ゲーム内Nation・Unit・Spell・Item表示、公式Documentation、現行Inspector、現行Community資料を照合し、実戦判断へ再構成しています。国家Site、Holy Point、Capital recruit、Blood Sacrifice、Extreme Scale、短命・老齢、National Spell、Patch、MODには例外があります。正確なCost・Path・Recruit条件・Research Levelはゲーム内表示と上記自動生成データを優先してください。

!!! warning "首都・国家Site Recruit"
    Burning One、Anointed of Rhuax、Warlock、Warlock Apprentice等は国家固有Siteや首都条件を持ちます。自動生成の通常Recruit表に現れない場合があるため、首都Recruit画面とExtended Magic Accessを正本にしてください。

---

# 一言でいうと

```text
盾持ち重装兵で射撃と接敵を受ける
→ Battleaxe・Flail・Burning Oneで敵前衛を破る
→ Fire Resistanceを自軍へ揃える
→ AnathemantがFire・Heat・Elementalを展開する
→ Fireで止まる敵にはEarth・Astral・Blood・装備で第二案を作る
```

国家です。

EA Abysiaは「兵が硬い」「Fireに無敵」という第一印象が強いですが、実戦では、

```text
何に硬いか
何に無防備か
何Turnで敵へ届くか
Fire以外に何があるか
```

を分ける必要があります。

---

# 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | Early Age |
| Nation ID | 16 |
| Epithet | Children of Flame |
| Preferred Temperature | Heat寄り |
| 軍事の中心 | 重装Abysian Infantry、Burning One、Salamander、首都特殊兵 |
| 確実なMagicの軸 | Fire、Earth、Holy |
| 首都で広がるPath | Astral、Blood、Fire・Earth random |
| 主要Mage | Anathemant Salamander、Anathemant Dragon、Anointed of Rhuax、Warlock |
| 国家特徴 | Fire Resistance、Heat Aura、Blood Sacrifice、Fire系国家Spell |
| 操作量 | 中～高。重装編成、Mage老齢、Blood、宗教、Gemを管理 |
| 主な弱点 | Fire Resistance、鈍足、射撃不足、Cold、AN・MR攻撃、Magic diversity |

## Recruitデータで見る兵の骨格

通常Abysian Infantryは、

- Size 3
- HP 15前後
- Strength 13前後
- MR 12前後
- Plate Hauberk等の重装備

を持ちます。

武器差が役割差になります。

| 装備 | 主な役割 |
|---|---|
| Battleaxe | 一撃Damage、高Protectionへの圧力 |
| Flail | 二回攻撃、Shield持ちへの命中補助、軽～中装処理 |
| Axe＋Tower Shield | 射撃・接敵を受けるScreen |
| Morningstar＋Tower Shield | Shield役兼、Pierce / BluntでArmorへ圧力 |

同じ名前のAbysian Infantryを一括して扱わず、装備で分けます。

---

# 国家エンジン

```text
重装兵で低損失Expansion
        ↓
ResourceとIncomeを確保
        ↓
AnathemantとFortを増やす
        ↓
Fire Resistanceを自軍へ揃える
        ↓
Fire・Heat・Elementalで敵だけを疲れさせる
        ↓
Field Battle勝利
        ↓
Siege・Blood Sacrifice・Templeで前線を固定
        ↓
Warlock・Blood・PretenderでMagic diversityを拡張
```

この循環が止まりやすい場所は、

1. 重装兵へResourcesを使いすぎ、第二Fortが遅れる
2. 首都Commander Pointを高価なCommanderへ使い、Researchが伸びない
3. Fire Spellだけを用意し、Fire Resistance相手に勝利条件が消える
4. Bloodを早く始めすぎ、Gold・Population・Researchを同時に失う

です。

---

# 国家固有のScaleと環境

## Heatを味方につける

AbysianはHeatへ適応し、Heat AuraやFire Powerを持つUnitを多く含みます。

Heatは、

- 自軍の国家能力
- 敵のFatigue
- Cold Blooded
- Supply
- Seasonal変化
- Enemy Dominion

へ影響します。

Heat 3で自軍が強くても、敵もFire・Heatへ適応しているなら差は小さくなります。

## Growth・Deathの特殊性

EA Abysiaは通常国家と異なるGrowth / Deathの影響を持ちます。

Pretender画面のTooltipと国家説明を確認し、

```text
表示Point
＋ Income
＋ Population
＋ Supply
＋ Blood経済
＋ 老齢Mage
```

を一緒に評価します。

## Blood Sacrifice

Blood Slaveを宗教圧力へ変換できます。

これは、

- Border Dominion
- Throne
- Enemy Dominion
- Incarnate Bless
- Sacred戦

に価値があります。

ただしBlood SlaveはSummon、Battle Spell、Ritualとも競合します。宗教戦へ何Slave使うかを決めます。

---

# 強み

## 1. 正面戦闘に強い重装兵

低～中Damageの通常兵に対し、ArmorとHPで戦線を維持できます。

盾持ち兵を前へ置けば、ArcherやJavelinへの耐性も上がります。

## 2. 高Strengthと武器選択

Battleaxe、Flail、Morningstarを使い分け、

- 一撃Damage
- 多段攻撃
- Shield対策
- Pierce / Blunt

を選べます。

## 3. 自軍がFireへ耐えやすい

通常国家ではFriendly FireになるFire・Heat効果を、自軍側だけ有利に使いやすいです。

```text
Fire Resistanceを確認
→ 前衛を整える
→ 敵だけがFire・Heatで消耗する
```

順序が重要です。

## 4. Fireの高Pathへ自然に届く

Anathemant Dragon、Anointed of Rhuax等により、FireのBattle spell、Elemental、国家Spellへ到達しやすいです。

## 5. Astral・Bloodの首都Engine

Warlock系により、Fire国家の外側へ、

- Astral utility
- MR attack
- Communion / Sabbath可能性
- Blood Hunt
- Blood summon

を開けます。

首都限定であることが最大の制約です。

---

# 弱み

## 1. 遠距離戦が弱い

国家兵に標準的なBow・Crossbowがありません。

敵射撃へ近づく間に損耗しやすく、

- Tower Shield
- Formation
- Hold
- Fire spellのRange
- Summon
- Storm等の環境

で回答します。

## 2. 鈍足

重装備のMap penaltyとCombat Speedにより、

- Buff前後の接敵Timing
- 敵Archerへの到達
- Raid対応
- Reinforcement

が遅れます。

## 3. Fire Resistanceで主力Magicを止められる

敵がFire Ward、Fire-resistant Unit、Elementalへ切り替えると、Fire Damageの投資効率が下がります。

Fireは国家の主軸ですが、唯一のDamage typeにしません。

## 4. Cold・Fatigue

Heatへ適応した軍は、Cold環境やCold Damageで性能を落とされる場合があります。

重装兵は長期戦でFatigueを溜めやすいため、敵を倒す速度とReinvigorationを考えます。

## 5. Magic diversityと首都依存

通常FortからはFire・Earth・Holyが中心です。

Astral・Blood・高位Crosspathを首都Mageへ依存すると、Capital Siegeで国家技術が止まります。

---

# 兵士

## Abysian Infantry：Battleaxe

高Damageの二手武器です。

### 向く相手

- 中～高Protection
- Giant
- Regeneration
- 少数Elite

### 弱点

- Shieldがない
- Defenceが低い
- 射撃を受ける
- 多数Chaffへ攻撃回数が不足

盾兵の後ろへ置きます。

## Abysian Infantry：Flail

二回攻撃とShieldに対する命中補助を持ちます。

### 向く相手

- Shield持ち
- 低～中Protection
- 数の多い通常兵

### 弱点

- 両手でShieldがない
- 高Protectionへ一撃が軽い
- Fire Shield等へ攻撃回数がRisk

## Abysian Infantry：Axe＋Tower Shield

Line holderです。

- Archerを受ける
- 最初のChargeを受ける
- Damage役へ時間を作る

用途があります。

Damageだけで比較してRecruitから外さないでください。

## Abysian Infantry：Morningstar＋Tower Shield

ScreenとArmor圧力を兼ねます。

MorningstarのDamage typeとShield補助を活かし、敵装備に応じてAxe盾兵と配分します。

## Salamander

Fire AP攻撃とHeat Auraを持つ特殊兵です。

### 強み

- ArmorへFire AP
- Magic Weapon
- 密集戦でHeat
- 通常兵にないDamage type

### 弱み

- Animal・Undisciplined
- Morale
- Shieldなし
- Fire Resistant相手
- 自軍の非耐性UnitへのHeat

大量に混ぜるより、必要なTargetへ少数投入します。

## Burning One

首都の代表的Sacredです。

- 高い戦闘Stats
- Fire Shield / Heat Aura
- 複数攻撃
- Berserk
- Bless

を使えます。

一方、

- Holy Point / Recruit limit
- 首都依存
- 高Resource
- Formation上の制約
- Anti-Sacred
- Cold・MR・AN

があります。

Heavy BlessはBurning One一体の強化だけでなく、供給数とScales損失で評価します。

## Misbred・Demonbred等

国家Site・首都の特殊兵です。

通常重歩兵と異なる、

- 機動
- Demon / Magic Being
- Special attack
- Commander / Raid

を担います。

出現条件と現在のUnit Tooltipを確認します。

---

# Commander・Mage

## Slayer

Assassin・Stealthとして、

- Scout排除
- Priest・Mage狙い
- Border圧力
- 敵Script崩し

へ使います。

敵Commanderを倒せる装備・Script・Bodyguard情報がないまま連投しないでください。

## Warlord

通常ArmyのLeadership担当です。

高価なMageをCommanderとして前線へ拘束せず、Warlordへ兵を持たせます。

## Beast Trainer

Salamander等のMagic / Animal Leadershipを含む特殊兵運用へ使います。

## Anathemant Salamander

F2 H1の量産Priest-Mageです。

- Research
- Fire Resistance
- 低～中位Fire damage
- Bless・Preach
- Site Search

を担います。

安価な量産MageをFirst warの数へ変える国家Engineです。

## Anathemant Dragon

F3 E1 H2の高位Mageです。

- Fire Elemental
- Fire battlefield
- Earth crosspath
- Army-wide Fire support
- 高位Holy

へ進みます。

Slow to recruitによりCommander Pointを複数Turn使う場合があります。毎Fortで何体必要か決めます。

## Anointed of Rhuax

首都の高位Fire・Holy Mageです。

- 高級Fire Spell
- 国家Spell
- Prophet / Throne候補
- Battle leader
- Global・Ritual

へ使えます。

高価なRare Commanderを通常Evocation一人として失わないでください。

## Warlock

Astral・Bloodの技術経路です。

- Blood Hunt
- Astral utility
- MR attack
- Sabbath / Communion
- Blood summon
- Booster

を担当します。

首都Commander PointをAnointed、Warlock、Apprenticeで分けるため、Recruit計画が必要です。

## Warlock Apprentice

Blood economyを広げる低位Mageです。

Research、Blood Hunt、Sabbath slave等へ使いますが、UnrestとPopulationを計画します。

---

# Magic Access

## 通常Fort

計画しやすい保証軸：

```text
Fire 3
Earth 1
Holy 2
```

です。

## 首都

国家Site Mageにより、

```text
Fire 4
Earth 1
Astral 1
Blood 2
Holy 3
```

へ広がります。

Randomにより一部Crosspathが増えますが、保証として扱いません。

## Fire

国家の主力です。

- Direct Damage
- Elemental
- Fire Resistance
- Heat
- Battlefield-wide effect
- Remote / Terrain

へつながります。

## Earth

低位でも、

- Self path boost
- Armor・Strength support
- Forge
- Fire / Earth国家Spell

へ価値があります。

高位Earthへ自然に届きにくい点をPretender・Booster・Empowermentで判断します。

## Astral

首都Warlockの重要Pathです。

- MR attack
- Antimagic
- Magic Duel
- Communion
- Teleport / Ritual

へ接続します。

## Blood

第二の国家Engineです。

Bloodを始める前に、

```text
Hunter
Patrol
Slave用途
研究Level
前線輸送
```

を決めます。

## 欠けるPath

Air、Water、Nature、Glamour、Deathは通常計画で不足します。

特に、

- Shock Resistance
- Cold対策
- Regeneration・Poison
- Death summon
- Mobility

をどこから得るかがPretender設計の中心です。

---

# 国家SpellとFire計画

## Liquid Flames of Rhuax

Fire・Earthの高Damage Fire spellとして、高Protection兵や大型Targetへ使います。

敵Fire Resistance、Range、Gem、Caster数を確認します。

## Inner Furnace

Abysian向けの自己・Army強化として、Heat / Fireを国家戦術へ接続します。

使用条件と効果範囲は現行Spell Tooltipを確認します。

## Hellscape

Province環境をAbysia側へ寄せる戦略Ritualです。

Battle直前に環境が変わると決めつけず、Turn処理順とEvent Timingを確認します。

## Fire Elemental

敵Fire Resistanceが低い通常兵へ非常に強力です。

しかし、

- Fire Resistance
- Magic Weapon
- 高Damage
- Water / Cold

を持つ敵へGem効率が下がります。

---

# Pretender方針

## 1. Heavy Bless

Burning One、Sacred Mage、Sacred Commanderを強化します。

### 候補となる目的

- Expansion
- Reinvigoration
- Attack / Damage
- Defence / Protection
- MR
- Cold / Shock / Poison Resistance

### 失敗条件

- Burning Oneの供給が少ない
- 首都を包囲される
- Incarnate Bless不在
- Anti-Sacred
- Scales不足

## 2. Light Bless＋Scales

Burning Oneの致命的弱点だけ補い、通常重歩兵とMage生産を伸ばします。

Abysiaは通常兵も強いため、Light Blessが国家全体の持続力と合う場合があります。

## 3. Diversity Rainbow

Air・Water・Nature・Death・Glamour等を補います。

- Shock Resistance
- Cold対策
- Booster
- Summon Mage
- Crosspath Item

を目的にします。

## 4. Imprisoned Scales

重装兵とMage、Fortを増やす長期経済設計です。

国家兵だけでExpansionできるか、Burning OneなしのFirst warが成立するかをTestします。

## 5. Awake Expander

Resourceの重い国家兵を待たず、Pretenderで別方向を取ります。

ただしAbysian Infantry自体がExpansion可能なら、Awake costと追加Province数を比較します。

---

# Scales

## Productivity

重装歩兵とBurning OneのResourceを支えます。

Capitalで、

```text
盾兵何体
＋ Damage兵何体
＋ Burning One何体
```

をRecruitできるかTestします。

## Order

高価なMage・Fort・ArmyのGoldを支えます。

## Heat

国家適性とHeat Auraを活かします。

## Growth / Death

国家固有補正とBlood経済、Mage老齢を含めて判断します。

## Magic

First warのFire・Resistance・Elemental到達を早めます。

Heavy Blessとの交換条件を比較します。

## Luck / Misfortune

短命MageやCapital依存が高い国家では、悪Eventの損失が大きくなる場合があります。単一Gameの結果で判断しません。

---

# 序盤拡張

## 標準Army

```text
Tower Shield infantry
＋ Battleaxe / Flail infantry
＋ Commander
＋ 必要ならPriest / Burning One
```

です。

Shield兵が先に接敵し、Damage役を少し後ろへ置きます。

## 攻めやすい相手

- 低Damage歩兵
- Fire Resistanceのない重歩兵
- Shieldが少ない兵
- Moraleの低い通常兵

## 危険な相手

### Archer・Crossbow

盾なしDamage役を先頭へ出さないでください。

### Cavalry

高Damage Chargeを盾兵で受けます。

### Barbarian

高Damage両手武器がArmorを抜きます。

### Cold・Water系特殊兵

Fire適性だけでは防げません。

### Elephant・Trample

Size・Morale・密集を確認します。

### Fire-resistant敵

Salamander・Fire spellへの依存を減らします。

## Expansion損失

Abysian Infantryは補充可能でも高Resourceです。

勝利数だけでなく、

- Damage役の損失
- Burning Oneの損失
- Commander
- 第二Army完成
- 第二Fort資金

を記録します。

---

# Economy・Fort

## Resource Fort

High-resource Provinceと隣接feederを使い、重装兵を生産します。

## Mage Fort

Resourcesが低くても、Anathemantを毎Turn雇えるなら価値があります。

## Capital

Capitalは、

- Burning One
- Anointed of Rhuax
- Warlock
- Warlock Apprentice

を巡るCommander / Holy / Resource bottleneckです。

首都Queueを毎Turn確認します。

## Cave・Wasteland

国家能力とFort bonus、Heat、Resourceを活かせる場合があります。

現在のFort TooltipとTerrainを確認してください。

## 前線Supply

重装兵は移動が遅く、Siegeが長引きます。

Supply Item、Nature access、Fort、Army分割を用意します。

---

# Research

## 第一Breakpoint：Fire Resistanceと接敵

自軍が自分のFire・Heat戦術へ耐える状態を先に作ります。

## 第二Breakpoint：Damage

- Fireball系
- Falling Fires系
- Fire Elemental
- Fire / Earth国家Spell

から、敵に合うものを選びます。

## 第三Breakpoint：Fire resistant対策

- Earth support
- Astral MR attack
- Blood summon・Battle buff
- Magic Item
- 通常高Damage兵

へ分岐します。

## Construction

- Fire booster
- Fire / Cold / Shock Resistance
- Research Item
- Thug装備
- Blood / Astral support

を作ります。

## Blood

Blood Huntを始める前に、最初の用途を一つ決めます。

```text
Battle buff
Summon
Sabbath
Blood Sacrifice
Booster / Item
```

用途がResearchの先なら、先に通常Mageを増やします。

---

# Army構成

## Shield Line

Axe・Morningstar＋Tower Shieldで、射撃と最初の接敵を受けます。

## Damage Line

Battleaxe、Flail、Burning Oneを後ろへ置きます。

## Salamander Section

少数を別Squadにし、TargetとHeat Auraを管理します。

## Mage Core

- Fire Resistance
- Elemental
- Direct Damage
- Fire / Earth support
- Astral / Blood second plan

へ役割を分けます。

## Assassin / Raider

Slayer、Demonbred、Summon等で敵後方へ圧力をかけます。

---

# Script例の考え方

```text
Anathemant A：Fire Resistance → Army support → Cast Spells
Anathemant B：Path boost → Elemental / Damage
Anathemant Dragon：Earth / Fire setup → National spell / Battlefield role
Warlock：Astral defence / MR attack / Sabbath
Priest：Bless → Sermon / Holy support
```

## Scriptが壊れる条件

- Enemy Fire Resistance
- Heatが敵にも有利
- Mage老齢・Disease
- Gem不足
- 盾兵よりDamage役が先に接敵
- Archerへ到達前に損耗
- SalamanderがRout
- Fire Storm等へ自軍非耐性Unitを混ぜた

---

# Siege・Map Control

## Siege

重装兵はField Battleへ強い一方、移動とSupplyが遅いです。

Siege Bonus、Summon、安価なIndependentを追加します。

## Storm

狭いGateへ重装兵が詰まり、Heat・AoE・Fatigueが増えます。

Shield、Morale、Reinvigoration、Mage位置をField Battleと別に設計します。

## Raid

Main Armyは鈍いため、Slayer、Demonbred、Summon、Magic Phaseを使います。

## Dominion

TempleとBlood Sacrificeで、新しいBorder・Throneへ国家環境を広げます。

---

# Counterと対応

## Fire Resistance

### 問題

Fire Damage、Salamander、Heatの効率が下がります。

### 対応

- Battleaxe・Morningstarの物理Damage
- Earth support
- Astral MR attack
- Blood summon
- Resistanceを剥がす / Casterを倒す

## Cold

- Cold Resistance
- Temperature control
- Mage・老人保護
- Fire環境の再構築

を使います。

## Shock

重装Armorへ依存しないDamageです。Shock Resistance、分散、敵Air Mage狙いを準備します。

## AP・AN

Protectionだけでなく、Shield、HP、Defence、Luck、敵Caster killを組み合わせます。

## MR attack

Antimagic、MR Item、Mindless / Demon Summon、Astral counterを使います。

## Flying・Attack Rear

Mageが高価で短命です。Bodyguard、分散、後衛Screenを置きます。

## Poison

Fire Resistanceでは防げません。Poison Resistance、戦闘時間短縮、Nature accessを検討します。

## Long-range Archer

Shield Line、Storm、Summon、Magic damageで射撃時間を短くします。

---

# Multiplayer

## 脅威認識

EA Abysiaは、

- Heavy Infantry rush
- Burning One Bless
- Fire Elemental
- Blood scaling
- Blood Sacrifice

を警戒されます。

## 情報管理

隠したいもの：

- Warlock数
- Blood Slave income
- Fire以外のPretender Path
- National spell到達
- Burning One Blessの弱点

## 外交

鈍足Armyは長いBorderと二正面戦争へ弱いです。

Border Fort、Choke、Throne、Temperatureを含めて境界を決めます。

## 戦争目的

Fire戦術が強いTimingで、

- Border Fort
- Mage拠点
- Fire-resistant Counterが揃う前の主力Army

を狙います。

---

# よくある失敗

## Battleaxe兵だけを作る

射撃とChargeを受けるShield Lineがありません。

## Fire spellだけを研究する

Fire Resistance一つで勝利条件が消えます。

## Heavy BlessだがBurning One供給を数えない

Scalesを削った対価を回収できません。

##首都Queueを管理しない

Anointed、Warlock、Burning Oneが同時に欲しくなり、全部遅れます。

## Bloodを早く始めすぎる

Research、Gold、Populationを失い、使うSpellがありません。

## Heat Auraを味方へ無視

非耐性IndependentやSummonが味方のHeatで疲れます。

## Mage老齢を無視

DiseaseでRare Pathと国家計画を失います。

## 重装兵で敵Raiderを追う

Main Armyが前線から外れます。

---

# Turnごとの確認

```text
1. CapitalのCommander / Holy / Resource bottleneck
2. Shield兵とDamage兵の比率
3. MageのAge・Disease
4. Fire Resistanceを持つ敵
5. Warlock・Blood Slave
6. TempleとDominion
7. 第二FortとResource feeder
8. Supply・Map Move
9. Fire以外の第二Damage
10. End Turn前のAssassin・Scout
```

---

# Test Game Checklist

## Expansion

- 盾兵比率
- Battleaxe / Flail損失
- Burning One供給
- Archer・Cavalry・Barbarianへの結果
- 第二Army完成Turn

## Economy

- Capital Resource
- Anathemant生産
- 第二Fort開始Turn
- Warlockを雇うと何が止まるか

## Research

- Fire Resistance
- Elemental / Direct Damage
- National spell
- Fire-resistant対策
- Blood開始Timing

## First War

- Shield Lineが先に接敵したか
- Fire Resistance差を作れたか
- 敵がFire Wardした後の第二案
- Mage老齢・Gem・Supply
- Siege継続

---

## 関連ページ

- [国家選択ガイド](../choose-a-nation.md)
- [Pretender設計サンプル](../../pretender/samples.md)
- [Bless](../../pretender/bless.md)
- [Fire](../../magic/paths/fire.md)
- [Blood](../../magic/paths/blood.md)
- [戦闘ルール](../../basics/combat-rules.md)
- [命令とBattle Script](../../basics/orders.md)
- [Researchと研究ルート](../../magic/research.md)
- [Gem](../../magic/gems.md)
- [Fort・Siege・Storm](../../systems/forts.md)
- [Dominion](../../systems/dominion.md)
- [初心者Q&A：内政・補給・自動化](../../getting-started/logistics-faq.md)

## 主な参照先

- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [Illwiki — EA Abysia](https://illwiki.com/dom5/ea_abysia)（現行挙動の照合用。数値はゲーム内表示と6.35固定データを優先）
