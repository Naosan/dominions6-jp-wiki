---
title: "Lucky Coin"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 168
---

# Lucky Coin

**軽いShield性能とLuckを一つの手Slotへまとめ、Carrierの通常防御と事故耐性を同時に補うConstruction 3 Shield。**

Lucky Coinは「Luckだけを付けるMisc Item」ではありません。攻略上は、**Shieldとして攻撃を受け止める層と、Luckによる確率的な生存層を同じ手Slotへ置くItem**として評価します。

- [Dominions 6.35固定データ — Item 168](../../data/items/by-id/168.md)
- [Magic Item攻略辞典](index.md)
- [武器と盾](../../basics/weapons-and-shields.md)
- [Thug・SC装備](../thug-equipment.md)

---

# まず何ができるか

6.35固定データでは、Lucky CoinはConstruction 3、Forge要求**G2**のShieldです。

Armor record 67では、

- **Shield Protection 19**
- **Defence 4**
- **Encumbrance 0**

を持ち、Item本体は装備者へ**Luck**を与えます。

Item descriptionでは、銀製のbucklerに刻まれた人物の顔がLady Luckに好まれ、装備者を幸運にすると説明されています。

このItemの構造は、

```text
Shieldとしての防御
＋
Luckによる確率的な生存
```

です。

---

# Luckだけを見るとSlot評価を誤る

Lucky CoinのLuckは重要ですが、このItemはShield Slotを使います。

つまり比較対象は、単なるLuck sourceだけでなく、

- 普通のShield
- Vine Shield
- Charcoal Shield
- Eye Shield
- 片手Weaponとの組み合わせ
- 両手Weapon Build

です。

Lucky Coinを選ぶと、

```text
手Slot一つ
→ Shield防御とLuckを同時取得
```

できます。

一方で、別ShieldのControl・Contact punish・Resistance等は得られません。

---

# Shield Protection 19の意味

Lucky Coinは大盾ではなく軽いbucklerです。

Shield Protection 19は、Shieldが有効に働く攻撃に対して防御層を加えますが、すべてのDamageやSpellを一律に止めるわけではありません。

確認すべきなのは、

- 敵のAttack数
- 攻撃がShieldで扱える種類か
- CarrierのDefence
- 敵WeaponのDamage・AP / AN属性
- MissileやSpellの有無
- FatigueによるDefence低下

です。

Shield値だけを見て、MR-negates Spellや広範囲Battle magicまで防げると考えないようにします。

---

# Defence 4・Encumbrance 0の軽さ

Armor record上、Lucky CoinはDefence 4、Encumbrance 0です。

このため、重いShieldでCarrierの行動やFatigueを悪化させるより、**軽い手Slot防御として組み込みやすい**ことが利点です。

特に、

- 元からDefenceが高い
- Fatigue収支を崩したくない
- Self-buff後に長く戦う
- Shieldを持ちつつQuickness等を使う

Carrierでは、Encumbrance 0がBuild全体を壊しにくくします。

ただしDefence 4だけで高Attackの敵を安定して避けられるわけではありません。

---

# Luckは確率的な防御層

LuckはProtectionやResistanceのような固定的な数値防御とは性質が違います。

攻略上は、

- 一撃で倒される事故を減らす可能性
- 連続被弾の一部を生き残る可能性
- 重要CasterがScriptを完走する可能性
- Raiderが撤退・任務完了まで残る可能性

を増やす**確率的な保険**として扱います。

Luckがあるから必ず生き残るわけではなく、短いTestで一度助かった／死んだだけでは期待値を判断できません。

複数回の同条件Battleで、死亡率・任務成功率を比較します。

---

# Luckは基礎防御の代わりではない

Lucky Coinは、成立していないBuildを単独で完成させるItemではありません。

Carrierに、

- Protection不足
- MR不足
- Elemental Resistance不足
- Fatigue問題
- HP不足
- Damage不足

がある場合、Luckだけでは敗因を解消できません。

```text
基礎防御で大半を耐える
＋
Lucky Coinで残る事故を減らす
```

という順で考えると、Itemの役割が分かりやすくなります。

---

# 相性の良いCarrier

Lucky Coinと相性が良いのは、

- Shieldを装備できる
- 片手WeaponまたはWeaponなしで任務が成立する
- 元から一定のProtection・Defence・MRを持つ
- 重要なScriptを最後まで実行したい
- 一回の事故死が高価
- Encumbranceを増やしたくない
- Controlより汎用生存を優先する

Carrierです。

候補には、

- 軽装・高Defence Thug
- 片手Weaponを使うRaider
- 前線へ出るBattle Mage
- 貴重なCommander
- 小規模戦を繰り返すCarrier

があります。

ただしCasterが両手Boosterを必要とする場合、Lucky Coinは装備できません。

---

# 片手Weaponと組み合わせる

Lucky CoinはShieldなので、一般的には片手Weaponと組み合わせます。

```text
片手Weapon
→ Damage source

Lucky Coin
→ Shield防御＋Luck
```

という分担です。

[Frost Brand](frost-brand.md)等の片手Weaponと組み合わせる場合、攻撃と防御を一つずつの手Slotへ配置できます。

ただしWeaponが両手を要求する場合、Lucky Coinは使えません。

CarrierのDamageが不足しているなら、Shieldを持つことで必要Hit数や殲滅速度が悪化しないかも確認します。

---

# Vine Shieldとの違い

[Vine Shield](vine-shield.md)は近接してくる敵を拘束し、Carrierへ集中する行動を乱すControl Shieldです。

Lucky Coinは敵を拘束せず、

- Shield防御
- Luck
- Encumbrance 0

でCarrier自身の生存を補います。

