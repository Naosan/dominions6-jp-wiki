---
title: MA Ermor
page_type: nation-guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
nation_id: 54
era: "MA"
epithet: "Ashen Empire"
---

# MA Ermor — Ashen Empire

MA Ermorは、**Goldで兵士とMageを雇う国家ではなく、DominionでPopulationを死者へ変え、Death GemとPriest turnで国家そのものを再構築する国家**です。

国家Engineは、

> **Land of UndeathによるPopkillとFreespawn**
> ＋ **Priest Reanimation**
> ＋ **Conjuration 0の国家Revival**
> ＋ **Temple・Lab・Death Gem network**

です。

通常Recruitable troopとCommanderはありません。

したがって、一般国家の、

```text
Gold
→ Recruit
→ Army / Mage
```

という循環は使えません。

代わりに、

```text
Dominion
→ Freespawn

Priest turn
→ Reanimation

Death Gem
→ Priest / Mage / Commander revival
```

で戦力を作ります。

この違いを理解しないと、

- Goldを使わず余らせる
- Commander不足でFreespawnを動かせない
- PretenderのDeath Pathが足りずMageを増やせない
- Populationが死んだ後にTemple・Labを建てられない
- 無料兵を失っても平気だと思い、PriestとGemまで失う

という形で国家が止まります。

- [自動生成Recruitデータ](../../data/recruitment/ma/ermor.md)
- [国家別Site Search能力](../../data/site-search/ma/ermor.md)
- [Extended Magic Access](../../data/extended-magic-access/ma/ermor.md)
- [Magic Access Route](../../data/magic-access-routes/ma/ermor.md)
- [Undead・Reanimation・Popkill](../../systems/undead-popkill.md)
- [Pretender設計サンプル](../../pretender/samples.md)

!!! note "このページの精度範囲"
    本文はDominions 6.35の固定データ、国家Ability、National spell、ゲーム内表示、現行Inspector、Community referenceを照合した運用記事です。Dominion Freespawnの具体的構成、初期Army、Map、Pretender、Game設定、Random Eventで展開は変わります。現在のSpell requirementとUnit値はゲーム内表示と自動生成データを優先してください。

---

# 一言でいうと

```text
PretenderでDeath accessを用意する
→ National RevivalでPriest・Mageを得る
→ Dominionを広げFreespawnを増やす
→ Priest turnをReanimationへ変える
→ Temple・Lab・Gem incomeを守る
→ 無料兵でMapを埋め、MageとEliteで決戦する
```

国家です。

MA Ermorは、

> **Armyが無料に近い国家**

ではなく、

> **ArmyのCostがGoldから、Dominion・Commander・Priest turn・Gem・操作量へ移った国家**

と考えます。

---

# 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | Middle Age |
| Nation ID | 54 |
| Epithet | Ashen Empire |
| 通常Recruit | 兵士・Commanderともなし |
| 国家の中心 | Dominion Freespawn、Reanimation、National Revival |
| 主要Magic | Death、Revived Dusk ElderのCrosspath |
| 宗教 | Undead Priest、Unholy支援、Blood SacrificeではなくDominion spread |
| Population | 自国Dominion下で減少し、通常経済が崩れる |
| Supply | 多くのUndeadはNeed Not Eat。Living同行Unitは別 |
| 主な資源 | Death Gem、Temple、Lab、Priest turn、Undead Leadership |
| 操作量 | 非常に高い。Freespawn配属、Commander輸送、Reanimation管理 |
| 主な弱点 | Banishment、Holy、Anti-undead、Control、Commander kill、Gem遮断 |

---

# 国家固有Rule

## Land of Undeath

Ermor DominionはPopulationを殺し、Undeadを発生させます。

これは、

```text
Candleを増やす
＝ Populationと通常Incomeを破壊する
＝ 同時にFreespawn生産圏を広げる
```

という国家Ruleです。

通常国家のDominionはScalesを運ぶ宗教Networkですが、Ermorでは、

