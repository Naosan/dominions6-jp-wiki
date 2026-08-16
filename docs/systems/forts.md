---
title: Fort・Siege・Storm
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# Fort・Siege・Storm

Fortは単なる「壁」ではありません。

> **生産枠、Resources、Income、Supply、退却先、増援拠点、時間稼ぎ**

を一つのProvinceへ集める国家運営の中核です。

同時に、敵Fortを取るには、

> **外のField Battleに勝つ**
> → **包囲を維持する**
> → **壁を破る**
> → **救援Armyを退ける**
> → **Storm戦に勝つ**

という複数段階を通る必要があります。

このページでは、Fortを建てる判断から、Siege、Break Siege、Relief Army、Storm、占領後の運用までを一つの流れとして整理します。

!!! note "このページの精度範囲"
    本文はDominions 6.35を対象に、現行Manualへの公式導線、ゲーム内Tooltip・Message、固定データ、Turn Order、Community testで確認されている主要挙動を実戦向けに整理しています。Fort type、国家固有のWall defender、特殊Fort、Ritual fort、Spell、別Plane、Stealthには例外があります。厳密な数値は現在のゲーム内Fort画面とUnit・Spell Tooltipも確認してください。

---

## 最初に覚える五つ

### 1. FortはProvinceを自動的に守るZone of Controlではない

Fortがあるだけで、隣接Provinceへの敵Movementが停止するわけではありません。

FortがChoke pointになるのは、

- Map connectionが少ない
- Fortを無視すると退路・補給が危険
- Fort内ArmyがBreak Siegeできる
- 後方からRelief Armyが来る
- Throne・Lab・Temple・重要Siteを押さえている

からです。

> **Fortそのものが道を塞ぐのではなく、Fortを無視する代償が道を塞ぎます。**

### 2. 敵は最初にProvinceの外側を取り、その後Fortを包囲する

Fort Provinceへ敵Armyが侵入すると、まず外にいるArmy、Province Defence、同時に到着した部隊とのField Battleが行われます。

攻撃側が勝っても、Fort内の守備隊まで即座に捕獲するわけではありません。

```text
Province外側を攻撃側が支配
＋
Fort内部を防御側が保持
＝
Siege状態
```

となります。

### 3. 壁を0にしたTurnとStormするTurnは通常別

Fort stormはMain Battleの後、Siege damageより前に処理されます。

したがって、

```text
このHostで壁を0にする
→ 次のTurn提出時にStormを命令
→ 次のHostでStorm戦
```

が基本です。

「今TurnのSiegeで壁が0になるから、同じTurnにStormする」という計画は成立しません。

### 4. Siegeに強いArmyとStormに強いArmyは同じとは限らない

大量の高Strength UnitやSiege Bonus Unitは壁を早く壊します。

しかし、その部隊が、

- 狭い突破口
- Wall defenderの射撃
- AoE
- 高Morale守備兵
- Gate周辺の重装兵
- Battlefield Spell

へ強いとは限りません。

逆に精鋭少数ArmyはStorm戦に強くても、壁を破るまで長時間かかる場合があります。

### 5. Fortの最大価値は「毎Turn何を生産するか」で決まる

Wall Integrityが高くても、毎Turn何も雇っていないFortは経済施設として眠っています。

Fortを評価するときは、

- Mageを毎Turn何人雇えるか
- Commander Pointが足りるか
- 兵士用Resourcesがあるか
- Lab・Templeが必要か
- 前線へ何Turnで届くか
- 敵を何Turn拘束できるか

を見ます。

---

# FortのLife Cycle

```text
建設候補を選ぶ
        ↓
Fort建設・Upgrade
        ↓
Lab / Templeを追加
        ↓
Mage・Commander・国家兵を継続生産
        ↓
敵がProvince外側へ侵攻
        ↓
Field Battle
        ↓
Siege
   ↙            ↘
Relief / Sally   Wallを0へ
   ↓              ↓
Siege解除        Storm
                    ↓
                Fort占領
                    ↓
         Repair・再生産・前線化
```

どの段階で止まっているかを確認すると、問題を切り分けやすくなります。

---

# Fortが生む経済

## National recruitment

多くの国家兵とCommanderはFortを必要とします。

さらにUnitによっては、

- Laboratory
- Temple
- Capital
- Coast
- Terrain
- Holy Point
- Commander Point
- Resource
- Recruitment Point

などの追加条件があります。

Fortを建てただけで、目的のMageやSacredを雇えるとは限りません。

## Commander Point

Commander Pointは、Fortで一TurnにCommanderを何人雇えるかを制限します。

たとえばMage一人が2 Commander Pointを使い、Fort側の利用可能Pointが3なら、

```text
1 Turn：Mage 1人
余り：1 Point
```

となります。

次のUpgradeでPointが増えれば、同じFortからのMage生産が大きく変わる場合があります。

### Commander Pointを見る理由

Fort数が同じでも、

- 低Point Mageを複数雇える国家
- 高Point Mageを一人ずつ雇う国家
- Capital-only CommanderへPointを使う国家
- Priest・Scout・Battle Commanderと競合する国家

では価値が違います。

> **Fort数ではなく、毎TurnのCommander生産量を見る。**

## Recruitment Point

兵士側にもRecruitment Pointがあります。

GoldとResourcesが足りていても、Recruitment Pointが不足すると注文が翌Turnへ持ち越されます。

高Tier FortへのUpgradeは、Wallだけでなく兵士生産速度を上げる場合があります。

## Resources

Fortは、

- 自Provinceの利用可能Resourcesを増やす
- Administrationに応じて隣接する未Fort ProvinceからResourcesを引く
- 重装兵、Cavalry、Giant装備の生産を可能にする

経済施設です。

### Fort同士のResource競合

近接したFortが同じ周辺ProvinceからResourcesを引くと、兵士生産拠点同士で競合します。

