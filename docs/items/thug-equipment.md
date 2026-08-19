---
title: Thug・Supercombatant装備
status: expanding
verified_version: "6.35"
last_verified: "2026-08-19"
---

# Thug・Supercombatant装備

Thugは、少数のMagic ItemとSelf Buffで、弱いProvince Defence、小部隊、特定のEnemy Commanderを処理するCommanderです。

Supercombatant（SC）はさらに多くのArmyを単独または少数で相手にします。

重要なのは「装備を全部埋める」ことではありません。

> **任務を決める → その任務に必要な防御と攻撃だけを買う**

のが基本です。

正確なItemの要求Path・Construction・効果は[Magic Itemデータ索引](../data/items/index.md)と[Dom6 Mod Inspector](https://larzm42.github.io/dom6inspector/)で確認し、このページではLoadoutの考え方とCounterを扱います。

---

# ThugとSCの違い

| 項目 | Thug | Supercombatant |
|---|---|---|
| 主な対象 | PD、小部隊、Raider、特定Thug | Army、大規模PD、主力Commander |
| Item投資 | 少～中 | 中～大 |
| 損失許容 | 比較的高い | 低い |
| 目的 | Map control、交換 | 主力戦力、決戦 |
| Counter | 限定的対策でも倒れる | 複数Counterへ耐える必要 |

HP15～20の人間Commanderへ高価なArtifactを集中させても、SCにはなりません。

---

# 最初に決める任務

## PD Raider

弱いProvince Defenceを倒し、Enemy Incomeと移動経路を壊します。

必要：

- Magic Weaponまたは十分なDamage
- 小Damage多数への防御
- Morale
- Fatigue管理
- Retreat / Strategic movement

## Anti-Thug

Enemy Thugを倒します。

必要：

- Enemy防御を突破する専用Weapon
- Enemy Damage typeへのResistance
- MR
- 命中
- Bodyguard / 支援兵

## Army同行型

自軍前衛に守られながら、高Protection、Giant、Commanderを処理します。

単独生存性を減らし、攻撃Itemへ投資できます。

## Assassin

一対一またはBodyguard込みの小戦闘です。

- Swarm / Summon
- Fear / Awe
- Poison
- Fatigue
- Returning
- Escape

が通常Army戦より重要です。

## Mage-Thug

Self Buff後に近接戦へ移ります。

Script時間、Spellcasting Encumbrance、Gem、Interruptを管理します。

---

# Chassisを見る

Itemを作る前にCommanderの素能力を見ます。

## HP

Regeneration、一撃死耐性、継続Damageへの余裕の土台です。

## Protection / Natural Protection

良いArmorを最初から持つなら、新ArmorをForgeする必要がありません。

## Defence

Shield、Weapon、Quickness、Encumbranceとの相性を決めます。

## Attack

高価なWeaponを当てられるか確認します。

## Strength

武器Damageへ影響します。高Strength Chassisは高Damage Weaponを活かしやすくなります。

## MR

Soul Slay、Charm、Paralyze、Controlへの耐性です。人間Commanderは低いことがあります。

## Encumbrance

長期戦とMage-ThugのFatigueを決めます。

## Size

Trample、包囲、Square密度、射撃対象、Mountとの関係があります。

## Recuperation / Regeneration / Reinvigoration

Item投資を減らせる固有能力です。

## Strategic movement

Raidの価値を決めます。戦闘では強くてもMap Moveが遅いChassisはProvinceを多く取れません。

---

# 装備の六層

## 1. 敵へ当てる

- Attack bonus weapon
- Precision / target補助
- 拘束支援
- Multiple attack
- Awe / Fearで敵攻撃を減らす

高Damageでも当たらなければ価値がありません。

## 2. 敵を倒す

- Magic Weapon
- Armor Piercing / Negating
- Life Drain
- AoE
- Armor破壊
- Anti-undead / Demon
- MR / Soul attack

Enemy defenceを見て選びます。

## 3. 通常攻撃へ耐える

- Armor
- Helmet
- Shield
- Defence
- Mistform / Ethereal / Luck
- Invulnerability

## 4. 魔法へ耐える

- Fire / Cold / Shock / Poison Resistance
- MR
- Antimagic
- 視認妨害が問題ならSpirit Sight / True Sight
- Returning等の生存・離脱手段

## 5. 戦い続ける

- Regeneration
- Reinvigoration
- Life Drain
- HP
- Recuperation

## 6. 任務を完了する

- Flying / Teleport
- Water Breathing
- Stealth
- Siege / Patrol
- Leadership
- Retreat route

---

# 最小装備

Thugは一個か二個の安価Itemだけで任務を達成できる場合があります。

例：

```text
既に良いArmorとShieldを持つCommander
+ Magic Weapon
+ 命中Item
= Etherealを含む弱PD Raider
```

```text
高HP Regeneration Chassis
+ 敵の主DamageへのResistance
= 通常PD / 小部隊へ低投資で投入
```

すでに持つ能力へItemを重複させないことが重要です。

---

# 攻撃装備

## Magic Weapon

Ethereal、Invulnerability等、通常の非Magic Weaponでは効率が落ちる相手への基本Counterです。

Etherealは「見えない」ことが本質ではないので、True Sight / Spirit Sightだけでは代用できません。

## 高Damage両手武器

高Strength Chassisへ向きます。

Shieldを失うため、射撃・多段攻撃への防御をSpellや素Statsで補います。

## AoE weapon

大量Chaffを処理し、包囲・Harassmentを減らします。

高Protection・高HP単体へのDamageは不足する場合があります。

## Life Drain weapon

DamageとHP / Fatigue回復を同時に行います。

対象のUnit classificationやDrain immunity等によって有効性が変わるため、戦う相手を確認します。

## Armor破壊

高Protection ThugへArmor damage weapon等を使い、後続攻撃を通します。

## Regenerationを越える

Regenerationは毎RoundのHP回復なので、Counterの基本は**回復量より速く勝つ**ことです。

- 大きなBurst Damage
- AP / AN等で継続的に高Damageを通す
- 多数攻撃で回復を上回る
- Fatigueで行動不能へする
- Soul Slay、Charm、Paralyze等、HP回復とは別軸で倒す

Poisonは長期的なDamage源にはなりますが、Regeneration側もPoison Damageで失ったHPを回復できます。Poisonを「Regenerationを止める効果」として扱わず、実際に蓄積Damageが回復量を上回るかを見ます。

DiseaseもRegenerationを直接停止する万能Counterではありません。戦略Map上の長期消耗と、一戦でのThug撃破を分けて考えます。

---

# 防御装備

## ArmorとHelmet

BodyだけでなくHead Protectionを揃えます。

重すぎるArmorはDefenceとFatigueを悪化させます。

## Shield

多数の通常攻撃と射撃へ強くなります。

AN、MR attack、Poisonには別防御が必要です。

## Defence

高Defenceは少数の敵へ強い一方、多数の攻撃によるHarassmentで下がります。

## Mistform / Ethereal / Luck

Protectionとは別の防御層です。ただしCounterは同じではありません。

- Ethereal → Magic Weapon / Magic Damage
- 視認妨害・Blur・Displacement等 → True Sight / Spirit Sightが有効な場合
- Mistform → 個別の解除条件・Damage interactionを確認
- Luck → 一撃の生存率を上げるが、Fatigue / Control /継続Damageは別問題

「True SightがあるからEtherealやMistformまで無効」という扱いはしません。

## Elemental Resistance

Enemy MageがいるProvinceへ固定装備でRaidしないでください。ScoutでDamage typeを確認します。

## MR

高価なItemを積んだCommanderほどMR attackの価値ある標的になります。

---

# Sustain

## Regeneration

最大HPに対する割合回復なので、高HPほど一回の回復量が大きくなります。

継続的な小DamageやPoison Damageを受ける戦闘でも生存時間を延ばしますが、一撃死、回復を上回るDamage、Fatigue lock、MR attack等には別対策が必要です。

## Reinvigoration

Quickness、Berserk、Heavy armor、Self Buff、長期戦へ必要です。

## Life Drain

対象に有効な場合、DamageとSustainを同時に確保できます。

## Recuperation

戦闘後に回復可能なAfflictionを治し、長期Raidの交換効率を上げます。

---

# Self Buff Script

Mage-Thugの基本：

```text
1. Path boost
2. Elemental / MR defence
3. Physical defence
4. Regeneration / Sustain
5. Attack
```

### 問題

- 5Roundかかる
- EnemyがRound 2に到着
- Gemを消費
- Interrupt
- Script対象なしで飛ばされる

初期配置を後ろへし、必要ならChaffを前へ置きます。

---

# PD Raiderの基準

PDの質は国家とProvinceで異なります。

確認：

- Spear / Pike
- Crossbow
- Cavalry
- Priest
- Mage / national PD
- Commander weapon
- Magic Weapon
- Province terrain
- PD level

同じ「PD 10」でも安全性は違います。

## テスト

Single PlayerやTest gameで、

- PD 1
- PD 6
- PD 11
- PD 21

へ当て、HP、Fatigue、Rout、Afflictionを確認します。

---

# Anti-Thug装備

Enemy Thugの防御を分解します。

| Enemy defence | Counter |
|---|---|
| 高Protection | AP / AN、Armor破壊、MR attack |
| 高Defence | 高Attack、多段、拘束 |
| Ethereal | Magic Weapon / Magic Damage |
| 視認妨害・Blur等 | True Sight / Spirit Sightが有効か確認 |
| Mistform | Magic Damage、十分なDamage、解除条件を確認 |
| Regeneration | Burst、継続高Damage、Fatigue、Soul / Control attack |
| Fire Shield | Fire Resistance、射撃、MR attack |
| High MR | Physical / Elemental |
| Invulnerability | Magic Weapon、Elemental |
| Awe | Morale、Berserk、射撃、Mindless |
| Fear | Morale、Undead / Mindless、Sermon |

一人のCommanderだけで解決せず、Mage、Crossbow、Chaff、Priestを組み合わせます。

---

# Supercombatant

SCは複数のCounterへ同時に耐える必要があります。

最低限考えるもの：

- 通常兵
- 高Damage AP / AN
- Shock等のElemental Damage
- Soul Slay / Charm
- Fatigue
- Poison
- Life Drain
- Horror
- Paralyze / Entangle
- Flying / Retreat blocking
- Anti-undead / Demon / Sacred

完全無敵ではなく、**敵がCounterへ払う研究・Gem・Mage turnを増やす**ことがSCの価値です。

---

# 投資上限

Chassisが安くても、Itemを積むと高価になります。

```text
Total cost
= Chassis cost
+ Item Gem
+ Forge turn
+ Booster / Construction研究
+ 戦闘Gem
+ 失った場合のEnemy loot / Carrier価値
```

同じGemで、

- Elementalを複数召喚
- Army-wide Buff
- Research Item
- Booster

を作る選択と比較します。

---

# Retreatと回収

Thugが勝てない場合に逃げられるか確認します。

- Friendly隣接Province
- Enemy movement
- Magic Phase battle順
- Flying / Teleport帰還
- Returning
- Rout時の退路

**RoutしただけでItemを失うわけではありません。** Commanderが生還して退却できれば装備は残ります。問題は退路がなく死亡すること、Assassination等でCarrier自体を失うことです。

---

# よくある失敗

## 完全装備してから任務を考える

先に対象を決めます。

## 人間Commanderへ過剰投資

HPとMRの低さは高価なArmorだけで解決しません。

## MRを無視

Soul Slay等のMR attackで高投資を失う可能性があります。

## Elemental Resistanceを固定

敵ごとにDamage typeが違います。

## Regenerationで無敵と思う

Burst、回復を上回る継続Damage、Fatigue、Soul / Control attackがあります。

## Poison / DiseaseをAnti-Regenと一括りにする

PoisonはDamage源、Diseaseは別の長期消耗mechanicです。Regenerationを直接OFFにする能力として扱わないでください。

## True SightをEthereal Counterにする

EtherealにはMagic Weapon / Magic Damageを用意します。

## Retreat先なし

Routが死亡へ直結します。

## Armyを倒そうとしすぎる

Thugの本来目的はProvince、Income、Tempoです。Enemy主力Armyを避けます。

---

# 装備設計テンプレート

```text
任務：PD Raid / Anti-Thug / Army同行 / Assassin
対象：
Carrier素Stats：HP / Prot / Def / MR / Enc / Move
必要な攻撃：
必要なResistance：
Sustain：
Mobility：
Self Buff：
Gem携行：
退路：
Total Gem：
失ってよいか：
```

---

## 関連ページ

- [Magic Item](index.md)
- [Forge計画とConstruction Breakpoint](forge-planning.md)
- [Resistance Item](resistance-items.md)
- [Booster](boosters.md)
- [Magic Itemデータ索引](../data/items/index.md)
- [両手武器・片手武器・盾](../basics/weapons-and-shields.md)
- [命令とBattle Script](../basics/orders.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
