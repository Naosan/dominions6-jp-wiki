---
title: 戦闘ルール
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# 戦闘ルール

Dominions 6の戦闘を、**配置とTiming → 命中 → Shield → Damage軽減 → 状態異常 → Fatigue → Moraleと退却**の順で整理します。

このページの目的は、個々のUnitを「強い・弱い」で覚えることではありません。

> **どの防御層が機能し、どの層が突破され、次の戦闘で何を一つ変えるべきか**

を自分で判断できるようにすることです。

!!! note "このページの精度範囲"
    ここではDominions 6.35のManual、公式変更点、ゲーム内表示、固定データから確認できる主要ルールを、実戦で使える順に整理します。内部処理にはSpell・Weapon・能力固有の例外があります。数式は理解用の概念式として読み、特定効果の最終判定はゲーム内Tooltipと現行データも確認してください。

---

## 最初に覚える三つ

### 1. 戦闘は防御層の競争

高ProtectionでもShockやPoisonには弱いことがあります。高DefenceでもAoE、拘束、多数の攻撃には崩されます。高MRでも通常武器には意味がありません。

相手の全能力を上回るのではなく、**最も薄い層へ攻撃を通す**のが基本です。

### 2. 戦闘はTimingの競争

同じSpellでも、接敵前に入ればArmy Buff、接敵後なら手遅れです。同じ両手武器兵でも、盾兵の後から入ればDamage役、最初に射撃を受ければ高価な損失になります。

### 3. 一回のReplayは証明ではない

多くの判定にDRNが使われるため、同じ編成でも結果は揺れます。一戦の勝敗だけでなく、接敵位置、命中、Damage type、Fatigue、Routの順序を見ます。

---

# 戦闘の全体像

以下は理解用の流れです。ゲーム内部の厳密な全サブフェーズ順を表すものではありません。

```text
戦闘前効果・初期配置
        ↓
移動・標的選択・接敵
        ↓
Awe / Repel / 回避 / Shieldなどの防御
        ↓
Damage / Protection / Resistance / MR
        ↓
状態異常・Fatigue・Affliction
        ↓
Morale check・Rout・Retreat
        ↓
次Roundまたは戦闘終了
```

プレイヤーが直接操作できるのは主に戦闘前です。

- CommanderとSquadの位置
- Squad分割
- Formation
- Attack / Fire order
- Hold回数
- Mage Script
- Gem
- Bodyguard
- Retreat route

したがって、戦闘中の強さは、

> **Unit性能 × 配置 × 命令 × Research × Gem × 情報**

で決まります。

詳しい命令は[命令とBattle Script](orders.md)を参照してください。

---

# 防御層

| 層 | 主な要素 | 代表的な突破方法 | Replayで見ること |
|---|---|---|---|
| 接敵させない | 距離、Screen、Obstacle、移動速度 | Flying、射撃、Teleport、機動 | 誰が最初に接敵したか |
| 攻撃させない | Awe、Fear、Repel、拘束 | Morale、長武器、射撃、Mindless、AoE | 攻撃動作が中止されていないか |
| 命中させない | Defence、Displacement、Mirror Image | Attack、多段、Harassment、必中、AoE、拘束 | Missが多いか |
| Shieldで受ける | Parry、Shield Protection | 高Attack、盾対策、AoE、AP・AN | Shield Hitが多いか |
| Damageを軽減 | Protection、Elemental Resistance、Physical Resistance | 高Damage、AP、AN、別Damage type | 当たるがHPが減らないか |
| 致命傷を防ぐ | HP、Luck、Regeneration、Damage reversal系 | Burst、持続Damage、即死、回復阻害 | 一撃死か長期消耗か |
| 戦闘を続ける | Fatigue、Morale、Leadership、退路 | Fear、Fatigue、Commander kill、包囲 | 死亡より先にRoutしたか |

同じ「前衛が崩れた」という結果でも、原因が違えばCounterも違います。

---

# Dominions Random Number（DRN）

Dominionsの多くの対抗判定では、能力値に**DRN**を加えて比較します。

DRNは概念的には開放型2D6です。6が出たダイスは5として数え、さらに振り足します。振り足しでも6が出れば続きます。

この仕組みにより、能力値差は重要ですが、絶対保証にはなりません。

## 実戦上の意味

- 能力値1点の差は、繰り返される全判定へ効く
- 大差でも低確率事故は残る
- 攻撃回数が増えると、低確率の成功もいずれ発生する
- 高価な一体へ勝敗を集中すると、事故の損失が大きい
- 一回のReplayより複数回のTest battleが信頼できる

### 例

Attack 13がDefence 11へ有利でも、毎回命中するわけではありません。逆にAttack 10でも、十分な攻撃回数があれば高Defenceへ命中が発生します。

