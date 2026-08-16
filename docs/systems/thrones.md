---
title: Throne of Ascension・Claim・勝利条件
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# Throne of Ascension・Claim・勝利条件

Throne of Ascensionは、強力なMagic Siteと守備隊を持つ特殊Provinceであり、標準的なGame設定では主要な勝利条件です。

Throne戦は、単に強いIndependentを倒す戦闘ではありません。

> **発見する**
> → **Guardianを分析する**
> → **ProvinceまたはFortを攻略する**
> → **Claim可能者を配置する**
> → **次のHostでClaimする**
> → **同じHostの終了時まで必要Pointを保持する**

という複数Turnの作戦です。

ClaimしたThroneはAscension Pointだけでなく、

- Gem・Blood Slave income
- Bless効果
- Scales
- Dominion spread
- Ritual range
- Mage・Unit recruitment
- Forge・Research・Ritual bonus
- Story Event
- 世界全体への有利・不利な効果

を与える場合があります。

しかし、最終的に重要なのは、

> **このThroneを取ることで何Point増え、いつClaimでき、勝利判定時にそのPointが残っているか**

です。

!!! note "このページの精度範囲"
    本文はDominions 6.35を対象に、現行Manualへの公式導線、公式Dom6変更点、固定したDom6 Inspectorデータ、ゲーム内UI、[ターン処理順](../reference/turn-resolution.md)、および現行Community資料で確認されている主要挙動を実戦向けに整理しています。特殊ThroneのEvent chain、同一Phase内の複数処理、Modded Game、Cataclysm、Automatic claim Event、別Plane、特殊国家・特殊Fortには例外があります。そのため記事Statusは`reviewed`であり、全内部処理を実験的に証明した`verified`ではありません。

---

## 最初に覚える八つ

### 1. Throne LevelとAscension Pointは通常同じ

標準のThrones of Ascension勝利では、

- Level 1 Throne：1 Point
- Level 2 Throne：2 Point
- Level 3 Throne：3 Point

を与えます。

Game開始時に、配置する各Levelの数と、勝利に必要な合計Pointを設定します。

### 2. すべてのLevelでClaim条件はH3

Throne Levelによって必要Holy levelが変わるわけではありません。

通常、Claimできるのは、

- Pretender God
- Disciple
- Holy 3以上のPriest

です。

Prophetは通常H3になるためClaim担当として使えます。

> **Level 1 ThroneならH1、Level 2ならH2でClaimできる、という仕組みではありません。**

H2 PriestをItem・特殊能力等でH3へ上げた場合はClaim可能になりますが、Claim時点で実際にH3へ届いている必要があります。

### 3. 占領とClaimは別

Throne Provinceを所有していても、ClaimしていなければAscension Pointは得られません。

```text
Provinceを占領
≠
ThroneをClaim
≠
勝利条件を達成
```

です。

### 4. ClaimはMovementより前

Claim ThroneはTurn処理のStep 8です。

通常Movement、Magic MovementによるBattle、Assassination、Main Battleより前に処理されます。

したがってClaim担当は、**Turn提出時点ですでにThroneにいなければなりません。**

- 歩いて到着して同TurnにClaim
- Teleportで到着して同TurnにClaim
- Become Prophetして同TurnにClaim

は通常できません。

### 5. 勝利判定はTurn終盤

Claim処理はStep 8ですが、Victory condition確認はStep 57です。

そのため、Claimで一時的に必要Pointへ到達しても、同じHostの後半で別のClaim済みThroneを失えば勝利できない場合があります。

### 6. Fortを包囲しただけではThroneを奪っていない

Claim済みThroneにFortがあり、防御側がFort内部を保持している場合、外側を包囲しただけでは通常Throneは防御側のものです。

FortをStormして奪うまで、敵のAscension Pointを消せないことがあります。

### 7. Independent Throne MageのGemはPingで枯れない

Throne GuardianのMageは、戦闘ごとにGemを補充します。

Scoutを繰り返し送り、敵のGemを消耗させてから本隊を送る、という通常のGem baitは期待どおり機能しません。

Pingの目的は、Gem枯らしではなく、

- Mage Path
- Spell選択
- Battlefield Enchantment
- Formation
- Commander数
- Damage type

を知ることです。

### 8. Claimは利益だけでなく世界を変える

一部Throneは、Claim時またはClaim後に、

- Global Scale変化
- Disease
- Unrest
- Monster attack
- Story Event chain
- Population loss
- 特殊召喚

を発生させます。

Pointだけを見てClaimせず、Throne説明の、

```text
通常のSite効果
Effects from claimed throne
特殊Event説明
```

を分けて読みます。

---

# 6.35のThroneデータ

固定したDominions 6.35データでは、Throne Siteは合計74件あります。

| Level | 登録数 | 標準Ascension Point |
|---:|---:|---:|
| 1 | 36 | 1 |
| 2 | 26 | 2 |
| 3 | 12 | 3 |
| 合計 | 74 | — |

全Throneの、

- Gem income
- Scale
- Dominion spread
- Recruitment
- Summon
- Research・Forge・Ritual効果
- Terrain制限
- Event

は、[Throneデータ一覧](../data/sites/thrones.md)を参照してください。

## Throne cluster

一部ThroneにはClusterがあり、同じClusterのThroneは同一Gameへ一緒に出現しやすくなります。

たとえば季節を表すThrone群などです。

一つを発見したとき、残りのThrone出現を完全に予測できるわけではありませんが、

> **Throne配置はすべて独立な抽選ではない**

ことは覚えておく価値があります。

## Terrain制限

Throneによって、

- Land only
- Sea / Deep Sea
- Cave
- 特殊Terrain
- Wild defender

などの条件があります。

海・洞窟・別PlaneのThroneは、Pointだけでなく、

- Amphibious access
- Water Breathing
- Plane入口
- Retreat route
- Claim担当の移動能力

が攻略条件になります。

