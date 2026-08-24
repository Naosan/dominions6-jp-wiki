---
title: "Water Bracelet"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 403
---

# Water Bracelet

**Water MageのWater Pathを+1する、Construction 7・W1 ForgeのMisc Booster。低いForge Pathで作れるが、Research到達は遅い。**

Water Braceletは、Forge要求だけを見ると作りやすく見えます。

しかし攻略上は、

```text
Forge要求 W1
＋
Construction 7解禁
＋
Misc Slot使用
```

を一体として評価するItemです。

- [Dominions 6.35固定データ — Item 403](../../data/items/by-id/403.md)
- [Magic Item攻略辞典](index.md)
- [Magic Path Booster](../boosters.md)
- [Bottle of Living Water](bottle-of-living-water.md)

---

# まず何ができるか

6.35固定データでは、Water Braceletは、

- Construction 7
- Forge要求 **W1**
- Miscellaneous Slot
- **Water +1**

を持ちます。

Item descriptionでは、水で作られたBraceletであり、Water magicの詠唱を楽にすると説明されています。

固定データ上、ReinvigorationやFatigue回復を独立したItem効果として持つわけではありません。

詠唱が楽になるという説明は、まず**Water Pathが上がることでSpell使用条件やFatigueが変わる**Itemとして読みます。

---

# Water +1は「何が新しくできるか」で測る

Water Braceletの価値は、Water表示が1増えたこと自体ではありません。

装備前後で、

- 新しく選べるBattle spell
- 新しく実行できるRitual
- 新しくForgeできるItem
- 同じSpellを高PathでCastした場合のFatigue
- Water summonへの到達
- Underwater戦略へ接続する役割
- 次のBooster chain

がどう変わるかを確認します。

```text
W1 Mage
→ Water Bracelet
→ W2として新しい仕事へ到達
```

のように、低Water Mageへ新しい役割を与えられる場合があります。

一方、W+1しても現在のResearchで何も増えないなら、Braceletは在庫になっています。

---

# W1でForgeできることの意味

Water Braceletの特徴は、Forge要求がW1であることです。

最初の一個に高Water Mageを要求するBoosterと違い、Construction 7へ到達さえすれば、比較的広いWater Mage層がForge候補になります。

```text
native W1
→ Water BraceletをForge
→ W2運用
```

という橋を作りやすいItemです。

ただし、ここで見落としやすいのがConstruction 7です。

W1 Forgerが序盤からいても、ResearchがC7へ届くまでBraceletは作れません。

```text
Path条件は軽い
≠
早期Item
```

です。

---

# Construction 7 Timingを評価する

Water BraceletはC7解禁なので、完成時にはゲームが中盤以降へ進んでいることが多くなります。

そのため投資判断では、

- C7へ寄るResearch routeが国家計画に合うか
- 完成後に何Turn使えるか
- 直近の戦争へ間に合うか
- すでに高Water Summon Mageを得ていないか
- 他のBoosterで代替済みではないか
- C7 Item全体の中で優先度があるか

を確認します。

早く作れる安いBoosterではなく、

> **C7到達後に低Water Mageをまとめて実用化できるItem**

として見る方が正確です。

---

# Battle Mageへ持たせる場合

前線Casterへ装備すると、

- Water spellの必要Pathを越える
- 高Path CastでFatigueを抑える
- Battle summonの規模・選択肢を変える
- Cold系・Water系のBattle planへ参加する

可能性があります。

確認する項目は、

- 目的Spellの必要Water
- 現在のResearch
- 必要Gem
- Bracelet装備後のFatigue
- Misc Slotを使ってもMR・Resistanceが足りるか
- Carrierが戦場へ間に合うか
- Underwater / Landのどちらで使うか

です。

Water +1だけで生存性、Precision、Range、MRが自動的に解決するわけではありません。

---

# 後方Ritual・Forge用では共有しやすい

Water BraceletはMisc Itemなので、Lab内で必要Turnだけ装備できます。

典型的には、

- Water Ritualを行うTurnだけ装備
- 高Water ItemをForgeするTurnだけ装備
- 使用後にLabへ戻す
- 別のW1 / W2 Mageへ渡す

という共有運用です。

```text
Water Bracelet一個
→ 複数のWater Mageが必要Turnだけ使用
```

できます。

後方運用ではMisc Slotの戦闘上の機会費用が小さく、Carrier死亡Riskも下げられます。

ただし別Fortへ置き忘れると必要Turnに使えないため、Item移送を先に計画します。

---

# Misc Slotの機会費用

Water BraceletはMisc Slotを一つ使います。

このSlotには、

- Amulet of Antimagic
- Ring of Regeneration
- Amulet of Resilience
- Girdle of Might
- Spell Focus
- Eye of the Void
- Coin of Meteoritic Iron
- Elemental Resistance Item

などが入ります。

前線Casterでは、

```text
Water +1で得る新しいSpell
vs
MR・Fatigue・Resistance・Penetrationを失うCost
```

を比較します。

後方RitualistならSlot競合は軽く、Combat Casterでは重くなります。

---

# Reinvigoration Itemではない

Item descriptionはWater magicの詠唱をless arduousにすると説明しています。

しかしWater Bracelet自体に、Amulet of ResilienceのようなReinvigoration値はありません。

したがって、

```text
Water Bracelet
→ Water +1
→ 目的SpellのPath余裕・Fatigueが変わる可能性
```

であって、

```text
Water Bracelet
→ 毎RoundFatigueを直接回復
```

ではありません。

Water以外のSpellや、Armor由来のFatigueまで一律に軽くすると考えないようにします。

実際のFatigueはSpellごとにBattle Replayで比較します。

---

# Bottle of Living Waterとの違い

