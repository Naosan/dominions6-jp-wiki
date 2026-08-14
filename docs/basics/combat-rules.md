---
title: 戦闘ルール
status: expanding
verified_version: "6.35"
last_verified: "2026-08-14"
---

# 戦闘ルール

Dominions 6の戦闘を、**命中・防御・Damage・Fatigue・Morale・配置**の順に整理します。

Dominionsの戦闘は、単純な「攻撃力－防御力」ではありません。攻撃を受ける側には複数の防御層があり、それぞれを突破する手段が異なります。

| 防御層 | 主な能力 | 主な突破方法 |
|---|---|---|
| 攻撃させない | Awe、Fear、Repel、足止め | Morale、長武器、射撃、魔法 |
| 命中させない | Defence、Mirror Image、Displacement | Attack、手数、必中・範囲攻撃、拘束 |
| 盾で受ける | Shield Parry | 高Attack、盾無視、Flail系、範囲攻撃 |
| Damageを軽減 | Protection、Resistance | 高Damage、AP、AN、対応外のDamage type |
| 致命傷を防ぐ | HP、Luck、Regeneration | Burst damage、持続Damage、即死・MR攻撃 |
| 戦闘継続 | Morale、Fatigue管理 | Fear、損害、Fatigue damage、長期戦 |

攻略上は、相手の全防御を正面から上回る必要はありません。**最も薄い層を攻撃する**のが基本です。

---

## Dominions Random Number（DRN）

Dominionsの多くの判定では、能力値に **DRN** を加えて比較します。

DRNは概念的には「開放型2D6」です。各ダイスで6が出た場合、その6を5として扱い、さらに振り足します。振り足しでも6が出れば続きます。

このため、能力値差が大きくても絶対に安全とは限りません。

### 攻略上の意味

- 能力値1点の差は、毎回の判定へ継続して効く
- しかし極端な出目で番狂わせが起こる
- 一回だけの決闘より、数十・数百回判定される集団戦の方が能力値差は安定して表れる
- 「勝率が高い」と「絶対に勝つ」は別

高価なCommander一体へ勝敗を依存させる構成では、低確率事故も無視できません。

---

## 戦場、Square、Size

戦場はSquareの集合として処理されます。一つのSquareに入れるUnit数はSizeによって変わり、密集度は次の要素へ影響します。

- 一度に接敵できる人数
- 範囲攻撃一発で巻き込まれるHP・Unit数
- 巨大Unitによる押し出しやTrample
- 後列のUnitが前へ出るまでの時間
- 狭い場所や障害物での詰まり方

### 小型Unit

同じSquareへ多く入れるため、前線の手数を増やしやすい一方、AoE攻撃や雲・毒・爆発にまとめて巻き込まれやすくなります。

### 大型Unit

一体あたりのHPとDamageが高い傾向がありますが、前線へ並べる数が少なく、包囲・射撃・MR攻撃を集中されやすい場合があります。

### Dom6固有の注意

Dominions 6では戦場にBush、RockなどのObstacleが生成されます。大型Creatureが障害物を破壊できる場合もあり、同じArmy同士でも戦場によって接敵速度や陣形維持が変わります。

---

## Formation

Formationは「見た目」ではなく、**前線幅、密集度、Morale、移動効率、AoE耐性**を調整する機能です。

### Box

部隊をまとまりとして扱いやすく、正面突破やCommander護衛に向きます。ただし後列が接敵するまで時間がかかり、範囲攻撃へ密集しやすくなります。

### Line

前線幅を広く取り、多くのUnitを同時に戦わせやすいFormationです。近接兵の基本候補ですが、戦場の端・障害物・異なるCombat Speedによって崩れることがあります。

### Double Line

Lineより奥行きを残しながら前線を広げます。非常に薄いLineで突破されるのを避けたい場合や、第一列が倒れた後も接敵人数を保ちたい場合に使います。

### Sparse / Loose系

Unit間隔を広げ、射撃・AoE・雲への被害を分散します。一方、同じ前線幅での密度が下がり、突破されやすくなる場合があります。

### Skirmish

広く散開します。射撃や大AoEへの被害分散には役立ちますが、Morale面や部隊統制に不利があります。Undisciplined Unitは命令・Formationに制約を受けます。

### 実戦の基準

- 通常近接兵：LineまたはDouble Lineから試す
- 射撃・AoEが怖い：Sparse / Skirmishを検討
- 高価な少数兵：過度に散らして各個撃破されないよう注意
- Bodyguard：Commanderへ近いBox
- 速度が違う兵種：別Squadに分ける

---

## 接近戦の命中判定

基本的な近接命中は、次の比較です。