---

# Game開始時に確認する設定

Throne戦略はGame開始時点から始まっています。

確認するもの：

```text
Level 1 Throne数：
Level 2 Throne数：
Level 3 Throne数：
勝利必要Ascension Point：
配置Point合計：
Story Event：
Cataclysm開始Turn：
Diplomacy：Binding / Non-binding / None
Score graph：
MapのPlane構成：
```

## 必要Pointの割合

勝利必要Pointが配置Point総数に対して低いGameでは、Throne rushが早くなります。

逆に必要割合が高いGameでは、

- 複数国家との戦争
- Level 3 Throne確保
- 長期Fort防衛
- Dominion・Cataclysm対応

が重要になります。

## 最初から勝利Setを考える

たとえば勝利に8 Point必要なら、単に「Throneを取る」のではなく、

```text
Level 3 × 2
＋ Level 2 × 1
＝ 8 Point
```

```text
Level 2 × 3
＋ Level 1 × 2
＝ 8 Point
```

のように、どの組み合わせが地理的・軍事的に現実的かを考えます。

---

# Throneの状態

Throneは次の状態を移動します。

```text
未発見
  ↓
Independent・未Claim
  ↓
占領済み・未Claim
  ↓
Claim済み
  ↓
包囲中・Claim維持
  ↓
FortまたはProvinceを敵が征服
  ↓
未Claimへ戻る
  ↓
新所有者が次Turn以降にClaim
```

## Independent・未Claim

Guardianを倒していない状態です。

Pointは誰にも属しません。

## 占領済み・未Claim

ProvinceはPlayerが所有していますが、Pointはまだ得ていません。

この状態を意図的に維持する理由：

- Claim時の悪影響を遅らせる
- 勝利意図を多少隠す
- 同時Claimまで待つ
- Claim担当が到着していない
- Story Eventの準備をする

ただし、Claim-onlyの利益、Dominion spread、Ascension Pointも得られません。

## Claim済み

Ascension PointとClaim-only効果が有効になります。

Dominions 6ではClaim済みThroneがMap上で光るため、他Playerにも重要性が伝わりやすくなります。

## 包囲中

Fort外側を敵が支配しても、Fort内部を自国が維持しているなら、通常Throneはまだ自国のClaim状態です。

このためThrone Fortは、

> **壁が勝利Pointを数Turn保持する施設**

になります。

## 征服され未Claimへ戻る

敵がThrone Provinceを完全に征服すると、そのThroneは通常未Claimへ戻ります。

旧所有者はPointとClaim-only効果を失い、新所有者は次のClaim処理までPointを得ません。

```text
旧所有者：-Throne Level
新所有者：まだ0
次HostでClaim：+Throne Level
```

という時間差があります。

---

# Throne Levelをどう評価するか

Levelは三つの意味を持ちます。

1. Ascension Point
2. Guardianの期待強度
3. Claim効果の期待規模

ただし、Levelだけで攻略難度は決まりません。

## Level 1

Pointは小さいですが、

- 序盤に取りやすい
- Clusterや位置が良い
- 重要Resistance Bless
- 独自Mage recruit
- Ritual range
- 強いDominion spread

を持つ場合があります。

一方、一部Level 1でも強力Mage・特殊Event・危険なGuardianがあります。

## Level 2

Pointと効果のBalanceが良く、Midgameの主要目標になりやすいLevelです。

- Gem income
- Mage recruit
- Scale
- Army-wide Bless効果
- Ritual bonus

など、国家技術を変える効果があります。

## Level 3

3 Pointを一度に得るため勝利計算上非常に大きい一方、

- 強いGuardian
- 大規模な世界効果
- 危険なStory Event
- 外交的Threat
- 多方面からの攻撃

を招きます。

Level 3を早く取ることが常に正解ではありません。

---

# Throne効果の読み方

Throne説明を次の順で読みます。

## 1. Claim前から有効な効果

一部Site効果は、ClaimしていなくてもProvince所有者へ作用します。

例：

- Local income
- Local resource
- Recruitable
- Site固有Event
- 周辺環境への影響

## 2. Claim後だけ有効な効果

`Effects from claimed throne`以降に記載される効果です。

例：

- Ascension Point
- Bless効果
- Dominion spread
- Global Scale
- Gem income
- Ritual range
- Call God bonus
- 国家全体の能力

## 3. Claim時に始まるEvent

ClaimそのものがEvent chainのTriggerになる場合があります。

- 世界規模のScale変化
- Guardian再襲来
- Disease
- Seasonal attack
- Story Event

などです。

## 4. OwnerまたはLocal Provinceだけの効果

「国家全体」と「Throne Provinceだけ」を区別します。

Gold、Resources、Research bonus、Summon、RecruitmentはLocalである場合があります。

## 5. Scale上限

Scale加算ThroneをClaimしても、すでに上限へ達していれば追加利益が出ない場合があります。

複数の正負Scale効果がある場合は相殺関係も確認します。

---

# Throneを発見する

## Hidden Map

Dominions 6ではMapが最初から完全には見えません。

Throneの位置、Terrain、接続、周辺Playerを早期に把握するため、Scout networkが必要です。

## Scout

確認するもの：

- Guardian総数
- Commander数
- Mage・Priest
- Giant・Monster
- Undead・Demon・Magic Being
- Archer・Crossbow
- Cavalry・Trample
- Fortの有無
- 隣接Province
- Rival到達Turn

Scout reportは概算であり、Stealth、Glamour、Fort内部、同Turn増援は完全には見えません。

## Scrying

Remote Scryは、

- 高価なScoutを失わない
- 遠隔地を確認する
- Player-held ThroneのArmyを更新する
- Magic Phase防衛を調べる

ために使います。

## Battle ping

安価なCommanderを送り、Battleを発生させます。

目的：

- MageのSpell
- Battlefield Enchantment
- Gem使用
- Formation
- Squad order
- Morale
- Damage type
- Resistances

