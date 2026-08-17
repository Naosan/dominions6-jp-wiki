---
title: LA Man
page_type: nation-guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
nation_id: 100
era: "LA"
epithet: "Towers of Chelms"
---

# LA Man — Towers of Chelms

LA Manは、**豊富な人間兵、長射程射撃、Fort建設能力、Drainへ強い研究者、広いが低いMagic Accessを組み合わせる国家**です。

MA Manのように「分かりやすいAir・Nature国家」ではありません。Old Magicは衰退し、国家の中心はWitchではなくMagisterへ移っています。

そのためLA Manは、

> **兵種を選別する**
> ＋ **Longbow・Crossbowと前衛を分業する**
> ＋ **Unhindered ResearcherでDrainを利用する**
> ＋ **MasonをFort networkへ変える**
> ＋ **Random Mageの当たり外れを国家計画へ組み込む**

ことで強くなります。

選択肢が多いため、最初から簡単な国家ではありません。しかし、

- 兵種の役割分担
- 射撃とFriendly Fire
- Commander Point
- Fort upgrade
- Research economy
- Random Pathの扱い
- Low-path Mageを数で使う方法

を学ぶ基準国家として非常に有用です。

> **LA Manは、強い一種類をSpamする国家ではなく、安い選択肢と高価な選択肢を必要な場所へ正しく配る国家です。**

- [自動生成Recruitデータ](../../data/recruitment/la/man.md)
- [国家別Site Search能力](../../data/site-search/la/man.md)
- [Extended Magic Access](../../data/extended-magic-access/la/man.md)
- [Magic Access Route](../../data/magic-access-routes/la/man.md)
- [Pretender設計サンプル](../../pretender/samples.md)

!!! note "このページの精度範囲"
    本文はDominions 6.35の固定データ、ゲーム内Nation・Unit・Spell・Item表示、公式Documentation、現行Inspector、およびDom6 Community資料を照合して再構成しています。Magister系のRandom Path、Hero、National Summon、Pretender、Map、Research設定により到達できる戦術は変わります。正確なCost・装備・Random率は上記の自動生成データを優先してください。

---

# 一言でいうと

```text
安い前衛と射撃でExpansion
→ FortとMagisterを増やす
→ DrainをDesign Pointへ変える
→ Air・Earth・Astral supportを数で揃える
→ Mason・Siege・Castle Defenceで戦線を固定
→ 欠けるNature・Water・BloodをPretender等で補う
```

国家です。

---

# 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | Late Age |
| Nation ID | 100 |
| Epithet | Towers of Chelms |
| 軍事の中心 | Infantry、Longbow、Crossbow、Knight、Fort defender |
| Magicの軸 | Air、Earth、Astral、Glamour、Holy |
| 条件付きAccess | Fire、Death、追加Air・Earth・Astral・Glamour |
| 大きな欠落 | Water・Nature・Bloodの安定Recruit access |
| 研究特徴 | 主要研究者にUnhindered Researcher |
| Scale特徴 | Drain limitに国家補正 |
| Fort特徴 | Capitalが高Tier、MagisterがMason・Siege・Castle Defenceを持つ |
| Capital-only | Lord Warden、Warden等 |
| 操作量 | 中～高。Roster選択、Random Mage、射撃、Fort運用 |
| 主な弱点 | Mageの個体差、低Path、Friendly Fire、欠落Path、Old Age |

---

# 国家エンジン

LA Manの循環は、次のようになります。

```text
役割別の安価な兵でExpansion
        ↓
IncomeとFort候補を増やす
        ↓
Magister・Magister Arcaneを継続雇用
        ↓
Unhindered ResearcherでDrain下でも研究
        ↓
MasonでFort networkを強化
        ↓
Longbow・Crossbow・Earth / Air supportをArmy化
        ↓
敵Fortを包囲し、Castle Defence・Reliefで新Borderを維持
```

この国家エンジンの本体は、Capital-only Wardenや一人のA3 Mageではありません。

> **Fort数 × Commander Point × 継続雇用する研究者数**

です。

---

# 強み

## 1. 兵種の選択肢が多い

LA Manには、

- 安価なSpearman・Longspear
- 高Damage Axeman
- Light Archer
- Crossbowman
- Longbowman
- Tower Guard・Defender
- Tower Knight
- Stealthy Forester
- Sacred Warden

があります。

これは初心者には迷いやすい反面、相手に合わせてArmyを変えられる強みです。

```text
敵が軽装・密集
→ Longbow・Archer

敵が重装
→ Crossbow・高Damage Axeman・Magic

敵がCavalry・Large
→ Longspear・Formation・Earth support

敵が射撃中心
→ Tower Guard・Defender・Knight

後方が薄い
→ Forester・Stealth Commander
```

と役割を変えます。

## 2. Longbow・Crossbowを同時に持つ

