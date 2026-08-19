---
title: Item固有効果・Weapon proc・副作用
status: expanding
verified_version: "6.35"
last_verified: "2026-08-19"
---

# Item固有効果・Weapon proc・副作用

Magic Itemは、Item本体の能力だけを見ても性能を判断できないことがあります。

特にWeapon / Armor Itemでは、

```text
Item record
↓
参照Weapon / Armor record
↓
Damage・Protection・property
↓
Secondary effect / Spell / Summon / 副作用
```

まで追って初めて「何に勝てる装備か」が分かります。

このページでは、その読み方を整理します。

正確な6.35データは、

- [Magic Itemデータ索引](../data/items/index.md)
- [Magic Item Weapon profile](../data/items/weapon-profiles.md)
- [Magic Item Armor profile](../data/items/armor-profiles.md)
- [Item Spell・自動効果](../data/items/active-effects.md)
- [Summon・Retinue Item](../data/items/summoning-effects.md)
- [Item副作用・装備制限](../data/items/risk-restrictions.md)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)

を使って確認します。

---

# なぜItem表だけでは足りないのか

例えばWeapon Itemには、Item record上の

- Construction
- Forge要求Path
- Gem cost
- Fire / Cold / Shock Resistance
- Strength
- Attack
- MR
- その他Item固有能力

だけでなく、別のWeapon recordに

- 基礎Damage
- Strength加算
- Attack / Defence modifier
- Length
- 攻撃回数
- Magic weaponか
- AP / AN
- Damage type
- Secondary effect
- AoE
- MR判定

が入っていることがあります。

したがって、

> **ItemのEffects欄が短い = 単純なItem**

とは限りません。

---

# Item recordとWeapon recordを分けて読む

## Item record

Itemそのものが与える能力です。

例：

- Resistance
- Stat bonus
- Magic Path
- Regeneration
- Reinvigoration
- Flying
- Research
- Start battle spell
- Summon
- Curse / Disease等

## Weapon record

装備したWeaponが攻撃するときの性能です。

例：

- Damage
- Damage type
- AP / AN
- Magic weapon
- Secondary effect
- 攻撃回数
- Range / AoE
- MR Negates

この二層を混ぜないことが重要です。

---

# Magic weaponとMagic damageは別

初心者が特に混同しやすい部分です。

## Magic weapon

WeaponそのものがMagic Weaponとして扱われます。

重要な用途の一つは、Ethereal等の**非Magic Weaponに対する防御**へ対応することです。

「Etherealに攻撃がほとんど当たらない」という症状なら、まずWeapon profileで`Magic weapon`か確認します。

## Magic damage

Damage type側がMagic damageであることを示します。

これは`Magic weapon`と同義ではありません。

したがってWikiのgenerated tableでも、

- **Properties: Magic weapon**
- **Damage type: Magic damage**

を別々に表示します。

---

# APとAN

## Armor Piercing

ArmorによるProtectionの効きを減らす方向のpropertyです。

高Protectionを見たとき、単純にWeapon Damageだけを増やすより、APを持つWeaponが有効な場合があります。

## Armor Negating

Armor Protectionをさらに強く無視する性質です。

ただし、

- HP
- Defence
- Luck
- Ethereal
- Regeneration
- MR

等は別問題です。

「ANだからThugを必ず倒せる」ではありません。

---

# Damage typeを必ず見る

Item Weaponを評価するときはDamage値だけでなく、何属性かを確認します。

代表的には、

- Slash
- Pierce
- Blunt
- Fire
- Cold
- Shock
- Poison
- Acid
- Magic damage
- True / Internal等の特殊Damage

があります。

## Counter

敵がItemで高いResistanceを積んでいる場合、そのDamage typeへ追加投資しても効率が下がります。

例えば、

```text
Fire Weapon
↓
敵が高FR
↓
別Damage type / Physical / MR攻撃へ切り替える
```

という判断をします。

---

# Secondary effect

Weaponには通常Damageとは別にSecondary effectを持つものがあります。

生成表では、

- `On damage`
- `Always`

を区別して表示します。

## On damage

主攻撃がDamageを与えたことに依存してSecondaryが発生するタイプです。

Protectionや回避で主攻撃が止まると、期待していた追加効果まで通らない可能性があります。

## Always

主攻撃Damageとは別条件で発生するSecondaryです。

実際の対象、AoE、Resistance判定、特殊条件はゲーム内表示で確認します。

