---
title: "Brazen Vessel"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 394
---

# Brazen Vessel

**Blood MageのBlood Pathを+1する、Construction 5・B5 ForgeのMiscellaneous Booster。**

Brazen VesselはC5で解禁されますが、最初の一個にB5を要求します。攻略上は、**すでに確保した高Blood accessを、Ritual・Forge・Battle casterへさらに一段伸ばす後方Infrastructure**として評価します。

- [Dominions 6.35固定データ — Item 394](../../data/items/by-id/394.md)
- [Magic Item攻略辞典](index.md)
- [Magic Path Booster](../boosters.md)
- [Blood Thorn](blood-thorn.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)

---

# まず何ができるか

6.35固定データでは、Brazen Vesselは、

- Construction 5
- Forge要求 **B5**
- Miscellaneous Slot
- **Blood +1**

を持ちます。

Item descriptionでは、金属製の頭蓋に縛られたDevilが装備者へ秘密を囁き、Blood magic skillを高めると説明されています。

基本用途は、

```text
B5 Mage
→ Brazen VesselをForge・装備
→ B6としてBlood magicを使う
```

という高Pathの閾値越えです。

---

# C5でも「低い入口」ではない

Brazen VesselはConstruction 5で解禁されます。

しかしForge要求はB5です。

```text
Research条件: C5
Path条件: B5
```

なので、C5へ早く到達しても、B5 Forgerがいなければ作れません。

最初の一個には、

- native B5 Mage
- Randomが同時成立してB5へ届くMage
- Pretender
- Hero
- 高Blood Summon
- Empowerment済みMage
- 別Booster込みでB5へ届くMage

が必要です。

Brazen VesselはB3やB4から自然にB5へ上がるための最初の橋ではなく、**すでにB5へ届いたaccessをB6以降へ伸ばすItem**です。

---

# 「国家にB5がある」と「今Forgeできる」は別

Magic access表で理論上B5へ届いていても、実際に最初のVesselを作れるとは限りません。

確認するのは、

- B5が同じMage上に成立しているか
- Random依存なら今回のGameで引けたか
- PretenderがAwake / Dormant / Imprisonedのどれか
- Summonに必要なResearchとSlaveを確保したか
- B5 MageをForgeへ一Turn回せるか
- Forgerが前線・Blood Hunt・Ritualで拘束されていないか

です。

```text
理論上のB5 access
≠
このTurnにForge orderを出せるB5 Mage
```

と考えます。

---

# Blood +1は新しい仕事で評価する

Brazen Vessel装備前後で、

- 新しくCastできるBattle spell
- 新しく実行できるBlood Ritual
- 新しくForgeできるItem
- 同じSpellを高PathでCastした場合のFatigue
- Sabbathを組まずに届くPath
- 高位Demon・Commander summonへの到達
- Global級Ritualへの到達
- 次のBooster chain

がどう変わるかを確認します。

```text
装備前: B5でできる仕事
装備後: B6で新しくできる仕事
```

の差がVesselの価値です。

B+1してもResearchやBlood Slave incomeが追いついていなければ、Path表示だけ増えて終わります。

---

# 高Pathで同じSpellを使う価値

新しいSpellを解禁しなくても、高Pathで同じBlood spellを使うことに価値が出る場合があります。

たとえば、

- Fatigueが変わる
- Slave使用の判断が変わる
- 効果量・対象数・Range等がPath scalingする
- Sabbathへの依存を減らせる
- Battle scriptの安定性が上がる

可能性があります。

ただし、これらはSpellごとに異なります。

```text
B+1だからすべてのBlood spellが同じ割合で強くなる
```

とは考えず、目的Spellのゲーム内表示とBattle Replayを確認します。

---

# Blood Thornとの違い

[Blood Thorn](blood-thorn.md)もBlood +1を与えますが、入口条件とSlotが大きく違います。

| Item | 解禁 | Forge要求 | Slot | 固有効果 |
|---|---:|---|---|---|
| Brazen Vessel | C5 | B5 | Misc | 後方運用しやすい恒常Booster |
| Blood Thorn | C7 | B3 | 片手Weapon | 命中時の生命吸収 |

攻略上は、

