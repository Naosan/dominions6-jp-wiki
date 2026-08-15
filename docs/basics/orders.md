---
title: 命令とBattle Script
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# 命令とBattle Script

Dominions 6の戦闘では、戦闘開始後にUnitを直接操作できません。

プレイヤーが作るのは、リアルタイムの指示ではなく、戦闘前の**行動計画**です。

> **偵察 × 初期配置 × Squad編成 × Formation × 部隊命令 × Commander Script × Gem × 退路**

が一つのBattle Scriptになります。

このページの目的は、個々の命令を暗記することではありません。

> **誰が、何Roundまで時間を作り、誰が、どの敵へ、何を通して勝つか**

を設計できるようにすることです。

!!! note "このページの精度範囲"
    本文はDominions 6.35を対象に、現行UIで使う命令、公式に示されたDom6の戦場・AI変更、ゲーム内Tooltip、Battle Replayで確認できる挙動を、実戦向けに整理しています。命令は標的選択の優先や行動方針を与えるもので、特定Unitへの到達やSpellの発動を絶対保証するものではありません。Obstacle、Range、Casting time、Target、Fatigue、Routなどによって結果は変化します。

---

## 最初に覚える四つ

### 1. 命令は保証ではなく優先方針

`Attack Rear`を選んでも、必ず敵Mageへ到達するわけではありません。

- 経路上の敵
- Obstacle
- Combat Speed
- 敵後衛の位置
- 前衛との接触
- 新しい標的
- Rout

によって途中で捕まったり、別の敵へ向かったりします。

同様に、ScriptしたSpellも、

- 有効Targetがいない
- Range外
- Path不足
- Gem不足
- 戦場条件不成立
- CasterがInterrupt・Stun・Rout・死亡

なら、予定どおりには発動しません。

### 2. 配置は最初の命令

Squadを何命令にするかより前に、

- どこへ置くか
- 誰を前へ置くか
- 誰を後から接敵させるか
- 左右のどちらを守るか
- Mageまで何Squareあるか

を決めます。

位置が悪ければ、正しい命令でも正しいTimingになりません。

### 3. Script後のMain Orderまで設計する

Commanderは通常、最大5枠の行動を上から順に試した後、設定したMain Orderへ移ります。

```text
Round 1：Self boost
Round 2：Resistance
Round 3：Army buff
Round 4：Control
Round 5：Main spell
その後：Cast Spells / Stay Behind Troops / Attack / Retreat 等
```

最初の5枠だけでなく、**6Round目以降に何をするか**が重要です。

MageがScript終了後に前進して死亡する、不要なGem Spellを使う、Friendly Fireの大きいSpellを連打する、といった事故はMain Orderから起こります。

### 4. Scriptは仮説

良いScriptは、見た目が複雑なScriptではありません。

```text
敵はRound 3に接敵する
→ Round 2までにShock Resistanceを入れる
→ Shield前衛がChargeを受ける
→ Damage役はHoldして後から入る
→ MageはRound 4からControlへ移る
```

のように、因果関係を説明できるScriptです。

Battle Replayで仮説と現実を比較し、次の戦闘では一つだけ変更します。

---

# 戦闘前に決める十項目

命令画面を開く前に、次へ答えます。

1. **戦闘目的**：敵主力撃破、Fort到達、Scout、Gem burn、退却のどれか
2. **敵の主なDamage源**：物理、Shock、Poison、MR、Fatigue等
3. **誰が最初に受けるか**
4. **何が敵を倒すか**
5. **どの敵を優先して倒すか**
6. **接敵は何Round目か**
7. **どのBuff・Battlefield Spellを接敵前に通すか**
8. **誰がMageとCommanderを守るか**
9. **何Gemまで使ってよいか**
10. **Rout・RetreatしたUnitがどこへ逃げるか**

一つでも答えがない場合、その部分をAIと偶然へ任せています。

---

# Battle Scriptの構成要素

| 要素 | 決めること | 失敗したときの症状 |
|---|---|---|
| 初期配置 | 誰がどこから始めるか | Buff前接敵、Rear attack、射線不良 |
| Squad | どのUnitを同じ判断単位にするか | 速度差、役割混在、Morale連鎖 |
| Formation | 前線幅・密度・奥行き | AoE被害、詰まり、突破 |
| 部隊命令 | 移動、攻撃、射撃、護衛 | 囮へ吸われる、標的へ届かない |
| Commander Script | 最初の最大5行動 | 主力Spellが遅い、不発、重複 |
| Main Order | Script後の行動 | 前進死、Gem浪費、無意味なAI Cast |
| Gem / Slave | 何を何回使うか | 不発、過剰消費、Retreat喪失 |
| Bodyguard | Commanderへ直接付ける護衛 | 暗殺・Rear attackで即死 |
| Guard Commander | SquadがCommander周辺を守る命令 | 後衛への突破 |
| Retreat route | Rout後の生存先 | 戦場外へ出たUnitが消失 |

---

# 情報収集からScriptへ落とす

## Scoutで見るもの

- 兵種とおおよその数
- Formation
- Shield・Armor
- Cavalry・Flying・Fast unit
- Archer・Crossbow
- MageとPriest
- Elemental Resistance
- Magic Resistance
- SacredとBless
- Summon・Chaff
- Commanderの位置
- Gemを使う可能性
- Fort relief army

情報が不足しているときは、一種類の勝ち方へ全投資しません。

```text
物理前衛
＋別Damage type
＋後衛防衛
＋退路
```

のように、最低限の保険を残します。

## 勝利条件を具体化する

悪い目標：

