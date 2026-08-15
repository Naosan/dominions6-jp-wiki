---
title: ターン処理順
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# ターン処理順

Dominions 6では、全Playerが命令を提出したあと、Hostが全国家の命令をまとめて処理します。

画面上では「同時Turn」に見えても、内部では、

> **Research → Recruitment → Ritual → Assassination → Movement → Battle → Event → Economy → Dominion → Healing**

のように、決められた順序で処理されます。

この順番を知る目的は、番号を暗記することではありません。

> **同じTurnに出した二つの命令のうち、どちらが先に成立し、後の処理へどんな状態を渡すか**

を判断できるようにすることです。

たとえば、

- Assassinationは通常Movementより先
- 味方Province間の移動は敵Provinceへの侵攻より先
- Main BattleはFort stormより先
- Siege damageはFort stormより後
- IncomeはPatrolによるUnrest低下より先
- Dominion spreadは通常Battleより後

です。

この差が、Armyの合流、Fort攻略、Stealth、Gem運用、Income、Dominion戦の結果を変えます。

!!! note "このページの精度範囲"
    本文はDominions 6.35を対象に、現行Manual、公式Documentation、現行IllwikiのTurn Order Sequence、ゲーム内Message・Battle Replayで確認できる挙動を整理しています。Manualに明記されない細部にはCommunity test由来の項目があり、同一Phase内の順序、特殊Spell、Event、別Plane、Season変化などには例外や未確定部分があります。そのため記事Statusは`reviewed`であり、全内部処理を実験的に証明した`verified`ではありません。

---

## 最初に覚える四つ

### 1. 全国家の命令はPlayer順に処理されるわけではない

Turnを先に提出したPlayerが先に動くわけではありません。

Hostは全Playerの命令を集め、処理種類ごとのPhaseへ分けます。

```text
全員のResearch
→ 全員のRecruitment
→ 全員のRitual
→ 全員のMovement
→ 全員のBattle
```

という考え方です。

### 2. 同じPhase内では順番が固定されないことがある

RitualはRandom orderで処理されます。Main BattleもRandom orderで解決されます。

したがって、

- 二国が同じUnique対象を狙う
- 複数のRitualが同じProvinceを変化させる
- 同じTurnに複数Provinceで戦闘する
- Retreat先の所有者が他Battleで変わる

といった場合、Phase番号だけでは最終結果を一意に決められないことがあります。

### 3. 早い処理は、後でCommanderが死んでも成立している

Research、Recruitment、Forgeなどは、Assassinationや通常Battleより前です。

Researcherがその後Assassinationで死亡しても、そのTurnのResearchはすでに処理されています。

### 4. 「今見えている状態」と「次のTurnの状態」を分ける

Season、Event、Dominion spread、Patrol、Building completionなどはBattleより後に処理されることがあります。

そのため、

> **このTurnのBattleへ間に合う変更**

と、

> **次Turnから利用できる変更**

を分けて考えます。

---

# Phase早見表

| 範囲 | Phase | 主な処理 | 戦略上の意味 |
|---:|---|---|---|
| 0 | Stealth準備 | Sneak前の潜伏切替 | 後続のRitual・Assassinationより早い |
| 1–10 | Pre-Battle | Message、Research、Recruit、Forge、Preach、Ritual | 生産・研究・魔法準備が戦闘より先 |
| 11–14 | Magic / Extra-planar Battle | Teleport系、別Plane戦、退却 | Magic Phase部隊は通常Armyより先に戦う場合がある |
| 15–19 | Godly Intermezzo | Site Search、Prophet、Call God、Awakening、Blood Hunt | 神・宗教・Blood経済の処理 |
| 20–22 | Horror・Assassination・Raid | Horror attack、暗殺、誘惑、Raid | CommanderをMovement前に失う可能性 |
| 23 | Relinquish | Province返還 | Disciple Game専用 |
| 24–25 | Movement | 味方間移動、敵地移動、Break Siege | 防御側の合流が侵攻より先 |
| 26–28 | Main Battle | Field Battle、Fort storm、退却 | Field Battleの後にFort戦 |
| 29–32 | Event | Global効果、Event、Event Battle | 通常Battle後に世界・Provinceが変化 |
| 33–34 | Item / Unit Effect | 自動効果、Patrol detection | Stealth発見はMovement後 |
| 35–47 | Admin | Siege、Building、Pillage、Income、Upkeep、Dominion、Aging | 内政・維持費・宗教効果の本処理 |
| 48 | Leftover Battle | 残余戦闘 | 特殊・未整理の戦闘枠 |
| 49–62 | Finalization | Healing、Mercenary、Hero、Scouting、Victory、Immortal | 次Turnの状態を確定 |

