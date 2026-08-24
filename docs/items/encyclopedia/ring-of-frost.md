---
title: "Ring of Frost"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-25"
item_id: 311
---

# Ring of Frost

**Cold Resistance +15をMisc Slotから一人へ与え、Cold damageと寒冷Battlefieldへ早期対応するConstruction 1の専門Resistance Item。**

Ring of FrostはWinter movement、Water Breathing、Cold Auraを与えるItemではありません。攻略上は、**Coldを主力とする敵に対し、重要Commander一体のCold ResistanceをC1・W1で確保する防御Item**として評価します。

- [Dominions 6.35固定データ — Item 311](../../data/items/by-id/311.md)
- [Magic Item攻略辞典](index.md)
- [Resistance Item](../resistance-items.md)
- [Elemental Armor](elemental-armor.md)
- [Robe of the Sea](robe-of-the-sea.md)

---

# まず何ができるか

6.35固定データでは、Ring of Frostは、

- Construction 1
- Forge要求 **W1**
- Miscellaneous Slot
- **Cold Resistance +15**

を持ちます。

Item descriptionは、SapphireのRingが装備者をあらゆる形のColdからほぼ完全に守ると説明しています。

攻略上は、固定fieldのCold Resistance +15を正本にします。

```text
素のCold Resistance
＋ Ring of Frostの+15
→ 装備後の表示値とBattle結果を確認
```

説明文を、Coldに関連する移動・Aura・Path・水中適性まで得る効果として読みません。

---

# Cold damageへ集中する専門Item

Ring of Frostは、

- Cold Evocation
- Frost weapon
- Cold Aura
- Ice / Water系のCold attack
- 寒冷Battlefield effect
- Grip of Winter等の長期圧力

へ対応する候補です。

ただし、個々のSpellやWeaponが、

- どのDamage typeを持つか
- Armor Piercing / Armor Negatingか
- Fatigueや追加効果を伴うか
- 何回Hitするか

は別に確認します。

```text
Cold componentを減らす
≠
Spell全体のすべての効果を消す
```

という区別が重要です。

---

# Construction 1で寒冷戦へ間に合わせる

Ring of FrostはC1で解禁されます。

そのため、

- 高位Cold Resistance Spellがない
- C5のElemental Armorまで遠い
- 敵のCold Raiderが早く来た
- 重要Mage一体だけ寒冷地へ出したい

時に、短いResearchとW1 accessから対処できます。

```text
目前のCold敗因
→ C1でRingを用意
→ Scriptの中心だけ先に保護
```

という使い方です。

早期ItemであることはTiming上の価値であり、敵がColdを使わない戦場での普遍的な強さではありません。

---

# Winter movementは付かない

Ring of Frostの固定主要効果はCold Resistanceです。

装備しても、

- Snow / WinterでのStrategic movement改善
- Winter move ability
- MountainやRiverの移動規則変更
- Supply改善
- Cold Scale適応

を自動的に得るItemではありません。

```text
Cold damageを受けにくくする
≠
Winterで速く移動できる
```

を分けます。

寒冷地へ出るCommanderには、ResistanceだけでなくMap Move、Supply、Army速度、帰還routeも確認します。

---

# Water Breathingは付かない

同じWater pathでForgeするため、[Robe of the Sea](robe-of-the-sea.md)やWater Breathing Itemと混同しやすいですが、役割は別です。

```text
Ring of Frost
→ Cold Resistance +15
→ Misc Slot
→ C1 / W1

Robe of the Sea
→ Water +1
→ 装備者本人の海陸呼吸
→ Armor Slot
→ C5 / W3
```

Ring of Frostだけでは、陸上Commanderを水中へ移動させる手段になりません。

水中へ行くための適性と、水中で受けるCold damageへの耐性は別の問題です。

---

# 相性の良いCarrier

候補になるのは、