を知ることです。

### Pingの重要な制限

Guardian MageのGemは次のBattleで補充されます。

したがって、

```text
Ping 1：大Spellを使わせる
Ping 2：Gem切れを期待
本隊：安全に攻撃
```

という計画は成立しません。

### Ping担当のScript

```text
Hold
Hold
Hold
Hold
Retreat
```

などで情報を取りますが、

- Fast enemy
- Flying
- Long-range spell
- Battlefield wipe
- Retreat routeなし

では逃げる前に死亡します。

---

# Guardianを分析する

Throne Guardianを兵数だけで評価しません。

## 分析順

1. CommanderとMage
2. Battlefield condition
3. 主Damage type
4. Protection・Defence・MR
5. Elemental Resistance
6. Size・Trample
7. Awe・Fear・Repel
8. Summon
9. Morale・Mindless
10. RetreatとTimer

## Generic Mage

GenericなThrone Mageは、専用のSpell候補からCastする場合があります。

Pathだけを見て、全Research Schoolの最適Spellを使うとは限りません。

## Unique Mage・Titan

固有Mage・Titan等は、Research capの範囲内で広いSpellを使うことがあります。

Scout reportだけではResearch capやGemを完全に判断できないため、Battle Replayと固定データを併用します。

## Guardianが強い典型

- Battlefield Enchantmentを持つ
- 高Path Mageが複数
- Undead・Demon＋Priest
- Giant＋Trample
- Awe＋高Morale Sacred
- 高Protection＋Elemental Resistance
- Long-range AoE
- Flying rear attack
- MindlessでMorale戦が効かない

## Counterを一文で書く

```text
Shield screenで射撃を受け、Shock Resistance後に高Damage兵で前衛を処理し、Flying部隊でMageを止める
```

のように、

> **誰が何を受け、誰が何を倒すか**

を一文にします。

詳しい戦闘分析は、[戦闘ルール](../basics/combat-rules.md)と[命令・Battle Script](../basics/orders.md)を参照してください。

---

# Independent Throne攻略

## 攻撃前Checklist

```text
Throne Level：
Guardian数：
Mage / Priest：
確認済Spell：
Battlefield Enchantment：
主Damage type：
必要Resistance：
Protection / Defence / MR：
Screen：
Damage役：
Mage script：
Gem予算：
Retreat route：
Claim担当の位置：
Rival最短到達Turn：
```

## Armyを二つに分ける

### Guardianを倒すArmy

- Screen
- Damage
- Resistance
- Mage control
- Commander redundancy
- Retreat route

が必要です。

### Claimを守るArmy

Guardian撃破後、主力が別Frontへ移動しても、

- Claim担当
- Assassin対策
- Magic Phase raid対策
- 最低限のPD
- Fort builder

を守る必要があります。

Guardian攻略に勝って全軍が瀕死になると、次Turnに隣国がThroneを奪います。

## 攻略後の最初のTurn

優先順位：

1. SurvivorとAffliction確認
2. Claim担当を確認
3. Enemy到達Turnを再計算
4. PD購入
5. Fort builder
6. Temple / Lab計画
7. Site説明を読む
8. Claim悪影響を確認
9. Claimするか待つか決める

---

# Player-held Throne攻略

Player-held Throneは、Guardian攻略と異なります。

- Scriptが更新される
- Gemが補給される
- Relief Armyが来る
- Magic Phase攻撃がある
- Fortがある
- Dome・Patrol・Assassinがいる
- 他国も勝利阻止へ参加する

からです。

## Unforted Throne

Field Battleに勝てばProvinceを奪い、旧Claimを解除できます。

ただしClaim Phaseはすでに終わっているため、新所有者がPointを得るのは通常次Hostです。

```text
Turn A：攻撃Order
Host A：Field Battle勝利、旧Claim解除
Turn B：Claim Order
Host B：Claim処理、Victory check
```

## Forted Throne

外側のField Battleに勝っても、Fort内を取る必要があります。

```text
外側を取る
→ Siege
→ Wall 0
→ Storm
→ Fort capture・旧Claim解除
→ 次TurnにClaim
```

Forted Throneは、Pointを数Turn維持する防御施設です。

詳しくは [Fort・Siege・Storm](forts.md) を参照してください。

---

# ClaimできるCommander

## Pretender God

PretenderはHoly level表示にかかわらずThroneをClaimできます。

利点：

- Claim条件を常に満たす
- Combat能力
- Dominion spread
- Magic Phase movementを持つ場合がある

Risk：

- Assassin
- Magic Duel等の特殊Counter
- Enemy Dominion
- Claim中に別の国家役割を行えない
- 死亡でIncarnate Bless・Magic accessを失う

## Disciple

Disciple GameではDiscipleもClaimできます。

Team内で、Pretenderを後方に残し、Discipleを前線Claim担当にすることができます。

## H3以上のPriest

Prophetは代表的なH3です。

他にも、

- National High Priest
- Summoned Priest
- Holy Boosterを持つPriest
- Site recruit
- 特殊変身・Event Commander

がH3へ到達する場合があります。

## Prophetの注意

Prophet宣言はTurn処理Step 16で、Claim ThroneはStep 8です。

したがって、

```text
Become Prophet
＋
同じHostでClaim
```

はできません。

Prophetになった次TurnからClaimします。

## Affliction・Path loss

ProphetやHigh PriestがAffliction等でHoly levelを失い、H2以下になっている場合、Claimできないことがあります。

名前や過去の役割ではなく、現在のPath表示を確認します。

---

# Claim Order

Claim担当を選択し、`Claim Throne of Ascension`を指定します。

## Claim Orderが表示される基本条件

- CommanderがPretender、Disciple、またはH3以上
- Claim可能なThrone Provinceにいる
- 自国がProvinceと必要なFort内部を支配
- Commanderが別Orderへ固定されていない
- Throneが自国によって未Claim

