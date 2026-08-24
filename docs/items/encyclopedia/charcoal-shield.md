---
title: "Charcoal Shield"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 173
---

# Charcoal Shield

**高いShield ProtectionとFire Resistanceを持たせ、近接して殴る敵へ熱の反撃を返すConstruction 5の接触Punish Item。**

Charcoal Shieldは「硬い盾」であるだけではありません。攻略上は、**Carrierへ集中する近接攻撃そのものを敵の損耗源へ変えるShield**として評価します。

- [Dominions 6.35固定データ — Item 173](../../data/items/by-id/173.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Resistance Item](../resistance-items.md)
- [Thug・SC装備](../thug-equipment.md)
- [Magic Item総論](../index.md)

---

# まず何ができるか

6.35固定データでは、Charcoal ShieldはConstruction 5、Forge要求**E2F1**のShieldです。

参照するShield / Armor record 60は、

- **Protection 26**
- **Defence 4**
- **Encumbrance 1**

を持ちます。

Item本体は装備者へ**Fire Resistance +10**を与えます。

さらにItem descriptionでは、盾へ打撃を加えた相手へ強烈な熱が武器を通じて伝わり、苦痛を与える性質が説明されています。

つまり一つのHand Slotで、

```text
Shield防御
＋ Fire Resistance
＋ 近接接触への熱反撃
```

をまとめます。

---

# Charcoal Shieldは「殴られる回数」を価値へ変える

通常、Carrierが多数の敵に囲まれるほど受ける攻撃回数が増え、不利になります。

Charcoal Shieldは近接攻撃へ反撃を返すため、

```text
敵がCarrierを殴る
→ CarrierはShieldで耐える
→ 攻撃者も熱で損耗する
```

という交換を作ります。

そのため価値は、単発の強敵より、

- 多数のMelee chaff
- 攻撃回数の多い敵
- Carrierへ長時間接触する敵
- Fire Resistanceの低い敵

に囲まれる場面で出やすくなります。

ただしCarrierがすぐ倒されるなら、反撃が積み上がる時間はありません。

---

# 反撃は生存力と掛け算になる

Charcoal ShieldのDamageは、Carrierが近接戦へ残り続けるほど機会が増えます。

そのため、

- Protection
- HP
- Regeneration
- Reinvigoration
- Elemental Resistance
- MR
- Control / Awe

と組み合わせて評価します。

[Ring of Regeneration](ring-of-regeneration.md)で生存Roundを伸ばすと、接触反撃が発生する時間も伸びます。

[Girdle of Might](girdle-of-might.md)でFatigueを抑えると、Carrier自身の攻撃と防御を維持しやすくなります。

Shield単体のDamageだけでなく、**何Round敵に殴らせ続けられるか**が重要です。

---

# Fire Resistance +10はCarrier側の防御

Charcoal Shieldは装備者へFire Resistance +10を与えます。

これは、

- Fire damageを使う敵
- Heatを伴う戦場
- Fire Shield同士の接触
- 自軍のFire系Battle planと同居する場面

でBuildを整えやすくします。

ただし+10だけでFire対策が完成するとは限りません。

敵のDamage量、Armor Piercing / Armor Negating、他のResistance sourceを含め、**最終Fire ResistanceをUnit画面で確認**します。

---

# Shield Statsにも意味とCostがある

Shield record 60はProtection 26、Defence 4、Encumbrance 1です。

高いShield ProtectionとDefenceはMissileやBlock可能な攻撃への防御を補いますが、Encumbrance 1は長期戦のFatigueへ加わります。

したがって、

- 高Defenseを維持したいか
- Fatigue余力があるか
- Shieldを使えるHand構成か
- 両手Weaponを捨てる価値があるか

を確認します。

Charcoal Shieldの接触反撃が強くても、Carrier全体のDamage planが両手Weaponに依存するなら採用できません。

---

# Vine Shieldとの違い

[Vine Shield](vine-shield.md)は近接してきた相手を拘束し、敵の行動量を乱すControl Itemです。

Charcoal Shieldは、近接攻撃を行う敵へ熱の反撃を返すPunish Itemです。

```text
Vine Shield
→ 敵を止め、殴られる回数を減らす

Charcoal Shield
→ 殴ってくる敵へDamageを返す
```

という違いがあります。

Carrierが敵を倒す速度、敵のFire Resistance、Controlへの抵抗、必要なShield Statsを見て選びます。

---

# Frost Brandとの片手Build

[Frost Brand](frost-brand.md)等の片手Weaponと組み合わせると、

