---
title: Dominion・Scales・宗教戦
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# Dominion・Scales・宗教戦

Dominionは、Provinceを誰が所有しているかではなく、

> **その土地で、どのPretender Godが、どれほど強く信仰されているか**

を表す仕組みです。

Map上ではCandleで表示されます。

Dominionは単なる宗教的な色塗りではありません。

- Provinceへ広がるScales
- Pretender・Disciple・Prophetの能力
- BlessとIncarnate Bless
- Sacred recruitmentのHoly Points
- ArmyのMorale
- 国家固有Dominion効果
- Temple・Preach・Blood Sacrifice
- ThroneとDisciple Game
- Dominion killによる国家消滅

を一つのNetworkとして結びます。

このページの目的は、Candle数を暗記することではありません。

> **どこから信仰が発生し、いつ戦闘条件へ反映され、どのProvinceを失うと宗教Networkが崩れるか**

を判断できるようにすることです。

!!! note "このページの精度範囲"
    本文はDominions 6.35を対象に、現行Manualへの公式導線、公式Dom6変更点、ゲーム内UI・Tooltip、[ターン処理順](../reference/turn-resolution.md)、および現行Community testで確認されている主要挙動を実戦向けに整理しています。Temple checkの内部経路、端数処理、特殊国家、Event、別Plane、Land/Sea境界、Discipleへの国家効果継承には例外があります。そのため記事Statusは`reviewed`であり、全内部処理を実験的に証明した`verified`ではありません。

---

## 最初に覚える七つ

### 1. Ownership、Dominion、Scalesは別

Provinceに自国の旗が立っていても、Enemy Dominion下にある場合があります。

同じように、自国Dominionがあるからといって、Provinceを自国が所有しているとは限りません。

```text
旗       ＝ Provinceの所有者
Candle   ＝ 信仰されているPretender
Scales   ＝ 現在のProvince環境
```

を分けます。

詳しくは [Province](province.md) を参照してください。

### 2. Pretender設計時のDominion値と、各ProvinceのCandle数は別

Pretender designのDominion strengthは、宗教Network全体の強さです。

各ProvinceのCandle数は、そのProvinceで現在どれほど信仰されているかです。

```text
Pretender Dominion strength
≠
現在いるProvinceのCandle数
```

同じ値になることはありますが、同じ概念ではありません。

### 3. Passive spreadとPreachは処理時期が違う

Priestの`Preach the Word of God`は、通常Battleより前にLocal Dominionを動かします。

一方、Temple・Capital・Pretender・Prophet・Throneによる通常のPassive spreadは、Turn後半、通常Battleより後に処理されます。

したがって、

> このTurnのStorm戦へFriendly Dominionを間に合わせたい

なら、Templeを建てたまま待つだけではなく、Preachを使う意味があります。

### 4. Temple 5棟は宗教上のBreakpoint

通常、Templeを5棟増やすごとにEffective Dominion strengthが1上がります。

これは、

- Dominion conflict
- Local Candle上限
- Sacred recruitmentのHoly Points

へ影響します。

Temple数は単なるSpread source数ではありません。

### 5. CandleはPretender・Disciple・Prophetの戦闘能力を変える

Friendly Dominionでは、Pretender、Disciple、ProphetのHP・Strength・MRが上がります。

Hostile Dominionでは逆に下がります。

Combat PretenderにとってDominionは、装備やBuffと同じ軍事資源です。

### 6. Candleが増えても、Scalesは即座に完成しない

ProvinceがFriendly Dominionへ変わっても、Order、Growth、Magic等がその瞬間に設計値へ揃うとは限りません。

Scalesは毎Turn少しずつLocal Dominionの目標値へ動きます。

### 7. 世界から自国Dominionが消えると敗北

Fort、Army、Gold、Gem、Pretenderが残っていても、自国Candleが世界から消滅すれば国家は敗北します。

Dominion killは、領土戦と並行して存在する独立した勝利・敗北経路です。

---

# Dominionを構成する六つの値

| 要素 | 何を表すか | 主な用途 |
|---|---|---|
| Base Dominion strength | Pretender design時の宗教強度 | Design Point、初期Spread、Holy Points |
| Effective Dominion strength | Temple等による増加を含む現在値 | Conflict、Local上限、Sacred recruitment |
| Local Candle | 一つのProvinceの信仰強度 | Stats、Morale、Scale移行、国家効果 |
| Temple checks | Passive Dominionを発生させる試行 | Dominion Networkの拡大 |
| Preach / Sacrifice | Commanderが行う能動的な宗教行動 | Local調整、Frontline宗教戦 |
| Current Scales | Provinceで現在作用する環境 | Economy、Research、Supply、Event、Battle |

この六つを一つの「Dominion値」として扱うと、

- Templeを増やしたのに前線Candleがすぐ増えない
- Friendly CandleなのにScalesがまだ悪い
- Local Candleが高いのにSacred生産数が増えない
- Enemy Dominion下でPretenderが予定より弱い

という混乱が起こります。

---

# Dominion strength

## Base Dominion strength

Pretender designで決める値です。

Base値はChassisによって異なり、Design Pointを使って上げます。

高くする主な理由：

- Sacredを多くRecruitする
- Strong Bless国家
- Pretender・Discipleを前線で戦わせる
- 強い国家固有Dominion効果
- Enemy Blood Sacrificeへ耐える
- Dominion kill Riskを下げる
- Scalesを早く定着させる

低くする主な理由：

- Scales・Magic Path・BlessへPointを回す
- Sacred供給量が少ない
- Pretenderを前線へ出さない
- Templeを大量に建てる予定
- 宗教戦を避けられるMap・外交

低Dominionは無料Design Pointではありません。

> **将来のTemple費用と宗教戦Riskを先に借りる設計**

です。

## Effective Dominion strength

Game中はTemple数により増加します。

通常は、

```text
Effective Dominion strength
＝ Base Dominion strength
＋ floor(Temple数 / 5)
```

として考えられます。

Disciple GameではTeam人数を考慮したTemple breakpointが使われるため、通常Gameと同じTemple数だけを見ないでください。