特殊状態・Insanity・Event・Modでは例外があります。

## ClaimはCommanderの一Turnを使う

Claim担当は同じTurnに、

- Movement
- Research
- Forge
- Ritual
- Preach
- Call God
- Patrol

を同時に行いません。

H3が国家唯一の重要Priestである場合、Claimに一Turn使うOpportunity Costも計算します。

---

# ClaimのTurn処理順

主要な順序：

```text
Step 2  Research
Step 4  Recruitment
Step 6  Preach
Step 8  Claim Throne
Step 10 Ritual
Step 16 Become Prophet
Step 21 Assassination
Step 24–25 Movement
Step 26 Main Battle
Step 27 Fort Storm
Step 43 Dominion spread
Step 57 Victory check
```

## Claim担当は事前配置が必要

ClaimはMovementより前なので、

- 通常Movement
- Flying movement
- Sailing
- Teleport
- Cloud Trapeze
- Gateway

で同Turnに到着してClaimすることはできません。

前Turnの終了時点で、Claim担当がThroneにいる必要があります。

## Teleport Claimは二段階

```text
Turn A：Magic MovementでThroneへ到着
Host A：必要ならBattle
Turn B：Claim Order
Host B：Claim
```

です。

Magic Phase mobilityはClaim担当の移送を速めますが、Claim Phaseそのものを後ろへ移しません。

## Recruitして即Claimできない

RecruitmentはClaimより前ですが、新RecruitにはTurn提出時点でOrderを出せません。

新しく雇ったH3は、次TurnからClaim担当になります。

## Awakeして即Claimできない

Dormant / Imprisoned PretenderのAwakeningはClaim Phaseより後です。

出現したHostで直ちにClaim Orderを実行することはできず、次Turnからです。

## Empowerして即Claimできない

Empowerment処理はClaimより前ですが、EmpowermentとClaimはどちらもCommander Orderです。

同じCommanderが一Turnで両方を行うことはできません。

---

# ClaimとAssassination

重要な前後関係です。

```text
Claim：Step 8
Assassination：Step 21
```

Claim Orderが有効に処理された後、同じHostでClaim担当がAssassinationされても、Claimそのものはすでに成立している可能性があります。

したがって、勝利直前のClaimを止めるために、

> **Claim HostでClaimantをAssassinateする**

だけでは遅い場合があります。

## Claimを止める方法

- 前TurnまでにClaimantを倒す
- ClaimantをThroneへ到着させない
- Throne Provinceを先に奪う
- Claim Hostの後半に別のClaim済みThroneを奪う
- FortをStormしてPointを落とす
- Claim Orderが出せない状態を事前に作る

Assassinationは次Turn以降の保持、Prophet喪失、Dominion防衛には有効ですが、処理順を理解して使います。

---

# Claimで何が同Turnに変わるか

ClaimはTurn序盤に成立します。

その後に評価される、

- Main Battle
- Income
- Dominion spread
- Victory condition

へClaim済み状態が影響する可能性があります。

## Battle

Bless・国家全体のStat・Dominion関連効果など、Claim後ただちに有効になる効果は、後続Battleへ影響し得ます。

ただし特殊EventやScale変化は、Event Phaseまたは後続Turnで発生する場合があります。

## Income

Income処理はClaimより後です。

Gem・Gold等の効果が同Hostから計上されるかは、Site効果の種類と特殊Eventを確認します。

## Dominion spread

Claimed ThroneのTemple checkは、後半のDominion spread時に作用します。

一般にLevel 1 / 2 / 3は、それぞれ1 / 2 / 3回のDominion spreadを持ちますが、より強い例外Throneがあります。

> `Spreads Dominion (x)`は、毎Turn必ずx Candle増える、という意味ではなく、x回のSpread checkを発生させる意味です。

## Victory

ClaimでPointは有効になりますが、最終Victory checkはStep 57です。

---

# Ascension Pointの計算

勝利Hostを次の式で考えます。

```text
Host開始時のClaim済みPoint
＋ Step 8で新しくClaimしたPoint
－ Host後半で失ったClaim済みPoint
＝ Step 57で判定されるPoint
```

## 例

```text
Host開始：6 / 8
Level 2 ThroneをClaim：+2
別のLevel 1 Throneを敵が奪う：-1
Victory check：7 / 8
```

Claim直後は8 Pointでも、最終的には勝利していません。

## Victory margin

勝利作戦では、

```text
Claim後Point
－ 勝利必要Point
```

だけでなく、同Hostに失う可能性のあるPointを引きます。

```text
安全Point
＝ Claim後Point
－ 失陥予想Point
```

安全Pointが必要値以上か確認します。

---

# Claim済みThroneを失う

## Fortなし

敵がField Battleに勝ちProvinceを奪うと、Claimが解除されます。

旧所有者は同HostのVictory check前にPointを失います。

## Fortあり

敵が外側を取っただけでは、Fort内部とClaimを維持することがあります。

敵は、

1. Field Battle
2. Siege
3. Wall破壊
4. Storm
5. Fort capture

まで進める必要があります。

## 新所有者は即Pointを得ない

Fortを取ったHostではClaim Phaseがすでに終わっています。

新所有者は通常、次TurnにClaim Orderを出します。

## Point swing

Level 3 Throneを敵から奪い、次TurnClaimすると、最終的には、

```text
敵：-3
自国：+3
合計差：6 Point
```

のSwingになります。

ただしFort capture Hostでは、まず敵の-3だけが起こり、自国の+3は次Hostです。

---

# Forted Throne攻略の標準Timeline

最短の典型例です。

## Turn T+0：侵攻

Order：

```text
主力Army：Throne FortへMove
Siege Unit：同行
Claim担当：同行または安全な近隣へ
```

Host：

- 外側のField Battle
- Siege開始
- Siege damage

## Turn T+1：壁を0へ

Wallがまだ残る場合、Siegeを継続します。