```text
Carrierの能動攻撃: Weapon
敵の近接攻撃への反撃: Charcoal Shield
Carrier防御: Shield + Armor + Resistance
```

というBuildを作れます。

この構成はDamage sourceを複数軸へ分けますが、

- Cold Resistanceの高い敵
- Fire Resistanceの高い敵
- 遠距離中心の敵

には効率が下がります。

Damage typeを固定せず、実際の対戦相手へ合わせます。

---

# 相性の良いCarrier

特に相性が良いのは、

- 近接戦へ入る
- 多数の敵に囲まれても数Round生存できる
- 片手WeaponまたはNatural attackでDamageを出せる
- Fatigueを管理できる
- Fire Resistanceも必要
- 敵の主力がMelee中心

Carrierです。

Charcoal Shieldは、敵から離れて戦うMageやArcherへ持たせても、接触反撃の機会が少なくなります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- E2F1 Forge accessを確保できる
- 近接Carrierがいる
- 多数のMelee attackを受ける任務がある
- Carrierが数Round以上生存できる
- 敵のFire Resistanceが高すぎない
- Fire Resistance +10もBuildへ有効
- Hand SlotへShieldを置いてもDamage planが成立する
- Test gameで敵の損耗速度が上がる

特にPD RaiderやChaff処理では、**Carrierが受ける攻撃回数と敵が倒れる速度**を同時に記録します。

---

# Forgeしない・別Itemを選ぶ条件

- 敵の主力がMissile / Battle magic
- 敵が高Fire Resistance中心
- Carrierが接敵後すぐ倒される
- MR-based effectで先に止まる
- 両手WeaponがDamage planの中心
- Fatigue余力がなくEncumbranceを増やしたくない
- Vine Shield等のControlの方が必要
- E2F1 accessや複合Gem投資が重い

Charcoal Shieldは**近接接触が起きるほど価値が増えるItem**です。接触の少ない戦場では機能の一部が遊びます。

---

# Counter：Fire Resistanceか、接触しない攻撃軸

敵がCharcoal Shieldを装備している場合、低Fire ResistanceのMelee chaffを大量にぶつけると相手の得意な交換になります。

Counterは、

- Fire Resistanceを持つUnitで接触する
- Missile / Battle magicで距離から削る
- Armor NegatingやMR-based effectでShield防御と別軸を攻める
- Burst damageを集中し、反撃が積み上がる前に倒す
- Fatigueを増やしてCarrier自身の機能を落とす
- Carrierを迂回してArmy・Mage・Provinceを狙う

のように、**熱反撃へ長時間付き合わない**方向で考えます。

---

# よくある失敗

## Fire Immunityを得ると思う

固定値はFire Resistance +10です。敵のFire damage量によっては追加対策が必要です。

## 接触反撃だけで敵を倒せると思う

Carrier自身のDamage sourceと生存力がなければ、反撃が積み上がりません。

## 遠距離国家へ同じBuildを持ち込む

接触してこない敵には熱反撃の機会が減ります。

## Shield StatsとEncumbranceを見ない

Protection 26 / Defence 4 / Encumbrance 1を含む最終Statsを確認します。

## 両手Weapon Buildへ無理に入れる

Hand Slot構成そのものが変わり、能動Damageを失うことがあります。

---

# Test game checklist

```text
[ ] C5・E2F1でCharcoal ShieldがForge可能か確認
[ ] Item 173 / Shield record 60であることを確認
[ ] Protection 26・Defence 4・Encumbrance 1を確認
[ ] Fire Resistanceが+10されることを確認
[ ] Melee attackerへ熱反撃が発生することをBattle Replayで確認
[ ] Fire Resistanceの異なる攻撃者でDamage差を比較
[ ] Missile / Magic攻撃時の挙動を確認
[ ] Charcoal Shieldなし／ありでCarrierの生存Roundを比較
[ ] Vine Shieldとの敵処理速度・生存時間を比較
[ ] Ring of Regeneration併用時の総反撃機会を比較
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 173](../../data/items/by-id/173.md)
- [Vine Shield](vine-shield.md)
- [Frost Brand](frost-brand.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Girdle of Might](girdle-of-might.md)
- [Resistance Item](../resistance-items.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Thug・SC装備](../thug-equipment.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / armors / protections_by_armor / Item description
- Dominions 6 Main Manual — Shield / Fire Resistance / Fatigue / Forge Item
- 接触反撃の発生・Damage、Shield判定、最終Statsはゲーム内Unit画面とBattle Replayを優先