> **能力値差は確率を傾ける。攻撃回数はその確率を試す回数を増やす。**

この二つを分けて考えます。

---

# 戦場、Square、Size、Obstacle

戦場はSquareの集合として処理されます。Square内へ入れるUnit数、同時に攻撃できる数、AoEで巻き込まれる数はUnitのSizeと密集度に左右されます。

## 小型Unit

同じ前線幅へ多く並び、攻撃回数を増やしやすい一方、

- AoE
- Poison cloud
- Fire cloud
- Trample
- Battlefield-wide damage

へまとめて巻き込まれやすくなります。

## 大型Unit

一体ごとのHP・Strength・Damageが高い傾向がありますが、

- 前線へ並ぶ数が少ない
- 射撃の標的になりやすい
- MR攻撃を集中されやすい
- Surroundされやすい
- 一体の行動不能が戦力低下へ直結する

という交換条件があります。

## Effective front width

Armyの人数ではなく、**同時に敵へ届いている攻撃数**を見ます。

100人いても狭い通路で20人しか戦っていなければ、残りは待機しています。逆に少数のFormation Fighterや小型Unitが広い前線で同時攻撃すると、表示人数以上の圧力を出します。

## Battlefield Obstacle

Dominions 6ではBush、Rock、TreeなどのObstacleが戦場へ生成されます。

- 移動経路が曲がる
- Lineが分断される
- Fast Squadだけ先行する
- Rear attackの経路が変わる
- 大型Creatureが障害物を破壊する
- AoEでObstacleごと周辺へ影響する

同じ配置でも、戦場ごとに接敵Timingが変わります。Replayでは最初に戦場全体を見ます。

---

# Formation

Formationは見た目ではなく、**前線幅、密集度、接敵Timing、AoE耐性、統制**を変える機能です。

| Formationの方向 | 得るもの | 失いやすいもの |
|---|---|---|
| 深く密集 | 戦線の厚み、Commander周辺の防衛 | 前線参加人数、AoE耐性 |
| 広いLine | 同時攻撃数、包囲 | 障害物への弱さ、薄い箇所の突破耐性 |
| Sparse / Loose | AoE・射撃・Cloudの分散 | 局所密度、相互支援 |
| Skirmish | 最大限の分散 | Morale・統制・集中戦闘力 |

## Box

Commander護衛、少数精鋭、突破されにくい塊を作りたい場合に向きます。後列が接敵するまで時間がかかり、AoEへ密集します。

## Line

通常近接兵の出発点です。多くのUnitを同時に戦わせやすい一方、ObstacleやCombat Speed差で線が曲がります。

## Double Line

前線幅と厚みを両立しやすいFormationです。第一列が倒れたあとも接敵人数を維持したい場合に使います。

## Sparse / Loose

大AoE、Cloud、射撃、Trample被害を分散します。敵の局所突破へ弱くなるため、高価な少数兵を過度に散らさないようにします。

## Formationを選ぶ手順

1. 敵の主Damageが単体かAoEかを見る
2. 自軍は同時攻撃数と耐久のどちらを必要とするか決める
3. 速度が違う兵種を別Squadへ分ける
4. ReplayでLineが維持されたか確認する

Formation名を正解として覚えず、**実際の接敵形状**で評価します。

---

# 配置、命令、接敵Timing

戦闘の多くは、最初の近接攻撃より前に決まります。

## ScreenとDamage役を分ける

```text
前方：盾兵・Chaff・耐久兵
後方または側面：両手武器・Sacred・専門Counter
後方：Mage・Archer・重要Commander
左右後方：Attack Rear対策
```

Damage役を前へ置くと、

- 最初の射撃
- Lance Charge
- Repel
- Enemy debuff

を受けて仕事前に失います。

## HoldはTimingを交換する命令

Hold and Attackは安全命令ではありません。

得るもの:

- Buffの完成
- 敵を引き込む
- 速度の違うSquadを同期する

失うもの:

- 射撃を受けるRound
- Enemy Spellが進む時間
- Battlefield effectの蓄積時間

## Combat Speed差

同じ位置・同じ命令でも、Fast Unitは先に接敵します。

- Cavalryだけ前へ飛び出す
- Heavy Infantryが遅れる
- Summonが本隊から分離する
- BodyguardがCommanderへ追従できない

という問題が起こります。速度が役割を壊すならSquadを分けます。

---

# 攻撃を開始できるか：Awe、Fear、Repel、拘束

命中判定の前に、攻撃そのものが止められる場合があります。

## Awe

Aweを持つ相手へ近接攻撃するUnitは、攻撃を実行するためのMorale系判定を要求される場合があります。

### Aweへの回答

- 高Morale
- Berserk
- Mindlessなどの例外特性
- 多数の攻撃機会
- 射撃
- Spell
- Awe持ちを拘束・疲労させる

