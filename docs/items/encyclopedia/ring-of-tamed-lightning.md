---
title: "Ring of Tamed Lightning"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-25"
item_id: 310
---

# Ring of Tamed Lightning

**Shock Resistance +15をMisc Slotから一人へ与え、Lightning系Damageへ早期対応するConstruction 1の専門Resistance Item。**

Ring of Tamed LightningはAir ShieldでもStorm immunityでもありません。攻略上は、**Shock damageを受ける重要Commanderへ、C1・A1という短い入口から専用防御を追加するItem**として評価します。

- [Dominions 6.35固定データ — Item 310](../../data/items/by-id/310.md)
- [Magic Item攻略辞典](index.md)
- [Resistance Item](../resistance-items.md)
- [Elemental Armor](elemental-armor.md)
- [Ring of Fire](ring-of-fire.md)

---

# まず何ができるか

6.35固定データでは、Ring of Tamed Lightningは、

- Construction 1
- Forge要求 **A1**
- Miscellaneous Slot
- **Shock Resistance +15**

を持ちます。

Item descriptionは、AquamarineのRingが装備者へLightningに対するほぼ完全な免疫を与えると説明しています。

攻略上は説明文の印象ではなく、固定fieldのShock Resistance +15と、装備後のUnit表示を基準にします。

```text
素のShock Resistance
＋ Ringの+15
→ 実際のShock damageと生存Roundを比較
```

「Lightning」という語から、Storm、Wind、Air Shield、Flyingまで守るItemへ拡張しません。

---

# Air Shieldではない

Air Shieldは主に射撃命中へ関わる防御です。

Ring of Tamed Lightningの主要効果はShock Resistanceです。

したがって、

```text
Arrow / Crossbow /通常Projectile
→ Air Shield・Shield・Mist等を検討

Lightning Bolt / Thunder Strike / Shock Weapon
→ Shock Resistanceを検討
```

とDamage typeを分けます。

敵がAir Mageだからといって、攻撃がすべてShockとは限りません。Spell名、Damage type、Battle Replayを確認します。

---

# Storm immunityでもない

Ringを装備しても、固定データ上、Storm immunityを得るItemではありません。

したがって、

- Storm下のFlying制限
- Storm関連のPrecisionやBattlefield条件
- Storm Power
- Windや射撃への別効果

を一括で解決するものとして扱いません。

Ringが担当するのはShock Resistanceです。

```text
Stormそのものへの対応
≠
Storm中に飛んでくるShock damageへの対応
```

を分けます。

---

# Protectionだけでは足りない戦場へ入れる

敵のShock攻撃recordがArmor NegatingまたはArmor Piercingなら、通常のProtectionだけでは十分な回答になりません。

高Protection Carrierほど、

- 通常兵には強い
- Lightningで急にHPを失う
- Armorを増やしても敗因が残る

ことがあります。

その場合、Ring of Tamed Lightningは防御層を追加します。

```text
Protection
→ 通常物理へ対応

Shock Resistance
→ Shock componentへ対応
```

と役割を分けます。

ただし、Ringを付けてもHP、MR、Fatigue、Positioningが不足していれば倒れます。

---

# Construction 1の緊急回答

C1・A1という入口は、Air戦への対応を早く用意できることが強みです。

候補になる状況は、

- Lightning Boltが戦場へ出始めた
- Thunder Strikeを使うMageが確認された
- Shock weapon持ちのEliteへThugを当てたい
- Wrathful Skies等のShock環境へ重要Casterを置く
- Air ElementalやStorm戦の周辺でShock damageを受ける

場合です。

高位のArmy-wide Shock Resistanceが間に合わない時、最重要Commanderだけ先に守れます。

C1で作れることはResearch上の強みですが、敵がShockを使わないならForge turnを払う理由にはなりません。

---

# 相性の良いCarrier

特に候補になるのは、

- Shock Evocationの射程内でScriptを完遂するMage
- 高Protectionだが素Shock Resistanceが低いThug
- Storm戦で前へ出るCommander
- 高価なCommunion / Sabbath Master
- Shock weaponを持つ敵Eliteへ接触するCarrier
- Army-wide対策から外れる単独Raider
- Battle spellをCastするまで生き残る必要があるPretender / Prophet

です。

CarrierはAttackやProtectionだけでなく、

- 素Shock Resistance
- HP
- MR
- Positioning
- Retreat route
- Misc Slotの余裕

から選びます。

---

# 一体を守るItemである

Ring of Tamed Lightningは装備者だけを守ります。

Thunder Strike等がArmy全体へ繰り返し当たる戦場で、Commander一体だけRingを持ってもArmy崩壊は止まりません。

```text
勝敗の中心が一体のCaster生存
→ Ring一個の価値が高い

勝敗の中心がArmy全体のShock被害
→ Ward系Spell・分散・Caster狩りを比較
```

と対象範囲で判断します。

RingはArmy-wide solutionの代替ではなく、重要個体へ確実に置く局所防御です。

---

# Misc SlotのOpportunity Cost

同じMisc Slotには、

- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Amulet of Resilience](amulet-of-resilience.md)
- [Girdle of Might](girdle-of-might.md)
- Path Booster
- Mobility Item
- 別Resistance Ring

が入ります。

Shock Resistanceを得た代わりに、

- MRが不足する
- Regenerationを失う
- Reinvigorationが不足する
- 必要SpellへPathが届かない

なら、Build全体では弱くなることがあります。

Ringは「空いているMiscへとりあえず」ではなく、次の敗因へ直接払うSlotです。

---

# Elemental Armorとの比較

[Elemental Armor](elemental-armor.md)はArmor SlotでFire・Cold・Shock Resistanceをまとめます。

