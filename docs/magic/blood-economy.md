---
title: Blood Economy・Blood Hunt・Blood Sacrifice
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
---

# Blood Economy・Blood Hunt・Blood Sacrifice

Bloodは、通常Gemとは別の生産・輸送・消費Networkです。

```text
PopulationのあるProvince
        ↓
Blood HunterがBlood Hunt
        ↓
Blood Slaveを確保
        ↓
UnrestをPatrol等で管理
        ↓
Lab・輸送Commanderで集約
        ↓
Ritual・Forge・Battle・Blood Sacrificeへ投入
```

Blood国家の強さは、強力なSpellをResearchしたことでは決まりません。

> **毎Turn、何人のHunterが、どのPopulationを使い、どれだけUnrestを発生させ、何Slaveを安全に前線へ届けるか**

まで完成して初めてBlood Magicが国家戦略になります。

このページでは、[EA Mictlan — Reign of Blood](../nations/ea/mictlan.md)を主要例として、Blood Hunt、Unrest、Patrol、Slave輸送、Sabbath、Blood Sacrificeを一つの経済として整理します。

!!! warning "数式とPatch"
    Blood Hunt量、Unrest、Population、Hunter bonus、Patrol効率等の正確な式はPatchと国家能力に依存します。本文は判断手順を扱い、現在の数値はゲーム内Help・Message・Province画面・Unit popupを優先してください。

---

## 最初に覚える十項目

| 項目 | 最初の理解 |
|---|---|
| Blood Slave | Gemに近い魔法資源だが、人間として扱われる場面もある |
| Blood Hunter | Blood PathとBlood Search bonusを持つMage・Priestが中心 |
| Population | Huntの基盤。枯らすと将来のIncome・Supply・Hunt能力が弱くなる |
| Unrest | Huntで上がり、Income・Recruitment・次のHunt効率を悪化させる |
| Patrol | Unrestを下げるが、Populationを傷付ける場合がある |
| Lab | Slaveの集約・受け渡し・Ritualの中心 |
| Transport | HunterからCaster・前線へSlaveを運ぶCommander turnが必要 |
| Research | Blood Spellを解禁しても、Slave supplyがなければ使えない |
| Sabbath | 戦闘中のBlood版Communion。Master数とSlave保護が必要 |
| Blood Sacrifice | TempleでSlaveを宗教圧力へ変換する国家固有の重要Order |

---

# Blood Slaveは何か

Blood Slaveは、Blood Spell、Blood Ritual、Blood Item、Blood Sacrifice等に使う資源です。

通常Gemと似ていますが、運用上は違います。

- ProvinceのPopulationから探す
- HuntでUnrestが発生する
- Hunter turnを消費する
- Patrolや輸送が必要
- Battleへ持ち込むとCasterが消費する
- 国家によって宗教資源にもなる

つまり、表示上のSlave数だけでなく、

```text
Hunter turn
Patrol turn
輸送turn
Population damage
失ったIncome
```

もCostです。

---

# Blood Economyを始める前の問い

Blood Huntを始める前に、次を書きます。

```text
最初に使うBlood Spell / Ritual：
必要Research：
必要Blood Path：
一回のSlave cost：
毎Turnまたは一回限り：
使用予定Turn：
必要Caster数：
必要Hunter数：
Hunt Province候補：
Patrol担当：
輸送経路：
```

用途が決まっていないのにHunterを大量生産すると、

- Researchが遅れる
- GoldをHunterへ使う
- UnrestでIncomeが減る
- Slaveだけ倉庫へ積まれる

ことがあります。

一方、Research完成後にBlood Huntを始めると、必要量が間に合いません。

Blood economyは、

```text
使用予定Turnから逆算してHunterを増やす
```

設計です。

---

# Blood Hunterを選ぶ

## 見るもの

```text
Blood Path
Blood Search bonus / Douse bonus
Gold cost
Commander Points
Research価値
Priest level
移動力
生存性
他の重要Role
```

## 高位MageをHunterへ固定しない

高位Blood Mageは一回のHuntで効率が高くても、

- Ritual
- Forge
- Battle
- Sabbath Master
- Research
- Blood Sacrifice

の価値が高い場合があります。

一般に、

```text
安価・量産可能なHunter
→ 日常のBlood Hunt

高Path・Rare Mage
→ Ritual・Forge・戦闘・Booster chain
```