Awe相手へ低Morale Chaffだけを当てると、人数が多くても攻撃回数が生まれません。

## Fear

FearはDamageを直接与えなくても、Morale低下とRoutを通じて戦線を崩します。

### Fearへの回答

- 高Morale
- Leadership
- Sermon / Morale Buff
- Fear sourceの集中排除
- Undead・Mindless等の性質確認
- Squadを分けて崩壊を局所化

## Repel

より長い武器を持つ防御側は、接近して攻撃する敵をRepelできる場合があります。

Repelは、

1. 武器長
2. Repel側の攻撃判定
3. Repel攻撃の有効性
4. 攻撃側のMorale

を段階的に処理し、失敗した攻撃側の攻撃を中止させます。

### Repelが強い状況

- Pike / Great Spearなど長Weapon
- 高Attack
- 敵のWeaponが短い
- 敵Moraleが低い
- 敵の一撃が重く、攻撃回数が少ない

### Repelへの回答

- 同等以上のWeapon Length
- 高Morale
- 射撃・Spell
- 多段攻撃
- 拘束
- Repel側をHarassmentで疲れさせる

Repelの目的は必ずしもDamageではありません。**敵の攻撃回数を消し、後衛が働くRoundを増やす**ことです。

## Entangle、Earth Meld、Paralyze、Stun

拘束・麻痺・気絶は、敵のDamageを減らし、Defenceを機能しにくくし、集中攻撃を可能にします。

高HP・高Protectionの敵を正面から削るより、行動不能にしてから倒す方が効率的な場合があります。

---

# 近接命中：AttackとDefence

基本的な近接命中は、概念的に次の比較です。

```text
攻撃側：Attack Skill + 武器補正 + 状態補正 + DRN
防御側：Defence Skill + 状態補正 + DRN
```

攻撃側が上回れば通常は命中し、同値は防御側に有利です。

## Attack Skill

Attackは威力ではなく、**一撃を命中させる能力**です。

Attackの価値が高いUnit:

- 攻撃回数が少ない
- 一撃のDamageが大きい
- On-hit効果が重要
- Commander・Thugを狙う
- Repelを使う

## Defence Skill

Defenceは近接攻撃を回避する能力です。Protectionとは別です。

Defenceを下げる主な要因:

- Armor・Shield・WeaponのDefence penalty
- Fatigue
- Harassment
- Stun / Paralyze / Entangleなど
- 一部のDebuff

## Harassment

同じRoundに多数の攻撃を受けるUnitは、後続攻撃を避けにくくなります。

高Defence Unitへの代表的な回答は、Attackを数点上げることだけではありません。

- 小型Unitで囲む
- 多段攻撃
- Summonを重ねる
- Mirror Imageを剥がす
- 拘束してDefenceを落とす

という形で、**判定回数とDefence低下を同時に作る**方法があります。

## 多段攻撃

多段攻撃は、

- 高Defence
- Mirror Image
- Chaff
- On-hit効果

へ強い一方、各攻撃のDamageが低ければ高Protectionへ通りません。

```text
高Defence・低Protection
→ Attack / 多段 / 拘束

低Defence・高Protection
→ 高Damage / AP / AN / Armor破壊
```

と分けます。

---

# ShieldとParry

盾はProtectionを常時そのまま足す装備ではありません。

近接攻撃では、結果を理解用に三段階へ分けられます。

1. **Miss**：通常Defenceで回避
2. **Shield Hit**：Defenceだけでは避けられないがParry込みで受ける
3. **Clean Hit**：Parryも突破され、BodyまたはHeadへ通る

Shield HitではShield ProtectionがDamage軽減へ参加します。

## 射撃とShield

射撃では通常のDefence Skillより、

- 射手のPrecision
- 距離
- 対象Size
- Shield
- Air Shieldなどの効果
- Storm・Wind・Darkness

が重要です。

大盾は射撃Screenとして非常に有効ですが、重量によってDefence・Encumbranceへ不利を持つ場合があります。

## Shieldの交換条件

| 装備 | 得るもの | 失いやすいもの |
|---|---|---|
| 小盾 | 軽いParry、機動性 | 高いShield Protection |
| 大盾 | 射撃防御、Shield Hit耐久 | Defence、Fatigue効率 |
| 盾なし両手武器 | Damage、Length | Parry、射撃耐性 |
| 複数武器 | 攻撃回数 | 盾、二刀Penalty |

詳しくは[両手武器・片手武器・盾](weapons-and-shields.md)を参照してください。

---

# Damage処理の流れ

攻撃が命中したあと、概念的には次を処理します。

```text
攻撃の基礎Damageを決める
        ↓
Hit location・Shield Hitを決める
        ↓
AP / AN / Damage typeを適用する
        ↓
Protection・Resistanceで軽減する
        ↓
HP Damage・Fatigue Damage・状態効果を適用する
        ↓
Affliction・死亡・Regeneration等を処理する
```

