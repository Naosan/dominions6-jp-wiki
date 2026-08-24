---
title: "Skull Staff"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 62
---

# Skull Staff

**Death MageのPathを+1し、届かなかったDeath spell / Ritual / Summonの閾値を越えるためのConstruction 5 Booster。**

Skull Staffは戦闘武器として見るより、**Mage一人の「使える魔法の集合」を一段上へずらすItem**として評価します。

- [Dominions 6.35固定データ — Item 62](../../data/items/by-id/62.md)
- [Magic Path Booster](../boosters.md)
- [Magic Item総論](../index.md)

---

# まず何ができるか

6.35固定データでは、Skull StaffはConstruction 5、Forge要求**D2**の両手武器で、装備者の**Deathを+1**します。

つまり典型的には、

```text
D2 Mage
→ Skull Staffを装備
→ D3としてDeath magicを使う
```

という閾値越えに使います。

重要なのは「Deathが1増える」こと自体ではありません。**その+1で新しく何をCastできるようになるか**です。

---

# BoosterはStats Itemではなく「解禁Item」

Path Boosterの価値は、装備前後で使えるSpellが変わるときに最大化します。

確認する順番は、

1. そのMageの素のDeath
2. Skull Staff装備後のDeath
3. そのPathで新たに届くBattle spell / Ritual / Summon
4. それを今のResearchで使えるか
5. 必要Gemを継続供給できるか

です。

```text
Path +1
→ Spell requirementを越える
→ 新しい役割が生える
→ 戦争計画またはGem economyが変わる
```

「D2がD3になったが、今のResearchでは何も新しく使わない」なら、その時点ではStaffが寝ています。

---

# どのMageへ持たせるか

優先したいのは、**+1によって明確な仕事が増えるMage**です。

たとえば、

- Battle spellの必要Pathへあと1足りない
- Ritual / Summonの必要Pathへあと1足りない
- さらに別Boosterへ届く起点になる
- 高Path Mageを前線でなく後方Ritualistとして使いたい

というCarrierです。

逆に、Staffなしでも必要な仕事を全部できるMageへ常設しても価値は薄くなります。

---

# D2でForgeできることの意味

Skull StaffはD2でForgeし、装備後はD3として扱えるため、**native D2をD3運用へ変える橋**になります。

ただし、native DeathがD1しかない国家がStaffだけで自己完結してD2へ上がれるわけではありません。

最初の一本には、

- native D2 Mage
- RandomでD2へ届くMage
- Summon / Hero / Pretenderなど別のD2 source

が必要です。

Booster計画では「完成後のPath」だけでなく、**最初の一本を誰がForgeするのか**まで書きます。

---

# 両手Slotが最大の機会費用

Skull Staffは**2-h weapon**です。

これはCaster専用なら問題になりにくい一方、Thug / SC / 前線Commanderへ持たせる場合は大きな制約になります。

両手を使うことで、

- Shield
- 片手武器
- 別の手持ちBooster
- 防御・攻撃用の手Slot構成

と競合します。

そのため、

```text
Death +1で得るCast能力
vs
両手Slotを失うBuild cost
```

を比較します。

Casterを戦闘の中央へ立たせるほど、このSlot競合は重くなります。

---

# Booster chainの一部として使う

Skull Staff単体で終わらず、別のPath上昇手段と組み合わせて**Magic access route**を作ることがあります。

考え方は、

```text
素のPath
→ Skull Staff
→ 次のSpell / Ritual / Booster閾値
→ さらに高いDeath access
```

です。

ただしchainが長くなるほど、

- Research
- Gem
- Forge turn
- Carrier
- Slot

を同時に要求します。

「理論上D5へ届く」ではなく、**何Turn目に、どのMageが、何のために届くのか**で評価します。

---

# 戦争前にForgeする条件

次が揃うほど優先度が上がります。

- D2 Forge Mageがいる
- Construction 5へ到達済み
- +1で具体的なBattle spellが解禁される
- そのSpellを使うResearchが終わっている
- 必要Gemを戦場へ持ち込める
- Carrierを前線へ安全に運べる
- 両手Slotを使ってもBuildが成立する

特に**「次の戦闘でStaffを持つことでscriptの何行目が変わるか」**まで書けるなら、Forge理由は明確です。

---

# 後方Ritual用にForgeする条件

戦闘に出さず、Lab内でPath requirementを越える用途も強力です。

この場合は、

- 両手Slotの戦闘上の欠点がほぼ消える
- 一つのStaffを複数Mageで使い回せる
- RitualするTurnだけ装備すればよい

ため、前線Casterより運用しやすくなります。

Staffを「Mage個人の所有物」ではなく、**Labに置く共有インフラ**として見ると無駄が減ります。

---

# Forgeしない・後回しにする条件

- +1しても今のResearchでは役割が増えない
- Death Gemを直近のBattle / Ritualへ回したい
- D2 MageのForge turnが高価
- 両手SlotをShieldや別Itemへ使いたい
- すでに高Path Mageだけで必要数を賄える
- Staffを作っても前線への輸送が間に合わない

Boosterは「いつか使う」だけでは弱く、**Research・Gem・戦争Timingが同時に噛み合う時**に強くなります。

---

# Counter：敵のStaffではなく閾値を読む

敵のSkull Staffを見たら、「Deathが+1された」で止めません。

見るべきなのは、

- そのCarrierの素Path
- Staff込みでどのPathへ届いたか
- そのResearch帯で何が新しくCast可能になったか
- Staffを失うとscriptが崩れるか

です。

対策は、

- CarrierをAssassination / Raidで狙う
- Gem carrierを落とす
- Staff依存の高Path spellにResistanceやMR等を合わせる
- 戦闘前にStaffを別Mageへ渡す物流を乱す

など、**Boosterで成立した新しい役割**へ向けます。

---

# よくある失敗

## 「D+1だから強い」でForgeする

新しいSpellが解禁されなければ、Path表示だけ増えて終わることがあります。

## 両手Slotを忘れる

前線Casterへ持たせた結果、Shieldや重要な手持ちItemを装備できなくなります。

## 最初の一本を誰がForgeするか決めていない

native D1しかなく、計画した時期にD2 Forge Mageが存在しないことがあります。

## Researchより先に作りすぎる

Boosterは完成しているのに、使いたいSpellが未研究という状態になります。

## 高価なMageへ常設する

後方Ritualなら一つを使い回せる場合があります。

---

# Test game checklist

```text
[ ] C5・D2でSkull StaffがForge可能か確認
[ ] Item 62であることを確認
[ ] 装備前後でDeathが+1されることを確認
[ ] 2-h weaponで両手Slotを占有することを確認
[ ] D2 Mageが装備後D3として目的Spellを選べるか確認
[ ] Battle spellのscript候補が装備前後でどう変わるか確認
[ ] RitualのPath requirementを越えられるか確認
[ ] Staffを別Mageへ渡して共有運用できるか確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 62](../../data/items/by-id/62.md)
- [Magic Path Booster](../boosters.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- Dominions 6 Main Manual — Forge Item / Magic Path
- Spell requirementと実際に選べるscriptはゲーム内表示を最終確認