### 5Temple breakpointの意味

5棟目、10棟目、15棟目のTempleは、単にTemple checkを一つ追加するだけではありません。

Effective Dominion strengthを上げ、

- Enemy Candleを押し返す力
- Passive spreadのLocal上限
- 各FortのHoly Points

も変えます。

Templeを建てるときは、

```text
現在のTemple数
→ 次の5棟Breakpointまで何棟か
→ Sacred生産とDominion戦に間に合うか
```

を確認します。

---

# Holy PointsとSacred recruitment

Sacred Unitは、Gold、Resources、Recruitment Pointsに加えてHoly Pointsを使います。

通常、TempleのあるRecruit拠点が毎Turn使えるHoly Pointsは、Effective Dominion strengthに基づきます。

一部Sacredは1ではなく複数Holy Pointsを使い、Recruitに複数Turnかかる場合は各TurnのHoly Pointを占有します。

```text
Goldがある
＋ Resourcesがある
＋ Recruitment Pointsがある
＋ Holy Pointsがある
＋ Templeがある
＝ Sacredが予定どおり完成する
```

## よくある誤解

### Local Candle数がSacred生産上限ではない

CapitalにWhite Candleが8本見えていても、それだけで各Fortが毎TurnSacred 8体をRecruitできるとは限りません。

見るべきなのはEffective Dominion strengthとUnitのHoly Point costです。

### TempleがないFortではSacredを雇えないことがある

National SacredやSacred Mageを各Fortで雇う国家では、FortだけでなくTemple建設も生産計画へ含めます。

### National exception

Ind、Piconye、特殊Site、国家能力等にはHoly PointやTempleの例外があります。

最終的にはRecruit画面のHoly Point表示を確認してください。

---

# Passive Dominionの発生源

## Capital

Capitalは宗教Networkの初期中心です。

Capitalを包囲・喪失すると、

- Spread source
- Pretender recall地点
- Capital-only Priest・Sacred
- Temple・Throne・Lab

を同時に危険へ晒す場合があります。

CapitalがFortとして残っていても、外側のProvince controlと税収・増援は失われるため、宗教戦を領土戦から切り離して考えないでください。

## Temple

通常、各Templeは毎Turn一つのTemple checkを発生させます。

Templeの役割は、

1. Passive Dominion source
2. Sacred・Priest recruitmentの解禁
3. Preachの強化
4. Blood Sacrificeの拠点
5. 5棟ごとのEffective Dominion strength上昇

です。

## Prophet

Prophetは通常、一つのTemple checkを発生させる移動可能な宗教sourceです。

また、

- 高Holy level
- 常時Bless
- 高Morale
- Friendly/Hostile Dominionによる能力変化
- Army同行
- Throne claim

を持つ戦略Commanderです。

Prophetを前線へ出す価値は高い一方、死亡後はすぐ同じ役割を再任命できません。

## Pretender

世界に存在するPretenderは強力なSpread sourceです。

現行の一般モデルでは、

- 一つのGuaranteed check
- 二つの通常Temple checks

を持つ、合計三つ相当のsourceとして扱われます。

Dormant、Imprisoned、死亡、特殊Plane等でPretenderが世界にいない期間は、

- このSpread
- Incarnate Bless
- Pretender本人の戦略行動

を失います。

## Claimed Throne

Claim済みThroneは、Descriptionに記載された数のDominion spreadを行う場合があります。

Throneは、

- Ascension Point
- Scale・Gem・Bless等のClaim効果
- Spread source
- 戦略Choke

を兼ねます。

詳しくは [Throne of Ascension](thrones.md) を参照してください。

## Dominion Spread能力

Juggernaut、召喚Commander、国家固有Unit等には、追加Temple checksを発生させる能力があります。

Unitの存在だけでなく、

- 移動可能か
- 生存しているか
- どのProvinceを起点にするか
- Gem・Researchが必要か

を見ます。

## National exception

一部国家では、Capital、Temple、Prophet、Pretenderによる通常Spreadが制限または変更されます。

代表例：

- Dying / Restricted Dominion
- Blood Sacrifice依存
- Inquisition
- Dominion conflict bonus
- TempleでFreespawn
- Discipleには継承されないDominion効果

国家選択画面と国家攻略記事を優先してください。

---

# Temple check

Temple、Capital、Prophet、Pretender、Throne等から発生するPassive spreadの試行を、一般にTemple checkと呼びます。

## Check成功率の計画用モデル

現行のCommunity testでは、通常checkの成功率は概ね、

```text
50% ＋ 5% × Effective Dominion strength
```

として扱われます。

| Effective Dominion | 通常checkの目安 |
|---:|---:|
| 1 | 55% |
| 4 | 70% |
| 6 | 80% |
| 8 | 90% |
| 10 | 100% |

これは、

> Temple一棟が必ず毎Turn一Candleを増やす

という意味ではありません。

Checkが成功した後、どのProvinceへ信仰が置かれるかという別処理があります。

## Checkの数と質

宗教Networkは、

```text
Temple checkの数
× Check成功率
× 信仰が必要な場所へ届く経路
```

で考えます。

Templeを多数建てても、後方の高Candle Provinceへ吸収され、前線へ十分届かない場合があります。

逆に、前線Temple、Prophet、Preach、Blood Sacrificeを使うと、必要な場所へ宗教圧力を集中できます。

---

# Passive Dominionはどこへ広がるか

## Neutral Dominion

Neutral Provinceへ成功した信仰が到達すると、通常は自国Candleが1増えます。

## Friendly Dominion

すでにFriendly Candleがある場合、現在Candleが高いほど、そのProvinceへさらに一Candleを追加しにくくなります。

現行のCommunity modelでは、起点Provinceへ留まる確率は概ね、

```text
30% － 3% × 現在のFriendly Candle
```

です。

高Candle Provinceで定着しなかった信仰は、隣接Provinceへ移動し、置き場所を探します。

このため、後方の高Candle地域は、前線へ信仰を送り出す通路として働くことがあります。

## Hostile Dominion

Hostile Dominionへ信仰が到達すると、まずEnemy Candleを1本減らそうとします。

