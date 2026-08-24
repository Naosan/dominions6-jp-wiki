---
title: "Amulet of Antimagic"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 369
---

# Amulet of Antimagic

**重要CommanderのMagic Resistanceを大きく補い、MR依存の即死・支配・行動阻害へピンポイントで備えるConstruction 5の防御Item。**

Amulet of Antimagicは「防御力を全部上げる」Itemではありません。**敵の勝ち筋がMR checkを通すことに依存しているとき、その一軸を強くするCounter**です。

- [Dominions 6.35固定データ — Item 369](../../data/items/by-id/369.md)
- [Resistance・Utility Item攻略](../resistance-items.md)
- [Magic Item総論](../index.md)

---

# まず何ができるか

6.35固定データでは、Amulet of AntimagicはConstruction 5のMiscellaneous Itemで、Forge要求は**S1**、基礎Costは**5S**、抽出される主要能力は**MR +4**と**Antimagic**です。

このページでは、固定データから確実に読める`MR +4`を中心に評価します。

`Antimagic`というItem flagの細かな相互作用は、対象SpellやPatchで誤読しないよう**ゲーム内表示・Test gameを優先**します。Army全体へ`Antimagic` Spellを自動展開するItemだとは扱いません。

---

# MRは「万能防御」ではない

Magic Resistanceを上げる価値は、敵の攻撃がMRで防げるときに発生します。

典型的には、

- 即死・Soul系のMR check
- Charm / Control系
- 一部の行動阻害
- 一部の特殊攻撃

など、**MR Negates / MR checkが明示された効果**への生存率を改善します。

一方で、

- 通常の物理Damage
- Elemental Damage
- Armor NegatingでもMRを使わない攻撃
- Poison
- Fatigue
- 大量の通常攻撃

まで止めるItemではありません。

敵のDamage sourceを分解してから作ります。

---

# 「MRが低いから装備」ではなく敵の勝ち筋から逆算する

MRは高いほど一般に安全ですが、Misc slotとGemは有限です。

Forge判断は、

```text
Enemyの重要攻撃
→ MRで防げる？
→ Carrierがその攻撃を受ける？
→ +4 MRで生存率を上げる価値がある？
→ Misc slotを使う価値がある？
```

の順で行います。

敵がFire / Shock / Poisonで倒してくるなら、Amuletより対応Resistanceを優先した方がよい場合があります。

---

# 誰に持たせるか

優先候補は、**死ぬと国家全体への損失が大きいCommander**です。

- Rare high-path Mage
- Battlefield caster
- Thug / Supercombatant
- Artifact carrier
- Booster chainの要
- Retreat不能になりやすい重要Commander

などです。

特に、ProtectionやHPは十分でもMRだけが穴になっているCarrierでは、一つのMisc slotで防御profileを整えられます。

---

# Misc slot競合が最大のコストになることがある

Amuletは安価でも、Misc slotは安くありません。

同じslotには、

- Path Booster
- Reinvigoration
- Regeneration
- Elemental Resistance
- Luck
- Mobility / Utility

などが競合します。

そのため本当のCostは、

```text
5S
+
Forge turn
+
Misc slot
+
外した別Itemの価値
```

です。

Carrierに元から十分なMRがあり、別の弱点が大きいなら、Amuletを足すほどBuild全体が強くなるとは限りません。

---

# Army-wide対策と個人Itemを分ける

敵のMR攻撃がArmy全体へ飛んでくる場合、重要Commander数人へAmuletを配るだけではArmy全体は守れません。

逆に、

- Commander snipe
- Anti-Thug Spell
- Rare Mage狙い

のように狙われる対象が少数なら、個人Itemが効率的です。

```text
少数の重要Carrierを守る
→ Item

Army全体を守る必要がある
→ Spell / bless / Army構成も検討
```

という役割分担で考えます。

---

# Forgeする条件

次が多いほど価値が上がります。

- Construction 5へ到達している
- S1へ簡単に届く
- 敵の主力CounterがMR依存
- 守りたいCommanderが少数で明確
- CarrierのMRがBuildの弱点
- Misc slotに余裕がある
- 5Sを払ってでもCarrier死亡Riskを下げたい

特に高価なCarrierほど、安い防御Itemへ払うGemの価値は上がります。

---

# Forgeしない・後回しにする条件

- 敵の主DamageがMRを使わない
- Carrierが既に十分高MR
- Elemental ResistanceやReinvigorationの方が急務
- Misc slotがBoosterで埋まっている
- Astral Gemを重要Ritual / Spellへ残したい
- 安価なCommanderへ過剰防御を積んでいる

「MR +4は強い」という一般論より、**そのCarrierが何で死ぬか**を優先します。

---

# Counter：敵がAmuletを積んだ場合

敵がMRを補ったら、同じMR attackをより強く押し続ける以外の選択肢があります。

- 物理Damageへ切り替える
- Elemental weaknessを突く
- Fatigueを攻める
- Poison / battlefield hazardを使う
- Commanderへ接近して通常攻撃で落とす
- Amuletのために空いたMisc slotの弱点を探す

つまりCounterは、**高くなったMRを正面突破するより防御軸をずらす**ことです。

---

# Thug / SCでは防御profile全体を見る

ThugへAmuletを付けるときは、次を一緒に確認します。

```text
Protection:
Defence:
MR:
Fire / Cold / Shock / Poison Resistance:
Reinvigoration:
Regeneration:
Magic Weapon対策:
Retreat route:
```

MRだけ高くしても、Fatigueで倒れる、Elemental Damageで焼かれる、通常兵に囲まれるならBuildは完成していません。

Amuletは**一つの穴を埋める部品**です。

---

# よくある失敗

## 敵を見ず全員へ配る

MR attackを使わないEnemyにはGemとslotを浪費します。

## Antimagicという名前からArmy-wide Spellを想像する

Item本体の実際の対象と挙動をゲーム内表示で確認します。

## 高MR Carrierへさらに積む

別の防御軸の方が限界効用が高い場合があります。

## Misc slot競合を忘れる

BoosterやReinvigorationを外した結果、別の弱点が生まれます。

## MRでElemental Damageまで防げると思う

攻撃ごとのMR check有無を確認します。

---

# Test game checklist

```text
[ ] C5・S1でAmulet of AntimagicがForge可能か確認
[ ] 実際の支払CostをForge画面で確認
[ ] 装備前後のMRを記録
[ ] MR +4が反映されることを確認
[ ] ゲーム内のAntimagic表示・説明を確認
[ ] MR Negates攻撃への実戦挙動を確認
[ ] MRを使わないDamageには別防御が必要なことを確認
[ ] Misc slot競合を実Buildで確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 369](../../data/items/by-id/369.md)
- [Resistance・Utility Item攻略](../resistance-items.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Thug / Supercombatant装備](../thug-equipment.md)
- [Magic Item総論](../index.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI
- Dominions 6 Main Manual — Magic Resistance / Magic Items
- `Antimagic` flagの細部はゲーム内Item表示とTest gameを優先