へ分けます。

## Priestとの競合

EA MictlanのようにBlood MageがPriestでもある国家では、同じCommanderが、

- Blood Hunt
- Blood Sacrifice
- Research
- Battle support
- Temple建設

を担当できます。

これは柔軟性である一方、Commander turnの競合です。

```text
今Turn Blood Huntした
＝ 今Turn Blood Sacrificeしていない
```

ことを毎Turn意識します。

---

# Hunt Provinceを選ぶ

## Population

Blood HuntはPopulationのあるProvinceで行います。

Populationは同時に、

- Income
- Supplies
- Recruitment capacity
- Province Defence上限
- 将来のBlood Hunt

でもあります。

一つのProvinceを短期間で枯らすより、複数ProvinceへHunterを分散する方が持続しやすい場合があります。

## 安全性

Hunterは通常、前線Battleに強いCommanderではありません。

Hunt Provinceは、

- Borderから距離がある
- Fortまたは警戒網がある
- Scoutが周囲を見ている
- Raiderの侵入路ではない
- Retreat先がある

場所を選びます。

## Incomeとの交換

高Income ProvinceでHuntするとSlaveを得やすい一方、UnrestによるGold損失も大きくなります。

低Population・低Income ProvinceはGold損失が小さい一方、長期的なHunt基盤として弱い場合があります。

したがって、

```text
Population
Income
安全性
Patrol能力
Fort・Lab
前線までの輸送距離
```

を一緒に見ます。

## FortとLab

LabがあるとSlave集約が容易になります。

FortはHunterを守りますが、Siegeされると、

- Hunterが閉じ込められる
- Slave輸送が止まる
- Labを失う
- Blood engine全体が見える

Riskがあります。

すべてのHunterを一つの巨大Blood Fortへ集めず、複数拠点へ分散します。

---

# Blood Huntの基本手順

```text
1. HunterをPopulationのあるProvinceへ置く
2. Blood Hunt orderを設定する
3. 次TurnのMessageとProvince Unrestを確認する
4. 得たSlaveをLabまたは輸送Commanderへ集める
5. Unrestが高いならHunter数を減らすかPatrolを増やす
6. Population・Income・Recruitmentの低下を確認する
7. 必要量が集まったらRitual・Forge・前線へ移す
```

## 一Turnの結果だけで判断しない

Blood Huntには変動があります。

一回の大成功・失敗だけでHunter効率を決めず、数Turn記録します。

```text
Turn：
Province：
Population：
Hunter：
Blood Path / bonus：
得たSlave：
Unrest増加：
Patrol：
Income変化：
```

を記録すると、国家とMapに合う運用が分かります。

---

# Unrest

UnrestはBlood economyの主要制約です。

高Unrestは、

- Income
- Resources
- Recruitment Points
- Commander Points
- Blood Hunt効率
- Event・Rebellion Risk

を悪化させます。

Blood Hunterを増やすほどSlaveは増えますが、Unrest管理が追いつかなければ、国家経済全体を止めます。

## Hunterを減らす判断

次の場合はHunterを増やすより減らします。

- Unrestが毎Turn増え続ける
- Mage Recruitが止まる
- Fort資金が貯まらない
- PatrolでPopulationを殺しすぎる
- Slaveの用途がまだResearchされていない
- 輸送できず拠点へ滞留する

## Hunt Provinceを休ませる

同じProvinceを永続的に使わず、

```text
Hunt
→ Unrest上昇
→ Hunterを移動
→ Patrol・自然低下
→ 回復後に再利用
```

というRotationも使います。

---

# Patrol

Patrolは、

- Unrest低下
- Stealth Unit発見
- Hunter拠点防衛

を同時に行えます。

しかしPatrolはPopulationを殺す場合があります。

Blood economyでは、

```text
Unrestを下げるためにPatrol
→ Populationを失う
→ 将来のIncome・Hunt基盤が弱くなる
```

という交換があります。

## Patrol担当

高価なMageをPatrolへ使わず、

- Patrol Bonus Unit
- 安価な兵
- Slave兵
- Freespawn
- 余剰Commander

を使います。

## Patrolしすぎない

Unrest 0を毎Turn絶対目標にすると、Population損失が大きくなる場合があります。

目的は、

```text
Blood HuntとRecruit・Incomeが継続できる範囲へUnrestを管理する
```