> 敵に勝つ

良い目標：

> Shield前衛で敵Cavalry Chargeを受け、Round 3までにShock Resistanceを入れ、Air MageをRear attackで止めながら敵主力を倒す

目標が具体的なら、必要なSquadとMage役割を逆算できます。

---

# 初期配置

## Screen

敵を最初に受ける層です。

候補：

- 盾兵
- Chaff
- Summon
- 高Protection
- 高Defence
- Elemental Resistance持ち
- Lanceを使わせる安価な兵

Screenの仕事は必ずしも敵を倒すことではありません。

- Chargeを吸収する
- Mageへ時間を与える
- Damage役を射撃から守る
- 敵を一か所へ固定する
- 敵のFatigueを増やす

こと自体が価値です。

## Damage line

両手武器、Sacred、高Attack、多段攻撃などのDamage役は、Screenより少し後方または左右へ置きます。

```text
敵
↓
Screenが接敵
↓
Damage lineが後から参加
```

とすることで、最初の射撃、Charge、RepelをDamage役へ集中させずに済みます。

## Flank

外周には、

- Cavalry
- Flying
- Fast infantry
- Stealth / Glamour unit
- Anti-cavalry
- Rear guard

を置きます。

敵後衛を狙うFlankerと、自軍後衛を守るCounter-flankerを分けます。

## Mage box

Mageを一列に並べるのではなく、重要度と敵の勝ち筋で配置します。

### 中央後方

通常は最も安定します。

- 前衛がScreenになる
- 左右どちらの攻撃にも距離がある
- Bodyguardを置きやすい

一方、Battlefield-wide AoEや中央を狙う攻撃へ巻き込まれます。

### 端

射撃線や中央AoEを避けられる場合がありますが、Attack Rear、Flying、外周Cavalryへ狙われやすくなります。

### 分散

Battlefield Enchantment caster、Communion master、Damage mageを別位置へ分けると、一度のRear attackで全機能を失いにくくなります。

## Decoy

安価なCommander、Summon、耐性持ちUnitを、敵AIが狙いやすい位置へ置く場合があります。

ただしAI Targetを完全に固定できるとは考えません。Decoyが機能したかはReplayで確認します。

---

# 接敵Timingを測る

ScriptはRound数ではなく、**接敵までの時間**で設計します。

```text
自軍前衛から敵前衛までの距離
÷
双方のCombat Speed
＋
Hold
＋
Obstacle
```

で概算します。

正確な内部計算式ではありませんが、次の判断には使えます。

- Buffを何個入れられるか
- Damage役へHoldが必要か
- 射撃が何回できるか
- Cavalryが外周を回れるか
- Summonが前線へ届くか

## Replayで測る

```text
Round 1：移動
Round 2：射撃開始
Round 3：Screen接敵
Round 4：Damage line接敵
Round 5：Rear attack到達
```

のように記録します。

次回は配置またはHoldを一つだけ変えます。

---

# Squadを分ける

## 分けるべき条件

- Combat Speedが違う
- ScreenとDamage役
- 射撃と近接
- 盾持ちと盾なし
- Sacredと非Sacred
- 長武器と短武器
- CavalryとInfantry
- Rear attackと正面戦闘
- Guard Commander
- Elemental Resistanceが違う
- Moraleが大きく違う

## 一つのSquadへ混ぜる問題

### 速度差

Fast unitが先行し、少数で敵へ接触します。

### 役割混在

盾兵と両手武器兵が同じ位置・命令で進み、両手兵も最初の射撃を受けます。

### Targetの不一致

PikeがCavalryを狙うべきなのに、全SquadがClosestのChaffへ向かいます。

### Formationの不一致

射撃兵と近接兵が同じ密度・前線幅になります。

## 分けすぎる問題

- Leadership不足
- SquadごとのMorale補正
- Commander PointとCommander数
- 操作量
- 小Squadが早くRoutする
- 狭い戦場で互いに詰まる

役割が同じUnitまで細分化する必要はありません。

---

# Formationと命令を組み合わせる

| 目的 | Formation候補 | 命令候補 |
|---|---|---|
| 正面で受ける | Line / Double Line | Attack Closest / Hold and Attack |
| Chargeを吸う | 広いLine | Attack Closest |
| AoEを避ける | Sparse / Skirmish | 敵に応じたAttack |
| 突破されにくくする | Box / Double Line | Attack Closest |
| Rear attack | 小さめの機動Squad | Hold and Attack Rear |
| Mage護衛 | Commander近くのBox | Guard Commander |
| 射撃 | Line / Sparse | Fire / Hold and Fire |
| Kiting | 散開できる高速Squad | Fire and Keep Distance |

Formationの詳細は[戦闘ルール](combat-rules.md)を参照してください。

---

# Undisciplined

Undisciplinedを含むSquadは、通常のFormation・命令へ強い制約を受けます。

実戦では、

- Skirmishへ固定される
- 指定したTarget orderを使えない
- Closestへ向かいやすい
- Rout後の統制が悪い

ことを前提にします。

Dominions 6には、特定のCommanderがUndisciplined Unitへ命令を与えられる能力もあります。該当Commanderの能力説明を確認してください。

!!! warning "混成Squad"
    Disciplined UnitのSquadへUndisciplined Unitを混ぜると、Squad全体の命令・Formationを壊す場合があります。Unitを一体追加しただけで命令欄が変わっていないか確認してください。

---

# 部隊のGeneral Order

## None

Squadの判断をAIへ任せます。

### 向く状況

- 特殊行動を持つUnit
- 混合武器でAI判断を試したい
- 何をさせるべきかまだ分からないTest
- 命令制約を受けるUnit

