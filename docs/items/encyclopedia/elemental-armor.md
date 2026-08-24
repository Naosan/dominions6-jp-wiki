---
title: "Elemental Armor"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 249
---

# Elemental Armor

**Fire・Cold・Shock Resistanceを一つのArmor Slotへまとめ、複数属性のBattle magicへ備えるConstruction 5の重装鎧。**

Elemental Armorは「Protectionが高い鎧」だけではありません。攻略上は、**Armor Slot一つで三属性の耐性穴を同時に塞ぐ代わりに、重い鎧によるDefense・Fatigue負担を受け入れるItem**として評価します。

- [Dominions 6.35固定データ — Item 249](../../data/items/by-id/249.md)
- [Magic Item攻略辞典](index.md)
- [Resistance Item](../resistance-items.md)
- [Thug・SC装備](../thug-equipment.md)

---

# まず何ができるか

6.35固定データでは、Elemental ArmorはConstruction 5、Forge要求**E2F1**のArmorで、装備者へ、

- **Shock Resistance +10**
- **Fire Resistance +10**
- **Cold Resistance +10**

を与えます。

参照するArmor record 59は、Defense modifier **-3**、Encumbrance **4**の重い鎧です。Item descriptionも、熱・寒さ・雷から装備者を守るplate hauberkとして説明しています。

したがって、このItemの取引は、

```text
三属性への広い耐性
＋
物理攻撃を受けるためのArmor

と引き換えに

Defense低下
＋
Encumbrance増加
＋
Armor Slot固定
```

です。

---

# 一属性を最大化するItemではない

Elemental Armorの強みは、Fireだけ、Coldだけ、Shockだけを極端に伸ばすことではありません。

価値が高いのは、敵Armyが、

- Fire damageを使うMage
- Cold damageを使うMage
- Shock damageを使うMage
- 属性の異なるSummonやWeapon

を混在させており、Carrier一体へ複数の耐性を同時に要求する時です。

```text
敵のDamage typeが一つに固定
→ 専門Resistance Itemの方がSlot効率が良い場合がある

敵のDamage typeが読みにくい／混在
→ Elemental Armorの三属性bundleが生きる
```

という関係です。

広さが強みであり、特定属性に対する完全な回答とは限りません。

---

# Armor Slotで耐性を確保する意味

ThugやCombat Casterは、Misc Slotへ、

- Amulet of Antimagic
- Ring of Regeneration
- Girdle of Might
- Amulet of Resilience
- Spell Focus
- Path Booster

を置きたいことがあります。

Elemental Armorで三属性耐性をArmor Slotへ移すと、Misc Slotを別の任務へ残せます。

これは単純なStats合計以上に重要です。

```text
Armor Slot: Elemental Armorで属性耐性
Misc Slot: MR・Regeneration・Reinvigoration
Hand Slot: Damage・Control
```

のように、Build全体の役割分担を作れるからです。

ただしCarrierに別の必須Armorがある場合、この利点は消えます。

---

# 重さは長期戦でCostになる

Armor record 59はDefense modifier -3、Encumbrance 4です。

これにより、Carrierは、

- 近接攻撃を回避しにくくなる
- 通常行動でFatigueを蓄積しやすくなる
- Self-buff後の余力が減る
- Quickness等で行動量を増やした時の負担が重くなる
- 長期戦でDefense低下や行動停止へ近づく

可能性があります。

属性Spellを耐えても、Chaffに囲まれてFatigue 100へ達すれば任務は失敗します。

したがって、Elemental Armorは、

```text
属性Damageを減らした結果、戦えるRoundが増えたか
```

だけでなく、

```text
Armorの重さで有効Roundを失っていないか
```

まで確認します。

---

# Amulet of Resilienceとの組み合わせ

[Amulet of Resilience](amulet-of-resilience.md)はReinvigorationをMisc Slotから補い、Elemental ArmorのEncumbrance負担を支える候補です。

```text
Elemental Armor
→ Fire / Cold / Shockへの広い耐性

Amulet of Resilience
→ 重装・Self-buff・長期戦のFatigueを軽減
```

と役割を分けられます。

ただしAmuletを装備すると、MR、Regeneration、別Resistance、Booster等のMisc Itemを一つ失います。

Fatigue対策を足した結果、MR-based Controlへ弱くなっていないかを確認します。

---

# Girdle of Mightとの違い

[Girdle of Might](girdle-of-might.md)もReinvigorationを補いますが、Strength +3とReinvigoration +3を組み合わせるItemです。

Elemental Armor Carrierが、

- 近接Damageも不足している
- Strengthを利用するWeaponを持つ
- Reinvigoration +3で十分

ならGirdleが合います。

一方、

- Damageは足りている
- Armor・Spell・長期戦のFatigueが主問題
- より強いReinvigorationを優先したい

ならAmulet of Resilienceを比較します。

Elemental Armorを装備した時点で、**敗因が属性DamageからFatigueへ移る**ことがあるため、Battle Replayから次の不足を選びます。

---

# 相性の良いCarrier

特に候補になるのは、

- 複数属性のBattle magicへ晒される前衛Mage
- Fire / Cold / Shockのどれが来るか読みにくいThug
- Misc SlotをMR・Regeneration・Boosterへ残したいCarrier
- 基礎DefenseよりProtection・Resistanceで受ける設計
- Reinvigorationを別枠で確保できるCommander
- E2F1 Forge accessを無理なく用意できるNation

