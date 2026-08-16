---
title: Disciple Game・Team設計・共有Dominion
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# Disciple Game・Team設計・共有Dominion

Disciple Gameは、複数Playerが一つのTeamとして戦うGame modeです。

ただし、一般的な協力Strategy Gameのように、Gold、Research、Army、Battlefieldをすべて一つへ統合するModeではありません。

> **一つのPretender God、Dominion、Scales、Bless、Ascension Pointを共有しながら、各Playerは別々の国家・Treasury・Research・Armyを運営するTeam Game**

です。

一つのTeamには、

- 一人のPretender Player
- 0人以上のDisciple Player

が存在します。

Pretender PlayerはTeamの宗教設計を担当します。

Disciple Playerは、自国の経済・研究・軍事を運営しながら、共有Pretenderの勝利を支えます。

Disciple Gameを理解するうえで最も重要なのは、

```text
共有されるもの
```

と、

```text
各国家に分かれたままのもの
```

を混同しないことです。

!!! note "このページの精度範囲"
    本文はDominions 6.35を対象に、現行Manualへの公式導線、公式Dom6変更点、ゲーム内Team設定・Pretender design・Message・Turn処理、[Dominion](dominion.md)、[Throne](thrones.md)、[ターン処理順](../reference/turn-resolution.md)、および現行Community資料で確認されている主要挙動を実戦向けに整理しています。国家固有Dominion効果のTeam継承、特殊Event、Modded Game、AI Team、別Plane、同一Phase内の複数Team処理には例外があります。そのため記事Statusは`reviewed`であり、全内部処理を実験的に証明した`verified`ではありません。

---

## 最初に覚える十項目

### 1. TeamにはPretenderが一人だけ

各Teamには、必ず一人だけPretender Playerが必要です。

それ以外のTeam memberはDiscipleになります。

Team人数は同数である必要がなく、

- Pretender一人だけのTeam
- Pretender一人＋Disciple一人
- Pretender一人＋Disciple三人

のような構成も可能です。

Game balanceとして公平かどうかは別問題です。

### 2. TeamのBless・Scales・DominionはPretenderが決める

Team全体で使う、

- Bless
- Scales
- Base Dominion strength
- Awakening category
- 宗教由来の一部特殊効果
- PriestのCustom Banishment / Smite系統

は、Team Pretenderの設計を基準にします。

Disciple自身のMagic Pathは、Team Blessを追加しません。

### 3. Discipleは自分のChassisとMagic Pathを設計する

標準Dom6では、Pretenderは通常450 Design Point、Discipleは400 Design Pointを使います。

Discipleは、

- Chassis
- Magic Path

を選びますが、自分専用のDominion、Scales、Bless、Awakening categoryは選びません。

利用できるChassis poolもPretenderとDiscipleで異なるため、Game内Design画面を確認してください。

### 4. DiscipleはPretenderより早くAwakeする

Team PretenderがAwakeなら、DiscipleもGame開始時から存在します。

PretenderがDormantまたはImprisonedの場合、Discipleは通常、そのPretenderより早くAwakeします。

ただしTurnはRandom性を持ちます。

> **Discipleが先にAwakeしても、Team Pretenderが不在ならIncarnate Blessは有効にならない**

点が重要です。

### 5. DiscipleはProphetの代替だが、H3 Priestではない

Discipleは、

- Mobile Dominion source
- Dominionによる能力増減
- Friendly Dominionでの常時Bless
- Throne Claim能力

を持つProphet的存在です。

しかしDiscipleは通常、Holy Magicを使うPriestではありません。

```text
Disciple
≠
H3 Priest
```

です。

TeamにDiscipleがいる場合、通常のProphetを任命できません。

PretenderしかいないTeamではProphetを任命できる場合があります。

### 6. Teamは一つのDominionを共有する

Disciple国家は自分専用Dominionを持ちません。

Team memberのCapital、Temple、Disciple、Pretender、Claimed Throne等は、同じTeam Dominionを広げます。

Team Dominionが消滅するRiskは、Team全体の宗教的敗北Riskです。

### 7. Gold・Gem・Research・Armyは自動共有されない

各国家は別々に、

- Gold Treasury
- Gem / Blood Slave stock
- Research level
- Unit / Commander
- Fort / Lab / Temple
- Recruit queue
- Province Defence
- Hero / Event

を管理します。

Team memberがAlteration 5へ到達しても、自国のAlterationは解禁されません。

必要な資源、Gem、Itemは、Message等で明示的に送ります。

### 8. Team memberのArmyは一つのBattleへ合流しない

二人のTeam memberが同じEnemy Provinceを攻撃しても、通常は一つのArmy Setupへ統合されません。

別々の国家として、別々のBattleを戦います。

そのため、

- 同じFormationを共有する
- Ally Mageが自軍へBuffする
- Ally Commanderが自軍兵を指揮する
- Foul Vapors耐性をTeam全体で一つのBattleへ合わせる

ことはできません。

Disciple Gameの協力は、Battlefield統合より**戦略Map上の分業**が中心です。

### 9. Ascension Pointと勝利はTeamで共有する

Team memberがClaimしたThroneのAscension Pointは、Teamの勝利条件へ加算されます。

Pretender、Disciple、H3以上のPriestはClaim担当になれます。

一方、Throne ProvinceのLocal income、Recruitment、Site効果などは、Province owner側へ帰属する要素があります。

```text
Victory PointはTeam共有
Local運用資源は国家別
```

と考えます。

### 10. 国家固有Dominion効果は必ず個別確認する

Pretender国家のDominion効果がDisciple国家へ及ぶ場合があります。

しかし、

- Team全体へ継承される
- Pretender国家だけに作用する
- Disciple国家が自分の能力を維持する
- Discipleになると失われる
- Team memberにも有害

という違いがあります。

Popkill、Freespawn、Insanity、Terrain変化、Blood Sacrifice、Scrying、Sailing等を「Teamなら全部共有」と推測しないでください。

---

# Disciple Gameの全体構造

```text
Team Pretenderを選ぶ
        ↓
共有Bless・Scales・Dominionを設計
        ↓
各Discipleが不足Pathと役割を設計
        ↓
各国家が別々にExpansion・Research
        ↓
Gold・Gem・Item・Provinceを交換
        ↓
戦線・研究School・Magic Pathを分担
        ↓
Team Dominionを維持
        ↓
複数Throneを攻略・Claim
        ↓
Team Ascension Pointで勝利
```

この流れのどこか一つだけを最適化しても、Team全体は強くなりません。

強いBlessを作っても、Disciple国家のSacredと合わなければ無駄になります。

Magic Pathを広げても、各国家が同じResearch Schoolを重複して上げればTimingを失います。

Throneを攻略しても、ClaimantがいなければPointになりません。

---

# Game Setup

## Team編成

Game作成時に、各Playerへ、

- Team number
- Pretender / Disciple
- Nation

を割り当てます。

