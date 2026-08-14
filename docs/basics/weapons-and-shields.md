---
title: 両手武器・片手武器・盾
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-14"
---

# 両手武器・片手武器・盾

## 結論

**両手武器が上位、盾が上位という関係ではありません。**

- **両手武器**：一撃のDamage、Strengthの活用、武器長を得やすい
- **片手＋盾**：Parry、Shield Protection、射撃耐性、戦線維持を得やすい
- **二刀・複数武器**：命中判定とOn-hit効果の回数を増やすが、Ambidextrous不足に注意

実戦では、

> 盾兵で受ける → 両手武器・射撃・Mageで倒す

という役割分担が最も安定しやすくなります。

---

## 武器を評価する項目

「片手か両手か」だけでなく、最低限次を見ます。

| 項目 | 意味 |
|---|---|
| Damage | 命中後にProtectionを突破する力 |
| Attack | 命中させる力 |
| Defence | 武器による近接Defence補正 |
| Length | Repelと接近戦の間合い |
| Damage type | Slash / Pierce / Blunt / Untyped等 |
| 特殊属性 | AP、AN、Magic、Bonus damage、Charge、On-hit効果等 |
| 攻撃回数 | 一Roundに何回判定を作るか |
| Strength | 近接Damageの土台 |
| Unit cost | Gold、Resource、Recruitment制限 |

同じGreat Swordでも、Strength 10の人間とStrength 22の巨人では価値が全く違います。

---

# 両手武器

## 強み

### 高Damage

両手武器は武器固有Damageが高い傾向があります。さらに近接のTwo-handed weaponはStrengthから得るDamageが通常より大きくなります。

そのため、次の相手へ向きます。

- 高Protection
- 高HP
- Giant
- 重装Sacred
- Regenerationを上回るBurst damageが必要な敵
- 低Defenceで硬い敵

### Overkillより「通るか」が重要な相手

Protection 5・HP 10の敵へDamage 30を出しても余剰Damageが大きくなります。

しかしProtection 22の敵にDamage 14を何回当てても、ほとんど通らない場合があります。この場合は手数より一撃の重さが必要です。

### Weapon Length

Great Spear、Pike、Halberdなどの両手武器は長いことが多く、Repelを利用できます。

ただし「両手武器だから長い」のではありません。Lengthは独立したStatsなので必ず個別に確認します。

## 弱み

- Shield Parryがない
- 射撃へ弱くなりやすい
- 高Damage攻撃を受ける前に倒される可能性がある
- 高Defence相手には一撃が当たらない
- 長武器相手にRepelされる場合がある
- 高価な両手Sacredを前へ出すと損耗が重い

## 向くUnit

- 高Strength
- 高Protectionまたは高Defenceを自前で持つ
- BlessやSpellで防御を補える
- 高Attack
- Formation Fighter等で前線効率がよい
- 安価で交換可能

---

# 片手武器＋盾

## 強み

### Parry

盾は近接攻撃に対してParryを提供します。Defenceだけでは避けられないが、Parry込みなら防げた攻撃はShield Hitになり、盾のProtectionを使えます。

### 射撃防御

盾はBow、Crossbow、Javelin等への重要な防御です。通常のDefence Skillは射撃回避の中心ではないため、盾の有無が接近までの損害を大きく変えます。

### 時間を買う

盾兵の重要な役割は、必ずしも敵を倒すことではありません。

- Chargeを受ける
- Arrowを受ける
- MageのBuff完成まで耐える
- 高火力兵が接敵するまで敵を固定する
- Battlefield Spellの効果が蓄積するまで生存する

こと自体が価値です。

## 弱み

- 片手武器のDamageが低い場合、高Protectionを倒せない
- 大盾は重く、Defence・Encumbranceへ不利がある
- AN、MR攻撃、Poison等には盾のProtectionが意味を持たない
- Shield Hitでなければ盾Protectionは使われない
- 盾だけで勝利手段を作ると長期戦で疲れる

## 向くUnit

- 前衛
- Bodyguard
- 射撃を受ける囮
- 高価なMageやSacredを守る兵
- 後衛火力を持つArmy
- Moraleが高く長く粘れる兵

---

# 複数武器・多段攻撃

攻撃回数が多いUnitは、次の利点があります。

- 高Defenceへ複数回の命中判定を作る
- Mirror Image等を剥がす
- Harassmentを蓄積する
- Poison、Life Drain、Fatigue、Stun等のOn-hit効果を複数回試す
- 低Protectionの大量兵を素早く処理する

一方、低Damage攻撃を増やすだけでは高Protectionに弾かれます。

### Ambidextrous

複数武器を使うUnitは、武器長や装備に応じた二刀流ペナルティを受けることがあります。Ambidextrousが十分なら緩和されます。

### 多段攻撃が向く相手

- 高Defence・低Protection
- Glamour / Mirror Image
- Chaff
- On-hit効果に弱い敵

### 多段攻撃が苦手な相手