---

# 完全処理順

番号`0`は、Manualの通常番号より前にあるCommunity側の補助的な整理です。

## 0：Stealth準備

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 0 | Sneakを行うStealthy Unitが潜伏状態へ移る | 後続のRitual、Assassination、通常Movementより前に隠れる |

Stealthy CommanderへSneak系Orderを出している場合、通常のRitualやAssassinationで出発Provinceへ干渉しようとしても、すでに隠れていることがあります。

これは「Stealthyなら何をしても安全」という意味ではありません。到着先では後のPatrol detectionにより発見される可能性があります。

---

## 1–10：Pre-Battle Phase

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 1 | Messageと添付資源の送付 | Gold、Gem、Itemの外交送付は非常に早い |
| 2 | Research | Researcherが後で死亡しても、そのTurn分は計上済み |
| 3 | Empowerment | Path上昇が適用される |
| 4 | Recruitment | 新Unit・Commanderが後続Phase前に出現する |
| 5 | Forge | Itemが国家Inventoryへ作成される |
| 6 | 通常Preach | Dominion変化が後続Battleへ影響し得る |
| 7 | HereticによるDominion低下 | Preach直後とされるが細部は要追加検証 |
| 8 | Claim Throne | Throne claimが後続処理より先に成立 |
| 9 | Siteへ入るOrder、Pearl cultivation等 | 特殊なProvince・Unit Order |
| 10 | RitualをRandom orderで処理 | Remote Spell、Magic Movement、Global等の発動 |

### Message

Gold、Gem、Itemの送付はTurnの最初期です。

後のAssassinationやBattleで送信者が死亡しても、送付処理はすでに終わっています。

ただし、このTurnにForgeされたItemを同じTurnのMessageで送ることはできません。MessageはForgeより先だからです。

### Research

ResearchはAssassination、Movement、Battleより先です。

したがって、Researcherがその後死亡しても、そのTurnのResearch Pointは失われません。

新しいResearch LevelがこのPhaseで完成すると、後続Battle時点ではそのLevelが解禁済みです。ただしTurn提出時点で未研究だったSpellは、通常は事前Scriptへ指定できません。Script後の`Cast Spells`でAIが利用する可能性はあります。

### Empowerment

Empowermentは早期に適用されます。

ただしEmpowerment自体がCommanderのそのTurnのOrderです。同じCommanderがEmpowermentしながらRitualをCastしたり通常Movementしたりするわけではありません。

### Recruitment

新規Recruitは後続Battleより前に存在します。

そのため攻撃を受けるProvinceでは、新しく雇ったUnitが防衛状態へ存在し得ます。

ただし、

- Fort内にいるか
- Field側にいるか
- Commanderへ編成済みか
- Leadershipがあるか

は別問題です。

### Forge

ForgeされたItemは国家Inventoryへ入ります。

しかしCommanderへの装備割当はHost中に自動で行われません。

> **このTurnに作ったItemを、このTurnのBattleで装備する**

ことは通常できません。

### PreachとDominion spreadの違い

PreachはBattleより前ですが、Temple等による通常のDominion spreadはStep 43で、Battleより後です。

したがって、

- Preachで変化したCandleは同TurnのBattleへ影響し得る
- 通常Dominion spreadは同TurnのMain Battleには間に合わない

という違いがあります。

### Ritual

RitualはRandom orderです。

含まれる代表例：

- Remote damage
- Remote summon
- Site Search Spell
- Teleport系Magic Movement
- Global Enchantment
- Province環境を変えるSpell
- Summon

同じ対象へ複数国家がRitualを使う場合、どれが先になるかを前提にしすぎない方が安全です。

---