Longbowは射程と射撃密度、Crossbowは高Protectionへの一撃を担当します。

両方を持つことで、

- 軽装多数
- ShieldなしMage
- 高Protection Infantry
- Giant・Large Target

へ別の射撃回答を用意できます。

ただし射撃を増やすほどFriendly FireとStorm・Arrow protectionへの依存も増えます。

## 3. Unhindered Researcher

Judge、Magister、Magister Arcane等の主要研究者はUnhindered Researcherを持ち、Drainの研究Penaltyを受けにくい国家です。

そのためPretender設計でDrainを取り、得たDesign Pointを、

- Order
- Productivity
- Growth
- Dominion
- Magic Path
- Bless

へ回せます。

ただし、

- Pretender
- Independent Mage
- Summon Mage
- Hero
- Battle spellのFatigue・環境

まで同じように無視するとは限りません。

> **国家研究者がDrainへ強いことと、国家全体がDrainの全影響を無視できることは別です。**

## 4. MasonによるFort運用

MagisterはMason、Siege Bonus、Castle Defenceを持ちます。

これは一人で、

- Research
- Fort建設・upgrade
- Siege
- Fort defence
- Spy
- Stealth

を兼ねられることを意味します。

Masonの価値はWallだけではありません。

- Commander Point
- Recruitment Point
- Administration
- Supply Storage
- Base Defenders

のBreakpointを上げ、毎Turnの生産量を増やします。

## 5. Capitalが高Tier Fort

Capitalは高TierのFortを持ち、序盤からCommander・兵・Resources・防御に優れます。

Capitalを単なる安全地帯として使うのではなく、

- 高価なMagister Arcane
- Capital-only Warden・Lord Warden
- Research core
- ItemとGemの集積

をどう配分するかが重要です。

## 6. Air・Earth・Astralの複合Support

Magister ArcaneはAirを軸にEarth・Astralを持ち、RandomでFire・Air・Earth・Astral・Glamour等へ広がります。

この組合せは、

- 射撃支援
- Shock
- Protection・Strength
- MR・Antimagic
- Teleport・Magic Phase
- Communion外の低Path支援
- Booster・Crosspath Item

へ接続します。

高Path一人に依存するより、複数のMagister Arcaneへ役割を分けます。

## 7. Fort戦が得意

Tower Guard・DefenderはCastle Defenceを持ち、MagisterもCastle Defence・Siege Bonusを持ちます。

そのため、

- 自Fortの壁を維持する
- 敵Fortの壁を壊す
- Relief Armyまで時間を買う
- Storm守備を厚くする

戦いに向きます。

---

# 弱み

## 1. Rosterが多く、間違った兵も大量生産できる

選択肢が多いことは、

> 何となく全兵種を均等に作る

失敗を生みます。

LA Manでは、Turnごとに、

```text
誰が最初に受けるか
誰が敵Protectionを抜くか
誰が射撃するか
誰が側面を守るか
誰がSiegeするか
```

を決めます。

## 2. MageのPathが不安定

MagisterやJudgeはMagicを持たない個体も存在し、Magister ArcaneのRandomも必要なPathへ必ず出るわけではありません。

したがって、

- Researcherとしての平均価値
- Magicを持たない個体の別用途
- Rare Path holder
- Battle Mage
- Mason・Spy

へ雇用後に分類します。

## 3. Magister Arcaneが高価

Magister Arcaneは強いMageですが、Gold Costが高く、Commander PointとUpkeepも国家経済へ負担を与えます。

毎Fortで無条件に雇うのではなく、

```text
研究用Magister
＋ 戦闘用Magister Arcane
＋ Fort作業用Magister
```

の比率を決めます。

## 4. Water・Nature・Bloodが安定しない

LA ManはRecruitable MageだけではWater・Nature・Bloodへ安定して入れません。

これは、

- Quickness・Water Elemental
- Regeneration・Poison Resistance・Supply
- Blood economy・Sabbath

の利用を難しくします。

Pretender、Hero、Independent Mage、Magic Site、Summon Mageを使って補います。

## 5. Low Pathの幅はあるが、Boosterへ自然につながらない

A3・E2・S2等の個体は得られますが、すべてのGameで同じCrosspathとBooster chainが揃うわけではありません。

「理論上はRingへ届く」と「現実的なTurnに量産できる」は別です。

[Magic Access Route](../../data/magic-access-routes/la/man.md)で、

- 確率
- Research
- Gem
- Unique Item
- Pretender依存

を確認します。

## 6. 射撃とCavalryが互いを邪魔しやすい

Longbow・Crossbowを大量に置き、Tower Knightを早く接敵させると、味方射撃がKnightや前衛へ当たることがあります。

- Squad分割
- Hold
- Target order
- 配置
- 射撃停止Timing

をReplayで確認します。