---

# Fire BrandのようなItemをどう読むか

6.35データではFire BrandはItem recordからWeapon record `Fire Brand`を参照します。

Weapon側には通常攻撃だけでなくSecondaryとして`Small Area Fire`があります。

つまり、

> 「Item本体のAttack / Resistance bonusだけを見る」

では、Chaff処理能力を見落とします。

評価するときは、

```text
Item本体
+ Weapon本体
+ Secondary effect
```

をセットで見ます。

---

# Frost Brand等も同じ読み方をする

Elemental Brand系は名前だけで「Fire版 / Cold版」と判断せず、

- Main Damage
- Damage type
- Secondary
- Resistanceとの関係
- Construction
- Forge Path
- Slot競合

をそれぞれ確認します。

Patchや世代差で旧作Wikiの定番知識をそのまま流用しないことが重要です。

---

# ItemからSpellが出る場合

ItemにはWeapon attackとは別にSpell系fieldが設定されていることがあります。

generated索引では、少なくとも次を分けます。

## Spell effect

BaseIの`spelleffect`に明示された効果です。

例えば6.35データでは、Wand of Wild Fireに`Fireball`、Staff of Corrosionに`Acid Bolt`が明示されています。

ただし、field名だけから発動Timingや使用回数を推測しません。

## Start battle spell

戦闘開始時に関係するSpell fieldです。

Staff of Stormsは6.35のBaseIで`Storm`が明示されています。

これは単なるWeapon性能ではなく、**戦場全体の前提を変えるItem**として評価します。

## Auto combat spell

戦闘中の自動Spell fieldです。

Staff of Stormsには`Lightning Bolt`も別fieldとして明示されています。

`Start battle spell`と`Auto combat spell`を同一視しません。

## Item spell / Ritual

使用可能SpellやRitualを持つItemもあります。

Forge前に、

- 誰が使うか
- Gemを使うか
- Actionを消費するか
- 戦闘かStrategicか
- Itemを持つだけでよいか

をゲーム内表示で確認します。

---

# Start battle効果はArmy全体への影響で評価する

Start battle効果を持つItemは、一人のCommander強化だけではありません。

例えばStormなら、

- Flying
- Air magic
- 射撃
- Storm Power
- Battlefield mobility

など複数systemと相互作用します。

そのため、

```text
Item cost
<
その戦場全体を自軍有利へ変える価値
```

なら高価でも投資価値があります。

逆に、自軍のFlyingや射撃を自分で妨害する場合もあります。

---

# Summon・Retinue Item

Itemの価値がCarrier本人ではなく、追加Unitを出すことにある場合があります。

BaseIには、

- Ritual summon
- Automatic summon
- Battle summon
- Battle-start summon
- Retinue
- Summoner

等のfieldがあります。

これらは[Summon・Retinue Item](../data/items/summoning-effects.md)へ抽出します。

---

# Summon Itemを評価する質問

## 何を増やすか

追加Unitの役割を見ます。

- Chaff
- Bodyguard
- Damage
- Siege
- Patrol
- Sacred
- Magic Being
- Undead
- Mage

## いつ増えるか

- Forge直後
- 毎Turn
- Battle開始
- Combat中
- Ritual実行時

では価値がまったく違います。

## Leadershipは足りるか

Unitを生んでも率いられなければ戦力化できません。

- Normal Leadership
- Undead Leadership
- Magic Leadership

を確認します。

## SupplyとUpkeep

召喚Unitが無料に見えても、SupplyやArmy sizeへの影響があります。

---

# Itemの副作用

高性能Itemほど、持たせるだけで安全とは限りません。

generated索引では、

- Curse
- Disease
- Insanity
- Aging
- Eye loss
- Transformation
- Horror関連
- Single use
- その他明示されたRisk

を[Item副作用・装備制限](../data/items/risk-restrictions.md)へまとめます。

---

# Curse / Disease / Insanityを分ける

これらを「なんとなく危険」と一括りにしないことが重要です。

## Curse

Affliction Risk等と関係する長期的な問題です。

## Disease

HP減少や長期生存へ関係する別systemです。

Poison Resistanceを積んでもDisease対策にはなりません。

## Insanity

Commanderが毎Turn安定してOrderを実行できるかというStrategic reliabilityの問題です。

Researcher、Global caster、Artifact carrierでは特に大きな損失になります。

---