### 問題

AIの判断基準を説明しにくく、Replayから再現可能な改善を作りにくくなります。

重要Squadには、可能な限り目的を与えます。

---

## Attack

近接戦闘へ向かいます。Target preferenceと組み合わせます。

### Attack Closest

最も近い敵へ向かう基本命令です。

向く状況：

- Screen
- 敵構成が不明
- 前線を崩したくない
- 遠い標的を追いたくない
- Chaffを確実に止める

弱点：

- 敵の安価な囮へ吸われる
- Anti-cavalryがCavalryへ届かない
- Flankerが敵前衛へ捕まる
- 高価なCounter兵が低価値Targetを殴る

### Attack Rear

敵後方を優先して外周へ回ろうとします。

向くUnit：

- Cavalry
- Flying
- 高Combat Speed
- Stealth / Glamour
- 少数でMageを倒せるUnit
- Magic Weaponを持つCounter-flanker

狙うもの：

- Mage
- Priest
- Archer
- Commander
- Battlefield Enchantment caster
- Communion slave / master

失敗する理由：

- 前衛へ接触した
- 外周を敵Unitに塞がれた
- Obstacleで経路が変わった
- 敵後衛が端から離れていた
- 自軍Flankerが早すぎて孤立した
- 敵のRear guardへ当たった
- 標的が移動・Routした

`Attack Rear`は「敵Commanderを指定する命令」ではありません。後方へ圧力をかける優先方針です。

### Attack Archers

Archer系の後衛を優先します。

向く状況：

- Bow・Crossbowが主なDamage源
- Archerが盾なし
- 敵Mageより射撃兵の方が多い
- Rear attackでは標的が不安定

弱点：

- Mageを優先しない
- 敵Archerが遠すぎて前線に捕まる
- Archerを倒しても主力Spellは止まらない

### Attack Cavalry

Cavalryや高速部隊を優先します。

向くUnit：

- Pike
- 長Weapon
- Anti-charge
- 高Protectionの受け部隊

注意：

遠いCavalryを追って中央に穴を開ける場合があります。敵CavalryがどちらのFlankにいるか、配置も合わせます。

### Attack Large Monsters

大型Unitを優先します。

向くもの：

- Giant killer
- 高Damage
- AP / AN
- Poison
- MR attack
- 拘束
- Anti-trample

注意：

Large Monsterの後ろにいるCommanderやMageを放置する場合があります。

### その他のTarget

UIにはUnitや命令に応じて、Fliersなど別のTarget categoryが表示されることがあります。

Target categoryは「該当Unit一体を固定指定する」ものではなく、該当する敵Squad・Unitを選ぶための優先です。

---

## Hold and Attack

開始直後に短時間その場を保ち、その後Attackへ移ります。

### 主な目的

- Mage Buffを待つ
- Screenを先に接敵させる
- Cavalry Chargeを別Squadへ使わせる
- 敵を自陣側へ引き込む
- 速度の違うSquadのTimingを合わせる
- Rear attackの回り込み距離を作る

### Hold中

射撃武器を持つUnitは、条件が合えば射撃する場合があります。

### よくある失敗

- 全軍が待ち、敵射撃・Spellを無料で受ける
- 敵もHoldして接敵が遅れすぎる
- Damage役が遅れ、Screenだけが壊れる
- Fast Flankerがそれでも早すぎる
- Buff担当MageのCasting timeが長く、間に合わない

Holdは安全ではなく、**時間を何と交換するか**を決める命令です。

---

## Guard Commander

SquadがCommander周辺へ留まり、近づいた敵を迎撃します。

### 用途

- Attack Rear対策
- Flying対策
- Mage保護
- Battlefield Enchantment caster保護
- Communion master・slave保護
- Archerへ入ってきた敵の処理
- Routed前衛の穴を塞ぐ

### Guard向きUnit

- 高Attack
- 高Morale
- 長Weapon
- Magic Weapon
- 高Protection
- 高Defence
- 敵Flankerへ対応するResistance
- 移動が速すぎずCommander周辺を維持できる

### Guardの限界

- 射撃・Remote damageは防げない
- Battlefield-wide Spellは防げない
- 大量のFlyingを少数Guardで止められない
- Commanderと同じAoEへ巻き込まれる
- Commanderが移動すると護衛形状も崩れる

## Guard CommanderとBodyguardの違い

- **Guard Commander**：Squadへ与える通常戦闘の命令
- **Bodyguard**：Commanderへ直接割り当てる護衛枠

Bodyguardは暗殺戦を含むCommander防衛に関係します。両方を同じものとして扱わず、重要Casterには必要に応じて併用します。

---

## Retreat

SquadまたはCommanderが戦場から離脱を試みます。

### 用途

- Scout戦闘
- 敵Script確認
- Gem使用確認
- Remote battleの偵察
- 本隊を温存したProbe
- 特殊Unitの救出
- 戦う価値のないBattle

### 危険

- 戦場端へ届く前に捕まる
- 退路が敵Provinceしかない
- 隣接自領がない
- Retreat先が占領される
- Commanderだけ逃げて兵がRoutする
- Gem・Item持ちが死亡する

Retreatは戦術命令であると同時に、Strategic Map上の命令です。

---

# 射撃命令

## Fire

Missile weaponを使用し、Target preferenceへ射撃します。

### Fire Closest

最も安定した基本です。

- 命中しやすい近距離Target
- 接近中の前衛
- Chargeしてくる敵

へ弾を使います。

弱点は、盾持ちChaffへ高価なBoltや矢を浪費することです。