このためFortを密集させるなら、役割を分けます。

```text
Fort A：重装兵を生産するResource Fort
Fort B：低ResourceでもMageを作るMage Fort
Fort C：前線補給と退路を作るRelay Fort
```

全Fortで同じ重装兵を雇う必要はありません。

### Land・Underwater・別Plane

LandとUnderwaterのResource接続、Cave entrance、別PlaneをまたぐResource吸収には特殊条件があります。

Map layerとProvince connectionが見た目どおりとは限らないため、重要拠点ではFort完成前後のResources表示を比較してください。

## Administration

AdministrationはFortの経済性能を示す重要値です。

主に、

- 自ProvinceのIncome bonus
- 周辺Resourcesの吸収
- Supply
- Fort type全体の経済品質

へ関係します。

高Administration Fortは後方経済拠点として強力ですが、前線で必要なのがWallと退路だけなら、必ずしも最大Upgradeが最適とは限りません。

## Income network

Incomeは、友軍Fortへつながる支配経路によって回収されます。

敵Raidによって道が切られると、Fort自体が無傷でも後方Incomeを失うことがあります。

したがってFort networkは、

> 城の点の集合

ではなく、

> **Income、Retreat、Reinforcementをつなぐ線**

として見ます。

## SupplyとSupply Storage

Fortは周囲へSupplyを供給し、包囲時には守備隊用のSupply Storageを持ちます。

Siegeが長引くほどFort内部のSupply条件は悪化します。

- 大量の通常兵
- Giant
- Mounted Unit
- Gluttony
- Disease
- Low Supply Terrain
- 冬・Heat / Cold
- 包囲Turn数

を考慮します。

Need Not Eat、Undead、Inanimate等を多く持つ国家は、長期Siegeへの耐性が大きく異なります。

## Province Defence

Forted ProvinceのProvince Defenceは、元のIndependent poptypeではなく国家固有のFort PDになる場合があります。

Fortを建てることでPDが必ず強くなるとは限りません。

国家画面と実戦Replayで、

- Commander
- 前衛
- 射撃
- 20以上で増えるUnit
- Fort専用守備兵

を確認します。

---

# Fort画面で読む値

| 項目 | 意味 | 攻略上の問い |
|---|---|---|
| Cost | 建設・Upgrade Gold | 現在Armyと第二Fortのどちらを遅らせるか |
| Build time | 完成までのTurn | 敵到達前に完成するか |
| Administration | Income・Resources・Supply | 経済Fortとして回収できるか |
| Commander Point | Commander生産量 | Mageを毎Turn何人雇えるか |
| Recruitment Point | 兵士生産量 | Gold・Resourcesを使い切れるか |
| Wall Integrity | 壁の最大耐久 | 敵Siege Armyを何Turn止めるか |
| Supply Storage | 包囲中の食料 | 守備隊が何Turn耐えるか |
| Base Defenders | Siege defence・Storm守備兵 | Wall維持とStorm射撃に何が出るか |
| Special rule | Ice、Underwater、City等 | Temperature・Terrain・国家例外は何か |

Fort名だけでなく、この値を見て役割を決めます。

---

# Fort typeとUpgrade

国家、Age、Terrain、特殊能力によって建てられるFort系統は異なります。

主な系統には、

- 標準Fort
- Primitive / Advanced
- Fortified City
- Giant Fort
- Wooden Fort
- Ice Fort
- Underwater Fort
- 国家固有Fort
- Site Fort
- Ritual Fort

があります。

## Upgradeの主な目的

Fort Upgradeで得たいものは次です。

1. Commander Point breakpoint
2. Recruitment Point
3. Administration
4. Supply Storage
5. Wall Integrity
6. Base Defenders
7. 国家固有の特殊効果

### Commander Point breakpointを優先する例

```text
Upgrade前：Mageを1人 / Turn
Upgrade後：Mageを2人 / Turn
```

になるなら、Wall上昇よりMage生産量の増加が本体です。

### Wallだけが増える場合

後方の安全なMage Fortなら、WallのためだけにGoldとBuilder turnを追加する価値は低い場合があります。

前線Choke、Capital、Throneなら、高いWallが救援までのTurnを買います。

## Mason

Mason能力を持つCommanderは、通常より上位のFortへUpgradeできる場合があります。

価値は単なる壁強化ではありません。

- Commander Point増加
- Recruitment Point増加
- Administration増加
- Supply Storage増加
- Base Defender増加

によって、国家全体の生産上限を上げます。

Mason Commanderは、

- 前線で死亡させない
- どのFortをUpgradeするか事前に決める
- Upgrade中の機会費用を計算する
- Siege / Castle Defence能力との兼任を考える

必要があります。

## 特殊Fort

Ice Fort、Underwater Fort、国家固有Fortは、Temperature、Terrain、Age、国家能力で性能が変化します。

名称だけから通常Fortと同じと判断せず、現在のFort Tooltipを確認します。

---

# Fortを建てる場所

## 1. Mage Fort

目的：

- Research
- Battle Mage
- Site Search
- Forge
- Ritual
- Priest
- Scout / Commander

必要条件：

- 継続雇用できるIncome
- 必要ならLab
- MageのCommander Point
- 前線への移動経路
- Rare Mageを守れる後方性

Resourceが低くても、Mageを毎Turn雇えるなら価値があります。

## 2. Resource Fort

目的：

- Heavy Infantry
- Cavalry
- Giant
- Resource-heavy Sacred
- Siege Unit

候補：

- Mountain
- Highland
- Cave
- Mine Site
- High Productivity
- 周辺に未FortのHigh Resource Provinceが多い場所

近接FortとのResource競合も見ます。

## 3. Border Fort

目的：

- Enemy侵攻をSiegeへ変える
- Gem・Item補給
- Battle Mageの集合
- Retreat route
- Relief Armyの基点
- Temple / Dominion
- Enemy Armyを拘束

