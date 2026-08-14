---
title: Air
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-14"
---

# Air

**Airは、鎧を無視するShock、射撃防御、飛行、Storm、Magic Phase移動によって「どこで、誰と戦うか」を支配するPathです。**

Fireが敵Armyを速く焼くPathなら、Airは高Protectionという長所を無効化し、敵後方・孤立部隊・重要Casterへ直接圧力をかけます。

---

# Airの勝ち筋

## Armor Negating Shock

Lightning系Spellの多くはArmor Negatingです。

そのため、

- 重装歩兵
- Earth Buff軍
- 高Protection Giant
- 高価なArmorを着たThug

に対して強力です。

Protection 30でもShock Resistanceが0なら脆い一方、Shock Resistanceを十分に積まれると火力が急落します。

## Magic Phase機動

Cloud Trapeze等でCommanderをMagic Phaseに移動させ、通常移動前に戦闘を起こします。

用途：

- 孤立Commanderの排除
- Raider迎撃
- Fort建設中のProvince攻撃
- Remote attackと通常軍の連携
- Enemy retreat先の遮断
- Throne戦への急行

## 射撃対策

Air Shield、Arrow Fend、Mist、Storm等で、弓・Crossbow・Arbalestへの生存性を上げます。

高価な軽装SacredやMage軍にとって、Protectionを上げるより射撃命中そのものを減らす方が効率的な場合があります。

## FlyingとMass Flight

Armyの移動・接敵方法を変えます。

- 敵前衛を飛び越える
- 地形・障害物の影響を減らす
- Rear attackを高速化
- 通常では届かないProvinceへ侵入

ただしStorm、敵のFlying迎撃、後方長槍、着地点の密集を考えます。

## Storm戦術

Stormは射撃、飛行、Precision、特定Spell、Air MageのPath boostへ関わります。

自軍だけStormを利用できるようにすると、敵射撃・飛行を弱体化しながらAir Spellを強化できます。

---

# Path level別の役割

| Path | 主な役割 |
|---:|---|
| A1 | Air Shield、Precision / Wind補助、Forge、Crosspath |
| A2 | Mistform系、Cloud Trapeze、実用Support Mage |
| A3 | Lightning / Thunder Strike級の砲兵、Storm利用 |
| A4 | Arrow Fend、Mass Flight、Fog / Army-wide defense |
| A5以上 | Wrathful Skies級、Global、戦場全体の支配 |

覚え方：

- **A2**：移動・自己防御
- **A3**：砲兵
- **A4以上**：Armyの司令塔

A1 Mageも、Storm Power、Item、Communionを使える国家では実戦価値が大きくなります。

---

# Researchの方向

## Evocation

- Lightning Bolt
- Thunder Strike
- Shock Wave
- Chain / Storm系Shock
- Battlefield-wide lightning

高Protectionへの主火力です。

## Alteration

- Air Shield
- Mistform
- Mirror / displacement系
- Body / speedの変化

Thug、Sacred、Mageの生存性を上げます。

## Enchantment

- Arrow Fend
- Storm
- Flight / Army movement
- Wrathful Skies等のBattlefield effect
- Shock Resistance

Army全体と戦場環境を変えます。

## Conjuration

- Air Elemental
- Storm Power系Path boost
- Air Mage・Flying unit召喚

Air ElementalはTrample、飛行、Ethereal等で通常兵へ強力ですが、Magic Weapon、高Size、高Damage、Shock Resistance等を確認します。

## Thaumaturgy / Ritual

- Cloud Trapeze
- Scrying
- Weather / map manipulation
- Remote attack

戦略機動と情報戦を作ります。

## Construction

- Air Booster
- Shock Resistance Item
- Wing / flight Item
- Research Booster
- Precision / Range補助

Rare Air accessをBooster chainで伸ばす価値があります。

---

# 重要Spellの見方

## Air Shield

射撃を受ける高価なUnitへ有効です。

Protectionが低いままでも、矢が当たらなければ生存できます。AoE Spell、Magic Missile、近接攻撃には別対策が必要です。

## Mistform

大きな一撃を軽減し、ThugやMageの事故死を減らします。

Magic damage、Shock、十分なDamage、特定効果で解除される可能性があるため、Mistformだけで無敵にはなりません。

## Cloud Trapeze

A2級CommanderをMagic Phase Raider / Interceptorへ変えます。

使用前に、

- 到着後の戦闘Script
- 帰還経路
- Enemy PD / Mage
- Dome
- Retreat先

を確認します。

## Thunder Strike

高Damage・範囲Shockを与える代表的なAir Evocationです。

