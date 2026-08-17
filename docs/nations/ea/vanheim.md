---
title: EA Vanheim
page_type: nation-guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
nation_id: 30
era: "EA"
epithet: "Age of Vanir"
---

# EA Vanheim — Age of Vanir

EA Vanheimは、**高DefenceのGlamoured Vanir、Stealth Army、Air・Glamour・Blood、Andvarian Dwarfの鍛造を、情報戦と局地的多数へ変換する国家**です。

国家の中心は、

> **GlamourとStealthを持つVanir兵**
> ＋ **騎乗Mage-PriestであるVanherse・Vanjarl**
> ＋ **Start Siteで雇うDwarven Smith**
> ＋ **Sailingと高Map Moveによる経路変更**
> ＋ **Air・Glamour・Blood・Earthを使うCounter装備**

です。

Vanheimの軍は、Map上で見えにくく、一見すると少数に見え、複数方向へ速く動けます。しかし、

- Vanir一体が高価
- Defenceへ依存し、AoE・Fatigue・Harassmentで崩れる
- MageがCommander・Priest・Raider・Casterを兼ねる
- Astral・Water・Natureが自然には不足
- Stealth Raidへ兵を回しすぎると正面Armyが薄くなる

という制約があります。

> **Vanheimの強さは、見えないことではなく、敵に「どこを守るか」を間違えさせることです。**

- [自動生成Recruitデータ](../../data/recruitment/ea/vanheim.md)
- [国家別Site Search能力](../../data/site-search/ea/vanheim.md)
- [Extended Magic Access](../../data/extended-magic-access/ea/vanheim.md)
- [Magic Access Route](../../data/magic-access-routes/ea/vanheim.md)
- [Stealth・Glamour・特殊作戦](../../systems/stealth-glamour.md)
- [Pretender設計サンプル](../../pretender/samples.md)

!!! note "このページの精度範囲"
    本文はDominions 6.35の固定データ、ゲーム内Nation・Unit・Spell・Item表示、公式Documentation、現行Inspector、現行Community資料を照合し、実戦判断へ再構成しています。Sailing、Stealth判定、Glamour、National Item、Start Site recruit、Hero、Random Path、Patch、MODには例外があります。正確なCost・Path・Order・効果はゲーム内表示と上記自動生成データを優先してください。

!!! warning "通常RecruitとStart Site recruit"
    Recruit索引の通常枠ではVanherse・VanjarlがAny-fort Mageとして表示されます。Dwarven Smithは国家Start Siteに基づくRecruitです。実際のRecruit場所・Commander Point・Slow recruitmentは現在のRecruit画面を正本にしてください。

---

# 一言でいうと

```text
Glamoured兵でExpansion
→ Vanherse・Vanjarlを増やす
→ Dwarven SmithでItemとBoosterを用意
→ 正面ArmyとStealth Raiderを分ける
→ Air・GlamourでBattleを有利化
→ Sailing・Stealthで敵後方へ圧力
→ 敵Counterに合わせて装備とDamageを切り替える
```

国家です。

Vanheimは、

```text
高Defenceだから正面で無敵
```

という国家ではありません。

正しい理解は、

```text
通常攻撃を受けにくい
＋
敵がArmy位置を把握しにくい
＋
必要な場所へ局地的に集中できる
```

です。

---

# 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | Early Age |
| Nation ID | 30 |
| Epithet | Age of Vanir |
| 軍事の中心 | Huskarl、Hirdman、Mounted Hirdman、Glamoured Commander |
| 通常Recruit Magic | Vanherse A1 G1 H1、Vanjarl A2 G1 B1 H2 |
| Start Site Magic | Dwarven Smith E2＋F/A/E/D/G Random |
| 戦略能力 | Stealth、Glamour、Sailing、騎乗、高Map Move、Blood Sacrifice |
| Magicの軸 | Air、Glamour、Blood、Earth |
| 主な不足 | Astral、Water、Nature |
| 操作量 | 高め。Stealth Army、Mage分類、Item、Blood、経路管理 |
| 主な弱点 | AoE、Fatigue、Harassment、True Sight、MR attack、高価な損失 |

## Recruitデータで最初に見るもの

### Troop

```text
Serf Warrior
Huskarl（Spear）
Huskarl（Axe）
Hirdman
Mounted Hirdman
```

Vanir系兵はGlamourとStealthを持ち、高Defence・高MR寄りです。

### Commander

