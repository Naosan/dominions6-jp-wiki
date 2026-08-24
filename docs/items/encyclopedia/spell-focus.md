---
title: "Spell Focus"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 370
---

# Spell Focus

**MRで抵抗できるSpellのPenetrationを補い、高MRの重要TargetへStatus・Control・即死系効果を通しやすくするConstruction 5のCaster Item。**

Spell FocusはSpell Damageを一律に増やすItemではありません。攻略上は、**Magic Resistance checkで失敗しやすいSpellだけの成功率を押し上げる専門装備**として評価します。

さらに装備者へLuckに似た副作用を与えますが、そのLuckは使い切ると悪い方向へ反転します。恒久的な防御Itemとしては扱わず、Caster強化の付随Riskとして管理します。

- [Dominions 6.35固定データ — Item 370](../../data/items/by-id/370.md)
- [Magic Item攻略辞典](index.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)

---

# まず何ができるか

6.35固定データでは、Spell FocusはConstruction 5、Forge要求**S1**のMiscellaneous Itemです。

Item descriptionでは、

- Spell Focusを使って唱えたSpellはMagic Resistanceで抵抗しにくくなる
- 特に敵MageへMR-negates Spellを使う時に有用
- 装備者へLuckが生じる
- そのLuckは使われた後に悪いLuckへ変わる

と説明されています。

したがって主効果は、

```text
MR checkを行うSpell
→ 抵抗される確率を下げる方向へ補助
```

です。

```text
すべてのSpell
→ Damage・Range・Accuracy・Cast回数が上がる
```

という万能Caster Itemではありません。

---

# 最初に「そのSpellはMRを使うか」を確認する

Spell Focusの価値は、使用SpellがMagic Resistance checkを行う時だけ発生します。

Spell説明や戦闘Logで、

- Magic Resistance negates
- Magic Resistance negates easily
- Magic Resistance check for partial effect
- MRを使わないDamage / Battlefield effect

を区別します。

MR checkがないSpellへSpell Focusを持たせても、主効果は勝敗へ寄与しません。

そのため装備計画は、

```text
Casterを選ぶ
→ Itemを持たせる
→ Spellを考える
```

ではなく、

```text
通したいMR-negates Spellを選ぶ
→ TargetのMRを想定
→ 必要なCasterとPenetration sourceを組む
```

の順で行います。

---

# 高MR Targetほど価値が見えやすい

低MRの一般兵へ大量にSpellを撃つ場合、Itemなしでも十分に効果が通ることがあります。

Spell Focusが重要になるのは、

- 敵Mage
- Commander
- Thug / SC
- 高MR Sacred
- MR Itemを積んだ重要Carrier
- 一回の抵抗成功が戦闘全体を変えるTarget

へSpellを通したい時です。

特に、

```text
成功すれば敵の重要Unitを無力化
失敗すればCasterの一行動を失う
```

Spellでは、成功率の小さな改善でも期待値が大きくなります。

---

# Penetrationは確定成功ではない

Spell Focusは抵抗を困難にしますが、MR checkそのものを消すItemではありません。

高MR Targetには、Itemを持っていても抵抗されることがあります。

実戦では、

- CasterのPath level
- Spell固有のMR補正
- Penetration Item
- TargetのMR
- Anti-Magic等のBattlefield buff
- 複数回試行できるCaster数

を合わせて考えます。

```text
一回の成功率を上げる
＋
試行回数を増やす
```

の両方を使う方が安定します。

Spell Focus一個に勝敗を依存させず、複数Casterや別Counter軸を用意します。

---

# Damage ItemではなくControl Itemとして強い

Spell Focusは、単純なDamage Spellより、成功時にTargetの機能を大きく失わせるSpellと相性が良くなります。

例えば目的は、

- 行動不能にする
- Charm / Enslave系で奪う
- 即死・Soul系効果を狙う
- Battlefieldから退場させる
- 高価なMageのScriptを崩す
- Buff済みThugをMR軸で止める

ことです。

ただし具体的なSpellがMR checkを使うか、Target制限があるかは個別Spell recordを確認します。

「強いStatus SpellだからSpell Focus」という一般化ではなく、**抵抗方式を確認してから採用**します。

---

# Luckの副作用は恒久防御ではない

Item descriptionでは、Spell FocusがMageへLuckを与える一方、そのLuckは使われた後に悪い方向へ変わると説明されています。

これは通常の安定したLuck Itemと同じものとして扱うべきではありません。

確認すべきなのは、

- どの攻撃・Damage・判定でLuckが消費されるか
- 消費後にどのStatusへ変化するか
- Battle中に表示がどう変わるか
- 次のBattleへ状態が持ち越されるか
- Retreat / Death / Item removalでどう扱われるか

です。

攻略上は、

```text
短期的な防御上振れ
＋
消費後の下振れRisk
```

を持つItemとして考えます。

Luckがあるから前線へ出してよい、とは判断しません。

---

# Casterは後方で守る

Spell Focusの価値は、CasterがScriptしたMR-negates Spellを実際に唱えることで生まれます。

したがって、

- Missileから守る
- Bodyguardを付ける
- Flying / Fast attackerの侵入を防ぐ
- Fatigueを管理する
- Range内へTargetが入る配置にする
- Spell選択AIが別Spellへ逸れないようScriptする

必要があります。

高価なPenetration Itemを持たせても、Casterが一発目を唱える前に倒れれば価値は0です。

---

# Path Boosterとの違い

Path Boosterは、

- 新しいSpell thresholdへ届く
- Fatigueを下げる
- DamageやAreaがPath scalingするSpellを強化する
- Ritual / Forge accessを広げる