| Item | 解禁 | Forge要求 | Slot | 役割 |
|---|---:|---:|---|---|
| Ring of Tamed Lightning | C1 | A1 | Misc | Shock +15へ集中 |
| Elemental Armor | C5 | E2F1 | Armor | Fire・Cold・Shockを広く補う |

Ringが向くのは、

- Shockだけが主脅威
- C1で急ぐ
- 現在のArmorを維持したい
- 重装のDefense / Encumbrance負担を避けたい

場合です。

Elemental Armorが向くのは、

- 複数属性が同時に来る
- Misc Slotを別機能へ残したい
- E2F1 accessがある
- Carrierが重いArmorを処理できる

場合です。

---

# Ring of Fire・Ring of Frostとの違い

C1専門Ring群は、同じResearch帯と同じSlotを使います。

- [Ring of Fire](ring-of-fire.md)：Fire Resistance +15
- Ring of Tamed Lightning：Shock Resistance +15
- [Ring of Frost](ring-of-frost.md)：Cold Resistance +15
- [Snake Ring](snake-ring.md)：Poison Resistance +30とPoison Touch

したがって、Forge順は固定Tierではなく、Enemy Damage typeで決まります。

```text
Air Nationと戦う
→ 必ずShock Ring
```

ではありません。

相手がAir accessをMobility、Mist、Storm、Summonへ使い、Shock damageをあまり出さないならRingの価値は下がります。

---

# Shock戦はPositioningも同時に直す

Resistanceだけでなく、

- Mageを後方へ置く
- Squadを分散する
- 高価なCommanderを密集させない
- Flying / Attack Rearで敵Casterへ圧力をかける
- Stormと射程の条件を読む
- DecoyやChaffでTargetingをずらす

ことも重要です。

Ringを装備しても、同じTileへ重要Commanderを密集させればAoE圧力は残ります。

```text
Resistance
＋ Positioning
＋ Caster pressure
```

の三層でShock戦へ対応します。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 1へ到達済み
- A1 Forgerを確保できる
- 敵が実際にShock damageを使用している
- 一体の重要Commander生存が戦術の前提
- ProtectionだけではLightningを処理できていない
- Army-wide対策のResearchが間に合わない
- Armor Slotを現在の装備へ残したい
- Misc SlotをShock対策へ割ける
- Ringを複数戦線で持ち回せる

C1の安さではなく、**Shockによる失敗を具体的に一つ消せるか**で決めます。

---

# Forgeしない・後回しにする条件

- 敵がShock damageをほとんど使わない
- 素Shock Resistanceで必要値へ届いている
- Army-wide SpellやBlessで十分
- 敗因がPhysical、MR、Poison、Fatigueにある
- Misc Slotへ必須BoosterやMR Itemがある
- Army全体が崩れており、一体だけ守っても勝てない
- Enemy Air Mageを直接狩る方が安い
- Air GemとForge turnを他の緊急用途へ回す必要がある

敵にAir Mageが見えたことと、Shock Ringが必要であることは同義ではありません。

---

# Counter：Shock以外の軸へ移る

敵CarrierがRing of Tamed Lightningを持つなら、Shockだけを重ねると専門防御へぶつかります。

Counterは、

- Fire / Cold / Poison / AcidへDamage typeを変える
- 高Damage物理を使う
- MR-negates Controlや即死系を使う
- Fatigueを蓄積させる
- Chaffで囲み長期戦へする
- Ring装備で失われたMR / Regeneration / Boosterを突く
- Carrierを避けてArmyやProvinceを狙う
- Casterを別Targetへ切り替える
- Item transportやLabをRaidする

です。

また、Ringを装備した一体だけを避け、未装備のMageやArmyへShockを当て続ける選択もあります。

---

# よくある失敗

## Air Shieldと混同する

Ringの主要効果はShock Resistanceです。Arrow対策は別です。

## Storm immunityと思う

Storm下の移動・Flying・Battlefield条件を解決するItemではありません。

## Protectionも上がると思う

通常物理防御は別に用意します。

## Air Nationなら必ず作る

相手がShock damageを使っているかを確認します。

## 一体だけ守ってArmy-wide AoEへ勝てると思う

勝敗の中心がArmy全体なら、分散、Ward、Caster狩りも必要です。

## Misc Slot競合を見ない

Shockを耐えても、MRやFatigueの不足でScriptを完遂できないことがあります。

---

# Test game checklist

```text
[ ] C1・A1でRing of Tamed LightningがForge可能か確認
[ ] Item 310であることを確認
[ ] Shock Resistance +15が装備画面へ反映されることを確認
[ ] 装備前後のShock Resistance合計を記録
[ ] Lightning Boltに対するDamageと生存Roundを比較
[ ] Thunder Strikeに対するDamageとFatigue推移を比較
[ ] Shock weaponへ接触した時の結果を比較
[ ] Storm下でもStorm immunityを得ないことを確認
[ ] Arrow / CrossbowにAir Shield効果を持たないことを確認
[ ] Elemental ArmorとのSlot・Research timingを比較
[ ] Army-wide Shock Resistanceとの重なりを確認
[ ] MR / Physical / Poison Counterには別対策が必要か確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 310](../../data/items/by-id/310.md)
- [Resistance Item](../resistance-items.md)
- [Elemental Armor](elemental-armor.md)
- [Ring of Fire](ring-of-fire.md)
- [Ring of Frost](ring-of-frost.md)
- [Snake Ring](snake-ring.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Amulet of Resilience](amulet-of-resilience.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- BaseI: C1 / A1 / Miscellaneous / Shock Resistance +15
- Item description: AquamarineのRingが装備者をLightningから守る
- Air Shield、Storm immunity、実際のDamage軽減、SpellごとのArmor propertyはゲーム内表示・Spell record・Battle Replayを優先