## 7. Old Age

Magister ArcaneやBishop等にはOld Ageが関係します。

長期Gameでは、

- Disease
- Affliction
- 重要Random Pathの突然死
- Booster chainの断絶

を考えます。

Rare Path一人へ国家計画を依存せず、複数個体・Pretender・Summonで代替を用意します。

---

# 国家固有要素

## Drain Limit補正

LA Manは通常より強いDrainを選べる国家です。

これは「Drainを必ず最大にする」という意味ではありません。

比較するもの：

```text
得るDesign Point
→ Order / Productivity / Growth / Pathへ何を買うか

失うもの
→ Pretender・Indie Mage・Summon Mage・Battle環境
```

です。

国家研究者の多くがUnhindered Researcherであるため、Scales型Pretenderの候補になります。

## MagisterのMason

Masonは国家のFort typeを一段上へ押し上げられる場合があります。

Upgrade前に、

- Commander Pointが増えるか
- Mage生産が毎Turn増えるか
- Wallだけが増えるか
- 敵が何Turnで到着するか
- MagisterのResearch turnを使う価値があるか

を見ます。

## National Summon

LA Manには、Black Dog、Cu Sidhe、Barghest、Unicorn、Bean Sidhe等の国家・系譜Summonがあります。

しかし要求Pathへ自然に届かないものもあります。

> **国家Spellが存在することと、通常Recruitだけで安定してCastできることは別です。**

Pretender・Hero・Summon Mageを含むAccess routeを先に確認します。

---

# 兵士

正確なCost・装備・Statsは[Recruitデータ](../../data/recruitment/la/man.md)を参照してください。

## Spearman

安価な数と槍を提供します。

- Chaff
- Giant・CavalryへのSquare密度
- Siege
- Archerの前Screen

として使います。

単体性能を期待せず、Longbow・Mageが働く時間を買います。

## Longspear

長い武器によるRepelと間合いを持つ前衛候補です。

- 低Morale・低Attack相手
- Cavalry・Large Unit
- Choke

へ意味があります。

高Protectionを抜くDamage役とは別に扱います。

## Axeman・Heavy Axeman

高Damage武器で敵Protectionへ圧力を掛けます。

- Heavy Infantry
- Giant
- Regenerationを上回る一撃

へ向きます。

Shieldが弱い・ない型では、射撃と高Defence相手に損失が増えます。

## Light Archer

安価に射撃数を増やす兵です。

- 軽装
- Shieldなし
- Large Target
- Chaff

へ使います。

High Protectionへ弾数だけを増やしても効果が低い場合があります。

## Crossbowman

高Protectionへ射撃で回答します。

主なTarget：

- Heavy Infantry
- Knight
- Giant
- Thugの低Defence形態

注意：ReloadとFriendly Fireがあるため、敵前衛へ味方が接敵した後の射撃効率をReplayで確認します。

## Longbowman

LA Manの代表的な射撃兵です。

- 長い射程
- 高いPrecision傾向
- 射撃密度
- Army-wide Air supportとの相性

が強みです。

ただし、

- Shield
- Protection
- Storm
- Arrow protection
- Flying・Attack Rear

へ対策されます。

## Tower Guard

安価な一般兵より高い装備とCastle Defenceを持つ守備兵です。

- Fort defence
- Archer Screen
- Choke
- Commander保護

へ使います。

前線で大量に消耗させるより、Fort・重要拠点で時間を買う価値もあります。

## Defender

高いResource CostとCastle Defenceを持つ精鋭防御兵です。

- Storm defence
- Fort Relief
- 高価値Mageの前衛
- 狭い戦場

に向きます。

GoldだけでなくResources・Recruitment Pointsを使うため、Fort立地を選びます。

## Forester

Forest Recruit可能なStealthy兵です。

- Scout網
- Raid
- Patrol補助
- Forest戦線
- Stealth Commanderとの小部隊

に使います。

Main Armyの正面性能だけで評価すると価値を見落とします。

## Tower Knight

高価な重騎兵で、突破・側面・Shock attackを担当します。

- Archer・Mage後衛への圧力
- 開けた戦場
- 低Damage兵の突破
- Mobile Reserve

に向きます。

Crossbow・Longbowの射線へ自分から入らないよう、SquadとTimingを分けます。

## Warden

Capital-only Sacred・StealthyのElite兵です。

- Stealth strike
- Bodyguard
- Sacred Shock troop
- Forest route

へ使えます。

供給量が限られ、Gold・Resourcesも重いため、Heavy Blessの対象数とScales損失を比較します。

---

# Commander・Mage

## Royal Forester

通常Scoutより高価ですが、Stealth・Patrol・Forest Survivalと少数兵の指揮を両立します。

- Border偵察
- Forester Raid
- Patrol
- Itemを持たない情報役

として使います。