```text
Vine Shield
→ 敵の近接行動を減らしたい

Lucky Coin
→ より汎用的な事故耐性が欲しい
```

という違いです。

大量の近接Chaffへ囲まれる任務ではVine Shieldが強く、高Damage・Spell・不確定要素を含む任務ではLucky Coinの汎用性が候補になります。

---

# Charcoal Shieldとの違い

[Charcoal Shield](charcoal-shield.md)はFire Resistanceと、近接攻撃者へのContact punishを持ちます。

Lucky CoinはFire対策や反撃Damageを与えません。

```text
Charcoal Shield
→ Fire対策＋殴ってくる敵へのPunish

Lucky Coin
→ 軽いShield＋Luckによる広い事故対策
```

です。

敵がFire damageを多用する、または多数の弱い近接攻撃者を反撃で削りたいならCharcoal Shieldを比較します。

特定属性への回答が不要で、より軽い汎用防御が欲しいならLucky Coinが候補です。

---

# Amulet of Antimagicとの役割分担

[Amulet of Antimagic](amulet-of-antimagic.md)はMisc SlotからMRを増やし、MR-based effectへの防御を安定させます。

Lucky CoinはShield SlotからLuckを与えますが、MRを直接増やしません。

Slotが異なるため、

```text
Lucky Coin
＋ Amulet of Antimagic
```

で物理・確率防御とMR防御を分担できます。

一方、装備予算が限られる場合は、敵が何でCarrierを倒すかを先に読みます。

MR-negates Controlが主なCounterなら、Lucky Coinだけを付けて安心しないようにします。

---

# Construction 3で使えるTiming

Lucky CoinはConstruction 3で解禁されます。

C5・C7 Itemより早い段階で使えるため、

- First war前のRaider準備
- 初期Thugの防御補助
- 早期の重要Caster保護
- Glamour Gemの初期用途

として検討できます。

ただしForge要求はG2です。

Construction到達だけでなく、G2 Forger、Glamour Gem income、Carrierの存在が揃って初めて実用になります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 3へ到達済み
- G2 Forge Mageがいる
- Shieldを使えるCarrierがいる
- 片手WeaponまたはWeaponなしで任務が成立する
- Luckによって事故率を下げたい
- Encumbranceを増やしたくない
- Vine Shield等の特化効果が不要
- Glamour Gemを別の重要用途から回せる
- 複数回Testで任務成功率が改善する

特に、安定して勝てるが時々事故死するCarrierでは、Lucky Coinの価値が見えやすくなります。

---

# Forgeしない・別Itemを選ぶ条件

- 両手Weapon・両手Boosterが任務に必須
- 敵の主CounterがMR-based effect
- 特定Elemental Resistanceが不足している
- 近接ControlにはVine Shieldが必要
- Contact punishにはCharcoal Shieldが必要
- Carrierの基礎Protection・HPが低すぎる
- Damage不足でShieldを持つ余裕がない
- G2 accessやGlamour Gemが希少
- Luckの有無より確定的な防御値が必要

Lucky Coinは汎用性がありますが、**特定の敗因へ直接答える専用Itemではない**場合があります。

---

# Counter：確率防御を回数と別軸で崩す

敵のLucky Coin Carrierへ一発勝負だけを狙うと、Luckで計画が崩れることがあります。

Counterは、

- 攻撃回数を増やし、確率防御へ繰り返し判定を迫る
- FatigueでDefenceと行動能力を落とす
- MR-based ControlでShield以外を攻める
- Elemental damageで不足Resistanceを突く
- 高AttackでShield・Defenceを上回る
- CarrierではなくArmy・Mage・Provinceを狙う
- Retreat routeを塞ぎ、任務成功条件を失わせる

ように、**Lucky Coin一枚が守っていない軸**を使います。

Luckの正確な発動結果はBattle Replayで確認し、単発の見た目だけでCounter成功率を判断しません。

---

# よくある失敗

## Luckがあれば必ず生き残ると思う

Luckは確率的な防御層です。連続攻撃や別軸のCounterで倒されます。

## Shield効果をすべてのSpellへ期待する

Shieldが有効でない攻撃・Spell・MR effectは別に対策します。

## 両手Weaponとの競合を忘れる

装備画面でLucky Coinと目的Weaponを同時に持てない場合があります。

## Vine Shield・Charcoal Shieldの代わりに惰性で選ぶ

敵構成が明確なら、特化Shieldの方が任務へ直結することがあります。

## 一戦だけで評価する

Luckは結果が揺れます。同条件を複数回Testします。

## G2で作れるから早期量産する

Carrier、Glamour Gem、任務がなければ在庫になります。

---

# Test game checklist

```text
[ ] C3・G2でLucky CoinがForge可能か確認
[ ] Item 168・Armor record 67であることを確認
[ ] Shield Protection 19を確認
[ ] Defence 4・Encumbrance 0を確認
[ ] 装備後にLuckが表示されることを確認
[ ] 同条件Battleを複数回行い死亡率を比較
[ ] 片手Weaponと同時装備できることを確認
[ ] 両手Weapon・Boosterとの競合を確認
[ ] Vine Shield / Charcoal Shieldとの任務成功率を比較
[ ] MR・Resistance不足が残っていないか確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 168](../../data/items/by-id/168.md)
- [Frost Brand](frost-brand.md)
- [Vine Shield](vine-shield.md)
- [Charcoal Shield](charcoal-shield.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [武器と盾](../../basics/weapons-and-shields.md)
- [Thug・SC装備](../thug-equipment.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / armors / protections_by_armor / Item description
- Dominions 6 Main Manual — Shield / Luck / Defence / Encumbrance
- Luckの実際の発動とShield処理はBattle Replayを最終確認