### Fire Archers

敵射撃兵を優先します。

比較するもの：

- 射程
- Precision
- Shield
- Protection
- Ammo
- Storm / Wind
- Darkvision
- Counter-fireの損失

### Fire Cavalry

Charge前に騎兵を削ります。

少数でもMount・RiderへDamageが入り、Chargeの形を崩せる場合があります。

### Fire Large Monsters

Sizeが大きく当てやすいTargetへ集中します。

- Giant
- Elephant
- Monster
- Mount

へ向きます。

### Fire Rear等

表示されるTarget optionは武器・UIによって異なります。狙う対象へ本当に弾が届くか、射程と射線を確認します。

---

## Hold and Fire

開始直後に位置を保ち、その後も射撃を中心に行動します。

### 主な用途

- 敵が近づいてから射撃して命中率を上げる
- Buffを待つ
- Javelin・投擲兵を前へ走らせない
- Crossbowの射線を維持する
- 前衛との距離を保つ

### 問題

- 敵射撃との撃ち合いで先に損耗する
- 敵が来ないと射程へ入らない
- 前衛が崩れた後に逃げ遅れる
- Obstacleで射線が塞がる

---

## Fire and Keep Distance

射撃しながら、敵が近づいたとき距離を取ろうとします。

### 向くUnit

- Mounted archer
- 高Combat Speed archer
- Skirmisher
- 移動しながら射撃できる特殊Unit
- 開けた戦場

### 失敗しやすい状況

- 戦場端が近い
- 敵がFlying
- 敵の方が速い
- Obstacleが多い
- Squadが大きすぎて互いに詰まる
- Crossbow等のReloadと移動が噛み合わない
- 逃げる方向へ味方後衛がいる

Kiting命令ではありますが、無限に距離を維持する保証はありません。

---

# Friendly Fire

射撃とAoEは、敵前衛だけを傷つけるとは限りません。

Friendly Fireが増える条件：

- 敵味方が同じSquare周辺で密集
- 低Precision
- 長距離
- Darkness
- Storm・Wind
- 大AoE
- 大量射撃
- 小型Unitの密集
- ShieldなしDamage役が前線へ入る

## 対策

- 射撃Targetを変える
- Archer Squadを分ける
- 前衛を左右へずらす
- 射撃兵を別角度へ置く
- 接敵後に有効な別Targetを作る
- Arrow系Buffを使う
- 高価な前衛へ撃ち込み続けるなら射撃量を減らす

Replayでは敵Killだけでなく、自軍が受けた射撃Damageも見ます。

---

# Commander Script

Commanderには通常、最初の最大5行動と、その後のMain Orderを設定します。

## Script slotで選ぶ代表行動

- Hold
- Hold or Fire missile weapon
- Hold or Cast a spell
- Cast a specific spell
- Attack one turn
- Fly Attack one turn

表示される選択肢はCommanderの能力、武器、Flying、Magic Path等によって変わります。Retreatは通常、Script後のMain Orderとして設定します。

## Main Order

- Stay Behind Troops
- Cast Spells
- Advance and Cast Spells
- Fire
- Attack
- Retreat

などから選びます。

!!! warning "Specific Spellは予約ではない"
    ScriptしたSpellをそのRoundにCastできない場合、同じSpellが次Roundへ必ず繰り越されるとは限りません。有効Targetがない場合などはその枠を飛ばし、AIが別Spellを選ぶ場合があります。Replayで「そのSpellが出なかった理由」を確認してください。

---

# CommanderのMain Order

## Stay Behind Troops

Commanderが前衛の後ろへ留まりながら、可能ならSpellやMissile weaponを使おうとします。

向くもの：

- 通常Commander
- Prophet
- Battlefield Enchantment caster
- Communion master
- Gem carrier
- 重要Booster holder

限界：

- 前衛が崩れれば敵が到達する
- Flying・Attack Rearは後衛を狙う
- 射撃・Spellは直接届く
- 戦場端で逃げ場を失う
- Commander自身の移動でBodyguard形状が変わる

「安全」ではなく、前進を抑えるMain Orderです。

## Cast Spells

AIが状況に応じてSpellを選びます。

### 任せやすい状況

- Gemを持っていない
- 有効Spellが少数
- Friendly Fireが小さい
- 敵Resistanceが明確
- 低級Supportを続けてほしい
- Script後に何を使っても大事故になりにくい

### 任せにくい状況

- Gemを温存したい
- Battlefield Enchantment重複が危険
- 大AoEが味方を巻き込む
- 敵Resistanceで有効Spellが狭い
- Rare Mageを前へ出したくない
- Communion fatigueが限界
- 特定Spell以外を使う価値が低い

## Advance and Cast Spells

Casterが前進しながらSpellを使います。

向く状況：

- Rangeが短い
- 前線Support
- Priest
- Short-range Control
- Combat caster
- 自己防御済みのMage

危険：

- 前衛崩壊時に巻き込まれる
- 脚が速くScreenを追い越す
- Bodyguardから離れる
- Gem・Boosterを失う

## Fire

Commander自身のMissile weaponを使います。

MageではないArcher commanderや特殊射撃Commanderへ使います。

## Attack

Commander自身を近接へ参加させます。

向くもの：

- Thug
- SC
- Heavy commander
- Prophet expander
- Combat summon

通常Mageへ不用意に設定すると、Script後に前進して死亡します。

## Retreat

Probe、Scout、Gem burn確認、勝てない特殊戦闘からの脱出へ使います。

退路を必ず確認します。

---

# Mage Scriptの実行条件

