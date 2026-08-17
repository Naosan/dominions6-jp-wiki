---
title: Pretender設計サンプル
page_type: guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
---

# Pretender設計サンプル

このページは、Pretenderの完成Buildをそのままコピーするための一覧ではありません。

Dominions 6のPretender designは、同じChassis・同じMagic Pathでも、

- NationとAge
- Map size
- Research speed
- Throne設定
- Multiplayer人数
- Sacred供給量
- Capital周辺のTerrain
- 想定するFirst war
- PatchとGame内Cost

によって価値が変わります。

そこで、このページでは数値を固定した「正解Build」ではなく、**国家攻略へ再利用できる設計骨格**をまとめます。

> **国家の不足を一つ決める**
> → **第一役割を選ぶ**
> → **第二役割を追加する**
> → **Scales・Dominion・登場時期の代償を確認する**
> → **Test gameで失敗条件を探す**

という順で使ってください。

!!! warning "Game内Design画面を最終基準にする"
    Chassis、Path cost、Bless cost、Extreme Scale、国家固有Pretender、選択可能な形態はNation・Age・Versionで異なります。本文は設計思想を示すものであり、現在のGame内Design画面に表示されるCostと制限を上書きしません。

!!! tip "まず総論を読む"
    Pretenderの役割、Awake・Dormant・Imprisoned、Dominion、Chassis、Expansion testの基本は[Pretender God](index.md)を参照してください。Scalesの意味は[Scales](scales.md)、Blessの選び方は[Bless](bless.md)で詳しく扱います。

---

# 最初に選ぶ設計骨格

| 国家の症状 | 第一候補 | Pretenderの第一役割 | 主な代償 |
|---|---|---|---|
| 国家兵だけではExpansionが不安定 | Awake Expander | Provinceを早期に取る | Scales・Bless・Magic diversity |
| 国家兵は強いがFirst warに高Path casterが欲しい | Dormant Midgame Caster | First warのSpell・Resistance・Ritual | 序盤不在、Incarnate Bless遅延 |
| 一般兵とMageを量産すれば強い | Imprisoned Scales | Economy・Research・Fort増加 | Pretender本人と技術Accessの遅延 |
| Sacredは強いが国家全部を任せるほど多くない | Light Bless＋Economy | 弱点補強と経済の両立 | Heavy Blessほどの突破力はない |
| Sacredを毎Turn大量に供給できる | Heavy Bless | Expansion・First warの主力化 | Scales・Magic diversity・Counter耐性 |
| 国家Magicが狭くGemを使い切れない | Rainbow / Diversity | Site Search・Booster・Crosspath | 前線戦闘力、暗殺耐性 |
| 特定Global・Ritualが国家計画の中心 | Global / Forge Bridge | 高PathとBooster chainの起点 | Pathが実戦前に眠るRisk |
| 後半に装備済みSCが欲しい | Dormant / Imprisoned Titan | Item・Self Buff完成後の戦闘 | 序盤への寄与が小さい |
| Capitalから動かす必要がない | Immobile Capital Engine | Forge・Global・Ritual・Dominion | Capital依存、前線参加不能 |
| Disciple GameでTeam全体を補いたい | Team Pretender / Disciple | Team Bless・Access・役割分担 | 個人国家だけでは最適化できない |

この表は入口です。二つ以上当てはまる場合は、第一役割を一つに絞り、第二役割を安価に追加します。

```text
良い設計：
Awake Expander
＋ 国家にない最低限のPoison対策

危険な設計：
Awake Expander
＋ Heavy Bless
＋ Rainbow
＋ Global caster
＋ Strong Scales
```

一体のPretenderへ全役割を要求すると、どの役割にも必要条件が足りなくなります。

---

# 全サンプル共通の五原則

## 1. Chassisより役割を先に決める

見た目や高StatsからChassisを選ぶと、後から国家に不要な能力へDesign Pointを払うことがあります。

先に、次の文章を完成させます。

```text
このPretenderは、
国家だけでは不足する＿＿＿＿を、
おおむね＿＿＿＿Turn帯までに解決する。
```

例：

```text
このPretenderは、
国家兵だけでは不安定な序盤Expansionを、
Game開始直後から解決する。
```

```text
このPretenderは、
国家にないNature AccessとPoison Resistanceを、
最初の対Player戦までに解決する。
```

## 2. 第一役割と第二役割を分ける

第一役割はDesignを成立させる理由です。

第二役割は、第一役割を壊さない範囲で追加する価値です。

| 第一役割 | 相性のよい第二役割例 | 危険な追加例 |
|---|---|---|
| Awake Expander | Site Search、低Path Resistance、Throne Claim | Heavy Blessと全Path Rainbowを同時に取る |
| Scales | 安価なUtility Path、Late Global、Forge bridge | 高価なCombat ChassisへPointを使う |
| Heavy Bless | Global caster、Sacred Mage支援 | Sacredに関係しない多数のPath |
| Rainbow | Site Search、Booster、Crosspath Item | 前線SCとして常用する |
| Global caster | 同PathのBless・Forge・Summon | 一つのGlobalしか用途がない過剰Path |

## 3. 登場時期を軍事計画へ書く

Awake・Dormant・ImprisonedはDesign Pointの交換だけではありません。

```text
Pretenderが不在の期間
＝
そのPretenderが担当するExpansion・Incarnate Bless・Forge・Site Search・Ritualが使えない期間
```

です。

Game内Design画面に表示される登場条件を確認し、次を書きます。