ことです。

---

# Slaveの集約と輸送

## Hunterから国庫へ

LabがあるProvinceでは、CommanderのPersonal Blood SlavesとNational Treasury間を移動できます。

高速移動Shortcutが使える場合もありますが、現在画面の`?`を基準にしてください。

## 輸送Commander

前線Blood MageへSlaveを渡すには、

- Mage本人が後方Labへ戻る
- 輸送Commanderが運ぶ
- Magic Movementで届ける
- 前線Labを建てる

方法があります。

輸送Commanderを、

```text
大量Slaveを一人へ集中
```

させると、Raid・Assassination・Route cutで全量を失います。

複数便へ分けます。

## 前線Lab

前線Labは、

- Slave補給
- Ritual
- Item受け渡し
- Mage再編

に便利です。

一方、敵Raidで奪われるとBlood engineが露出します。

Border直上だけでなく、一歩後ろのFortやRally pointを補給拠点にします。

---

# Blood Researchと生産計画

Blood Magicは、Research levelが上がるほど、

- Demon summon
- Vampire・特殊Commander
- Remote attack
- Blood economy支援
- Sabbath
- Global・Large ritual

へ広がります。

しかし、Researchだけを先行させてもSlaveが足りません。

## Breakpointの書き方

```text
Spell / Ritual：
Blood level：
Caster：
Booster：
一回Cost：
一Turnに何回使う：
必要Slave reserve：
Hunter何人で何Turn準備する：
```

## 毎Turn消費と一回消費

```text
一回だけ使う大型Ritual
```

と、

```text
毎Battle・毎Turn使うSummon / Ritual
```

では必要経済規模が違います。

毎Turn10 Slave使う計画なら、平均生産が10未満では在庫を食い潰します。

---

# Blood ItemとBooster

Blood boosterは、

- 高位Ritual
- Blood summon
- Sabbath Master
- Blood Sacrifice Item

へつながります。

Item評価では、

```text
Construction level
Forge Path
Slave / Gem cost
誰がForgeするか
誰が装備するか
失ったときの再建Turn
```

を見ます。

Booster holderを通常Hunterへ戻すと、国家のRitual accessが止まる場合があります。

Rare CasterとBoosterを別名・番号で管理します。

---

# Sabbath

SabbathはBlood Magicを使うCommunion類似構造です。

基本は、

```text
Sabbath Master
＋ Sabbath Slave
→ MasterのPathを上げる
→ SlaveへFatigue・効果が流れる
```

です。

[Communion・Sabbath](communions.md)の共通原則も参照してください。

## 設計順

```text
1. 必要Spellを決める
2. 必要Pathを計算する
3. 最小Slave数を決める
4. Master数を制限する
5. SlaveのResistance・Reinvigorationを確認する
6. 総Roundを短くする
7. Battle後に生存率を確認する
```

## Slaveは無料ではない

Sabbath Slaveが安価でも、

- Recruit turn
- Commander Points
- Slaveとして使うBlood Slave
- Script操作
- Battle後の回復

を使います。

毎BattleでSlaveを全損する構造は、長期戦で崩れます。

## Crosspath

Blood MageがFire・Water・Astral・Nature等も持つ国家では、SabbathでCrosspath Spellへ届きます。

EA Mictlanでは、Sun・Rain・Moon・LandのPriestが異なるPathを持つため、

```text
Bloodを共通Networkとして
Fire / Water / Astral / Natureを高位化する
```

運用が可能です。

ただしMage種類と首都Queueを事前に揃える必要があります。

---

# Blood Sacrifice

Blood Sacrificeは、TempleでPriestがBlood Slaveを消費し、Dominion spreadへ変換するOrderです。

## 何と競合するか

Blood Sacrifice中のPriestは、同Turnに、

- Blood Hunt
- Research
- Preach
- Ritual
- Forge
- 移動

を行えません。

したがってSacrifice costは、SlaveだけでなくPriest turnです。

## MictlanのRestricted Dominion

EA Mictlanでは、通常の国家よりDominion spreadが制限され、Blood Sacrificeが国家存続と前線Dominionの中心になります。

運用は、

```text
Templeを建てる
→ Sacrifice Priestを置く
→ Slave補給を維持する
→ Border・Capital・ThroneのCandleを監視する
```

です。

Blood Sacrificeを忘れると、Heavy Blessや国家Army以前にDominionで敗北するRiskがあります。