> **生産設備そのもの**

です。

## 通常Recruitがない

自動生成Recruitデータでは、Recruitable troop・Commanderが0です。

したがってFortを建てても、通常国家のようにMage queueが増えるとは限りません。

Fortの価値は、

- Temple・Lab保護
- Choke防衛
- Gem Site防衛
- Retreat point
- Siege delay
- Revival・Item集約拠点

です。

## Reanimation Rule

MA Ermorは、

- Priest Reanimation
- Undead Priest Reanimation
- H3+でLongdead Horseman
- H4+でLictor

へアクセスします。

高位Priestを得ることは、単にHoly Spellが増えるのではなく、**毎Turnの生産品が変わる**ことです。

---

# 国家Engine

```text
Pretender / 初期Caster
        ↓
National Revival
        ↓
Priest・Spectator・Dusk Elder
        ↓
Temple / Reanimation / Research / Site Search
        ↓
Freespawn・Gem income・Commander増加
        ↓
複数前線へUndead Army
```

## 第一の詰まり：Caster

National RevivalにはDeath casterが必要です。

主な国家Spellは、現在データでは、

| Spell | 要求 | 得るCommander |
|---|---:|---|
| Revive Acolyte | D2 | Acolyte of Eldregate H1 |
| Revive Bishop | D2 | Bishop of Eldregate H2 |
| Revive Arch Bishop | D3 | Arch Bishop of Eldregate H3 |
| Revive Spectator | D2 | Spectator D2 |
| Revive Dusk Elder | D3 | Dusk Elder F1 S1 D3＋Random |

です。

最初のD3 casterがいつ使えるかで、国家のResearchとCommander productionが決まります。

## 第二の詰まり：Death Gem

Revival casterがいても、Gemがなければ増やせません。

```text
最初のGem
→ 何をReviveするか
→ そのCommanderが何Turnで次のGem・Research・Priestを生むか
```

を比較します。

## 第三の詰まり：Undead Leadership

Freespawnが増えても、Commanderがいなければ前線へ送れません。

毎Turn、

```text
新規Freespawn数
現在のUndead Leadership
前線輸送Commander
予備Commander
```

を確認します。

---

# Pretender方針

MA ErmorのPretenderは、他国家より国家起動への影響が大きいです。

## Awake Death Bootstrap

### 解決するもの

- 早期National Revival
- Site Search
- Research開始
- Expansion支援
- Commander不足

### 必要条件

- D2～3以上へ届く
- Death Gemを使い切らない
- Pretender本人を危険なExpansionへ出しすぎない
- Revive後の役割分担を決める

### 失敗条件

- PretenderがBattleで死亡
- Death Gemがなく、Pathだけ余る
- ReviveしたMageを全員Researchへ置きPriest不足
- Expansionへ出し、国家唯一のCasterを失う

## Dormant / Imprisoned

Design Pointを得られますが、Pretenderが国家唯一の確実なDeath bootstrapなら、Revivalが遅れます。

選ぶ前に、

```text
Pretender不在中に
誰がCommanderを得るか
誰がResearchするか
誰がReanimateするか
```

をTestします。

## Dominion重視

DominionはFreespawn生産圏を広げます。

高Dominionは、

- Populationを早く殺す
- Freespawnを早く増やす
- Enemy Dominionへ押し込む

一方、Populationを使える期間を短くします。

## Missing Path

Revived Dusk ElderはF1 S1 D3にElemental・Sorcery Randomを持ちますが、Nature・Blood等は自然には安定しません。

Pretenderで、

- Nature：Regeneration、Poison、Supply、Mage summon
- Air：Shock対策、Storm、Cloud movement
- Water：Cold・Quickness・Water summon
- Glamour：Stealth・Illusion・Support

等を補う案があります。

ただし国家起動に必要なDeathを削らないことが先です。

---

# Expansion

MA ErmorのExpansionは、通常国家のRecruit queueではなく、