```text
Pretender不在中のExpansion担当：
Pretender不在中のBless性能：
Pretender不在中のMagic Access：
登場後すぐ行う仕事：
```

## 4. Scalesの損失を一Provinceではなく国家全体で見る

PretenderへPointを使うほど、Scales・Dominion・他Pathへ使えるPointが減ります。

Scalesの差は、

```text
一Provinceの毎Turn差
× 自国Dominion下のProvince数
× 残りTurn
```

へ累積します。

Awake Expanderが追加Provinceを早く取れば、弱いScalesを一部回収できる場合があります。一方、Expanderが事故死してExpansion差を作れなければ、Scales損失だけが残ります。

## 5. Buildの強さではなく失敗条件をTestする

Test gameでは、最良結果より次を探します。

- どのIndependentで事故るか
- 何Damage typeに穴があるか
- Fatigueが何Roundで危険になるか
- 何Turnまでに第二Fortを建てられるか
- First war用Researchが間に合うか
- Sacredを毎Turn何体供給できるか
- Pretender死亡時に国家計画がどこまで止まるか

> **一回うまくいったBuildではなく、何が起きると壊れるBuildかを知る。**

これがPretender testの目的です。

---

# Sample 1：Imprisoned Scales

## 一言でいうと

> **国家兵・Mage・Fortがすでに強い国家で、Pretender本人より国家全体へPointを配る設計。**

## 向く国家

- 国家兵だけでExpansionできる
- Recruit-anywhere Mageを継続雇用したい
- 一般兵またはMageが主力
- Sacredが少数、またはBlessなしでも働く
- Early warをPretenderなしで戦える
- Strong Economyが中盤以降へ累積する

## 設計骨格

```text
状態：Imprisoned
Chassis：安価なImmobile、Human、Rainbow等
Dominion：国家のSacred供給・宗教戦に必要な水準
Scales：国家の主要Bottleneckへ集中
Magic：登場後も価値が残るUtility・Forge・Global Path
第一役割：Scales
第二役割：Late ritual / Booster / Diversity
```

## Scalesの優先例

### Gold・Mage制約

```text
Order / Growthを重視
→ MageとFortの継続生産
→ 中盤のResearchとBattle Mage数へ変換
```

### Resource制約

```text
Productivityを重視
→ Capitalと第二Fortで主力兵を十分生産
→ Expansion Armyを複数作る
```

### Research制約

```text
Magic
＋ Mageを増やせるEconomy
→ Breakpoint到達を早める
```

すべてを平均的に上げるのではなく、国家が最初に詰まるResourceを解決します。

## この設計が買うもの

- 毎TurnのGold・Resource・Research
- 第二・第三Fortの早期稼働
- Mage生産量
- 通常兵の補充力
- 長期戦でのPopulation・Supply

## 諦めるもの

- Pretender本人によるExpansion
- Early Site Search
- Early Booster・Forge
- Early Global / Ritual
- Incarnate Blessの序盤利用
- Pretenderを使った宗教戦・Throne攻略

## よくある失敗

### 国家兵Expansionを過大評価する

Scalesを強くしても、Provinceを取れなければ回収できません。

```text
Test結果：
初期Armyが一戦ごとに大損
→ Imprisoned ScalesではなくAwake ExpanderまたはLight Blessを再検討
```

### Late-game用Pathを取りすぎる

Pretender登場後に、

- Research未到達
- Gem不足
- Booster未完成
- 既に別Mageで代替可能

なら、Path投資が長期間眠ります。

### Dominionを下げすぎる

Strong Scalesは自国Dominion下で働きます。Dominionを削りすぎ、TempleへGoldを使うなら、見かけほどEconomy designではありません。

## Test checklist

- [ ] Pretender不在で二つ目のExpansion Armyを作れる
- [ ] 第一Research Breakpointへ予定Turnまでに届く
- [ ] 第二Fort資金を作ってもMage生産が止まらない
- [ ] Incarnate BlessなしでSacredが役割を果たす
- [ ] Pretender登場後の仕事が一つ以上ある
- [ ] Enemy Dominionへ弱すぎない

---

# Sample 2：Dormant Midgame Caster

## 一言でいうと

> **序盤は国家兵で進み、最初の本格戦争前後に高Path Caster・Resistance・Forge・Ritualを追加する中間設計。**

## 向く国家

- Expansionは国家兵で可能
- Awakeを買うほど序盤は困っていない
- First warで国家Mageより高いPathが必要
- Dormant登場後にIncarnate BlessがSpikeになる
- 特定ResistanceやArmy-wide Buffが国家に不足
- PretenderをMagic Phase・Throne・Globalへ使いたい

## 設計骨格

```text
状態：Dormant
Chassis：Titan、Monster、Human、Rainbow等
Scales：国家兵Expansionを維持できる水準
Magic：First warで使うSpell・Resistance・Forgeへ直結
Dominion：前線運用とSacred供給に合わせる
第一役割：Midgame Caster
第二役割：Light Bless / Booster / Global
```

## 良いPath選択

次の形式で説明できるPathです。

```text
Pretender Path：
必要Research：
最初に使うSpell / Item：
対象：
必要Gem：
登場後何Turnで実戦投入するか：
```

悪い例：

> 強いSpellが多そうなので高Pathを取った。

良い例：

> First warで敵Shockを受けるため、PretenderがArmy-wide Resistanceを担当し、国家MageはDamageへ集中する。

## この設計が買うもの

- Awakeより良いScales・Bless
- First warの高Path Caster
- 国家にないForge・Summon・Global route
- Dormant登場を合図にしたTiming attack
- Pretender自身のThrone・Combat利用