## Castellan

通常Armyの安価なCommanderです。

MageをLeadershipへ使わず、Castellanに兵を預けます。

## Judge

Lab不要で雇えるUnhindered Researcher・Patrollerです。個体によってFireまたはDeath等のMagicを得ますが、Magicなしも存在します。

### MagicなしJudge

- Research
- Patrol
- Commander
- 後方管理

に使います。

### MagicありJudge

- Site Search
- Fire・DeathのCrosspath
- Skull系Item
- Reanimation・Battle support

へ使います。

Lab不要という性質は、Fort完成前・僻地・Blood対策Patrolで特に価値があります。

## Magister of Theology

H1 Sacred・Inquisitorです。

Enemy Dominionを押し返すLocal役として、通常H1以上の価値を持ちます。

- Border Preach
- Temple defence
- Banishment
- Sermon

へ使います。

## Bishop

H2の上位Priestです。

- Prophet候補
- Sermon of Courage
- Banishment
- Throne Claimへの補助
- Dominion defence

を担当します。

Old Ageと前線生存に注意します。

## Magister

LA Manの重要な多目的Commanderです。

- Unhindered Researcher
- Mason
- Siege Bonus
- Castle Defence
- Spy
- Stealth
- Random Magic

を持ちます。

Magicなしでも仕事があります。

```text
Magister A：Research
Magister B：Fort upgrade
Magister C：Siege
Magister D：Spy・Stealth
Magister E：Random PathのSite Search
```

へ分けます。

## Magister Arcane

Air・Earth・Astralを持つ主力Mageです。

主な役割：

- Research
- Air・Earth Army support
- Astral utility・MR defence
- Random Pathによる高Path個体
- Battle magic
- Forge・Ritual

高価なので、何人をResearchへ残し、何人をFirst warへ出すか決めます。

### Random個体の扱い

- A3：Air主力・射撃支援・Shock
- E2：Earth Buff・Forge
- S2：Astral support・Magic Duel環境
- G1：Glamour utility・Site Search
- Crosspath：UniqueなItem・Spell route

として保護します。

## Lord Warden

Capital-onlyのGlamour・Holy、Sacred、Stealthy Combat Casterです。

- Warden指揮
- Bless
- Stealth Army
- Glamour Site Search
- Thug候補

に使えます。

ただしGold・Commander Pointを使うため、通常Commanderとしてだけ雇うのは高価です。

---

# Magic Access

## 確実な軸

- Air：Magister Arcane
- Earth：Magister Arcane
- Astral：Magister Arcane
- Glamour：Lord Warden
- Holy：Bishop・Priest系

## Random・条件付き

- Fire：Judge・Magister Arcane等
- Death：Judge等
- 追加Air・Earth・Astral・Glamour：Magister Arcane

## 欠落

- Water
- Nature
- Blood

を通常Recruitだけで安定して用意できません。

## Path別の主な役割

| Path | 主な用途 | 国家内の制約 |
|---|---|---|
| Air | 射撃支援、Shock、Storm、移動 | 高Path個体はRandom依存 |
| Earth | Protection、Strength、Forge、Fort戦 | E2個体を保護 |
| Astral | MR、Antimagic、Teleport、Magic Duel | S1個体の消耗に注意 |
| Glamour | Stealth、Illusion、Luck、Control | 確実なGはCapital-only |
| Fire | Fire Resistance、範囲Damage、Forge | Judge等のRandom |
| Death | Reanimation、Summon、Fear | D2以上へ自然に届きにくい |
| Nature | Poison・Supply・Regeneration | Pretender・Indie・Summonが必要 |
| Water | Quickness・Cold・海 | 外部Accessが必要 |
| Blood | Blood economy・Sabbath | Hero等を除き標準Accessなし |

## Magic Accessの運用原則

```text
毎Game確実に使うPlan
＝ A2 E1 S1を中心に作る

Randomが出たら追加するPlan
＝ A3 / E2 / S2 / G1 / F1 / D1

Pretenderで買うPlan
＝ Nature・Water・Blood・高Path bridge
```

と分けます。

---

# Pretender方針

## Plan A：Imprisoned Scales / Drain利用

### 向く状況

- 国家兵だけでExpansionできる
- Fortと研究者を増やすほど強くなる
- Capital-only SacredへHeavy Blessを必要としない
- Long game

### 買うもの

- Order・Productivity・Growth
- Dominion
- 欠落Path

### 特徴

Unhindered ResearcherによりDrainの研究Penaltyを軽減し、Design Pointを経済へ回します。

### Test

- Capitalで何兵種を何体作れるか
- 第二Fort開始Turn
- MagisterとMagister Arcaneの比率
- Pretender不在中のNature・Water対策

## Plan B：Dormant Rainbow / Missing Path Bridge

### 向く状況