## 11–14：Magic・Extra-planar Battle

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 11 | Ritualが原因のBattle | Teleport、Wind Ride等による戦闘 |
| 12 | Inferno・Kokytos滞在Damage | 別Plane固有処理 |
| 13 | 別Plane上、または別Planeからの移動に伴うBattle | Extra-planar戦闘 |
| 14 | このPhaseのBattleからのRetreat | 通常Movementより前に退却が確定 |

## Magic Phase Armyは通常Armyより先に到着する

Teleport、Cloud Trapeze等のMagic Movementで敵Provinceへ入る部隊は、通常MovementのArmyが到着する前に戦う場合があります。

```text
Ritual Cast
→ Magic Phase Battle
→ 通常Movement
→ Main Battle
```

したがって、

> TeleportしたMageが、歩いて来る本隊と同時に戦う

とは限りません。

Magic PhaseでBattleが発生すると、同Provinceで`Attack Current Province`等を指定したStealthy Unitがその戦闘へ参加する場合があります。Magic Phase Battleが発生しなければ、それらはMain Battle側で処理されます。

### 実戦上の用途

- Magic PhaseでPDや少数守備を排除する
- Fort上の敵Commanderを先に狙う
- 本隊到着前にBattlefield条件を変える
- Stealth部隊とMagic Phase部隊を合わせる

### 主なRisk

- 通常Armyがまだ来ておらず、Mageが単独戦闘する
- 敵主力が想定外に残っている
- Magic Phase Battle後のRetreat先が悪い
- Ritual順がRandomで前提が崩れる

---

## 15–19：The Godly Intermezzo

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 15 | Commander OrderによるSite Search | Search Spellではなく現地探索 |
| 16 | Prophet宣言 | 新Prophetが成立 |
| 17 | Call God | Pretender復活への祈りを処理 |
| 18 | Dormant / Imprisoned GodのAwakening、復活処理 | Godが出現する |
| 19 | Blood Hunt | Blood Slave獲得処理 |

### Site Search Spellとの違い

- Site Search Spell：Step 10のRitual
- Province内での`Search for Magic Sites`：Step 15

です。

Search Spellで先にSiteが見つかっても、同じTurnにそのSiteのIncomeやRecruitをすべて利用できるとは限りません。Income、Site effect、Recruitmentはそれぞれ別Phaseです。

### ProphetとGod

Prophet宣言やAwakeningは通常Movementより前です。

ただし新しく出現したGodが、そのTurnに改めてMovement Orderを受け取ることはできません。OrderはHost前に提出済みだからです。

---

## 20–22：Horror・Assassination・Raid

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 20 | Horror MarkによるHorror attack | CommanderがMovement前に襲われ得る |
| 21 | Assassination・Seduction | CommanderをMovement前に排除できる |
| 22 | Raid Order | 通常Movementより先にRaidを処理 |

## AssassinationはMovementより先

これはTurn Orderで最も重要な関係の一つです。

```text
Assassination
→ Friendly Movement
→ Hostile Movement
→ Main Battle
```

敵Armyの唯一のCommanderをAssassinationで倒した場合、配下Unitは通常Movementできません。

ただし、

- 別Commanderがいる
- Assassinが失敗する
- Target選択が想定と違う
- Mindless・Undead Leadership等の別条件がある

ならArmyは予定どおり動く可能性があります。

### Seduction

Seductionも通常Movementより前に処理されます。

成功・失敗の結果としてCommanderが別Provinceへ移動したりBattleになったりするため、後続Movement計画へ影響します。

### Raid

Raidは通常侵攻とは別Orderで、通常Movement前に処理されます。

Raid後に同じCommanderがさらに通常Movementするわけではありません。CommanderのOrderはRaidです。

---

## 23：Relinquish Province

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 23 | ProvinceのRelinquish | Disciple GameでProvinceをTeam内へ返還 |

通常Gameではほぼ関係しません。

詳しくは[Disciple Game](../systems/disciple-game.md)を参照してください。

---

## 24–25：Movement

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 24 | 味方Province間のMovement | 防御側が侵攻前に合流できる |
| 25 | 敵対ProvinceへのMovement、Break Siege | 侵攻・包囲突破 |