```text
Brazen Vessel
→ B5 Forgerを確保済み
→ C5から高Bloodを伸ばす
→ Hand Slotを空けたい
→ Ritual / Forge / backline caster向け

Blood Thorn
→ B3までは届く
→ C7までResearchする
→ Weapon Slotを使える
→ Hit依存の生命吸収も使う
```

と使い分けます。

B3～4中心の国家では、Vesselを欲しくても最初のB5が最大の問題です。

高Blood PretenderやSummonで最初のVesselを作れる国家では、C5時点から高位Blood routeを早く開けます。

---

# Misc Slotの機会費用

Brazen VesselはMisc Slotを一つ使います。

同じSlotには、

- MR防御
- Reinvigoration
- Regeneration
- Penetration
- Blood Hunt補助
- Elemental Resistance
- Luck
- 別Path Booster
- 特殊作戦Item

を置けます。

後方RitualistならMR・Resistanceの必要性が低く、Vesselを常設しやすくなります。

前線Blood Mageでは、

```text
Blood +1で得るScript
vs
MR・Fatigue・Resistance等を失うCost
```

を比較します。

高Path casterを一つのVesselへ依存させるなら、Carrier保護もItem costの一部です。

---

# Hand Slotを空けられる価値

Blood Thornと違い、Brazen Vesselは手を使いません。

そのためCarrierは、

- Shield
- Weapon
- Staff
- Matrix
- 別のHand-slot Booster

を同時に装備できます。

Backline casterでも、Hand Slotへ別Path BoosterやMatrixを置くBuildではMisc Boosterの方が組みやすくなります。

一方、Misc Slotが少ないCarrierでは、手が空く利点よりMR・Fatigue Itemを失うCostが重くなる場合があります。

---

# 後方共有Infrastructureとして使う

Brazen VesselはRitual・Forge担当へ常設するより、必要Turnだけ共有できます。

```text
B5 Mage AがVesselを装備
→ 高位Ritual
→ Labへ戻す
→ B5 Mage Bが次Turnに装備
→ 高Path ItemをForge
```

という運用です。

共有すると、

- 複数個のForge costを省く
- 高価なMage全員へ配らずに済む
- 前線喪失Riskを減らす
- 目的TurnだけB+1を得る

ことができます。

ただしVesselを別Fortへ運ぶTurn、Courier、Lab接続が必要です。

---

# Blood Slave economyが第二の入口

B6へ届いても、目的RitualのBlood Slaveを用意できなければ役割は成立しません。

確認するのは、

- 毎TurnのBlood Slave income
- Huntを行うMage数
- UnrestとPopulation
- 目的Ritual一回のSlave cost
- BattleへのSlave輸送
- 連続使用するTurn数
- 他のDemon summon・Item Forgeとの競合

です。

```text
VesselでPath requirementを越える
＋
Slaveを継続供給する
→ 高Blood planが動く
```

という二段構造です。

Brazen VesselはBlood Slaveを自動生成しません。

---

# Blood Huntに使う場合は実測する

Blood +1がBlood Hunt担当の結果へ影響するかを期待して常設する場合、

- Hunt order実行時にItemが参照されるか
- Hunt結果がどの程度変わるか
- 同じVesselをRitualistへ渡す方が価値が高くないか
- Misc Slotの別Blood Hunt Itemと競合しないか

をTest gameで確認します。

一Turnの結果はRandomに揺れるため、同条件を複数Turn比較します。

Vesselの主用途は高Bloodの閾値越えです。Blood HuntだけのためにB5 ForgerのTurnを使う価値があるかは別途判断します。

---

# Battle casterへ持たせる場合

前線Blood Mageへ持たせるなら、

- B+1でScriptの何行目が変わるか
- 必要Blood Slaveを持ち込めるか
- Sabbathなしで目的Pathへ届くか
- Misc Slotを防御Itemへ使わなくてよいか
- CarrierがScript完走まで生存できるか
- Slave carrierが先に倒されないか
- Retreat routeがあるか

を確認します。

高Path Blood Mageは高価で、VesselとBlood Slaveも同時に持ちます。