## 諦めるもの

- 最序盤のPretender Expansion
- Early Site Search
- 登場前のIncarnate Bless
- Imprisonedほど強いScales・Heavy Bless

## よくある失敗

### 登場してもResearchがない

Pretenderが出ても、使うSpell・Itemが解禁されていなければ高価なCommanderが増えただけです。

### ArmyがPretenderへ依存しすぎる

Pretenderが別Frontへ移動、死亡、Call God中になると全Army planが停止します。

### 登場Turnだけを見て移動Turnを忘れる

Capitalに出現しても、前線まで複数Turnかかる場合があります。Magic Phase movementがあるか、Rally pointまで何Turnかを確認します。

## Test checklist

- [ ] Pretender不在のExpansion planがある
- [ ] 登場時点で必要Researchが完成している
- [ ] Gem・Booster・Itemを事前に用意できる
- [ ] 前線までの移動経路がある
- [ ] Pretenderが不在でも最低限戦える第二案がある
- [ ] First war後にもRitual・Global等の仕事が残る

---

# Sample 3：Awake Expander

## 一言でいうと

> **Pretender本人が序盤Provinceを取り、追加Income・Fort候補・接続を国家へ渡す設計。**

## 向く国家

- 国家兵Expansionが弱い
- 初期Armyの損失が大きい
- Capital周辺を早く確保したい
- 第二Fortを急ぐ価値が高い
- Expanderが装備なしまたは少ない支援でIndieを倒せる
- Pretenderが後から別役割へ移れる

## 設計骨格

```text
状態：Awake
Chassis：Monster、Dragon、Titan等
Dominion：前線Statsと事故率に必要な水準
Magic：生存・Damage・Fatigue・Resistanceへ直結
Scales：Expanderが作る領土差で回収可能な範囲
第一役割：Expansion
第二役割：Site Search / Throne / Midgame Combat
```

## Expanderの防御層

一つの高Statsだけで安全とは限りません。

```text
攻撃を受ける前に倒す
→ Attack / Damage / AoE / Fear

命中させない
→ Defence / Awe / Displacement

命中後に耐える
→ Protection / Resistance / HP

長期戦を続ける
→ Regeneration / Reinvigoration / Low Encumbrance

崩壊しても失わない
→ Morale / Retreat route / Returning
```

複数層を作ります。

## 最低限のTest相手

- Archer・Slinger
- Heavy Infantry
- Cavalry・Lance
- Barbarian等の高Damage兵
- Tribal・Poison
- Undead
- Elephant・Trample
- Magic Weaponを持つ特殊Independent

同じ類型を一回だけでなく複数回試します。

## Testで記録するもの

```text
相手：
自Dominion / Enemy Dominion：
Script：
戦闘開始HP：
戦闘終了HP：
最大Fatigue：
Affliction：
Rout / Retreat：
勝因：
事故条件：
次に攻めない相手：
```

## この設計が買うもの

- Early Province数
- 高Income・High Resource候補
- 第二Fortの早期建設
- 国家兵の損失回避
- Scout情報なしでも対応できる標的の増加
- Early Dominion・Throne圧力

## 諦めるもの

- Strong Scales
- Heavy Bless
- 幅広いMagic diversity
- 後方Research・Forgeを行うTurn
- Pretender死亡時の安全性

## よくある失敗

### AwakeだがCapitalで研究する

Awake costを払ったのに、Expansion差を作っていません。Awake Supportとして明確な別理由がないなら設計を見直します。

### 一回勝って安全と判断する

DRN、Poison、Lance、Afflictionで事故ります。

### Retreat routeを見ない

負けたときに安全な自領へ逃げられなければ、通常の敗北がPretender喪失になります。

### Dominion依存を忘れる

Friendly Dominionでは勝てても、Neutral・Enemy DominionでStatsが落ち、同じIndependentへ負ける場合があります。

### Expanderを永遠に単独運用する

Player戦ではMagic Weapon、AN、MR attack、Fatigue、Soul attack等が用意されます。中盤はArmy support、Throne、Ritualへ役割を変えることも検討します。

## Test checklist

- [ ] 何Turn目からCapital外へ出るか決めた
- [ ] 安全に倒せるIndependent類型を複数確認した
- [ ] 攻めないIndependent類型を決めた
- [ ] Retreat routeを毎戦確認する
- [ ] Poison・Elemental・Magic Weaponへの穴を把握した
- [ ] Expanderが死亡しても国家兵Expansionを再開できる
- [ ] Midgameの第二役割がある

---

# Sample 4：Awake Support / Early Rainbow

## 一言でいうと

> **Pretender本人はExpansionせず、Game開始直後からSite Search・Forge・Ritual・Research・Dominionを行う設計。**

## 向く国家

- 国家兵Expansionは十分
- Early Site SearchでGem incomeを増やす価値が高い
- 国家MageにないCrosspath Itemを早期Forgeしたい
- Early Ritual・Summon・Fort生成が勝ち筋
- PretenderがCapital defenceも兼ねる
- Awake costを具体的な毎Turn利益へ変えられる

## 設計骨格

```text
状態：Awake
Chassis：Human / Rainbow / Immobile等
Magic：Site Search・Forge・Ritualへ直接使うPath
Scales：Awake costを払っても国家生産が成立する水準
第一役割：Early utility
第二役割：Rainbow / Research / Capital defence
```

## Awake costを回収する問い

```text
Turn 1：何をする？
Turn 2：何をする？
Turn 3：何をする？
最初のForge：
最初のRitual：
最初に見つけたいSite：
```