- Cold Evocationの射程内でScriptを完遂するMage
- Cold Aura持ちへ接触するThug
- Frost weaponを持つ敵Eliteへ当てるCommander
- Grip of Winter等の長期戦へ残る重要Caster
- 素Cold Resistanceが低い高価なSummoned Commander
- Army-wide Cold Resistanceから外れる単独Raider
- 寒冷BattlefieldでFatigue推移を管理したいHeavy / Quickness Carrier

です。

最後の用途では、Ring装備前後のFatigueをBattle Replayで比較し、Cold Resistanceが実際に有効Roundを増やしているかを確認します。

---

# 一体を守る局所防御

Ringが守るのは装備者です。

Cold AuraやBattlefield-wide effectがArmy全体へ作用する戦闘では、一人だけRingを持っても全軍の問題は解決しません。

```text
一体のCasterが生きれば戦術が成立
→ Ringの局所防御が有効

Army全体がCold / Fatigueで崩れる
→ Army-wide Spell・Unit選択・Caster狩りが必要
```

と範囲を分けます。

Ringは重要個体の保険として強く、Army全体へ配るほど常に効率的とは限りません。

---

# Misc Slotの競合

Ring of FrostはMisc Slotを一つ使います。

競合するのは、

- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Amulet of Resilience](amulet-of-resilience.md)
- [Girdle of Might](girdle-of-might.md)
- Path Booster
- Mobility Item
- 別Resistance Ring

です。

Cold Resistanceを得ても、

- MR-based Controlを受ける
- Reinvigoration不足で止まる
- Regenerationを失い通常Damageで削られる
- Path Boosterを外してScriptが成立しない

なら、目的を達成できません。

Ringを入れた後のBuild全体で勝敗を評価します。

---

# Elemental Armorとの比較

[Elemental Armor](elemental-armor.md)はArmor SlotからFire・Cold・Shock Resistanceをまとめます。

| Item | 解禁 | Forge要求 | Slot | 役割 |
|---|---:|---:|---|---|
| Ring of Frost | C1 | W1 | Misc | Cold +15へ集中 |
| Elemental Armor | C5 | E2F1 | Armor | 三属性を広く補う |

Ringが向くのは、

- Coldだけが現実の脅威
- C1で急ぐ
- 現在のArmorを維持したい
- Armorの重さを増やしたくない

場合です。

Elemental Armorが向くのは、

- Fire・Cold・Shockが混在する
- Misc SlotをMR・Regeneration・Boosterへ残したい
- 重装のDefense / Encumbrance負担を処理できる

場合です。

---

# Ring of Fire・Ring of Tamed Lightningとの持ち替え

C1専門Ring群は、敵の主Damage typeへ合わせて使います。

- [Ring of Fire](ring-of-fire.md)：Fire Resistance +15
- [Ring of Tamed Lightning](ring-of-tamed-lightning.md)：Shock Resistance +15
- Ring of Frost：Cold Resistance +15
- [Snake Ring](snake-ring.md)：Poison Resistance +30とPoison Touch

敵がWater Mageを持つからRing of Frost、とは限りません。

Water accessが、

- Quickness
- Water Elemental summon
- Friendly Currents
- Water mobility
- Buff

へ使われ、Cold damageが主力でないなら優先度は下がります。

敵のPathではなく、実際のSpell・Weapon・Auraを見ます。

---

# Cold Auraへ接触するBuild

Cold Aura持ちへ近接するCarrierでは、

- 接触Round数
- CarrierのCold Resistance
- Encumbrance
- Reinvigoration
- Quickness等による行動量
- 敵を倒すまでのRound

を一緒に確認します。

RingはCold componentへ作用しますが、Carrierが通常攻撃、Fear、MR effect、Surroundで止まる問題は残ります。

```text
Cold Auraを耐える
＋
接敵後に短時間で仕事を終える
```