現行の計画用モデルでは成功率は概ね、

```text
50%
＋ 5% × 自国Effective Dominion strength
－ 5% × Local Enemy Candle
```

です。

したがって、

- 自国Dominion strengthが高い
- Enemy Candleが低い
- Temple check数が多い

ほど押し返しやすくなります。

Enemy Candleを減らし切ってNeutralにし、その後White Candleへ変えるには複数回の成功が必要です。

## LandとSea

LandからSea、SeaからLandへPassive spreadが渡るときは、通常より通りにくくなります。

水中国家と地上国家の宗教Frontは、陸上だけのFrontより不安定になりやすいため、

- Coastal Temple
- Underwater Priest
- Amphibious Prophet
- Blood Sacrifice
- Throne
- Pretender移動

を使って補います。

## Plane境界

Cave、Surface、Void等の別Plane接続では、Map接続と特殊Effectの組み合わせに例外があります。

Plane入口を、

- Fort
- Temple
- Scout
- Mobile Priest

で押さえます。

Passive spreadがどのように境界を越えるかはMap・Version・特殊接続により確認してください。

---

# Local Candleの上限

通常のPassive spreadで一Provinceへ置けるFriendly Candleは、Effective Dominion strengthに制約されます。

ただし、

- Preach
- Event
- 特殊国家能力
- Spell・Item

は通常上限と異なる挙動をする場合があります。

Local Candleが設計値を超えて見える場合、Bugと決めつけず、Preach、Event、Temple、Throne、特殊Effectを確認します。

---

# Preach the Word of God

PreachはPriestが一Turn使い、そのProvinceだけのDominionを能動的に動かすOrderです。

Passive spreadと違い、成功したCandleは隣接Provinceへ広がりません。

> **宗教Network全体を広げるのではなく、今必要な一Provinceを変える行動**

です。

## 成功率の計画用モデル

通常PriestのPreach成功率は概ね、

```text
30% × Holy level
＋ Templeがあれば15%
－ 5% × Local Enemy Candle
```

です。

最低成功率が残る場合や、100%を超えた分が追加checkになる場合があります。

### 例1：H1、Templeなし、Enemy Candle 4

```text
30% － 20% ＝ 約10%
```

### 例2：H1、Templeあり、Enemy Candle 4

```text
30% ＋ 15% － 20% ＝ 約25%
```

### 例3：H3、Templeあり、Enemy Candle 2

```text
90% ＋ 15% － 10% ＝ 約95%
```

## Preach上限

通常、PriestがPreachだけで押し上げられるLocal DominionにはHoly levelに応じた上限があります。

計画上は、

```text
Templeなし：Holy level × 2
Templeあり：Holy level × 2 ＋ 1
```

を目安にします。

H1 Priest一人を長期間置いても、Local Candleを際限なく増やすことはできません。

## Inquisitor

InquisitorはHostile Dominion下でPreachするとき、Holy levelをより高く数える能力を持ちます。

役割は、

- Enemy Candle除去
- Occupied Provinceの宗教安定化
- Fort storm前のLocal調整
- Enemy national Dominion effectの除去

です。

InquisitorをFriendly Dominionの後方で通常Preachさせるより、Enemy Dominionへ投入した方が価値が高いことがあります。

## Preachの主な用途

- Storm前にFriendly Dominionへする
- Break Siege前に守備Pretenderを強化
- Throne claim地点を安定化
- Enemy national Dominion effectを除去
- Dominion killを一Turn遅らせる
- Enemy Temple破壊後の空白を埋める
- Combat Pretenderの侵攻路を準備

## PreachはBattleより前

Preachは通常Battleより前に処理されるため、成功すれば同TurnのBattleへ、

- Pretender・Prophet・DiscipleのStats
- 自動Bless条件
- Army Morale
- 一部国家Dominion効果

を間に合わせられます。

一方、Passive Temple checksはBattle後です。

この差を [ターン処理順](../reference/turn-resolution.md) と合わせて確認してください。

---

# SiegeとPreach

Sieged Fortでは、Province外側とFort内部の支配が分かれています。

外側をSiegerが支配していても、Fort内部のPriestは生存し、Orderを実行できる場合があります。

StormまたはBreak Siegeを予定するTurnでは、

```text
Preach
→ Local Dominion更新
→ Field Battle / Fort Storm
```

という順序が重要です。

## 防御側

- Fort内PriestでPreach
- Prophet・Pretenderを守る
- Enemy DominionによるHP・MR低下を防ぐ
- Incarnate Bless条件を維持
- Break Siege前にMoraleを整える

## 攻撃側

- Province外側のPriestでPreach
- Enemy Candleを減らす
- Defender Pretender・Prophetを弱体化
- Enemy national Dominion effectを消す
- Storm前にFriendly Dominionを作る

Fort戦の全体像は [Fort・Siege・Storm](forts.md) を参照してください。

---

# Blood Sacrifice

一部国家は、TempleでBlood SlaveをSacrificeし、追加Temple checksを発生させられます。

通常、一Turnに使えるBlood Slave数はPriestのHoly levelで制限され、一Slaveが一Temple check相当として働きます。

```text
Eligible Priest
＋ Temple
＋ Blood Slave
＋ Sacrifice Order
＝ 追加Temple checks
```

## 強み

- 必要なFrontへ宗教圧力を集中
- 低Base Dominionを補う
- Enemy Temple networkを上回る
- Land/Sea・Plane境界の弱いSpreadを補完
- Dying / Restricted Dominion国家を維持
- Dominion killを能動的に狙う

## Cost

- Blood Slave消費
- Priest turn消費
- Templeが必要
- Blood Hunter・Patrol・Populationへの投資
- Raid・Assassinationで拠点を失うRisk

Blood Sacrifice国家の宗教力は、Priest数だけでなく、

> **Blood economyを何Templeへ毎Turn配送できるか**

で決まります。

## Counter

- Sacrifice TempleをRaid
- Blood Slave輸送を切る
- Eligible PriestをAssassinate
- Blood ProvinceへUnrest・Remote attack
- 複数Frontを作りSacrificeを分散
- 自国Templeの5棟Breakpointを前倒し