## 概念式

通常Damageは理解用に次のように考えられます。

```text
最終HP Damage ≒ Damage側の値 + DRN - Protection側の値 - DRN
```

0以下なら通常はHP Damageになりません。ただしSpell、Poison、Fatigue、MR効果などは別の処理を持ちます。

## 近接Damageの材料

- UnitのStrength
- Weapon固有Damage
- 片手 / 両手のStrength利用
- Charge
- Bless
- Spell
- Item
- Affliction・状態補正

表示Damageだけでなく、**命中率と攻撃回数を掛けた実効Damage**を見ます。

---

# Protection

Protectionは命中後のDamageを軽減します。

主な構成要素:

- Natural Protection
- Body Armor
- Helmet
- Shield Protection（Shield Hit時）
- Spell・Bless・Item

Natural ProtectionとArmor Protectionは、常に単純加算されるわけではなく、組み合わせに逓減があります。

## HeadとBody

攻撃はHeadまたはBodyへ命中します。

- Body Armorは高いがHelmetが弱い
- Helmetは強いが胴体が薄い
- Shield HitならShield Protectionが加わる

という違いがあります。

表示上の平均Protectionだけでなく、装備内訳を確認します。

## Protectionが強い相手

Protectionは低～中Damageの多数攻撃へ特に強くなります。

- Militiaの短剣
- 低Strengthの多段攻撃
- 低Damage Bow
- 弱いSummon

は命中してもHPを減らせない場合があります。

## Protectionへの回答

- 高Strength・高Damage
- 両手武器
- Piercing
- Armor Piercing
- Armor Negating
- Armor破壊
- Poison
- MR攻撃
- Fatigueで眠らせる

---

# Armor Piercing、Armor Negating、Magic Weapon

この三つを混同しないことが重要です。

## Armor Piercing（AP）

Protectionの一部だけを計算へ使います。高Protectionへ有効ですが、鎧が完全に消えるわけではありません。

## Armor Negating（AN）

通常のProtectionを無視します。Shock系など、重装備の価値を大きく迂回する攻撃に見られます。

## Magic Weapon

Magic Weaponは、Etherealなど魔法武器を要求する防御や一部の特殊対象へ対応する性質です。

> **MagicだからAP・ANとは限らず、AP・ANだからMagic Weaponとは限りません。**

Weapon・Spellの属性を個別に確認します。

---

# Slash、Pierce、Blunt、Untyped

物理Damage typeは、Protection計算や対応Resistanceとの相性を変えます。

## Slashing

Protectionを抜いた後の殺傷力が高くなりやすいDamage typeです。肉体へDamageが通る相手に向きます。

## Piercing

Armorに対してProtectionを一部減らす性質を持ちます。CrossbowなどのAPと組み合わさると、高Protectionへの一般兵Counterになります。

## Blunt

Head Hitや盾への圧力で価値が出るDamage typeです。Skeleton、Statue、PlantなどはPhysical Resistanceが異なるため、対象の能力を確認します。

## Untyped

Slash / Pierce / Blunt固有の補正を持たない代わりに、それら専用Resistanceの対象外になります。

## Physical Resistance

Slash、Pierce、Blunt Resistanceは、対応する物理Damageをさらに軽減します。

高Protectionだけを見て武器を選ぶと、対応Resistanceで止められることがあります。

---

# Ethereal、Mirror Image、Displacement

これらはすべて「避ける防御」ですが、同じではありません。

## Ethereal

通常武器の攻撃を高確率で無効化する防御です。Magic WeaponやSpellが基本的な回答になります。

## Mirror Image

攻撃を受けることで像が消費されるタイプの防御です。多段攻撃、射撃、低Cost攻撃で像を剥がしてから本命を当てます。

## Displacement系

命中そのものをずらす・失敗させる防御です。Attack、必中、AoE、拘束などで回答します。

### 共通の誤解

高Damage一撃が強くても、命中段階で無効化されればDamage判定へ進みません。

> **Damageを上げる前に、攻撃がDamage段階へ到達しているかを見る。**

---

# Elemental Resistance

Fire、Cold、Shock、Poison、Acidなどには対応するResistanceがあります。

Dominions 6ではResistanceは、一定量の軽減に加えて、残ったDamageの割合も軽減します。そのため低～中Damageの多段攻撃へ特に強く、十分なResistanceは実質的な無効化に近づきます。

## Resistanceを評価する手順

1. 敵の主Damage typeを特定する
2. 単体ItemかArmy-wide Spellかを選ぶ
3. Buffが接敵前に入るか確認する
4. 敵が別Damage typeへ切り替えられるか考える
5. ReplayでResistance後のDamageを確認する

## Resistanceへの回答