Risk：

- 完成前に奪われる
- 敵が取ると前線拠点になる
- 迂回可能なら拘束力が低い
- Lab・Booster・Rare Mageを失う

## 4. Choke Fort

Connectionが少なく、迂回に大きな代償がある場所です。

ただしFort自体にZone of Controlはありません。

良いChoke Fortは、

- 後方Income networkを守る
- 敵のRetreat routeを制限する
- 複数の自軍Fortから救援できる
- 敵が無視すると後方を攻撃される

位置にあります。

## 5. Throne Fort

Throneは勝利条件とGlobal effectを持ちます。

必要なのはWallだけではありません。

- ClaimできるPriest
- Temple
- Lab
- Dominion
- Relief route
- Anti-teleport
- Remote attack対策
- Storm defence
- 第二Army

をセットで準備します。

## 6. Site Fort

次を守るFortです。

- Mage recruitment Site
- Gem income
- Ritual discount
- Forge discount
- Summon
- Plane entrance
- Unique Commander
- Special recruit

Site自体の価値が高いほど、敵がFortを取った場合の損失も大きくなります。

## 7. Blood / Ritual Fort

後方で、

- Blood Hunter
- Patrol
- Slave storage
- Summon
- Forge
- Ritual
- Research

をまとめます。

Blood HuntingのUnrestとIncome低下を、Mage Fort経済と混同しないよう役割を分けます。

## 8. Relay Fort

大規模生産より、

- Retreat
- Lab network
- Gem補給
- Item交換
- Scout
- Reinforcement
- 海・洞窟・別Planeへの入口

を作るFortです。

安価なFortでも戦略上の価値があります。

---

# 建設候補を比較する

| 評価軸 | 質問 |
|---|---|
| Income | Fort・Lab・Mageを継続維持できるか |
| Resources | 何を生産するFortか |
| Connections | 何方向を守り、何方向から救援できるか |
| Distance | Capital・前線・Throneまで何Turnか |
| Enemy access | 完成前に敵が到達できるか |
| Site | 守るべき特殊Siteがあるか |
| Terrain | Fort type、Supply、移動へ影響するか |
| Retreat | 敗北時に友軍Provinceへ逃げられるか |
| Dominion | Temple・Preach・Sacredへ意味があるか |
| Capture risk | 敵が取ったとき、どれだけ強い前線拠点になるか |

---

# Fort建設の費用

Fortの費用は表示Goldだけではありません。

```text
総投資
=
Fort Gold
＋ Lab
＋ Temple
＋ Upgrade
＋ Builderの行動Turn
＋ 建設中に雇えなかったArmy
＋ 完成後のMage維持費
```

一方、Returnは、

```text
毎TurnのMage・Commander
＋ 兵士生産
＋ Resources
＋ Income
＋ Supply
＋ Retreat
＋ 敵を止めるTurn
```

です。

## Break-evenを考える

たとえばFort完成後にMageを毎Turn1人追加できるなら、

```text
完成Turn
→ Mage 1
→ Mage 2
→ Mage 3
→ ...
```

とResearchとBattle Mageが累積します。

Fortが早いほど長く生産できますが、早すぎてExpansion Armyが不足すると、Fort候補自体を守れません。

## 第二Fortを急ぐ条件

- National troopだけでExpansionが安定
- CapitalのCommander Pointが詰まっている
- Cheap Mageを各Fortで量産できる
- Capital Resourcesが不足
- Borderが遠く、防衛線を作れる
- Research raceが重要
- High Income / Resource候補がある

## 第二Fortを遅らせる条件

- 即時Rushが見えている
- Expansion Armyが一つしかない
- Awake Expanderが停滞
- 主力がCapital-only
- Fort完成前に敵が到達
- Lab・MageまでGoldが続かない
- 現在Armyの増員で重要Provinceを取れる

> **Fortを建てるかではなく、今TurnのArmyをFortへ変換しても国土が崩れないかを考えます。**

---

# Fort建設・Upgradeの処理

## Goldは先に支払う

建設開始時にGoldを支払います。

建設中にProvinceを失っても、通常は返金されません。

## Commanderが建設を監督する

建設にはCommanderの行動が必要です。

- 同じCommanderが続ける
- 別Commanderへ引き継ぐ
- 一時停止して後で再開

が可能な場合があります。

BuilderがResearch、Preach、Move、Siegeへ回れば、その分だけ完成が遅れます。

## 通常建設はMovement・Battleより後

Fort建設完了は通常のMovementとBattleより後に処理されます。

したがって、

```text
今Turn完成予定
＋
同じTurnに敵が侵攻
```

なら、先にBattleが起こります。

Provinceを守れなければ、完成予定だったFortは防壁になりません。

## Ritual Fortは別

一部のRitualはMagic PhaseにFortを作ります。

Ritual Fortは通常Movementより先に成立するため、

- Throne rush
- 孤立した重要Province
- 敵侵攻直前
- Underwater bridgehead
- 別Plane入口

を同TurnからFort化できる場合があります。

ただし、

- Range
- Terrain
- 既存Fort
- Gem / Slave
- Caster生存
- Ritual順
- Spell固有条件

を確認します。

## Upgrade中のFort

既存FortのUpgrade中にSiegeされると、Goldは返らず、完成Timingへ影響します。

Fortを失えば投資も失うため、前線Upgradeは敵到達Turnと比較します。

---

# Fort Provinceへ侵攻したとき

## Step 1：外側のField Battle

攻撃側はまず、

- Province Defence
- Fort外のArmy
- 同Turnに到着したFriendly reinforcement
- Break Siege部隊
- 第三国Army

などとField Battleを行います。

## Step 2：外側の支配

攻撃側が勝つとProvince外側を支配します。

Fort内のCommander・Unit・Lab・Temple等は直ちに攻撃側のものにはなりません。

