---
title: "Frost Brand"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 54
---

# Frost Brand

**片手武器の命中にArmor PiercingのCold副次ダメージを重ね、Carrier自身にもCold Resistanceを足すConstruction 5の近接Item。**

Frost Brandは単純なDamage値だけでなく、**一回の命中で通常武器とColdの二つの処理を通すこと**、そして片手のままShield等と組みやすいことからThug装備として評価します。

- [Dominions 6.35固定データ — Item 54](../../data/items/by-id/54.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Magic Item総論](../index.md)

---

# まず何ができるか

6.35固定データでは、Frost BrandはConstruction 5、Forge要求**W1**の片手武器です。Item本体は装備者へ**Cold Resistance +5**を与えます。

参照するWeapon 82は、

- Damage 8
- Attack +1
- Defence +2
- Length 1
- 1 attack

の主武器で、さらに**常時発生するsecondary effect 765**を持ちます。

このsecondary effectを6.35のeffect tableで復号すると、**Damage 8 / Chill-Cold / Armor Piercing**です。

つまり攻略上は、

```text
主武器の命中
＋
8 Cold, Armor Piercing の副次ダメージ
```

として考えます。

---

# 「Damage 8の剣」だけで見ない

Frost Brandの強さは、主武器の表面Damageだけでは判断できません。

一回のHitにCold副次ダメージが重なるため、重要なのは、

- Carrierがそもそも命中できるか
- 一Roundに何回攻撃できるか
- 相手のProtectionだけでなくCold Resistanceがどうか
- Carrierが何Round生存して殴れるか

です。

強いCarrierへ持たせるほど、**Hit数 × 副次効果**の価値が積み上がります。

---

# Carrierは「当てて生き残る」ことが先

Frost Brandを持たせたいのは、武器だけで仕事を作るCommanderではなく、すでに近接戦へ入れる基礎能力を持つCarrierです。

確認するのは、

- Attackが敵Defenseへ届くか
- Protection / Resistanceが足りるか
- Fatigueで止まらないか
- Surroundされても数Round動けるか
- Retreat routeがあるか

です。

高価な武器を渡しても、最初の接敵で倒れるCarrierでは副次ダメージを活かせません。

---

# 片手武器であることの価値

Frost Brandは**1-h weapon**なので、もう一方の手へShieldを残せるCarrierではBuildを組みやすくなります。

典型的には、

```text
Frost Brand
＋ Shield / defensive hand slot
＋ Armor / Resistance / Reinvigoration
```

というように、Damageだけでなく生存性を別Slotから足します。

ただし手SlotにはBoosterや特殊Utilityも入るため、「片手だから必ず採用」ではありません。

---

# Cold Resistance +5は副次的な防御

Item本体はCarrierへCold Resistance +5を与えます。

これは、

- Cold damageが飛ぶ戦場
- Cold auraを持つ敵との接近戦
- 自軍のCold系Battle planと同居する場面

でBuildを整えやすくします。

ただし+5だけでCold対策が完成するとは限りません。敵のDamage量と他のResistance sourceを合わせて、**最終Resistanceをゲーム内Unit画面で確認**します。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- W1 Forge Mageを確保できる
- 近接Carrierがすでにいる
- Carrierが十分な命中率と生存力を持つ
- 敵のCold Resistanceが高すぎない
- 片手武器＋Shield等のBuildが成立する
- Weaponを作ることでRaid / PD処理 / 小規模迎撃の勝率が明確に上がる

**「このCarrierは何を何Roundで倒すのか」**をTest gameで確認できるならForge判断が安定します。

---

# Forgeしない・別装備を選ぶ条件

- 敵が高Cold Resistance中心
- CarrierのAttackが低く、そもそもHitしない
- Survival装備が足りず接敵後すぐ落ちる
- 高Protectionより別の防御軸が問題になっている
- Hand slotをBooster / Shield / 特殊Counterへ使いたい
- 近接戦ではなくBattle magicで解決すべき相手

Frost Brandは汎用的でも、**相手のResistanceとCarrier性能に依存する武器**です。

---

# Counter：Cold Resistanceだけで終わらない

敵がFrost Brand Carrierを出したら、Cold Resistanceは第一候補ですが、それだけでは主武器部分やCarrier本人の強さは残ります。

Counterは複数軸で考えます。

- Cold Resistanceを上げて副次ダメージを圧縮する
- 高Defense / Glamour等でHit数を減らす
- FatigueやControlで攻撃回数を減らす
- Armor Negating / MR系など別軸でCarrierを落とす
- Chaffで囲み、目的地へ到達させない
- Remote / Assassinationで戦場前にCarrierを狙う

要するに、**副次効果を耐える**か、**そもそも殴らせない**か、**Carrierを別軸で処理する**かです。

---

# よくある失敗

## WeaponだけでThugが完成したと思う

Frost BrandはDamage源です。命中、生存、Fatigue、MR、Retreatなどは別途必要です。

## Cold Resistanceの高い相手へ惰性で使う

副次ダメージの価値が落ちているなら、別のDamage typeへ切り替えます。

## 主武器Damageしか見ない

Weapon 82のsecondary effect 765まで含めて評価するItemです。

## Cold Resistance +5を完全耐性と思う

実際に受けるCold damage量と最終Resistanceを確認します。

## 高価なCarrierへ持たせて回収できない

小規模Raidで失うと、ItemだけでなくCommander本体まで失います。Riskと期待利益を合わせます。

---

# Test game checklist

```text
[ ] C5・W1でFrost BrandがForge可能か確認
[ ] Item 54 / Weapon 82であることを確認
[ ] 1-h weaponとして片手Slotを使うことを確認
[ ] CarrierのCold Resistanceが+5されることを確認
[ ] 主武器のDamage / Attack / Defence表示を確認
[ ] 命中時にCold副次ダメージが発生することをBattle Replayで確認
[ ] Cold Resistanceの異なる相手でDamage差を比較
[ ] Shield併用Buildと両手武器Buildを比較
[ ] 予定するPD / Raider / Thug相手へ実戦Test
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 54](../../data/items/by-id/54.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [用途別Magic Item辞典](../purpose-dictionary.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / weapons / effects_weapons / effect_modifier_bits / Item description
- Dominions 6 Main Manual — Weapon / Resistance / Forge Item
- Damage解決とCarrierの最終Statsはゲーム内表示・Battle Replayを優先