一体へ価値を集中させすぎると、Assassination・Teleport strike・Flankerの優先Targetになります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- このGameで実際にB5 Forgerを確保できた
- B+1で具体的なSpell・Ritual・Forgeが解禁される
- 目的RitualのBlood Slaveを供給できる
- Misc Slotを使ってもCarrierの任務が成立する
- Hand Slotを別Itemへ残す価値がある
- 一本を複数Mage・複数Turnで共有できる
- C7のBlood Thornを待たずに高Blood accessを伸ばしたい

特に、

```text
高Blood Pretender / Summon
→ 最初のVesselをForge
→ 別Mageへ渡す
→ 国家全体の高Blood担当を増やす
```

ように、希少なB5 accessを共有可能なItemへ変換できると価値が高くなります。

---

# Forgeしない・後回しにする条件

- B5 Forgerが存在しない
- B+1しても今のResearchでは役割が増えない
- Blood Slave incomeが目的Ritualを支えられない
- B5 MageのForge turnが高価すぎる
- Misc SlotへMR・Reinvigoration・Resistanceが必須
- C7のBlood ThornをB3から作る方が現実的
- すでに高Blood Mage一人で必要な仕事を賄える
- Vesselを前線へ輸送するTimingが間に合わない
- Carrier死亡時に国家のBlood plan全体が止まる

C5という数字だけで早期Itemと判断せず、**B5 accessの実在と目的RitualのTiming**を見ます。

---

# Counter：高Blood accessの集中点を狙う

敵のBrazen Vesselを確認したら、

- Carrierの素Blood
- Vessel込みのBlood
- 新しく届いたRitual / Battle spell
- Blood Slave income
- Vesselを共有しているFort
- B5 Forgerが一人だけか
- Carrierが前線か後方か

を読みます。

Counterは、

- B5 ForgerやVessel carrierをAssassinationで狙う
- Blood Hunt ProvinceをRaidしてSlave incomeを落とす
- Unrest・Population pressureを掛ける
- Slave輸送をInterceptする
- Lab・Fortを落としてItem共有を止める
- 高Blood ritualのTargetを分散・秘匿する
- 前線casterへMR・Burst・Flankerを合わせる
- Vessel依存のScriptを使わせないTimingで攻める

ように、**Item、Carrier、Slave economyの三点**を分けて攻めます。

---

# よくある失敗

## C5だから簡単に作れると思う

最初の一個にB5が必要です。

## B4からVesselでB5へ上がろうとする

B4 MageだけではVesselをForgeできません。最初のB5 sourceが別に必要です。

## Blood +1だけを見て作る

新しいRitualやForgeがなければPath表示だけ増えます。

## Blood Slave incomeを確認しない

Pathへ届いてもRitual costを払えません。

## Misc Slotの防御を外す

前線CasterがMR・Fatigue・Resistance不足でScript前に倒れます。

## 希少なB5 Mageを前線へ出す

Mage、Vessel、Blood Slave、国家のhigh-Blood accessを同時に失います。

---

# Test game checklist

```text
[ ] C5・B5でBrazen VesselがForge可能か確認
[ ] Item 394であることを確認
[ ] Blood Mage装備時にBloodが+1されることを確認
[ ] B0のPathless bearerでBlood表示がどうなるか確認
[ ] 目的Battle spell・Ritual・Forgeが新しく選べるか確認
[ ] 同じBlood spellのFatigue・Slave使用が装備前後でどう変わるか確認
[ ] Blood Hunt orderでItemの有無による結果を複数Turn比較
[ ] Sabbath内外でPath表示とScriptを比較
[ ] Blood ThornとのResearch・Forge要求・Slot差を比較
[ ] Vesselを別Mageへ渡して共有運用できるか確認
[ ] Carrier死亡時のItem回収・喪失をTest gameで確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 394](../../data/items/by-id/394.md)
- [Magic Path Booster](../boosters.md)
- [Blood Thorn](blood-thorn.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- Dominions 6 Main Manual — Blood Magic / Blood Hunt / Sabbath / Forge Item
- Pathless bearer、Spell Fatigue、Blood Hunt、Slave使用の実挙動はゲーム内表示・Turn message・Battle Replay・Test gameを最終確認