これが空欄なら、Dormant・Imprisonedでも同じ仕事ができる可能性があります。

## この設計が買うもの

- Early Site Search
- Gem incomeの早期立ち上げ
- Booster・Research Item・Resistance Item
- 国家にないCrosspath
- Capital defence
- Early Dominion action

## 諦めるもの

- ExpanderほどのProvince差
- ImprisonedほどのScales
- Heavy Bless
- 前線での安全性

## よくある失敗

- Awake costの回収計画がない
- Site SearchだけしてGemを使うResearchがない
- Rainbowを前線へ出し、国家唯一のAccessを失う
- Assassin・Remote attack対策がない
- Forge予定が国家Mageだけで代替可能

---

# Sample 5：Light Bless＋Economy

## 一言でいうと

> **Sacredの致命的弱点を一つか二つ補いながら、一般兵・Mage・FortへScalesを残す設計。**

## 向く国家

- SacredはExpansion・First warで重要
- Sacredだけでは国家全Armyを構成しない
- Sacred supplyがCapital-onlyまたは中程度
- 一つの弱点を補えば十分働く
- Sacred Mage・CommanderにもBlessが有効
- Long gameで通常兵とMageへ移行する

## 設計骨格

```text
状態：Awake / Dormant / ImprisonedをIncarnate依存から選ぶ
Bless：第一に致命的弱点、第二に既存の強み
Scales：Mage・Fort・通常兵が増える水準を維持
Dominion：Sacred供給と宗教戦に必要な水準
第一役割：Light Bless
第二役割：Scales / Utility caster
```

## 第一Blessの選び方

```text
攻撃が当たらない
→ Attackまたは拘束・多段支援

Damageが通らない
→ Strength・追加Damage・AP等

射撃で死ぬ
→ Shield相当の防御、Defence、Protection、HP等

長期戦で疲れる
→ Reinvigoration・戦闘時間短縮

Poisonで崩れる
→ Poison Resistance

MR攻撃に弱い
→ MRまたはResearch側のAntimagic
```

## 第二Blessの選び方

Sacredが元から持つ長所を増幅します。

```text
多段攻撃
→ 一撃ごとに働く追加Damage・Kill連鎖

高HP
→ Regeneration・Sustain

高Protection
→ HP・Resistance・Reinvigoration

Sacred Mage
→ Reinvigoration・MR・Far Caster・Resistance
```

## この設計が買うもの

- Expansion損失の低下
- Sacredの役割明確化
- Heavy Blessより良いEconomy
- Midgame通常兵・Mageへの移行
- Sacred Commander・Mageへの継続価値

## 諦めるもの

- Heavy Blessの圧倒的なEarly spike
- Sacredだけで全Counterを解決する能力
- 一部の高価なIncarnate combination

## よくある失敗

- Sacredの供給量を数えない
- Offensive Blessだけで接敵前に死ぬ
- Defensive Blessだけで敵を倒せない
- Elemental追加Damage一本でWardに止まる
- Light BlessなのにScalesも中途半端

## Test checklist

- [ ] Sacredを一Turn何体増やせるか確認した
- [ ] BlessなしのStatsと比較した
- [ ] Expansion損失が実際に減った
- [ ] Sacred Mageにも価値があるか確認した
- [ ] First war後の通常兵・Mage計画がある
- [ ] Enemy Resistance時の第二Damageがある

---

# Sample 6：Heavy Bless

## 一言でいうと

> **大量または極めて重要なSacredへ国家のDesign Pointを集中し、ExpansionとFirst warで領土差を作る設計。**

## 向く国家

- Sacredを十分な数Recruitできる
- SacredがExpansionの中心
- Sacred Mage・Commanderも多い
- Sacred Summonを中盤以降も使う
- Blessで致命的弱点と強みを同時に扱える
- First warまでに投資を回収できる

## 設計骨格

```text
状態：Incarnate BlessのTimingからAwake / Dormant / Imprisonedを選ぶ
Bless：防御またはSustainを一層、攻撃を一層、必要Resistance
Dominion：Sacred supplyとEnemy Dominion戦を維持
Scales：Sacred生産に必要なGold・Resourceを最低限確保
第一役割：Heavy Bless
第二役割：Global / Sacred Mage support / Team role
```

## Blessを三層へ分ける

### 層1：最初の接敵を生きる

- Defence
- Protection
- HP
- Luck
- Resistance
- Morale

### 層2：敵を倒す

- Attack
- Strength
- Damage
- 多段攻撃と相性のよい追加効果
- Magic Weapon・Armor対策

### 層3：戦闘を続ける

- Regeneration
- Reinvigoration
- Recuperation
- Undying
- MR

三層すべてを最大化する必要はありませんが、攻撃だけ・防御だけへ偏らないようにします。

## Awake・Dormant・Imprisonedの選択

### Awake

- Incarnate BlessをExpansionから使う
- Early rushへ最も強い
- Scalesが弱くなりやすい

### Dormant

- 序盤は非Incarnate部分でExpansion
- 登場後のTiming attack
- 序盤Sacredが予定性能を持つかTest必須

### Imprisoned

- 最も重いBless・Scalesを取りやすい
- Incarnate効果を長期間使えない
- Sacred Expansionが不完全Blessで成立する国家向け

## この設計が買うもの

- Sacred Expansion
- First warの質的優位
- 毎戦無料で働く基礎Buff
- Sacred Mage・Commander・Summonへの長期価値

## 諦めるもの

- Strong Economy
- 幅広いMagic diversity
- Non-Sacred Armyへの直接効果
- Counterされた後の切替余地
- Pretender死亡時の安定性