---

# HereticとAnti-Dominion

Heretic能力を持つUnitやItemは、Local Dominionを減らします。

一般的な計画モデルでは、Heretic levelごとに20%の確率で一Candleを減らします。

```text
Heretic 1：20%
Heretic 2：40%
Heretic 5：100%
```

高い値ではGuaranteed reductionと余剰checkに分かれる場合があります。

## 注意

Hereticは、Enemy DominionだけでなくFriendly Dominionも減らし得ます。

自国Templeの中へHereticを長期間置けば、敵がいなくても宗教Networkを弱くする可能性があります。

## 用途

- Enemy Throne・CapitalのCandle削減
- Enemy Pretenderの前線能力低下
- Dominion kill支援
- National heresy mechanics

## Risk

- 自国Dominionも消す
- Patrolで発見される
- StealthとMap Move不足
- Temple破壊より遅い
- Local Candleが0になるとそれ以上働かない

Stone Idol、特殊Commander、Insanity由来の行動、国家固有宗教効果には別処理があります。

---

# Prophet

Prophetは単なる高Holy Priestではありません。

主な機能：

- 移動可能なPassive Dominion source
- 高Holy combat magic
- 常時Bless
- Friendly/Hostile Dominionによる能力変化
- High Morale
- Throne claim
- Armyの宗教的中心

## Frontline Prophet

主力Armyへ同行させると、

- Divine spell
- Banishment
- Bless
- Dominion source
- Throne claim

を一人で担当できます。

しかし死亡すると、

- 前線Spread
- H3級のHoly magic
- Throne claim担当
- 常時Bless Commander

を同時に失います。

## Prophet保護

- Bodyguard
- Rear guard
- Commander分散
- Missile対策
- Assassin対策
- Retreat route
- Enemy Dominion確認

を行います。

詳しい配置は [命令とBattle Script](../basics/orders.md) を参照してください。

---

# Pretender・Disciple・ProphetへのCandle効果

一般的な現行モデルでは、一Candleごとに次の変化があります。

| Local Dominion | HP | Strength | Magic Resistance |
|---|---:|---:|---:|
| Friendly 1 Candle | +10% | +1 | +0.5 |
| Friendly 5 Candles | +50% | +5 | +2.5 |
| Friendly 10 Candles | +100% | +10 | +5 |
| Enemy 1 Candle | -10% | -1 | -0.5 |
| Enemy 5 Candles | -50% | -5 | -2.5 |

Enemy DominionによるHP低下には最低値がありますが、深いEnemy DominionはCombat Pretenderにとって非常に危険です。

## Friendly Dominion

- Pretender、Disciple、Prophetは常時Bless状態
- Pretender・Discipleは同行Sacredを戦闘開始時にBlessできる
- Statsが上昇
- Friendly Armyは通常Morale +1

## Hostile Dominion

- Statsが低下
- Pretender・Discipleは通常Blessを受けられない
- Hostile Armyは通常Morale -1
- Enemy national Dominion effectを受ける場合がある

ProphetはPretender・Discipleと異なり、Friendly Dominion外でも通常のCombat Blessを受けられる場合があります。

## HP表示のTiming

Pretender等のCurrent HPは、Province移動のたびに即座に新しい最大HPへ完全同期するとは限りません。

前TurnのCurrent HPを持ち越し、Turn後半のHealing・Disease処理やBattle・Remote damageで更新されるため、

- Friendly高CandleからEnemy Dominionへ侵攻
- Enemy DominionからFriendly Dominionへ帰還
- Remote attack後のHP

では、Current HPとMax HPの表示を分けて見ます。

---

# PretenderをEnemy Dominionへ出す前の確認

```text
Local Candle：
移動後のHP / Strength / MR：
自動Bless：
Incarnate Bless：
Enemy national effect：
Temperature / Magic / Drain：
Retreat route：
Preach担当：
Temple / Prophet support：
Enemy Assassin / MR attack：
```

## 危険なパターン

- 高HPに見えるAwake ExpanderをBlack Candle 5へ単独侵攻
- MR低下後にSoul Slay・Charm系を受ける
- Friendly Dominionを出てRegeneration等のBlessを失う
- Enemy TemperatureでFatigueが増える
- Retreat先もEnemy Dominion
- Prophetを同じArmyに入れ一度の敗北で宗教sourceを二つ失う

Combat Pretenderの評価は、ChassisのBase statsだけでなく、戦うProvinceのDominionを含めます。

---

# BlessとIncarnate Bless

## 通常Bless

Sacred UnitはPriest、Pretender、Disciple、Item等によりBlessされます。

Bless中はPretender designで選んだ効果が適用され、通常Moraleも上がります。

## Incarnate Bless

高Pathを要求するIncarnate Blessは、Pretenderが世界に存在するときだけ有効です。

次の期間は通常無効です。

- Dormantで未覚醒
- Imprisonedで未覚醒
- Pretender死亡中
- 特殊Plane・Banish等で世界から離れている状態

Sacred ArmyがIncarnate Blessへ依存する場合、Pretenderの生存は国家全体の軍事資源です。

## Dominionと自動Bless

Friendly Dominion内でPretenderまたはDiscipleが戦う場合、同行Sacredは戦闘開始時にBlessされます。

しかし、

- Hostile Dominion
- Pretender不在
- Disciple不在
- Incarnate Bless停止

では同じ編成が同じ性能になりません。

詳しくは [Bless](../pretender/bless.md) を参照してください。

---

# Pretenderの死亡とCall God

Pretenderが死亡すると、

- Pretender由来の三つ相当のSpread
- Incarnate Bless
- Pretender本人のResearch・Forge・Ritual・Combat
- Throne claim能力
- Global caster

を失います。

## Call God

Priestは`Call God`を行い、死亡したPretenderを呼び戻せます。

現行のCommunity testでは、合計約50 Recall Pointsが必要で、各PriestはHoly levelを基礎に毎Turn多少変動するPointsを加えます。

```text
高Holy Priestを複数投入
→ Recallを短縮
→ その間はPreach・Research・Battleへ使えない
```