# Friendly Movementが先

味方Provinceから味方Provinceへの移動は、敵Provinceへの侵攻より先です。

そのため、敵が攻め込む予定のProvinceへ複数方向から防衛Armyを集めることができます。

```text
北の自軍 → 中央自領
南の自軍 → 中央自領
敵Army   → 中央自領
```

この場合、北・南の自軍がStep 24で先に中央へ入り、その後Step 25の敵侵攻を迎えます。

## Magic Phaseで中継Provinceを失った場合

複数Provinceを通るMovementでは、予定していた中継ProvinceがMagic Phase Battleで敵領になった場合、Armyが移動しないことがあります。

Map上でOrderを出した時点の経路だけでなく、Magic Phase後の所有状態が影響します。

## Hostile Movement

敵対Provinceへの侵攻と、FortからのBreak Siegeはここで処理されます。

複数Armyが同じ敵Provinceへ入った場合、Battle自体は次のMain Battle Phaseです。

---

## 26–28：Main Battle

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 26 | Main Battle | Movementで同Provinceへ入った敵Army同士が戦う |
| 27 | Fort storm Battle | Field Battle後に要塞内部へ攻撃 |
| 28 | このPhaseからのRetreat | Battle結果に応じて退却 |

# Main BattleはRandom order

複数ProvinceでBattleがある場合、BattleはRandom orderで解決されます。

Provinceの所有者がBattleで変わるため、他BattleからのRetreat先や特殊条件へ影響する可能性があります。

すべてのBattleがMap番号順、Player順、Army規模順で解決されるとは考えない方が安全です。

# Field Battleの後にFort storm

同じProvinceで外部ArmyとのField Battleが発生する場合、まずStep 26で解決されます。

その後、Fort storm Orderが成立していればStep 27で要塞戦です。

Main Battleから退却した敵Unitの一部がFort内へ入った場合、そのUnitが続くFort stormへ存在する場合があります。

# このTurnのSiege damageで壁を0にしても、Stormは次Turn

Siege damageはStep 35です。

Fort stormはStep 27なので、

```text
Step 27：Fort storm
Step 35：Siege damage
```

という順です。

したがって、通常はこのTurnのSiege damageで壁を破壊しても、Fort storm Phaseはすでに終わっています。Storm Orderを実行するのは次Turnになります。

これはFort戦争の重要な一Turn差です。

---

## 29–32：Global・Event

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 29 | Global EnchantmentのTurn効果 | Main Battle後に発生するGlobal効果 |
| 30 | Random Event・Player起因Event | Province・Unit・Scale等が変化 |
| 31 | Event Battle | Barbarian attack等のEvent戦闘 |
| 32 | Event BattleからのRetreat | Event戦の退却 |

# Eventは通常Battleより後

EventによるProvince変化やTemperature変化は、Main Battleへ間に合わない場合があります。

特に、Wolven WinterやBreath of the DesertによるTemperature変更はRitual PhaseではなくEvent Phaseで発生します。

```text
Ritual Cast
→ Main Battle
→ Temperature Event
```

したがって、同TurnのMain Battleは変更前のTemperatureで戦う可能性が高く、変更は次TurnのBattle環境へ反映されると考えるのが安全です。

SeasonそのものによるTemperature変化の厳密な位置には未確定部分がありますが、実戦上は、

> **現在見えているTemperatureが、このTurnの通常Battle条件**

という扱いが安全です。

---

## 33–34：Item・Unit自動効果とStealth発見

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 33 | Reaper、自動Summon、Item・MonsterによるScale変化等 | Event後、Income前の自動効果 |
| 34 | PatrolによるStealthy Unit発見 | Movement後に潜伏Unitを探す |

# Stealth detectionはMovement後

Patrol detectionはStep 34です。

そのため、

- Provinceを出ていくStealthy Unitは出発地Patrolに捕まりにくい
- 到着したStealthy Unitは目的地Patrolに発見され得る

という関係になります。

```text
Sneak Movement
→ 到着
→ Patrol detection
```

発見された場合は、その場でBattleになります。

# Bane Venom Charm等が先

Item・Unit自動効果はPatrol detectionより先です。

