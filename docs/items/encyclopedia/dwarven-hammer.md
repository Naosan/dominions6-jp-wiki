---
title: "Dwarven Hammer"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 29
---

# Dwarven Hammer

**Forge Bonusを安全な鍛造Mageへ持たせ、繰り返すForgeの総Gem支出を下げるConstruction 3の経済Item。**

Dwarven Hammerは「強い武器を一人へ渡す」ためのItemというより、**これから作る複数のMagic Itemを安くするための生産設備**として評価します。

- [Dominions 6.35固定データ — Item 29](../../data/items/by-id/29.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)
- [Magic Item総論](../index.md)

---

# まず何ができるか

6.35固定データでは、Dwarven HammerはConstruction 3の片手武器で、Forge要求は**E3**、基礎Costは**15E**、Forge Bonusは**+2**です。

重要なのは、Hammer自身へ払ったGemを、その後のForgeで少しずつ回収する構造です。

```text
E3 Mage
→ Dwarven HammerをForge
→ Hammerを装備して次のItemをForge
→ Forge Bonusで支払Costを圧縮
→ さらに別のItemをForge
```

一個だけItemを作るなら、Hammerの先行投資がそのまま重くなります。多数のItemを作るほど価値が出ます。

---

# 「15EのItem」ではなくForge pipelineとして見る

Dwarven Hammerの損得は、Hammer単体のStatsではなく**今後の生産予定**で決まります。

考えるべきなのは、

- この後何個Forgeするか
- 高Cost Itemを何個作るか
- Earth Gemを今使ってよいか
- Forge担当Mageを何Turn拘束するか
- Hammerを何人の鍛造者で使い回せるか

です。

Forge Bonusの価値は、

```text
先行投資
vs
一個あたりの節約 × 今後のForge回数
```

で考えます。

実際の支払額は丸め、国家能力、別のForge Bonus、Item固有Costなどで変わるため、**ゲーム内Forge画面を最終確認**します。

---

# 早く作るほど回収期間が長い

同じHammerでも、ゲーム終了直前より、まだ多数のForge turnが残る時期の方が経済価値は高くなります。

Construction 3へ早めに到達し、

- Research Item
- Booster
- Resistance Item
- Thug装備
- 後の高級Item

を継続生産する計画があるなら、Hammerは国家のForge economyへ早く効き始めます。

逆に「今から一戦だけのCounter Itemを一個作る」場面では、Hammerを挟む一Turnが戦争Timingを遅らせることがあります。

---

# 誰に持たせるか

基本は**安全な後方Forge Mage**です。

Dwarven Hammerは片手Slotを使いますが、Forge専任なら戦闘装備との競合は小さくなります。

理想的な運用は、

- Fort / Lab内に置く
- 必要なMageへだけ渡す
- Forge後に別のMageへ回す
- F8で所在を確認する

です。

Hammerを持つためだけにRare Mageを前線へ出す必要はありません。

---

# Hammerを「貸す」発想

Dwarven Hammerの価値はCarrierへ固定されません。

一つのHammerを、

```text
Turn A: E MageがForge
→ Treasury / handoff
Turn B: S MageがForge
→ handoff
Turn C: N MageがForge
```

のように、生産予定に合わせて回せます。

このため、Hammerの数を増やす前に、**同じTurnに何人が同時Forgeするのか**を確認します。

Hammerを三本持っていても、一人しかForgeしないなら二本は寝ています。

---

# Forgeする条件

次が多いほど優先度が上がります。

- E3へ無理なく届く
- Construction 3を早期に通る
- 今後多数のItemをForgeする
- 高Cost Itemや複合Path Itemを予定している
- Earth Gemに余裕がある
- Forge担当Mageを確保できる
- Hammerを安全に使い回せる

特に「次の10 Turnで何をForgeするか」が書けるなら判断しやすくなります。

---

# Forgeしない・後回しにする条件

- 今後のForge予定が少ない
- Earth GemをBattle magic / Ritualへ回す必要がある
- E3へ届くための追加投資が重い
- Rare E3 Mageの一Turnが非常に高価
- Counter Itemを今Turn作らないと戦争に間に合わない
- ゲーム終了までの残りTurnが少ない

**割引Itemだから必ず得**ではありません。

Hammerを作る一Turnそのものも、Research・Ritual・別Item Forgeを失う機会費用です。

---

# Researchとの競合

序盤のForge経済にはメタな問題があります。

```text
Hammerを早く作る
→ 将来のForgeは安くなる
→ しかしMageのResearch 1 Turnを失う
```

Constructionをさらに伸ばしたい時期ほど、この一TurnがBreakpoint到達を遅らせます。

そのため、HammerはGemだけでなく**Mage turnを投資する経済Item**です。

---

# Counter：敵のForge economyを攻める

敵がHammerを使っている場合、Hammer一個を正面からCounterする必要はありません。

価値は安全なForge pipelineから発生するので、

- Forge hubをRaidする
- Rare Forge MageをAssassinationで狙う
- Gem Siteを奪う
- 戦争を早めてForge turnをBattleへ引き出す
- Booster / Hammerの所在管理を難しくする

ことで、割引を利用できるTurnそのものを減らせます。

経済ItemへのCounterは、Item性能ではなく**生産環境を壊すこと**です。

---

# よくある失敗

## 一個安く作るためにHammerを先に作る

Hammer本体のGemとForge turnまで含めると、総投資が増えます。

## Hammerを装備したMageを前線へ出す

Forge infrastructureを戦闘Riskへ晒しています。

## Hammerを必要数以上に量産する

同時Forge人数より多いHammerは遊休資産になりやすくなります。

## 基礎Cost表だけで節約額を決める

実支払額はForge Bonus、国家割引、丸め等で変わります。

## Earth Gemの別用途を無視する

Gem節約のために作ったHammerが、直近のEarth spellや重要Summonを遅らせることがあります。

---

# Test game checklist

```text
[ ] C3・E3でDwarven HammerがForge可能か確認
[ ] Hammerなしの対象Item支払Costを記録
[ ] Hammer装備後の支払Costを記録
[ ] Forge Bonus +2表示を確認
[ ] 複合Path Itemの各Gem支払を確認
[ ] 国家Forge Bonus等との併用時のCostを確認
[ ] 片手Slotを占有することを確認
[ ] Hammerを別Mageへ受け渡してForgeできることを確認
[ ] F8で所在を追跡できることを確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 29](../../data/items/by-id/29.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)
- [Magic Path Booster](../boosters.md)
- [Research Item](../research-items.md)
- [Gem](../../magic/gems.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- Dominions 6 Main Manual — Forge Item / Forge Bonus
- 実際の支払Costはゲーム内Forge画面を優先