ScriptしたSpellが出るには、複数の条件が同時に必要です。

## 1. Research

Spellが研究済みであること。

## 2. 現在Path

Battle開始時の基礎Pathだけではありません。

```text
基礎Path
＋ Item
＋ Self boost
＋ Communion / Sabbath
＋ Battlefield condition
＋ Gemによる一時boost
```

でCast時点のPathが決まります。

### 順序依存

```text
Storm
→ Summon Storm Power
→ Air Spell
```

のようなScriptは、別CasterのCasting timeと発動点に依存します。

同じRoundに並べただけで、全Casterが必ず前提効果を受けてから次Spellを開始するとは限りません。

順序依存ScriptはTest battleで確認します。

## 3. Gem・Blood Slave

必要GemをCasterが持っていること。

Blood Slaveは通常Gemとは異なり、周辺のBlood Mageが使用できる仕組みがあります。距離と配置を確認します。

## 4. 一度に使えるGem量

Casterは一つのSpellで無制限にGemを使えません。現在Path、Spell requirement、Fatigue軽減に使う追加Gemの関係があります。

詳細は[GemとCombat Gem](../magic/gems.md)を参照してください。

## 5. 有効Target

Spellが対象にできるUnitが存在すること。

例：

- Undead専用SpellにUndeadがいない
- Damage Spellの対象がResistanceでAI上ほぼ無効と判断される
- Buff対象が既に効果を持つ
- Range内に敵がいない
- Friendly targetが遠い

有効TargetがないScript slotは飛ばされる場合があります。

## 6. Range

CasterとTargetの距離が射程内であること。

Range不足の典型：

- Mageを後ろへ置きすぎた
- 敵がHoldした
- Control Spellが前衛へ届かない
- Targetが外周を移動した
- Battlefield Obstacleで経路と接敵が変わった

## 7. 戦場条件

- Storm
- Rain
- Underwater
- Darkness
- Temperature
- Plane
- Terrain
- Battlefield Enchantment

などによって、Cast可否や価値が変わります。

## 8. 行動可能

Casterが、

- Stun
- Paralyze
- Sleep
- Entangle
- Rout
- Unconscious
- Silence等
- 死亡

で行動不能になっていないこと。

## 9. Interrupt

Spellは選択と同時に即時発動するとは限りません。

Casting timeの準備中にDamageを受けると、SpellをInterruptされる場合があります。

したがって、Caster保護は生存だけでなく、**Spellを完成させるため**にも必要です。

---

# Gem運用

## Gemの三つの役割

1. Spell固有Cost
2. Pathを一時的に1上げて要求へ届く
3. 追加GemでSpell Fatigueを減らす

Casterの現在Pathと一度に使える量には上限があります。

## Conservative Gem Use

UIでConservative Gem Useを選べる場合、Script後のAIによるGem使用を抑える目的で使います。

ただし、

- ScriptしたGem Spell
- AIの戦力評価
- Spell requirement
- 追加Fatigue軽減

と完全に一致する保証ではありません。

Replayで実際の消費を確認します。

## Gemを持たせる量

```text
必須SpellのCost
＋ Path boost用
＋ Fatigue軽減用
＋ 予備
```

を分けます。

### 少なすぎる

- 主力Spell不発
- 一回しかCastできない
- Path boost後の本命Gemがない
- 第二戦に残らない

### 多すぎる

- 小規模戦で浪費
- Retreat・Routで失う
- Mage死亡時に敵へ渡る
- Gem baitに反応
- Script後のAIが高価なSpellを使う

## Gem budget表

| Caster | 役割 | 必須Spell | 最低Gem | 最大使用許容 | 生存優先度 |
|---|---|---|---:|---:|---|
| A | Battlefield condition | Spell A | 1 | 2 | 最重要 |
| B | Resistance | Spell B | 1 | 1 | 高 |
| C | Damage | Spell C | 2 | 4 | 中 |
| D | Summon | Spell D | 3 | 3 | 高 |

戦闘前に「持っているGem」ではなく「使ってよいGem」を決めます。

---

# Mageを役割分担する

## 1. Condition caster

Storm、Darkness、Rain等、戦場条件を作ります。

一人のCaster死亡で戦略全体が崩れる場合があります。

## 2. Self-boost caster

Summon Earthpower、Power of the Spheres等で自分のPathとFatigue効率を上げます。

Self boostを本命Spellより前に置きます。

## 3. Resistance caster

- Fire
- Cold
- Shock
- Poison
- Acid
- MR

など、敵の主Damageへ対応します。

接敵後では遅い場合が多いため、優先Roundを早くします。

## 4. Defensive buff caster

- Protection
- Defence
- Ethereal
- Luck
- Regeneration
- Mistform系

を担当します。

## 5. Offensive buff caster

- Strength
- Attack
- Quickness
- Magic Weapon
- AP weapon
- Archer buff

を担当します。

## 6. Control caster

- Earth Meld
- Entangle
- Paralyze
- Confusion
- Swarm
- Wall・Prison
- Slow

等で敵の攻撃機会を減らします。

## 7. Damage caster

- Evocation
- MR attack
- Poison
- Fatigue
- Skeleton
- Elemental summon

など、敵の薄い防御層を攻撃します。

## 8. Sustain caster

- Reinvigoration
- Relief
- Healing
- Morale
- Fatigue support

を担当します。

## 9. Battlefield Enchantment anchor

戦場全体効果を維持する重要Casterです。

- 後方配置
- Bodyguard
- Guard Commander
- Elemental Resistance
- MR
- Arrow protection
- 予備Caster

