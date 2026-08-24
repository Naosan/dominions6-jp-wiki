---
title: "Starshine Skullcap"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 207
---

# Starshine Skullcap

**Astral MageのAstral Pathを+1し、Magic Resistanceも+2する、Construction 7のHelmet型Booster。**

Starshine SkullcapはAstral accessを伸ばすだけでなく、重要CasterのMRも同じHelmet Slotから補います。攻略上は、**高Astralの閾値越えと、敵のMR依存Counterへの小さな保険を一枠へまとめるItem**として評価します。

- [Dominions 6.35固定データ — Item 207](../../data/items/by-id/207.md)
- [Magic Item攻略辞典](index.md)
- [Magic Path Booster](../boosters.md)
- [Coin of Meteoritic Iron](coin-of-meteoritic-iron.md)

---

# まず何ができるか

6.35固定データでは、Starshine Skullcapは、

- Construction 7
- Forge要求 **S2**
- Helmet Slot
- **Astral +1**
- **Magic Resistance +2**
- Armor record 83

を持ちます。

Armor record 83はDefence 0、Encumbrance 0の軽い頭部装備です。

Item descriptionでも、純粋なAstral lightを帯びたskullcapが、

- Astral magicを扱いやすくする
- hostile spellへ抵抗しやすくする

と説明されています。

したがって、

```text
Astral +1
＋
MR +2
＋
軽いHelmet
```

が一つのItemへ入っています。

---

# 主目的はAstralの閾値越え

Skullcapの価値は、Path表示が1増えたこと自体ではありません。

装備前後で、

- 新しくCastできるBattle spell
- 新しく実行できるRitual
- 新しくForgeできるItem
- 同じSpellを高PathでCastした場合のFatigue
- Communionを組まずに届くPath
- GlobalやTeleport系Ritualへの到達
- 次のBooster chain

がどう変わるかを確認します。

```text
S2 Mage
→ Starshine Skullcap
→ S3として目的Spell / Ritual / Forgeへ到達
```

のように、**あと1で役割が生えるAstral Mage**へ持たせます。

S+1しても現在のResearchでは何も増えないなら、その時点ではSkullcapが寝ています。

---

# C7・S2という入口条件

Forge要求はS2だけなので、S2E2を要求する[Coin of Meteoritic Iron](coin-of-meteoritic-iron.md)よりCrosspath条件は軽いです。

一方、解禁はConstruction 7です。

```text
Starshine Skullcap
→ Forge MageのPath条件は比較的単純
→ ResearchはC7まで必要

Coin of Meteoritic Iron
→ C5で解禁
→ S2E2を同じMageへ要求
```

という違いがあります。

Skullcapを計画するときは、

- C7へ何Turn目に到達するか
- C7を優先して他Schoolが遅れないか
- その時点でS+1が何を解禁するか
- C7到達までCoin等で代用できないか

を見ます。

「S2で作れるから簡単」だけでは不十分で、**Research timingの重さ**を含めて評価します。

---

# Coin of Meteoritic Ironとの違い

Coin of Meteoritic IronもAstral +1を与えますが、Slotと入口条件が違います。

| Item | 解禁 | Forge要求 | Slot | 追加効果 |
|---|---:|---|---|---|
| Starshine Skullcap | C7 | S2 | Helmet | MR +2、軽い頭部防具 |
| Coin of Meteoritic Iron | C5 | S2E2 | Misc | MR +1 |

攻略上の使い分けは、

```text
Skullcap
→ Helmet Slotを使える
→ Misc SlotをMR・Penetration・別Boosterへ残したい
→ S2E2 Crosspathがない
→ C7まで待てる

Coin
→ C5から使いたい
→ S2E2 Forgerがいる
→ Helmet Slotを別装備へ残したい
```

です。

両方を同時装備できるCarrierならAstralをさらに伸ばせますが、必要Path、Research、Gem、Slotが本当に任務へ変換されるかを確認します。

---

# MR +2は付随効果だが軽視しない

Starshine SkullcapはMR +2も与えます。

これは、

- MR-negates Spell
- Mind control
- Soul系effect
- Charm・Paralyze等のControl
- Assassinが使うMR依存手段
- 敵Astral MageのCounter