```text
Van Scout
Vanherse   A1 G1 H1
Vanjarl    A2 G1 B1 H2
```

Vanherse・Vanjarlは、

- Army Commander
- Priest
- Battle Mage
- Stealth leader
- Raider
- Thug候補
- Blood Sacrifice担当

を兼ねます。

この多機能性は強みですが、一体を失うと複数Roleを同時に失います。

---

# 国家エンジン

Vanheimの国家Engineは次の循環です。

```text
Glamoured兵で低損失Expansion
        ↓
Income・Fort候補・Coastを確保
        ↓
Vanherse・Vanjarlを複数Fortで生産
        ↓
Dwarven SmithがItem・Boosterを鍛造
        ↓
正面ArmyとStealth Armyを分業
        ↓
Air・Glamour・装備でBattle条件を改善
        ↓
Raid・Sailingで敵Reserveを分散
        ↓
Main ArmyがFort・Throneを取る
```

止まりやすい場所は、

1. 高価なVanirをExpansionで失う
2. Mage-Priestを戦闘で使い潰し、Researchが遅れる
3. Raiderを増やしすぎ、Fort攻略Armyが足りない
4. Constructionへ偏り、Battle Spellがない
5. Bloodを始めるが用途・Patrol・輸送がない

です。

---

# 強み

## 1. 高Defence・GlamourのVanir兵

HuskarlとHirdmanは、一般的な人間兵より、

- Defence
- Attack
- MR
- Combat Speed
- Stealth

で優位を取りやすいです。

通常兵の少数攻撃には強く、Independent Expansionで低損失を作れます。

ただし、Protection・HPだけで耐える国家ではありません。

## 2. Army全体を隠せる

Commanderと兵のStealthを揃えると、敵領へ潜入・移動できます。

- 低PD Raid
- Tax route切断
- Lab・Temple圧力
- Retreat route切断
- Fort建設妨害
- Main Army方向の偽装

へ使えます。

## 3. Vanherse・Vanjarlの多機能性

VanherseはA1G1H1、VanjarlはA2G1B1H2です。

この組み合わせにより、

- Air support
- Glamour support
- Blessing
- Blood Sacrifice
- Stealth command
- Battle Magic
- Thug化

を行えます。

## 4. Dwarven Smith

Dwarven SmithはEarthを基礎にRandom Pathを持ち、Forge能力へ優れます。

- Earth Booster
- Air Booster
- Glamour Item
- Resistance Item
- Thug gear
- Crosspath Item

を国家内で作りやすくします。

Itemは、敵Counterへ具体的に回答する手段です。

## 5. Sailingと騎乗機動

Sailingと高Map Moveにより、陸路だけでは予測しにくい経路を使えます。

Stealthと組み合わせると、敵は、

```text
Armyが見えない
＋
到着経路も読みにくい
```

状態になります。

## 6. Blood Sacrifice

PriestがBlood SlaveをTempleで捧げ、Dominion pressureを増やせます。

Bloodを軍事召喚だけでなく宗教Networkへ使えるため、Throne・Border Temple・Dominion戦へ価値があります。

---

# 弱み

## 1. 一体が高価

Huskarl、Hirdman、Vanherse、Vanjarlは安価なChaffではありません。

Battleに勝っても、

```text
高価なVanirを毎回少数失う
```

なら、長期交換で負けます。

## 2. Defence依存

高Defenceは、

- Harassment
- 多数攻撃
- Fatigue
- Entangle
- Web
- AoE
- True Sight

で弱くなります。

## 3. Protection・HPはGiant級ではない

一度当たった高Damage・AP・AN・Elemental attackが重くなります。

## 4. Mageが高価でRole競合

Vanjarlを、

- Research
- Battle
- Raid
- Blood
- Priest
- Commander

へ同時に使えません。

## 5. Astral・Water・Nature不足

Mind protection、Magic Duel、Water battlefield、Nature regeneration・Poison対策等が不足しやすいです。

Pretender、Site Mage、Summon、Hero、Empowermentを検討します。

## 6. Stealthへ依存しすぎる

敵がPatrol、Scout、Reserve、True Sightを用意すると、Raid効率が下がります。

正面Army、Siege、Gem Magicを残します。

---

# 兵士

# Serf Warrior

安価な通常人間兵です。

主な役割は、

- Siege
- Patrol
- Chaff
- Arrow受け
- PD補助
- Vanirを使うほどでない仕事

です。