## 復活Cost

通常のPretenderは復活時に、

- Magic Path loss
- Dominion strength loss
- 一部Affliction回復
- 特殊なPath変化

が起こる可能性があります。

Nature、Death、Immortality、Ur / Uruk、Trinity、Disciple等には例外があります。

正確なRiskは [Pretender God](../pretender/index.md) とゲーム内表示を確認してください。

## 復活地点

通常、PretenderはCapital Provinceへ戻ります。

Capitalを所有していれば、Siege中でもFort内部へ戻る場合があります。

Capitalを失っている場合は、外側へ出現し、Battleへ巻き込まれるRiskがあります。

## Immortal Pretender

Immortalは通常Call Godではなく、固有のReform処理を使います。

Soul-slaying、別Plane死亡、Home Province喪失等は通常のImmortalityを妨げる場合があります。

---

# ScalesはDominionを通じて広がる

Pretender designのScalesは、Friendly Dominionを持つProvinceのCurrent Scalesを毎Turn目標値へ動かします。

```text
PretenderのScale設計
        ↓
Local Dominion
        ↓
ProvinceのCurrent Scalesが少しずつ近づく
```

Candleを置いた瞬間に、全Scaleが一度で設計値へ変わるわけではありません。

## Scale移行の計画用モデル

現行のCommunity modelでは、各Scaleが一Step目標へ動く確率は概ね、

```text
10% × 目標との差の絶対値
＋ 5% × Local Friendly Candle
```

です。

確率が100%を超える場合、複数Step動くことがあります。

### 例

Current Growth 0、Pretender Growth 3、Local Candle 4なら、

```text
10% × 3
＋ 5% × 4
＝ 約50%
```

で一Step近づく計画になります。

## Scaleが設計値と違う原因

- Candleが低い
- Dominionが最近変わった
- Enemy Dominionから奪った直後
- Magic Site
- Event
- Ritual
- Season
- Extreme Scaleの隣接圧力
- National effect
- Throne effect
- Terrain変化

Scalesを確認するときは、Pretender design画面だけでなく、実際のProvince表示を見ます。

---

# Hostile Dominion下のScales

Enemy Dominion下のOwned Provinceでは、すべてのScaleが同じように働くわけではありません。

## Positive経済Scaleが無効になるもの

一般に、Owned ProvinceがHostile Dominion下にある場合、

- OrderのPositive部分
- ProductivityのPositive部分
- LuckのPositive部分
- MagicのResearch bonus

を自国が受けられません。

## Negative Scaleは残る

- Turmoil
- Sloth
- Misfortune
- Drain

のPenaltyはHostile Dominionでも作用します。

つまりEnemy Dominion下では、

> 良いScaleは奪われるのに、悪いScaleは残る

という不利な状態になり得ます。

## Growth / DeathとTemperature

Growth / Death、Heat / ColdはLocal環境としてPopulation、Supply、Aging、Temperature等へ作用し、Ownershipだけでは無効になりません。

## Magic / DrainのCombat effect

Magic / DrainによるSpell Fatigue等のLocal battle effectは、Research bonusとは異なり、Dominionの所有関係にかかわらず作用するものがあります。

```text
Friendly Magic Scale
＝ Research bonus ＋ Battle magic環境

Hostile Magic Scale
＝ Research bonusは得にくい
  しかしLocal Spell Fatigue等は残る場合がある
```

Scaleの一語だけで全効果をまとめないでください。

詳しくは [Scales](../pretender/scales.md) を参照してください。

---

# 六つのScale軸とDominion戦

| Scale | Friendly時の主用途 | Enemy Dominion下での注意 |
|---|---|---|
| Order / Turmoil | Income、RP、Unrest、Event | Positive Orderを失い、Turmoilは残る |
| Productivity / Sloth | Resources、重装生産 | Positive Productivityを失い、Slothは残る |
| Heat / Cold | Income、Supply、Encumbrance、Season | Local Temperatureとして作用 |
| Growth / Death | Population、Supply、Aging | Local環境として作用 |
| Luck / Misfortune | Event、Hero | Positive Luckを失い、Misfortuneは残る |
| Magic / Drain | Research、MR、Spell Fatigue | Research bonusとBattle effectを分離 |

Enemy Dominionを放置すると、Provinceを所有していても、Pretender designで購入した良Scaleの利益を受けられない場合があります。

宗教戦は、Candleの勝敗だけでなく、Scalesへ払ったDesign Pointを実際の国力へ変換できるかという戦争です。

---

# Extreme Scales

Dominions 6では、一部国家・Pretenderが通常範囲を越えるScale 4～5を選べます。

Extreme Scaleは通常の延長だけではなく、追加Effectを持ちます。

代表的な方向：

- Extreme OrderによるResearch penalty
- Extreme Productivity / MagicによるUnrest
- Extreme Heat / ColdによるPopulation death
- Extreme Growth / DeathによるTerrain変化
- Extreme LuckによるIncome・Resources penalty
- 周辺ProvinceへScale圧力

公式Dom6変更点でも、Extreme Scalesと長期的Terrain alterationが新要素として挙げられています。

## 攻略上の意味

Extreme Scale国家と戦う場合、Provinceを占領してCandleを変えても、

- Current Scale
- Terrain
- Population damage
- Site・National effect

は即座には元へ戻りません。

> **宗教を押し返すTurn**

と、

> **土地が回復するTurn**

を分けて考えます。

---

# Army MoraleとDominion

通常、Armyは、

- Friendly Dominion：Morale +1
- Hostile Dominion：Morale -1

の影響を受けます。

一見小さい差ですが、

- Fear
- 大損害
- Commander死亡
- Fatigue
- Chaff
- Long battle

と組み合わさると、Rout Timingを変えます。

Enemy Dominionへ侵攻するときは、Damage・ProtectionだけでなくMorale層も確認します。

詳しくは [戦闘ルール](../basics/combat-rules.md) を参照してください。

---

# 国家固有Dominion効果

国家によってFriendly Dominionは、Scales carrier以上の役割を持ちます。

代表的な種類：