# 装備制限もCostである

Itemが強くても、Carrier条件が厳しい場合があります。

例えば、

- Minimum Size
- Maximum Size
- Minimum Strength
- Minimum hands
- Flying / Mounted限定
- Inanimate不可
- Mindless不可
- Mage限定

等です。

これはGem costとは別の**Carrier opportunity cost**です。

---

# Armor ItemはProtectionだけ見ない

Armor / Shield / HelmetもItem recordだけでは不十分です。

参照Armor recordから、

- Shield Protection
- Parry
- Defence penalty
- Body Protection
- Head Protection
- Encumbrance
- Map move penalty
- Armor attributes

を見ます。

---

# MageへArmorを着せる場合

高Protectionだけを見てMageへ重装を渡すと、

- Encumbrance
- Spellcasting fatigue
- Movement
- Slot競合

で損をする場合があります。

Caster用防具は、

```text
生存性上昇
-
追加Fatigue / Mobility低下
```

で評価します。

---

# ShieldはParryとDef penaltyを分ける

Shieldは「Defenceが上がる装備」だけではありません。

- Shield Protection
- Parry
- 通常Defenceへのpenalty
- Encumbrance

を別に確認します。

多数の通常攻撃や射撃へ有効でも、

- AN
- Poison
- AoE
- MR攻撃

には別Counterが必要です。

---

# Item固有効果を使ったCounter思考

敵Itemを見たら、Statsだけでなく効果の発生源を分解します。

## Weapon secondaryが主力

主Weaponを無力化するだけでなく、

- Resistance
- 分散
- Range
- 高Defence
- Disarm / kill carrier

を考えます。

## Start battle spellが主力

Carrier本人を倒した後では遅い場合があります。

- 戦闘前にAssassinate
- 別戦場へ誘導
- 自軍構成を変える
- 同じbattlefield conditionを利用する

等を考えます。

## Summon Itemが主力

Carrier一体ではなく、毎Turn生むUnit総量を見ます。

- Forge hubをRaid
- Carrierを早期に倒す
- Leadershipを狙う
- Chaff counterを用意する

方が効く場合があります。

## 副作用がある高級Item

敵が既にInsanity / Disease / Curse等を負っているなら、長期戦へ持ち込むこと自体がCounterになります。

---

# Itemを評価する実戦手順

```text
1. Item名を確認
2. Construction / Req / Gemを確認
3. Item本体Effectsを見る
4. Weapon / Armor参照があるか確認
5. Damage / Prot / AP / AN / Magic weaponを見る
6. Secondary effectを見る
7. Spell / Start battle / Auto combat fieldを見る
8. Summon / Retinueを見る
9. Curse / Disease / Insanity / 装備制限を見る
10. CarrierのSlot・Stats・任務へ戻る
11. Enemy Counterを考える
12. Forge画面で最終Costを確認
```

この順番なら、Item名の知名度に引っ張られにくくなります。

---

# よくある失敗

## Item本体のEffectsだけを見る

Weapon secondaryやArmor profileを見落とします。

## Damageだけ見る

Magic weapon、AP / AN、Damage type、MR判定を無視します。

## Magic weaponとMagic damageを混同する

Ethereal counterを誤ります。

## Secondaryの条件を見ない

`On damage`と`Always`では期待値が変わります。

## Start battleとAuto combatを同じ扱いにする

戦場条件と戦闘中の追加Castを混同します。

## Summon数だけ見る

Leadership、Supply、Timingを無視します。

## 高性能Itemの副作用を無視する

Rare MageやArtifact carrierが長期的に機能停止します。

## ArmorのProtectionだけ見る

EncumbranceとDefence penaltyで期待した性能が出ません。

---

# テストゲームで確認する

Itemの特殊効果は、文章だけでなくTest Gameでも確認します。

特に、

- Secondaryの発動条件
- AoE
- Resistance判定
- MR判定
- Battle-start timing
- Summon timing
- Carrier死亡時
- Retreat後

はReplayで見る価値があります。

---

## 関連ページ

- [Magic Item総論](index.md)
- [用途別Magic Item辞典](purpose-dictionary.md)
- [Forge計画とConstruction Breakpoint](forge-planning.md)
- [Resistance・Utility Item](resistance-items.md)
- [Thug / SC装備](thug-equipment.md)
- [武器と盾](../basics/weapons-and-shields.md)
- [Combat data](../data/combat/index.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