各TeamにはPretenderが一人だけ必要です。

Disciple数は0人以上です。

## Team人数

Team人数が多いほど、

- 国家数
- Capital数
- Initial Army数
- Recruit可能Mageの種類
- Gem income
- Researcher数
- Front数

が増えます。

一方で、

- Temple breakpointが重くなる
- 意思決定が遅くなる
- Resource要求が競合する
- Map上で開始位置が離れる
- Bless・Scalesの妥協が増える

というCostがあります。

単に人数が多ければ連携が簡単になるわけではありません。

## Team人数が不均衡なGame

Team人数が異なる場合、総Capital、総Gold、総Research、総Armyが大きく変わります。

AIを含むCo-op Gameでは意図的に不均衡にすることもできますが、対人戦では、

- Player数
- Nation strength
- Start位置
- Throne配置
- AI difficulty
- Research設定

を合わせて評価します。

## 最初に確認するGame設定

- Age
- MapとPlane
- Team数・人数
- Research difficulty
- Independent strength
- ThroneのLevel別個数
- 勝利に必要なAscension Point
- Cataclysm
- Story Event
- Diplomacy設定
- AI / Human
- Mod

Disciple Gameでは、通常Game以上にGame設定がTeam設計へ影響します。

---

# PretenderとDiscipleの違い

| 項目 | Team Pretender | Disciple |
|---|---|---|
| Team内人数 | 一人 | 0人以上 |
| 標準Design Point | 450 | 400 |
| Blessを決める | する | しない |
| Scalesを決める | する | しない |
| Base Dominionを決める | する | しない |
| Awakening categoryを決める | する | Team Pretenderに従う |
| Chassis / Pathを選ぶ | する | する |
| Dominion spread | Pretenderとして強い | Prophet相当のsource |
| Throne Claim | 可能 | 常に可能 |
| Holy spell | 通常使えない | 通常使えない |
| Incarnate Blessの存在条件 | 本人の存在 | Disciple本人では有効化しない |
| Team victory上の役割 | 宗教・Designの中核 | 戦線・Magic・Claimの分担 |

## Team Pretenderの責任

Team Pretender designは、一国家だけのBuildではありません。

次を同時に評価します。

- 全Team memberのSacred
- 全国家のTemperature preference
- Gold / Resource制約
- Living / Undead / Demon構成
- Blood economy
- Magic / Drain耐性
- National Dominion effect
- Team全体の不足Path
- Incarnate Blessの必要Timing
- Throne ClaimとGlobal caster

Team Pretender Playerが、自国だけに最適なBuildを選ぶと、他のDisciple国家が数十Turnにわたり不利なScalesとBlessを背負います。

## Discipleの責任

Disciple designは、Blessを作る設計ではありません。

主な役割は、

- TeamにないMagic Path
- Booster chain
- Site Search
- Global / Ritual caster
- Early combat
- Throne Claim
- Mobile response
- Supercombatant
- Forge access
- Resistance補完

です。

DiscipleのPathは、Team PretenderのBless Pointへ加算されません。

そのため、

> **Team Blessを良くするためにDiscipleが高Pathを取る**

という設計は成立しません。

---

# Awakening

## Awake Team

Team PretenderがAwakeなら、DiscipleもGame開始時から利用できます。

### 利点

- 複数のEarly Expander
- 即時Site Search
- Early Forge
- Early Magic diversity
- Mobile Dominion source
- Throne Claim準備

### Cost

Team Pretender側はAwake Costを払い、Scales・Bless・Pathを削ります。

Disciple側も400 Point内でChassisとPathを完成させる必要があります。

## Dormant Team

Pretenderは後から登場し、Discipleは通常それより早くAwakeします。

### 利点

- DiscipleがFirst war前に参加しやすい
- Pretender側が追加Design Pointを得る
- DiscipleがSite Search・Expansionを先行

### 注意

Team Pretenderがまだ不在なら、Incarnate Blessは停止したままです。

```text
DiscipleがAwake
≠
Incarnate BlessがActive
```

です。

## Imprisoned Team

Pretenderは長く不在で、Discipleはおおむねその中間期にAwakeします。

### 利点

- 強いTeam BlessまたはScales
- DiscipleがPretenderより早く中盤役を開始

### Risk

- Incarnate Blessが長期間停止
- Main PretenderのGlobal・Forgeが遅い
- Team Dominionの強いsourceが不在
- Pretender本人が必要なThrone planが遅い

## Awakeningは固定Turnではない

AwakeningにはRandom性があります。

Community testではDisciple用の早いAwakening分布が確認されていますが、作戦では、

```text
最速で出た場合
通常Timing
遅れた場合
```

の三つを用意します。

---

# Incarnate Bless

Incarnate Blessは、Team Pretenderが世界に存在している間だけ有効です。

通常、次では停止します。

- Dormantで未Awake
- Imprisonedで未Awake
- Team Pretender死亡中
- 世界外・特殊Plane

Discipleが生存していても代替できません。

TeamのSacred ArmyがIncarnate Blessへ依存する場合、Team Pretenderの状態は全国家共通の軍事Resourceです。

## Incarnate依存の確認

```text
Team PretenderのAwakening予測：
First war予定Turn：
IncarnateなしでExpansion可能か：
IncarnateなしでFirst war可能か：
Pretender死亡時の代替Army：
Call God担当Priest：
```

---

# Team Bless

Team member全員のSacredは、Team Pretenderが選んだ同じBlessを使います。

## Blessを一国家だけで決めない

各国家について、次を表にします。

| Nation | Sacred数 | 攻撃回数 | 主な弱点 | Capital-only | Mage Sacred | Summon Sacred |
|---|---:|---:|---|---|---|---|
| A | 多い | 多い | Shock | Yes | 少ない | 中盤 |
| B | 少ない | 一撃 | Fatigue | No | 多い | なし |
| C | 中程度 | 多段 | MR | Yes | なし | 終盤 |

この表から、Team全体で価値の高いBlessを選びます。

## BlessのTeam適性

### 多数の通常Sacred

- Attack
- Strength
- Weapon effect
- Morale
- Elemental Resistance

の価値が高くなります。

### Giant・高HP Sacred

- Regeneration
- Reinvigoration
- Resistance
- Defence
- Recuperation

を評価します。

### Sacred Mage・Commander

- Reinvigoration
- MR
- Resistance
- Recuperation
- Undying
- Strategic innate effect

が重要です。

### Sacred Summon中心

Early gameではBlessへの投資を回収できません。

Research、Gem income、Summon Timingまで確認します。

## Innate Bless

Strategic mapでも常時作用するInnate Blessは、Team全体へ長く価値を与えます。

ただし、

- Underwater access
- Survival
- Recuperation
- Half Dead
- Inspirational effect

が、全国家で同じ価値を持つとは限りません。

## Bless妥協の原則

Team Blessは、全国家へ100点を与える必要はありません。

次の優先順位が実用的です。