[Bottle of Living Water](bottle-of-living-water.md)もConstruction 7のWater系Misc Itemですが、役割は別です。

```text
Water Bracelet
→ CarrierのWater Path +1
→ Caster本人の仕事を増やす

Bottle of Living Water
→ BattleへWater Elementalを追加
→ 別Unitを一体増やす
```

という違いです。

目的が、

- 高Water Spell・Ritual・ForgeならBracelet
- Battle summonの追加BodyならBottle

です。

同じW Gem、C7、Misc Slotを使うため、Carrierと戦争計画に合わせて選びます。

---

# 他のWater Boosterとの組み合わせ

Waterは複数SlotのBoosterを組み合わせられる場合があります。

考え方は、

```text
素のWater
→ Water Bracelet
→ 別Water Booster
→ Ritual / Global / Forgeの最終閾値
```

です。

ただしBoosterを増やすほど、

- Research
- Gem
- Forge turn
- Slot
- Carrier
- Item移送

を要求します。

理論上の最高Pathではなく、

> **何Turn目に、誰が、何のためにそのWaterへ届くか**

で評価します。

一戦だけのBattle spellなら、別Caster、Gem boost、Communion等の代替も比較します。

---

# Carrierを選ぶ

優先したいCarrierは、

- 素でWater magicを持つ
- +1で具体的なSpell・Ritual・Forgeが解禁される
- 目的Researchへ到達済み
- 必要Gemを受け取れる
- Misc Slotを他の必須Itemへ使わない
- 前線なら生存・移動・配置を確保できる
- Underwater / Landの活動範囲が任務と一致する

Mageです。

すでにBraceletなしで必要な仕事を行える高Water Mageへ常設するより、W1→W2、W2→W3で役割が増える安いMageへ渡す方が効率的な場合があります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 7へ到達済み、またはC7 routeが計画に合う
- W1 Forgerがいる
- W+1で具体的な仕事が増える
- 完成後に十分な使用Turnがある
- Water Gemを確保できる
- 前線用か後方共有用か決めている
- Misc Slot競合を解決済み
- 目的Spell・Ritual・Forgeが現在のResearchで利用可能
- Item移送を管理できる

C7へ到達したから作るのではなく、

> **Bracelet完成後の最初の仕事**

を決めてからForgeします。

---

# Forgeしない・後回しにする条件

- C7 routeが国家の必要Researchから外れる
- W+1しても仕事が増えない
- 高Water Mageがすでに必要数いる
- 完成時期が戦争へ間に合わない
- Misc SlotへMR・Resistance・Fatigue Itemが必須
- Water GemをBattle summonやRitualへ使いたい
- 別Water Boosterで同じ閾値へ届く
- 一戦だけなら別CasterやGem boostで代替できる
- Itemを移送するTurnがない

Forge要求W1の軽さだけで量産しないことが重要です。

---

# Counter：Bracelet込みのWater閾値を読む

敵のWater Braceletを見たら、Carrierの素Waterと装備後Waterを確認します。

見るべきなのは、

- どのSpell閾値を越えたか
- Battle summonが変わったか
- Cold・Water系Battle planの中心か
- Ritual・Globalの準備か
- 必要Gemを誰が運んでいるか
- Braceletを失うとScriptが崩れるか

です。

Counterは、

- Cold Resistance等、目的Spellに合う防御を用意する
- CarrierをAssassination・Raid・Missileで狙う
- Gem carrierを落とす
- Misc SlotをBraceletで使っているため、MR・Fatigue・Resistance不足を突く
- 高Water Spellが揃う前に戦争Timingを早める
- Lab・Fortを攻め、Braceletの共有運用を乱す
- Underwater / Landの移動境界を利用する

ように、**Water +1で成立した役割**へ向けます。

---

# よくある失敗

## W1で作れるから早期Itemだと思う

解禁はConstruction 7です。

## Reinvigoration Itemだと思う

Water +1は与えますが、独立したReinvigoration値はありません。

## Waterを持たないCommanderへ新Pathを与える前提にする

装備前後のPath表示とSpell選択をゲーム内で確認します。

## C7到達時に目的を決めていない

使うSpell・Ritual・Forgeがなければ在庫になります。

## 前線CasterのMisc Slot競合を忘れる

MR・Resistance・Fatigue・Penetrationを外すCostがあります。

## Bottle of Living Waterと同じ用途だと思う

BraceletはPath Booster、BottleはBattle summonです。

## 高Water Mageへ常設する

後方Ritual・Forgeなら一個を共有できる場合があります。

---

# Test game checklist

```text
[ ] C7・W1でWater BraceletがForge可能か確認
[ ] Item 403であることを確認
[ ] 装備前後でWater +1を確認
[ ] Waterを持たないCommanderでPath表示がどうなるか確認
[ ] 独立したReinvigoration値が付かないことを確認
[ ] Braceletなし／ありで目的Spellの選択可否を比較
[ ] 同じWater SpellのFatigueを装備前後で比較
[ ] Ritual・Forge requirementを越えられるか確認
[ ] Bottle of Living WaterとのMisc Slot競合を確認
[ ] MR・Fatigue・Resistance Itemを外したBuildと比較
[ ] 後方Labで別Mageへ共有できるか確認
[ ] Underwater / Landの予定RouteでCarrierが移動できるか確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 403](../../data/items/by-id/403.md)
- [Magic Path Booster](../boosters.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)
- [Bottle of Living Water](bottle-of-living-water.md)
- [Amulet of the Fish](amulet-of-the-fish.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- BaseIで確認した主要field：C7、W1、Miscellaneous、Water +1
- 独立したReinvigoration fieldは確認できない
- Spell Fatigue、Pathless Carrier、Underwater / Landでの最終挙動はゲーム内表示・Battle Replayを優先
