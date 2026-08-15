---
title: Battle Replayの読み方
page_type: guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-15"
---

# Battle Replayの読み方

Battle Replayは、戦闘結果を眺めるための映像ではありません。

> **自分が立てた仮説と、実際に起きた戦闘を比較する検証記録**

です。

負けた戦闘ほど情報量がありますが、勝った戦闘も必ず確認します。勝利していても、Commanderが危険な位置にいた、Gemを浪費した、主力Spellが不発だった、補充不能なUnitを失った、という問題は残ります。

---

## Replayを開く前に書く四つ

映像を見る前に、戦闘前の想定を短く書きます。

```text
誰が最初に敵を受ける予定だったか
何が主なDamage源だったか
Mageは何Round目に何を使う予定だったか
敵は何をしてくると予想したか
```

これを書かずにReplayを見ると、起きたことへ後から理由を付けやすくなります。

---

## 三回に分けて見る

一度の再生ですべてを理解しようとしません。

## 一回目：戦場全体を見る

細かいDamage表示より、Armyの形を見ます。

- 最初の接敵位置
- Squadの移動経路
- 前衛とDamage役の間隔
- FlankとAttack Rear
- Commanderの位置
- Mageが敵射撃へ露出したか
- Rout開始地点
- 退却方向

ここで「想定した戦場になったか」を判断します。

## 二回目：最初の崩壊点を見る

自軍全体が負けた瞬間ではなく、**最初に計画が壊れた瞬間**まで戻します。

例：

- 盾兵より先に両手武器兵が接敵した
- Cavalry Chargeで前衛の一部が即死した
- Commanderが射撃で倒れた
- MageがBuff前に攻撃Spellを使った
- 敵のResistanceで主力Damageが通らなかった
- Fatigue 100で主力が気絶した
- Fearまたは損失で一SquadがRoutした

その後の崩壊は、最初の失敗の結果であることが多くあります。

## 三回目：数値とScriptを見る

Unitを選び、次を確認します。

- HP
- Fatigue
- Morale
- Protection
- Defence
- MR
- Elemental Resistance
- Affliction
- Status effect
- 使用中のBuff
- Spellcastingの順序

戦闘後の結果画面だけでは、途中で一時的に何が起きたか分からないため、重要Roundで停止して見ます。

---

## 最初に見る八項目

## 1. 接敵順

予定した前衛が敵を受けたか確認します。

### 問題例

- Damage役が前へ出すぎた
- Hold回数が合わない
- Combat Speed差でSquadが分離した
- Formationが想定より広い／深い
- Attack orderで別の敵を追った

### 次に試すこと

位置を少し変える、Holdを一回だけ調整する、Squadを分ける、Attack orderを変える、のいずれか一つを試します。

## 2. Damage type

Unitが何で死んだかを見ます。

- Slash
- Pierce
- Blunt
- Fire
- Cold
- Shock
- Poison
- Acid
- AP
- AN
- MRを狙う効果

「魔法で死んだ」では不十分です。Protection、Resistance、MRのどれが対策になるかはDamage typeで変わります。

## 3. 命中と防御

敵の攻撃が当たりすぎているのか、当たった後に耐えられないのかを分けます。

- 高Defenceで避ける段階
- Shieldで受ける段階
- Protectionで軽減する段階
- HP、Regeneration、Luck等で耐える段階

最初の防御層が機能しているなら、別の層へ投資する必要があります。

## 4. Mage Script

各Mageについて、予定Spellを実際に使ったか確認します。

不発の原因候補：

- Research不足
- Path不足
- Gem不足
- Range外
- 有効なTarget不在
- Fatigue
- Silence、Stun、Paralyze等
- 敵が想定と違う
- Script前に接敵・死亡
- AIが別Spellを選ぶ条件になった

「AIが馬鹿だった」で終わらせず、Scriptが成立する条件を分解します。

## 5. Buff Timing

Buffが入ったかだけでなく、入る前に何が起きたかを見ます。