1. Teamの主力Sacredへ必須Counterを与える
2. 複数国家で再利用できるResistanceを取る
3. Sacred MageとCommanderの生存を上げる
4. 一国家だけの贅沢な攻撃Blessを削る
5. Incarnate依存とAwakening Timingを確認する

---

# ScalesをTeamで設計する

Scalesは、Team member全員のProvinceへDominionを通じて広がります。

Team Pretender国家だけの経済設定ではありません。

## Order / Turmoil

確認するもの：

- Team全体のGold需要
- Blood HuntによるUnrest
- Freespawn国家
- Event economy
- Fort建設数
- Mage upkeep

通常兵・Mage・Fortを多く使うTeamではOrderの累積価値が高くなります。

Turmoilを必要とする国家固有能力がある場合は、他Team memberが失うIncomeと比較します。

## Productivity / Sloth

確認するもの：

- Heavy Infantry
- Cavalry
- Giant
- Resource-heavy Sacred
- Summon中心国家
- Mage-only Fort

一国家が軽装・Summon中心でも、他の二国家が重装ならSlothはTeam全体へ大きなCostになります。

## Heat / Cold

最も衝突しやすいScaleです。

各国家について、

- Preferred Temperature
- Cold Blooded
- Heat / Chill Aura
- Fire / Water magic
- Seasonal movement
- Supply

を確認します。

```text
Pretender nation：Heat 2 preferred
Disciple A：Cold 2 preferred
Disciple B：Cold Blooded
```

のようなTeamでは、誰かが毎TurnPenaltyを受けます。

Nation選択の時点で解決すべき問題です。

## Growth / Death

確認するもの：

- Living population economy
- Blood economy
- Popkill
- Undead国家
- Supply
- Long game
- Old age Mage

Popkill PretenderとLiving Gold国家を組ませる場合、Team memberのPopulationまで失われる可能性があります。

## Luck / Misfortune

Random Eventは各国家・Provinceで発生します。

Team全体で見ると、Province数が多いため、期待値とRiskの両方が増えます。

- Event耐性
- Fort数
- Story Event
- Turmoil
- Treasury reserve

を確認します。

## Magic / Drain

Researchは国家別ですが、ScaleはTeam共有です。

Magicは、各国家のResearcherとBattle Mageへ利益を与えます。

Drainを許容できる国家が一つあっても、他二国家がMage-heavyならTeam全体では高Costです。

---

# 共有されるもの・共有されないもの

## 基本表

| 分類 | Team共有 | 国家別 |
|---|---|---|
| Team関係 | Ally / Victory | Nation identity |
| Dominion | 一つのTeam Dominion | 独自Dominionなし |
| Scales | Team PretenderのScales | 独自設計不可 |
| Bless | Team PretenderのBless | Disciple Pathは追加しない |
| Ascension Point | Team合計 | Throne Province ownerは国家別 |
| Gold | 自動共有なし | 各Treasury |
| Gem / Blood Slave | 自動共有なし | 各Stock |
| Research | 共有なし | 各Research level |
| Army | 共有なし | 各Unit / Commander |
| Battle | Joint Battleなし | 国家ごとに別Battle |
| Province | 所有者は一国家 | Relinquish可能 |
| Fort / Lab / Temple | Team Dominionへ影響 | Ownerが管理 |
| Hero / Event | 共有なし | 国家別 |
| Global | Dominion effectはTeamへ及ぶ場合あり | Ownership・Gem incomeはCaster側 |
| Dominion kill | Team共通Risk | 寺院・Priest負担は分散 |

## 自動共有されないからこそ計画する

Team memberが、

- 100 Fire Gemを持つ
- Construction 6へ到達する
- Fire 5 Casterを持つ

としても、他の国家が自動的にその能力を使えるわけではありません。

実際に利益へ変えるには、

- ItemをForgeして送る
- Gemを送る
- GlobalをCastする
- Summonを作る
- 対象ProvinceへRitualを使う
- Province ownershipを移す

必要があります。

---

# Researchは国家別

Disciple Gameで最も起こりやすい誤解の一つです。

```text
Team AがConstruction 6
≠
Team BもConstruction 6
```

です。

各国家は、自分のResearch Pointを自分のSchoolへ入れます。

## Team Researchの目的

全員が同じSchoolを同じLevelまで上げるのではなく、

> **Team全体として必要なSpell・Item・Summonを、誰が最短で供給するか**

を決めます。

## Research分担表

| Member | 主School | Breakpoint | Teamへ供給するもの | 自国で必要なもの |
|---|---|---|---|---|
| Pretender nation | Construction | Booster / Item | Resistance Item | Nation troop buff |
| Disciple A | Conjuration | Summon Mage | Magic diversity | Elemental |
| Disciple B | Enchantment | Army buff / Global | Team support | Sacred buff |

## 重複Researchが必要な場合

分担が常に正解ではありません。

次では各国家が同じSchoolを研究する価値があります。

- 自国Mageが自国ArmyへBattle Spellを使う
- Joint Battleがなく、Ally Mageを借りられない
- Frontが離れている
- Item輸送が間に合わない
- 同時Throne rush
- 一国家が脱落しても機能を維持する

特にBattlefield Spellは、Team memberの別Battleへ持ち込めません。

```text
Team memberがFog Warriorsを研究
≠
自国ArmyがFog Warriorsを使える
```

点を忘れないでください。

---

# Magic Path分担

TeamのMagic diversityは、各国家のNative Mage、Rare random、Disciple、Pretender、Summonを合わせて評価します。

## Path担当表

```text
Fire：
Air：
Water：
Earth：
Astral：
Death：
Nature：
Glamour：
Blood：
Holy / Claim：
```

各Pathについて、

- Site Search
- Booster
- Combat Spell
- Ritual
- Global
- Summon Mage
- Resistance Item
- Throne attack

の担当を決めます。

## Discipleで補うPath

Discipleは400 Pointを、TeamにないPathへ集中できます。

有力な役割：

### Rainbow engineer

- Wide Site Search
- Booster Forge
- Crosspath Item
- Summon access

### Specialist Global caster

- 高PathGlobal
- Ritual range
- Dispel
- Late-game spell

### Mobile claimant

- Flying
- Teleport
- Map Move
- Throne Claim
- Anti-assassination

### Combat Disciple

- Early Expansion
- First war
- Thug / SC
- Magic Phase response

### Forge hub

- Construction
- Forge Bonus
- Booster chain
- Resistance装備

## Generated dataを使う

- [Mage Access](../data/mage-access.md)
- [Magic Access Routes](../magic/magic-access-routes.md)
- [Magic Path総論](../magic/paths/index.md)
- [Booster](../items/boosters.md)

を使い、Team全体の到達経路を作ります。

---

# Custom Priest Spell

PriestのBanishment・Smite系統は、宗教のPretender design時Magic Pathにより変化する場合があります。

Disciple Gameでは、Team memberのPriestが崇拝するGodはTeam Pretenderです。