Bane Venom CharmのようなProvinceへ影響する効果は、所持者がPatrolで発見される前に作用し得ます。

---

## 35–47：Admin Zone

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 35 | Siege damage | Fort壁を削る |
| 36 | Building建設・破壊 | Fort、Lab、Temple等を完成・破壊 |
| 37 | Reanimation・Summon Allies | 自動・Commander OrderによるUnit生成 |
| 38 | Pillage | Population・Unrest等へ影響 |
| 39 | Income | Gold・Gem等のTurn収入 |
| 40 | Dominion・Scale・PatrolによるUnrest変動 | PatrolのUnrest低下はIncome後 |
| 41 | Starvation | Supply不足の影響 |
| 42 | Upkeep | 軍・Commander維持費 |
| 43 | Dominion spread | Temple・Pretender等からCandle拡散 |
| 44 | Dominion固有効果 | Popkill、Insanity、Temperature、Turmoil等 |
| 45 | Magic Site効果 | Disease等のSite効果 |
| 46 | 超大規模GameのUnit数制限処理 | 約15万Unit時の技術的整理 |
| 47 | Aging | Unitが加齢する |

# Siege damageとBuilding

Siege damageが先、Building完成が後です。

新しいFort、Lab、TempleがこのPhaseで完成しても、

- RecruitmentはStep 4
- RitualはStep 10
- BattleはStep 26–27

です。

したがって、新Buildingを同Turnの前半処理へ遡って利用することはできません。

### 例：Lab完成

```text
Step 10：Ritual Phaseはすでに終了
Step 36：Lab完成
```

Labを使ったRitualやItem transferは次Turnからです。

# PillageはIncomeより先

PillageはStep 38、IncomeはStep 39です。

PillageによるPopulation・Unrest変化は、このTurnのIncomeへ影響し得ます。

# IncomeはPatrolによるUnrest低下より先

IncomeはStep 39、Patrol等によるUnrest低下はStep 40です。

したがって、Unrestの高いProvinceを同TurnにPatrolしても、

> **Patrol後の低いUnrestで、そのTurnのIncomeを受け取る**

わけではありません。

Incomeは先に低下した状態で計算され、Patrolの恩恵は主に次Turnへ現れます。

# StarvationはBattleより後

StarvationはStep 41です。

ArmyはSupplyの悪いProvinceへ侵攻し、そのTurnのBattleを行った後にStarvation処理を受けます。

つまり、十分に補給されたArmyはWasteland等へ一度入り、そのBattleを戦ってからSupply不足の影響を受けることがあります。

ただし長期滞在、Siege、次Battleでは問題が蓄積します。

# Incomeの後にUpkeep

Incomeが先、Upkeepが後です。

Treasuryを評価するときは、

```text
Turn Income
－ Upkeep
－ 次TurnのRecruit / Building / Mercenary予算
```

まで見ます。

# Dominion spreadはBattleより後

通常のDominion spreadはStep 43です。

同TurnのMain BattleはStep 26なので、Battleに使われるDominionは、主にHost前の状態と早期Preach結果です。

Temple check等で後から広がったCandleは、次Turnの戦場・Income・Scaleへ影響します。

# Dominion effectとSite effect

Dominion固有の、

- Population kill
- Insanity
- Temperature変化
- Turmoil変化

などはStep 44です。

Magic Site固有のDisease等はStep 45です。

これらはBattle後ですが、後のHealing・Disease処理へ影響する場合があります。

---

## 48：Leftover Battle

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 48 | 残余Battle | 通常区分へ入らなかった特殊Battle |

現在のCommunity資料でも、この枠に入る全Battle種類は完全には整理されていません。

通常の戦略判断では、Magic Phase、Main Battle、Fort storm、Event Battleを優先して考えます。

---

## 49–62：Finalization

