---
title: "Vine Shield"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 176
---

# Vine Shield

**近接してきた相手を生きた蔓で拘束しようとし、Carrierが囲まれた時の「敵の行動量」を削るConstruction 5のControl系Shield。**

Vine ShieldはShield Protectionを積むだけの装備ではありません。攻略上は、**Carrierへ接触した敵を止めることで、受ける近接攻撃のTempoを崩す装備**として評価します。

- [Dominions 6.35固定データ — Item 176](../../data/items/by-id/176.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Magic Item総論](../index.md)

---

# まず何ができるか

6.35固定データでは、Vine ShieldはConstruction 5、Forge要求**N2**のShieldです。参照するShield / Armor record 63は、

- Shield Protection 13
- Defence 5
- Encumbrance 0

です。

さらにItem descriptionでは、**bearerとclose combatに入った相手へ蔓が伸び、相手をその場へ拘束しようとする**性質が明記されています。

ここがVine Shieldの主な攻略価値です。

---

# 「防御値」より敵の行動を減らすShield

普通の防御装備は、攻撃を受けた後にDamageを減らしたり、Hitされにくくしたりします。

Vine Shieldはそれに加えて、近接してきた敵へControlを掛け、**敵が自由に殴り続ける状況そのものを崩す**方向で働きます。

そのため価値は、

```text
一体ずつ強い敵を止める
```

より、

```text
多数の近接敵に囲まれるCarrier
→ 接触した敵の一部が拘束される
→ 同時に有効行動する敵を減らす
→ Carrierが生き残るRoundを伸ばす
```

という場面で理解しやすくなります。

---

# Thug装備では「時間を買う」役

Thug / SCは、Damageを完全に0へする必要はありません。

- Buffが立ち上がるまで
- Regenerationが追いつくまで
- 敵を少しずつ処理するまで
- Fatigue差が広がるまで

生存できれば勝てるBuildがあります。

Vine Shieldは、近接敵の行動を乱すことで**その必要時間を買う**装備として組み込みます。

だからShield単体で見るより、

- Protection
- Regeneration
- Reinvigoration
- Resistance
- MR
- Damage source

との組み合わせで評価します。

---

# Carrierは「囲まれても仕事を続ける」型

相性が良いのは、近接戦へ入ること自体は許容でき、数Round以上その場へ残りたいCarrierです。

確認するのは、

- 本体HP / Protection
- Regenerationや回復手段
- Fatigue
- MRとElemental Resistance
- Damage output
- Retreat route

です。

Vine Shieldだけで耐久が完成するわけではありません。

特にMagic、Armor Negating、MR-based effectなど**近接接触以外の軸**は別に対策する必要があります。

---

# Shield StatsとSlotを分けて見る

6.35のShield record自体は**Defence 5 / Encumbrance 0**で、重いShieldのようなEncumbrance負担を持ちません。

一方で機会費用は、数値Penaltyより**手SlotをShieldへ固定すること**にあります。

- 両手武器を使えない
- 別のShieldを使えない
- 手SlotをBoosterや特殊Utilityへ回せない

というBuild上の選択が発生します。

「Vine拘束が強いから採用」ではなく、**Shield recordのStatsと、手Slotを使う機会費用を別々に確認**します。

---

# Frost Brand等との片手Build

片手武器と組み合わせやすいのもVine Shieldの強みです。

```text
Damageを出す片手Weapon
＋ Vine Shieldで近接Control
＋ Armor / Miscで耐久
```

のように、攻撃とControlを別の手へ分けられます。

ただし「定番セットだから固定」にはしません。

敵が遠距離・Magic中心ならVine ShieldのControl部分は働く機会が減るため、Resistanceや別のShield / Utilityへ差し替える方がよい場合があります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- N2 Forge Mageを確保できる
- 近接Chaffや多数のMelee unitへ突っ込むCarrierがいる
- Carrierが数Round以上戦える基礎耐久を持つ
- Hand slotへShieldを置いてもDamage planが成立する
- 敵の主な脅威が近接接触から来る
- Controlで生存時間を伸ばすことに意味がある

特にPD Raiderや小規模迎撃では、**何体に囲まれた時に崩れるか**をTestすると効果を判断しやすくなります。

---

# Forgeしない・別装備を選ぶ条件

- 敵の主力Damageが遠距離 / Magic
- CarrierがMR-based Controlで先に止まる
- Armor Negating等で短時間に落ちる
- 両手武器がDamage planの中心
- Hand slotを別のBooster / Shield / 特殊Counterへ使いたい
- 近接敵をControlするよりResistanceを足す方が重要

Vine Shieldは**近接戦のTempoを変えるItem**なので、戦場に近接接触が少ないと価値も下がります。

---

# Counter：Vine Shieldへ付き合わない

敵のVine Shield Carrierへ、近接Chaffを延々ぶつけると相手の得意な状況を作ります。

Counterは、

- Missile / Battle magicで接触前から削る
- MR系、Fatigue、Armor Negating等の別軸を使う
- 高火力を集中し、長期戦にさせない
- Carrierを迂回してArmy / Mage / Provinceを狙う
- Remote attackやAssassinationで戦場外から圧力を掛ける

のように、**close combatのControlへ依存しない攻撃軸**を選びます。

「拘束を全部突破する」より、そもそもVine Shieldが価値を出す戦い方をしない方が簡単なことがあります。

---

# よくある失敗

## Vine Shieldだけで無敵になると思う

近接Controlは耐久の一部です。MagicやResistance不足は別問題です。

## CarrierのDamage不足を無視する

敵を止めても倒せなければ、長期戦でFatigueや援軍に負けます。

## Shieldの固定値と特殊効果を混同する

Shield Protection 13 / Defence 5 / Encumbrance 0というrecordと、close combat相手を拘束しようとする特殊効果は別レイヤーです。

## 遠距離国家へ同じBuildを持ち込む

接触してこない相手にはControlの機会が減ります。

## Retreat routeなしでRaidする

Carrierが勝てない相手に当たった時、Itemごと失うRiskが高くなります。

---

# Test game checklist

```text
[ ] C5・N2でVine ShieldがForge可能か確認
[ ] Item 176 / Shield record 63であることを確認
[ ] Shield Protection 13 / Defence 5 / Encumbrance 0を確認
[ ] 装備後の最終StatsをUnit画面で確認
[ ] close combat相手へvineの拘束が発生することをBattle Replayで確認
[ ] 少数精鋭と多数Chaffの両方で挙動を比較
[ ] ShieldなしBuildと生存Roundを比較
[ ] Missile / Magic中心の相手で価値がどう変わるか確認
[ ] 片手Weaponとの組み合わせを実戦Test
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 176](../../data/items/by-id/176.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [用途別Magic Item辞典](../purpose-dictionary.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / armors / protections_by_armor / Item description
- Dominions 6 Main Manual — Shield / Encumbrance / Forge Item
- Vine拘束の実際の発生・抵抗・対象条件はゲーム内Battle Replayを最終確認