したがって、Disciple自身のMagic Pathを上げても、TeamのCustom Priest Spellを別系統へ変更する目的には使いません。

Team Pretender design時に、

- Undead対策
- Demon対策
- SmiteのDamage type
- Priest量産国家

まで確認します。

---

# Dominion Network

Teamには一つのDominionしかありません。

## 主なSource

- Team Pretender
- 各Disciple
- Team member各国のCapital
- 各Temple
- Claimed Throne
- Dominion spread能力
- Preach
- Blood Sacrifice

DiscipleはProphet相当のMobile spread sourceです。

しかし、通常のProphetのようにH3 Divine Magicを使うわけではありません。

## Team Temple breakpoint

Disciple Gameでは、Effective Dominionを1上げるTemple数がTeam人数に応じて増えます。

計画用には、

```text
Effective Dominion
≈ Base Dominion
＋ floor(Team全Temple数 / (5 × Team人数))
```

として考えます。

例：3人Teamなら、通常15 Templeごとに+1のBreakpointです。

Game内のDominion overviewを最終確認にしてください。

## なぜ人数補正があるか

三人Teamは、

- Capitalが三つ
- Temple建設拠点が三国家
- Disciple sourceが二つ
- Gold economyが三国家

あるため、通常Gameと同じ5 TempleごとではDominionが急速に強くなりすぎます。

## Temple担当を決める

全員が無計画にTempleを建てるのではなく、

```text
現在Team Temple数：
次Breakpoint：
不足Temple数：
誰が建てるか：
完成予定Turn：
守るFront：
```

を共有します。

## Dominion kill

Team Dominionが世界から消えるRiskは、Team全体の問題です。

一国家が、

> 自国CapitalにはWhite Candleがあるから安全

と思っていても、Team全体のSourceが、

- Pretender死亡
- Disciple死亡
- Temple raid
- Capital siege
- Blood Sacrifice
- Heretic

で失われれば危険です。

詳しくは [Dominion・Scales・宗教戦](dominion.md) を参照してください。

---

# 国家固有Dominion効果

この項目は、Team作成前に必ず確認します。

## Pretender国家がTeam全体へ与える効果

一部の、

- Population kill
- Freespawn
- Insanity
- Scrying
- Temperature
- Unrest
- Terrain変化
- Corpse利用

は、Team Pretender国家のDominionとしてDisciple領へ広がります。

これは強力な相乗にも、Team全体を破壊するPenaltyにもなります。

## Disciple国家が失う可能性のある効果

国家固有Dominion効果の中には、Discipleになり、別国家のPretenderを崇拝すると失われるものがあります。

自国攻略ページに、

```text
PretenderとしてのDominion effect
Discipleとして残るeffect
Discipleになると失うeffect
Team memberへ移るeffect
```

を分けて記録する必要があります。

## 例：Popkill系

Popkill PretenderがTeamを率いると、Living Disciple国家の、

- Population
- Gold
- Supply
- Recruitment
- Blood economy

を破壊する可能性があります。

逆にPopkill国家が通常DominionのDiscipleになった場合、自国の通常GameとはFreespawn・Population処理が変わる場合があります。

## 例：情報共有系

Dominion下のScrying等、一部情報効果はDiscipleにも利益を与える場合があります。

情報を得る国家と、その情報を使って攻撃する国家を分けられます。

## 例：移動能力

Dominion内Sailing等は、

- Team全員へ移る
- 元国家だけ使える
- Discipleとして元国家が保持する

が能力ごとに異なります。

一般化しないでください。

---

# Prophet

## DiscipleがいるTeam

通常、Prophetを任命できません。

DiscipleがProphetの宗教的役割を担うためです。

失うもの：

- 無料H3
- Divine Blessing
- Smite
- Throne Claim担当
- Mobile Temple check
- 30 Morale等のProphet特性

得るもの：

- Pretender型Disciple
- Magic Path
- Chassis能力
- Throne Claim
- Dominion scaling

## Pretender一人だけのTeam

Disciple Game設定でも、TeamにDiscipleがいないPretenderはProphetを任命できる場合があります。

UI上の`Become Prophet`を確認してください。

## DiscipleをH3として数えない

DiscipleはThroneをClaimできます。

しかし、

- Divine Blessing
- Smite
- Fanaticism
- Preach
- Call God

のPriest役を自動的に行えるわけではありません。

National H3や召喚Priestの価値は残ります。

---

# Pretender・DiscipleのDominion Bonus

Discipleは、Pretender・Prophetと同様に、Local Candleで能力が変わります。

Friendly Dominionでは、一Candleごとに概念的に、

- +10% HP
- +1 Strength
- +0.5 MR

を得ます。

Hostile Dominionでは同じ方向にPenaltyを受けます。

Friendly Dominionでは常時Blessされ、Hostile Dominionでは通常Blessできません。

## Team memberのCandleは同じ

Disciple Aの領土でも、Disciple Bの領土でも、Team DominionならFriendlyです。

DiscipleはTeam内を移動しながら、

- Mobile combat
- Throne Claim
- Frontline spread
- Site Search
- Ritual

を行えます。

## Enemy Dominion侵攻

Combat Discipleは、Chassisの表示値だけで評価しません。

```text
Friendly Candle 5
→ Enemy Candle 5
```

へ入ると、HP、Strength、MR、Bless状態が大きく変わります。

Preach、Temple、Retreat route、Resistanceを用意します。

---

# Gold・Gem・Itemの分担

## Treasuryは別

Team memberは、それぞれ別のGold Treasuryを持ちます。

一国家がRichでも、別国家のFortやRecruitへ自動的にGoldは使われません。

## Messageで送る

Multiplayer Messageで、

- Gold
- Gem
- Item

を送れます。

Turn処理上、Message送付は非常に早く、Research・Forge・Ritual・Battleより前です。

事前に合意していれば、同Host後半のRitualやRecruitへ使える場合があります。

ただし、

- RecipientのLab
- CasterのGem access
- Order
- Item装備Timing
- 送付量

を確認してください。

## Team resource request

```text
要求国家：
目的：Spell / Item / Fort / Recruit
必要資源：
必要Turn：
送付元：
返済・交換：
失敗した場合：
```

「余っていたらGemをください」ではなく、用途とTimingを書きます。

## Forge分担

Construction担当国家は、

- Booster
- Resistance Item
- Research Item
- Supply Item
- Thug装備

を作り、他Team memberへ送ります。

ただしForge担当がすべてのGemを持つと、

- Battle Gem
- Ritual
- Global
- Emergency resistance

が不足します。

Team Gem budgetを分けます。

---

# Global Enchantment

Disciple Gameでは、CasterのDominionへ作用するGlobal効果がTeam Dominion全体へ及ぶ場合があります。

CasterがPretender国家かDisciple国家かにかかわらず、Team memberが恩恵を受けられることがあります。