```text
Round 1：Self Buff
Round 2：Resistance
Round 3：Army Buff
Round 4：敵接敵
```

の予定が、Round 2で敵が接敵していれば、Spell自体が正しくても計画は失敗しています。

## 6. Fatigue

Fatigueは長期戦の勝敗を変えます。

- 前衛が何Roundで疲れたか
- Mageが何Castで100へ達したか
- Armor Encumbranceが高くないか
- Heat / Cold、Battlefield effect、Aura等の影響
- ReinvigorationやReliefが間に合ったか

序盤は耐えていたArmyが突然崩れる場合、Fatigueを疑います。

## 7. MoraleとRout

死亡数だけでなく、Routがいつ始まったかを見ます。

- Squad損失
- Fear
- Commander死亡
- Army全体の損害
- Leadership
- 特殊Rout条件

前衛がまだ生きているのに全体が逃げ始めたなら、Damage不足ではなくMorale問題かもしれません。

## 8. Retreat route

RoutしたUnitがどこへ逃げたか確認します。

退却先がなく、戦場から逃げたUnitが失われている場合、Battle ScriptだけでなくStrategic Map上の侵攻経路が問題です。

---

## 症状別の診断表

| Replayの症状 | 主な原因候補 | 次に試すこと |
|---|---|---|
| 接敵直後に前衛が消える | Charge、高Damage、AP・AN、配置不良 | Screen追加、標的変更、Resistance・防御層確認 |
| 敵へ攻撃がほとんど当たらない | 高Defence、Darkness、Debuff、Fatigue | Attack向上、複数攻撃、拘束、疲労させる |
| 当たるが敵HPが減らない | Protection、Shield、Resistance、低Damage | 高Damage、AP・AN、別Damage type |
| 序盤は優勢だが後半崩れる | Fatigue、Morale、Summon切れ、Caster死亡 | Reinvigoration、短期決着、予備前衛、Caster保護 |
| Archerが味方を殺す | 射線、Target、接敵後も射撃継続 | 配置変更、対象変更、射撃Squad分割 |
| Mageが予定Spellを使わない | 条件不足、Range、Target、Gem、Fatigue | Script成立条件を一つずつ確認 |
| Mageが早く気絶する | Spell Fatigue、Armor Encumbrance、Path不足 | 軽装化、Path boost、Reinvigoration、Cast数削減 |
| Battlefield Enchantmentが途中で消える | Caster死亡・退場 | 後方配置、Bodyguard、射撃・Flank対策 |
| Commander死亡後にArmyが崩れる | 後方防御不足、Attack Rear、射撃 | Commander分散、Bodyguard、予備Leadership |
| 敵がほぼ無傷で自軍だけRout | Fear、Morale、Leadership、損失集中 | Morale向上、Squad再編、Fear source処理 |
| Elemental Spellが急に効かない | Resistance、Ward、Target変更 | 別Element、物理、MR、Poison等へ分散 |
| MR Spellが通らない | 高MR、Antimagic、Mindless、Penetration不足 | Penetration、別Target、Protectionを狙う攻撃 |
| Thugが雑兵に囲まれて停止する | Fatigue、攻撃回数不足、拘束、Chaff | AoE、Reinvigoration、援護、退路 |
| 勝ったが次戦へ進めない | 損失過多、Gem枯渇、Commander不足 | 補給、停止、役割別予備Army |
| Rout後に大量消失する | 退却先不足、敵領への侵入 | 攻撃経路と隣接自領を見直す |

---

## Damageを防御層へ分解する

「前衛が弱い」と判断する前に、どの層が破られたかを分けます。

```text
攻撃させない
→ 命中させない
→ Shieldで受ける
→ Protection / Resistanceで軽減する
→ HP・Regeneration等で耐える
→ MoraleとFatigueで戦闘継続する
```

### 例1：Shieldは機能しているが死ぬ

Shield Hit後も高DamageがProtectionを抜いています。Shieldをさらに増やすより、Protection、Damage reduction、敵Damage役の処理が必要です。

### 例2：Protectionは高いが毒で死ぬ