に対する防御を補います。

ただし、MR +2だけで全Counterへ安全になるわけではありません。

```text
主目的: Astral +1で役割を解禁
付随価値: MR +2でCarrier Riskを少し下げる
```

と考えます。

敵の主な勝ち筋がMR-based effectなら、[Amulet of Antimagic](amulet-of-antimagic.md)等の専用Itemも比較します。

---

# Amulet of Antimagicとの役割分担

[Amulet of Antimagic](amulet-of-antimagic.md)はMisc SlotからMRを大きく補う防御Itemです。

Starshine SkullcapはHelmet SlotからAstral +1とMR +2を与えます。

Slotが違うため、

```text
Starshine Skullcap
＋
Amulet of Antimagic
```

でPathとMR防御を積み重ねることもできます。

ただし装備数が増えるほど、

- Gem cost
- Forge turn
- Item輸送
- Carrier死亡時の損失
- 他Slotの機会費用

も増えます。

MRをどこまで上げるべきかは、敵SpellとCarrier価値を見て決めます。

---

# Spell Focus・Eye of the Voidとの違い

[Spell Focus](spell-focus.md)と[Eye of the Void](eye-of-the-void.md)は、敵へMR-negates Spellを通すPenetration側のItemです。

Starshine SkullcapはPenetrationを直接増やすItemではありません。

```text
Starshine Skullcap
→ Astral requirementを越える
→ 高Path Castへ届く
→ 自分のMRも増える

Spell Focus
→ Penetrationを直接増やす
→ Pathは増えない

Eye of the Void
→ Penetrationを大きく増やす
→ 自分のMR低下と眼の置換Riskを負う
```

目的SpellをそもそもCastできないならSkullcapが先です。

目的SpellはCastできるが、高MR Targetへ通らないならPenetration Itemを比較します。

HelmetとMiscでSlotが異なるため、SkullcapとPenetration Itemを組み合わせる余地もあります。

---

# Communionとの役割分担

AstralはCommunionによってBattle中のPathを大きく上げられます。

一方、Starshine Skullcapは装備中のItem Boosterなので、

- Battle spell
- Ritual
- Forge

すべてで使えます。

```text
Skullcap
→ Strategic Map上でもS+1
→ Ritual・Forgeへ使える
→ Slave不要

Communion
→ Battle中だけPath上昇
→ Slave、配置、Script、Fatigue管理が必要
```

という違いです。

大規模BattleだけならCommunionで代替できる場合があります。

Ritual、Forge、少人数戦、Assassination、即応迎撃ではSkullcapの恒常的な+1が使いやすくなります。

---

# Helmet Slotの機会費用

Starshine SkullcapはHelmet Slotを使います。

前線CasterやThugでは、同じSlotに、

- 高Protection Helmet
- Elemental Resistance付きHelmet
- Fear・Spirit sight等の特殊Helmet
- [Flame Helmet](flame-helmet.md)
- [Winged Helmet](winged-helmet.md)

を置けます。

Skullcapは軽くEncumbranceを増やしませんが、重い一撃への頭部Protectionを最大化するItemではありません。

```text
Astral +1とMR +2でScriptを成立させる価値
vs
より高い頭部Protection・別耐性を失うCost
```

を比較します。

後方Ritualist・Forgerでは、このSlot costは小さくなります。

---

# 後方共有Itemとして使う

RitualやForgeだけが目的なら、Skullcapを一人へ常設する必要はありません。

Labで、

- RitualするTurnだけ装備
- ForgeするTurnだけ装備
- 使用後に別Mageへ渡す

運用ができます。

```text
Skullcap一個
→ 複数S2 Mageが必要Turnだけ共有
```

とすると、Gem投資を圧縮できます。

ただし別Fortへ置き忘れると目的Turnを失うため、誰が持っているかを管理します。

---

# 前線Carrierへ持たせる条件

前線で使うなら、PathだけでなくCarrierの生存と到達を確認します。

- Skullcap込みで目的SpellをCastできる
- 必要Gemを持つ
- Script完走まで生存できる
- MR +2が敵Counterへ意味を持つ
- Helmet SlotのProtection不足を他装備で補える
- Retreat routeがある
- Carrier死亡時にSkullcapを失っても戦略全体が止まらない