一方、Gem生成等の所得はCaster国家だけに入る場合があります。

```text
Dominion-wide effect：Teamへ作用し得る
Gem income・Ownership：Caster国家
```

と分けます。

## Global担当を決める

- 必要Research
- Caster Path
- Booster
- Gem income
- Overcast
- Dispel defence
- Caster protection
- Center Province防衛
- Team全体の利益

を一国家にまとめます。

## GlobalをTeam共有と誤解しない

すべてのGlobalが、全効果を均等配分するわけではありません。

Spell descriptionで、

- Caster nation
- Caster's Dominion
- Friendly units
- World
- Province center
- Gem income

を確認してください。

---

# Income routeとAlly領

Disciple Gameでは、Gold incomeの経路をTeam memberの領土へ通せる場合があります。

これにより、Team領が連続していれば、孤立ProvinceのTax routeを支えられます。

ただし、

- Resources
- Recruitment Points
- Commander Points
- Gem stock

が全国共有になるわけではありません。

```text
Ally領がTax routeになる
≠
Local Resourcesを共有する
```

です。

## Team corridor

Team間の接続Provinceは、

- Tax route
- Reinforcement
- Retreat
- Gem・Item courier
- Throne response
- Dominion network

を支えます。

Incomeが低くても、Team全体では重要なProvinceです。

---

# ProvinceをTeam memberへ渡す

Disciple Gameでは、`Relinquish Province`によりTeam memberへProvinceを譲渡できます。

## 基本条件

通常、

- 譲渡側CommanderがRelinquishを命令
- 受取側の非Stealth CommanderがProvinceに存在

する必要があります。

## Turn Timing

Relinquishは、通常Movementより前のStep 23で処理されます。

そのため、譲渡後のOwnerを基準に、後続Movement・Battle・Incomeへ影響します。

## 維持されるもの

通常、

- Fort
- Laboratory
- Temple

は維持されます。

Province Defenceは約25%減少するため、直後の侵攻に注意します。

## 譲渡する理由

### National recruit

SiteやTerrain recruitmentを最も使える国家へ渡します。

### Magic Site

そのPath、Discount、Recruitを活用できる国家へ渡します。

### Fort network

同じPlayerへFrontline Fortを集め、MovementとRecruit責任を明確にします。

### Throne

Claimant、防衛Army、Temple、Dominion担当を持つ国家へ管理を集めます。

Ascension PointはTeam共有ですが、Local Site利益と防衛責任はOwnerに影響します。

### Underwater / Cave / Plane

環境へ対応できる国家へ入口を渡します。

### Blood economy

High Population ProvinceをBlood担当へ渡す場合があります。

## 譲渡前Checklist

```text
Receiver Commanderは非Stealthか：
Fort / Lab / Temple：
PD減少後の値：
Enemy invasion：
Tax route：
Resource draw：
Site income：
Local recruit：
Throne claim：
Retreat route：
```

---

# ArmyはJoint Battleしない

Disciple Gameでは、Team memberのArmyを同じBattlefieldへ統合できません。

これはTeam戦術を大きく変えます。

## 同じProvinceを攻撃した場合

Team member AとBが同じEnemy Provinceを攻撃すると、通常は別々のBattleになります。

```text
Battle A vs Enemy
        ↓
Battle B vs 残存Enemy
```

のような逐次戦闘になり得ます。

ただし、どちらが先になるかを完全に前提にしないでください。

## 共有できないもの

- Formation
- Squad order
- Battle Script
- Army-wide Buff
- Bodyguard
- Leadership
- Battlefield Enchantment
- Friendly AoE
- Retreat control

Team memberのMageは、自国Battleだけを支援します。

## 逐次戦闘の使い方

### Ping担当

安価Armyで、

- Enemy Script
- Gem use
- Formation
- Summon
- Battlefield Enchantment

を確認します。

### Gem burn

Player Armyは前BattleでGemを使い、後Battleで不足する場合があります。

ただしBattle順とAI判断があるため、完全依存しません。

Independent Throne GuardianのMageはBattleごとにGemを補充するため、この方法では枯れません。

### Morale・損耗

前BattleでUnit・Commanderを削り、後Battleが本命を倒します。

### Retreat route切断

別Team memberが周辺Provinceを取り、主戦闘側がRout損失を増やします。

## Team Battleの代わりに戦線を分ける

強い分担は、

- A：Main Army
- B：Raid・Retreat cut
- C：Siege・Relief block

です。

同じProvinceへArmy三つを重ねるより、戦略目的を分けます。

---

# Team戦術Pattern

## Pattern 1：Main Army＋Raider

```text
Member A：Enemy主力を拘束
Member B：Income・Lab・TempleをRaid
Member C：Retreat routeを切る
```

主戦闘に全員を投入しない構成です。

## Pattern 2：Siege＋Relief interception

```text
Member A：FortをSiege
Member B：Enemy Relief routeを封鎖
Member C：後方Raid・Gem route破壊
```

Fort戦を一国家、外側の戦争を別国家が担当します。

## Pattern 3：Magic Phase＋Normal invasion

```text
Member A：Magic Phase attack
Member B：通常Movementで侵攻
```

Battleは別々ですが、

- PD排除
- Commander sniping
- Gem use
- Retreat誘導

を先行させられる場合があります。

Magic Phase側が単独で敵主力へ当たるRiskがあります。

## Pattern 4：Throne multi-prong

```text
Member A：Throne 1攻略＋Disciple Claimant
Member B：Throne 2攻略＋H3
Member C：既存Throne防衛
```

Team Pointは共有ですが、ClaimantとArmyは各地へ必要です。

## Pattern 5：Forge support

```text
Member A：Construction担当
Member B：Frontline combat
Member C：Summon・Global
```

ItemとGemをTurn単位で交換します。

---

# ThroneとTeam Victory

Ascension PointはTeamで共有します。

## Claim可能者

- Team Pretender
- Disciple
- H3以上のPriest

DiscipleはHoly Pathを持たなくてもClaimできます。

## Claim Timing

ClaimはStep 8で、Movement、Assassination、Battleより前です。

ClaimantはHost開始時点でThroneにいる必要があります。

詳しくは [Throne of Ascension・Claim・勝利条件](thrones.md) を参照してください。

## Claimant分担

Disciple GameではDisciple自体がClaimantです。

そのためTeamは、Pretenderを遠くへ動かせなくても、複数Discipleを別Throneへ配置できます。

## Team Point表

```text
現在Team Point：
勝利必要Point：
不足Point：

Throne A：Level / Owner / Claim状態 / Claimant
Throne B：Level / Owner / Claim状態 / Claimant
Throne C：Level / Owner / Claim状態 / Claimant

既存Point防衛：
同Hostに失うRisk：
Step 57予測Point：
```

## Local benefitのOwner

Throneが与える、

- Local Mage recruitment
- Research bonus
- Forge discount
- Ritual discount
- Gem income
- Province effect