- 別Element
- 通常物理
- AP / AN
- MR攻撃
- Poison以外の持続Damage
- Buff Casterの排除

一種類のElemental Damageだけに依存するArmyは、Ward系Spell一つで機能を失う場合があります。

---

# HP、Regeneration、Luck、Affliction

Protectionを抜いたあとも、Unitは同じ耐久ではありません。

## HP

高HPは、

- 大きな一撃
- AoE
- AN Damage
- MRを通った非即死Damage

への最後の余裕になります。ただしHPが高いだけでは、Fatigue、Soul effect、Control、Diseaseを防げません。

## Regeneration

RegenerationはRoundをまたいでHPを回復します。

強い状況:

- 小Damageを繰り返し受ける
- 戦闘が長い
- Protection・Resistanceも高い

弱い状況:

- 一撃死
- 回復量を超える集中Damage
- 即死・Control
- Disease・Decayなどの長期的問題

## Luck

Luckは致命的なDamageを無効化する機会を作りますが、永続的な無敵ではありません。攻撃回数を増やし、判定を繰り返すことで突破されます。

## Affliction

生存しても、

- Limp
- Lost eye
- Chest wound
- Feebleminded
- Disease

などのAfflictionが残れば、戦略的には大きな損失です。

高価なCommander、Pretender、Thugは勝敗だけでなく、**戦後に継続使用できるか**を評価します。

---

# Poison、Fatigue Damage、状態異常

HPを直接削る通常Damageだけが勝利手段ではありません。

| 効果 | 主に攻撃する層 | 防御・回答 |
|---|---|---|
| Poison | Protectionの外側、時間 | Poison Resistance、短期決着、回復 |
| Fatigue Damage | 行動継続 | Reinvigoration、Relief、Caster排除 |
| Stun / Paralyze | 行動・Defence | MR・Resistance・分散・解除 |
| Entangle / Earth Meld | 移動・Defence | Strength、解放、射撃、別Target |
| Fear | Morale | Morale Buff、Leadership、Source排除 |
| Decay / Disease | 長期耐久 | Resistance・治療・短期運用 |
| Charm / Enslave | MR・Control | MR、Penetration対策、Mindless、Caster排除 |

## Poison

Poisonは遅れてDamageが現れるため、接敵直後に強く見えたArmyが戦闘後半で崩れることがあります。

Replayでは、

- Poisonが入ったRound
- 蓄積量
- Poison Resistance
- 戦闘が長引いた原因

を見ます。

## Fatigue Damage

Fatigue Damageは高Protectionへも有効です。敵を即死させなくても、100以上へ追い込み気絶させれば、通常攻撃で処理しやすくなります。

## Stun / Paralyze

行動を奪う効果は、敵のDamageを0へ近づける防御でもあります。高価な少数精鋭ほど、一体の行動不能が大きな割合の戦力を失わせます。

---

# 射撃戦

射撃の命中・被害には主に次が関わります。

- Precision
- WeaponのPrecision補正
- 距離
- 対象Size
- Shield
- Air Shield
- Storm、Wind、Darkness
- Target order
- AoE
- 味方と敵の接触位置

## 射撃の役割

| 射撃 | 向く相手 | 注意 |
|---|---|---|
| Bow | 軽装、Chaff、接敵前の削り | 高Protection、盾 |
| Crossbow / Arbalest | 高Protection | 発射間隔、Friendly Fire |
| Sling | 安価な面制圧 | 重装相手のDamage不足 |
| Javelin | 接敵前の一斉射撃、Strength活用 | 射程、弾数 |
| AoE Spell / Weapon | 密集Square | 味方巻き込み、Resistance |

## Friendly Fire

射撃は外れたときに近隣Squareへ飛び、接敵後は味方へ当たる可能性があります。

Replayでは敵Kill数だけでなく、

- 自軍へ当たった弾
- Damage役が射線を塞いだRound
- Fire orderが適切だったか
- 接敵後も射撃を続ける価値があったか

を確認します。

## 射撃への回答

- Shield
- Sparse Formation
- Air Shield / Arrow protection
- Fast attack / Flying
- Storm
- Battlefield obstacle
- 射手Commanderの排除
- 接敵Timingの短縮

---

# Area of Effectと密集度

AoEは単体Damageの大きさだけでなく、**一発で何HP・何Unitへ判定を作るか**で評価します。

小型Unitが密集しているSquareは、AoE一発の価値が高くなります。

## AoEに強くする方法

- Sparse / Loose Formation
- Squadを分ける
- 高価なUnitを一箇所へ集中しすぎない
- Resistanceを事前に入れる
- Casterへ早く圧力をかける
- Battlefield-wide SpellのCasterを狙う

## AoEの交換条件

- Friendly Fire
- Precision
- Range
- Gem
- Caster Fatigue
- Resistanceで無効化されるRisk

