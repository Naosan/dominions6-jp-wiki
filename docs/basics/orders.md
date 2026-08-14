---
title: 命令とBattle Script
status: expanding
verified_version: "6.35"
last_verified: "2026-08-14"
---

# 命令とBattle Script

Dominionsの戦闘では、戦闘開始後にUnitを直接操作できません。

したがって、

> **初期配置 × Squad編成 × Formation × 命令 × Mage Script**

が戦術そのものです。

同じ兵数・同じ装備でも、命令と配置が違えば全く別のArmyになります。

---

## 戦闘前に決める五つ

1. **誰が最初に敵を受けるか**
2. **どのSquadがどの敵を狙うか**
3. **何Round待ってから動くか**
4. **Mageが何Round目に勝利Spellを使うか**
5. **敵のRear attackから誰がCommanderを守るか**

命令を選ぶ前に、この五つへ答えを作ります。

---

## 初期配置

### 前方中央

敵前衛を最初に受ける部隊です。

- 盾兵
- Chaff
- 高Protection兵
- Summon兵
- Body Ethereal等の防御を持つ部隊

を置きます。

前へ出しすぎるとBuff前に接敵し、後ろへ置きすぎると敵がMageへ近づく時間を与えます。

### 第二線

火力兵・両手武器・Sacredなどを、受け部隊より少し後ろまたは左右へ置きます。

これにより、盾兵へ敵が接触した後に火力兵が参加し、盾なしUnitが最初の射撃とChargeを受けるのを避けられます。

### 左右

- 騎兵
- Fast unit
- Flanker
- 長槍
- Rear attack対策

を置きます。

敵騎兵が外周を回るなら、左右後方にGuard Commander部隊を置く方がよいこともあります。

### 後方中央

Mageと重要Commanderの基本位置です。

端へ置くと「Attack Rear」を受けやすく、中央へ置くとAoEやEarthquake等に巻き込まれる可能性があります。敵の勝ち筋を見て位置を変えます。

---

## Squadを分ける理由

一つの巨大Squadへ全兵を入れると管理は簡単ですが、次の問題が起こります。

- 武器やCombat Speedが違う兵が同じ命令で動く
- 盾兵と両手武器兵が同時に接敵する
- 一つのMorale崩壊で全員がRoutする
- 一つの標的命令へ全兵が引っ張られる
- Formationが兵種に合わない

### 分ける基準

- Combat Speedが違う
- 防御役と火力役が違う
- 射撃と近接
- Sacredと非Sacred
- 長武器と短武器
- Rear attack要員
- Bodyguard

ただしSquadを細かくしすぎると、CommanderのLeadership、Squad Morale bonus、操作量が問題になります。

---

# 部隊命令

## Attack Closest

最も基本的な命令です。近い敵へ向かいます。

### 向いている状況

- 敵構成が不明
- 前衛同士を正面衝突させたい
- 特殊な標的を追って陣形を崩したくない
- 受け部隊

### 弱点

敵が安価な囮を前へ置くと、主力が囮へ吸われます。

---

## Hold and Attack

一定Round待ってから攻撃します。

### 主な目的

- Mage Buffが入るまで待つ
- 敵をこちら側へ引き込む
- 敵射撃兵へ接近距離を短くする
- 速度の違うSquadの接敵Timingを合わせる
- Enemy ChargeをChaffへ使わせた後に投入する

### よくある失敗

全軍をHoldにすると、敵の射撃とSpellを一方的に受けます。

Holdは「安全に待つ命令」ではなく、**Timingを交換する命令**です。

---

## Attack Rear

敵後方へ回り込みます。

### 狙うもの

- Mage
- Archer
- Commander
- 高価なSupport unit

### 向いている部隊

- 高Combat Speed
- Flying
- Cavalry
- Stealthy / Glamour raid unit
- 少数でも後衛を倒せる高Attack兵

### 弱点

- 敵のBodyguard
- 後方に置かれた長槍
- 外周の迎撃部隊
- 障害物による経路変更
- 相手後衛が中央ではなく端へ寄っている

Attack Rearは「必ずMageを狙う」命令ではありません。経路上の敵、戦場の形、速度、接敵判定によって前衛へ捕まることがあります。

---

## Attack Archers

射撃部隊を優先します。