## Step 3：Siege開始

攻撃側ArmyがFortの外に残り、壁を破る処理へ入ります。

防御側は、

- Fort内で待つ
- Break Siege
- Stealthで出入りする
- 外部Reliefを呼ぶ
- Ritual・Remote attack
- Wall・Supplyを強化
- Storm defenceを準備

します。

---

# Siege中に何が変わるか

## Recruitment停止

包囲されたFortでは通常Recruitmentが停止します。

注文済みUnitがいたとしても、継続生産を前提に防衛計画を作らないでください。

Fort一つを包囲されることは、

> Wallを削られること

だけでなく、

> **毎TurnのMage・Commander生産を止められること**

です。

## Movement制限

通常UnitはFortへ自由に出入りできません。

防御側が外へ戦うには、Break Siege / Sally等の命令が必要です。

Stealth Unitには例外がありますが、

- SneakでFortへ入ったTurn
- Storm defenceへ参加するTiming
- Siege側のPatrol
- Scale Walls
- Assassin
- Magic Phase movement

は別々に確認します。

特に、Stealthで同TurnにFortへ入れば必ずそのTurnのStormへ参加できる、とは限りません。

## Income

包囲中のProvince Incomeは、外側を支配するSiegerとFortを保持する側へ分かれます。

そのためSiegeは防御側経済を完全に0へするとは限りませんが、通常運用より大きく低下します。

## Gem income

Fort内にLabがあり、Magic SiteがGemを生む場合、Site incomeはFort保持側へ入る扱いがあります。

ただしLab破壊、特殊Site、占領Timing等の例外はMessageとTreasuryを確認してください。

## Supply

Fort内部のSupplyは包囲期間とStorageに左右されます。

長期Siegeでは、

- Starvation
- Disease
- Morale
- HP
- Encumbrance
- Storm戦前の消耗

が問題になります。

大量Armyを壁の内側へ詰め込むことが、常に良い防御ではありません。

## Province外側はSiegerの拠点

Siegerは外側を友軍Provinceに近い状態として扱います。

- Reinforcement
- Preach
- Supply
- Retreat
- 周辺Raid
- Lab / Templeへの圧力

を行えます。

ただしPriestがPreach等の別行動を行う場合、そのUnitはSiege作業へ参加しません。

---

# Wall Integrity

Wall IntegrityはFortの壁耐久です。

Siege Turnごとに、

```text
攻撃側の総Siege Strength
－
防御側の総Siege Defence
```

に応じて増減します。

攻撃側が上回れば壁が減り、防御側が上回れば壁は最大値まで修復されます。

## Wallを削る速度が重要な理由

壁を1Turnで壊すArmyと5TurnかかるArmyでは、同じField Battle勝利でも結果が異なります。

時間が増えるほど防御側は、

- Relief Armyを集める
- Ritualを使う
- Gemを運ぶ
- 外交支援を得る
- 別戦線を攻める
- Siege ArmyをFatigue・Disease・Supplyで弱らせる

機会を得ます。

---

# Siege Strength

Communityで使われる実用モデルでは、Unitの基礎Siege contributionはStrengthの二乗に近い形で増えます。

概念的には、

```text
基礎Siege Strength ≒ Strength² / 100
Flyingなら基礎部分が増える
＋ Siege Bonus
```

です。

そのためStrengthは線形ではありません。

| Strength | 概念的な基礎寄与 |
|---:|---:|
| 10 | 約1 |
| 15 | 約2.25 |
| 20 | 約4 |
| 25 | 約6.25 |
| 30 | 約9 |

### 攻略上の意味

- Giantは少数でも壁へ強い
- Strength buffがSiegeへ影響する場合がある
- Flyingは壁越え能力だけでなくSiegeにも強い
- Siege Bonusは低Strength Unitにも明確な役割を与える
- 大量の低価値Unitも合計では有効
- 戦闘に弱いSummonでもSiege chaffとして価値がある

!!! warning "数式の扱い"
    上表は編成判断用の概念値です。丸め、Flying、特殊Trait、Unit状態、Spell、Version差があります。最終的な進行はHost MessageとFortのWall表示で確認してください。

## Siege Bonus Unit

Sapper、Engineer、Siege Golem等のSiege Bonus Unitは、通常戦闘力以上の壁破壊能力を持ちます。

これらを使うと、

- Siege Armyを小さくする
- Supplyを節約する
- Relief到着前に壁を0にする
- Main Armyを別方向へ動かす

ことができます。

ただしSiege Bonus UnitがStorm戦でも最良とは限りません。

---

# Siege Defence

Siege DefenceはFort内部のUnit、Commander、Fort固有守備兵から生まれます。

主な要素：

- Strength
- Castle Defence Bonus
- Flying
- Mindless
- Animal
- Undisciplined
- FortのBase Defenders
- 国家固有の守備兵
- Spell・Site・Fort効果

一般に、通常UnitのSiege Defence寄与はSiege Strengthより小さく、Castle Defence能力が重要です。

## Intrinsic defender

Fortは国家とTierに応じた自動守備兵を持つ場合があります。

彼らは、

- Wall維持
- Storm戦のWall defender
- 射撃
- Gate周辺の防御

へ寄与します。

高Tier Fortでは数が増える場合があります。

## Castle Defence Unit

Castle Defence Bonusを持つUnitやCommanderは、Fort内部へ置く価値があります。

ただし、

- Field Armyから外す損失
- Upkeep
- Supply
- Capital-only
- Commander Point
- Storm戦での実戦能力

も比較します。

## 隠れているUnit

Stealth状態のUnitがSiege Defenceへ寄与する場合でも、CommanderやStorm参加Timingには別条件があります。

「隠れているから何もしていない」とも、「必ずStormで守る」とも決めつけず、MessageとReplayを確認します。

---

# Siege Messageの読み方

Siegerには壁の損傷状況を示すMessageが届きます。

