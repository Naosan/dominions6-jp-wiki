---
title: "Ring of Fire"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-25"
item_id: 309
---

# Ring of Fire

**Fire Resistance +15をMisc Slotから一人へ与え、Fire damageと熱環境へ早期対応するConstruction 1の専門Resistance Item。**

Ring of Fireは「炎に完全無敵になるRing」ではありません。攻略上は、**敵の主Damage typeがFireだと読めた時、重要Commander一体の耐性穴を小さいResearch投資で塞ぐItem**として評価します。

- [Dominions 6.35固定データ — Item 309](../../data/items/by-id/309.md)
- [Magic Item攻略辞典](index.md)
- [Resistance Item](../resistance-items.md)
- [Elemental Armor](elemental-armor.md)
- [Charcoal Shield](charcoal-shield.md)

---

# まず何ができるか

6.35固定データでは、Ring of Fireは、

- Construction 1
- Forge要求 **F1**
- Miscellaneous Slot
- **Fire Resistance +15**

を持ちます。

Item descriptionは、RingのRubyが火を食べ、装備者を熱と炎からほぼ完全に守ると説明しています。

ただし、攻略上の正本は固定fieldのFire Resistance +15です。

```text
装備前のFire Resistance
＋ Ring of Fireの+15
→ 装備後の表示値と実戦結果を確認
```

と読み、説明文の「ほぼ完全」を、すべてのFire関連効果を無条件で無効化する保証へ拡張しません。

---

# 一属性へ深く寄せるItem

Ring of Fireの強みは、Fire・Cold・Shockを少しずつ補うことではありません。

```text
敵の主力がFire
→ Fire Resistance +15がほぼ全て働く

敵の主力がCold / Shock / Poison / MR attack
→ Ringの主要効果は働かない
```

という、非常に明確な専門Itemです。

そのため、敵の構成が読めるほど価値が上がります。

- Fire Evocation
- Fire Shieldを持つ近接Carrier
- Fire Elemental
- Fire系Weapon
- Heatを伴うBattlefield環境
- Fire damageを重ねるThug / SC

など、実際に受けるDamage typeをUnit詳細とBattle Replayで確認してから投入します。

---

# Construction 1で間に合うことが最大の強み

Ring of FireはC1で解禁されます。

これは、

- C5の複合防具までResearchする
- 高位Resistance Spellを解禁する
- 複数Itemを組み合わせる

より前に、Fire対策を一体へ渡せることを意味します。

```text
敵のFire圧力が目前
→ C1とF1でRingを用意
→ 重要Commanderだけ先に守る
```

という短い対応ができます。

一方で、C1だから自動的に最優先ではありません。敵がFireを使わないなら、早く作れても任務は増えません。

---

# Army全体ではなく重要Carrierを守る

Ring of Fireが守るのは装備者一体です。

候補になるのは、

- Fire damageへ晒されるBattlefield caster
- Fire Shield持ちへ接触するThug
- Fire Evocationを受けながら前進するCommander
- 高価なCommunion / Sabbath Master
- Fire battlefieldの中心でScriptを完遂するMage
- Fire Vulnerabilityや低い素Resistanceを補いたい重要Unit
- Army-wide Fire Resistanceを受け損ねる単独Raider

です。

通常兵の大軍全体を守る必要があるなら、Itemを大量配布するより、Army-wide Spell、Bless、Unit選択、陣形、Caster排除を比較します。

---

# Protectionの代わりではない

Fire ResistanceはFire componentへ対応します。

Ringを装備しても、

- 通常物理Damage
- Cold / Shock / Poison / Acid
- MR-negates Control
- Fatigue damage
- Morale崩壊
- Affliction
- Surroundと通常攻撃

を同じように防ぐわけではありません。

```text
Fireで死ぬ
→ Ring of Fireが敗因へ直接作用する

物理・MR・Fatigueで死ぬ
→ Ringを足しても敗因が残る
```

と分けます。

Fire対策後に何が新しい敗因になるかをReplayで確認します。

---

# Fire MageだけのItemではない

Forge要求はF1ですが、Carrier自身がFire Mageである必要はありません。

