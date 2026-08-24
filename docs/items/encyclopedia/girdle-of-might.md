---
title: "Girdle of Might"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 366
---

# Girdle of Might

**Strength +3とReinvigoration +3を一つのMisc Slotへまとめ、近接DamageとFatigue耐性を同時に底上げするConstruction 5 Item。**

Girdle of Mightは派手な特殊効果を持つItemではありません。攻略上は、**Carrierが殴る力と、殴り続ける時間を同時に伸ばす基礎装備**として評価します。

- [Dominions 6.35固定データ — Item 366](../../data/items/by-id/366.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Thug・SC装備](../thug-equipment.md)
- [Magic Item総論](../index.md)

---

# まず何ができるか

6.35固定データでは、Girdle of MightはConstruction 5、Forge要求**E1**のMiscellaneous Itemで、装備者へ、

- **Strength +3**
- **Reinvigoration +3**

を与えます。

Item descriptionも、装備者を強化し、激しい作業による負担を軽くすると説明しています。

この二つは別々の効果ですが、近接Carrierでは同じ目的へ繋がります。

```text
Strengthで一撃の価値を上げる
＋
Reinvigorationで有効に動けるRoundを伸ばす
```

という構造です。

---

# Strength +3は「表示Damage」だけではない

Strengthは主にStrengthを加算する近接武器のDamageへ関わります。

そのため価値は、

- Carrierの基礎Strength
- 使用武器がStrengthをどれだけ利用するか
- 一Roundの攻撃回数
- 敵Protection
- Armor Piercing / Armor Negating等のDamage処理

で変わります。

高いStrengthを持つCarrierへ足す場合も、低Strengthを補う場合もあり得ますが、**実際に倒したい敵への必要Hit数が変わるか**を確認します。

表示Damageが3増えても、敵を倒すHit数が同じなら戦術上の差は小さいことがあります。

---

# Reinvigoration +3は「もう一Round動けるか」で見る

Reinvigorationの価値は、戦闘終了時のFatigue値だけではありません。

重要なのは、

- Fatigue 100へ到達するRoundが遅れるか
- Defence低下や行動停止を避けられるか
- Self-buff後に近接戦へ移れるか
- 長期戦で攻撃回数を維持できるか
- Quickness等の行動増加を支えられるか

です。

```text
Girdleなし: Round 8で機能停止
Girdleあり: Round 11まで有効行動
```

のように、追加された有効Roundを測ると価値が分かりやすくなります。

---

# Thugでは攻撃とSustainを一枠で補う

Thug装備では、Misc SlotへDamageだけを置くとFatigueが残り、Reinvigorationだけを置くと敵を倒す速度が不足することがあります。

Girdle of Mightは、

```text
Weapon / procでDamage sourceを確保
＋ GirdleでStrengthとReinvigoration
＋ Armor / Shield / Ringで生存
```

というように、二つの不足を一枠で薄く補えます。

ただし一つのItemで完全解決するほどの値とは限りません。

高Encumbrance Armor、複数のSelf-buff、Quickness、長期戦が重なるなら、Reinvigoration +3だけでは不足することがあります。

---

# Combat Casterでも候補になる

Girdleは近接専用ではありません。

Battle mageが、

- 複数のSelf-buffを使う
- 高Fatigue spellを繰り返す
- Cast後に近接戦へ入る
- Fatigueによる事故を減らしたい

場合、Reinvigoration +3が役立つことがあります。

ただし純粋な後方CasterではStrength +3をほぼ利用しません。

その場合は、同じMisc SlotへPenetration、MR、Resistance、Booster等を置く方が任務へ直結することがあります。

---

# Ring of Regenerationとの役割分担

[Ring of Regeneration](ring-of-regeneration.md)はHP損耗を戻しますが、Fatigueは戻しません。

Girdle of MightはFatigueを軽減しますが、失ったHPは戻しません。

したがって長期戦Buildでは、

```text
Ring: HP sustain
Girdle: Fatigue sustain + Strength
```

として役割を分けられます。

両方を装備する価値があるかは、Misc Slotを二つ使ってもMR・Resistance等が足りるかで決まります。