主な表現は、

- Lightly damaged
- Moderately damaged
- Severely damaged
- Critically damaged
- Work is going very slowly

です。

Messageから、

```text
現在のWall残量
÷
前Turnの減少量
```

を概算し、Storm可能Turnを予測します。

## 予測する項目

- この速度なら何Turnで0か
- Enemy Reliefは何Turnで来るか
- Supplyは持つか
- Siege Bonusを追加するか
- Main Armyを残すか
- GemをStorm用に温存するか
- 別FortへArmyを分けるか

---

# Break Siege、Sally、Relief Army

## Break Siege / Sally

Fort内部のArmyが外のSiegerへ攻撃する行動です。

目的：

- Siege解除
- Siege Unitの破壊
- Gem burn
- Relief Armyとの合流
- Enemy Commander kill
- 壁が0になる前の決戦

## Relief Army

外部からSieged Provinceへ来る友軍Armyです。

同TurnにFort内部がBreak Siegeし、外部Armyも到着すると、同じField Battleへ参加できます。

```text
Fort内Army ─ Break Siege ┐
                         ├→ Field Battle vs Sieger
外部Army ─ Relief ───────┘
```

これはFort防衛の最重要連携です。

## Friendly Movementの価値

Turn処理では友軍Province間のMovementが敵地侵攻より先に処理されます。

複数の後方Fortから中央Fortへ救援を集める配置は、Border Armyを一か所に固定するより柔軟です。

詳しくは[ターン処理順](../reference/turn-resolution.md)を参照してください。

## Magic Phaseの制約

Besieged側のMagic Phase movementはFort内部へ入る扱いになり、SiegerへMagic Phase attackできない場合があります。

つまり、

> Teleport Mageを同じProvinceへ送れば、包囲Armyを先に焼ける

とは限りません。

第三国のRemote attackやSpell固有効果は別です。

## Stealth reinforcement

Stealth Unitは包囲線を越えて出入りできる場合があります。

しかし、

- Sneakの処理
- Fort内部へ入る処理
- Break Siege
- Storm参加
- Patrol detection

は同じではありません。

救援Turnの直前にStealth Armyを入れる場合は、小規模TestでTimingを確認します。

## Sallyで負けたとき

Fort側Commanderの退却先は、同TurnにFortが保持されるか、後続Stormが成功するかで変化し得ます。

「負けても必ずFortへ戻れる」と仮定せず、

- 隣接友軍Province
- 後続Storm
- Commander生存
- Retreat route

を確認します。

---

# Relief作戦の設計

## 1. 勝利条件

悪い目標：

> Siegeを破る

良い目標：

> 外部Armyで敵Damage Mageを拘束し、Fort内ArmyがSiege Bonus Unitを倒して壁破壊能力を失わせる

必ずしもSieger全滅が必要とは限りません。

## 2. Timing

- 壁が何Turn持つか
- Relief ArmyのMap Move
- Builder・Mageの到着
- Enemy reinforcement
- Storm命令可能Turn
- Gem輸送
- Season・Terrain

を合わせます。

## 3. Fort内と外部Armyの役割

| 部隊 | 役割例 |
|---|---|
| Fort内 | 正面Screen、Gate守備兵、Priest、短距離Caster |
| 外部Relief | Flank、射撃、Battlefield Spell、退路遮断 |
| Stealth | Commander狙い、Siege Bonus狙い、後方Raid |
| Magic | Resistance、Remote pressure、別Provinceへの陽動 |

## 4. 失敗時の残存戦力

Reliefに全軍を投入して負けると、Fortも後方も同時に失います。

- 第二Army
- 隣接Fort
- Retreat route
- Gem reserve
- Commander reserve

を残します。

---

# Storm命令

## Stormできる条件

通常は、Turn提出時点でWall Integrityが0である必要があります。

Siege Messageだけでなく、FortのWall表示を確認します。

## 同TurnのSiege damageは間に合わない

Turn Orderは概念的に、

```text
Field Battle
→ Fort Storm
→ Retreat
→ Siege damage
```

です。

したがって、そのHostのSiege damageで壁が0になっても、Storm処理はすでに終わっています。

## Wallを後から増やした場合

Storm命令がすでに有効になった後、Iron Walls等で現在Wallが増えても、その同TurnのStormを止められない場合があります。

WallはStorm命令を出せるかを制限するもので、発行済み命令を必ず取り消すものではありません。

## 外側のField Battleが先

Storm予定TurnにRelief Armyが来た場合、

1. 外側のField Battle
2. Storm戦

の順です。

SiegerがField Battleで敗北すれば、予定したStormは成立しません。

---

# Storm戦はField Battleと違う

## BreachとChoke

攻撃側は壁の突破口やGate周辺へ集中します。

このため、

- 前線幅が狭い
- 後列が詰まる
- 大型Unitが通りにくい
- AoEが密集へ刺さる
- Long weapon・Repelが機能しやすい
- Screenの損失が進軍全体を止める

場合があります。

## Wall defender

Fort固有の射撃Unitが壁上へ出現する場合があります。

彼らは、

- 高所・壁の防御
- Unlimited ammo
- Gateへ集中する攻撃側
- 射線
- Fort Tierによる人数

を利用します。

Storm戦で表示されたUnitが通常Recruitできるとは限りません。

## Wallを無視する能力

次の能力はStorm geometryを変えます。

- Flying
- Ethereal
- Scale Walls
- Teleport / Blink系
- Wall crossing固有能力
- Spell固有移動

ただしStorm、Wind、Obstacle、Target order、Fort固有効果によって挙動は変わります。

## Fort enchantment

一部のRitualはFortへ、

- Wall強化
- Gate周辺Damage
- 火・冷気・特殊効果
- 防御側Bonus

を付与します。

攻撃前にFort icon、Battlefield effect、Spell dataを確認します。

## Retreat