Glamour・Stealth Armyへ混ぜると潜伏計画を壊す可能性があります。

```text
Vanirの代用品
```

ではなく、

```text
Vanirへ安い仕事をさせないための兵
```

と考えます。

---

# Huskarl

二種類あります。

## Spear Huskarl

- Spear
- Javelin
- Shield
- Glamour
- Stealth

を持ちます。

役割は、

- Screen
- Charge受け
- 接敵前Javelin
- Raider前衛
- Hirdmanの保護

です。

## Axe Huskarl

- Axe
- Javelin
- Shield
- やや重いArmor

を持ちます。

Spear型よりDamageへ寄せやすく、Shieldを保ちます。

## Huskarlの共通弱点

- AoE
- Fatigue
- 高Protection
- Poison
- MR attack
- True Sight

です。

---

# Hirdman

Broad Sword、Shield、Scale armorを持つ精鋭歩兵です。

- Attack
- Defence
- Morale
- Armor
- Stealth
- Glamour

のバランスがよく、正面Army・Raider両方へ使えます。

しかし、Hirdmanだけを大量に作ると、

- Gold不足
- Mage不足
- Siege不足
- Chaff不足

になります。

---

# Mounted Hirdman

Light Lance、Javelin、Shield、Fay Horseを持つ機動兵です。

役割は、

- Charge
- Flank
- Raid
- 追撃
- 高Map Move Army

です。

MountとRiderは別Statsです。

- LanceのCharge
- Mount HP
- Mount Defence
- Mount喪失後
- Terrain
- Retreat

を確認します。

---

# Commander

# Van Scout

Stealth Scoutです。

VanheimではScoutが特に重要です。

敵がStealth国家へ対策を始めたかを確認します。

```text
Patrol
PD
Reserve
True Sight
Lab
Mage
```

を見ます。

---

# Vanherse

A1 G1 H1のSacred Mage-Priest Commanderです。

## Role

- Air support
- Glamour support
- Bless
- Stealth Army command
- Expansion commander
- Light thug
- Blood Sacrifice以外のPriest work

## Light thug

騎乗、高Defence、Glamour、Sacredを活かし、少量装備でPD・小Armyを処理できます。

ただし、

```text
Thugとして使う
＝ Researcher・Priest・Commanderを危険へ出す
```

ことです。

敵Mage・MR attack・Fatigue・Poisonがある場所へ送らないでください。

---

# Vanjarl

A2 G1 B1 H2です。

Vanheimの中核Commanderです。

## Air

- Air support
- Lightning
- Wind
- Defence
- Storm関連
- Air Booster route

## Glamour

- Luck
- Illusion
- Defence
- Mind・Perception
- Glamour Ritual

## Blood

- Blood Hunt
- Blood Sacrifice
- Battle Blood
- Booster・Ritual

## Holy

H2により、

- Bless
- Preach
- Smite等
- Throne Claim条件への寄与
- Blood Sacrifice

を行います。

## 失うと重い

Vanjarl一体の死亡は、

- A2
- G1
- B1
- H2
- Commander
- Stealth leader
- Sacred

を同時に失います。

Rare Item carrierへする場合はBodyguardと退却先を用意します。

---

# Dwarven Smith

国家Start Siteで雇うForge中核です。

## 基礎

- E2
- F/A/E/D/G Random
- Master Smith系Forge能力
- Slow recruitment等の供給制約

があります。

## 分類

Recruit後に、

```text
Pure Earth Smith
Air crosspath
Fire crosspath
Death crosspath
Glamour crosspath
High Earth
```

へ分類します。

## 仕事

- Booster
- Resistance Item
- Thug equipment
- Research Item
- National discount Item
- Crosspath chain

です。

Rare Random個体を通常Item量産で使い潰さず、Access chain用に保存します。

---

# Expansion

## 基本方針

VanheimのExpansionは、

```text
Huskarl / Hirdmanが被弾を避ける
→ Shieldで射撃・Chargeを受ける
→ 高Attack・DamageでIndependentを減らす
→ 損失を抑える
```

ことです。

## Commander

VanherseはExpansion Commanderとして使えますが、高価です。

Cheap commanderが不足する場合、

```text
一軍を増やす
vs
Mage・PriestをResearchへ残す
```

を比較します。

## Independent別

### Archer

Shield Huskarlを前へ置きます。

Mounted Hirdmanだけで突入すると、接敵前の損失が重くなります。

### Cavalry