---

# Boots of Quicknessを支える

[Boots of Quickness](boots-of-quickness.md)は攻撃と移動を大きく速めますが、行動量が増えるほどFatigue管理も重要になります。

Girdleは、

- 攻撃一回あたりのDamageを上げる
- 増えた行動をReinvigorationで支える

ため、Quickness Carrierの候補装備になります。

ただしQuicknessの負担を必ず相殺できるとは限りません。Battle ReplayでRoundごとのFatigue推移を確認します。

---

# Misc Slotの機会費用

Girdle of MightはMisc Slotを使います。

このSlotには、

- Amulet of Antimagic
- Ring of Regeneration
- Elemental Resistance
- Luck
- Path Booster
- 特殊作戦Item

も入ります。

CarrierがMR-based effectで落ちるなら、StrengthやReinvigorationよりMRが優先です。

Girdleは**敗因がDamage不足またはFatigueである時**に強いItemです。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- E1 Forge Mageを確保できる
- Strengthを利用する近接Carrierがいる
- 長期戦またはSelf-buffでFatigueが問題になる
- Strength +3で必要Hit数が減る
- Reinvigoration +3で有効行動Roundが増える
- Misc Slotを使ってもMR・Resistanceが足りる
- Earth Gemを他の重要Forge / Battle magicから回せる

E1でForgeできるためAccessは比較的軽いですが、**作りやすさと必要性は別**です。

---

# Forgeしない・別Itemを選ぶ条件

- 純粋な後方CasterでStrengthを使わない
- 戦闘が短くReinvigorationの差が出ない
- CarrierがFatigueより先に倒される
- MR / Resistance不足が主な敗因
- 武器がStrengthを活かしにくい
- Misc Slotへ必須Boosterがある
- Earth GemをArmorや重要Boosterへ使う必要がある

Girdleは平均点を上げるItemですが、**明確なCounter Itemの代わりにはなりません**。

---

# Counter：長期戦の前提を壊す

敵のGirdle Carrierは、近接DamageとFatigue耐性が少しずつ高くなっています。

Counterは、

- 接敵前にMissile / Battle magicで削る
- Burst damageで長期戦にさせない
- MR-based Controlで行動そのものを止める
- Fatigue damageを集中し、+3を上回る負荷を掛ける
- 高DefenseやChaffで有効Hit数を減らす
- Carrierを迂回してMage・Army・Provinceを狙う

のように、**StrengthとReinvigorationが積み上がる交換戦を避ける**方向で考えます。

---

# よくある失敗

## E1で作れるから量産する

簡単にForgeできても、Carrierと任務がなければMisc Slotを埋めるだけです。

## Reinvigoration +3でFatigue問題が消えたと思う

Armor、Self-buff、Quickness、戦闘時間によっては不足します。

## Strength +3だけを見て採用する

実際に必要Hit数が変わらない相手では価値が小さいことがあります。

## MRやResistanceを外す

平均性能を上げる代わりに致命的Counterへ弱くなる場合があります。

## 純Casterへ惰性で装備する

Strength部分を使わず、より任務に直結するMisc Itemを失っています。

---

# Test game checklist

```text
[ ] C5・E1でGirdle of MightがForge可能か確認
[ ] Item 366であることを確認
[ ] Strength +3がUnit画面へ反映されることを確認
[ ] Reinvigoration +3がUnit画面へ反映されることを確認
[ ] Girdleなし／ありで敵を倒すHit数を比較
[ ] RoundごとのFatigue推移を記録
[ ] Self-buff後に有効行動できるRound数を比較
[ ] Boots of Quickness併用時のFatigueを確認
[ ] Ring of Regenerationとの併用Buildを比較
[ ] MR / Resistance ItemとのSlot競合を比較
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 366](../../data/items/by-id/366.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Boots of Quickness](boots-of-quickness.md)
- [Frost Brand](frost-brand.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Thug・SC装備](../thug-equipment.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- Dominions 6 Main Manual — Strength / Fatigue / Reinvigoration / Forge Item
- 実際のDamage・Fatigue推移・最終Statsはゲーム内Unit画面とBattle Replayを優先