Besieged CommanderがStorm戦でRetreatすると死亡します。

守備側には通常Field Battleのような安全な後退先がありません。

このため、

- Morale
- Leadership
- Fear対策
- Commander分散
- Bodyguard
- Battlefield Enchantment caster保護

が極めて重要です。

---

# Stormする側の編成

## 1. Siege chaffとStorm forceを分ける

壁を壊すだけの低価値Unitを、狭い突破口へ全投入すると詰まります。

```text
Siege chaff：壁を壊す
Storm screen：最初にGateを受ける
Storm damage：守備前衛を倒す
Mage：AoE・Control・Resistance
Flanker：Wall defender・後衛へ圧力
```

へ役割分担します。

## 2. 高Morale

Chokeで一部Squadが大損害を受けるとRoutが連鎖します。

- High Morale
- Inspirational Leadership
- Sermon / Priest
- Fear対策
- Squad分割

を準備します。

## 3. Fatigue管理

狭い突破口で戦闘が長引くと、重装兵とThugが疲れます。

- Reinvigoration
- Relief
- Summon screen
- 交代可能な複数Squad
- AoEで短期決着

を使います。

## 4. AoEとControl

Gate周辺へ密集する守備兵には、

- AoE Damage
- Cloud
- Earth Meld
- Entangle
- Fear
- Fatigue
- Armor destruction
- Battlefield Enchantment

が有効です。

Friendly Fireにも注意します。

## 5. Resistance

Fort enchantmentと守備MageのDamage typeを偵察します。

- Fire
- Cold
- Shock
- Poison
- Acid
- MR attack
- Fatigue

への防御を接敵前に入れます。

## 6. Caster保護

攻撃側CasterもWall defenderの射撃、AoE、Flying守備兵を受けます。

- 後方配置
- Shield screen
- Arrow protection
- Bodyguard
- 複数Caster
- Script後Main Order

を設計します。

---

# Stormを守る側の編成

## 1. Gate blocker

突破口へ、

- 高Protection
- 高Defence
- High Morale
- Regeneration
- Long weapon
- Formation Fighter
- Sizeに適したUnit

を置きます。

一体の強いUnitより、交代できる複数層が安定します。

## 2. Pike・Repel

長Weaponは狭い突破口で敵の攻撃機会を減らします。

ただし、

- High Morale
- Mindless
- 射撃
- Spell
- 長Weapon
- 多段攻撃

には弱点があります。

## 3. 射撃

Wall defenderと通常Archer・Crossbowを組み合わせます。

攻撃側は密集しやすいため命中しやすい一方、自軍前衛へFriendly Fireする可能性もあります。

## 4. AoEとCloud

Gateへ集まる攻撃側へ、

- Fire
- Poison
- Cold
- Shock
- Acid
- Fatigue
- Summon

を重ねます。

守備側Resistanceを先に用意します。

## 5. Commander redundancy

一人のCommander死亡で全Squadが崩れないよう、

- 複数Commander
- Leadership分散
- Bodyguard
- Mage box
- Priest
- 予備Caster

を置きます。

## 6. Supply

Storm当日だけ強くても、包囲中にStarvationとDiseaseで弱っていれば機能しません。

守備隊規模はSupply Storageと救援予定Turnから逆算します。

---

# Fort defenceは壁だけではない

Fortを守る層は次です。

```text
Scout
→ Border Province
→ Mobile Army
→ Province Defence
→ Field Battle
→ Wall
→ Relief Army
→ Storm defence
→ Counterattack
```

## Scout

敵Siege Armyの、

- Siege Bonus
- Map Move
- Mage
- Gem
- Storm force
- Relief screen

を早期に把握します。

## Border Province

周辺Provinceを守ると、

- Supply
- Retreat
- Reinforcement
- Income
- Siege route

を維持できます。

## Mobile Army

Fort内部へ全軍を閉じ込めると、Siegerの外側を攻撃できません。

近隣FortにMobile reserveを残し、Relief・Raid・退路遮断を行います。

## Counterattack

SiegerがStorm用GemとSiege Unitを失った後に追撃します。

Fortを守っただけで満足せず、敵のRetreat routeと補給線を攻めます。

---

# Fortを包囲する側の戦略

## Fortだけを見ない

周辺Provinceを取ることで、

- Income
- Resources
- Supply
- Retreat
- Reinforcement
- Dominion
- Scout route

を削れます。

敵FortをすぐStormできなくても、外側の国家機能を破壊できます。

## Main Armyを拘束しすぎない

Fort一つへ全主力を置くと、別戦線を失います。

選択肢：

- Siege Bonus Unitを残す
- Siege chaffを残す
- Storm forceだけ残す
- Main Armyを次Provinceへ動かす
- Relief迎撃Armyを別位置へ置く

## Relief routeを読む

敵がどのFort・Provinceから来るかを確認します。

```text
Fort A ─ 1 Turn
Fort B ─ 2 Turn
Capital ─ 3 Turn
```

なら、壁破壊予測と合わせて待ち伏せを作ります。

## Supply attack

Siege Army自身もSupplyを消費します。

- Enemy Dominion
- Wasteland
- Winter
- Large Army
- Gluttony
- Disease
- Remote effect

で長期包囲が危険になります。

---

# Ritual FortとThrone rush

Ritual FortはMagic Phaseに成立するため、通常建設とは戦略価値が異なります。

## 主な用途

- Claim直前のThroneをFort化
- Enemy normal movementを一回の占領で済ませない
- Underwater foothold
- 別Plane入口
- Remote Siteの防衛
- Capital Fortの特殊Upgrade / replacement
- Late gameの即席Retreat network

## 注意

Ritual Fortがあっても、

- Magic Phase attack
- Assassination
- Remote ritual
- Dominion kill
- Claim Priest死亡
- Storm force
- Third-party attack

は防げません。