を用意します。

---

# 一人へ全部やらせない

悪い例：

```text
Round 1：Self boost
Round 2：Fire Resistance
Round 3：Protection
Round 4：Strength
Round 5：主力Control
Round 6以降：Damage
```

敵がRound 3に接敵するなら、主力Controlは間に合いません。

改善：

```text
Mage A：Self boost → Resistance → Cast Spells
Mage B：Self boost → Protection → Cast Spells
Mage C：Self boost → Strength → Control → Damage
Mage D：Battlefield condition → Damage
```

Mageの人数を使って処理を並列化します。

ただし、全員が同じSelf boostを必要とするとは限りません。研究、Path、Gem、Casting timeを比較します。

---

# 依存関係を図にする

Scriptを書く前に、Spell dependencyを並べます。

```text
Storm
  ↓
Storm Power
  ↓
Lightning damage
```

```text
Communion Slave
  ↓
Communion Master
  ↓
Path boost
  ↓
Army-wide spell
```

```text
Poison Resistance
  ↓
Foul Vapors
```

```text
Fire Resistance
  ↓
Heat / Fire battlefield effect
```

## 依存関係の危険

- 前提Casterが遅い
- 前提CasterがInterrupt
- Slaveが間に合わない
- Caster順序がCasting timeで前後する
- 前提SpellがTargetなしで飛ぶ
- 前提効果がDispel・Caster死亡で消える
- Gemが足りない

一つの前提へ全Armyを依存させるなら、Caster保護と代替を用意します。

---

# Mage Script Template

以下は固定解ではなく、役割を考えるための型です。

## 早い接敵への最小Script

```text
Round 1：最重要ResistanceまたはSelf boost
Round 2：勝利に直結するBuff / Control
Round 3：Main damage
Round 4–5：Main damage / Control
Main Order：Cast Spells
```

Buffを欲張りません。

## 重装Armyの支援

```text
Self boost
→ Resistance
→ Offensive buff
→ Armor破壊 / Control
→ Main spell
→ Cast Spells
```

Protectionをさらに上げるだけでなく、AN・Poison・MRへの回答を入れます。

## 対Elemental Army

```text
対応Resistance
→ 第二防御
→ 敵CasterへのControl
→ 別Damage type
→ Cast Spells
```

## Summon Screen

```text
Summon
→ Summon
→ Control
→ Damage
→ Cast Spells
```

Summonが前線へ届くTimingと、召喚中に本来のArmyが接敵しないかを確認します。

## Battlefield Enchantment

```text
Self protection
→ 必要Path boost
→ Battlefield Enchantment
→ Sustain / Control
→ Cast Spells
Main Order：Stay Behind TroopsまたはCast Spells
```

Casterが死ぬと解除される効果か確認します。

## Communion / Sabbath

### Slave側

```text
Communion Slave / Sabbath Slave
→ 必要な自己防御
→ 低Fatigue行動または待機
```

### Master側

```text
Communion Master / Sabbath Master
→ Resistance
→ Army buff
→ Main spell
→ Sustain
```

Slave Fatigue、Master数、Path差、Armor Encumbranceを確認します。

詳細は[Communion・Sabbath](../magic/communions.md)を参照してください。

## Thug / SC

```text
Self protection
→ Elemental Resistance
→ Reinvigoration / Regeneration
→ Attack
```

敵の接敵が早ければBuffを削ります。

Script終了後に`Attack`へ移るか、`Hold`を挟むかを決めます。

---

# Priest Script

PriestもMageと同じくTimingが重要です。

## Bless

Sacredが接敵する前にBlessが入ること。

```text
Bless / Divine Blessing
→ Morale support
→ Banish / Smite / Cast Spells
```

### よくある失敗

- Sacredが前へ出すぎてBless前接敵
- PriestがRange外
- Sacred Squadが分散
- Priestが敵射撃でInterrupt
- Bless後にPriestが前進

## Undead対策

```text
Banish
→ Banish
→ Morale / Support
→ Cast Spells
```

Undead数、Priest level、Range、Fatigueを確認します。

---

# 部隊編成Template

## Screen＋Damage＋Mage

```text
前方：盾兵 / Chaff ─ Attack Closest
第二線：両手武器 / Sacred ─ Hold and Attack Closest
左右後方：Rear guard ─ Guard Commander
後方中央：Resistance / Buff / Control Mage
外周：Fast unit ─ Hold and Attack Rear
```

## 対射撃

```text
前方：大盾 / 安価なScreen
主力：Hold and Attack
左右：Fast unit ─ Attack Archers
射撃：Fire ArchersまたはFire Closest
Mage：Arrow防御 / Storm / Mist系
```

## 対Cavalry Charge

```text
前方：ChaffまたはShield line
左右：Pike ─ Attack Cavalry
第二線：Damage役 ─ Hold and Attack
射撃：Fire Cavalry
Mage：拘束 / Defence低下
```

## 対Flying / Rear attack

```text
前方：通常Screen
Mage周辺：Guard Commander
後方左右：Magic Weapon / 長Weapon
Commander：Bodyguard
機動予備：Attack ClosestまたはFliers優先
```

## 対高Defence

```text
Screen：Attack Closest
多段攻撃：Hold and Attack
Mage：拘束 / Defence低下
射撃・AoE：密集Squareを狙う
```

## 対高Protection

```text
盾兵：敵を固定
高Damage / AP：後から接敵
Mage：Armor破壊 / AN / MR / Poison
Crossbow：適切なTargetへ射撃
```

## Mage-heavy Army

