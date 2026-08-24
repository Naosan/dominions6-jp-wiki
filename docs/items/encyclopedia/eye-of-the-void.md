---
title: "Eye of the Void"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 371
---

# Eye of the Void

**MRで抵抗されるSpellのPenetrationを+2する代わりに、装備者自身のMRを-2し、眼の置換とVoid視覚を伴うConstruction 5の高Risk Caster Item。**

Eye of the Voidは「すべてのSpellを強くするItem」ではありません。攻略上は、**MR-negates Spellを通す確率を上げる攻撃投資と、Caster自身が敵Spellへ弱くなる防御低下を交換するItem**として評価します。

- [Dominions 6.35固定データ — Item 371](../../data/items/by-id/371.md)
- [Magic Item攻略辞典](index.md)
- [Spell Focus](spell-focus.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

---

# まず何ができるか

6.35固定データでは、Eye of the VoidはConstruction 5、Forge要求**S1**のMiscellaneous Itemです。

主要効果は、

- **Penetration +2**
- **Magic Resistance -2**
- Illusionを見抜くVoid由来の視覚効果
- 眼を置換する装備形態

です。

Item descriptionでは、死んだVoid beingの眼を、取り除いた眼のsocketへ入れることで、

- 世界の真の姿を見る
- Illusionを非常に効果的に見破る
- Spellをより効果的に使う
- 敵Spellへより脆弱になる

と説明されています。

---

# Penetration +2が効くSpellを選ぶ

Penetration Bonusは、敵がMagic Resistanceで抵抗するSpellへ価値があります。

したがってEye of the Voidを装備する前に、Script内のSpellを、

```text
MRで抵抗されるSpell
MRで抵抗されないSpell
```

に分けます。

Eyeの価値が高いのは、

- 高MR Commanderを狙う
- MR-negates Controlを通す
- 単体または少数の重要TargetへSpellを当てる
- 一回の抵抗失敗がBattleを変える

場合です。

Damage SpellやBattlefield effectでMR判定を使わないものに対しては、Penetration +2が期待した形で働かないことがあります。

---

# すべてのCaster性能が上がるわけではない

Eye of the Voidは、

- Magic Path
- Spell Range
- Area of Effect
- Research
- Reinvigoration
- Spell回数

を一律に増やすItemではありません。

```text
Penetrationが敗因
→ Eyeが直接効く

Path不足が敗因
→ Boosterが必要

Fatigueが敗因
→ Reinvigorationが必要

Range不足が敗因
→ 別の対策が必要
```

です。

「Caster Itemだから強い」ではなく、目的Spellの抵抗判定へPenetration +2が関与するかを確認します。

---

# MR -2は本物の代償

Eye of the Voidは装備者のMRを-2します。

これは敵のMR-negates Spell、Control、特殊効果へCaster自身が弱くなることを意味します。

特に、

- Communion Master
- 貴重な高Path Mage
- 前線Battle Mage
- Assassinationを受けやすいCommander
- 敵Casterから狙われる大型Unit

では、攻撃性能を上げる代わりに死亡・Control Riskが増えます。

```text
敵へSpellを通しやすくなる
＋
敵Spellも自分へ通りやすくなる
```

という対称的な交換として理解します。

---

# 後衛に置けばMR低下が消えるわけではない

後衛配置は近接攻撃や一部MissileからCarrierを遠ざけますが、MR -2そのものは残ります。

敵が、

- Long-range Spell
- Battlefield-wide effect
- Remote attack
- Assassination
- Flying / Stealth Raider

を使う場合、後衛でも狙われます。

Eye Carrierを安全にするには、配置だけでなく、

- Bodyguard
- MR補助
- Resistance
- Retreat route
- Mage screen
- 敵Casterへの先制

を含めて考えます。

---

# Illusionを見破る視覚効果

Item descriptionでは、Eyeにより世界の真の姿が見え、Illusionを非常に効果的に見破れると説明されています。

この効果は、Glamour・Illusion・見かけを利用する敵に対して追加価値を持ちます。

ただし、

- どの特殊能力がゲーム内表示へ付くか
- どのIllusion・Image処理へ作用するか
- Scout情報とBattle内Targetingのどちらへ効くか

は、固定表の一語だけで広く断定せず、対象UnitとのTest gameで確認します。

Eyeを「Penetration +2だけのItem」と見ると、この視覚用途を見落とします。

---

# 眼の置換を伴うItem

Item descriptionは、新しく取り除いた眼のsocketへVoid eyeを入れると説明しています。

そのため、通常の指輪や護符のような気軽な着脱Itemとして扱わず、

- Carrierに眼があるか
- すでにEye afflictionがあるか
- 装備時にどのAfflictionが付くか
- 外した時に元の眼が戻るか
- Itemを他Carrierへ渡せるか
- Shape change後にどう扱われるか

をTestします。

眼の置換・解除挙動を確認せず、唯一の高Path Mageへ最初から装備するのは危険です。

---

# Carrier選択

相性が良いCarrierは、

- MR-negates Spellを主力にする
- Penetration +2で成功率が意味のある形で変わる
- 後方から安全にScriptを実行できる
- 元のMRが十分高い
- 眼の置換Riskを許容できる
- Misc SlotをBoosterや防御Itemへ使わない
- Illusion看破にも価値がある

Mageです。

逆に、

- MRが元から低い
- 前線で敵Spellを受ける
- Path Boosterが必須
- 主力SpellがMR判定を使わない
- 眼やShapeに特殊制約がある

Carrierでは慎重にします。

---

# 高MR Targetへ使う

Eye of the Voidの主な目的は、通常の兵を大量に削ることより、**高MRの重要TargetへMR-negates Spellを通すこと**です。

対象には、

- Enemy Mage
- Thug / SC
- Commander
- Sacred elite
- Summoned elite
- Battleを支えるSupport Unit

があります。

ただしTargetのMRが非常に高い場合、Penetration +2だけで十分な成功率になるとは限りません。

Spell回数、Caster数、別のPenetration source、Target selectionも合わせます。

---

# Spell Focusとの違い

[Spell Focus](spell-focus.md)もMR-negates Spellを通しやすくするMisc Itemです。

大きな違いは、

```text
Spell Focus
→ Penetration補助
→ Luckと、その消費後の不安定な副作用

Eye of the Void
→ Penetration +2
→ MR -2
→ 眼の置換
→ Illusion看破
```

です。

Eyeはより大きなPenetration Bonusを持ちますが、Carrier自身のMRを下げます。

Spell Focusは別種のRiskを持つため、

- 目的Spellの重要度
- CarrierのMR
- Luck副作用
- 眼の置換
- Misc Slot

を比較します。

同じ「Penetration Item」として一括りにしないことが重要です。

---

# Amulet of Antimagicとの緊張関係

[Amulet of Antimagic](amulet-of-antimagic.md)はMRを増やし、Eye of the VoidはMRを減らします。

両方を装備できるSlotがある場合、MR低下を補いながらPenetrationを得るBuildも考えられます。

ただしMisc Slotを二つ使うため、

- Path Booster
- Reinvigoration
- Resistance
- Regeneration
- Mobility

を置けなくなります。

```text
Eyeで攻撃成功率を上げる
＋
Amuletで自己防御を戻す
```

ことが、二枠分の価値を生むかを確認します。

元のMRが十分なら別Itemを優先できる場合もあります。

---

# Communionでの注意

Communion参加MageへEyeを持たせる場合、役割ごとにRiskが違います。

- Masterが重要Spellを通すために使う
- SlaveがMR低下を負う必要はない
- MasterがControlされるとCommunion全体のScriptが崩れる
- Misc SlotがMatrixやBoosterと競合する

ため、単純なPenetration最大化だけで決めません。

特にMasterのMR -2が敵Counterへ直結する場合、Spell Focusや別Caster増員の方が安全なことがあります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- S1 Forge Mageがいる
- 主力SpellがMR-negates
- 高MRの重要Targetを倒す必要がある
- Penetration +2で成功率改善が見込める
- Carrierの元MRが十分
- 後方配置・Bodyguard等で守れる
- 眼の置換挙動をTest済み
- Illusion看破にも価値がある
- Misc Slotを使ってもBuildが成立する

「敵のMRが高い」だけでなく、**何のSpellを誰へ通すか**まで決めます。

---

# Forgeしない・別Itemを選ぶ条件

- 主力SpellがMR判定を使わない
- Path不足が本当の問題
- CarrierのMRが低く、-2が致命的
- EnemyがMR-based Counterを多用する
- 眼の置換を許容できない唯一のMageである
- Misc Slotへ必須Boosterがある
- Spell Focusで十分
- Caster数を増やす方が安全
- TargetのMRが高すぎて+2だけでは不足
- EnemyがIllusionを使わず視覚効果の価値が低い

Eyeは攻撃的ですが、Carrierを失えばPenetration投資ごと消えます。

---

# Counter：MR -2を逆利用する

敵のEye of the Void Carrierは、こちらへMR-negates Spellを通しやすくする一方、自分のMRを下げています。

Counterは、

- MR-negates SpellをEye Carrierへ返す
- Assassinationで低下した自己防御を突く
- Long-range ControlでScript前に止める
- Missile・Flying Unitで後衛を狙う
- Bodyguardを別攻撃で剥がす
- Carrierを倒さずRetreatさせる
- Target側のMRをさらに上げる
- Caster数・Spell回数に耐えるChaffを用意する

ように、**Eyeが作った攻撃力と防御低下の両方**を読みます。

Illusionだけに依存した防御は、Eyeの視覚効果で弱くなる可能性があるため、Protection・MR・数・配置も重ねます。

---

# よくある失敗

## すべてのSpellが強くなると思う

PenetrationはMR判定へ関係します。Path、Range、Damage、Cast回数は別です。

## MR -2を無視する

重要Casterが敵のControlへ弱くなり、Scriptを完走できないことがあります。

## 眼の置換を確認せず装備する

装備・解除・Afflictionの挙動を小さなTest gameで先に確認します。

## 高MR Targetへ一人だけで挑む

Penetration +2でも確定成功ではありません。試行回数と別Counterを用意します。

## Spell Focusと同じItemだと思う

Bonus量、自己MR低下、Luck副作用、視覚効果、眼の扱いが違います。

## 前線Casterへ無防備に持たせる

Penetrationを使う前に、近接・Missile・敵Spellで倒されることがあります。

---

# Test game checklist

```text
[ ] C5・S1でEye of the VoidがForge可能か確認
[ ] Item 371であることを確認
[ ] 装備後にPenetration +2を確認
[ ] 装備後にMR -2を確認
[ ] 眼のAffliction・装備条件を確認
[ ] Itemを外した時の眼とAfflictionを確認
[ ] MR-negates Spellの成功率を複数回比較
[ ] MRを使わないSpellでは差がないか確認
[ ] Illusion / Glamour Unitへの視覚効果を確認
[ ] Spell Focusとの成功率・Riskを比較
[ ] Amulet of Antimagic併用時の最終MRを確認
[ ] Assassination・敵Controlへの耐性を確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 371](../../data/items/by-id/371.md)
- [Spell Focus](spell-focus.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Skull Staff](skull-staff.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Magic Item固有効果・発動効果](../effects-and-procs.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- Dominions 6 Main Manual — Magic Resistance / Penetration / Affliction / Illusion
- 眼の置換・解除、視覚効果、実際の抵抗判定はゲーム内表示とTest battleを最終確認