- First warまでは国家兵・A/E/Sで戦える
- MidgameにNature・Water・Death・Glamour等が必要
- National Summon・Booster routeを開きたい

### 買うもの

- Poison Resistance・Supply
- Water・Nature Summon
- Global・Forge bridge
- Site Search

### Test

```text
登場後最初のForge：
最初のRitual：
最初に補うResistance：
First warへ間に合うか：
```

を埋めます。

## Plan C：Light Bless＋Scales

WardenとLord Wardenへ小さなBlessを与えつつ、通常兵・Mage economyを維持します。

候補となる役割：

- Survival
- MR
- Reinvigoration
- Morale
- Stealth部隊の持久力

Heavy Blessより、通常Army全体をResearchとScalesで支える設計です。

## Plan D：Awake Expander

LA Manの兵だけでExpansionが不安定なMap、早い第二Fortが必要なGameでは候補です。

ただし、

- Strong Scales
- Drain利用
- Missing Path

を同時に取りづらくなります。

Awake Expanderが取る追加Province数と、弱いEconomyの長期損失を比較します。

---

# 序盤拡張

LA ManはRosterが多いため、Expansion Armyを一種類に固定しない方が安定します。

## Plan 1：Shield・Spear Screen＋Longbow

```text
前：Spearman / Tower Guard等
後：Longbowman
Commander：Castellan
```

軽装・低ShieldのIndependentへ向きます。

### 注意

- Cavalry Charge
- Archer counter-fire
- 接敵後のFriendly Fire

を確認します。

## Plan 2：Screen＋Crossbow

High Protection相手へ使います。

```text
前：安価な槍兵
後：Crossbowman
側面：高Damage Axeman
```

CrossbowがReload中に前衛が崩れないよう、人数と配置を調整します。

## Plan 3：Tower Guard / Defender中心

損失を抑えたい危険Provinceへ使います。

Resourcesが重いため、すべてのExpansion Armyを精鋭化しないでください。

## Plan 4：Tower Knight

低Damage・低数の相手を速く崩します。

- Chargeを受ける敵
- Archer後衛
- 広い戦場

に強い一方、Lance・Crossbow・高Damage・Trample・Friendly Fireへ注意します。

## Independent別

### Light Infantry

Longbowと通常前衛で処理します。

### Heavy Infantry

Crossbow、高Damage Axeman、Earth supportを使います。

### Cavalry

LongspearとScreenでChargeを受け、Knight・Crossbowで返します。

### Archer

Tower Guard・Defender等の装備を使い、軽装Damage兵を後ろへ置きます。

### Barbarian

高Damage一撃を安価Screenへ受けさせ、射撃で数を減らします。

### Undead

Bishop・Priest、Morale、長期戦を確認します。

## 二軍への分割

分割条件：

- 両軍に前衛がある
- 両軍にDamage sourceがある
- Commanderがいる
- Friendly Fireを管理できる
- 安全な標的が二つある

弓兵だけ、Knightだけの二軍を作らないようにします。

---

# Economy・Fort計画

## Capitalの役割

Capitalでは、

- Magister Arcane
- Lord Warden
- Warden
- Tower Knight・精鋭兵
- Research core

が競合します。

毎Turn、Commander PointとResourcesを何へ使うか決めます。

## 第二Fort

LA Manの第二Fortは、Mage生産とFort networkの開始です。

候補：

1. High IncomeでMagisterを維持できる
2. ResourcesがありDefender・Knightを作れる
3. Frontlineへ近い
4. Capitalと別方向へRetreat routeを作る
5. MasonでUpgradeする価値がある

## Fortの役割分担

```text
Capital：Magister Arcane・Capital-only
Mage Fort：Magister・Judge・Arcane
Resource Fort：Defender・Knight・Tower Guard
Border Fort：Castle Defence・Relief
Relay Fort：Lab・Gem・Item・Retreat
```

と分けます。

## MasonのOpportunity Cost

MagisterがFortをUpgradeしているTurnはResearchしません。

```text
失うResearch
対
今後増えるCommander Point・生産・Wall
```

を比較します。

## Drain Economy

Drainで得たPointを、

- OrderでGold
- ProductivityでResources
- Growthで長期Income
- DominionでScale定着

へ変えます。

Drainを取っただけで、他Scaleが弱いなら国家エンジンは完成しません。

---

# Researchルート

LA Manは、Schoolを広く少しずつ上げると何も完成しません。

First war用の第一Breakpointと、Counter用の第二Breakpointを分けます。

## Route A：射撃Army支援

目的：Longbow・Crossbowの命中・生存・戦場条件を改善する。

主な役割：

- Precision
- 射撃範囲・命中
- Enemy射撃対策
- Wind・Storm環境
- Shock Damage

使用Mage：主にAir個体。

### 注意

Storm系の戦場条件は、自軍Longbowを止める場合もあります。