## よくある失敗

### Sacred数が少ない

Heavy Blessが少数Capital-only Unitにしか働かず、国家全体のPoint効率が低くなります。

### Incarnate Timingを忘れる

Pretender不在中のExpansion planが成立しません。

### Anti-Sacredへ全Armyを出す

Non-Sacred Chaff・通常兵・Summonで対象を分散します。

### Attritionを軽視する

毎戦少数を失うだけでもCapital-only Sacredは補充不能になります。

### Scales不足でSacredを雇えない

強いBlessを持っていてもGold・Resource・Holy Pointが足りなければArmyになりません。

## Test checklist

- [ ] Sacred供給量をTurn単位で数えた
- [ ] Incarnate不在期間の戦い方がある
- [ ] Gold・Resource・Holy Pointを満たせる
- [ ] Anti-SacredへNon-Sacred部隊を用意した
- [ ] Elemental Wardへの第二Damageがある
- [ ] Pretender死亡時のArmy性能を把握した
- [ ] Midgame Sacred Summon・MageにもBlessが働く

---

# Sample 7：Rainbow / Magic Diversity

## 一言でいうと

> **多数の低～中PathからSite Search・Booster・Crosspath Item・Summon Mageへ入り、国家のMagic上限を広げる設計。**

## 向く国家

- 国家兵Expansionは十分
- Native Magicが一～二Pathへ偏る
- 複数種類のGemを使い切れない
- Booster chainの最初の一段がない
- ResistanceやCrosspath Itemが不足
- Late gameに複数PathのGlobal・Summonが必要

## 設計骨格

```text
状態：Dormant / Imprisonedが基本、明確なEarly用途があればAwake
Chassis：Path costが安いHuman / Rainbow / Immobile等
Magic：Site Searchだけでなく、具体的なForge・Summon・Globalへ接続
Scales：国家兵ExpansionとMage生産を支える
第一役割：Magic diversity
第二役割：Scales / Site Search / Global
```

## Pathを取る順番

1. 国家Mageが確実に届くPathを書く
2. Booster後の確実な到達点を書く
3. 国家にない最初の一段を書く
4. その一段で開くItem・Summon・Resistanceを書く
5. Gem incomeを確保できるか確認する

```text
Pathを持つ
≠
そのPathの国家戦略が成立する
```

です。

## 良いRainbow Path

- 国家にないBoosterをForgeする
- Crosspath Itemを開く
- Mage summon chainの入口になる
- Army-wide Resistanceを得る
- Remote Site Searchへつながる
- 一つ以上のGlobal・Ritualへ使える

## 弱いRainbow Path

- Site Search以外の用途がない
- Gem incomeがほぼない
- 国家Mageがすでに同じ役割を量産できる
- Pretenderしか使えず前線へ出せない
- Researchが遅すぎてGame中に使わない

## この設計が買うもの

- Gem economyの多様化
- Booster・Crosspath Item
- Resistance
- Summon Mage chain
- Global・Ritualの選択肢
- Empowerment回避

## 諦めるもの

- Combat chassisの生存性
- Heavy Bless
- Strong Scalesの一部
- Pretenderを危険な前線へ出す自由

## よくある失敗

### 全Pathを均等に取る

各Pathが具体的なBreakpointへ届かず、器用だが何も完成しません。

### Site Searchだけで満足する

見つけたGemを何へ使うか決まっていません。

### Rainbowを通常Battle Mageとして失う

国家唯一のForge・Global・Summon accessが消えます。

### Hero・Site Mageを確定Accessとして期待する

Pretender設計では、再現性の高いAccessと偶発的Accessを分けます。

## Test checklist

- [ ] 各PathにSite Search以外の用途がある
- [ ] 最初のBooster・Item・Summonを書ける
- [ ] Gem incomeの入手経路がある
- [ ] Pretenderを後方で守れる
- [ ] 国家Mageとの役割重複が少ない
- [ ] Late gameまで残る仕事がある

詳しいAccessの考え方は[Magic Access到達経路](../magic/magic-access-routes.md)と[拡張Magic Accessの読み方](../magic/extended-magic-access.md)を参照してください。

---

# Sample 8：Global / Forge Bridge

## 一言でいうと

> **特定の高Pathへ集中し、国家Mageが届かないGlobal・Ritual・Booster chainを開く設計。**

## 向く国家

- 使いたいGlobalが国家計画の中心
- 国家Mageが一段だけPath不足
- PretenderがBoosterをForgeすれば量産Mageも届く
- Gem incomeとResearch Timingが明確
- Global以外にもSummon・Resistance・Blessへ同Pathを使える

## 設計骨格

```text
状態：Dormant / Imprisoned、Early GlobalならAwakeも検討
Chassis：高Pathを安価に取れるもの
Magic：目標GlobalだけでなくForge・Summon・Battle利用も確認
Scales：目標ResearchとGem economyを支える
第一役割：Global / Ritual / Forge bridge
第二役割：Bless / Resistance / High-end caster
```

## Global計画を成立させる七項目

```text
Global / Ritual：
Research School・Level：
Base Path：
Booster後Path：
必要Gem：
発動予定Turn：
発動後の防衛・Dispel対策：
```

これを書けない場合、高Pathを取っても計画ではありません。

## この設計が買うもの

- 国家Mageが届かない高Path
- Booster chainの起点
- Global・Legendary・大規模Ritual
- 同PathのArmy-wide Spell
- PretenderによるThrone・Magic Phase作戦

## 諦めるもの

