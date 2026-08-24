---
title: "Amulet of Resilience"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 383
---

# Amulet of Resilience

**Reinvigoration +5をMisc Slotから与え、重装・Self-buff・高Fatigue Spell・長期戦でCarrierが動けるRoundを伸ばすConstruction 5 Item。**

Amulet of ResilienceはDamageもProtectionも直接増やしません。攻略上は、**すでに成立している行動をFatigueで失わないための専用Sustain Item**として評価します。

- [Dominions 6.35固定データ — Item 383](../../data/items/by-id/383.md)
- [Magic Item攻略辞典](index.md)
- [Girdle of Might](girdle-of-might.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

---

# まず何ができるか

6.35固定データでは、Amulet of ResilienceはConstruction 5、Forge要求**N2**のMiscellaneous Itemで、装備者へ**Reinvigoration +5**を与えます。

Item descriptionでは、九つのamber stonesが装備者をreinvigorateし、激しい作業の負担を大きく軽減すると説明されています。

このItemが行うのは、

```text
毎RoundのFatigue回復を増やす
```

ことです。

HPを回復するItemでも、Damageを増やすItemでも、MRを上げるItemでもありません。

---

# 「最終Fatigueが低い」より「有効行動が増えたか」

Reinvigorationは、戦闘終了時のFatigue値だけを見ても価値を測れません。

重要なのは、

- Fatigue 100へ到達するRoundが遅れたか
- Defense低下を避けられたか
- 意識を失う前に敵を倒せたか
- Self-buff後に近接戦へ入れたか
- 高Fatigue Spellを追加で一回唱えられたか
- 長期戦で命令通りに動き続けたか

です。

```text
Amuletなし: Buff後、Round 7で有効行動を失う
Amuletあり: Round 12まで攻撃・詠唱を継続
```

のように、**増えた有効Round**へ変換して評価します。

---

# Fatigue収支を見る

CarrierのFatigueは、

- Armor Encumbrance
- 通常行動
- Spell casting
- Self-buff
- Quickness等による行動増加
- Heat / Coldや特殊環境
- 敵のFatigue attack
- Reinvigoration

の収支で動きます。

Amulet of Resilienceは+5を足しますが、負荷がそれを大きく上回ればFatigueは増え続けます。

```text
毎Roundの負荷が小さい
→ +5でFatigueが安定または減少しやすい

毎Roundの負荷が非常に大きい
→ +5でも機能停止を少し遅らせるだけ
```

です。

「Reinvigoration +5があるから疲れない」と固定的に考えず、Battle Replayで収支を確認します。

---

# Girdle of Mightとの違い

[Girdle of Might](girdle-of-might.md)は、

- Strength +3
- Reinvigoration +3

を一つのMisc Slotへまとめます。

Amulet of ResilienceはStrengthを与えませんが、Reinvigorationは+5です。

```text
Girdle of Might
→ 近接Damageも欲しい
→ Fatigue対策は+3で足りる

Amulet of Resilience
→ Damageは別に確保済み
→ Fatigue対策を最大限優先したい
```

という使い分けになります。

純CasterではStrength部分を使わないため、Amuletがより任務へ直結することがあります。

一方、近接CarrierでStrength +3が必要Hit数を減らすなら、Girdleの総合価値が上回る場合があります。

---

# Boots of the Messengerとの違い

[Boots of the Messenger](boots-of-the-messenger.md)は、Reinvigoration +3とMap Move BonusをBoots Slotから与えます。

Amulet of ResilienceはMap Moveを与えません。

Carrierが、

- 戦略Mapで遠くへ動く必要がある
- Misc SlotをMR・Regenerationへ残したい

ならBoots of the Messengerを比較します。

Carrierが、

- 固定Frontや防衛地点で戦う
- Reinvigoration +3では不足する
- Boots SlotにQuicknessやBoosterが必要

ならAmuletが候補です。

Slotが違うため、極端なFatigue Buildでは両方を併用する余地もありますが、過剰装備になっていないかを確認します。

---

# Elemental Armor等の重装を支える

[Elemental Armor](elemental-armor.md)は複数属性ResistanceとProtectionをまとめますが、Encumbrance 4とDefense低下を伴います。

Amulet of Resilienceは、

```text
Armorで受Damageを減らす
＋
AmuletでArmor由来のFatigueを戻す
```

という役割分担を作ります。

同様に、重いArmor、Shield、複数Self-buffを組み合わせるBuildでは、+5が有効Roundを大きく伸ばすことがあります。

ただし重装CarrierがMR-based effectやBurst damageで即座に倒れるなら、Fatigue対策より別防御が先です。

---

# Combat Casterでの価値

Combat Casterは、

- 初手から高Fatigue Spellを唱える
- 複数のSelf-buffを積む
- Cast後に近接戦へ移る
- 長いBattleでSpellを繰り返す

ため、Fatigueが任務の上限になりやすい役割です。

Amulet of Resilienceにより、

- 予定したScriptを最後まで実行する
- Buff後に余力を残す
- Spell casting後のDefense低下を抑える
- 追加の有効詠唱を得る

可能性があります。

ただしSpellのPath requirement、Range、Precision、Penetrationは変わりません。

必要Spellを唱えられないMageへ持たせても、Fatigueだけ余ります。

---

# Thug・SCでの価値

近接Carrierでは、長期戦ほどAmuletの価値が積み上がります。

相性が良いのは、

- ProtectionやRegenerationで交換戦を続ける
- 多数のChaffへ囲まれる
- Self-buffを複数使う
- Quickness等で行動量が多い
- 敵を倒すまで時間が掛かる
- Fatigue 100が明確な敗因

Buildです。

逆に、数Roundで敵を倒す短期決戦や、接敵直後にBurst damageで倒されるBuildでは+5を活かす時間がありません。

---

# HP sustainとは別

[Ring of Regeneration](ring-of-regeneration.md)はHPを戻しますが、Fatigueを戻しません。

Amulet of ResilienceはFatigueを戻しますが、HPを戻しません。

```text
Ring of Regeneration
→ 傷を負いながら戦う時間を伸ばす

Amulet of Resilience
→ 疲労で動けなくなるまでの時間を伸ばす
```

という違いです。

長期戦Buildでは両方欲しくなることがありますが、Misc Slotを二つ使います。

MR・Resistance・Luck・Boosterを外しても成立するかを確認します。

---

# Misc Slotの機会費用

Amulet of Resilienceの最大のCostは、Misc Slotを一つ占有することです。

同じSlotには、

- Amulet of Antimagic
- Ring of Regeneration
- Girdle of Might
- Spell Focus
- Elemental Resistance Item
- Path Booster
- 特殊作戦Item

が入ります。

CarrierがFatigueで負けているならAmuletは強い回答です。

CarrierがMR-based Controlで負けているならAmulet of Antimagicが先です。

CarrierがDamage不足ならGirdleやWeaponが先です。

**敗因とItemの作用軸を一致させる**ことが重要です。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- N2 Forge Mageを確保できる
- Carrierの敗因がFatigueまたはFatigue 100
- Reinvigoration +3では不足する
- Strengthを増やす必要がない
- 長期戦または複数Self-buffを予定する
- Misc Slotを使ってもMR・Resistanceが足りる
- +5によって有効行動Roundが明確に増える
- Nature GemをSummon・Thistle Mace等から回せる

「Reinvigorationが高いから」ではなく、**Testで任務成功率が変わるCarrierへ**Forgeします。

---

# Forgeしない・別Itemを選ぶ条件

- 戦闘が短くFatigue差が出ない
- CarrierがFatigueより先にHPを失う
- MR-based Controlが主な敗因
- Strength +3も必要でGirdleの方が効率的
- Map Moveも必要でBoots of the Messengerが合う
- Misc Slotへ必須Boosterがある
- ReinvigorationなしでもFatigue収支が安定している
- Nature Gemを重要Summonや別Boosterへ回す必要がある

Fatigue問題が存在しないCarrierへ装備すると、Stats画面は良くても任務結果は変わりません。

---

# Counter：+5を上回る負荷か別軸を使う

敵のAmulet Carrierへ低密度の長期戦を挑むと、Reinvigorationの積み上げを活かされます。

Counterは、

- Fatigue damageを集中し、+5を上回る負荷を掛ける
- 高Encumbrance環境や長いSpell exchangeへ引き込む
- Burst damageで回復が積み上がる前に倒す
- MR-based Controlで行動そのものを止める
- Poisonや継続DamageでHP側を攻める
- 高DefenseやChaffで有効攻撃を減らす
- Carrierを避け、Army・Mage・Provinceを狙う
- Misc SlotからMRやRegenerationが外れている点を突く

のように、**Fatigue以外の不足またはReinvigorationを超える負荷**へ切り替えます。

---

# よくある失敗

## +5ならFatigueが増えないと思う

毎Roundの負荷が+5を上回れば、Fatigueは増え続けます。

## 戦闘終了時のFatigueだけを見る

重要なのは、途中で何Round有効に動けたかです。

## HP sustainと混同する

傷は回復しません。Burst damageへの耐性も直接増えません。

## Girdleより常に上位だと思う

近接CarrierではStrength +3を含むGirdleの方が任務へ合う場合があります。

## Misc SlotからMRを外す

Fatigueに強くなっても、MR-based effectで即座に止められることがあります。

---

# Test game checklist

```text
[ ] C5・N2でAmulet of ResilienceがForge可能か確認
[ ] Item 383であることを確認
[ ] Reinvigoration +5がUnit画面へ反映されることを確認
[ ] Amuletなし／ありでRoundごとのFatigueを記録
[ ] Fatigue 100へ達するRoundを比較
[ ] Self-buff後に有効行動できるRoundを比較
[ ] 高Fatigue Spellの有効詠唱回数を比較
[ ] Girdle of Mightとの任務成功率を比較
[ ] Boots of the MessengerとのSlot・移動差を比較
[ ] Elemental Armor等の重装併用時を比較
[ ] Ring of Regeneration併用時にMR・Resistance不足がないか確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 383](../../data/items/by-id/383.md)
- [Girdle of Might](girdle-of-might.md)
- [Boots of the Messenger](boots-of-the-messenger.md)
- [Elemental Armor](elemental-armor.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- BaseI: C5 / N2 / Reinvigoration +5
- 実際のFatigue収支、Spell詠唱回数、Armorとの相互作用はゲーム内Unit画面とBattle Replayを優先
