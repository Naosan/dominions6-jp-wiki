---
title: "Endless Bag of Wine"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-25"
item_id: 379
---

# Endless Bag of Wine

**Supply +75を低いNature Pathから持ち運び、補給不足になる軍団だけを支えるConstruction 5の軽量Logistics Item。**

Endless Bag of Wineは「75体の兵を常に完全補給する袋」でも、ProvinceのSupplyを恒久改善する施設でもありません。攻略上は、**N1 MageのForge turnと少量のNature Gemを、移動できるSupply bufferへ変換するItem**として評価します。

- [Dominions 6.35固定データ — Item 379](../../data/items/by-id/379.md)
- [Magic Item攻略辞典](index.md)
- [Enormous Cauldron of Broth](enormous-cauldron-of-broth.md)
- [用途別Magic Item辞典](../purpose-dictionary.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [初心者Q&A：内政・補給・自動化](../../getting-started/logistics-faq.md)

---

# まず何ができるか

6.35固定データでは、Endless Bag of Wineは、

- Construction 5
- Forge要求 **N1**
- Base Gem cost **5N**
- Miscellaneous Slot
- **Supply +75**

を持ちます。

Item descriptionでは、創造の力を込めた酒袋が無限にWineを生み、痩せた土地でも最大75人ほどを養えると説明されています。

ただし攻略上は、説明文の「75 soldiers」を、

```text
どんなUnitでも必ず75体
```

と読み替えません。

UnitごとのSupply consumption、Army規模、Province側のSupply、季節、地形、敵地・包囲等を含めた最終的な不足量に対して、**Supply +75を足すItem**として扱います。

---

# Supply +75は「不足分を埋める値」

このItemの価値は、Armyの総Supply consumptionだけでは決まりません。

重要なのは、

```text
Armyが必要とするSupply
-
そのProvinceで得られるSupply
=
実際の不足量
```

です。

不足が小さいなら、Supply +75だけで問題を解消できる可能性があります。

不足が大きいなら、Bagを一個足しても不足が残ります。

そのため、

- 平地では足りるがWasteやMountainで不足する
- 自国では足りるが敵地で不足する
- 夏は足りるがWinterに崩れる
- 通常進軍では足りるがSiege中に不足する
- 増援合流後だけ不足する

といった**条件付きの補給穴**を埋めるのが得意です。

---

# Army全体の設計を変えるItemではなく、局所的なBuffer

Endless Bag of Wineは、巨大軍団を無条件に維持する万能解ではありません。

```text
不足量がSupply +75以内
→ 一袋で任務が安定する可能性が高い

不足量がSupply +75を大きく超える
→ Army分割、別Supply Item、Province選択、兵種構成の見直しが必要
```

というItemです。

特に価値が高いのは、

- 高価な主力Armyがあと少しだけSupply不足
- Raider群ではなく、一つの主力軍を安定させたい
- Supplyの良い経路から一時的に外れる
- 冬季や荒地を数Turnだけ通過する
- 敵Fort前で停滞する可能性がある

場合です。

---

# CarrierがArmyと一緒にいることが前提

Supply Itemは、倉庫へ置いておくだけでは前線を支えません。

基本運用は、

```text
Bagを持つCommander
＋
補給したいArmy
→ 同じProvinceを移動する
```

です。

Carrier候補は、

- 主力Armyから離れないCommander
- 戦闘で前線へ突出しない
- Retreat・暗殺・遠隔攻撃で失いにくい
- Misc Slotに他の必須Itemが少ない
- Army再編時にBagを受け渡しやすい

Unitです。

高価なMageへ持たせる必要はありません。Itemの効果を維持しながら生存できる安価なCommanderで十分な場合があります。

---

# Armyを分割するとBagも一方にしか残らない

Supply Itemの見落としやすい制約は、Army分割です。

一つのArmyを、

- Main Army
- Siege detachment
- Reinforcement column
- Raider group
- Retreat routeを守る予備隊

へ分けると、Bagを持つCommanderと同行する部隊だけが同じ補給計画を使えます。

```text
一袋で一つの大軍を支える
```

ことと、

```text
複数の小軍へSupplyを配る
```

ことは別です。

後者では、Bagを複数作る、別Supply Itemを配る、Armyの移動経路を分けるなどが必要になります。

---

# Construction 5だがForge要求はN1

Endless Bag of Wineは、Research上はC5まで必要ですが、ForgeするMageはN1で足ります。

これは、

```text
Research条件は重い
Path条件は軽い
```

Itemです。

NationにNature Mageが少なくても、N1を一人確保できれば量産候補になります。

一方、補給問題が序盤から発生しているのにConstruction 5へ寄る計画がない場合、解禁が間に合わないことがあります。

C5へ到達する頃には、Army規模・前線・季節が変わっているため、**解禁時点で実際にSupply不足が残っているか**を再確認します。

---

# Enormous Cauldron of Brothとの違い

[Enormous Cauldron of Broth](enormous-cauldron-of-broth.md)は、C3・N3からSupply +150を与えます。

| Item | Research | Forge要求 | Base cost | Supply | Slot |
|---|---:|---:|---:|---:|---|
| Endless Bag of Wine | C5 | N1 | 5N | +75 | Misc |
| Enormous Cauldron of Broth | C3 | N3 | 15N | +150 | Misc |

両者は単純な上位・下位関係ではありません。

```text
早いResearchと高いNature accessがある
→ Cauldronを先に使える

高Nature MageはないがC5へ進む
→ Bagを多くのN1 Mageから作れる
```

という入口条件の違いがあります。

また、Supply不足が60ならBagで足ります。150を必要としないArmyへCauldronを作ると、使われないSupplyへ追加Gemと高Path MageのForge turnを払うことになります。

---

# 数ではなく「何Turn使うか」で評価する

Supply Itemは一戦だけの装備ではありません。

価値は、

```text
不足を防げるSupply
×
危険地帯で使うTurn数
×
守るArmyの価値
```

で考えます。

一Turnだけ荒地を通るために作る価値は、Armyの重要度によって変わります。

逆に、毎冬同じ前線で不足する、長いSiegeを繰り返す、複数戦線で持ち回れるなら、5NとForge turnを長期間回収できます。

---

# Battle用Itemではない

Endless Bag of Wineは、

- Protection
- MR
- Regeneration
- Reinvigoration
- Damage
- Resistance

を直接増やしません。

BattleでCarrierが狙われた場合、Misc Slotを一つ使っているため、純戦闘装備より脆くなることがあります。

そのため、

```text
Map上ではSupply Item
Battleでは空いていないMisc Slot
```

という二面性があります。

前線Commanderへ持たせる場合、BagのせいでMR・Resistance・生存Itemを外していないかを確認します。

---

# 相性の良い運用

特に相性が良いのは、

- 大型Unitや重装兵を含む主力軍
- Winterや荒地を越える攻勢
- 敵Fort前で長期化しやすいSiege Army
- 補給の良いProvince間隔が広いMap
- 召喚増援が途中合流する軍団
- C5を他のItem目的でも研究するNation
- N1 Mageが多くForge turnを捻出しやすいNation

です。

一方、小規模Raiderが各地へ散る戦略では、一袋を共有できません。Raiderごとに配るとForge turnとMisc SlotのCostが急増します。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み、または他目的で向かっている
- N1 Forgerを確保できる
- Nature Gem 5を他の優先用途から回せる
- 実際のSupply不足が75以内、または75で大きく改善する
- Bagを持つCommanderがArmyと同行できる
- 同じArmyが複数Turnにわたり補給難へ晒される
- Starvation等による戦力低下が戦争計画を壊している
- CauldronのN3条件や15Nが重すぎる

「いつか役立つかもしれない」ではなく、次の進軍経路とArmy consumptionを見てForgeします。

---

# Forgeしない・後回しにする条件

- 現在のProvince Supplyだけで十分
- Armyを小さく分ければ問題が解消する
- C5 Researchが戦争Timingに間に合わない
- Misc Slotへ必須のMR・Resistance・Boosterがある
- Carrierが頻繁にArmyから離れる
- 補給不足が75を大きく超え、一袋では任務が変わらない
- Cauldron一個で大型Armyをまとめて支える方が安い
- Nature Gemが重要なSummon・Spell・別Itemに必要
- 進軍経路を一Province変えるだけでSupply問題を避けられる

Supplyが足りている時、Bagは戦闘能力を持たないMisc Itemになります。

---

# Counter：CarrierとArmyの結び付きを崩す

敵がEndless Bag of Wineで大軍を維持している場合、正面戦闘以外にも崩し方があります。

- Bagを持つCommanderを暗殺・遠隔攻撃・Rear attackで狙う
- Armyを複数方向へ対応させ、分割を強いる
- 補給の悪いProvinceへ誘導する
- FortやChokepointで停滞Turnを増やす
- Reinforcement合流でSupply需要が増える時を狙う
- CarrierがRetreat・移動失敗でArmyから離れる状況を作る
- Forge hubやNature Gem incomeへ圧力をかけ、代替Bagを作らせない

ただし、Item一個を失わせるために高価な作戦を使う価値があるかは、守られているArmyの規模で判断します。

---

# よくある失敗

## 「75 soldiers」と兵数だけで計算する

実際にはUnitごとのSupply消費とProvince側のSupplyがあります。最終表示とTurn結果で確認します。

## C5へ行けば序盤から使えると思う

Researchが必要です。補給問題が起きたTurnとC5到達Turnを比較します。

## 一袋で複数Armyを支えられると思う

Armyを分ければ、Itemを持つCommanderも一方にしか同行できません。

## CarrierがArmyから離れる

Scout、Research、Forge、Patrol等で別行動させると、補給計画が崩れます。

## Misc Slot競合を無視する

Supplyは足りても、MRやResistanceを失ったCarrierがBattleで倒れる場合があります。

## 不足量を測らず作る

Supply不足が15なら有効ですが、300ならBag一個では根本解決にならない可能性があります。

---

# Test game checklist

```text
[ ] C5・N1でForgeできることを確認
[ ] Base costが5Nであることを確認
[ ] Item 379 / Misc Slotであることを確認
[ ] 装備前後のSupply表示を比較
[ ] Supply +75が反映される範囲を確認
[ ] ArmyとCarrierが別Provinceになった場合を確認
[ ] Army分割時にどちらが恩恵を受けるか確認
[ ] Winter / Waste / Enemy territory / Siegeで比較
[ ] 複数所持時のStack挙動を確認
[ ] Starvation発生・解消のTurn timingを確認
[ ] Enormous Cauldron of Brothと同じArmyで比較
[ ] Misc Slotを戦闘Itemへ替えた場合のBattle結果を比較
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 379](../../data/items/by-id/379.md)
- [Enormous Cauldron of Broth](enormous-cauldron-of-broth.md)
- [用途別Magic Item辞典](../purpose-dictionary.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [初心者Q&A：内政・補給・自動化](../../getting-started/logistics-faq.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- BaseI: C5 / N1 / Misc / Supply +75
- generated Item record: Base cost 5N
- 「75 soldiers」はItem descriptionの表現。実際のSupply scope、Stack、Turn timingはゲーム内Army表示とTurn resultを優先