- Path集中によるMagic diversity
- Global解禁前の寄与
- Pretender死亡・Feebleminded時の安定性
- Gemを別戦術へ使う自由

## よくある失敗

- Global一つしか用途がない
- Researchより早くPretenderが登場して待機する
- Gem incomeが足りない
- Boosterを誰がForgeするか決まっていない
- Dispel・競合Globalを考えていない
- 発動後にPretenderを前線へ出して失う

---

# Sample 9：Dormant / Imprisoned Titan SC

## 一言でいうと

> **序盤は国家兵で進み、Research・Item・Self Buff完成後にPretenderをThug / Supercombatantとして投入する設計。**

## 向く国家

- Early Expansionを国家兵で行える
- Construction・Alteration・Enchantment等を自然に研究する
- Booster・防御ItemをForgeできる
- Pretenderが複数Item Slotを持つ
- Mid～Late gameに単独作戦・Throne攻略が必要
- SC以外のRitual・Global役もある

## 設計骨格

```text
状態：Dormant / Imprisoned
Chassis：Titan、Humanoid Giant等
Magic：Self BuffとResistanceを自力で組めるCrosspath
Scales：装備・Research完成まで国家を支える
第一役割：Late combat
第二役割：Global / Forge / Throne
```

## SCの防御層

- 通常物理
- Magic Weapon
- AP / AN
- Fire / Cold / Shock / Poison / Acid
- MR attack
- Fatigue
- Soul・Control・Charm
- Horror
- Lifeless / Undead固有Counter
- Retreat / Returning

HP・Protectionだけでは不十分です。

## 実戦投入条件

```text
必要Research：
必須Self Buff：
必須Item：
必要Gem：
倒すTarget：
避けるCounter：
Retreat route：
死亡時の国家損失：
```

一つでも空欄なら、まだ「強そうなPretender」であって作戦Unitではありません。

## この設計が買うもの

- Thug / SC
- Throne攻略
- Raid・Choke defence
- 高Path Battle spell
- Item Slotを使った柔軟なCounter

## 諦めるもの

- Early Expansion
- 装備・Research完成前の価値
- ItemとGemの他用途
- Soul attack等へ完全な安全性

## よくある失敗

- 裸のDormant Titanを出現直後に前線へ送る
- 一つの防御層だけで無敵だと思う
- Enemy Scoutに装備とScriptを見せ続ける
- Retreat routeがない
- 国家唯一のGlobal casterとSCを同一個体へ依存する
- Affliction・Diseaseの回復手段がない

---

# Sample 10：Immobile Capital Engine

## 一言でいうと

> **Capitalから動かず、Forge・Research・Ritual・Global・Dominionを行う代わりに安いChassisや高Magicを利用する設計。**

## 向く国家

- Capital defenceが強い
- Pretenderを前線へ出す必要がない
- Global・Forge・Summonが国家計画の中心
- Path costまたはChassis costの利点が大きい
- Magic Phaseや遠隔Ritualで仕事ができる
- Capital喪失Riskを管理できる

## 設計骨格

```text
状態：Awake / Dormant / Imprisonedを仕事の開始時期で選ぶ
Chassis：Immobile
Magic：Forge・Global・Ritual・Summonへ集中
Scales：国家ArmyとFort networkを支える
第一役割：Capital magic engine
第二役割：Dominion / Research / Capital defence
```

## この設計が買うもの

- 安価な高Path
- 安全な後方Forge・Ritual
- Capital defence
- Global caster
- 国家にないCrosspath

## 諦めるもの

- Normal Movement
- 前線Throne Claim
- Retreatによる生存
- Capital以外での柔軟な運用

## よくある失敗

### Capitalが唯一の失敗点になる

Siege、Remote attack、Assassination、Dominion pressureで国家Magic engineごと止まります。

### 前線へ届かないSpellを取る

Range・Plane・Target条件を確認します。

### Awakeなのに仕事がない

CapitalでResearchするだけなら、Awake costを回収できない場合があります。

## Test checklist

- [ ] Capitalが包囲された場合の第二Casterがいる
- [ ] 遠隔で実行できる仕事が複数ある
- [ ] Lab破壊・Siege時の影響を把握した
- [ ] Global競合・Dispelへ備えた
- [ ] Pretenderが動けないことを国家のRetreat・Throne計画へ反映した

---

# Sample 11：Disciple GameのTeam Pretender

## 一言でいうと

> **一国家だけでなくTeam全体のSacred、Magic Access、Expansion、Dominion、勝利Timingを補う設計。**

Disciple Gameでは、PretenderのBlessと一部の国家・宗教要素がTeam全体へ関係します。個人戦の「自国に最適」をそのまま使わないでください。

詳しい継承・制約・Team運用は[Disciple Game](../systems/disciple-game.md)を参照してください。

## Teamで最初に共有するもの

```text
各NationのSacred：
各NationのExpansion方法：
Team全体で不足するResistance：
Team全体で不足するStrategic Path：
Pretenderが担当するGlobal / Forge：
Throne Claim担当：
Dominion・Temple計画：
```

## Team Pretenderの代表骨格

### Team Heavy Bless

複数Nationが十分なSacredを持ち、同じBlessから価値を得る場合です。

Risk：

- 一国のSacredにだけ最適化
- 他国Sacred Mageへ不利
- Incarnate不在期間がTeam全体へ影響
- Scales・Magic diversity不足

### Team Rainbow / Access

Team各国のNative Pathを接続し、Booster・Crosspath Item・Globalを開きます。

Risk：

- 誰がGemを供給するか不明
- Pretenderだけが全Accessを持ち、前線要請が競合
- Team communication不足

