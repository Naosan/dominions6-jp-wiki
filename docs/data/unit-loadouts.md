---
title: Unit装備・Mountの読み方
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-14"
---

# Unit装備・Mountの読み方

国家Recruitページでは、Unitの基礎能力値だけでなく、**実際に参照しているWeapon・Armor・Mount record**を結合して表示します。

- [全国家Recruitデータ](recruitment/index.md)
- [Weapon・Armor・Damage data](combat/index.md)
- [両手武器・片手武器・盾](../basics/weapons-and-shields.md)
- [戦闘ルール](../basics/combat-rules.md)

!!! info "自動生成の役割"
    このページ群は「そのUnitが何を装備しているか」を確認するための事実索引です。どの兵を何割雇うか、どの敵へ当てるか、BlessやBuffをどう組むかは国家攻略で扱います。

---

## データの結合方法

Dominions 6のUnit recordには、主に次の参照があります。

```text
Unit
├ wpn1 ... wpn7      → Weapon record
├ armor1 ... armor4  → Armor record
└ mountmnr           → Mount側のUnit record
```

Weapon recordからは、基礎Damage、Attack / Precision補正、Defence補正、Length / Range、攻撃回数、Damage type、AP / AN、Secondary effect等を取得します。

Armor recordからは、Body / Head / Shield Protection、Parry、通常Defenceへの補正、Encumbrance、Map movement penalty等を取得します。

Mountは単なる装備品ではなく、**別のUnit record**です。そのためRiderとMountは、HP、Protection、Defence、Morale、武器、防具を別々に持ちます。

---

# Recruitページの二つの表

各Recruit区分には、原則として二種類の表があります。

## 基礎能力表

| 項目 | 主な意味 |
|---|---|
| Size | Square占有、標的Size、Trample等に関係 |
| HP | RiderまたはUnit本体のHP |
| Prot | Unit record上の表示Protection |
| MR | Magic Resistance |
| Mor | Morale |
| Str | 近接Damageや投擲Range等の土台 |
| Att | Unit本体のAttack Skill |
| Def | Unit本体のDefence Skill |

この表は「最終的にゲーム画面へ表示されるUnit能力」を把握するために使います。

## 装備・Mount表

| 列 | 内容 |
|---|---|
| Weapons | Unitが参照するWeapon record |
| Armor | 盾、胴鎧、兜、Misc防具 |
| Mount | Mount側のUnit能力・攻撃・防具 |
| Profile | 盾持ち、両手、射撃、AP、AN、Charge等の簡易タグ |

基礎能力表と装備表は競合するものではありません。

```text
Unitの表示能力
＋
Weaponの攻撃Profile
＋
Armorの部位別Profile
＋
Mountの別Profile
```

を重ねて読むためのものです。

---

# Weapon欄

Weapon欄では、次のような形式で表示します。

```text
Spear #1 — Dmg 3+STR; Att +0; Def +0; Len 3; Pierce; Nonmagical
```

## Dmg

Weapon recordの基礎Damageです。

`3+STR`なら、基礎Damage 3に装備者のStrengthが加わることを示します。`STR/2`や`STR/3`の場合はStrengthの一部だけが加わります。

ただし、実際の最終Damageには次が関係します。

- UnitのStrength
- Two-handedによるStrength利用
- Charge
- Bless
- Strength of Giants等のBuff
- FatigueやAffliction
- Mount / Riderのどちらが攻撃するか

したがってWeapon欄のDmgだけで、Unitの最終攻撃力を決めないでください。

## Att / Prec

近接WeaponではAttack補正、射撃WeaponではPrecision補正です。

Unit本体のAttack SkillにWeapon補正を加えて命中能力を考えます。高DamageでもAttack補正が低ければ、高Defence相手へ安定して当たりません。

## Def

近接Weaponが持つDefence補正です。

SwordやQuarterstaffのように防御へ寄与するWeaponもあります。両手WeaponでもDefence補正が高いものがあるため、「盾がないから必ずDefenceが低い」とは限りません。