物理防御は機能しています。Poison Resistance、短期決着、射撃処理へ変えます。

### 例3：一体ずつは耐えるが全体が逃げる

Morale、Leadership、Fear、Squad損失が問題です。

詳しくは[戦闘ルール](../basics/combat-rules.md)を参照してください。

---

## Mage Replayの読み方

Mageは「何人いたか」より、何Round働いたかを見ます。

各Mageについて次を記録します。

```text
初期Fatigue：
Round 1：
Round 2：
Round 3：
Round 4：
Round 5：
Script後の行動：
死亡・気絶・RoutしたRound：
使用Gem：
```

### Mageが多いのに弱い場合

- 同じ役割へ重複しすぎている
- 前衛が時間を作れていない
- Targetが存在しない
- Rangeが足りない
- Counter Resistanceへ一種類のSpellだけを撃っている
- Script終了後のAI行動が危険

のいずれかを疑います。

### Gemを見る

- 必須Spellへ使ったか
- 不要なSpellへ使ったか
- 予定より早く消費したか
- 余らせたか
- Retreatで失ったか

を確認します。

Gemを持たせる量は、Battle数、AIの選択、失うRiskの釣り合いです。

---

## 勝ったReplayも分析する

勝利時は、次の三つを探します。

## 偶然勝った部分

- 敵Scriptが不発
- 敵Commanderが早期死亡
- Morale checkが有利
- DRNの偏り
- 敵がGemを持っていない

## 再現できる部分

- 接敵順
- Resistance Timing
- Focus fire
- Commander protection
- Reinforcement

## 次に対策される部分

- 一種類のElemental Damage
- 一人のBattlefield Enchantment Caster
- Sacredへの依存
- Thug一体
- Archer line

勝った直後に、相手が最も安く用意できるCounterを考えます。

---

## 一変更Rule

敗戦後に、兵種、Formation、Research、Pretender、全Scriptを同時に変えると、何が改善したか分かりません。

まず最初の崩壊点へ直接関係する変更を一つ選びます。

```text
変更前：Damage役が盾兵より先に接敵
変更：Damage役へHold and Attackを一回追加
それ以外：同じ
```

次のReplayで接敵順だけを比較します。

実戦では敵も変化するため完全な実験にはなりませんが、無秩序な変更より学習できます。

---

## Battle Report Template

```text
Game / Turn：
敵国家・Army：
戦闘Province：
戦闘前の想定：
自軍の勝利条件：
敵の想定勝利条件：

最初の接敵：
最初の崩壊点：
主なDamage type：
Shield / Protection / Resistance / MR：
Mage Script結果：
Buff完成Round：
Mage Fatigue：
前衛Fatigue：
Commander死亡：
Rout開始：
Retreat結果：
使用Gem：

想定どおりだったこと：
想定と違ったこと：
次回変えること一つ：
```

国家攻略やMatchup記事を書くときも、この形式で根拠を残すと、単なる印象から再現可能な知見へ変わります。

---

## よくある見誤り

### Kill数だけを見る

Rout、Commander死亡、Gem消費、補充不能な損失が見えません。

### 最後の崩壊だけを見る

原因は数Round前の接敵順、Buff不発、Caster死亡かもしれません。

### Unitの強弱だけで説明する

配置、命令、Research、Resistance、地形を無視しています。

### Replayを最大速度で一度だけ見る

重要Roundを止めず、Damage typeとFatigueを確認していません。

### 「AIが使わなかった」で終える

Range、Target、Gem、Path、Fatigue、Script条件を分解していません。

### 勝ったので問題なしとする

次のCounterを見逃します。

---

## 関連ページ

- [戦闘ルール](../basics/combat-rules.md)
- [命令とBattle Script](../basics/orders.md)
- [両手武器・片手武器・盾](../basics/weapons-and-shields.md)
- [GemとBlood Slave](../magic/gems.md)
- [Communion・Sabbath](../magic/communions.md)
- [序盤拡張](expansion.md)
- [最初の戦争](first-war.md)

## 主な参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