ことがあります。

Spell FocusはPath levelを上げるItemではなく、主にMR抵抗を突破するための専門装備です。

そのため、Misc Slotが競合する場合は、

```text
BoosterでSpell自体を使えるようにする
vs
Spell Focusで既に使えるSpellを通しやすくする
```

を比較します。

Spellを唱えられなければPenetrationは意味がないため、通常はThreshold確保が先です。

---

# Amulet of Antimagicとの対称関係

[Amulet of Antimagic](amulet-of-antimagic.md)はCarrierのMRを上げ、敵のMR-based effectへ抵抗しやすくします。

Spell Focusは逆に、Caster側からTargetのMRを突破しやすくします。

```text
Spell Focus
→ 攻撃側のMR突破

Amulet of Antimagic
→ 防御側のMR強化
```

という対称関係です。

敵がAmulet of Antimagicを見せたからSpell Focus一個で相殺できる、と単純には決まりません。最終MR、Spell補正、複数のPenetration sourceを合わせてTestします。

---

# Misc Slotの機会費用

Spell FocusはMisc Slotを一つ使います。

Casterが同じSlotへ欲しいものには、

- Path Booster
- Amulet of Antimagic
- Elemental Resistance
- Reinvigoration
- Gem生成 / temporary gem Item
- Research Item
- Mobility Item

があります。

特に前線Casterでは、Penetrationを上げる代わりにMRやResistanceを失うと、Spellを唱える前に倒される可能性があります。

Item単体の成功率上昇ではなく、**Casterが予定行動を完了する確率**で比較します。

---

# 複数Casterへ配るか、一人へ集中するか

Spell Focusを一個だけ作る場合、最も重要なSpellを使うCasterへ持たせます。

複数作る場合は、

- 同じTargetへ試行回数を増やす
- 複数TargetへControlを分散する
- Main casterが倒れた時のBackupを作る
- 別ArmyにもMR Counterを持たせる

ことができます。

ただしS Gem、Forge turn、Misc Slotが増えるため、Target数と戦争計画を超えて量産しないようにします。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- S1 Forge Mageを確保できる
- 通したいMR-negates Spellが決まっている
- CasterがそのSpell thresholdへ既に届く
- 敵の重要Targetが高MR
- 一回の成功が戦闘結果を大きく変える
- Casterを安全にScript完了まで守れる
- Misc SlotへBoosterや必須防御が不要
- Luck副作用を理解しTest済み

「Astral ItemだからMageへ持たせる」のではなく、**対象SpellとTargetが決まった時にForge**します。

---

# Forgeしない・別Itemを選ぶ条件

- 主力SpellがMR checkを使わない
- BoosterなしではSpell thresholdへ届かない
- CasterがRangeやFatigueでSpellを撃てない
- 敵TargetのMRが低くItemなしで十分
- Battlefield spellや直接Damageの方が確実
- Misc Slotへ生存用Itemが必須
- Luck反転のRiskを許容できない
- S GemをCommunion、Teleport、Booster等へ回す必要がある

Spell Focusは万能Caster装備ではなく、**MR checkを攻める時だけ強い専門Item**です。

---

# Counter：MRを上げるだけではない

敵がSpell Focusを使っている場合、第一候補はMR強化ですが、他の方法もあります。

- Amulet of AntimagicやAnti-MagicでMRを上げる
- 高価なTargetを分散し、一発で戦局が崩れないようにする
- ChaffやDecoyでTarget selectionを乱す
- Spell Focus CarrierをMissile / Assassin / Flying unitで狙う
- Range外から攻める
- CasterへFatigueやSilence系Controlを掛ける
- MR checkを受ける前にBattleを短く終わらせる

Penetration勝負だけへ付き合わず、**Casterが試行できる回数を減らす**ことも有効です。

---

# よくある失敗

## すべてのSpellが強くなると思う

主効果はMRで抵抗されるSpell向けです。

## Damage・Range・Cast speedも上がると思う

Item descriptionはMR抵抗の突破を中心に説明しています。別Statsは個別に確認します。

## Spell thresholdを無視する

Spell FocusはPath Boosterではありません。唱えられないSpellは使えるようになりません。

## 一回で高MR Targetへ確実に通ると思う

MR checkは残ります。複数試行とBackup planを用意します。

## Luckを恒久防御と思う

Luckは使われた後に悪い方向へ変わる副作用があります。

## Caster防御を外す

Penetrationを上げても、詠唱前に倒されれば意味がありません。

---

# Test game checklist

```text
[ ] C5・S1でSpell FocusがForge可能か確認
[ ] Item 370であることを確認
[ ] MR-negates Spellの成功率をItemなし／ありで比較
[ ] MR checkのないSpellへ影響しないことを確認
[ ] Path level・Damage・Range・Cast回数が変化するか表示で確認
[ ] 高MR / 低MR Targetの両方で複数回Test
[ ] Luckの初期表示を確認
[ ] Luckがどの判定で消費されるか確認
[ ] 消費後にどの悪いStatusへ変わるか確認
[ ] 次Battleへの持越しとItem removal時の状態を確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 370](../../data/items/by-id/370.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Skull Staff](skull-staff.md)
- [Thistle Mace](thistle-mace.md)
- [Bottle of Living Water](bottle-of-living-water.md)
- [Shroud of the Battle Saint](shroud-of-the-battle-saint.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- MR突破効果とLuck反転はItem descriptionを正本とする
- 成功率、Spell固有MR補正、Luck消費条件、反転後Statusはゲーム内Spell description・Unit画面・反復Testを優先