「AoEが大きいから強い」ではなく、敵の密集度と味方の巻き込みを含めて判断します。

---

# Magic Resistance（MR）

MRはProtectionとは別の防御です。

Soul、Mind、Control、Paralyzeなど、Spellや能力に`MR Negates`等が付く場合に使われます。

## MR判定を読む

確認するもの:

- MR Negatesか
- MR Negates Easilyなどの差
- CasterのPenetration
- TargetのMR
- Antimagic等のBuff
- Mindless・Magic Being等の対象条件
- AoEと試行回数

## Penetration

PenetrationはMRを突破しやすくします。

- Caster能力
- Path
- Item
- Spell固有補正
- Scale・Battlefield effect

などが関わります。

## MR攻撃の向く相手

- 高Protection・低MR
- Giant・Monsterで一体の価値が高い
- RegenerationやPhysical Resistanceが厚い
- 通常武器で時間がかかる

## MR攻撃への回答

- MR Buff
- Antimagic
- Mindless等の性質
- Caster assassination
- 分散
- 安価なTargetを前へ出す
- Protectionを狙う通常Damageへ敵を切り替えさせる

MR攻撃一本に依存すると、Antimagicや対象免疫でArmy全体が止まります。

---

# Spellcasting、Gem、Battlefield Enchantment

MageはPathを満たすだけでは戦力になりません。

```text
Research
＋ Path
＋ Gem
＋ Range
＋ Target
＋ Cast time
＋ Fatigue
＋ 生存時間
```

が揃って初めて予定Spellが働きます。

## Scriptが不発になる主な理由

- Research不足
- Path不足
- Gem不足
- Target不在
- Range外
- Casterが接敵・Stun・Silence・死亡
- Fatigue過多
- AIが条件に合う別Spellを選ぶ
- Battlefield条件が変化

## Gem

Gemは、

- 必須Cost
- 一時的Path boost
- Fatigue軽減
- AIのSpell選択

へ影響します。

多く持たせるほど安全とは限りません。不要なSpellへ消費したり、死亡・Retreatで失うRiskがあります。

## Battlefield Enchantment

戦場全体へ作用するSpellの一部は、Casterが死亡・退場すると解除されます。

Casterには、

- 後方中央配置
- Bodyguard
- Arrow対策
- Flying / Attack Rear対策
- Retreat route
- 予備Caster

を用意します。

相手の勝利条件が一人のCasterに依存するなら、そのCasterを倒すことが最短Counterです。

---

# Fatigue

Fatigueは戦闘の時間資源です。

## 主な発生源

- 移動
- 近接攻撃
- Armor Encumbrance
- Spellcasting
- Heat / Cold環境
- Aura
- Fatigue Damage
- Communion / Sabbath
- 一部の特殊能力

## Fatigueの影響

Fatigueが増えると、

- Attackが不利になる
- Defenceが不利になる
- Repelが機能しにくくなる
- Armor-defeating hitを受けやすくなる
- 行動頻度が落ちる
- 100以上で気絶する
- 極端な蓄積はHP損失へつながる

Protection 30でも、眠ったまま囲まれれば安全ではありません。

## 重装兵

重装兵は短期の通常物理戦へ強く、長期戦で弱点が出ます。

- Chaff
- Skeleton
- Summon
- Fatigue Spell
- Heat
- Fearと長期拘束

で戦闘を延長すること自体がCounterになります。

## Mage

Spell Fatigueは、要求Pathより高いPath、Gem、Reinvigoration等で管理できます。一方、Armor Encumbranceは別の負担になります。

Mage一人の価値は、Pathの高さだけでなく、

> **予定Spellを何回使い、何Roundまで生存したか**

で評価します。

## Fatigueへの回答

- Reinvigoration
- Relief
- Summon Earthpower等
- 軽装化
- Caster数を増やし役割分担
- 戦闘を短くする
- Chaff処理を用意する
- Enemy Fatigue sourceを倒す

---

# Morale、Leadership、Rout

UnitはHPが0になるまで戦うとは限りません。

Moraleは、

- Squadの損害
- Army全体の損害
- Fear
- Commander死亡
- Leadership
- Fatigue
- 特殊効果

などによって試されます。

## Squadを分ける意味

一つの巨大Squadは管理しやすい一方、一度のMorale崩壊が大人数へ波及します。

小さく分けると崩壊を局所化できますが、

- Leadership
- Commander数
- Squad bonus
- 操作量

が必要です。

## Commander死亡

Commanderを失うと、

- Leadership
- Battle Script
- Battlefield Enchantment
- Retreat制御
- ArmyのMorale

を同時に失う場合があります。

前衛のHPだけでなく、後方のCommander防御もArmy耐久の一部です。

## Berserk、Mindless、Undead