## Len

Weapon Lengthです。Repelと接近戦の間合いに関係します。

Lengthは両手・片手とは別の値です。PikeやGreat Spearは長い一方、両手武器でも短いものがあります。

## Damage type

- Slash
- Pierce
- Blunt
- Fire
- Cold
- Shock
- Poison
- Acid
- Magic damage
- True / Internal damage

等を表示します。

Damage typeとAP / ANは別概念です。`Pierce`だから必ずArmor Piercingとは限りません。

## Properties

主要なPropertyを表示します。

- 両手
- AP / AN
- Charge
- 盾無視
- Defence Negate
- MR Negates
- Soul Slay
- Repel不可 / Repelされない
- 騎乗時のみ / 徒歩時のみ
- Flail系の対盾Attack補正
- Magic weapon / Nonmagical

`Magic weapon`はEthereal等への命中に関係します。Armor Negatingを意味するものではありません。

## Secondary effect

Weaponが別Weapon recordを追加効果として参照する場合に表示します。

```text
On damage: Poison #...
Always: Shock #...
```

のような区別があります。

ただしSecondary effectには、命中時、Damage通過時、常時、特定対象のみ等の条件があります。厳密な発動条件はゲーム内詳細とBattle Replayでも確認してください。

---

# Armor欄

Armor欄は、盾・胴鎧・兜を分けて表示します。

## 盾

例：

```text
Kite Shield #3 — Shield Prot 19; Parry 6; Def -2; Enc 2
```

### Shield Protection

Shield Hitになったときに関係するProtectionです。

Unitの通常Protectionへ常時そのまま足される値ではありません。

### Parry

通常Defenceを突破した攻撃を、盾で受ける範囲に関係します。

### Def

盾の重さによる通常Defenceへの補正です。大盾はParryが高い一方、通常Defenceを下げる場合があります。

### Enc

盾のEncumbranceです。長期戦とFatigueへ影響します。

---

## 胴鎧

例：

```text
Chain Mail Hauberk #... — Body Prot 18; Def -1; Enc 1; Map penalty 2
```

### Body Protection

Torso / Upper / Lower zoneから、Inspectorと同じ表示式で算出した装備単体のBody Protectionです。

次は含みません。

- Natural Protection
- Helmet
- Shield Hit
- Stoneskin / Ironskin
- Marble Warriors
- Bless
- MountのArmor

Unit基礎表の`Prot`と、装備欄の`Body Prot`が同じとは限りません。

### Map penalty

重いArmorがStrategic movementへ与える装備側Penaltyです。UnitのTerrain Survival、Mount、国家能力、特殊移動を含む最終Map Moveとは別です。

---

## 兜

Head Protectionを表示します。

Body Armorが強くても、Helmetが弱ければHead Hitで倒されることがあります。Blunt攻撃や頭部命中率を上げる特殊Weaponを相手にするときは、Body Protectionだけを見ないでください。

---

# Mount欄

Dominions 6ではRiderとMountが別々にDamageを受けます。

Mount欄では、次を表示します。

- Mount名とUnit ID
- HP
- Protection
- MR
- Morale
- Defence
- Map Move
- AP
- Mount自身の攻撃
- Mount自身のArmor / Barding

## RiderとMountを分けて読む

たとえば騎兵にLanceとHorse Hoofがある場合、両方が同じ身体から出る一つの攻撃Profileではありません。

- Rider：Lance、Sword、Bow等
- Mount：Hoof、Bite、Trample等

という別の攻撃主体です。

AoE攻撃では、RiderとMountの双方がDamageを受ける場合があります。Mountが倒されてもRiderが徒歩で残る場合があります。

## 条件付きWeapon

一部Weaponには、

- 騎乗時のみ
- 徒歩時のみ

という条件があります。

Mountを失った後に、同じWeapon構成・Defence・Combat Speedで戦い続けるとは限りません。

## 現在の限界