Fortは勝利条件の一層であって、単独の安全装置ではありません。

---

# Fortを失った後・奪った後

## 失った側

確認するもの：

- Capital-onlyでないMage供給
- Income network
- Retreat route
- Gem Site
- Lab Inventory
- Booster
- Temple / Dominion
- Builder
- Rare Commander
- 次の防衛線

Fort喪失そのものより、国家機能が一か所へ集中していたことが致命傷になる場合があります。

## 奪った側

すぐに確認します。

- Wall状態
- Lab・Temple
- Supply
- Unrest
- Dominion
- Recruit可能Unit
- Enemy Relief
- Retreat route
- Builder / Repair
- Siege ArmyのFatigueとGem

Stormに成功したArmyが、次TurnのReliefに耐えられるとは限りません。

## Fortを前線化する

占領後は、

1. Scout
2. Lab / Temple整備
3. Retreat route確保
4. WallとSupply確認
5. Mobile reserve配置
6. Mage・Commander生産
7. 次のSiege route

を作ります。

---

# 実戦例

## 例1：第二Fortを早く建てたがArmyが消えた

### 状況

Expansionが安定する前にFortへGoldを使い、第一Armyを補充できなかった。

### 原因

将来のMage生産を優先しすぎて、現在のProvince獲得能力を失いました。

### 修正

- 第二Expansion Armyを先に完成
- Fort候補を守れる位置まで拡張
- Fort＋Lab＋最初のMageまでGoldを確保
- BuilderとArmyを別Commanderにする

---

## 例2：Field Battleに勝ったがFortを取れない

### 状況

精鋭Armyで外側を制圧したが、壁がほとんど減らない。

### 原因

Storm combat力はあるがSiege Strengthが不足しています。

### 修正

- Siege Bonus Unit
- 高Strength Summon
- 大量の安価Unit
- Flying
- Strength強化
- 別ArmyをSiege要員として残す

---

## 例3：壁を0にしたのにStormできなかった

### 状況

Host結果でWall 0になったが、そのTurnにStorm戦が発生しなかった。

### 原因

Storm Phaseは同HostのSiege damageより前です。

### 修正

次のTurn提出で`Storm Castle`を命令します。

---

## 例4：Relief Armyが各個撃破された

### 状況

Fort内Armyと外部Armyを同じTurnに動かしたが、別々に戦った。

### 原因候補

- Break Siege命令でない
- Relief ArmyがProvinceへ到達できない
- Magic Phaseとnormal movementを混同
- Map Move不足
- Stealth entryのTiming
- Third-party Battle

### 修正

Turn Order、Movement path、命令名、到着Phaseを分けて確認します。

---

## 例5：Siege chaffでStormして詰まった

### 状況

壁を早く壊した大量の低価値UnitがGateで詰まり、守備AoEで消えた。

### 原因

Siege要員とStorm要員を分けていません。

### 修正

- Storm screenだけ前へ
- Damage Squadを後方
- Siege chaffは一部を外す
- AoE Casterを追加
- Sparse / Squad分割
- Flying flank

---

## 例6：大軍をFort内へ入れたら病気になった

### 状況

Storm防衛用に大量兵を詰め込み、長期SiegeでStarvationとDiseaseが発生した。

### 原因

Wall Integrityだけを見てSupply StorageとSiege期間を見ていません。

### 修正

- Need Not Eat部隊へ置換
- 外部Mobile reserveへ分割
- 早期Break Siege
- Supply強化
- 救援Turnを前倒し

---

## 例7：Stealth救援がStormに参加しなかった

### 状況

Stealth Unitを同TurnにFortへSneakさせたが、Storm守備に現れなかった。

### 原因

Sneak、Fort entry、Storm participationは同一処理ではありません。

### 修正

一Turn早く入れる、Break Siegeへ使う、Scale Walls等の条件を確認します。

---

## 例8：Ritual FortでThroneを守ったがClaim Priestを失った

### 状況

Movement前にFortは完成したが、Assassination・Magic Phase attackでPriestが死亡した。

### 原因

Fortはnormal invasionをSiegeへ変えましたが、全ての早期Phase攻撃を止めるわけではありません。

### 修正

- Priest複数
- Bodyguard
- Stealth
- Dome
- Anti-assassin
- Claim Timing
- Dominion

を組み合わせます。

---

# 症状から原因を探す

| 症状 | 主な原因 | 最初に試すこと |
|---|---|---|
| Fortが多いのにResearchが伸びない | Mage未雇用、CP不足、Lab不足 | 毎TurnのMage queueを確認 |
| 重装兵を注文できない | Resources競合、RP不足 | Fort配置とUpgradeを確認 |
| 建設完成TurnにProvinceを失う | BuildingはBattle後 | 一Turn早く守備を置く |
| 壁が減らない | Siege Strength不足、Defence高い | Siege Bonus・高STRを追加 |
| 壁が修復される | Defender優勢 | Castle Defenceを倒す／増援 |
| Wall 0なのにStormなし | 命令提出時は0でなかった | 次TurnにStorm命令 |
| Siege中も敵Gemが増える | Fort内LabとSite income | Lab・Fort占領を急ぐ |
| ReliefとSallyが合流しない | Phase・命令・到達失敗 | Turn Orderを確認 |
| Magic Phase救援がSiegerを攻撃しない | Fort内部へ入る処理 | normal reliefか第三者Pressure |
| Stormで前衛が詰まる | Choke・Size・Squad過多 | Storm forceを絞る |
| Stormで全軍Rout | Morale・Commander死亡 | Leadership分散・Fear対策 |
| Fort内が病気になる | Supply不足・長期Siege | Army分割・早期救援 |
| 敵がFortを無視する | Map上Chokeでない | Mobile Armyと後方Riskを作る |
| Fortを取った直後に奪回される | Relief・Gem不足 | 占領後防衛を事前準備 |

---

# よくある誤解