一Turn crackが可能なら、このHost後にWall 0になります。

Order：

- Relief Army対策
- Storm用Gem温存
- Claim担当をFort上へ確実に置く

## Turn T+2：Storm

Order：

```text
Storm Army：Storm Castle
Claim担当：Storm後に生存する位置
外部Army：Relief迎撃
```

Host：

- 外側のField Battle
- Fort Storm
- 勝てば旧Claim解除

## Turn T+3：Claim

Order：

```text
H3 / Pretender / Disciple：Claim Throne
```

Host：

- Step 8 Claim
- 後半の反撃を処理
- Step 57 Victory check

Wall、Relief、Storm結果により一Turn以上ずれます。

---

# Unforted Throne攻略の標準Timeline

## Turn T+0

Armyが攻撃します。

Hostで勝てばProvinceを占領します。

## Turn T+1

すでにThroneにいるClaim担当がClaim Orderを出します。

Host終盤まで保持すればPointになります。

> **Unfortedでも「攻撃とClaim」は通常別Turnです。**

---

# Claim担当をStormへどう同行させるか

## 主力Commanderにする

H3がArmy Commanderを兼ねる方法です。

Risk：

- Gate戦で死亡
- Rout
- Fatigue
- Assassin
- Leadership崩壊

## 後衛へ置く

BodyguardとRear guardを付け、Storm戦を生き残らせます。

## Storm後にMagic Movementで入れる

Storm勝利Hostの後、次TurnのClaimまでにMagic Movementで到着させる方法があります。

ただしMagic Movement到着HostでClaimはできないため、さらに一Turn遅れる場合があります。

## Claim専用H3を複数準備

複数Throne rushでは、ArmyよりClaim担当がBottleneckになることがあります。

```text
攻撃Army 3個
Claim可能者 1人
```

では、同時に3ThroneをClaimできません。

---

# Throne rush

Throne rushは、勝利に必要な複数Throneを短期間で奪い、他Playerが対応する前にClaimする作戦です。

## 必要な七要素

1. 正確なPoint計算
2. 最新のScout情報
3. 複数の攻略Army
4. Siege Strength
5. Claim可能者
6. 自国既存Throneの防衛
7. 同一HostのTiming管理

## Target選択

各Throneを次で評価します。

```text
獲得Point
＋ 敵から奪うPoint
＋ Throne効果
＋ Strategic position
－ 攻略損失
－ 必要Siege Turn
－ ClaimまでのTurn
－ 敵救援Risk
－ 外交Threat
```

## 取る優先度

### 自国所有・未Claim

最も速いPointです。

Claim担当を事前配置し、複数を同HostにClaimできます。

### Independent・Fortなし

Guardianを倒す必要がありますが、Player reliefがありません。

### Enemy・Fortなし

Field Battle一回で敵Pointを落とせます。

### Enemy・Fortあり・Wall 0

Storm成功後、次TurnClaimできます。

### Enemy・健全なFort

Siege Turnが必要で、全世界に意図が伝わります。

## 同時Claim

複数の自国ThroneへClaim担当を事前配置し、同じHostでClaimします。

利点：

- 勝利意図を見せる期間が短い
- Claim effectを同時に得る
- 対応先を分散

必要：

- ThroneごとにClaim担当
- すべてのClaimantが前Turnから現地
- 全Throneを同Host終盤まで保持

## 同時攻撃

複数のEnemy Throneを攻撃し、防衛側を分散させます。

ただし、CaptureとClaimは別Turnなので、

> 同時に取るArmy

だけでなく、

> 次Turnに同時にClaimするH3

まで計画します。

---

# 勝利Hostの設計

勝利Hostでは、すべての戦域を一つの処理順で見ます。

## Step 8：新Claim

どのThroneで何Point増えるか。

## Step 10–27：敵の反撃

- Remote ritual
- Magic Phase attack
- Assassination
- Normal movement
- Field Battle
- Fort Storm

でどの既存Throneを失うか。

## Step 54：Fort奪回

Besiegerが消え、Fort側が外部Province controlを戻す可能性があります。

## Step 57：Victory check

最終的に残ったClaim済みPointで判定します。

## Victory Host Checklist

```text
Host開始Point：
Step 8 Claim予定：
Claim後Point：
敵が一Turnで取れるUnforted Throne：
敵が一TurnでStormできるThrone：
Magic Phase threat：
Assassin threat：
各ThroneのFort / Wall：
Mobile reserve：
予想失陥Point：
Step 57予想Point：
```

---

# Throne rushを止める

相手が必要Pointへ届きそうな場合、狙われているThroneだけを守る必要はありません。

> **相手のClaim済みThroneをどれか一つ落とし、Step 57のPointを不足させる**

ことでも勝利を止められます。

## 防御の優先順位

1. 相手の現在Pointを数える
2. Claim可能な未Claim Throneを探す
3. Claimantの事前配置を探す
4. 自国の危険Throneを守る
5. 相手の最も弱い既存Throneを攻撃
6. 一Turn crack可能なFortを探す
7. H3・Pretenderを狙う

## Claimant暗殺のTiming

Claim HostのAssassinationはClaim後です。

Claimを止めるには、前Turnに倒す、移動を妨害する、または後半にPointそのものを奪います。

## One-turn unclaim

Unforted ThroneまたはWall 0のFortを同Hostに奪えれば、相手が新ThroneをClaimしてもVictory check前にPointを減らせます。

## Claimantを孤立させる

- Retreat routeを切る
- Bodyguardを消す
- Fortを包囲
- Labを破壊
- Magic Phase移動を監視
- Prophetを前TurnにAssassinate

ことで次のClaimを遅らせます。

## Point denialだけでよい場合

相手のLevel 3 Throneを奪ったHostで、自国がまだClaimできなくても、相手はすでに3 Point失っています。

勝利阻止が目的なら、即ClaimよりCaptureを優先する場合があります。