です。

逆に、高Defenseを主防御にしている軽装Carrierへ着せると、Defense -3がBuildの中心を壊すことがあります。

---

# ProtectionとResistanceは別の防御層

Elemental Armorは鎧なので物理Protectionを与えますが、三属性Resistanceとは別に評価します。

- Armor Protectionで通常の物理Hitへ耐える
- Fire ResistanceでFire componentを減らす
- Cold ResistanceでCold componentを減らす
- Shock ResistanceでShock componentを減らす

という複数の防御層を一枠へ持ちます。

ただし、

- Armor Negating damage
- MRで抵抗するSpell
- Poison
- Acid
- Fatigue damage
- Soul Slay等のHP以外を攻める効果

へ同じように強いわけではありません。

「Elemental」という名前をUniversal defenseと読み替えないことが重要です。

---

# 専門Resistance Itemとの比較

敵がFire中心なら、Fire Resistanceをより安く、別Slotで確保できる可能性があります。

同様にCold、Shockにも専門Itemがあります。

Elemental Armorを選ぶ判断は、

- 三属性のうち何種類が実際に脅威か
- Armor SlotとMisc Slotのどちらが余っているか
- Carrierが重装を許容できるか
- E2F1 Forge accessを持つか
- 専門Itemを複数作るGem・Forge turnがあるか

で決まります。

一属性しか来ない戦場で三属性bundleへ払うと、使われないResistanceが増えます。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- E2F1 Forge Mageを確保できる
- Fire / Cold / Shockの複数属性が現実の脅威
- CarrierのArmor Slotが空いている
- Misc Slotを別機能へ残したい
- Defense -3を許容できる
- Encumbrance 4をReinvigorationや短期決戦で管理できる
- 現在のArmorより任務成功率が上がる
- Earth / Fire Gemを別ForgeやBattle magicから回せる

「三つのResistanceが付くから」ではなく、**三つのうち複数を実際に使い、重さを処理できる時**にForgeします。

---

# Forgeしない・別Itemを選ぶ条件

- 敵Damageが一属性へほぼ固定されている
- Poison / Acid / MR-based effectが主な脅威
- 高Defenseを維持することがBuildの中心
- Carrierが既にFatigue問題を抱えている
- Armor Slotへ別の必須効果がある
- E2F1 accessのために重いBooster chainが必要
- 三属性耐性をSpellやBlessで安く得られる
- Carrierが属性Damageを受ける前に別の理由で倒れる

Elemental Armorは防御範囲を広げますが、**間違った敗因へ防御を足すと高価な重装になるだけ**です。

---

# Counter：三属性以外の防御層を攻める

敵のElemental Armor CarrierへFire・Cold・Shockだけを重ねると、Itemの強みを正面から受けます。

Counterは、

- 高Damageの物理攻撃でProtectionを越える
- Armor Piercing / Armor Negating attackを使う
- PoisonやAcid等、三Resistance外のDamage typeを使う
- MR-based Controlや即死系でHP防御を迂回する
- Fatigue damageでEncumbrance負担を増幅する
- Chaffで囲み、長期戦へ引き込む
- 高Defense Targetを別に用意し、重装Carrierの命中・移動を浪費させる
- Carrierを避けてMage・Army・Provinceを狙う

のように、**Itemが一枠で守っていない軸**へ切り替えます。

---

# よくある失敗

## 三属性Resistanceがあるので何にでも強いと思う

Poison、Acid、MR-based effect、Fatigue等は別です。

## Defense -3を見ない

属性Spellへの耐性を得ても、通常攻撃の命中数が増えて倒れることがあります。

## Encumbrance 4を無視する

Self-buffや長期戦と重なると、Fatigueが新しい敗因になります。

## 一属性しか来ない戦場で使う

使われないResistanceへArmor SlotとForge costを払っています。

## Misc Slotが空くことを活用しない

Elemental Armorの利点の一つは、三ResistanceをArmor Slotへまとめることです。空いたMisc Slotへ任務に必要な機能を置けなければ、bundleの価値は下がります。

---

# Test game checklist

```text
[ ] C5・E2F1でElemental ArmorがForge可能か確認
[ ] Item 249 / Armor record 59であることを確認
[ ] Shock / Fire / Cold Resistance +10が反映されることを確認
[ ] Defense modifier -3を装備前後で確認
[ ] Encumbrance 4を装備前後で確認
[ ] Fire damageへの生存Roundを比較
[ ] Cold damageへの生存Roundを比較
[ ] Shock damageへの生存Roundを比較
[ ] RoundごとのFatigue推移を記録
[ ] Amulet of Resilience / Girdle of Might併用時を比較
[ ] 専門Resistance ItemとのSlot・Gem効率を比較
[ ] Poison / Acid / MR-based Counterでは守れないことを確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 249](../../data/items/by-id/249.md)
- [Amulet of Resilience](amulet-of-resilience.md)
- [Girdle of Might](girdle-of-might.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Resistance Item](../resistance-items.md)
- [Thug・SC装備](../thug-equipment.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description / Armor record 59
- BaseI: C5 / E2F1 / Shock・Fire・Cold Resistance +10
- Armor record 59: Defense modifier -3 / Encumbrance 4
- 実際のDamage軽減、Fatigue推移、別Resistanceとの重なりはゲーム内Unit画面とBattle Replayを優先