- 初期Army
- 初期Freespawn
- Pretender
- Revived Commander
- Undead Leadership

の組み合わせです。

## 出発条件

```text
□ Commanderが十分なUndead Leadershipを持つ
□ Mindless Unitを制御できる
□ 敵にPriestがいない
□ Magic Weaponが必要な相手ではない
□ Retreat先がある
□ Pretenderを失っても国家が動く
```

## Armyを急いで出しすぎない

Freespawn数が少ない段階で毎Turn小Armyを出すと、

- Commanderを多く使う
- 各Armyが薄い
- PDで削られる
- 再編が増える

ことがあります。

最初は一つの安全なExpansion Armyを作り、Commander supplyが増えた後に分割します。

## Indie Priest

Independent PriestやHoly Unitは、Undead Armyへ大きな交換効率を持ちます。

Scout報告だけでなく、Battle ReplayでBanishment数を確認します。

## Pretender Expansion

Pretender本人がExpansionする場合、

```text
一Province得る価値
vs
National Revivalが一Turn遅れる価値
```

を比較します。

Pretenderが唯一のD3 casterなら、Battleでの事故が国家Engine停止へ直結します。

---

# Freespawn Army

## Longdead系

Screen、Siege、PD処理、消耗戦へ使います。

装備差があるため、

- Shield
- Spear
- Sword
- Armor
- Horse

を一括評価しません。

## Soulless

CorpseのあるProvinceで生産価値が上がります。

低Combat statsでもHP・Size・数を利用し、Mageへ時間を渡します。

## Ghoul

Populationを消費する場合があります。

Populationが残る時期とDominion spreadを調整します。

## Longdead Horseman

Map Control、Flank、Raidへ使います。

H3+ Priest turnと交換するため、通常Longdeadとの生産比率を決めます。

## Lictor

Sacred Elite Undeadとして、通常Freespawnでは倒しにくい相手へ使います。

H4+ Priest turnを使うため、

```text
Lictorを作る
vs
Dominion・Throne・BattleへPriestを使う
```

交換があります。

---

# Commander / Mage

## Acolyte・Bishop・Arch Bishop

主な役割は、

- Reanimation
- Unholy支援
- Dominion
- Throne Claim
- Army leadership

です。

低位Priestを日常Reanimation、高位PriestをLictor・Battle・Throneへ分けます。

## Spectator

D2のSpectral Commanderです。

- 次のRevival
- Death Site Search
- Battle support
- Stealth / Ethereal運用

へ使えます。

国家唯一のD2 chainを前線で失わないようにします。

## Dusk Elder

Dusk Elderは、

```text
F1 S1 D3
＋100%でF/A/W/E/S/Dから+1
＋10%追加Random
```

を持つ国家の主要Mageです。

### 分類

```text
D4以上
→ 高位Death、Mage revival、Global・Ritual候補

S2以上
→ Astral support、Booster、MR攻撃

F2以上
→ Fire support、Forge、Anti-chaff

A1 / W1 / E1
→ Resistance、Crosspath、Booster入口
```

Rare Random個体を通常Skeleton spamへ使い捨てず、国家技術へ残します。

## Hero

Heroは保証されません。

Wraith King、Forgotten King、Dusk Elder hero等は国家上限を大きく上げますが、

```text
Heroが来る前提
```

でResearch routeを組みません。

---

# Magic Access

## Native保証とRevivalを分ける

自動生成Accessでは通常Recruitは0です。

Revived Dusk Elder等はNational spellで得るため、

```text
Pathを持つ
＋
CasterをReviveするGemとTurnがある
```

ことが必要です。

## Death

Deathは、

- Mage revival
- Reanimation支援
- Skeleton
- Undead summon
- Darkness
- Fatigue・Death battlefield
- Remote ritual

の中心です。

## Astral

Dusk ElderのAstralは、

- MR attack
- Antimagic
- Teleport / Returning系
- Booster
- Magic Duel対策