> 敵射撃を止めるSpellと、自軍射撃を強くするPlanを同じBattleで混同しない。

## Route B：Earth Infantry support

目的：安価な人間兵をProtection・Strengthで実戦水準へ上げる。

- 前衛Protection
- Axeman・KnightのDamage
- Fort・Siege支援
- Counter Item

を担当します。

E1個体は戦闘中のPath boostを前提にする場合があるため、接敵Timingを調整します。

## Route C：Astral utility・MR defence

目的：

- Antimagic・MR
- Body Ethereal・Luck等の防御層
- Teleport・Magic Phase
- Enemy MageへのControl

を使うことです。

S1 Mageを大量に前線へ出すとMagic Duel環境で消耗するため、敵Astral数を確認します。

## Route D：Construction・Research economy

Air・Earth・AstralのCrosspathを使い、

- Research Item
- Booster
- Resistance Item
- Commander保護

へ進みます。

Magisterを増やす国家なので、Research Item一個の価値ではなく、

```text
Forgeに使うMage turnとGem
対
残りGameで得るResearch
```

を比較します。

## Route E：National Summon bridge

Black Dog、Cu Sidhe、Barghest、Unicorn、Bean Sidhe等は、

- Stealth戦力
- Sacred Summon
- Assassin・Fear
- Magic Access拡張

を提供します。

ただし要求Pathへ届く方法を先に確保します。

```text
Spellを研究
＋ Caster
＋ Path
＋ Gem
＋ Terrain条件
```

が揃って初めてPlanです。

研究レベルと要求Pathは[Spellデータ索引](../../data/spells/index.md)で現行値を確認してください。

---

# 重要Spell・運用テーマ

| 問題 | 主な回答 | 注意 |
|---|---|---|
| 軽装多数 | Longbow、Air damage | Shield・Storm |
| 高Protection | Crossbow、Earth・Astral、Magic | Friendly Fire |
| Giant | Longspear、Crossbow、Fatigue | Square密度 |
| Archer | Tower Guard、Air defence | 自軍射撃との両立 |
| MR attack | Astral、Antimagic、MR Item | S1消耗 |
| Poison | Pretender・Nature外部Access、Item | 国家の大きな欠落 |
| Flying・Rear | Bodyguard、分散、Knight reserve | Commander集中を避ける |
| Thug・SC | Crossbow、Astral、Earth、Counter Item | 単一Damageへ依存しない |

---

# Magic Item

## 優先順位

1. Missing Pathを開くBooster
2. Poison・Shock等のResistance
3. Research Item
4. Rare Random Mageの保護
5. Counter-thug・SC対策

です。

## Air Research Item

Air Mageを多く雇う国家では、Research Itemが長期的な価値を持ちます。

ただし、

- Forge Gem
- Forge turn
- そのMageを前線へ出す機会費用
- Game残りTurn

を比較します。

## Rare Crosspath Item

理論上ForgeできるUnique Itemを国家標準Planにしないでください。

必要個体、複数Booster、Unique競合がある場合は、

```text
出れば使う上振れPlan
```

として扱います。

---

# Army構成

## 1. Longbow Combined Arms

```text
前衛：Spearman / Tower Guard
第二線：Axeman / Defender
後衛：Longbowman
側面：Tower Knight
Mage：Air射撃支援、Earth前衛支援
```

勝利条件：

> 接敵前に射撃で敵数を減らし、前衛が固定した相手をAxeman・Knight・Mageで処理する。

## 2. Crossbow Anti-Armor

```text
前：安価なScreen
後：Crossbowman
Mage：Earth / Astral support
Reserve：KnightまたはDefender
```

射線とReloadを考え、Screenを薄くしすぎないようにします。

## 3. Fort Defence Army

```text
Tower Guard・Defender
＋ MagisterのCastle Defence
＋ BishopのMorale・Holy
＋ Short-range Mage
＋ Relief Army
```

でFortを時間資源へ変えます。

## 4. Stealth / Forest pressure

```text
Royal Forester / Magister / Lord Warden
＋ Forester / Warden
＋ Glamour support
```

を使い、敵後方へ圧力を掛けます。

Main ArmyからCapital-only Wardenを抜きすぎないようにします。

---

# Battle Script

## Air support例

```text
Self Path boost
Precision /射撃支援
Shock / Control
Cast Spells
```

自軍射撃を維持するか、Storm等で戦場を変えるかを先に決めます。

## Earth support例

```text
Self Path boost
Protection
Strength
Control / Damage
Cast Spells
```

## Astral support例

```text
MR / Antimagic
Defensive utility
Control
Cast Spells
```

## Commander保護

Longbow・Crossbow ArmyはCommanderが後方に集まりやすいです。

- 全Commanderを同じSquareへ置かない
- Bodyguard
- Flying・Attack Rear対策
- AoE分散
- Retreat route