```text
前方：Summon / Chaff
第二線：本来の主力
後方：役割別Mage
左右後方：Guard Commander
予備Commander：Leadership維持
```

---

# Script後のFallback

Scriptが終わった後、AIへ何を許すか決めます。

## Cast Spellsへ任せる

条件：

- Gemをほぼ持たせない
- 有効Spellが多い
- Friendly Fireが許容
- Casterを失ってもよい
- Rangeが十分

## Stay Behind Troops

条件：

- Rare Mage
- Battlefield Enchantment caster
- Booster holder
- AI Castの価値が低い
- 生存が最優先

ただし、後方から届く有効Spellが少ない場合や射程が短い場合は、行動価値が下がります。

## Advance and Cast

条件：

- Range不足
- Short-range support
- 前衛が安定
- 自己防御済み

## Attack

条件：

- Thug / SC
- Combat Commander
- 近接参加が勝利条件

## Retreat

条件：

- 情報収集が目的
- Gemを使わせた
- 本戦を避ける
- 退路がある

---

# Conservative Gem UseとGem Bait

## Gem Bait

相手へ、

- 小Army
- Summon
- Remote attack
- Scout
- Raid

を当て、高価なGem Spellを使わせる戦術です。

対策：

- Gemを必要量だけ持たせる
- Conservative Gem Use
- Script後のMain Orderを制限
- 小戦闘用Mageを分ける
- Battlefield Enchantmentを毎戦使わない
- Replayで消費を確認

## Gem burn後の本戦

敵が一戦目でGemを使ったからといって、全て失ったとは限りません。

- 予備Gem
- 別Mage
- Lab補給
- Blood Slave
- Item cast

を確認します。

---

# Commander保護

## Bodyguard

Commanderへ直接割り当てます。

向くUnit：

- 高Morale
- 高Protection
- 高Attack
- Magic Weapon
- 長Weapon
- 敵Assassinへ有効なResistance

## Guard Commander Squad

通常戦闘でCommander周辺を守ります。

## Commander分散

一人のCommander死亡で全SquadがLeadershipを失わないようにします。

- 前衛Commander
- Archer Commander
- Mage Commander
- 予備Commander

を分けます。

## 配置

- 全Commanderを同じSquare周辺へ密集させない
- 端へ並べすぎない
- Mageを一直線にしない
- Battlefield Enchantment casterを最奥へ置く
- Blood SlaveとBlood Mageの距離を確認

---

# RetreatとRoutをScriptへ含める

戦闘前にStrategic Mapを見ます。

- 自領が隣接しているか
- Fortへ逃げられるか
- Enemy Zoneで孤立していないか
- Teleport後に退路があるか
- Multiple planeで逃げ先が成立するか
- 敵が同Turnに退路を取らないか

## Probe battle

情報収集のために意図的に小戦闘を行う場合、

```text
Scout /耐久Commander
→ HoldまたはCast
→ Retreat
```

とし、目的を一つにします。

- Enemy Scriptを見る
- Gemを見る
- Formationを見る
- Battlefield Enchantmentを見る
- Resistanceを見る

高価なItemやGemは持たせません。

---

# 症状別の診断

| Replayの症状 | 主な原因 | 最初に試す変更 |
|---|---|---|
| Buff前に接敵 | 配置前すぎ、Hold不足、敵が速い | 前衛を下げる、Buffを削る |
| Screenだけ壊れる | Damage役が遅い、Hold過多 | Damage役を前へ、Holdを減らす |
| Damage役が先に死ぬ | Squad混在、速度差 | Squad分割、Screenを前へ |
| Rear attackが前衛へ当たる | 経路遮断、早すぎる | 後方配置、Hold、別Flank |
| Archerが味方を殺す | 射線、Target、接敵後射撃 | Target変更、配置角度、射撃量 |
| Mageが予定Spellを使わない | Target、Range、Path、Gem | 条件を一つずつ確認 |
| Spellが一Round遅い | Casting time、依存Caster、移動 | Script短縮、Caster分担 |
| Casterが詠唱中断 | 射撃・AoE・Rear attack | Bodyguard、Shield、位置 |
| Script後にMageが前進死 | Main OrderがAttack / Advance | Stay Behind / Cast Spells |
| Gemを使いすぎる | AI Cast、余剰Gem | Gem量削減、Conservative |
| Gem Spellが不発 | 一度の使用上限、Path不足 | Booster、Self boost、Gem再計算 |
| Battlefield Enchantmentが消える | Caster死亡・Rout | Caster保護、予備 |
| Communion Slaveが倒れる | Fatigue、Master過多、Path差 | Master数削減、Slave増、Sustain |
| 全軍Holdで削られる | Timing交換が不利 | Screenだけ前進、Hold削減 |
| Guardが足りない | Flying数、広いRear attack | Guard増、Commander分散 |
| Undisciplinedが命令無視 | Squad制約 | Squad分離、対応Commander |
| Formationが崩れる | Obstacle、速度差、Squad干渉 | 配置分散、Squad再編 |
| Rout後に大量消失 | Retreat routeなし | 侵攻経路・隣接自領を修正 |

---

# Battle Replayの確認手順

詳細は[Battle Replayの読み方](../getting-started/battle-replay.md)を参照してください。

命令を評価するときは、次の順で見ます。

1. **予定**：誰が何Roundに何をするはずだったか
2. **接敵**：Screenは何Roundに接触したか
3. **分離**：Fast unitが孤立しなかったか
4. **標的**：Target orderは何を選んだか
5. **経路**：Attack Rearがどこを通ったか
6. **射撃**：誰へ撃ち、Friendly Fireはいくつか
7. **Spell**：各Script slotで何を試したか
8. **Gem**：何個使用したか
9. **Interrupt**：CasterがDamageを受けたRound
10. **Main Order**：Script後に何をしたか
11. **Commander**：死亡とRoutの順序
12. **退路**：逃げたUnitが生き残ったか