| No. | 処理 | 実戦上の意味 |
|---:|---|---|
| 49 | HealingとDisease | Battle後にHP・Affliction・Disease処理 |
| 50 | Insanity発生 | 次TurnのCommander Orderへ影響 |
| 51 | Mercenary bid解決・Mercenary出現 | このTurnのBattleには参加しない |
| 52 | Hero出現 | 次Turnから利用 |
| 53 | 敵地でCommanderを失ったUnitの削除 | Leadership喪失の最終処理 |
| 54 | Besieger不在FortがProvinceを奪回 | Fort側が外部Province controlを戻す |
| 55 | Scouting report生成 | 新Turnで読む情報を作る |
| 56 | Defeat condition確認 | Nation消滅等を判定 |
| 57 | Victory condition確認 | Throne等の勝利判定 |
| 58 | Stat graph更新 | Graph情報を確定 |
| 59 | Heroic Ability更新 | Heroic progress |
| 60 | Immortal再生 | Immortalが復活 |
| 61 | Population不足によるPD低下 | 10 Population / PD pointを維持できない場合 |
| 62 | Aftermath | Order validation、強制Shape change等 |

# HealingはBattle後

Battle前に自然回復してから戦うのではありません。

Battleを終えた後にHealingとDiseaseが処理されます。

負傷したThugやMageを同TurnにBattleへ投入するときは、Host後のHealingを先取りして考えないようにします。

# MercenaryとHeroはBattle後に出現

Mercenary bidはStep 51です。

そのTurnに落札したMercenaryは、すでに終わったMain Battleへ参加できません。

HeroもStep 52で出現するため、次Turnから利用します。

# Commanderを失ったUnit

敵地でCommanderを失い、誰にも率いられていないUnitはStep 53で失われる場合があります。

Battleに勝った兵が残っていても、Leadershipを失った状態で敵地に取り残されると保存できないことがあります。

# FortのProvince奪回

Fort内に守備側が残り、外部を包囲するArmyがいなくなった場合、Step 54でFortがProvince controlを取り戻します。

Field Armyが退却・消滅した後のProvince所有を考える際に重要です。

# Scouting reportは最後に近い

Scout reportはStep 55で、新Turnの最終状態に近い情報として生成されます。

ただしStealth値、Spy能力、Dominion、Event等によって、完全な情報になるとは限りません。

# Victory checkは非常に遅い

Defeat check、Victory checkは、Battle、Event、Income、Dominion spread、Fort奪回などの後です。

ThroneをClaimする処理自体はStep 8ですが、最終勝利判定はStep 57です。

# ImmortalはBattle後に再生

Immortal reformはStep 60です。

このTurn中に死亡から復帰して同じTurnのBattleへ再参加するわけではありません。復活後は次Turnの状態として現れます。

---

# 重要な前後関係

| 問い | 先 | 後 | 結論 |
|---|---|---|---|
| ResearcherがAssassinationされる | Research | Assassination | そのTurnのResearchは計上される |
| RecruitしたProvinceが攻撃される | Recruitment | Battle | 新Recruitはすでに存在する |
| Forge Itemを同Turnに装備する | Forge | Battle | Itemは作れるが自動装備されない |
| Teleport部隊と徒歩Armyを合わせる | Magic Battle | Normal Movement | Magic部隊が先に単独戦闘し得る |
| Assassinで敵Armyを止める | Assassination | Movement | 唯一のCommanderを倒せば移動阻止になり得る |
| 防衛Armyと侵攻Armyが同Provinceへ行く | Friendly Movement | Hostile Movement | 防衛側は先に合流できる |
| Field BattleとFort storm | Main Battle | Fort storm | 外部戦の後に要塞戦 |
| 壁を0にして即Stormする | Fort storm | Siege damage | 同TurnのSiege damage後にはStorm Phaseが残っていない |
| Wolven Winterと同Turn侵攻 | Main Battle | Temperature Event | 同TurnBattleへTemperature変更が間に合わない |
| Sneak移動とPatrol | Movement | Patrol detection | 到着先で発見され得る |
| PatrolしてIncomeを戻す | Income | Patrol unrest reduction | 改善は主に次TurnIncomeへ効く |
| Building完成とRitual | Ritual | Construction | 完成Labは次Turnから利用 |
| BattleとStarvation | Battle | Starvation | 侵入TurnのBattle後に飢餓処理 |
| Battleと通常Dominion spread | Battle | Dominion spread | spread後のCandleは次Turn中心 |
| BattleとHealing | Battle | Healing | 戦闘後に回復 |
| Mercenary落札とBattle | Battle | Mercenary arrival | 落札Turnの戦闘には不参加 |
| Immortal死亡と復帰 | Battle | Immortal reform | 復帰はBattle後 |