通常のMorale挙動と異なるUnitがあります。

- Berserk後は逃げにくいが、制御も失う
- Mindlessは精神効果へ強い一方、Leadership条件が特殊
- Undead・Demonは指揮とBanishment等のCounterが異なる

Unitの属性を確認し、通常人間兵と同じMorale対策を当てないようにします。

---

# RoutとRetreat route

Routは即死亡ではありません。戦場から離脱したUnitは退却を試みます。

しかし、

- 退却可能な隣接自領がない
- 敵領の奥へ侵入した
- Plane・地形・移動条件が合わない
- Retreat先が敵に取られた

場合、Routが大量死へ変わります。

## 戦闘前の確認

```text
負けた場合、どこへ逃げるか
Commanderと兵士は同じ場所へ逃げられるか
退却先は今Turnも自領か
Fortへ戻れるか
別Planeへ閉じ込められないか
```

Battle Scriptの一部としてStrategic Map上の退路を設計します。

---

# Mounted Unit

Dominions 6ではRiderとMountが別のStats・HPを持ちます。

- RiderだけがDamageを受ける
- MountだけがDamageを受ける
- AoEで双方がDamageを受ける
- Mountが死亡し、Riderが徒歩で戦闘を続ける
- Mount側のWeapon・Armor・能力が使われる

という状況があります。

## Mounted Unitを読む手順

1. RiderのHP・Defence・Weaponを見る
2. MountのHP・Size・Attackを見る
3. Bardingを確認する
4. Lance Charge後の継続武器を見る
5. Dismount後のStatsとCombat Speedを見る

表示HP一つだけで総耐久を判断しません。

## Mounted UnitへのCounter

- Pike / 長Weapon
- 射撃
- Earth Meld等の拘束
- MountとRiderを巻き込むAoE
- Fatigue
- LanceをScreenへ使わせる
- Magic Bardingに対応するDamage type

---

# TrampleとSize差

Trampleは通常の武器交換と異なる、移動を伴う特殊攻撃です。大きなUnitが小さなUnitのSquareへ進み、Damageと陣形破壊を発生させます。

## Trampleが強い状況

- 小型Unitが密集
- 前線が薄い
- Moraleが低い
- Tramplerが高HP・高Protection
- 後衛へ到達すると価値が高い

## Trampleへの回答

- 同等以上のSize
- Sparse Formation
- 高Defence
- Pike・高Damage
- 射撃
- 拘束
- Fatigue
- TramplerのMoraleを崩す

Protectionが高い小型兵でも、Trampleでは通常の正面戦と異なる損失が出ます。

---

# 戦闘例：防御層で考える

## 例1：盾重装兵がCrossbowで減る

症状:

- Bowには耐える
- Crossbowで少しずつ死ぬ
- 接敵後は自軍が勝つ

診断:

- ShieldとProtectionは機能している
- しかしPiercing / APと高Damageが一部を突破している
- 接敵までのRoundが長い

変更候補:

- 前方配置
- Sparse
- Fast flank
- Air Shield
- 射手を狙う命令

「もっとProtectionを上げる」だけが回答ではありません。

## 例2：高Defence Sacredへ攻撃が当たらない

症状:

- 自軍のDamageは十分
- Hitしたときは倒せる
- 大半がMiss

診断:

- 問題はDamage層ではなく命中層

変更候補:

- Attack Buff
- 多段攻撃
- ChaffでHarassment
- Entangle / Earth Meld
- AoE
- Mirror Imageを剥がす射撃

## 例3：高Protection ArmyがPoisonで崩れる

症状:

- 接敵直後はほぼ無傷
- 戦闘後半で連続死亡
- Armorを増やしても改善しない

診断:

- Protection層は機能している
- Poisonが別経路で蓄積
- 戦闘が長すぎる

変更候補:

- Poison Resistance
- Short battle
- Caster kill
- Chaff処理
- Nature access

## 例4：Mageが多いのにBuff前に負ける

症状:

- 予定Spellは研究済み
- MageもGemも存在
- 前衛がRound 2で接敵
- Army BuffはRound 3以降

診断:

- Spell性能ではなくTimingの失敗

変更候補:

- 前衛を後ろへ下げる
- Screenを追加
- Self Buffを減らす
- Mageを役割分担
- Holdを調整

---

# 症状からCounterを選ぶ