```text
攻撃側：Attack Skill + 武器補正 + 各種補正 + DRN
防御側：Defence Skill + 各種補正 + DRN
```

攻撃側が防御側を上回ると、通常は命中します。同値は防御側有利です。

### Attack Skill

Attackは「当たった後の威力」ではなく、**攻撃を命中させる能力**です。高Damageの両手武器でも、Attackが低ければ高Defenceの敵へ空振りします。

Attackを上げる価値が高いUnitは次です。

- 一撃が重い
- 強力なOn-hit効果を持つ
- 攻撃回数が少ない
- 敵CommanderやThugを狙う
- Repelを活用する長武器兵

### Defence Skill

Defenceは近接攻撃を避ける能力です。Protectionとは別物で、射撃に対して通常のDefenceは主要防御になりません。

Defenceは次によって下がります。

- ArmorやShieldのEncumbrance・Defence penalty
- Fatigue
- Harassment
- 拘束・麻痺・気絶
- 一部のDebuff

高Defence兵でも、多数の攻撃を短時間に受けるとHarassmentで回避力が低下します。したがって、**手数と包囲は高Defenceへの現実的なCounter**です。

---

## ShieldとParry

盾は単純にProtectionを常時加える装備ではありません。

近接攻撃では、Defenceだけなら避けられなかったものの、Shield Parryを含めれば防げた場合に**Shield Hit**になります。Shield Hitでは盾のProtectionがDamage計算へ加わります。

つまり結果は三段階です。

1. 攻撃側がDefence＋Parryを上回る：Clean Hit
2. Defenceは上回るがDefence＋Parryを上回れない：Shield Hit
3. Defenceも上回れない：Miss

### 射撃に対する盾

射撃では通常のDefenceより、Size、射手のPrecision、距離、Shield Parryなどが重要になります。大盾は接近戦だけでなく、弓・Crossbowへの前衛として価値があります。

### 盾の交換条件

盾はParryとProtectionを提供しますが、重量によってDefenceやEncumbranceへ不利を与える場合があります。

- 小盾：軽く、機動性を保ちやすい
- 大盾・Tower Shield：射撃・盾受けに強いが重い
- 盾なし両手武器：Damageと武器長を得やすいが、射撃と通常攻撃への生存性を失う

詳しくは [両手武器・片手武器・盾](weapons-and-shields.md) を参照してください。

---

## DamageとProtection

攻撃が命中すると、概念的には次のようにDamageとProtectionの双方へDRNを加えて比較します。

```text
最終Damage ≒ 攻撃側のDamage + DRN -（対象Protection + DRN）
```

0以下なら通常はHP Damageを与えません。

### 近接Damage

多くの近接武器では、表示Damageは次の要素で決まります。

- UnitのStrength
- 武器固有Damage
- 両手武器によるStrength寄与
- Charge bonus
- Bless、Spell、Item、Afflictionなどの補正

高Strength Unitほど両手武器の価値が上がりやすくなります。

### Protection

Protectionは命中後のDamageを軽減します。

- Natural Protection
- Armor Protection
- Shield Protection（Shield Hit時）
- Spell・Bless・Itemによる補正

Natural ProtectionとArmor Protectionは単純加算ではなく、組み合わせると逓減があります。Shield ProtectionはShield Hit時に別枠で加わります。

### HeadとBody

通常の攻撃ではHeadまたはBodyへ命中します。Helmetが弱いUnitは低確率のHead Hitで大Damageを受けることがあります。AoE攻撃ではキャラクター画面の平均Protectionが参照される場合があります。

### Armor-defeating hit

Protection側の出目が極端に悪いと、Protectionが一部低下するArmor-defeating hitが起こります。Fatigueが高いUnit、気絶・拘束されたUnitはこの危険が増えます。

このためProtection 30でも、Fatigue 100で眠ったまま殴られ続ければ安全ではありません。

---

## Armor PiercingとArmor Negating

### Armor Piercing（AP）

対象Protectionの一部だけを計算へ使います。高Protectionへ有効ですが、Protectionが完全に消えるわけではありません。

### Armor Negating（AN）

Protectionを無視します。代表的にはShock系に多く、Earth Buffや重装甲へ非常に強力です。

### 重要な区別

- **Magic Weapon**：Etherealや一部の魔法防御へ対応する性質
- **Armor Piercing**：Protectionを部分的に無視
- **Armor Negating**：Protectionを完全に無視

「魔法攻撃だから鎧を無視する」とは限りません。Spell説明のDamage属性を確認してください。

---

## Slash、Pierce、Blunt、Untyped

物理Damage typeにも役割があります。

### Slashing