- 高Protection
- Fire Shield等の反撃効果
- Physical Resistance
- Mossbody等の一撃ごとに軽減する防御

---

# Damage typeで選ぶ

## Slashing

Protectionを抜いた後のDamageを増やしやすく、肉体へ通ったときの殺傷力に優れます。盾を傷める用途も得意です。

## Piercing

Protectionの一部を減らして計算します。CrossbowのようにArmor Piercingも持つ場合、高Protectionへの有力な一般兵Counterになります。

## Blunt

Head Hitで威力が上がり、盾へ圧力をかけます。Skeleton、Statue、Plant等はPhysical Resistanceが異なるため、相手の耐性を確認します。

## Untyped

追加ボーナスはありませんが、Slash / Pierce / Blunt Resistanceで軽減されません。

---

# 盾の大きさ

## 小型Shield

- 軽い
- Defence penaltyが小さい
- Parry・Protectionは控えめ
- 高Defence Unitの機動性を維持しやすい

## Standard Shield

攻防のバランスがよく、通常歩兵の基準です。

## Tower Shield / 大盾

- ParryとShield Protectionが高い
- 射撃へ非常に強い
- 重く、Defence・Encumbranceへ不利
- Fatigue戦では弱点が出る

大盾兵へ低Attackの通常兵を当てると、Shield Hitを繰り返してDamageが通りません。高Attack、Flail系、AP / AN、Spellを使います。

---

# 相手別の判断

| 相手 | 優先しやすい装備・攻撃 |
|---|---|
| 大量の軽歩兵 | 盾、複数攻撃、範囲Damage |
| Bow・Crossbow | 大盾、散開、射撃対策Spell |
| 高Protection | 両手高Damage、Piercing＋AP、AN、MR攻撃 |
| 高Defence | 高Attack、多段攻撃、拘束、必中・AoE |
| Giant | 高Damage、AP / AN、Fatigue、MR攻撃 |
| Cavalry Charge | 盾・Chaffで受ける、Pike、射撃 |
| Skeleton | Blunt、Holy、範囲攻撃、疲れない軍 |
| Ethereal | Magic Weapon、Spell |
| Regeneration | Burst damage、Poison、Disease、即死・MR攻撃 |

---

# Army内での混ぜ方

## 標準形

- 盾兵：40～60%
- 両手火力兵：20～40%
- 長武器・専門Counter：10～20%
- 射撃・Mage・機動兵：敵に応じて追加

これは固定比率ではなく、初見の敵に対する出発点です。

## 配置

```text
前方：盾兵 ─ Attack Closest
後方または左右：両手武器 ─ Hold and Attack
側面：Pike / Cavalry counter
後方：Crossbow / Mage
```

盾兵と両手武器兵を同じSquadへ混ぜると、両手兵も最初の射撃・Chargeを受けます。役割が違うならSquadを分けます。

---

# SacredとBuffによる逆転

装備だけを見てUnitを評価してはいけません。

盾なし両手Sacredでも、BlessやSpellで、

- Protection
- Defence
- Luck
- Regeneration
- Elemental Resistance
- Ethereal / Mistform系

を補えば、弱点を消しながら高Damageだけを残せます。

逆に盾重装兵でも、敵がAN Shock、Poison、MR攻撃、Fatigueを使うなら装備投資が機能しません。

**装備評価は、Bless・研究・敵Counter込みで行います。**

---

# 5秒判定法

Unitを見たら次の順で判断します。

1. **Strength**：高いなら両手武器評価を上げる
2. **最終Damage**：敵Protectionへ通るか
3. **Attack**：その一撃は当たるか
4. **Defence＋Protection**：接敵後何Round生きるか
5. **Shield**：射撃と通常攻撃を受ける役割か
6. **Length**：Repelできるか、されるか
7. **Damage type / AP / AN / Magic**：敵防御のどこを突破するか
8. **Gold / Resource**：同じ投資で何人並ぶか

---

# よくある誤解

## 「鎧にはBlunt」

BluntであることとArmor Piercingは別です。高Protectionへ必要なのは、最終Damage、Piercing、AP、AN、Armor破壊等です。

## 「Flailは盾を無視する」

Flail系は盾持ちへの命中を助けますが、Shield ProtectionやArmorを自動的に無視するわけではありません。低Damageなら当たっても弾かれます。

## 「Defenceが高ければ弓も避ける」

通常のDefence Skillは射撃防御の中心ではありません。盾、Size、距離、Precision、Air Shield等を見ます。

## 「Damageが高いほど常に得」

低HP・低Protection相手ではOverkillになります。生存性、手数、価格の方が重要なことがあります。

---

## 関連ページ

- [戦闘ルール](combat-rules.md)
- [命令とBattle Script](orders.md)
- [Magic Item](../items/index.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [illwiki: Protection](https://illwiki.com/dom5/dom6/protection)
- [illwiki: Attack Skill](https://illwiki.com/dom5/dom6/attack-skill)
- [illwiki: Repel](https://illwiki.com/dom5/dom6/repel)