は、Province owner側で運用する要素があります。

Team PointだけでOwnerを決めず、Local benefitを使える国家へ譲渡する判断もあります。

## Claim済みThroneの譲渡

同Team内のClaim状態・Local effect・Owner表示は特殊処理を含む可能性があります。

重要な勝利HostでRelinquishを使う場合は、Test GameまたはGame内表示で確認してください。

---

# Call God・DiscipleのRecall

PretenderまたはDiscipleが死亡した場合、Priestの`Call God`で復帰を支援できます。

## Team PretenderをRecallする

Team Pretenderは、

- Pretender国家のPriest
- 各Disciple国家のPriest

が支援できます。

Team全体のPriest turnを集められるため、通常Gameより早く戻せる場合があります。

## DiscipleをRecallする

死亡したDiscipleは、

- そのDisciple国家のPriest
- Team Pretender国家のPriest

が支援できます。

別のDisciple国家のPriestは、通常そのDiscipleを直接Recallできません。

## Recall権限表

| Priest所属 | Main Pretender | 自国Disciple | 他国Disciple |
|---|---|---|---|
| Pretender nation | 支援可能 | — | Team内Discipleを支援可能 |
| Disciple A | 支援可能 | Aを支援可能 | Bは通常不可 |
| Disciple B | 支援可能 | Bを支援可能 | Aは通常不可 |

## Recall優先順位

### Team Pretender死亡

失う可能性：

- Incarnate Bless
- 強いDominion source
- Global caster
- Booster chain
- Team宗教の中核

通常は最優先です。

### Disciple死亡

失う可能性：

- Magic Path
- Throne Claimant
- Combat role
- Mobile Dominion source
- Site Search

Team Pretender国家のPriestが支援できるため、Team内でPriest turnを調整します。

## Priest turnの交換条件

Call Godへ回すPriestは、同Turnに、

- Preach
- Banish
- Research
- Claim
- Army support

を行えません。

Dominion killが迫っている場合、全PriestをRecallへ回すとTeam Candleが先に消える可能性があります。

---

# Province ownershipと役割分担

Team Mapを、国家色だけでなく役割で見ます。

## Frontline owner

- Fast reinforcement
- Fort defence
- PD
- Patrol
- Local Mage
- Retreat route

を担当します。

## Research hinterland

- Safe Fort
- Mage production
- Lab network
- Research Item
- Low raid risk

を担当します。

## Forge hub

- Construction Mage
- Gem stock
- Dome
- Item courier
- Booster

を置きます。

## Blood zone

- High Population
- Patrol
- Blood Hunter
- Slave transport
- Unrest recovery

を担当します。

## Throne zone

- Claimant
- Fort
- Temple
- Mobile reserve
- Dome
- Scout ring

を用意します。

## Underwater・Cave・Plane担当

環境へ対応する国家が、

- Entrance
- Fort
- Claim
- Supply
- Retreat

を管理します。

---

# Team composition

## 通常兵＋Magic support

- Pretender nation：強Scales・Dominion
- Disciple A：Magic diversity
- Disciple B：Frontline・Siege

安定した構成です。

## Sacred portfolio

複数国家がSacredを主力にします。

### 強み

一つのBless投資を複数国家で回収できます。

### Risk

- Holy Points競合
- Anti-Sacred
- Incarnate停止
- Capital siege
- 同じResistance不足

## Blood Team

- Blood Sacrifice
- Blood economy
- Demon summon
- Horror counter

を分担します。

Gold・Population・Patrolの負担を他国家へ押し付けないようにします。

## Popkill Pretender Team

Team全域へPopulation damageとFreespawnを広げる構成です。

### 向くDisciple

- Undead
- Pop-independent
- Summon中心
- Gold需要が低い
- Supply不要

### 危険なDisciple

- Gold-heavy Mage
- Blood
- High Population recruitment
- Living Supply-heavy Army

## Underwater＋Land Team

海国家が、

- Sea Throne
- Coastal raid
- Water magic

を担当し、Land国家が地上経済を支えます。

問題は、

- DominionのLand / Sea境界
- Claimant移動
- Item transfer
- Water Breathing
- Tax route
- Mutual relief

です。

## Stealth・Raid Team

一国家がEnemy後方を荒らし、別国家がMain Armyを拘束します。

- Temple破壊
- Lab破壊
- Retreat cut
- Throne threat
- Scout network

との相性が良い構成です。

---

# Team role

一人が複数Roleを持つ場合があります。

## Team leader

- Turn planをまとめる
- Throne Pointを管理
- 外交方針を統一
- Resource requestを整理

Pretender Playerである必要はありません。

## Front commander

- Enemy Main Army
- Fort
- Battle Script
- Relief Army

を管理します。

## Research coordinator

- 各School
- Breakpoint
- 重複
- Completion Turn

を一覧化します。

## Magic coordinator

- Path coverage
- Booster
- Summon
- Global
- Site Search

を管理します。

## Quartermaster

- Gold
- Gem
- Item
- Blood Slave
- Supply Item

の送付を管理します。

## Intelligence officer

- Scout
- Spy
- Scrying
- Battle Replay
- Enemy Research
- Throne Guardian

を共有します。

## Throne coordinator

- Current Point
- Claimant
- Attack Turn
- Existing Throne defence
- Step 57 Point

を管理します。

---

# Team communication

Disciple Gameでは、戦力より情報共有の遅れで負けることがあります。

## 毎Turn共有するもの

```text
Enemy Main Army：
Enemy research / spell：
自国Research completion：
Gem request：
Item request：
Fort / Temple completion：
Throne Claim：
Disciple / Pretender状態：
Dominion危険：
Province transfer：
Next Turn attack：
```

## 情報の時間Stamp

Scout情報には、

- 確認Turn
- Source
- 精度
- 推定

を付けます。

```text
Turn 24 Scout：Enemy 80 units
Turn 25 Spy：Mage 6確認
Turn 26予想：Relief 40追加可能
```

と書きます。

## Diplomacy

外部Playerとの、

- NAP
- Border
- Throne分配
- War declaration
- Trade
- Joint target

をTeamで統一します。

一人がNAPを守り、別Team memberが同じ相手へ攻撃する状態を避けます。

---

# Turn Orderで見るTeam連携

| Step | 処理 | Team上の意味 |
|---:|---|---|
| 1 | Message送付 | Gold・Gem・Itemを早期移動 |
| 2 | Research | 各国家で別々に進む |
| 4 | Recruitment | 各国家のQueue |
| 6–7 | Preach・Heretic | 同Turn Battle前のTeam Dominion |
| 8 | Claim Throne | Team Point追加 |
| 10 | Ritual | Team memberが送ったGemを使う計画 |
| 16 | Prophet | Disciple Teamでは通常利用不可 |
| 17 | Call God | Pretender・Disciple Recall |
| 23 | Relinquish Province | Team内Ownership変更 |
| 24 | Friendly movement | Ally territoryへの移動 |
| 25 | Other movement | Enemy侵攻・Break Siege |
| 26–27 | Battle・Storm | Team Armyは別Battle |
| 43 | Dominion spread | Team Temple・Discipleの宗教Network |
| 57 | Victory check | Team Ascension Point判定 |