へ使います。

高S個体を一か所へ集めません。

## Elemental Random

F/A/W/E randomは、

- Resistance
- Army-wide buff
- Elemental summon
- Booster
- Crosspath Item

へ使います。

一体のRare Mageへ国家全体を依存しないよう、複数個体を保存します。

---

# Research方針

## 起動段階

最初はNational Revivalと基礎Death運用を優先します。

Conjuration 0の国家SpellはResearch不要でも、CasterとGemが必要です。

## Conjuration

- Undead summon
- Mage summon
- Elemental
- Spectral Commander
- Army量の変換

へつながります。

## Enchantment

- Undead強化
- Darkness
- Protection
- Battlefield fatigue
- Army-wide support

を検討します。

## Thaumaturgy

- Site Search
- MR attack
- Control
- Soul・Mind系

へ進みます。

## Construction

- Black Laurel
- Death booster
- Resistance Item
- Research Item
- Commander保護

へ使います。

## Evocation

Freespawnでは倒しにくい、

- 高Protection
- Regeneration
- Priest blob
- Elite Sacred

へ直接Damageを足します。

---

# First War

## 戦争目的

MA Ermorは低Income Provinceを多く取ること自体が目的ではありません。

優先Targetは、

```text
Temple
Lab
Fort
Magic Site
Throne
Enemy Priest production
Gem income
```

です。

## Armyを三層にする

```text
層1：Freespawn Screen
層2：Lictor・Horseman・Damage Summon
層3：Priest・Dusk Elder・Support Mage
```

Freespawnだけを増やしても、敵の高Protection・Regeneration・Holyへ止まります。

## 複数方向へ圧力

無料兵の数を活かし、

- Main Army
- Siege Army
- Raid Army
- Commander transport

を分けます。

ただしMageとHigh Priestを分散しすぎて、どのBattleでも勝利条件がない状態を避けます。

---

# Battle Script

## Priest support

```text
Unholy protection / power系
→ 必要ならBless
→ 後方維持
```

目的はFreespawnの一体性能を上げるより、前線が崩れるRoundを遅らせることです。

## Dusk Elder support

```text
Self path boost / defence
→ Army support
→ 敵防御に合うDeath・Astral・Elemental spell
→ Cast Spells
```

Rare Crosspath個体へ、通常D3個体と同じScriptを貼り付けません。

## Anti-Priest

```text
Fast / Horseman Squad
→ Attack Rear / closest適切Target

Mage
→ Priest blobへAoE / MR / fatigue
```

Banishment casterを放置すると、Freespawn数が敵火力へ変わります。

---

# Counterされるもの

| 相手の手段 | なぜ危険か | 対応 |
|---|---|---|
| Banishment | 低HP Undeadをまとめて処理 | Priestを先に狙う、散開、Elite混成 |
| Holy / Anti-undead | 分類Counter | Non-undead summon、Mage、遠隔圧力 |
| Control Undead | 自軍Eliteが敵Armyへ変わる | MR、Antimagic、Target分散 |
| Fire・AoE | 密集Freespawnへ高効率 | Formation、Resistance、複数Army |
| Trample | Small Chaffを一方的に処理 | Large Undead、高Damage、拘束 |
| Commander kill | Mindless Armyが機能停止 | Commander分散、Bodyguard、予備 |
| Gem route cut | Mage・Revival生産停止 | Site防衛、輸送分散、予備Gem |
| Dominion pressure | Freespawn生産圏を縮小 | Temple、Priest、複数宗教Front |
| Fast Raid | 後方Temple・Labを破壊 | Mobile reserve、Fort、Scout |

---

# Siege

## 壁を削るArmy

大量Freespawnを使います。

## Storm Army

Fort内のMage・Priest・Eliteを倒すため、

- Lictor
- High-quality summon
- Dusk Elder
- Priest support
- Magic Weapon

を別に用意します。

## Relief対策