Spear、Shield、Formation、配置を使います。

### Barbarian

高Damage一撃がDefenceを抜くとVanirが死にます。

数、配置、Javelin、Commander safetyを確認します。

### Heavy Infantry

Axe Huskarl、Hirdman、Mage supportを使います。

### Undead

PriestとMagic Weaponを確認します。

### Elephant・Trample

高DefenceだけではTrampleを止めません。

分散、Morale attack、Damage、Body sizeを考えます。

---

# Expansion評価

```text
Province取得Turn：
Vanir損失：
Commander損失：
二軍完成Turn：
Fort資金：
Mage Recruit：
```

を記録します。

一戦勝利より、

```text
高価な兵を補充せず連戦できるか
```

が重要です。

---

# Economy・Fort

## Gold

VanirとMageが高価です。

毎Turn、

```text
兵
Mage
Fort
Lab
Temple
Item用Mage
```

が競合します。

## Fortの役割

- Vanherse・Vanjarl生産
- Stealth Army出発点
- Coast・Sailing拠点
- Gem・Item受け渡し
- Retreat route
- Border reserve

です。

## Dwarven Smith供給

Start Site依存のSmithを国家全Fortで増やせるとは限りません。

そのためSmith turnを、

- Booster
- Mass Item
- Unique
- Research

へどう割るか決めます。

---

# Pretender

Vanheimでは、少なくとも四案を比較します。

## 1. Imprisoned Scales

国家兵だけでExpansionし、

- Gold
- Productivity
- Growth
- Research
- Dominion

を増やします。

向く場合：

- Expansionが安定
- Light Blessで十分
- Smith・Mage・Fortを増やしたい

## 2. Light Bless＋Scales

Vanherse・Vanjarl・Sacred兵の弱点を一つ補います。

候補の方向は、

- Defenceの上積み
- Protection
- Reinvigoration
- Resistance
- Attack
- Magic Weapon

です。

Bless名を先に選ばず、Replayで弱点を確認します。

## 3. Dormant Diversity

Astral、Water、Nature等を補います。

- Mind protection
- Booster
- Summon Mage
- Resistance
- Global

へつなげます。

## 4. Awake Expander

危険なCapital周辺をPretender本人で取り、Vanir Armyを別方向へ回します。

Design Pointと死亡RiskをScales案と比較します。

---

# Research

VanheimのResearchは、敵とGame planで変わります。

## Alteration

- Self buff
- Defence
- Protection
- Elemental adaptation
- Glamour support

## Construction

- Dwarven Smith
- Booster
- Resistance
- Thug Item
- Research Item

## Enchantment

- Air support
- Army-wide effect
- Resistance
- Blood・Death support

## Evocation

- Lightning
- Air damage
- Battlefield pressure

## Thaumaturgy / Glamour

- Mind
- Perception
- MR attack
- Dream・Illusion

## Blood

- Blood Huntの用途
- Sabbath
- Demon
- Battle support
- Blood Sacrificeと別のSlave消費

## Conjuration

- Elemental
- Summon Mage
- National summon
- Late-game access

---

# First war plan

```text
目的：
敵Main Army：
敵Counter：
正面Army：
Stealth Army：
Research：
Gem：
Item：
Sailing route：
撤退条件：
```

を決めます。

## 正面Army

- Huskarl Screen
- Hirdman Damage
- Mounted flank
- Vanherse / Vanjarl support
- Scout
- Serf Siege

## Stealth Army

- 最小Raider
- Stealth Commander
- 退却先
- 明確なTarget

## Item

敵に応じて、

- Shock Resistance
- Fire Resistance
- Poison Resistance
- MR
- Fatigue
- Magic Weapon

を用意します。

---

# Battle Scriptの骨格

## Vanherse

```text
Buff
Buff
Air / Glamour support
Attack / Retreat
```

## Vanjarl

```text
必要Resistance
Army support
Battlefield control
Damage / Hold
```

## Dwarven Smith

通常は後方でForge・Researchです。

前線へ出すなら、Rare Randomを失う価値があるか確認します。

---

# Stealth作戦

## 正面固定＋後方Raid

```text
Main Army
→ Border Fortを包囲

Stealth Army
→ Tax route・Lab・Templeへ侵入
```

敵は、

- Fort relief
- Raider迎撃
- Capital防衛

へ戦力を分けます。

## False pressure

小Raiderを複数方向へ見せ、Main Armyの本命を隠します。

## Sailing