### Team Awake Expander

Pretenderを持つ側がEarly Expansion差を作り、他DiscipleへBorder・Throne・Goldを還元します。

Risk：

- 一国だけが領土を増やしTeam全体へ還元されない
- Pretender死亡でTeam Bless・Dominion計画も損傷

## Disciple側の設計

DiscipleはPretender designと独立ではありません。

- Team Blessを受けるSacred供給
- 自国ScalesとEconomy
- Pretender不在中の戦い方
- Team内で不足するMagic Path
- Throne Claim・Dominion役
- Front担当と後方Research担当

を明確にします。

## Team test

一国ずつTestするだけでなく、

```text
TeamのExpansion合計
TeamのResearch合計
TeamのGem供給
同じTurnに出せるArmy数
Throne Claim timing
Pretender死亡時のTeam性能
```

を確認します。

---

# Chassisを選ぶ比較表

| Chassis類型 | 強み | 主な用途 | 主なRisk |
|---|---|---|---|
| Monster | HP、Natural Protection、Awe、Fear、Regeneration等 | Awake Expansion | Slot不足、Resistance穴、Affliction |
| Dragon / Multiple form | 高機動、形態変化、Early combat | Expansion、Raid、Midgame caster | 形態ごとのStats・Slot・Path差 |
| Titan | Item Slot、High Stats、Late scaling | Dormant Caster、SC、Throne | Cost、Fatigue、即死・Soul attack |
| Human / Rainbow | 安いPath cost、多Path | Diversity、Site Search、Forge | 低HP、暗殺、前線不向き |
| Immobile | 安価・高Magic・Capital defence | Global、Forge、Ritual | Capital依存、移動不能 |
| National / Special | 国家固有相乗 | Bless、Dominion、特殊戦術 | 一般論が通用しない固有制約 |

Chassisの見た目ではなく、次のCostを含めて比較します。

```text
Chassis cost
＋ 必要Path cost
＋ Awake / Dormant / Imprisoned cost
＋ 必要Dominion
＋ 失うScales
＋ 必要な装備・Research
```

---

# Design選択フロー

```text
国家兵だけで安全にExpansionできる？
├─ No
│   ├─ Sacred Blessで解決できる？
│   │   ├─ Yes → Light / Heavy BlessをTest
│   │   └─ No  → Awake ExpanderをTest
│   └─ Expanderが安全なChassisを持つ？
│       ├─ Yes → Awake Expander
│       └─ No  → 国家兵・Summon・Pretender方針を再設計
└─ Yes
    ├─ Sacredが国家主力？
    │   ├─ Yes → Light / Heavy Bless
    │   └─ No
    ├─ 国家Magicが狭い？
    │   ├─ Yes → Rainbow / Forge Bridge
    │   └─ No
    ├─ First warに高Pathが必要？
    │   ├─ Yes → Dormant Midgame Caster
    │   └─ No
    └─ Economyを増やすほど強い？
        ├─ Yes → Imprisoned Scales
        └─ No  → Global / Titan / Utilityを比較
```

このFlowは最終回答ではありません。候補を二つまで絞り、同じMap・同じNationで比較Testします。

---

# 二つのBuildを比較する方法

Pretender designを感覚で比べず、同じ条件へ置きます。

| 評価軸 | Build A | Build B | 見るもの |
|---|---|---|---|
| Expansion |  |  | Turn、損失、事故率、二軍作成 |
| Economy |  |  | Income、Resource、第二Fort |
| Research |  |  | 第一・第二Breakpoint到達Turn |
| Sacred |  |  | 毎Turn供給、損失、Incarnate依存 |
| Magic Access |  |  | Booster、Summon、Global、Gem |
| First war |  |  | Caster、Resistance、Army数 |
| Midgame |  |  | Fort数、Mage数、Pretender役割 |
| Failure |  |  | 死亡、Counter、Dominion、Supply |
| 操作量 |  |  | Script、Gem配布、Site Search |

## 最低限の比較期間

- Expansion Armyが二つ以上動くまで
- 第二Fortを建て、Mage生産を開始するまで
- 第一Research Breakpointへ届くまで
- PretenderがFirst warで役割を果たすまで

Awake ExpanderとImprisoned ScalesをTurn 1のStatsだけで比較してはいけません。

---

# 国家攻略へ記載する形式

国家記事へPretender例を書くときは、画像やPathだけで終わらせません。

```text
設計骨格：Dormant Midgame Caster

解決する問題：
国家MageだけではFirst warまでにArmy-wide Shock Resistanceへ届かない。

第一役割：
Dormant登場後にResistanceと高Path Battle spellを担当。

第二役割：
国家にないBoosterをForgeし、後半Globalへつなぐ。

犠牲：
Imprisoned ScalesよりEconomyが弱く、Awake Expansionはできない。

Pretender不在中：
国家兵二ArmyでExpansion。Incarnate Blessへ依存しない。

最初のResearch：
＿＿＿＿。

最初の実戦Turn：
＿＿＿＿。

失敗条件：
Research遅延、Gem不足、前線到着前のRush、Pretender死亡。
```

複数例を載せる場合は、同じ役割の微差ではなく、異なる国家計画を示します。

```text
例A：安全なScales
例B：First war重視のDormant caster
例C：特殊Matchup用Awake expander
```

---

# MA Ulmへ当てはめる例

[MA Ulm](../nations/ma/ulm.md)のように、

- 国家兵Expansionが可能
- ResourceとFort配置が重要
- Recruit-anywhere Mageを増やすほど強い
- Native Magicは強いが幅に限界がある