強力ですがFatigueが重く、A3 Mageを一人置くだけでは数発で停止します。

- Path boost
- Gem
- Reinvigoration
- Communion
- 複数Caster

で砲列を作ります。

## Storm

敵射撃と通常Flyingを弱め、Storm PowerやStorm対応Unitを活かします。

自軍ArcherやFlying Sacredも弱体化するため、Army全体をStorm前提で組みます。

## Arrow Fend

Army-wide射撃防御です。

Crossbow国家、Flaming Arrows、Massed Bowに対する研究Counterになります。

## Fog Warriors

ArmyへMistform系防御を配る高級Spellです。

通常物理軍を急に無力化できますが、Magic damage、AoE、Shock等で効果を剥がされます。

## Wrathful Skies

戦場全体へ継続Shockを与えます。

自軍Shock Resistance、Caster生存、Storm環境、戦闘時間が揃えば勝利Spellになります。

---

# 戦場での使い方

## Thunder Strike砲列

```text
前衛：盾 / Chaffで固定
Air Mage：Storm / Path boost
Air Mage群：Thunder Strike系
Support：Shock Resistance / Fatigue回復
```

敵を一Squareへ密集させる拘束Spellと相性があります。

## 射撃無効化

```text
Air Shield / Arrow Fend
+ 大盾前衛
+ Storm
+ Fast unitでAttack Archers
```

一つの防御だけでなく、命中率・射線・後衛圧力を重ねます。

## Magic Phase迎撃

Enemy Raiderが次に攻めるProvinceを予測し、Cloud Trapeze Casterを先に着地させます。

これは単独Thugだけでなく、Battle Mageを必要な戦場へ即時投入する用途にもなります。

---

# Ritual・召喚・経済

## Site Search

Air SiteはAir Gem、Air Mage、Flying unit、Precision / Weather / movement効果を持つ場合があります。

## Air Elemental

接敵直後に後衛へ到達しやすく、ChaffをTrampleできます。

敵のSize、Magic Weapon、Shock Resistance、Bodyguardを見ます。

## Flying Commander / Mage召喚

戦略移動、Raid、Magic diversityを開きます。Mage召喚は新Path Boosterへの入口になることがあります。

## Global

Wind、Storm、Air income、移動、世界規模Shock等へ関わります。自軍構成と外交影響を確認します。

---

# 相性のよいPath

## Water

Quickness、Cold、Storm、飛行でTempoを支配します。Air / Water Crosspathは天候・射撃・機動に強い傾向があります。

## Earth

AirがAN Shockを担当し、Earthが前衛のProtectionと拘束を担当します。敵はProtectionとShock Resistanceの両方を要求されます。

## Astral

CommunionでA3～4へ届き、AntimagicやTeleportを補います。Magic Phase戦略も強化されます。

## Glamour

Luck、Illusion、Stealth、Flightを重ね、高価な少数精鋭や奇襲Armyを作ります。

## Nature

Shock Resistance、Regeneration、Fatigue回復でAir Mageと前衛を支えます。

---

# Counter / 弱点

## Shock Resistance

最も明確な火力Counterです。

相手がThunder Ward等を用意したら、

- Fire
- MR attack
- Poison
- Earth buff兵
- Cold

へ分散します。

## Fatigue

Thunder Strike等はCaster負担が重く、Mageが少ないと攻撃が続きません。

## Stormの自己妨害

自軍の、

- Archer
- Flying unit
- Precision依存Spell

も影響を受けます。Storm casterだけを追加してもArmyが強くなるとは限りません。

## 分散・高HP

大AoEは密集軍に強く、散開した高HP Unitには一発あたりの効率が下がります。

## Mage狩り

Air戦術は高価なCasterとBattlefield conditionへ依存します。Assassin、Remote attack、Magic Duel、Attack Rearを警戒します。

## Dome

Cloud TrapezeやRemote ritualはDomeで妨害・反撃される場合があります。

---

# Airを選ぶ判断

- 敵は高Protection・低Shock Resistanceか
- A3以上を何人用意できるか
- Fatigueをどう管理するか
- Stormは自軍へ有利か
- Archer / FlyingへのCounterが必要か
- Cloud Trapeze後にCasterが勝てるか
- Shockが止まった場合の第二Damage typeはあるか

---

## 関連ページ

- [Magic Path総論](index.md)
- [Research](../research.md)
- [Gem](../gems.md)
- [Path Boosting](../boosting.md)
- [命令とBattle Script](../../basics/orders.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [illwiki: Air Magic](https://illwiki.com/dom5/dom6/air)
