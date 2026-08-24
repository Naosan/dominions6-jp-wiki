---
title: "Shroud of the Battle Saint"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 252
---

# Shroud of the Battle Saint

**非SacredのCommanderにも自国のBlessを常時適用し、Bless設計を個人装備Buildへ転用するConstruction 5のArmor Item。**

Shroud of the Battle Saintは重装甲を得るための鎧ではありません。攻略上は、**Pretender設計で選んだBless一式を、一人のCarrierへArmor Slot経由で追加するItem**として評価します。

ただし一度着ると外せません。採用は「とりあえず装備」ではなく、Carrierと最終Buildを確定してから行う必要があります。

- [Dominions 6.35固定データ — Item 252](../../data/items/by-id/252.md)
- [Magic Item攻略辞典](index.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Thug・SC装備](../thug-equipment.md)

---

# まず何ができるか

6.35固定データでは、Shroud of the Battle SaintはConstruction 5、Forge要求**S1**のArmor Itemです。

Item descriptionでは、

- 装備者は常にBlessedになる
- Sacredでない装備者にも作用する
- 一度装備すると外せない

ことが明記されています。

重要なのは、

```text
Blessedになる
≠
Sacred Unitそのものになる
```

という点です。

Shroudは戦闘中のBless効果を与えるItemであり、Recruit条件、Sacred upkeep、Holy leadershipとの関係など、Unitの基礎分類すべてをSacredへ変えるItemとして扱うべきではありません。

---

# Blessの価値をCarrier一人へ移す

Shroudの性能はItem単体では決まりません。

同じShroudでも、自国のBlessが、

- 近接Damageを増やす
- Defence / Protection / Resistanceを補う
- RegenerationやSustainを与える
- Mobilityや特殊能力を与える
- Mageの生存や詠唱後の近接戦を支える

といった何を含むかで役割が変わります。

したがって評価式は、

```text
Shroudの価値
=
現在のBless package
×
Carrierがその効果を利用できる割合
×
Carrierが生存して働くRound
```

です。

「有名なItemだからForge」ではなく、**自国BlessとCarrierの噛み合わせ**を先に確認します。

---

# Blessの各要素を分解して見る

ShroudをForgeする前に、Blessを一つの塊として見ず、各効果がCarrierへ何を足すかを分解します。

## 攻撃系Bless

Carrierが実際に近接攻撃するか、命中できるか、攻撃回数が十分かを確認します。

後方Casterへ攻撃Blessを与えても、接敵しないなら価値は出ません。

## 防御系Bless

Carrierが負ける原因と一致しているかを確認します。

Fire Resistanceが必要な戦場でShock対策だけ増えても、敗因は変わりません。

## Sustain系Bless

RegenerationやReinvigoration等がある場合、最大HP、Encumbrance、戦闘時間と組み合わせます。

一撃で倒されるCarrierには継続回復の機会がありません。

## 特殊能力系Bless

特殊な反撃、Aura、Status、移動能力等は、発生条件と対象をTest gameで確認します。

表示上Blessedでも、すべての効果がすべてのCarrier・形態・攻撃へ同じように働くとは限りません。

---

# 非Sacred Carrierを選ぶ意味

Sacred Unitは通常の方法でBlessを受けられます。

Shroudの独自価値は、**本来Bless対象ではないCommanderへBlessを持ち込むこと**です。

候補になりやすいのは、

- 高HP・高Statsだが非SacredのThug候補
- 特殊なNatural attackを持つCommander
- Self-buff後に近接戦へ入るCombat Caster
- AssassinやRaiderなど、小規模戦で常時Blessが欲しいCarrier
- Battle開始直後からBlessを確実に有効化したいCommander

です。

ただし、Carrierが元からSacredで、通常のBless手段を安定して使えるなら、Armor SlotをShroudへ使う必要性は下がります。

---

# 常時BlessのTiming価値

Shroudの装備者は、PriestによるBless詠唱やSquad配置を待たずにBlessed状態で戦闘へ入れます。

これは、

- Assassination
- Raid
- 少人数迎撃
- Priestを同行させにくい遠征
- Battle開始直後から接敵する高速Carrier

で特に意味があります。

通常軍ではBlessを担当するPriestを用意できても、独立行動するCommanderではその前提が崩れます。

ShroudはBless効果だけでなく、**Blessを供給する物流とScriptを省くItem**でもあります。

---

# Armor Slotを使うという大きなCost

ShroudはArmor Slotを占有します。

これは、

- 高Protection Armor
- Elemental Resistance Armor
- Ethereal / Glamour / Displacement等の防御Armor
- Encumbranceを抑えた専用Armor
- 特殊なBattle-start効果を持つArmor

を同時に装備できないことを意味します。

Blessで得る防御が、外したArmorのProtectionやResistanceを上回るとは限りません。

比較は、

```text
Shroud + Bless
vs
代替Armor + 通常のBless供給なし
```

で行います。

Shroud単体のArmor値ではなく、**最終Unit Statsと実際の敗因**で決めます。

---

# 一度着ると外せない

Item description上、Shroudは一度装備すると外せません。

この制約は非常に重く、