を確認します。

---

# Friendly Fire管理

LA Manの重要な技術です。

## 起きやすい状況

- Knightが早く敵へ突入
- Crossbowが接敵後も射撃
- 敵と味方が同じ密集へ重なる
- Attack Closestで全Squadが中央へ集中

## 対策

```text
射撃Squadを分ける
Targetを分ける
KnightへHoldを入れる
前衛を後方配置しすぎない
Replayで最初の味方被弾Roundを見る
```

射撃Damageだけでなく、味方のMorale・Routへの影響も確認します。

---

# Raid・Map Control

LA ManはEA Ulmほど国家全体がStealthではありませんが、Royal Forester、Forester、Magister、Lord Warden、Wardenを使えます。

主な用途：

- Scout網
- Forest経路
- Tax route切断
- Lab・Templeへの圧力
- Fort Siegeの補助
- Enemy reinforcement確認

MagisterをRaidへ出す場合、Research・Mason・SiegeのOpportunity Costを忘れないでください。

---

# Siege・Fort defence

## 攻撃側

MagisterのSiege Bonus、通常兵数、Knight・高Strength兵を使い壁を削ります。

しかしStorm forceは、

- Choke
- Wall defender
- AoE
- Morale
- Fatigue

へ別に最適化します。

## 防御側

Tower Guard、Defender、MagisterのCastle Defence、高Tier Fortを使い、Relief ArmyまでTurnを買います。

```text
Fort内Army
＋ 外部Relief
＋ Friendly Movement
```

を同期させます。

詳しくは[Forts](../../systems/forts.md)を参照してください。

## Upgrade判断

Wallだけでなく、

- Commander Point
- Mage生産数
- Recruitment Point
- Supply Storage

が増えるFortを優先します。

---

# Counterされるもの

| 相手の手段 | なぜ危険か | 対応 |
|---|---|---|
| Shield・Arrow protection | Longbow効率が落ちる | Crossbow、Magic、近接Damage |
| Storm・Wind | 射撃Planが停止 | 別Army構成、Storm caster排除 |
| Fast Cavalry・Flying | 後衛へ到達 | Bodyguard、Reserve、配置 |
| High Protection | Light Archerが通らない | Crossbow、Axeman、Earth・Astral |
| Poison・Foul Vapors | Nature不足を突かれる | Pretender、Item、外部Mage、短期決戦 |
| Magic Duel | S1 Mageが消耗 | SなしCaster、分散、敵Astral数確認 |
| Old Age pressure | Rare MageがDisease | 代替個体、Healer、役割分散 |
| Assassin・Remote attack | 高価なArcane Mageを失う | Bodyguard、Fort、分散 |
| Raid | 広いFort networkとTax routeを切られる | Scout、Mobile Reserve、PD、Fort |
| AoE | 人間兵・射撃密集が消耗 | Formation、Resistance、Army分割 |
| Fear・Morale | Screen崩壊で射撃が露出 | Bishop、Leadership、Morale support |

---

# 対主要Archetype

## 高Protection

- Crossbow
- Heavy Axeman
- Earth Strength
- Astral・Magic damage
- Fatigue・MR攻撃

を混ぜます。

## Giant

Longspear、Crossbow、Chaff、Fatigue、Controlを使い、Knightを正面から単独突撃させません。

## Archer国家

Tower Guard・DefenderをScreenにし、Air defenceとCounter-fireを使います。

## Undead・Demon

Bishop・Priestを増やし、LongbowだけでNeed Not Eat・Fear Armyを止めようとしないでください。

## Glamour・Stealth

Patrol Bonusを持つJudge・Royal Forester、Scout、True Sight外部Accessを使います。

## Poison

国家固有の大きな弱点です。

- Nature Pretender
- Resistance Item
- Independent Nature Mage
- Short battle
- Remote pressure

を事前に準備します。

---

# First War Plan

LA Manは「何でも少しできる」ため、開戦時に目的を絞らないとResearchとRecruitが分散します。

```text
敵の主前衛：
敵のShield・Protection：
敵の射撃：
敵のRear attack：
自軍の主Damage：Longbow / Crossbow / Knight / Magic
自軍のScreen：
第一Research Breakpoint：
必要Magister Arcane数：
必要Gem：
Siege Bonus：
Retreat Province：
戦争終了条件：
```

を埋めます。

## 典型的な第一戦争

```text
Border Fortを目標
→ Scoutで敵ArmyとFortを確認
→ Longbow / Crossbow比率を敵装備へ合わせる
→ Earth・Air supportを少数用意
→ MagisterでSiegeを速める
→ 新FortをMasonで強化しBorderを固定
```

Field Battleに勝ってもFortを取れないArmyは、戦争を終わらせられません。

---

# Midgame