敵がArcher以外の後衛Mageを主力にしている場合、Attack Rearより目的に合わないことがあります。敵編成をReplayや偵察で確認します。

---

## Attack Cavalry / Large Monsters / Other Targets

特定の兵種を狙う命令は、Counter兵を正しい相手へ当てるために使います。

例：

- Pike → Cavalry
- Giant killer → Large Monster
- Magic weapon兵 → EtherealやSummon
- Guardian系 → Sacred

ただし遠い標的を追って前線に穴を空ける場合があります。

---

## Guard Commander

Commanderの近くに留まり、接近した敵を迎撃します。

### 重要な用途

- Attack Rear対策
- Flying assassin対策
- Mageを射撃後の近接から守る
- Battlefield Enchantment casterを生存させる
- Blood Slave周辺を守る

Bodyguardは「敵Armyを倒す部隊」ではなく、**数RoundだけCommanderを生存させる保険**です。

### 選び方

- 高Morale
- 高Attack
- Magic weapon
- 長武器
- 高Protectionまたは高Defence
- 敵Flankerへ有効なResistance

安価な兵でも、敵一体を足止めしてSpell一回を通せれば仕事を果たします。

---

## Fire

射撃を続けます。標的優先を指定できます。

### Fire Closest

最も安定しますが、盾持ちChaffへ弾を浪費する場合があります。

### Fire Large Monsters

大きく当てやすいUnitへ集中します。Giant、Elephant、Monsterへ有効です。

### Fire Cavalry

騎兵Chargeを接敵前に削ります。

### Fire Archers

敵射撃部隊との撃ち合いです。射程、Precision、盾、Storm等を比較します。

### Friendly Fire

味方前衛と敵が接触した後も射撃を続けると、外れた弾が味方へ当たります。

特にCrossbow、Arbalest、AoE射撃は自軍の高価な兵も倒します。Replayで味方Killを確認します。

---

## Fire and Keep Distance

射撃しながら距離を取ろうとします。

Combat Speedや戦場幅が不足すると、逃げ切れず陣形を崩すだけになる場合があります。Fast archer、Mounted archer、特殊なSkirmisher向けです。

---

## Retreat

戦闘開始後に退却を試みます。

### 用途

- Scoutや偵察Commanderを生存させる
- Ritualで作った戦闘Replayだけを確認する
- Enemy scriptを見て本隊を温存する
- Siegeや特殊戦闘で特定Unitを救う

退路が敵Provinceしかない、またはBattle終了前に戦場端へ到達できない場合は死亡します。

---

# Commander命令

## Stay Behind Troops

Commanderが前へ出るのを抑えます。

ただし「絶対に安全な位置へ留まる」わけではありません。前衛が崩れれば敵が到達し、射撃・Spell・Flyingは後衛を直接攻撃できます。

---

## Hold

その場で待ちます。

- 敵を引きつける
- 前衛との距離を維持する
- Script後の不用意な前進を防ぐ
- Rear attackを迎撃する

目的で使います。

---

## Cast Spells

AIが状況に応じてSpellを選びます。

### AIへ任せやすい状況

- 低級攻撃Spellを連打する
- 有効標的が明確
- Gemを持たせていない
- Script後に何をCastしても大事故になりにくい

### AIへ任せにくい状況

- Gemを温存したい
- Friendly Fireが致命的
- 特定のBuff順が必要
- 敵Resistanceにより有効Spellが変わる
- Battlefield Enchantmentの重複を避けたい

---

## Attack / Fire

Commander自身を戦闘参加させます。

MageやPriestへ不用意にAttackを設定すると、Script終了後に前へ歩き出します。戦闘用Commander以外はStay Behind TroopsやCast Spellsへ戻す方が安全です。

---

# Mage Script

Mageは通常、複数のSpellを順番に指定できます。

## Scriptの基本構造

```text
1. Path boost / 自己防御
2. Army-wide defense
3. Army-wide offense
4. 敵への拘束・Debuff
5. 主力攻撃Spell
6. Cast Spells
```

すべてのMageへ同じScriptを入れるのではなく、役割を分けます。

### Booster担当

Summon Earthpower、Phoenix Power、Power of the Spheres等でPathとFatigue効率を上げます。

### 防御担当

Resistance、Protection、Luck、Regeneration、Antimagic等を配ります。