---

# Throne防衛

Throne防衛は五層で考えます。

## 1. Information

- Scout ring
- Spy
- Scrying
- Enemy Army arrow
- Gem・Mage監視
- Diplomacy

最も安い防御は、敵の準備を一Turn早く知ることです。

## 2. Province exterior

- PD
- Patrol
- Anti-raider
- Mobile reserve
- Choke control

Fortに入る前の敵を止めます。

## 3. Fort wall

- Wall Integrity
- Castle Defence
- Repair unit
- Relief timing
- Supply Storage

Pointを数Turn保持します。

## 4. Storm defence

- Gate blocker
- High Morale
- Pike・Repel
- AoE
- Resistance
- Wall defender
- Multiple Commander
- Battlefield Enchantment

## 5. Claim・宗教・特殊攻撃防御

- Claimant Bodyguard
- Anti-assassination
- Dome
- Patrol
- Temple
- Preach
- Magic Phase reserve
- Dominion

Fortだけで、Assassin、Teleport、Dominion kill、Remote ritualを防げるわけではありません。

---

# ThroneへFortを建てる

## Fortの最大価値

Claim済みThroneのFortは、

> **StormされるまでAscension Pointを保持する**

ことです。

通常Province Fort以上に、壁一Turnの価値が大きくなります。

## 建設Timing

通常のFort完成はBattleより後です。

完成予定Turnに敵が侵攻すれば、Fort完成前にField Battleが起きます。

したがって、Guardian撃破直後の建設期間が最も危険です。

## Fortと一緒に建てるもの

### Temple

- Dominion spread
- Preach
- Priest・Sacred recruitment
- Claimant支援
- Enemy Dominion対策

### Laboratory

- Gem補給
- Item交換
- Battle Mage
- Ritual defence
- Magic Phase移動
- Dome

### Scout ring

Fortがあっても、一Turn crack＋次TurnStormを見逃せば遅れます。

## Fort内部へ全軍を詰めない

Fort内部だけに戦力を集中すると、

- Supply不足
- Disease
- 外側のProvince control喪失
- Relief不在
- Retreat不能

が起こります。

近隣にMobile reserveを置きます。

---

# DominionとThrone

Claimed ThroneはDominion sourceです。

一般に、

- Level 1：1 check
- Level 2：2 checks
- Level 3：3 checks

を発生させますが、より強い例外があります。

## Friendly DominionでClaimする必要はあるか

通常、Claim資格はPretender・Disciple・H3とProvince controlで決まり、Hostile Dominionであること自体はClaimを禁止しません。

ただしHostile Dominionでは、

- Pretender・Disciple・Prophetの能力低下
- Army Morale
- Enemy national effect
- Scales
- Incarnate Bless運用

が不利になります。

## Storm前のPreach

PreachはClaimやBattleより前です。

Throne FortをStormするTurnにPreachできれば、

- Defender Pretenderを弱める
- 自軍Prophetを強める
- Army Moraleを改善
- Enemy Dominion effectを弱める

可能性があります。

詳しくは [Dominion・Scales・宗教戦](dominion.md) を参照してください。

---

# Throne Effectを国家戦略へ使う

## Gem・Blood income

新PathのGem incomeは、

- Booster
- Summon Mage
- Resistance Item
- Global
- Empowerment

の入口になります。

## Bless効果

Throne BlessはSacred Armyだけでなく、

- Sacred Mage
- Prophet
- Pretender
- Sacred Summon

へ長期的に影響します。

Claim後、現在のBless表示と実戦Statsを確認します。

## Mage・Unit recruitment

Throne recruitは国家にないPathや能力を開く場合があります。

Fort・Lab・Commander Point・Recruitment条件を確認します。

## Ritual range

特定PathのRitual rangeが伸びるThroneは、

- Remote attack
- Site Search
- Teleport network
- Global支援

の戦略距離を変えます。

## Forge・Research・Ritual bonus

Local bonusの場合、MageをThrone Provinceへ置く必要があります。

安全性、Lab、Assassin、Dome、Fortを整えます。

## Scale

自国に有利なScaleだけでなく、世界またはLocalに悪影響を与えるThroneがあります。

Point urgencyと長期Costを比較します。

---

# Claimを遅らせる判断

占領後すぐClaimしない方がよい場合があります。

- Claimで危険なEventが始まる
- Negative Scaleが長期経済を壊す
- 同時Claimまで勝利意図を隠したい
- Claimantを安全に守れない
- 外交Coalitionを避けたい
- 特殊Throneの事前Eventを完了したい

一方、遅らせるCost：

- Ascension Pointなし
- Claim-only Gem・Blessなし
- Dominion spreadなし
- 敵に奪われるRisk
- Claimant turnを後で必要

です。

## 即Claimが正しい場合

- Claimで勝利する
- 効果がFirst warへ間に合う
- Rivalが次Turnに奪える
- Dominion kill防衛に必要
- H3がすぐ別Frontへ移動する

---

# DiplomacyとThreat

Throneは軍事資産であると同時に、外交情報です。

## ClaimでThreatが上がる理由

- Score上のAscension Point
- Map上のClaim表示
- 強いBless・Scale効果
- 勝利までの残りPoint減少
- Fort化
- H3移動

が他Playerへ伝わります。

## Early Claim

効果を長く利用できますが、早期Coalitionの標的になります。

## Delayed Claim

勝利意図を隠しやすい一方、効果とPointを捨てています。

## Formal diplomacy

Binding NAPがあるGameでも、

- NAP期限
- Throne例外
- Victory clause
- Team協定

を確認します。

相手が勝利直前なら、通常の国境合意よりVictory denialが優先されることがあります。

---

# Disciple Game

Disciple Gameでは、TeamでAscension Pointを共有します。

Claim可能者：

- Team Pretender
- 各Disciple
- H3以上のPriest

## 役割分担

### Claim担当