自動表は`mountmnr`で参照されるMount recordを表示しますが、次は完全には再構成しません。

- Dismount後の完全なShape / Sprite / Weapon切替
- Regain Mountの全挙動
- RiderとMountのTarget分配
- Bardingを含むゲームUI上の最終表示
- Conditional attackの実際の順序

重要な騎兵はゲーム内詳細とBattle Replayでも確認してください。

---

# `×2`と複数Weapon

同じWeapon IDがUnit recordの複数Slotに現れる場合、`×2`のようにまとめます。

これは「そのWeapon recordが二回参照されている」ことを示しますが、必ずしも単純に毎Round二回、Penaltyなしで攻撃することを保証しません。

次が関係します。

- Ambidextrous
- Weapon Length
- 二刀流Penalty
- Intrinsic weapon
- 攻撃回数をWeapon自身が持つか
- 騎乗時 / 徒歩時条件
- Single-use weapon
- Ammunition
- Secondary effect

したがって、`複数武器`と`武器内多段`を分けて表示しています。

---

# Profileタグ

Profile列は、装備構成を素早く走査するための補助です。

| タグ | 意味 |
|---|---|
| 盾持ち | Shield recordを持つ |
| 両手武器 | Two-handed propertyを持つWeaponがある |
| 射撃 | Ranged Weaponがある |
| AP / AN | 対Armor propertyを持つ |
| Charge | Charge propertyを持つ |
| 盾無視 | Ignore Shieldsを持つ |
| Defence Negate | Defence判定への特殊効果を持つ |
| MR Negates | MR判定を持つWeaponがある |
| Soul Slay | Soul Slaying propertyを持つ |
| 武器内多段 | 一つのWeapon recordが複数Attackを持つ |
| 複数武器 | Unitが複数Weapon IDを参照する |
| Ambidextrous | Unit側にAmbidextrousがある |
| 騎乗 | MountまたはMounted属性を持つ |

Profileは攻略評価ではありません。たとえばAP武器を持っていても、Attackが低い、Damageが小さい、Unitが高価、射程が短い等の理由で主力Counterにならない場合があります。

---

# 実戦での読み方

## 高Protection相手

1. Unit基礎表でStrengthを見る
2. Weapon欄で基礎DamageとStrength加算を見る
3. AP / ANの有無を見る
4. Attack補正とLengthを見る
5. 相手の盾、Defence、Resistanceを見る

## 高Defence相手

1. Attack SkillとWeapon Attack補正を見る
2. 複数Weapon・多段攻撃を見る
3. Flail、Defence Negate、AoE、拘束を探す
4. 一撃のDamageだけで判断しない

## 射撃相手

1. Shieldの有無
2. Shield ProtectionとParry
3. ArmorとUnit最終Protection
4. Combat Speedと接敵Turn
5. Air Shield、Arrow Fend等の魔法支援

## 騎兵

1. RiderのLance / Bow / Sidearm
2. MountのHP・Protection・Defence
3. Mount攻撃
4. 騎乗時のみWeapon
5. Mount喪失後の戦力低下

---

# 自動生成データの限界

次は表だけで完全に決められません。

- 最終Gold / Resource Cost
- Recruitment PointとCommander Point効率
- Natural Protectionと装備Protectionの内部合成
- 二刀流・攻撃順の全処理
- Shape Change
- Start Item / Random Item
- BlessとBattlefield Buff
- Mounted combatのTarget選択
- Affliction、Fatigue、Morale
- 国家固有のRecruit条件
- Patchで変化した未抽出仕様

このため、装備表は「Unitの強さを自動採点する表」ではありません。

> **何を持っているかを確認する**
> → **戦闘ルールで意味を解釈する**
> → **国家攻略で生産・研究・Counterへ接続する**

という順番で使います。

---

## 出典

- Dominions 6ゲーム内Unit詳細
- Dominions 6 Manual / Modding Manual
- Dominions 6 Mod Inspector
- 固定データSnapshot: `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`（Dominions 6.35対応）