Coast・海路を使える場合、敵の陸上Chokeを迂回します。

## Assassin対策

敵もStealthを使います。

Vanjarl・SmithへBodyguard、Patrol、Fortを用意します。

---

# Counter

## True Sight・Mindless

Glamour・Illusionの一部を弱くします。

通常Damage、Air、Blood、Itemへ切り替えます。

## AoE

高Defenceを無視して複数Vanirへ当たります。

分散、Resistance、射撃・Caster狙いを使います。

## Fatigue

長期戦でDefenceが落ちます。

Reinvigoration、短期決戦、Mage supportを用意します。

## MR attack

HP・Defence・Protectionを無視します。

MR、Antimagic、Caster assassination、Raidを使います。

## High Protection

Spear・Swordだけでは通りにくい相手へ、

- Axe
- Lightning
- Blood
- Item
- Summon
- Fatigue

を使います。

## Poison

HPが低めのVanirへ累積します。

Resistance、Healer、短期決戦を用意します。

## Patrol・Reserve

Stealth Raidが止まります。

大きなRaiderで無理に突破せず、Main Armyへ価値を戻します。

---

# Magic Access

## 保証Layer

- A2
- G1
- B1
- H2
- Start SiteのE2

## Random Layer

Dwarven SmithとVanjarlのRandomで、

- Fire
- Air
- Earth
- Death
- Glamour
- Blood

が広がります。

## Missing Path

- Astral
- Water
- Nature

を優先的に評価します。

## Summon Dwarf

高いAir・Earthへ届くと、国家召喚でさらにPathを広げられる可能性があります。

Research、Booster、Pretender、Candidate poolを確認します。

---

# Multiplayer

## 敵から見たVanheim

敵は、

- Stealth Raid
- Sailing
- Vanjarl thug
- Glamour spell
- Blood Sacrifice
- Dwarven Item

を警戒します。

## 見せる情報

- Borderを明確にする
- Raiderが入っていない方向
- Formal agreement
- Throne intent

## 隠す情報

- Stealth Armyの数
- Dwarven Smith Random
- Booster
- Blood Slave
- Sailing route
- Main Armyの本命

## 外交

Stealth国家は、存在するだけで隣国に高いPatrol・PDを強制します。

その圧力を、

- Border agreement
- 共同戦争
- Gem trade
- Threat deterrence

へ使います。

---

# よくある失敗

## 1. Vanirだけで全部行う

Serf、Mercenary、Summonへ安い仕事を移します。

## 2. Stealth Armyを大きくしすぎる

正面Armyがなくなります。

## 3. Defenceを無敵と思う

AoE、Fatigue、Harassmentへ崩れます。

## 4. Dwarven Smithを毎Turn同じItemへ使う

Rare RandomとAccess chainを分類します。

## 5. Constructionだけ研究する

Itemを使うBattle Spellが必要です。

## 6. VanjarlをThugとして失う

A2G1B1H2とCommanderを失います。

## 7. Blood Huntを用途なしで始める

Population・Unrest・Researchを失います。

## 8. Scout reportを完全情報と思う

敵にもStealth・Magic Phaseがあります。

---

# Test game

```text
Turn：
Expansion Province：
Vanir損失：
二軍完成：
第二Fort：
Vanherse数：
Vanjarl数：
Smith分類：
第一Research：
最初のItem：
最初のRaid：
Raidで敵が動かした戦力：
First war用Gem：
Missing Path：
```

---

# End Turn checklist

```text
[ ] Stealth Armyへ非Stealth Unitが混ざっていない
[ ] VanjarlのRoleを一つに決めた
[ ] Smith Randomを分類した
[ ] Raiderに退却先がある
[ ] Main ArmyにSiege要員がいる
[ ] Scout reportを確認した
[ ] Blood Slaveの用途がある
[ ] Sailing routeをMapで確認した
[ ] True Sight・AoE・MRへの第二案がある
[ ] Fort・Throne防衛をRaiderより優先した
```

---

# 関連ページ

- [Stealth・Glamour・特殊作戦](../../systems/stealth-glamour.md)
- [Magic Path: Glamour](../../magic/paths/glamour.md)
- [Magic Path: Air](../../magic/paths/air.md)
- [Blood Economy](../../magic/blood-economy.md)
- [Thug装備](../../items/thug-equipment.md)
- [Pretender設計サンプル](../../pretender/samples.md)
- [ターン処理順](../../reference/turn-resolution.md)