| 症状 | 破られた層 | 最初に試す変更 |
|---|---|---|
| 攻撃動作が出ない | Awe / Repel / Fear | Morale、長Weapon、射撃、Spell |
| 攻撃が当たらない | Defence / Image | Attack、多段、拘束、AoE |
| Shield Hitばかり | Shield | 高Attack、盾対策、AoE、AP・AN |
| 当たるがHPが減らない | Protection / Resistance | 高Damage、AP・AN、別Damage type |
| 序盤は耐えるが後半崩れる | Fatigue / Poison / Morale | Reinvigoration、Resistance、短期決着 |
| 少数精鋭が雑兵に止められる | 攻撃回数 / Fatigue | AoE、援護、Reinvigoration |
| Mageが予定Spellを使わない | Script条件 | Research、Path、Gem、Range、Target確認 |
| Battlefield Spellが消える | Caster生存 | Bodyguard、配置、予備Caster |
| 死亡前に全軍が逃げる | Morale / Leadership | Morale、Commander保護、Squad再編 |
| Rout後に大量消失 | Retreat route | 戦略移動と退却先を修正 |
| 騎兵が接敵後急に弱い | Charge後 / Mount損失 | 継続武器、Dismount、撤退Timing確認 |
| 小型前衛が一気に崩れる | Trample / AoE | Size、Sparse、拘束、射撃 |

---

# Battle Replayの分析手順

詳細は[Battle Replayの読み方](../getting-started/battle-replay.md)を参照してください。戦闘ルールを確認するときは、最低限次を見ます。

1. **戦闘前の仮説**：誰が受け、何が倒す予定だったか
2. **接敵形状**：FormationとObstacleでどう変わったか
3. **攻撃機会**：Awe・Repel・拘束で攻撃が止まったか
4. **命中**：Miss、Shield Hit、Clean Hitのどこで止まったか
5. **Damage type**：Slash / Pierce / Blunt / Fire / Shock / Poison / MR等
6. **Fatigue**：前衛とMageがいつ100へ達したか
7. **Caster**：予定Spell、Gem、Range、死亡Round
8. **Morale**：最初のRoutと引き金
9. **退路**：逃げたUnitが生存できたか
10. **次の変更**：一つだけ変えて再Testする

## 一つだけ変える理由

配置、兵種、Spell、Gemを全部同時に変えると、何が改善したか分かりません。

```text
Test 1：配置だけ変更
Test 2：Resistanceだけ追加
Test 3：Target orderだけ変更
```

のように差を見ます。

---

# よくある誤解

## 「Protectionが高ければ硬い」

通常物理には硬くても、AN、Poison、MR、Fatigue、Controlには別の防御が必要です。

## 「Magic attackはArmorを無視する」

Magic Weapon、AP、ANは別属性です。

## 「Damageが高ければ勝てる」

命中しない、Shieldで受けられる、攻撃前にRepelされるならDamage段階へ到達しません。

## 「多段攻撃は高Protectionにも強い」

各攻撃のDamageが低ければ全て弾かれます。

## 「Defenceが高ければ射撃も避ける」

射撃ではPrecision、距離、Size、Shield、戦場効果が重要です。

## 「勝ったReplayは見る必要がない」

敵Script不発やDRNに助けられただけかもしれません。再現可能な部分と偶然を分けます。

## 「CasterがSpellを発動したら仕事は終わり」

一部のBattlefield EnchantmentはCaster生存へ依存します。

## 「Routしただけなら損失は少ない」

退路がなければRoutが全滅へ変わります。

---

# 記事の検証範囲と今後の分離

この総合ページは、戦闘全体を一度に理解するための基準記事です。

次の項目は、個別の厳密記事へ分離する価値があります。

- DRNと対抗判定の確率表
- Shield Hitと射撃Shield
- Natural ProtectionとArmorの合成
- AP・AN・物理Damage type
- Repelの全判定
- Fatigue閾値と回復
- Morale・Army Rout・Retreat
- MountedとTrample
- Elemental Resistanceの正確な軽減

個別記事が追加されても、このページは全体像と実戦診断の入口として残します。

---

## 関連ページ

- [命令とBattle Script](orders.md)
- [両手武器・片手武器・盾](weapons-and-shields.md)
- [Battle Replayの読み方](../getting-started/battle-replay.md)
- [初心者向けTips](../getting-started/beginner-tips.md)
- [魔法の基本](../magic/index.md)
- [GemとCombat Gem](../magic/gems.md)
- [Communion・Sabbath](../magic/communions.md)
- [Combat data索引](../data/combat/index.md)
- [武器データ](../data/combat/weapons/index.md)
- [防具データ](../data/combat/armor/index.md)
- [Weapon property・Damage type](../data/combat/weapon-properties.md)
- [特殊Damage・状態効果](../data/combat/special-damage.md)

## 主な情報源

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
- Dominions 6.35ゲーム内Tooltip・Battle Replay
- このWikiの6.35固定Weapon・Armor・Spellデータ

!!! note "記事状態"
    本文の構造、主要防御層、Dominions 6固有のObstacle・Mount・Resistance変更、主要な実戦診断は6.35を対象にレビューしています。すべての特殊Weapon・Spell・Unit能力の内部例外を実験で証明した状態ではないため、記事Statusは`reviewed`としています。