- 敵に合わせてArmorを交換できない
- Booster運用へ戻しにくい
- Carrierの役割変更が難しい
- Itemを別Commanderへ貸し回せない
- Bless設計が期待ほど機能しなくても修正しにくい

という長期Costを作ります。

装備前に、

```text
Carrier
＋ Weapon / Shield
＋ Helmet / Boots / Misc
＋ Shroudで得るBless
```

を最終形まで組み、Test gameで確認します。

Dwarven Hammerのように回す生産設備とは逆で、Shroudは**Carrierへ固定するCommitment Item**です。

---

# Blessの状態はゲーム状況にも依存する

Bless効果の一部は、Pretenderの状態やBless固有条件によって利用可能性が変わる場合があります。

Shroudを装備しただけで、通常なら無効なBless要素まで無条件に有効になると決めつけない方が安全です。

特に、

- Incarnate要素
- 特定攻撃にだけ作用する効果
- Sacred-only表記を伴う特殊処理
- Shapechange前後の適用

は、対象Carrierと現在のゲーム状態でTestします。

固定データは「Blessを与える」ことを示しますが、Bless内部の全条件までShroudが上書きするとは限りません。

---

# 相性の良いBuild

Shroudが強くなりやすいのは、Blessが複数の不足を同時に埋めるBuildです。

例えば、

```text
非Sacred高HP Carrier
＋ ShroudでRegeneration / Resistance
＋ WeaponでDamage
＋ MiscでMR / Reinvigoration
```

のように、Armor Slot一つで複数効果を得られるならSlot効率が上がります。

逆にBlessの大半がSacred Army向けで、個人Carrierが利用できる要素が少ない場合、Shroudの価値は低下します。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- S1 Forge Mageを確保できる
- 非Sacredで強いCarrierがいる
- 自国Blessの複数要素がCarrierへ有効
- Priestなしで常時Blessedにする意味がある
- Shroudを着ても必要Protection / Resistanceが残る
- Carrierの役割と最終装備が確定している
- 一度装備すると外せない制約を許容できる
- Test gameで代替Armorより任務成功率が高い

S1でForgeできても、**装備後のCommitmentが軽いわけではありません**。

---

# Forgeしない・別Itemを選ぶ条件

- BlessがCarrierの役割と噛み合わない
- Carrierが元からSacredで通常Blessが容易
- Heavy Armorや特殊Armorが必須
- 敵ごとにArmorを交換したい
- CarrierをForge / Research等へ戻す可能性が高い
- Blessの重要要素が現在利用できない
- Astral GemをBoosterやBattle magicへ回す必要がある
- Test前に本番Carrierへ固定するしかない

Shroudは汎用Armorではなく、**Bless設計とCarrierを固定するBuild Item**です。

---

# Counter：Blessの外側を攻める

敵がShroud Carrierを出したら、まず相手Blessの内容を確認します。

Counterは、Blessで補われていない軸を探します。

- Elemental Resistanceの穴を突く
- MRが低いならMR-based effectを使う
- 高ProtectionならArmor Negatingを使う
- RegenerationならBurst damageやFatigueを使う
- 高Defenseなら必中・AoE・別判定を使う
- 接近戦が強いならMissile / Battle magicで距離から処理する

さらにShroudは外せないため、一度弱点を特定すると、Carrier側はArmor交換で適応しにくくなります。

**相手の強化内容より、固定されたBuildの空白を読む**ことがCounterになります。

---

# よくある失敗

## Shroudを着るとSacredになると思う

Item descriptionは非SacredでもBlessedになると述べています。Unit分類そのものの変更とは分けて考えます。

## Bless内容を確認せずForgeする

Shroudの価値は自国Blessに依存します。

## Protectionを失う

Armor Slotを使うため、代替Armorを外した最終Protectionを確認します。

## Test前に本番Carrierへ装備する

一度着ると外せません。試験用Commanderと本番Carrierを分けます。

## 敵ごとの装備交換を前提にする

Shroud CarrierはArmorを柔軟に変更できません。

## すべてのBless要素が無条件に働くと思う

Bless固有条件、Pretender状態、攻撃種別、Shape等を確認します。

---

# Test game checklist

```text
[ ] C5・S1でShroud of the Battle SaintがForge可能か確認
[ ] Item 252 / Armor record 54であることを確認
[ ] 非Sacred Commanderが戦闘開始時からBlessedになることを確認
[ ] Unit自体のSacred分類が変わるかを表示で確認
[ ] 自国Blessの各要素がCarrierへ反映されるか確認
[ ] Incarnate / 条件付きBlessの挙動を確認
[ ] Shapechange前後でBless表示と効果を確認
[ ] Shroud装備後のProtection・Encumbranceを確認
[ ] 一度装備すると通常手段で外せないことを確認
[ ] 代替Armor Buildと生存Round・勝率を比較
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 252](../../data/items/by-id/252.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Girdle of Might](girdle-of-might.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Frost Brand](frost-brand.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Thug・SC装備](../thug-equipment.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / armors / protections_by_armor / Item description
- Blessの個別効果、Pretender状態への依存、Shapeとの相互作用はゲーム内Unit画面とBattle Replayを優先
- 一度装備すると外せない制約はItem descriptionに基づく