- Population kill
- Freespawn
- Disease
- Insanity
- Scrying
- Temperature spread
- Terrain change
- Construct HP
- Sailing・Movement条件
- Enemy Income penalty
- Temple spawn
- Unrest
- Dominion conflict bonus
- Restricted spread

## Candle数との関係

国家効果は、

- Dominionが1以上あれば有効
- Candle数に比例
- Fort・Templeが必要
- Scalesに比例
- Ownerだけ、Enemyだけ、Discipleにも作用

など条件が異なります。

国家攻略記事では、必ず次を確認します。

```text
Dominion effect：
発動条件：
Candle数依存：
Owner / Enemy / Disciple：
Fort / Temple依存：
Counter：
```

## National exceptionを一般則へしない

Mictlan、Ermor、Therodos、R'lyeh、Phaeacia、Marignon等の挙動を、全国家のDominionへ一般化しないでください。

国家選択画面のSpecial Feature、Unit ability、実際のMessageを優先します。

---

# Dominion kill

自国Dominionが世界の全Provinceから消えると、国家は敗北します。

領土、Fort、Army、Pretender、Throneを持っていても救われません。

## 危険信号

- White Candle ProvinceがCapital周辺だけ
- Base Dominionが低い
- Temple 5棟Breakpointへ届かない
- Prophet死亡
- Pretender死亡・未覚醒
- Capital包囲
- Enemy Blood Sacrifice
- 複数国家からBlack Candleが入る
- Sea・Planeで宗教Networkが分断
- Temple Raidを繰り返される
- Hereticを発見できない
- 国家がRestricted / Dying Dominion

## 緊急対応の優先順

1. White Candleが残るProvinceを確認
2. Temple・Capital・Throne・PretenderのSpread sourceを数える
3. PriestをPreachへ回す
4. Prophet・Pretenderを安全な宗教Frontへ移動
5. 5Temple breakpointを完成
6. Enemy Temple・Sacrifice拠点をRaid
7. Heretic・Stealthy PriestをPatrol
8. Blood Sacrifice可能ならSlaveを集中
9. Capital Siegeを解除
10. 無関係な戦争を止める

## Dominion kill攻撃

Enemyを宗教的に消すには、単にBlack Candleを押すだけでなく、Enemy sourceを破壊します。

```text
Enemy Temple破壊
＋ Prophet / Priest排除
＋ Pretender死亡
＋ Capital Siege
＋ Sacrifice拠点破壊
＋ 自国Temple・Preach
＝ Dominion Network崩壊
```

Armyを倒さずに宗教だけで勝つこともできますが、Enemy ArmyがTempleを破壊し返すため、領土戦と宗教戦は相互依存します。

---

# Templeを建てる場所

## Capital圏

目的：

- Dominion kill耐性
- Sacred・Priest recruitment
- Pretender recall地点の保護
- 5Temple breakpoint

CapitalだけにTempleを集中すると、前線へ信仰が届くまで時間がかかります。

## Mage Fort

Sacred Mage・Priest・Sacred Commanderを毎Turn雇うFortでは、Templeは生産設備です。

Templeを後回しにすると、FortとLabがあっても計画したMageが出ません。

## Border Fort

目的：

- Enemy Dominion除去
- Friendly Scales定着
- Combat Pretender支援
- Fort storm条件
- Enemy national Dominion effect除去

Risk：

- Raidで破壊
- Enemyに奪われる
- 前線GoldをArmyから奪う

## Choke・Plane入口

宗教Networkが分断される場所へ置きます。

- Land / Sea境界
- Cave入口
- Void入口
- Island
- 一方向接続

## Throne

Claimed ThroneのSpreadとTempleを重ね、Victory Point、Claim Priest、Dominion、Scalesを守ります。

## Blood Sacrifice hub

Blood Slave輸送、Eligible Priest、Temple、Lab、Patrolを一つの後方拠点へ集めます。

ただし一か所へ集中しすぎると、Raid一回で宗教力を失います。

---

# Temple投資のOpportunity Cost

Templeは強力ですが、同じGoldで、

- Mage
- Fort
- Laboratory
- Army
- Province Defence
- Mercenary

も購入できます。

## Templeを急ぐ状況

- Sacredを各FortでRecruit
- 次の5棟Breakpointが近い
- Enemy Dominionが前線を越えた
- Blood Sacrificeを開始
- Throne claim
- Pretender・Discipleが前線で戦う
- Strong national Dominion effect
- Dominion kill Risk

## Templeを遅らせる状況

- Rush防衛が最優先
- そのFortでSacredを雇わない
- Enemyから遠い安全なMage-only Fort
- 次のBreakpointが遠い
- Goldが第二Army・第二Fortを止める

Templeを「宗教建物だから何となく建てる」のではなく、

```text
Spread source
＋ Sacred production
＋ Preach bonus
＋ 5Temple breakpoint
＋ National effect
```

のうち何を買っているか書きます。

---

# 宗教戦の三つのScale

## Local battle

対象：一つのProvince

手段：

- Preach
- Inquisitor
- Prophet
- Pretender
- Heretic

目的：

- 今TurnのBattle条件を変える
- Enemy national effectを消す
- PretenderのStatsを変える

## Frontline network

対象：数Provinceの戦線

手段：

- Border Temple
- Mobile Priest
- Claimed Throne
- Blood Sacrifice
- Temple Raid

目的：

- Scalesを前線へ定着
- Retreat・Fort・Throneを宗教的に守る
- Enemy Spread sourceを削る

## Strategic elimination

対象：Enemy国家全体

手段：

- Capital Siege
- Temple network破壊
- Pretender・Prophet排除
- Sacrifice hub破壊
- Multi-front Dominion pressure

目的：Dominion kill

三つを混ぜると、H1 Priestを十人並べてLocal Candleだけ上げ、Enemy Temple networkを放置するような非効率が起こります。

---

# Frontline Dominion計画

```text
Front Province：
現在Ownership：
現在Candle：
Enemy Effective Dominion：
自国Effective Dominion：
自国Temple：
Enemy Temple：
Preach担当：
Inquisitor：
Prophet位置：
Pretender位置：
Blood Sacrifice：
今TurnのBattle：
必要なFriendly Candle：
Enemy national effect：
Retreat route：
```