DiscipleやHigh Priestを各Frontへ事前配置します。

### Guardian攻略

Armyの強いTeam memberが担当します。

### Siege

Earth・Giant・Summonに強い国家が壁を破ります。

### Magic Phase

Air・Astral・Glamour等の国家が同時Throne攻撃・防衛を担当します。

### Fort化

Gold・Mason・Castle Defenceを持つ国家が守備を整えます。

## Team Temple・Dominion

Team DominionとThrone spreadは、通常Gameとは異なるTemple breakpointや国家固有效果があります。

詳しくは [Disciple Game](disciple-game.md) を参照してください。

## Teamの失敗

- Claim可能者を一人に集中
- 誰がFort費用を払うか未決定
- GemをStorm Armyへ渡していない
- Team内でVictory Pointを数えていない
- DiscipleがClaimではなく別Order
- Teamの既存Throne防衛を忘れる

---

# Cataclysm

Cataclysm設定は、Gameへ終盤の時間制限を与えます。

Dominions 6ではCataclysmへの対抗が以前より難しくなっています。

正確なEvent内容と進行はGame設定・Version・Messageで確認してください。

戦略上は、

> **Cataclysm開始Turnから逆算し、研究・Fort・Global・Throne rushのどれが間に合うかを再評価する**

ことが重要です。

## Cataclysm前の再計算

```text
残りTurn：
現在Point：
不足Point：
未Claim自国Throne：
攻略可能Independent Throne：
敵Forted Throne：
一Turn crack能力：
Claim可能者：
Fort建設完了Turn：
必要Research完成Turn：
```

## よくある誤り

- Cataclysm開始後も通常の長期経済計画を続ける
- Level 3 Throneを取らずGlobalだけ増やす
- Claim担当を用意していない
- Fort建設が完成前にGame局面が変わる
- 既存Throneを静的守備だけに任せる

---

# 実戦例

## 例1：Independent Level 1を攻略

### Turn A

Guardianを倒してProvinceを占領します。

Claim Phaseはすでに終わっています。

### Turn B

現地のProphetがClaimします。

Host終盤まで保持すれば1 Pointを得ます。

---

## 例2：Level 1ならH1でClaimできると思った

### 状況

- Level 1 Throne
- H1 Priest
- Claim Orderが表示されない

### 原因

Throne Levelにかかわらず、通常はH3が必要です。

### 対応

- Prophetを送る
- Pretenderを送る
- H3 recruit・summonを使う
- H2をBoosterでH3へ上げる

---

## 例3：Become ProphetとClaimを同時に指定したい

Prophet宣言はClaimより後に処理されます。

```text
Turn A：Become Prophet
Host A：Prophet成立
Turn B：Claim
```

とします。

---

## 例4：TeleportしたH3がClaimできない

ClaimはRitual・Magic Movementより前です。

```text
Turn A：Teleport
Host A：到着
Turn B：Claim
```

が必要です。

---

## 例5：8 Pointへ到達したのに勝てない

### 状況

- Host開始6 Point
- Level 2をClaimして8 Point
- 同じHostで敵が自国Level 1を奪う

### Victory check

```text
6 + 2 - 1 = 7
```

必要8 Pointに届きません。

Claim画面だけでなく、全ThroneのHost後状態を見ます。

---

## 例6：Claimantを同HostにAssassinateしたが敵が勝利

ClaimはAssassinationより先です。

Claimant死亡時点ではClaimが成立済みでした。

勝利を止めるには、

- 前Turnに倒す
- 別のClaim済みThroneを奪う
- Claim対象を同Host後半に征服する

必要があります。

---

## 例7：PingでGuardianのGemを枯らす

Guardian Mageは次BattleでGemを補充します。

PingはSpell・Script確認には成功しましたが、Gem burnにはなっていません。

本隊は同じ大Spellを再び受ける前提で組みます。

---

## 例8：Fort外側を取ったので敵Pointが減ったと思った

EnemyがFort内部を保持しているなら、ThroneはまだClaim済みの可能性があります。

Wallを破り、StormしてFortを取る必要があります。

---

## 例9：特殊Throneを即Claimして世界Eventが始まる

Throne説明のClaim Eventを読まず、長期のDisease・Unrest・Attackを発生させました。

Pointが勝利に必要でない場合は、事前Event、対策Mage、Season、外交影響を確認してからClaimします。

---

## 例10：三つのThroneを同時攻略したがClaimは一つだけ

Armyは三個ありましたが、Claim可能者がProphet一人だけでした。

次回は、攻撃Armyと同じ数のH3・Disciple・Pretender accessを事前に準備します。

---

# 症状から原因を探す

| 症状 | 最初に疑うもの |
|---|---|
| Claim Orderが表示されない | H3未満、Pretender/Discipleでない、Throne control不足 |
| Level 1をH1がClaimできない | 全Level共通でH3必要 |
| ProphetにしたTurnにClaimできない | Become ProphetはClaimより後 |
| Teleport到着TurnにClaimできない | ClaimはMagic Movementより前 |
| Captured ThroneからPointを得られない | まだ未Claim |
| Claimしたのに勝利しない | 必要Point、同HostのThrone喪失、Team設定 |
| Enemy Fortを包囲したがPointが減らない | Fort内部が未征服 |
| Storm勝利直後にClaimできない | Claim PhaseはStormより前 |
| ClaimantをAssassinateしたのにClaimされた | ClaimがAssassinationより先 |
| Guardian Mageが同じ大Spellを再使用 | BattleごとにGem補充 |
| Throne効果が出ない | Claim-only、Local限定、Event条件、Scale上限 |
| Claim後に悪いEventが始まる | Story Event・Claim Trigger |
| Throneを奪ったのに自国Pointが増えない | 敵Point消失と自国Claimは別Host |
| 勝利直前にPointが落ちる | 別Throneが同Hostに征服された |
| Claimed Throneが光って目立つ | Dom6のClaim表示 |
| Sacred生産が変わった | Throne Bless、Dominion、Holy Points |
| 前線Dominionが急に強くなる | Claimed ThroneのSpread checks |