Protection計算後のDamageを増やしやすく、肉体へ通ったときの殺傷力が高いDamage typeです。盾を傷める能力にも優れます。

### Piercing

対象Protectionの一部を減らして計算します。Armor Piercingと組み合わさるCrossbowなどは、高Protectionへの一般兵Counterになります。

### Blunt

Head Hitで威力が上がり、盾を傷める用途もあります。Skeleton、Constructなど相手側のPhysical Resistanceとの相性も確認します。

### Untyped

固有ボーナスはありませんが、Slash / Pierce / Blunt Resistanceの対象になりません。

### Physical Resistance

Slash、Pierce、BluntへのResistanceは、対応するDamageをProtection計算後に軽減します。したがって、高Protection＋Physical Resistance＋Regenerationの組み合わせは、通常物理へ極めて強くなります。

---

## Weapon LengthとRepel

より長い武器を持つ防御側は、攻撃してくる相手をRepelできる場合があります。

Repelは単なる先制攻撃ではなく、概ね次の段階を通ります。

1. 武器長を比較する
2. 防御側がAttack系判定でRepelを試みる
3. 攻撃側がMorale判定に失敗すると攻撃を中止する

Repelが成立した場合、攻撃そのものを防ぎ、相手へHarassmentを蓄積できます。

### Repelが向く状況

- 敵武器が短い
- 敵Moraleが低い
- 自軍のAttackが高い
- PikeやHalberdを多数並べる
- 高Damageだが攻撃回数の少ない敵を止める

### Repelが弱い状況

- 相手も長武器
- 高Morale・Mindless
- 射撃やSpell
- 武器長を問わない特殊攻撃
- 多数の小攻撃でRepel側がHarassmentを受ける

Repelだけで敵を倒すのではなく、**敵の攻撃回数を減らして後衛火力が働く時間を作る**と考えます。

---

## 射撃戦

射撃の命中には主に次が関わります。

- 射手のPrecision
- 武器のPrecision補正
- 距離
- 対象Size
- Shield
- Storm、Wind、Darknessなどの戦場効果
- 発射物・Spell固有のAoE

射撃は敵前衛だけでなく、外れた弾が近くのSquareへ飛ぶため、Friendly Fireが発生します。

### 一般的な使い分け

- Bow：軽装・大量Chaffへ
- Crossbow / Arbalest：高Protectionへ。ただし射撃間隔とFriendly Fireに注意
- Sling：安価な面制圧。高Protectionには弱くなりやすい
- Javelin：接敵前の一斉射撃とStrengthの活用
- AoE Spell：密集Squareへ。自軍前衛を巻き込む可能性あり

射撃部隊は「Fire Closest」だけでなく、Large Monster、Cavalry、Archersなどの優先目標を敵構成に応じて設定します。

---

## Elemental Resistance

Fire、Cold、Shock、Poison、Acidなどには対応するResistanceがあります。

Dom6ではResistanceは、一定値をDamageから差し引くだけでなく、残ったDamageも割合軽減します。このためResistanceは低～中Damageの多段攻撃に特に強く、十分に高いResistanceはほぼ無効化に近づきます。

### 攻略上の基準

- 敵の主力Damage typeを一つ確認する
- 自軍全体へResistanceを付与できるか調べる
- Resistanceを用意して、敵味方へ作用するBattlefield Spellを使う
- 相手がResistanceを積んだら、別Damage typeへ切り替える

一種類のElemental Damageだけに依存するArmyは、Ward系Spellで急に機能しなくなることがあります。

---

## Magic Resistance（MR）

MRはProtectionとは別の防御能力です。

Soul Slay、Paralyze、Charm、Enslave、各種Mind effectなど、MR判定を要求する効果に使われます。Spellごとに「MR Negates」「MR Negates Easily」などの表示を確認します。

### Penetration

Caster側のPath、Spell、Item、Scale、各種Bonusによって、MRを突破しやすさが変わります。

### 攻略上の見方

- 高Protection・低MR：Astral、Death、Glamour系のMR攻撃候補
- 低Protection・高MR：通常DamageやElemental Damage候補
- Mindless：Mind effectに強いが、Leadershipや特殊Counterを持つ
- Antimagicが見えた：MR攻撃一本からAP・AN・Poison等へ分散する

---

## Fatigue

FatigueはDominions戦闘の中心的な資源です。

Unitは攻撃、移動、Spell、Auraや環境効果などでFatigueを得ます。通常、毎Round一定量を回復しますが、Encumbranceが高いUnitは戦い続けると蓄積します。

### Fatigueの主要な影響

- Defenceが低下する
- Attackも不利になる
- Armor-defeating hitを受けやすくなる
- 100以上で気絶し、行動できない
- 極端なFatigueはHP Damageへ転換される