## MessageとRitual

Message送付はRitualより先です。

事前合意があれば、

```text
Member A：20 Astral Pearl送付
Member B：同HostにGlobal Cast
```

のような計画が可能です。

CasterがLabへいて、Orderが有効で、必要Gemへアクセスできることを確認します。

## RelinquishとMovement

Province譲渡はMovementより先です。

譲渡後、

- Friendly / Enemy判定
- Fort内外
- Tax route
- Retreat

が変わる可能性があります。

Frontlineでの譲渡は、侵攻予測と合わせます。

## ClaimとBattle

ClaimはBattleより先です。

Teamが同Hostで必要Pointへ到達しても、後半に別Throneを失えばStep 57で不足する場合があります。

---

# First War

## 開戦前に決めるもの

- Teamの戦争目的
- 主戦場
- 各MemberのTarget
- Research breakpoint
- Gem budget
- Siege担当
- Raid担当
- Retreat cut担当
- Enemy Throne
- 終戦条件

## 同じTargetへ全員を向けない

Joint Battleがないため、全Memberが一Provinceへ突入すると、逐次撃破される可能性があります。

強い配置：

```text
Member A：Enemy Main Army
Member B：第二Fort
Member C：Lab・Temple・Retreat route
```

です。

## 一人が負けた場合

Team planは、

- Frontline国家敗北
- Disciple死亡
- Gem stock喪失
- Fort陥落
- Throne喪失

へ代替を持つ必要があります。

別Memberが、

- Relief
- Item供給
- Counter-research
- Province transfer
- Recall

を担当します。

---

# Throne rush

## Teamなら複数Claimantを持てる

Pretender一人に加え、各DiscipleがClaim可能です。

三人Teamなら、最低でも三体の固有Claimantを持てます。

これは同時Claimで大きな強みです。

## 勝利Hostの分担

```text
Pretender nation：既存Throne防衛
Disciple A：Throne A Claim
Disciple B：Throne B Claim
Reserve H3：失敗時の再Claim
```

## ClaimantをArmyより先に用意する

Throneを攻略してからClaimantを探すと、一Turn以上遅れます。

各攻撃Armyへ、

- Disciple
- H3
- Pretender

のいずれかを前Turnまでに用意します。

## Team全体を守る

最後のClaimだけでなく、既存のWeak Throneを守ります。

Enemyは、最後のClaim Provinceではなく、別のUnforted Level 1を奪って勝利を止められます。

---

# 実戦例

## 例1：Team PretenderがDormant、Discipleが先にAwake

### 状況

- Team BlessにIncarnate effect
- DiscipleはTurn 7にAwake
- PretenderはまだDormant

### 誤解

DiscipleがAwakeしたのでIncarnate BlessもActiveだと思う。

### 実際

Incarnate BlessはTeam Pretenderの存在を必要とします。

Discipleは、IncarnateなしのStatsでExpansionとFirst warを行います。

---

## 例2：DiscipleがFire 6を取ったがBlessは変わらない

### 状況

- Team PretenderはEarth / Nature Bless
- DiscipleがFire 6

### 結果

DiscipleのFire Pathは、

- Fire Ritual
- Forge
- Global
- Combat

には使えます。

Team BlessへFire Bless Pointを追加しません。

---

## 例3：三人TeamがTemple 5棟でDominion増加を期待

### 状況

- Team人数3
- Base Dominion 5
- Team Temple 5

### 問題

通常Gameの5 Temple breakpointをそのまま使っている。

### 計画

三人Teamでは、計画上15 TempleごとのBreakpointとして管理します。

Game内Dominion値を確認します。

---

## 例4：一人がAlteration 7へ到達

### 状況

- Disciple A：Alteration 7
- Pretender nation：Alteration 3
- Disciple B：Alteration 2

### 誤解

Team全体がMarble Warriors等を使えると思う。

### 実際

Researchは国家別です。

AのMageだけがAのBattleで利用できます。

Teamへ利益を渡すには、Summon、Item、Ritual、Global等へ変換します。

---

## 例5：二国家が同じProvinceを攻撃

### 状況

- Member AとBが同じEnemy Fortへ侵攻

### 誤解

一つのBattlefieldへ合流し、AのMageがBのArmyをBuffすると思う。

### 実際

別Battleとして解決されます。

AとBは、

- どちらがPingか
- どちらが本命か
- Enemy Gem burn
- Retreat route

を決めます。

Battle順は確定前提にしません。

---

## 例6：Construction担当へEarth Gemを送る

### 状況

- Member AがEarth Gem 20を持つ
- Member BがConstruction 6とForge Bonus

### 処理

```text
Step 1：AからBへGem送付
Step 5：BがForge
```

事前にOrderとGem量を合わせれば、同HostのForgeへ使えます。

完成Itemをさらに同じHostにAへ返すことは、MessageがForgeより先なのでできません。

---

## 例7：Unique Mage SiteをTeam memberへ譲渡

### 状況

- Member AがSite Provinceを所有
- Member BだけがそのMageとGemを活用できる

### 手順

1. Bの非Stealth Commanderを配置
2. AがRelinquish Province
3. Step 23でOwner変更
4. PD減少を考慮
5. Bが次Turn以降Recruit・Fort運用

Buildingは通常維持されます。

---

## 例8：Main Pretender死亡

### 損失

- Incarnate Bless停止
- Pretender spread消失
- Global caster不在
- Team morale計画崩壊

### 対応

- 全Disciple国家のPriestがCall God支援
- 一部PriestはPreachへ残す
- First warを短縮
- Sacred Armyの代替Script
- Enemy Dominion pushを止める

---

## 例9：Disciple Bが死亡

### 誤解

Disciple AのPriestがBをRecallできると思う。

### 実際

通常、B国家のPriestとTeam Pretender国家のPriestがBを支援します。

AはMain Pretenderを支援できますが、別Disciple Bを直接支援できない場合があります。

---

## 例10：三つのThroneを攻略したがClaimが一つだけ

### 状況

- Team Armyは三方向で勝利
- ClaimantはDisciple一体だけ

### 結果

同Turnに一つしかClaimできません。

攻略Army数ではなく、Claimant数が勝利Timingを制約します。

---

## 例11：Popkill国家をTeam Pretenderへ選ぶ

### 状況

- Pretender nation：Popkill / Freespawn
- Disciple A：Gold-heavy Mage
- Disciple B：Blood nation

### 結果

Team Dominionが、Disciple領のPopulation、Gold、Supply、Blood基盤を破壊する可能性があります。

強いFreespawnだけを見ず、Team経済全体をTestします。

---

## 例12：GlobalのGem incomeを全員が受け取ると思う