Siege中、敵Relief Armyが来ると、Freespawnが外側Battleで崩れStormできません。

Scoutと予備Armyを置きます。

---

# Map Control

## Temple Network

TempleはDominionとFreespawnの生産Nodeです。

Border Templeを失うことは、Province一つ以上の損失です。

## Lab Network

LabはDeath Gemを、

```text
Revival
→ Mage
→ Research / Battle
```

へ変える設備です。

## Popkill Border

敵はErmor Dominionを嫌い、Border交渉が難しくなります。

自国Dominionが相手Populationを殺すため、戦争前から脅威と見なされます。

外交では、

- Dominion方向
- Temple位置
- NAP
- Throne
- 共同Anti-Ermor連合Risk

を確認します。

---

# Multiplayer

## 脅威認識

Ermorは時間とDominionでArmyが増えるため、実際の兵数以上に警戒されます。

外交で、

```text
今は弱い
```

と主張しても、将来のPopkillとFreespawnが評価されます。

## 早い包囲網

複数国がTemple・Labを同時に狙うと、無料兵が多くてもMageとCommanderが足りません。

一方向で決着し、他方向はFort・Chaffで遅延します。

## 取った土地の価値

敵がErmor領を奪ってもPopulationが死んでおり、戦利品が少ない場合があります。

これは防御ですが、味方へ譲れる価値も低いことを意味します。

---

# よくある失敗

## PretenderのDeath accessを軽視

National Revivalが遅れ、Research・Priest・Commanderが増えません。

## Goldを使わない

Populationが死んだ後、Temple・Lab・Fortを建てられません。

## Freespawnを未配属Poolへ放置

Army数は増えても前線へ届きません。

## 全PriestをReanimationへ使う

Dominion、Battle support、Throne Claimが止まります。

## Dusk ElderのRandomを分類しない

Rare Crosspathを通常Mageとして失います。

## 無料兵だけでFirst Warへ行く

敵の高Protection・Holy・AoEへ勝利条件がありません。

## 一Armyへ全Commanderを集める

Remote・Assassin・rear attackで国家生産力をまとめて失います。

## Populationを通常経済として守ろうとする

Ermor Dominion自体がPopulationを殺します。Temple・Lab・Siteへ価値を移します。

---

# Test gameで記録するもの

```text
Turn 1のCaster：
最初のD2 / D3：
最初にReviveしたCommander：
二人目のMage完成Turn：
最初のTemple：
最初のLab：
ProvinceごとのFreespawn量：
Undead Leadership不足Turn：
第一Expansion開始Turn：
第一Research Breakpoint：
Lictor生産開始Turn：
Death Gem income：
First war時のPriest / Mage / Commander数：
Banishmentに失ったUnit数：
```

---

# 毎Turn Checklist

```text
□ FreespawnをCommanderへ配属した
□ Undead Leadershipを確認した
□ Death GemのRevival用途を決めた
□ PriestをReanimation・Dominion・Battleへ分けた
□ Temple・Lab・Fortを建てるGoldを使った
□ Dusk Elder Randomを分類した
□ Site SearchとGem輸送を確認した
□ 敵Priest・Holy・Control spellをScoutした
□ Siege ArmyとStorm Armyを分けた
□ Pretenderを失ってもRevival chainが残る
```

---

## 関連ページ

- [Undead・Reanimation・Popkill](../../systems/undead-popkill.md)
- [Dominion](../../systems/dominion.md)
- [Forts](../../systems/forts.md)
- [Death](../../magic/paths/death.md)
- [Holy](../../magic/paths/holy.md)
- [戦闘ルール](../../basics/combat-rules.md)
- [命令とBattle Script](../../basics/orders.md)
- [Pretender設計サンプル](../../pretender/samples.md)
- [Reanimationデータ](../../data/units/reanimation.md)
- [国家Freespawnデータ](../../data/units/nation-generation.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [MA Ermor community reference](https://illwiki.com/dom5/dom6/ermor-ma)