### 重装兵の弱点

重装兵は通常攻撃に強くても、長時間戦うと疲れます。Chaff、Skeleton、召喚、Fatigue Spellで戦闘を引き延ばすこと自体がCounterになります。

### MageのFatigue

SpellのFatigueは、要求Pathより高いPathを持つほど減ります。一方、Armor Encumbranceは別に加算されるため、重装MageはSpellを数回使っただけで気絶することがあります。

Reinvigoration、Gemの追加消費、Communion、Relief、Summon Earthpowerなどで管理します。

---

## Morale、Rout、Retreat

UnitはHPが0になるまで戦うとは限りません。

Morale判定は次のような状況で発生します。

- Squadが大きな損害を受ける
- Fearや恐慌効果を受ける
- CommanderやLeadershipを失う
- Army全体のHPが大きく減る
- 特殊なTurn Rout条件へ到達する

### Routは敗北と同じではない

戦場から離脱できたUnitは隣接ProvinceやFortへ退却を試みます。しかし、敵Provinceへ逃げたUnitや退路を失ったUnitは死亡します。

### 攻略上の意味

- FearはHPを削らずに戦線を崩せる
- Moraleの低い大量Chaffは、少数損害から連鎖崩壊する場合がある
- Rear attackでCommanderを倒すと、Leadership不足による崩壊を起こせる
- 退路を塞いだ戦闘ではRoutが大量死へ直結する
- 勝った側でも逃げた部隊はProvinceから消える

Battle Replayでは「殺された数」だけでなく、「いつRout判定が始まり、何が引き金だったか」を確認します。

---

## Mounted Unit

Dominions 6ではRiderとMountが別のStats・HPを持ちます。

- RiderだけがDamageを受ける
- MountだけがDamageを受ける
- AoEで双方がDamageを受ける
- Mountが倒れ、Riderが徒歩で戦闘継続する

といった状況があります。

### 攻略上の注意

- 騎兵の表示HPだけで総耐久を判断しない
- Mountが大型ならAoE・射撃の標的になりやすい
- Lance Chargeを使い切った後の武器とStatsを見る
- Mountを失った後のCombat Speed・Defence・装備を確認する
- Magic BardingやMount用能力をRider装備と混同しない

---

## Battlefield EnchantmentとCaster死亡

戦場全体へ作用するSpellの一部は、Casterが死亡すると解除されます。

そのためBattlefield Spellを使うMageには、単にPathを満たすだけでなく、

- 中央後方へ配置
- Bodyguardを付ける
- Arrow Fend等の防御を準備
- Flying / Attack Rear対策を置く
- Spell発動後も生存させる

必要があります。

逆に相手のArmy-wide効果が一人のCasterに依存しているなら、そのCasterを倒すことが最短のCounterです。

---

## Battle Replayの分析手順

負けた戦闘を次の順に見ます。

1. **最初の接敵位置**：想定したSquadが敵を受けたか
2. **最初に崩れた防御層**：命中、Protection、Resistance、MR、Moraleのどれか
3. **Damage表示**：Slash / Pierce / Shock / Poison等、何で死んだか
4. **Mage Script**：予定SpellがCastされたか、対象がいたか
5. **Fatigue**：Mageと前衛が何Roundで100へ達したか
6. **Commander**：Rear attackや射撃で落ちていないか
7. **Rout**：純粋な死亡より先にMoraleが崩れていないか
8. **Gem**：必要数を持ち、AIが想定どおり使ったか

原因を一つに決めつけず、次の戦闘では**一つだけ変更して差を見る**と学習しやすくなります。

---

## 関連ページ

- [両手武器・片手武器・盾](weapons-and-shields.md)
- [命令とBattle Script](orders.md)
- [魔法の基本](../magic/index.md)
- [Combat Gem](../magic/gems.md)
- [Communion](../magic/communions.md)

## 主な参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
- [illwiki: Dominions Random Number](https://illwiki.com/dom5/dom6/drn)
- [illwiki: Attack Skill](https://illwiki.com/dom5/dom6/attack-skill)
- [illwiki: Protection](https://illwiki.com/dom5/dom6/protection)
- [illwiki: Repel](https://illwiki.com/dom5/dom6/repel)
- [illwiki: Rout](https://illwiki.com/dom5/dom6/rout)
- [illwiki: Mounted Units](https://illwiki.com/dom5/dom6/mounted)

!!! note "数式の扱い"
    このページでは実戦で使える概念を優先しています。個別の例外や内部処理はPatchで変わる可能性があるため、厳密な検証記事は今後、能力ごとの独立ページへ分離します。