## 「Fortを建てれば敵Movementを止める」

Fortに自動Zone of Controlはありません。

敵が無視できない地形・経済・退路・Armyを作って初めてChokeになります。

## 「高いWallほど常に良いFort」

後方Mage FortではCommander PointとAdministrationの方が重要な場合があります。

## 「Field Battleに勝てばProvinceを取った」

Fort内部は残ります。包囲とStormが必要です。

## 「壁が0になるTurnにStormできる」

StormはSiege damageより先です。通常は次Turnです。

## 「Siege Strengthが高ければStormにも強い」

壁破壊能力とGate戦闘能力は別です。

## 「Fort内へ全軍を入れれば安全」

Supply、Disease、Rout、Remote attack、Storm AoEが悪化します。

## 「Teleportで包囲Armyを攻撃できる」

Besieged側のMagic Phase movementはFort内部へ入る場合があり、Siegerを直接攻撃できるとは限りません。

## 「Stealthなら包囲中も全て自由」

出入り、Assassination、Storm参加、Patrol detectionは別処理です。

## 「FortがあるProvinceのLabとTempleは絶対安全」

Assassination、Remote ritual、Dominion、Storm、占領後処理があります。

## 「最大Upgradeが国家の完成形」

Fortごとの役割とCommander Point breakpointから必要Tierを選びます。

---

# Fort建設Checklist

```text
Province：
Fortの役割：
Income：
Resources：
隣接Resources：
Connections：
Capitalからの距離：
前線までの距離：
敵の最短到達Turn：
Retreat route：
守るSite / Throne：
Fort type：
Cost：
Build time：
Administration：
Commander Point：
Recruitment Point：
Wall Integrity：
Supply Storage：
Lab：
Temple：
毎Turn雇うMage：
毎Turn雇う兵士：
Builder：
Upgrade予定：
奪われた場合のRisk：
```

---

# Siege計画Checklist

```text
対象Fort：
現在Wall：
想定Siege Turn：
自軍Siege Strength：
敵Siege Defence：
Siege Bonus Unit：
Storm force：
Siege chaff：
Supply：
Gem：
Enemy Relief route：
Enemy Magic Phase：
Retreat route：
Storm可能予定Turn：
Storm後に残すArmy：
```

---

# Relief計画Checklist

```text
Fortが持つ残りTurn：
Fort内Army：
外部Relief Army：
Break Siege命令：
到着Phase：
Map Move：
Magic Phase Unit：
Stealth Unit：
Enemy reinforcement：
勝利条件：
失敗時の第二防衛線：
```

---

# Storm計画Checklist

```text
Wall 0を確認：
外側のRelief戦：
Gate screen：
Damage Squad：
AoE / Control：
Resistance：
Morale：
Fatigue管理：
Wall defender対策：
Flying / Ethereal対策：
Commander redundancy：
Bodyguard：
Battlefield Enchantment：
Retreat不能Risk：
占領後のGem・Supply：
```

---

# Battle Replayで見るFort戦

詳細は[Battle Replayの読み方](../getting-started/battle-replay.md)を参照してください。

Fort関連では次を記録します。

1. Field BattleとStormのどちらか
2. Relief ArmyとSallyが同じBattleへ参加したか
3. Gateへ最初に入ったSquad
4. Unitが突破口で詰まったか
5. Wall defenderの射撃対象
6. Friendly Fire
7. Casterが何Round生存したか
8. Fatigue 100へ達したRound
9. Commander死亡とRoutの順序
10. 守備CommanderがRetreatしたか
11. Storm後に残ったGem
12. 次TurnのReliefへ耐えられるか

---

# 検証が必要な細部

次は独立Testへ分離する価値があります。

- Dom6.35でのSiege Strength・Siege Defenceの全丸め
- Castle Defence Bonusの最終寄与
- Mindless・Animal・Undisciplinedの全係数
- Hiding UnitとCommanderのSiege Defence
- SneakでFortへ入ったTurnの全Storm参加条件
- Magic Phase movementとBesiegerへの攻撃の全例外
- Cave entrance・別PlaneをまたぐResource吸収
- Fort固有Wall defenderの国家別一覧
- Storm時のFlying・Ethereal・Scale Wallsの全経路
- Fort enchantmentの重複と解除
- 同TurnにWallを増減する複数Ritualの順序
- 占領時のLab・Temple・Inventoryの全例外

この総合ページでは、戦略判断へ必要な主要ルールを扱い、特殊例は断定しすぎない方針とします。

---

## 関連ページ

- [Province](province.md)
- [Dominion](dominion.md)
- [Throne of Ascension](thrones.md)
- [ターン処理順](../reference/turn-resolution.md)
- [戦闘ルール](../basics/combat-rules.md)
- [命令とBattle Script](../basics/orders.md)
- [最初の戦争](../getting-started/first-war.md)
- [Battle Replayの読み方](../getting-started/battle-replay.md)
- [Research](../magic/research.md)
- [GemとCombat Gem](../magic/gems.md)
- [データ索引](../data/index.md)

## 主な情報源

- [Dominions 6公式Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [illwiki: Forts](https://illwiki.com/dom5/fort)
- [illwiki: Siege](https://illwiki.com/dom5/siege)
- [illwiki: Strength](https://illwiki.com/dom5/dom6/strength)
- [illwiki: Stealth](https://illwiki.com/dom5/dom6/stealthy)
- Dominions 6.35ゲーム内Fort Tooltip、Host Message、Battle Replay

!!! note "記事状態"
    Fortの経済層、建設Timing、Field BattleからSiege・Stormへの流れ、Relief・Sally、Wall 0とStormのTurn差、主要なStorm戦設計は6.35を対象にレビューしています。全Fort type、国家固有Wall defender、特殊Trait、Ritual、別Planeの内部例外を実験的に証明した状態ではないため、記事Statusは`reviewed`としています。