## Script記録Template

```text
戦闘目的：
敵の主Damage：
敵のCounter：
接敵予想Round：

Squad A：
- 役割：
- 配置：
- Formation：
- Order：
- 実際の接敵Round：

Squad B：
- 役割：
- 配置：
- Formation：
- Order：
- 実際の接敵Round：

Mage A：
- 役割：
- Slot 1：
- Slot 2：
- Slot 3：
- Slot 4：
- Slot 5：
- Main Order：
- Gem：
- 実際にCastしたもの：

最初の計画崩壊：
次回一つだけ変えること：
```

---

# 一つだけ変える

悪い検証：

```text
配置を変更
＋ Unit比率変更
＋ Spell変更
＋ Gem変更
＋ Target変更
```

これでは何が効いたか分かりません。

良い検証：

```text
Test 1：Holdだけ減らす
Test 2：Resistanceだけ追加
Test 3：Rear guardだけ増やす
```

DRNによる揺れがあるため、重要なBattle Scriptは複数回試します。

---

# よくある誤解

## 「Attack RearならMageを倒せる」

後方を優先する命令であり、Mage一体を指定する命令ではありません。

## 「HoldすればBuffは完成する」

敵の速度、射撃、Casting time、ObstacleでTimingは変わります。

## 「Specific Spellなら必ずCastする」

Target、Range、Path、Gem、行動可能状態が必要です。

## 「Script slotは不発なら次Roundへ繰り越す」

必ずしもそうではありません。そのRoundの行動として飛ばされ、AIが別Spellを選ぶ場合があります。

## 「GemはSpell Cost分だけ使う」

Path boostやFatigue軽減へ追加Gemを使う場合があります。

## 「Stay Behind Troopsなら安全」

前衛崩壊、Flying、射撃、Spellには安全ではありません。

## 「Guard CommanderとBodyguardは同じ」

Squad orderとCommanderへの直接護衛は別です。

## 「全Mageへ同じScriptが安定」

同じSpellが重複し、主力SpellのTimingとGemを浪費します。

## 「長いScriptほど強い」

接敵前に必要な効果が間に合う短いScriptの方が強い場合があります。

## 「一度勝ったから完成」

敵Script不発、Target選択、DRNに助けられた可能性があります。

---

# 実戦用チェックリスト

## 戦闘前

- [ ] 戦闘目的を一文で書いた
- [ ] 敵の主Damage typeを確認した
- [ ] ScreenとDamage役を分けた
- [ ] Combat Speed差を確認した
- [ ] FlankとRear guardを用意した
- [ ] 接敵予想Roundを決めた
- [ ] 最重要Buffが接敵前に入る
- [ ] Mageを役割分担した
- [ ] Script後のMain Orderを確認した
- [ ] Gem最大使用量を決めた
- [ ] Battlefield Enchantment casterを守った
- [ ] BodyguardとGuard Commanderを区別した
- [ ] Undisciplinedを混ぜていない
- [ ] Retreat routeがある

## 戦闘後

- [ ] 最初の接敵Round
- [ ] 最初に壊れたSquad
- [ ] Attack Rearの到達先
- [ ] Friendly Fire
- [ ] Script不発
- [ ] Caster Interrupt
- [ ] Gem消費
- [ ] Script後の行動
- [ ] Commander死亡
- [ ] 最初のRout
- [ ] Retreat後の消失
- [ ] 次回一つだけ変える項目

---

# 記事の今後の分離

このページは、配置からMage Scriptまでを一つの戦術設計として理解するための総合記事です。

次は個別記事へ分離する価値があります。

- Target orderの選択規則
- Casting timeとInterrupt
- Combat Gemの厳密な使用規則
- Communion Script
- Blood Slave配置
- Battlefield Enchantment caster保護
- Bodyguardと暗殺戦
- Archer射線・Friendly Fire
- Undisciplinedと特殊Commander
- Test battleの記録方法

個別記事が追加されても、このページはBattle Script全体の入口として残します。

---

## 関連ページ

- [戦闘ルール](combat-rules.md)
- [両手武器・片手武器・盾](weapons-and-shields.md)
- [Battle Replayの読み方](../getting-started/battle-replay.md)
- [序盤拡張](../getting-started/expansion.md)
- [最初の戦争](../getting-started/first-war.md)
- [Magicの基本](../magic/index.md)
- [GemとCombat Gem](../magic/gems.md)
- [Communion・Sabbath](../magic/communions.md)
- [Research](../magic/research.md)
- [Shortcut key](../getting-started/shortcuts.md)
- [国家別Recruitデータ](../data/recruitment/index.md)
- [Combat data索引](../data/combat/index.md)

## 主な情報源

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
- Dominions 6.35ゲーム内Army Setup・Battle order Tooltip
- Dominions 6.35 Battle Replay
- このWikiの固定Spell・Unit・Weapon・Armorデータ

!!! note "記事状態"
    部隊命令、最大5枠のCommander Script、Main Order、Target・Range・Gem・Casting timeによる不発、Dom6のObstacleとUndisciplined例外、Replay診断を6.35向けに整理しています。AIの全Target選択規則、全Spell固有例外、Casting pointの乱数、暗殺戦Bodyguard処理をすべて実験的に証明した状態ではないため、Statusは`reviewed`としています。