Midgameの優先順位：

1. Fort・Commander Point
2. Magister / Arcaneの継続雇用
3. Air・Earth・Astralの役割分担
4. Missing PathへのPretender・Indie route
5. Research Item・Booster
6. National Summon access
7. Stealth・Spy情報網
8. Castle DefenceとRelief route

MagisterをResearchだけに置くとMason・Siegeを使えず、Masonだけに使うとResearchが遅れます。国家全体の人数で役割を分担します。

---

# Late game

Late gameでは、通常兵と射撃だけでは、

- Battlefield-wide Resistance
- Mass Protection
- Army-wide Arrow protection
- Elemental Storm
- Thug・SC
- Remote attack
- Global

へ止められます。

必要になるもの：

- Summon Mage
- Missing Path Pretender
- Booster chain
- Magic Phase movement
- National Summon
- Remote Ritual
- MR・Poison・Elemental Resistance
- Multiple damage type

LA ManのLate game目標は、

> **安価な人間Armyを数とFortで維持しながら、Random Mageと外部Accessを少数の決定的な役割へ集中すること**

です。

---

# Multiplayer

## 相手から見たLA Man

- Longbow・Crossbowが多い
- Fortを増やしやすい
- Drain Scalesで経済が良い可能性
- Mage Pathが読みにくい
- Nature・Water・Bloodが薄い
- Capital-only要素がある

国家です。

## 隠したい情報

- A3・E2・S2等のRare個体
- Pretenderが補ったMissing Path
- Fort upgrade予定
- Stealth Magister・Warden
- National Summon route

です。

## 外交上の注意

Fort networkが完成すると防衛しやすい一方、Expansionと第二Fortが遅れると周辺国から弱く見られます。

序盤は、

- Border
- Fort完成Turn
- Main Armyの射撃量
- 第三国との関係

を管理します。

---

# よくある失敗

## 1. 全兵種を均等にRecruitする

Armyの勝利条件がありません。

## 2. Longbowだけを増やす

Shield・Storm・Protection一つで止まります。

## 3. CrossbowとKnightを同じTimingで突入させる

Friendly Fireで高価なKnightを失います。

## 4. Magister Arcaneだけを毎Fortで雇いGold不足

Fort・兵・二軍が作れません。

## 5. MagisterをResearchだけに使う

Mason・Siege・Spyの国家能力を眠らせます。

## 6. Drainを取ったから研究は完全に無料だと思う

Pretender・Indie・Summon MageとBattle環境へ影響します。

## 7. Random Pathを確定Accessとして研究する

欲しい個体が来ず、Spellを使えません。

## 8. Nature不足を放置する

Poison・Supply・Regeneration戦で崩れます。

## 9. Capital-only WardenへHeavy Blessを過剰投資

通常兵・Mage・Fort economyが弱くなります。

## 10. Fort upgradeの目的がWallだけ

Commander Point・生産Breakpointを見ていません。

## 11. Old AgeのRare Mage一人へ国家Planを依存

DiseaseでBooster・Global routeが消えます。

## 12. 勝ったReplayを見ない

Friendly Fire、Mageの不発、不要Gem消費を見逃します。

---

# 初回Play用チェックリスト

## Turn 1–12

- [ ] Expansion Armyごとに主Damageを決めた
- [ ] LongbowとCrossbowを敵装備で使い分けた
- [ ] Commander Pointを確認した
- [ ] Magister Arcaneを止める理由がある
- [ ] 第二Fort候補のIncome・Resourcesを見た
- [ ] Drainで得たPointの使い道を説明できる

## First war前

- [ ] 敵Shield・Protection・射撃を確認した
- [ ] Air・Earth・Astral Mageを役割分担した
- [ ] Friendly FireをTestした
- [ ] Siege Bonusを用意した
- [ ] Poison対策がある
- [ ] Rare Randomを一人だけに依存していない

## Midgame

- [ ] Fortごとの役割を分けた
- [ ] Mason upgradeの回収先を決めた
- [ ] Missing Path routeを一つ完成させた
- [ ] National SummonのCasterとGemを確認した
- [ ] Old Mageの代替を用意した

---

# 情報源・検証

- Dominions 6.35ゲーム内Nation Overview
- Unit・Commander・Spell・Item popup
- Battle Replay
- 固定したDominions 6 Mod Inspector data
- [Recruitデータ](../../data/recruitment/la/man.md)
- [Magic Access Route](../../data/magic-access-routes/la/man.md)
- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [Illwiki LA Man](https://illwiki.com/dom5/dom6/man-la)（Dom6 Community側のRoster・運用知見を照合）

## 更新履歴

| 日付 | Version | 内容 |
|---|---|---|
| 2026-08-17 | 6.35 | 初版。Roster、Research economy、Fort、射撃、Pretender、Counterを統合 |