## Sacrifice拠点

拠点は、

- Capital
- Border Temple
- Throne
- Enemy Dominionと接するFort
- 新しいPlane・Cave入口

に置きます。

すべてのTempleへ毎Turn同数を配るのではなく、宗教戦線へ集中します。

## Jade Knife等

EA MictlanのJade Knifeのように、Blood Sacrifice能力を高めるItemがあります。

装備者のPriest level、Adept Sacrificer、現在のTemple、Slave数を確認し、

```text
一体の高効率Sacrificer
vs
複数の安価Priest
```

を比較します。

---

# EA Mictlanを例にしたBlood Engine

EA Mictlanは、

- Any-fort Mictlan Priest：B1 H1
- Any-fort Nahualli：S1 N2
- 首都Site Mage：Fire / Water / Astral / NatureとB2～3
- Restricted Dominion
- Blood Sacrifice
- Sacred Jaguar Warrior
- Blood向けPretender・Bless Point

を持ちます。

基本Engineは、

```text
Mictlan Priestを複数Fortで量産
→ 後方ProvinceへBlood Hunterとして配置
→ PatrolとRotationでUnrest管理
→ TempleへSlaveを送りBlood Sacrifice
→ 首都高位PriestへSlaveを集約
→ Blood Ritual・Sabbath・Summonへ投入
```

です。

詳しくは[EA Mictlan国家攻略](../nations/ea/mictlan.md)を参照してください。

---

# Blood国家へのCounter

## Hunter ProvinceをRaidする

Blood Hunterを倒すだけでなく、

- Labを奪う
- Templeを壊す
- Patrolを分散させる
- Slave輸送路を切る

と、Blood engine全体へ効きます。

## Populationを奪う

高Populationの安全な後方を奪うと、将来のSlave供給が減ります。

## Blood Mageを戦闘へ強制する

Hunter・Researcher・Ritual casterを防衛へ出させると、敵の長期生産を止められます。

## Slave在庫を消費させる

小BattleやRemote attackを繰り返し、敵にGem・Slaveを使わせます。

## Templeを狙う

Blood Sacrifice国家ではTemple破壊がDominion戦へ直結します。

---

# 毎Turn Checklist

```text
□ Blood Hunt結果とUnrestを確認した
□ Hunterを増やすProvince・休ませるProvinceを決めた
□ PatrolでPopulationを殺しすぎていない
□ SlaveをHunter個人へ放置していない
□ 前線補給便と予備便を分けた
□ 次のBlood Researchの使用量を計算した
□ Blood Sacrifice担当を忘れていない
□ Rare Blood Mageを通常Hunterへ戻していない
□ SabbathのMaster数とSlave保護を確認した
□ RaiderがHunter Provinceへ届く経路をScoutした
```

---

# よくある失敗

## Bloodを始める＝Hunterを大量生産する

用途、Research、輸送、Patrolが決まっていません。

## Unrestを見ず同じProvinceでHuntし続ける

Income・Recruit・Hunt効率が同時に壊れます。

## PatrolでPopulationを消し飛ばす

短期的にUnrestが下がっても、長期Blood基盤を失います。

## 高位Mageを全員Hunterにする

Ritual・Forge・Battle・Researchへ使えるCasterがいなくなります。

## Slaveを一人の輸送Commanderへ集中する

Raid一回で数Turn分の生産を失います。

## Blood Researchだけ先に上げる

使用Slaveがなく、Research Pointが実戦力へ変わりません。

## SabbathのSlave数だけ増やす

Master数・総Round・Slave resistanceを管理せず全滅します。

## Blood Sacrificeを通常Preachと同じ感覚で扱う

Slave、Temple、Priest turn、輸送を必要とする独立した宗教経済です。

---

## 関連ページ

- [EA Mictlan — Reign of Blood](../nations/ea/mictlan.md)
- [Blood Path](paths/blood.md)
- [Communion・Sabbath](communions.md)
- [GemとBlood Slave](gems.md)
- [Research](research.md)
- [Dominion](../systems/dominion.md)
- [Province](../systems/province.md)
- [内政・補給・自動化Q&A](../getting-started/logistics-faq.md)
- [命令とBattle Script](../basics/orders.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [EA Mictlan community reference](https://illwiki.com/dom5/dom6/mictlan-ea)