## 一Turnで必要なものを分ける

```text
今TurnのBattleへ必要
→ Preach、Prophet、Pretender、Local ability

次Turn以降のNetworkへ必要
→ Temple、Throne、Passive spread、Scales定着
```

この区別が最も重要です。

---

# Disciple Game

Disciple Gameでは、Team内に一人のPretenderと複数のDisciplesがいます。

Disciplesは独自のDominion・Scales・Blessを持たず、Team Pretenderの宗教を共有します。

## 共有されるもの

- Dominion
- Scales
- Bless
- Holy Pointsの基準
- TeamのDominion kill運命

## Disciple

DiscipleはPretenderに似たUnitで、

- Friendly DominionでStats上昇
- Friendly Dominionで自動Bless
- Throne claim
- 死亡時Recall

を持ちます。

## Prophet

通常のDisciple Gameでは、Discipleが宗教上Prophetの位置を占めるため、通常Gameと同じProphet任命を行いません。

## Temple breakpoint

Team GameではEffective Dominion strengthを上げるTemple数の計算がTeam規模に合わせて変わります。

一人用Gameの「5Templeごと」をそのまま当てはめず、Team全体のTemple数と各Playerの建設計画を共有します。

## National Dominion effect

国家固有Dominion効果は、

- Team全体へ継承
- Pretender nationだけ発生
- Disciple nation自身だけ発生
- Discipleには継承されない
- Enemyと同様にDiscipleも被害

など国家ごとに異なります。

> **Disciple nationの特殊Dominion効果が、自動的にTeam Dominionへ追加されるとは限りません。**

ゲーム開始前に各国家のSpecial Featureを確認します。

## Recall

Team PriestsはMain PretenderのCall Godへ協力できます。

DiscipleのRecallは、自国PriestとTeam Priestの役割に制約があります。

詳しくは [Disciple Game](disciple-game.md) を参照してください。

---

# 実戦例

## 例1：Storm前にEnemy Candle 3

### 状況

- Wall 0
- Defender PretenderがFort内
- Local Enemy Candle 3
- AttackerにH3 PriestとTempleあり

### 問題

そのままStormすると、Defender PretenderはFriendly Dominion bonusを受け、AttackerはHostile Dominion penaltyを受けます。

### 対応

```text
H3 Priest：Preach
Storm Army：Storm Castle
```

Preachが成功すれば、Storm処理前にEnemy Candleを減らし、戦場条件を変えられます。

Passive Temple spreadだけでは同TurnのStormへ間に合いません。

---

## 例2：Templeが4棟から5棟へ

### 状況

- Base Dominion 5
- Temple 4
- Sacredを各Fortで量産

### 変化

5棟目により、通常はEffective Dominion strengthが6になります。

得られるもの：

- 追加Temple check source
- Enemy Dominion conflict強化
- 各FortのHoly Points増加

単なる「Temple一棟分」の価値ではありません。

---

## 例3：White Candle 6だがSacredが6体出ない

### 原因候補

- Effective Dominionは4
- UnitがHoly Points 2を使う
- Resources不足
- Recruitment Points不足
- Templeなし
- 複数Turn recruit

Local Candleを見ず、Recruit画面のHoly PointsとBottleneckを確認します。

---

## 例4：Awake PretenderがEnemy Candle 5へ侵攻

### 変化の目安

- HP -50%
- Strength -5
- MR -2.5
- 自動Bless喪失
- Army Morale -1

Base statsだけを見たExpansion testとは別のUnitとして扱います。

Preach、Prophet、Temple、Retreat routeなしの単独侵攻は避けます。

---

## 例5：自国Order 3なのに前線Incomeが低い

### 原因候補

- Enemy Dominion
- Current ScaleがまだTurmoil
- Tax route切断
- Unrest
- Temperature
- Site・Event

Pretender designのOrder 3は、所有する全Provinceへ自動適用される全国Buffではありません。

---

## 例6：Blood SacrificeでIsland国家を圧迫

### 状況

- Land / Sea境界でPassive spreadが弱い
- DefenderのTemple数が少ない
- AttackerがBlood Slaveを継続供給

### 戦術

- Coastal / Underwater TempleでSacrifice
- Defender TempleをRaid
- Prophet・High PriestをAssassinate
- 複数点からTemple checksを発生

地理的に届きにくいDominionを、Blood economyで強制的に押します。

---

## 例7：CapitalとArmyがあるのにDominion kill寸前

### 症状

- White CandleがCapitalの1本だけ
- Pretender死亡
- Prophet死亡
- Temple 3棟
- EnemyがSacrifice

### 優先行動

1. Capital PriestをPreach
2. Temple 5棟Breakpointを完成
3. Eligible PriestをCall GodとPreachへ分担
4. Enemy Sacrifice TempleをRaid
5. Capital Siegeを防ぐ

Field warでProvince一つを取るより、宗教sourceを一つ守る方が重要です。

---

## 例8：Enemy Dominionを取ったがScalesが戻らない

### 理由

Dominion changeとScale changeは別処理です。

White Candle 1へ変わっても、Current Death 3、Misfortune 2、Drain 2が即座に設計値へ戻るとは限りません。

### 対応

- Candleを増やす
- Templeを維持
- 数Turn待つ
- Site・Event・Extreme Scaleを確認

---

## 例9：Disciple nationのDominion効果を期待したが発生しない

### 原因

National Dominion effectがDiscipleからTeamへ継承されない種類だった可能性があります。

Disciple Gameでは、Pretender nationがTeam Dominionの性質を決めるEffectが多く、国家ごとの例外があります。

---

## 例10：Prophetを主力Armyと同時に失う

### 損失

- Army Commander
- High Holy magic
- Mobile Temple check
- Throne claim担当
- 常時Bless Commander
- 前線宗教支援

Prophetを単なる無料H3として消耗させず、宗教NetworkのUnique assetとして扱います。

---

# 症状から原因を探す