---

# よくある誤解

## 「Levelが高いほど必要Holy levelも高い」

誤りです。通常はすべてH3です。

## 「Provinceを取ればPointが入る」

Claimが必要です。

## 「攻撃して勝った同TurnにClaimできる」

Claim PhaseがBattleより前なので、通常は次Turnです。

## 「TeleportでH3を送り、そのままClaimできる」

Magic MovementもClaimより後です。

## 「Claimした瞬間に勝利が確定する」

Victory checkはTurn終盤です。

## 「Claimantを同Hostで暗殺すれば止まる」

AssassinationはClaimより後です。別Throneを奪う等の対策が必要です。

## 「Fortを包囲すればEnemy Pointは消える」

Fort内部を保持されている限り、Pointが残ることがあります。

## 「PingでGemを枯らせる」

Independent Guardian MageはGemを補充します。

## 「Throne効果はすべて良い」

Globalな悪影響やStory Eventを持つThroneがあります。

## 「Fortを建てれば安全」

One-turn crack、Magic Phase、Assassin、Dominion、Relief阻止があります。

## 「Armyが多ければThrone rushできる」

Siege StrengthとClaim可能者が必要です。

## 「早くClaimするほど必ず得」

Point・効果と、外交Threat・Negative Eventを比較します。

---

# Throne攻略Template

```text
Throne名：
Level / Point：
Terrain / Plane：
Cluster：
現在Owner：Independent / Player
Claim状態：Unclaimed / Claimed
Fort：
Wall：
Guardian / Defender：
Mage / Priest：
確認済Spell：
主Damage：
Protection / Defence / MR：
必要Resistance：
Battlefield condition：
Attack Army：
Siege Strength：
Storm Army：
Claim担当：
Claim担当の到着Turn：
最短Capture Turn：
最短Claim Turn：
Enemy Relief Turn：
Claim effect：
Negative effect / Event：
Fort計画：
Step 57予想Point：
```

---

# Game全体のPoint表

```text
勝利必要Point：

自国Claim済み：
- Throne A：Level / Fort / Wall
- Throne B：Level / Fort / Wall

自国未Claim：
- Throne C：Level / Claimant

Enemy Claim済み：
- Nation X / Throne D：Level / Fort / Wall
- Nation Y / Throne E：Level / Fort / Wall

Independent：
- Throne F：Level / Guardian / 距離

このHostの新Claim：
このHostの失陥予想：
Step 57予想Point：
```

---

# Throne防衛Checklist

```text
Claim状態：
Fort / Wall：
Castle Defence：
Supply：
Gate defence：
Temple / Dominion：
Lab / Dome：
PD / Patrol：
Claimant / H3：
Bodyguard：
Scout ring：
Magic Phase threat：
One-turn crack threat：
Enemy Storm Army：
Nearest relief Army：
Retreat route：
このThroneを失った後のPoint：
```

---

# Throne rush Checklist

```text
現在Point：
必要Point：
不足Point：
Target set：
各TargetのCapture Turn：
各TargetのClaim Turn：
Claim可能者数：
Siege Army数：
Storm Army数：
Magic Phase部隊：
Gem予算：
既存Throne防衛：
敵が同Hostに奪える自国Throne：
Claim後予想Point：
失陥後予想Point：
外交反応：
Fallback：
```

---

# Battle Replayで確認するもの

Guardian・Storm・Relief戦後に確認します。

1. 最初に計画が崩れたRound
2. Guardian MageのSpell順
3. Battlefield Enchantment caster
4. Gem使用
5. Screenの接敵Timing
6. Gateの詰まり
7. Friendly Fire
8. Claim担当の生存位置
9. Commander死亡とRout
10. Retreat route
11. 次のRelief戦に残るGem
12. Storm後にClaim可能者が現地に残ったか

詳しくは [Battle Replayの読み方](../getting-started/battle-replay.md)を参照してください。

---

# 追加検証が必要な項目

次は特殊条件が多く、個別Testを必要とします。

- Automatic claim Eventの全条件と処理Timing
- 複数国家が同Hostに特殊EventでClaimする場合
- Claim直後の全Throne固有效果の発動Phase
- Siege中の特殊Site・Recruit・Event
- Modで変更されたAscension Point
- Cross-plane Dominion spread
- Story Eventを無効にした特殊Throne
- Cataclysmの全段階と対抗手段
- Insanity・Shattered Soulによる自動Claim
- Fort capture・Fort奪回・Victory checkの特殊同時処理
- Disciple Gameでの特殊Throne・国家効果継承
- AIによるClaim判断

不明点は推測で埋めず、Version、Save、Game設定、Turn、Messageを記録します。

---

## 関連ページ

- [Throneデータ一覧](../data/sites/thrones.md)
- [Magic Siteデータ](../data/sites/index.md)
- [Province](province.md)
- [Fort・Siege・Storm](forts.md)
- [Dominion・Scales・宗教戦](dominion.md)
- [ターン処理順](../reference/turn-resolution.md)
- [命令とBattle Script](../basics/orders.md)
- [戦闘ルール](../basics/combat-rules.md)
- [最初の戦争](../getting-started/first-war.md)
- [Battle Replayの読み方](../getting-started/battle-replay.md)
- [Pretender God](../pretender/index.md)
- [Holy](../magic/paths/holy.md)
- [Magic Path Booster](../items/boosters.md)
- [Disciple Game](disciple-game.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
- [Dominions 6.35固定Throneデータ](../data/sites/thrones.md)
- [Illwiki: Thrones of Ascension](https://illwiki.com/dom5/thrones)
- [Illwiki: Owl's Mini-Guide to Throne Rushes](https://illwiki.com/dom5/owl-mini-guide-thronerush)