国家では、Pretender候補を次のように比較できます。

## 候補A：Imprisoned Scales

```text
目的：
Resource・Gold・Mage生産を増やし、第二・第三Fortを早く稼働する。

強み：
国家の本来の生産Engineを最大化しやすい。

弱み：
PretenderによるEarly diversity・Site Search・Combatがない。
```

## 候補B：Dormant Diversity / Caster

```text
目的：
First war前後に国家にないResistance・Crosspath・高Pathを追加する。

強み：
国家兵Expansionを維持しながら中盤の技術上限を広げる。

弱み：
Scalesを一部失い、登場までUtilityが使えない。
```

## 候補C：Awake Expander

```text
目的：
周辺Independentが危険、またはMap条件上Capital周辺を急いで確保する。

強み：
序盤Province差を作れる。

弱み：
本来強い国家兵Expansionと役割が重複し、Economyを削る可能性がある。
```

このように、国家の「強いもの」ではなく、**同じ国家で何を優先するGame planか**によってPretenderを選びます。

!!! note "国家記事を優先する"
    上記は設計骨格の当てはめ方です。実際のChassis、Path、Scales、Researchは、現在の国家記事とGame内Design画面で確認してください。

---

# Pretender Test Game手順

## Step 1：比較条件を固定する

- 同じNation・Age
- 同じMapまたは似たCapital周辺
- 同じAI・Research・Throne設定
- 同じ初期Recruit方針
- 同じExpansion target類型

## Step 2：Turn 1の予定を書く

```text
Recruit：
Research：
Prophet：
Pretender Order：
Initial Army target：
```

## Step 3：Expansionを記録する

```text
Turn：
取得Province：
Army：
損失：
Pretender HP / Fatigue：
次の標的：
```

## Step 4：Economyを記録する

```text
第二Expansion Army完成：Turn ＿
第二Fort開始：Turn ＿
第二Fort完成：Turn ＿
Mage数：Turn ＿時点で＿人
第一Research Breakpoint：Turn ＿
```

## Step 5：First war相当のTestを行う

AI戦でも、想定Counterを意図的に用意します。

- 高Protection
- 高Defence
- Archer
- Elemental Damage
- Poison
- MR attack
- Giant
- Undead / Demon

Pretenderが担当するSpell・Bless・Combat役割が本当に機能するか確認します。

## Step 6：死亡・不在をTestする

Pretenderを一時的に使わず、

- Armyがどこまで弱くなるか
- Incarnate Blessが消えた場合
- Booster・Global accessを失った場合
- Call GodへPriest turnを使う場合

を確認します。

Strong Buildは、Pretenderが生きているときだけ強いBuildではなく、**事故後に国家が何を残せるか分かっているBuild**です。

---

# Build記録テンプレート

```text
Nation / Age：
Game setting：
Map / Player数：

Chassis：
Awake / Dormant / Imprisoned：
Dominion：
Scales：
Magic Path：
Bless：
Incarnate Bless：

設計骨格：
第一役割：
第二役割：
解決する国家の不足：
諦めるもの：

Pretender不在中のPlan：
Pretender登場後の最初の仕事：
Expansion target：
避けるIndependent：
最初のResearch：
最初のForge：
Booster chain：
最初のGlobal / Ritual：
First war予定Turn：

想定Counter：
Pretender死亡時の代替：
Dominion Risk：
Test回数：
確認Version：
```

Design画像を保存する場合も、この記録を添えてください。

---

# よくある設計失敗

## 一体へ全役割を詰め込む

Expander、Heavy Bless、Rainbow、Global、Strong Scalesを同時に成立させようとし、すべてが不足します。

## Awakeの理由がない

Game開始直後から毎Turn何をするか書けません。

## Imprisonedの不在期間を無視する

Incarnate Bless、Site Search、Booster、Globalが必要Turnに間に合いません。

## Scalesを「余り」として決める

国家のGold・Resource・Research Bottleneckと接続していません。

## Dominionを無料Pointとして削る

Sacred供給、Scales伝播、Pretender Stats、Dominion kill耐性を失います。

## Sacredを数えずHeavy Bless

Bless対象が少なく、通常兵とMageが弱くなります。

## Pathを取っただけでAccessが成立したと思う

Research、Gem、Booster、Caster location、Plane、Rangeが不足します。

## ExpanderをTestしない

Poison、Lance、Fatigue、Affliction、Retreatで事故ります。

## Sampleを唯一の正解としてコピーする

Map、Nation、Patch、Opponentが違えば必要役割も変わります。

---

# 次に読む

1. [Pretender God](index.md)で役割と設計手順を確認する
2. [Scales](scales.md)で国家EconomyのBottleneckを選ぶ
3. [Bless](bless.md)でSacredの弱点と供給量を評価する
4. [Pretender chassis索引](../data/units/pretenders.md)で候補を調べる
5. [国家選択ガイド](../nations/choose-a-nation.md)と国家記事でGame planを決める
6. Test gameでExpansion・Fort・Research・First warを比較する

## 関連ページ

- [Pretender God](index.md)
- [Scales](scales.md)
- [Bless](bless.md)
- [Dominion](../systems/dominion.md)
- [Throne of Ascension](../systems/thrones.md)
- [Disciple Game](../systems/disciple-game.md)
- [Magic Access到達経路](../magic/magic-access-routes.md)
- [拡張Magic Accessの読み方](../magic/extended-magic-access.md)
- [国家攻略テンプレート](../templates/nation-template.md)

## 主な参照先

- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