### 攻撃担当

Strength、Quickness、Weapons buff、Flaming Arrows等を使います。

### Control担当

Earth Meld、Maws、Paralyze、Confusion、Swarm等で敵を止めます。

### Damage担当

Evocation、Soul Slay、Skeleton spam、Elemental summon等を使います。

---

## 一人へ全部やらせない

一人のMageへ、

1. Path boost
2. Fire Resistance
3. Protection
4. Strength
5. 主力Spell

と詰め込むと、主力Spellが出るまで数Roundかかります。

敵がRound 2に接敵するなら、Round 5の勝利Spellは間に合いません。

**Mageの数で並列化する**のが重要です。

---

## Scriptが飛ばされる理由

指定Spellが使われない主な理由は次です。

- 要求Pathへ届いていない
- 必要Gemがない
- 一度に使えるGem上限を超える
- 有効な標的が射程内にいない
- Spellが現在の戦場条件では使用不可
- Casterが移動・気絶・Interruptされた
- 先に別の効果でPathや環境条件が変化した

Replayでは「AIが勝手なことをした」と判断する前に、Spell description、Path、Gem、Range、Targetを確認します。

---

## Gemを持たせるときの注意

Mageは必要Gemだけでなく、Fatigue軽減や一時Path boostのために追加Gemを使う場合があります。

したがって、

- この戦闘で何個まで使ってよいか
- Retreat時に失ってよいか
- AI Cast Spellsへ移った後も消費してよいか
- Gem baitやGem burnを受けないか

を考えます。

詳しくは [GemとBlood Slave](../magic/gems.md) を参照してください。

---

# 典型的な配置例

## 盾＋火力＋Mage

```text
前方：盾兵 / Chaff ─ Attack Closest
第二線：両手武器 / Sacred ─ Hold and Attack
左右後方：Guard Commander
後方中央：Buff Mage / Damage Mage
外周：Fast cavalry ─ Attack Rear
```

思想は次の通りです。

- 盾兵は倒さなくてよい。時間を買う
- 火力兵は最初のChargeと射撃を受けなくてよい
- MageはArmorへ付き合わず、別の防御層を攻撃する
- Cavalryは前衛を殴らず、後衛へ圧力をかける

## Skeleton / Summonで時間を稼ぐ

```text
前方：少数の受け兵
後方：Death Mageを複数
側面：通常主力
```

Skeletonが接敵とChargeを吸収し、敵が疲れた後に通常主力を投入します。

## 射撃対策

```text
前方：大盾 / 安価な囮
主力：Hold and Attack
左右：Fast unitでAttack Archers
Mage：Arrow Fend / Storm / Mist等
```

全軍をただ前へ走らせるより、射撃を受ける対象と射撃を止める対象を分けます。

---

# よくある失敗

## 全軍Attack Closest

敵Chaffへ主力が吸われ、Counter兵が必要な標的へ届きません。

## 全軍Hold and Attack

Buffは完成しますが、敵射撃とMagicを無料で受けます。

## Mageを端へ並べる

Attack RearやFlyingに順番に狩られます。

## Commanderを前に置く

Arrow、Trample、Charge、AoEでLeadershipを失います。

## Rear attackへ全騎兵を使う

敵が後方迎撃を用意していると高価な騎兵が孤立します。

## Scriptを長くしすぎる

勝利Spellが発動する前に前衛が崩れます。

## Gemを大量に渡してCast Spells

小規模戦で戦略資源を使い切ります。

---

# Battle Replay確認表

- 初期配置から接敵まで何Roundか
- Holdは必要だったか
- Rear attackはどこへ到達したか
- Guard Commanderは敵を止めたか
- Spellは指定順に発動したか
- Gemは何個使われたか
- Friendly Fireは何人倒したか
- Commander死亡がRoutへつながったか
- 別Squadへ分けるべき兵種が混在していないか

---

## 関連ページ

- [戦闘ルール](combat-rules.md)
- [両手武器・片手武器・盾](weapons-and-shields.md)
- [魔法の基本](../magic/index.md)
- [Communion](../magic/communions.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [illwiki: Combat Magic](https://illwiki.com/dom5/dom6/combat-magic)
- [illwiki: Undisciplined](https://illwiki.com/dom5/dom6/undisciplined)