### 状況

- Disciple AがGem生成GlobalをCast

### 誤解

Team member全員のTreasuryへGemが分配される。

### 実際

Dominion-wide効果はTeamへ及ぶ場合がありますが、Gem incomeはCaster国家側へ入る場合があります。

Aが必要に応じてGemを送ります。

---

# 症状から原因を探す

| 症状 | 最初に疑うもの |
|---|---|
| Disciple Pathを上げたのにBlessが増えない | BlessはTeam Pretenderが決定 |
| DiscipleがAwakeしたのにIncarnateがない | Main Pretender未Awake・死亡 |
| Prophetを任命できない | TeamにDiscipleがいる |
| DiscipleがHoly Spellを使えない | DiscipleはH3 Priestではない |
| Team memberのSpellを自国Mageが使えない | Researchは国家別 |
| Ally Armyと合流しない | Joint Battleなし |
| Team Temple 5でDominionが上がらない | Team人数補正 |
| Sacred生産数が少ない | Effective Dominion、Holy Points、Temple |
| AllyがRichなのに自国Recruitできない | Treasuryは別 |
| Global効果はあるがGemが増えない | Gem incomeはCaster国家 |
| Provinceを渡せない | Receiver非Stealth Commander不在 |
| 譲渡直後にPDが低い | RelinquishによるPD減少 |
| AllyのDiscipleをRecallできない | Priest所属制限 |
| Team Dominionが味方領を破壊 | Pretender国家のDominion effect |
| Throneを取ったのにPointがない | 未Claim、Claimant不在 |
| 三Armyで勝ったのに一つしかClaimできない | Claimant数不足 |
| Ally領の先でIncomeが途切れる | Tax route・Fort・Ownership例外 |
| TeamのScalesが一国家に不利 | Nation選択とTemperature等の衝突 |

---

# Team Setup Checklist

```text
Team member：
Pretender nation：
Disciple nation：

Team Bless：
Incarnate：
Base Dominion：
Temple breakpoint：
Scales：
Temperature conflict：
National Dominion effect：
Popkill / Freespawn：
Blood Sacrifice：
Custom Priest Spell：

Pretender role：
Disciple A role：
Disciple B role：

不足Magic Path：
Global担当：
Forge担当：
Throne担当：
Underwater / Cave担当：
```

---

# Research Checklist

```text
Member：
Current RP：
Primary School：
First breakpoint：
Teamへ供給するSpell / Item：
自国Battleで必要なSchool：
重複Research：
不足Gem：
Completion Turn：
```

---

# 毎Turn Team Checklist

```text
Team Temple数：
次Dominion breakpoint：
Team Pretender状態：
Disciple状態：
Incarnate Bless：
Dominion kill Risk：

Current Ascension Point：
Claim予定：
既存Throne Risk：

各Member Research：
今Turn送るGold：
今Turn送るGem：
今Turn送るItem：
Relinquish Province：

Enemy Main Army：
Enemy Throne：
Team attack：
Relief / Raid / Siege担当：
```

---

# Throne Rush Checklist

```text
必要Team Point：
現在Point：
不足Point：

Target Throne A：
攻略Army：
Claimant：
Claim Turn：

Target Throne B：
攻略Army：
Claimant：
Claim Turn：

既存Weak Throne：
Mobile defence：
Enemy counter-rush：
Step 57予測Point：
```

---

# Recall Checklist

```text
死亡者：Pretender / Disciple
Incarnate停止：
失ったMagic role：

Pretender nation Priest：
Own nation Priest：
他Disciple Priest：
Preachへ残すPriest：
Claimへ残すPriest：
予想復帰Timing：
復帰までの代替Plan：
```

---

# よくある誤解

## TeamならResearchを共有する

共有しません。

各国家が自分のResearch levelを持ちます。

## DiscipleのPathがBlessへ加算される

加算されません。

BlessはTeam Pretender designで決まります。

## DiscipleはH3 Prophetである

Prophet的Dominion sourceですが、通常のH3 Priestではありません。

## Team memberのArmyは同じBattleへ参加する

通常、別Battleです。

## TeamのGold・Gemは一つのTreasury

国家別です。

明示的に送ります。

## Awake DiscipleがIncarnateを有効化する

Team Pretenderの存在が必要です。

## 全国家固有Dominion効果が共有される

効果ごとに異なります。

## Team Templeは通常Gameと同じ5棟Breakpoint

Team人数に応じて必要数が増えます。

## Province譲渡はOwnership表示だけ変える

PD、Tax route、Recruit、Fort運用、Site利益が変わります。

## 同時Throne攻略にはArmyだけあればよい

各ThroneへClaimantが必要です。

## Main Pretender死亡はPretender Playerだけの問題

Incarnate Bless、Dominion、Global、Team勝利へ影響します。

---

# 追加検証が必要な項目

- Dom6.35における全Pretender / Disciple Chassis選択条件
- Awakeningの厳密なRandom分布とAnnouncement
- 全国家固有Dominion効果のTeam継承一覧
- Disciple GameにおけるCustom Priest Spellの全例外
- Ally領を通るGold tax routeの全接続例外
- Ally Lab・Gem collection・別Plane経路の細部
- RelinquishとClaim済みThroneの同Host相互作用
- Relinquish後のNational Site・Capital Site・Event ownership
- 複数Team memberが同じProvinceを攻撃したときのBattle順
- AI DiscipleのResource・Province transfer判断
- GlobalごとのTeam効果とCaster-only効果
- Team Dominion消滅と個別国家滅亡の同一Host判定
- Modded Victory condition・Cataclysm・Story Event

不明な項目は、Single Playerの小規模Disciple Gameで、

```text
条件
Order
Host Message
Battle Replay
次Turn状態
```

を記録して検証します。

---

## 関連ページ

- [Pretender God](../pretender/index.md)
- [Bless](../pretender/bless.md)
- [Scales](../pretender/scales.md)
- [Dominion・Scales・宗教戦](dominion.md)
- [Throne of Ascension](thrones.md)
- [Province](province.md)
- [Fort・Siege・Storm](forts.md)
- [ターン処理順](../reference/turn-resolution.md)
- [Magic総論](../magic/index.md)
- [Research](../magic/research.md)
- [Magic Access Routes](../magic/magic-access-routes.md)
- [命令とBattle Script](../basics/orders.md)
- [戦闘ルール](../basics/combat-rules.md)
- [最初の戦争](../getting-started/first-war.md)

## 参照先

- [Dominions 6公式Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
- [Illwiki: Disciples](https://illwiki.com/dom5/disciples)
- [Illwiki: Pretenders](https://illwiki.com/dom5/dom6/pretenders)
- [Illwiki: Dominion](https://illwiki.com/dom5/dominion)
- [Illwiki: Global Enchantments](https://illwiki.com/dom5/dom6/globals)
- [Illwiki: Relinquishing Provinces](https://illwiki.com/dom5/relinquish)