| 症状 | 最初に疑うもの |
|---|---|
| Templeを増やしたが前線Candleが増えない | Check失敗、後方吸収、経路、Land/Sea |
| Preachしても増えない | Holy level、Enemy Candle、Local上限 |
| White CandleだがScalesが悪い | Scale移行遅延、Site、Event、Season |
| Sacredを予定数Recruitできない | Holy Points、Temple、RP、Resources |
| PretenderのHPが予定より低い | Hostile Candle、Current/Max HP Timing |
| SacredがBlessされていない | Hostile Dominion、Priest不在、Incarnate停止 |
| 前線Armyが早くRoutする | Hostile Dominion、Fear、Leadership |
| 自国Provinceで良Scaleが効かない | Hostile Dominion、Current Scale |
| Blood Sacrificeができない | National ability、Temple、Priest、Slave |
| Dominionが自国でも減る | Heretic、Event、特殊国家、Enemy Preach |
| Temple 5棟なのにTeam値が上がらない | Disciple GameのTeam breakpoint |
| FortがあるのにDominion kill寸前 | Spread source不足、Capital Siege、Pretender死亡 |
| Incarnate Blessが消えた | Pretender未覚醒・死亡・世界外 |
| Enemy Templeを壊してもBlack Candleが残る | Pretender、Prophet、Capital、Throne、他Temple |

---

# Dominion設計Checklist

```text
Nation / Age：
Base Dominion strength：
Sacred Holy Point cost：
各FortのSacred生産目標：
National Dominion effect：
Restricted / Dying Dominion：
Blood Sacrifice：
Pretender combat role：
Incarnate Bless：
Temple 5棟Timing：
Enemy Dominion threats：
Land / Sea / Plane境界：
Dominion kill Risk：
```

---

# 毎Turn確認Checklist

```text
総Temple数：
次の5Temple breakpoint：
White Candleが残るProvince数：
Capital Candle：
Frontline Candle：
Prophet位置：
Pretender状態：Awake / Dormant / Dead / Other Plane
Call God進捗：
Enemy Sacrifice拠点：
Enemy Temple：
Heretic / Stealthy Priest情報：
今TurnのStorm / Break Siege：
Preach担当：
```

---

# Enemy Dominionで戦う前のChecklist

```text
Local Candle：
Army Morale modifier：
Pretender / Prophet / Disciple stats：
Bless activation：
Incarnate Bless：
Temperature：
Magic / Drain：
Enemy national Dominion effect：
PreachはBattle前に間に合うか：
Temple / Prophet支援：
Retreat先のDominion：
```

---

# Dominion kill防衛Checklist

```text
最後のWhite Candle Province：
Capital ownership / Siege：
Temple数：
Spread source数：
Pretender状態：
Prophet状態：
Preach可能Priest：
Blood Sacrifice：
Enemy Temple Raid候補：
Enemy Sacrifice hub：
Call GodとPreachのPriest配分：
救援Army：
```

---

# よくある誤解

## Dominion strengthとLocal Candleは同じ

違います。

Design・Templeで決まる宗教強度と、各Provinceの現在Candleを分けます。

## Temple一棟は毎Turn必ず一Candleを増やす

違います。

Templeはcheckを発生させ、成功率と配置処理があります。

## Provinceを所有すれば自国Scalesが作用する

違います。

Hostile Dominion下ではPositive Scaleの利益を失う場合があります。

## White CandleになればScalesも即座に直る

違います。

Scalesは時間をかけて目標へ動きます。

## Local CandleがSacred生産数を決める

通常はEffective Dominion strengthとHoly Point costです。

## PreachとPassive spreadは同じ

違います。

PreachはLocalでBattle前、Passive spreadはNetwork型でTurn後半です。

## PretenderはEnemy DominionでもPriestにBlessしてもらえる

Pretender・DiscipleはFriendly Dominion外では通常Blessを受けられません。

## TempleをCapitalだけに置けば安全

前線Scales、Storm、Sacred生産、Land/Sea境界へ宗教が届きにくくなります。

## Armyが強ければDominion killされない

Candleが世界から消えればArmy数にかかわらず敗北します。

## Disciple国家のDominion効果はすべてTeamへ追加される

国家ごとに継承規則が異なります。

---

# 追加検証が必要な項目

今後、6.35上で独立Testを行う価値が高いものです。

- Temple checkの全端数処理
- 同一Phase内の複数国家Dominion conflict順
- EventによるLocal上限超過
- Land / Sea境界の全例外
- Plane connectionを越えるPassive spread
- Siege中のPriest・Temple・Siteの全処理
- Blood SacrificeとHereticの厳密な同Turn順
- 特殊国家のTemple / Prophet / Capital checks
- Disciple TeamのTemple breakpoint表示
- Local Candle変化とCurrent HP更新の全Timing
- Prophet再任命の特殊例外
- Call GodのPoints、Path loss、Immortality例外
- Extreme ScaleのTerrain変化確率
- National Dominion effectのDisciple継承一覧

不明点を一般則で埋めず、国家・Unit・Event単位の検証記事へ分離します。

---

## 関連ページ

- [Pretender God](../pretender/index.md)
- [Scales](../pretender/scales.md)
- [Bless](../pretender/bless.md)
- [Holy](../magic/paths/holy.md)
- [Province](province.md)
- [Fort・Siege・Storm](forts.md)
- [Throne of Ascension](thrones.md)
- [Disciple Game](disciple-game.md)
- [ターン処理順](../reference/turn-resolution.md)
- [命令とBattle Script](../basics/orders.md)
- [戦闘ルール](../basics/combat-rules.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
- [Illwiki: Dominion](https://illwiki.com/dom5/dominion)
- [Illwiki: Dom6 Scales](https://illwiki.com/dom5/dom6/scales)
- [Illwiki: Dom6 Pretenders](https://illwiki.com/dom5/dom6/pretenders)
- [Illwiki: Dom6 Holy](https://illwiki.com/dom5/dom6/holy)
- [Illwiki: Dom6 Sacred](https://illwiki.com/dom5/dom6/sacred)
- [Illwiki: Disciples](https://illwiki.com/dom5/disciples)