むしろ、

- 素のFire Resistanceを持たないAstral Mage
- Fire Shieldへ接触するEarth / Nature Thug
- Fire battlefieldへ入るPriest
- Fire対策を持たないSummoned Commander

など、Fire accessを持たないCarrierへ渡す価値があります。

Fire Mageは種族・Unitごとに素Resistanceが異なるため、「Fire Mageだから不要」「Fire Mageだから必要」とPathだけで決めません。

---

# Misc Slotの競合

Ring of FireはMisc Slotを一つ使います。

同じ枠には、

- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Amulet of Resilience](amulet-of-resilience.md)
- [Girdle of Might](girdle-of-might.md)
- Path Booster
- Mobility Item
- 別属性のResistance Ring

が入ります。

したがって、

```text
Fire Resistanceを足して生き残る価値
vs
MR / Regeneration / Reinvigorationを失うCost
```

を比較します。

Misc Slotが一つしかないCarrierでは、Ringを付けた結果、MR-based ControlやFatigueへ弱くなることがあります。

---

# Elemental Armorとの比較

[Elemental Armor](elemental-armor.md)はArmor SlotからFire・Cold・Shock Resistanceをまとめて与えます。

| Item | 解禁 | Forge要求 | Slot | Resistanceの幅 |
|---|---:|---:|---|---|
| Ring of Fire | C1 | F1 | Misc | Fire +15へ集中 |
| Elemental Armor | C5 | E2F1 | Armor | Fire・Cold・Shockをまとめる |

Ring of Fireが向くのは、

- Fireだけが主脅威
- C1段階で急いでいる
- Armor Slotを別防具へ使いたい
- 重装ArmorのDefense / Encumbrance負担を避けたい

場合です。

Elemental Armorが向くのは、

- 複数属性が同時に来る
- Misc SlotをMR・Regeneration・Boosterへ残したい
- Carrierが重装の負担を処理できる

場合です。

「Resistance合計」だけでなく、Research timingとSlot配置で選びます。

---

# Charcoal Shieldとの比較

[Charcoal Shield](charcoal-shield.md)もFire対策をBuildへ組み込み、近接攻撃者への反撃機能を持つShieldです。

```text
Ring of Fire
→ Misc Slot
→ Fire Resistanceへ集中
→ Hand Slotを空ける

Charcoal Shield
→ Hand Slot
→ Shield防御と接触Punishも担う
→ Weapon / Boosterとの手Slot競合がある
```

後方CasterをFireから守るだけならRingの方が役割を理解しやすい場合があります。

近接CarrierがShield防御と接触反撃も必要ならCharcoal Shieldを比較します。

---

# 他のResistance Ringとの持ち替え

同じC1帯には、

- [Ring of Tamed Lightning](ring-of-tamed-lightning.md)：Shock Resistance +15
- [Ring of Frost](ring-of-frost.md)：Cold Resistance +15
- [Snake Ring](snake-ring.md)：Poison Resistance +30とPoison Touch

があります。

同じCarrierへ固定装備するより、Enemy compositionに合わせてLabで持ち替える運用が有効です。

```text
対Fire戦
→ Ring of Fire

対Air / Lightning戦
→ Ring of Tamed Lightning

対Cold戦
→ Ring of Frost

対Poison戦
→ Snake Ring
```

この柔軟性は、C1専門Ring群を一つの常設Buildではなく、**偵察結果へ応じる工具箱**として見る理由です。

---

# Spell・Blessとの重なり

Carrierがすでに、

- 素のFire Resistance
- Bless
- Self-buff
- Army-wide Fire Resistance
- 別Item

から十分な値を得ている場合、Ringの+15は過剰になることがあります。

一方、Army-wide Spellが、

- Script前にCasterを守れない
- 単独Raiderへ届かない
- DispelやCaster死亡で失われる
- Researchが間に合わない

場合、常時ItemであるRingに価値があります。