両方が必要です。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 1へ到達済み
- W1 Forgerを確保できる
- 敵の主要DamageがColdだと確認できる
- 一体の重要Commanderを守れば戦術が成立する
- Cold Auraや寒冷Battlefieldへ接触する任務がある
- 高位のArmy-wide対策が間に合わない
- Armor Slotを別装備へ残したい
- Misc SlotをCold対策へ割ける
- Ringを戦線間で持ち回せる

**Water accessがあるからではなく、Coldによる敗因があるから**Forgeします。

---

# Forgeしない・後回しにする条件

- 敵がCold damageをほとんど使わない
- Carrierの素Cold Resistanceで十分
- BlessやArmy-wide Spellで必要値へ届く
- 敗因がPhysical、MR、Shock、Poisonにある
- Misc Slotへ必須BoosterやMR Itemがある
- Army全体が寒冷効果で崩れ、一体だけ守っても勝てない
- Enemy Cold Casterを先に倒す方が安い
- Water GemとForge turnを別のTimingへ使う必要がある

Ringは万能防御ではなく、Cold専門の局所回答です。

---

# Counter：Cold以外へ攻撃軸を変える

敵CarrierがRing of Frostを持つなら、Coldだけを重ねると専門防御へ当たります。

Counterは、

- Fire / Shock / Poison / AcidへDamage typeを変える
- 高Damage物理で攻める
- MR-negates Controlや即死系を使う
- Cold以外のFatigue sourceを重ねる
- Chaffで囲み通常行動を浪費させる
- Ring装備で失われたMR / Regeneration / Boosterを突く
- Carrierを避けてArmy・Mage・Provinceを狙う
- Item transportやLabをRaidする

です。

また、Ring装備者だけを避け、未装備のArmyやCommanderへColdを集中する方法もあります。

---

# よくある失敗

## Water Breathingが付くと思う

Ringの主要効果はCold Resistanceです。海陸移動は別Item・能力が必要です。

## Winter movementが付くと思う

寒冷Damage対策とStrategic movementは別です。

## Cold Auraを得ると思う

Ringは装備者へCold Resistanceを与える防御Itemです。

## Water Nationなら常に必要と思う

敵の実際のDamage typeを確認します。

## Army全体が守られると思う

装備者一体だけです。Battlefield-wide問題には別対策が必要です。

## Misc Slot競合を見ない

Coldを耐えてもMRやReinvigoration不足で任務を失うことがあります。

---

# Test game checklist

```text
[ ] C1・W1でRing of FrostがForge可能か確認
[ ] Item 311であることを確認
[ ] Cold Resistance +15が装備画面へ反映されることを確認
[ ] 装備前後のCold Resistance合計を記録
[ ] Cold Evocationに対するDamageと生存Roundを比較
[ ] Cold Auraへ接触した時のHP / Fatigue推移を比較
[ ] Grip of Winter等の寒冷Battlefieldで有効Roundを比較
[ ] Winter movementが付かないことを確認
[ ] Water Breathingが付かないことを確認
[ ] Elemental ArmorとのSlot・Research timingを比較
[ ] Army-wide Cold Resistanceとの重なりを確認
[ ] Physical / MR / Poison Counterには別対策が必要か確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 311](../../data/items/by-id/311.md)
- [Resistance Item](../resistance-items.md)
- [Elemental Armor](elemental-armor.md)
- [Robe of the Sea](robe-of-the-sea.md)
- [Ring of Fire](ring-of-fire.md)
- [Ring of Tamed Lightning](ring-of-tamed-lightning.md)
- [Snake Ring](snake-ring.md)
- [Amulet of Resilience](amulet-of-resilience.md)
- [Ring of Regeneration](ring-of-regeneration.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- BaseI: C1 / W1 / Miscellaneous / Cold Resistance +15
- Item description: SapphireのRingが装備者をColdから守る
- Winter movement、Water Breathing、Cold Auraは固定効果として付与されない
- 実際のDamage軽減、Cold Aura / Battlefield effectとの相互作用、Fatigue推移はゲーム内表示とBattle Replayを優先