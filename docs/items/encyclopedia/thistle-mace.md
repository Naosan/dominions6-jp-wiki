---
title: "Thistle Mace"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 65
---

# Thistle Mace

**Nature MageのPathを+1し、Nature magicの重要な閾値を越えつつ、片手Slotで比較的組み込みやすいConstruction 5 Booster。**

Thistle Maceは武器でもありますが、攻略上の主役は**Nature accessを一段引き上げること**です。攻撃性能ではなく「装備前後で何がCast可能になるか」から評価します。

- [Dominions 6.35固定データ — Item 65](../../data/items/by-id/65.md)
- [Magic Path Booster](../boosters.md)
- [Magic Item総論](../index.md)

---

# まず何ができるか

6.35固定データでは、Thistle MaceはConstruction 5、Forge要求**N2**の片手武器で、装備者の**Natureを+1**します。

典型形は、

```text
N2 Mage
→ Thistle Maceを装備
→ N3としてNature magicを使う
```

です。

Item descriptionでは、武器で傷つけた相手へ毒を与える性質も確認できます。ただしCaster運用では、Maceを振ることより**N+1で新しい役割を解禁すること**の方が重要です。

---

# 価値は「N+1」ではなく新しく届く仕事

NatureはBattlefield buff、回復・耐久補助、Summon、Ritualなど複数の用途へPath requirementが伸びます。

そのためThistle Maceは、

1. 素のNature Pathを確認
2. 装備後のPathを確認
3. 今のResearchで新しく使えるSpellを洗う
4. 必要GemとFatigueを確認
5. 戦争・経済のどちらへ使うか決める

という順で評価します。

```text
N2 → N3
```

という表示変化そのものではなく、**N3になった結果、戦術またはRitual計画のどこが変わるか**がForge理由です。

---

# N2からN3へ上げる橋

Thistle MaceはN2でForgeできるため、native N2 Mageを一段上のNature運用へ移しやすいBoosterです。

一方で、native N1しかいない国家がMaceだけでN2 Forge requirementを自己解決することはできません。

最初の一本を作るには、

- native N2
- RandomでN2へ届くMage
- Pretender / Hero / Summonなど別のN2 source

が必要です。

Booster routeを考えるときは、**完成した後の最高Pathより、最初のForge担当を先に確定**します。

---

# 片手であることが大きい

Skull Staffのような両手Boosterと比べ、Thistle Maceは**1-h weapon**です。

そのため、手Slotを持つCommanderなら、もう一方へShieldや別の片手Itemを残せることがあります。

これは前線CasterやThug寄りMageで特に重要です。

ただし「片手だから無料」ではありません。

- 攻撃用Weapon
- 別の片手Booster
- Shieldとの組み合わせ
- Dancing / utility系の手Slot

との競合は残ります。

**Path +1で得るものと、片手Slotを埋めることで失うもの**を一緒に見ます。

---

# 前線Casterへ持たせる

Battle spellの閾値を越える用途では、Research timingと戦争Timingを一致させます。

良いForge理由は、

> 「次の主力戦で、N2では使えない役割をN3として担当させる」

と具体化できます。

このとき必要なのはMaceだけではありません。

- 対象SpellのResearch
- Gemを使うなら戦場へのGem輸送
- Fatigue対策
- Casterを守る配置
- Scriptの再確認

まで揃って初めて戦力になります。

---

# 後方Ritualistへ持たせる

Thistle MaceはLab内で使う場合も価値があります。

Ritual / SummonのPath requirementを越えるだけなら、戦闘装備との競合は軽くなり、必要Turnだけ装備して別Mageへ回せます。

```text
Turn A: Mage 1がMaceでRitual
→ handoff
Turn B: Mage 2がMaceでRitual
```

のように、**国家共有のPath access**として使えます。

一人へ常設する前に、同じMaceを何人で使い回せるか確認します。

---

# Booster chainへ組み込む

Thistle Maceで越えたPathが、さらに高いSummonや別のBooster、Ritualへの入口になることがあります。

ただしchainは、

- Construction Research
- Nature Gem
- Forge turn
- Carrier
- Slot
- 次段階のResearch

を要求します。

「最終的に高Pathへ行ける」だけではなく、**何を解禁するために、どの順序で投資するか**を書きます。

---

# Forgeする条件

次が多いほど優先度が上がります。

- N2 Forge Mageを確保済み
- Construction 5へ到達済み
- +1で具体的なSpell / Ritual / Summonが解禁される
- そのResearchが現在の戦略に合う
- Nature Gemを他用途と両立できる
- 一つのMaceを複数Mageで共有できる
- 前線Casterでも片手Slot構成が成立する

特に「このMaceがないと誰も担当できない仕事」がある場合、価値は高くなります。

---

# Forgeしない・後回しにする条件

- +1しても使いたいSpellが増えない
- Researchがまだ遠い
- Nature GemをSummon / Ritual / Battleへ直接回したい
- N2 Forge MageのTurnが不足している
- すでに高Nature Mageが十分いる
- 手Slotが別の生存装備に必要

Boosterを作ること自体が目的にならないよう、**解禁先のないPath +1は保留**します。

---

# Counter：敵のNature閾値を読む

敵のThistle Maceを見たら、Carrierの素Natureと装備後Pathを比較します。

見るべきなのは、

- Maceがないと届かないSpellが何か
- そのSpellが今のResearch帯で現実的か
- Battle Mageか後方Ritualistか
- Maceを複数Mageで回しているか

です。

CounterはMace自体を殴るより、

- Booster依存Casterを狙う
- Gem carrierを落とす
- Nature battlefield planと異なるDamage / Control軸を当てる
- Ritual拠点やItem輸送をRaidする

など、**+1で成立した役割を崩す**方向へ向けます。

---

# よくある失敗

## 毒武器としてだけ評価する

Thistle Maceの主な戦略価値はNature +1です。Casterが接近戦を始める前提でBuildすると、本来の役割から外れることがあります。

## +1後のSpellを確認していない

Pathは上がっても、Research上の役割が変わらなければ投資回収が遅れます。

## N1国家がすぐ作れると思う

Forge requirementはN2です。最初のN2 sourceを別に用意する必要があります。

## 片手Slotの競合を無視する

Shieldや別の重要Itemを外す必要があるCarrierでは、Path +1の代償が大きくなります。

## 共有できるMaceを量産する

後方Ritual中心なら、一つを順番に使う方が効率的な場合があります。

---

# Test game checklist

```text
[ ] C5・N2でThistle MaceがForge可能か確認
[ ] Item 65であることを確認
[ ] 装備前後でNatureが+1されることを確認
[ ] 1-h weaponとして片手Slotを使うことを確認
[ ] N2 Mageが装備後N3として目的Spellを選べるか確認
[ ] 装備前後でBattle script候補を比較
[ ] Ritual / SummonのPath requirementを越えられるか確認
[ ] Maceを別Mageへ受け渡して共有できるか確認
[ ] 武器で傷つけた相手への毒効果を実戦で確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 65](../../data/items/by-id/65.md)
- [Magic Path Booster](../boosters.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- Dominions 6 Main Manual — Forge Item / Magic Path
- Spell requirement、毒の実挙動、script可否はゲーム内表示とTest gameを最終確認