---

# 実戦例

## 例1：新Recruitで急襲を守る

状況：

- Border Provinceで兵をRecruit
- 同Turnに敵が侵攻

処理：

```text
Step 4：Recruitment
Step 25：敵Movement
Step 26：Battle
```

新RecruitはBattle前に存在します。

ただしCommanderへ編成されていない、Fort内部にいる、Leadership不足などにより、期待した形で戦えない場合があります。

---

## 例2：Research完成Turnの戦闘

状況：

- このTurnのResearchでAlteration Levelが上がる
- 同Turnに敵とのBattleがある

処理：

```text
Step 2：Research完成
Step 26：Battle
```

Battle時点ではResearch Levelは解禁済みです。

ただしTurn提出時に未研究だったSpellを手動Scriptできなかった場合、確実なCastは保証できません。AIの`Cast Spells`へ依存するか、次TurnにScriptします。

---

## 例3：Teleport Mageと通常Army

状況：

- MageをTeleport
- 隣接Provinceから本隊も侵攻

処理：

```text
Step 10：Teleport Ritual
Step 11：Magic Phase Battle
Step 25：本隊Movement
Step 26：Main Battle
```

Mageは本隊より先にBattleへ入る可能性があります。

本隊と合わせたいなら、

- Magic Phaseに敵Battleが起きない条件を作る
- Stealth部隊を利用する
- Mage単独でも生存できるScriptにする
- 一Turnずらす

などを考えます。

---

## 例4：Assassinationで侵攻を止める

状況：

- 敵ArmyのCommanderが一人
- そのCommanderをAssassination
- 敵は同Turnに侵攻Order

処理：

```text
Step 21：Assassination
Step 25：Hostile Movement
```

Assassinationが成功し、代替Commanderがいなければ、UnitはMovementできません。

ただしAssassinationのTargetと成功は確率的です。侵攻阻止をAssassin一人へ完全依存させない方が安全です。

---

## 例5：防衛Armyの合流

状況：

- 二つの自領から中央Provinceへ防衛Armyを動かす
- 敵も中央へ侵攻

処理：

```text
Step 24：味方Army二つが中央へ合流
Step 25：敵Armyが中央へ侵攻
Step 26：Battle
```

防衛側は先に合流できます。

この仕組みは、中央位置、Road、Map Move、Fort網の価値を高めます。

---

## 例6：Wolven Winterを侵攻へ合わせる

状況：

- Wolven WinterでColdへ変える
- Cold適性Armyが同Turnに侵攻

処理：

```text
Step 10：Ritual Cast
Step 26：Main Battle
Step 30：Temperature Event
```

Temperature変更はBattle後です。

同TurnBattleでCold環境を前提にしたScriptは失敗する可能性があります。次Turnの戦闘計画として使います。

---

## 例7：SpyをPatrolで捕まえる

状況：

- 敵Spyが自ProvinceへSneak
- 自軍がPatrol

処理：

```text
Step 24–25：Sneak Movement
Step 34：Patrol detection
```

Spyは到着後にPatrol判定を受けます。

逆に、すでにProvinceを出ていくSpyを出発地Patrolで捕まえることは難しくなります。

---

## 例8：PatrolでUnrestを下げてIncomeを回復する

状況：

- Unrestが高いProvince
- 大軍でPatrol

処理：

```text
Step 39：高UnrestのままIncome計算
Step 40：PatrolでUnrest低下
```

そのTurnのIncomeはすでに計算済みです。

Patrolの経済効果は主に次Turnから現れます。

---

## 例9：壁を壊して即Storm

状況：

- Fort壁があと少し
- このTurnのSiegeで0になる見込み

処理：

```text
Step 27：Fort storm Phase
Step 35：Siege damage
```

壁が0になるのはStorm Phase後です。

通常は、

```text
Turn A：Siege damageで壁を0
Turn B：Storm Fort
```

となります。

---

## 例10：Mercenaryを救援に使う

状況：

- Border Fortが攻撃される
- 同TurnにMercenary bid

処理：