高価なAstral Mageへ複数Boosterを集中すると、敵にとって分かりやすい優先Targetになります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 7へ到達済み、または明確に向かっている
- S2 Forgerを確保できる
- S+1で具体的なSpell・Ritual・Forgeが解禁される
- Coin of Meteoritic IronのS2E2条件を満たせない
- Helmet Slotが空いている
- Misc Slotを別Itemへ残したい
- MR +2がCarrierの生存に役立つ
- Skullcapを複数Turn共有・再利用できる

最も良いForge理由は、

```text
Skullcapを装備すると、次Turnに誰が何を実行できるか
```

を具体的に言えることです。

---

# Forgeしない・後回しにする条件

- C7到達が他の重要Researchを大きく遅らせる
- S+1しても現在のResearchで役割が増えない
- C5のCoin of Meteoritic Ironで必要数を満たせる
- Helmet Slotへ別の防御Itemが必須
- MRではなくElemental damageや物理Burstが敗因
- S2 MageのForge turnが高価
- Skullcapを前線へ輸送するTimingが間に合わない
- すでに高Astral Mageだけで必要な仕事を賄える

Boosterは「強いから作る」のではなく、**閾値を越えた結果を買うItem**です。

---

# Counter：Skullcapではなく新しいAstral役割を読む

敵がStarshine Skullcapを装備していたら、

- Carrierの素Astral
- Skullcap込みのAstral
- 現在のResearch帯
- 新しく届いたBattle spell / Ritual
- Communionの有無
- MR +2込みの最終MR

を見ます。

Counterは、

- CarrierをAssassination・Raidで狙う
- Gem carrierを落とす
- Script開始前にPressureを掛ける
- 高MRで敵のMR-negates Spellを受ける
- Magic Duel等のAstral対策を検討する
- Elemental damage・物理BurstなどMR以外を突く
- Skullcap依存のMageを複数地点へ分散させる

ように、**Boosterで成立した役割**へ向けます。

Skullcapを外させるだけで目的Spellが使えなくなるなら、CarrierとItem物流は明確な弱点です。

---

# よくある失敗

## S+1だけを見て作る

装備後も新しい仕事が増えなければ、GemとForge turnを寝かせます。

## C7到達Costを無視する

Forge要求S2は軽くても、ResearchはC7です。

## MR +2を完全防御と思う

最終MRと敵のPenetrationを確認します。

## 頭部Protectionを忘れる

軽いSkullcapなので、前線Carrierでは別Helmetとの比較が必要です。

## Coinとの違いを見ない

C5かC7か、S2E2かS2か、MiscかHelmetかで国家ごとの価値が変わります。

## 高価なCarrierへ全Boosterを集中する

死亡時にMage、Skullcap、Gem、戦略accessを同時に失います。

---

# Test game checklist

```text
[ ] C7・S2でStarshine SkullcapがForge可能か確認
[ ] Item 207 / Armor record 83であることを確認
[ ] 装備前後でAstralが+1されることを確認
[ ] Magic Resistanceが+2されることを確認
[ ] Defence 0・Encumbrance 0のHelmetであることを確認
[ ] S0のPathless bearerでAstral表示がどうなるか確認
[ ] 目的Battle spell・Ritual・Forgeが新しく選べるか確認
[ ] 同じSpellのFatigueが装備前後でどう変わるか確認
[ ] Communion内外でPath表示とScriptを比較
[ ] Magic Duel等のAstral相互作用を同条件で確認
[ ] Coin of Meteoritic Iron装備時とのSlot・Stats差を比較
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 207](../../data/items/by-id/207.md)
- [Magic Path Booster](../boosters.md)
- [Coin of Meteoritic Iron](coin-of-meteoritic-iron.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Spell Focus](spell-focus.md)
- [Eye of the Void](eye-of-the-void.md)
- [Communion](../../magic/communions.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / armors / protections_by_armor / Item description
- Dominions 6 Main Manual — Magic Path / Magic Resistance / Forge Item / Communion
- Pathless bearer、Spell Fatigue、Magic Duel等の実挙動はゲーム内表示・Battle Replay・Test gameを最終確認