装備前後の表示値とBattle結果を比較し、Ringが実際に生存Roundを増やしているかを確認します。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 1へ到達済み
- F1 Forgerを確保できる
- 敵の主要DamageがFireだと確認できる
- 一体の重要Commanderを守れば戦術が成立する
- Armor / Hand Slotを別任務へ残したい
- Misc Slotの競合よりFire対策を優先できる
- Army-wide対策のResearchが間に合わない
- Ringを戦線間で持ち回せる
- Fire Gemを別の緊急用途から回せる

早いから作るのではなく、**目前のFire敗因をC1で消せる時**に作ります。

---

# Forgeしない・後回しにする条件

- 敵がFire damageをほとんど使わない
- Carrierの素Fire Resistanceで十分
- Army-wide SpellやBlessで必要値を得られる
- 敗因がMR、Physical、Poison、Fatigueにある
- Misc Slotへ必須BoosterやMR Itemがある
- 守りたい対象が大軍で、Ring一個では範囲不足
- Fire Casterを先に倒す方が安い
- C1 ResearchとForge turnを別のTimingへ使う必要がある

Ringは狭い問題へ強いItemです。問題が違えば価値は急に下がります。

---

# Counter：Fire以外へ攻撃軸を切り替える

敵CarrierがRing of Fireを装備しているなら、Fireだけを重ねるとRingの専門性を正面から受けます。

Counterは、

- Cold / Shock / Poison / AcidへDamage typeを変える
- 高Damage物理でProtectionを越える
- MR-negates Controlや即死系を使う
- Fatigueを蓄積させる
- Chaffで囲み長期戦へ引き込む
- Ringで空いた防御穴をScoutする
- Carrierを避けてMage・Army・Provinceを狙う
- Forge hub、Lab、Item transportをRaidする

のように、Ringが守っていない軸へ移します。

Ringを見たからFire戦術を全廃するのではなく、Battle Replayで実際の軽減と残るDamageを確認します。

---

# よくある失敗

## 「ほぼ完全な免疫」を完全無効と読む

説明文ではなく、現在のFire Resistance表示とBattle結果を確認します。

## 敵のDamage typeを見ずに常設する

Fireが来ない戦闘ではMisc Slotが働きません。

## Protectionまで上がると思う

Ringの主要効果はFire Resistanceです。通常物理防御は別に用意します。

## Army全体が守られると思う

守られるのは装備者です。大軍には別の配布手段を検討します。

## Misc Slot競合を無視する

Fireを耐えても、失ったMR・Regeneration・Reinvigorationが新しい敗因になることがあります。

## 素Resistanceと重ねすぎる

過剰なFire ResistanceへSlotを払い、別の防御穴を残すことがあります。

---

# Test game checklist

```text
[ ] C1・F1でRing of FireがForge可能か確認
[ ] Item 309であることを確認
[ ] Fire Resistance +15が装備画面へ反映されることを確認
[ ] 装備前後のFire Resistance合計を記録
[ ] Fire Evocationに対するDamageと生存Roundを比較
[ ] Fire Shieldへ接触した時の結果を比較
[ ] Heatを伴うBattlefieldでFatigue / Damage推移を比較
[ ] Army-wide Fire Resistance Spellとの重なりを確認
[ ] Elemental ArmorとのSlot・Research timingを比較
[ ] Charcoal ShieldとのHand / Misc Slot差を比較
[ ] Ringを外した時に別の防御穴が埋まるか確認
[ ] Cold / Shock / Poison / MR-based Counterには別対策が必要か確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 309](../../data/items/by-id/309.md)
- [Resistance Item](../resistance-items.md)
- [Elemental Armor](elemental-armor.md)
- [Charcoal Shield](charcoal-shield.md)
- [Ring of Tamed Lightning](ring-of-tamed-lightning.md)
- [Ring of Frost](ring-of-frost.md)
- [Snake Ring](snake-ring.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Ring of Regeneration](ring-of-regeneration.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- BaseI: C1 / F1 / Miscellaneous / Fire Resistance +15
- Item description: Rubyが火を吸収し、装備者を熱と炎から守る
- 実際のDamage軽減、他のResistanceとの重なり、Battlefield effectへの影響はゲーム内表示とBattle Replayを優先