```text
Step 26–27：Battle
Step 51：Mercenary bid解決・出現
```

新Mercenaryは救援Battleに間に合いません。

次TurnのRelief Army、Patrol、Siege参加として計画します。

---

# Turn Orderを使った計画手順

## 1. 同じTurnに行う二つの処理を書く

例：

```text
Assassination
敵ArmyのMovement
```

## 2. 番号を調べる

```text
Assassination：21
Hostile Movement：25
```

## 3. 先の処理が後へ何を渡すか考える

```text
Commander死亡
→ 配下UnitがMovementできるか
```

## 4. 同一PhaseのRandom orderを確認する

Ritual、Main Battle等では番号だけで決まらない場合があります。

## 5. 失敗条件を列挙する

```text
Assassinが負ける
別Commanderがいる
Targetが違う
ArmyがMindless Leadershipで動く
```

## 6. ReplayとMessageで確認する

- 何が何番目にMessageへ出たか
- Province所有がいつ変わったか
- CommanderがどのPhaseで消えたか
- BattleがMagic PhaseかMain Phaseか
- EventがBattle前後のどちらか

を記録します。

---

# よくある誤解

## 「同時Turnだから、攻撃側と防御側は同時に動く」

味方Province間Movementが先です。防御側は侵攻前に合流できます。

## 「Teleport部隊と徒歩部隊は同じBattleへ入る」

Magic Phase Battleが先に発生すると、Teleport部隊だけで戦います。

## 「壁がこのTurnに0になるならStormできる」

Storm PhaseはSiege damageより先です。

## 「Patrolしたから今TurnのIncomeは戻る」

Income計算が先です。

## 「DominionがこのTurn広がるからBattleでも有利になる」

通常Dominion spreadはBattle後です。早期Preachは別です。

## 「Event系Temperature RitualはCast直後にBattleへ効く」

Temperature EventはMain Battle後に発生します。

## 「新しく落札したMercenaryが今Turnの戦闘へ来る」

Mercenary出現はBattle後です。

## 「Immortalは死亡したTurnに再び戦える」

Immortal reformはすべての主要Battle後です。

## 「番号が分かれば結果を完全予測できる」

Ritual・Main BattleのRandom order、Target選択、DRN、Event、Retreat、特殊能力により結果は揺れます。

Turn Orderは結果を保証する表ではなく、**因果関係を整理する骨格**です。

---

# 未確定・追加検証項目

現行資料でも、次は完全には確定していません。

- Blood Sacrificeと通常Preachの厳密な同一Phase内順序
- Heretic処理の全例外
- Horror Seedを含むHorror attackの細分類
- Step 48のLeftover Battleへ入る全戦闘種類
- Season変化によるTemperature更新の厳密な位置
- 同一Phase内で複数特殊Effectが競合した場合の順序
- Event Modや特殊Nation能力による独自処理

重要なMultiplayer戦術がこれらへ依存する場合は、専用Test Gameで確認してください。

---

## 関連ページ

- [命令とBattle Script](../basics/orders.md)
- [戦闘ルール](../basics/combat-rules.md)
- [最初の戦争](../getting-started/first-war.md)
- [Battle Replayの読み方](../getting-started/battle-replay.md)
- [Research](../magic/research.md)
- [GemとCombat Gem](../magic/gems.md)
- [Site Search](../magic/site-search.md)
- [Fort](../systems/forts.md)
- [Dominion](../systems/dominion.md)
- [Province](../systems/province.md)
- [Disciple Game](../systems/disciple-game.md)

## 主な情報源

- [Dominions 6 Official Documentation](https://illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Illwiki: Turn Order Sequence](https://illwiki.com/dom5/turn-order-sequence)
- [Illwiki: Stealth](https://illwiki.com/dom5/dom6/stealthy)
- Dominions 6.35のMessage、Strategic Map、Battle Replayによる確認

!!! note "記事状態"
    Phase全体、主要な前後関係、Friendly / Hostile Movement、Magic Phase Battle、Assassination、Fort storm、Event、Income、Patrol、Dominion、Healingの実戦的な意味を6.35向けにレビューしています。Community資料自体が未確定としている細部は本文でも未確定と明示し、断定していません。