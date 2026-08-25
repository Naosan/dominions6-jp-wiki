---
title: "Enormous Cauldron of Broth"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-25"
item_id: 341
---

# Enormous Cauldron of Broth

**Supply +150をConstruction 3から一つの軍団へ持ち込み、大型Armyの補給不足を早期に埋める高Path・大容量Logistics Item。**

Enormous Cauldron of Brothは、Researchが早い代わりにN3 Forgerと15Nを要求します。攻略上は、**高いNature accessを早期の大容量Supplyへ変換し、主力軍の進軍可能な地形・季節・滞在Turnを広げるItem**として評価します。

- [Dominions 6.35固定データ — Item 341](../../data/items/by-id/341.md)
- [Magic Item攻略辞典](index.md)
- [Endless Bag of Wine](endless-bag-of-wine.md)
- [用途別Magic Item辞典](../purpose-dictionary.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [初心者Q&A：内政・補給・自動化](../../getting-started/logistics-faq.md)

---

# まず何ができるか

6.35固定データでは、Enormous Cauldron of Brothは、

- Construction 3
- Forge要求 **N3**
- Base Gem cost **15N**
- Miscellaneous Slot
- **Supply +150**

を持ちます。

Item descriptionでは、空にしても自動的にBrothが満ち、兵から好まれてはいないものの大量の食料を供給すると説明されています。

固定効果はSupply +150です。

```text
装備者が持ち運ぶSupply source
```

であって、Provinceの人口・Income・恒久Supplyを増やす施設ではありません。

---

# 大型Armyの不足を一枠で埋める

Supply +150は、[Endless Bag of Wine](endless-bag-of-wine.md)の+75より大きい値です。

この差が生きるのは、

- Giantや大型Summonを含む
- 重装兵を大量にまとめる
- 複数の軍団が合流する
- Siegeで長期間同じProvinceへ留まる
- Winterや荒地を越える
- 敵地でProvince Supplyが足りない

場合です。

重要なのは、Armyの総兵数ではなく、

```text
実際のSupply不足がどれだけ残っているか
```

です。

不足が120ならCauldron一個で解消できる可能性があります。

不足が20なら、Supply +150の大半は使われません。

---

# Construction 3は早いが、N3は軽くない

CauldronはC3で解禁されます。

Researchだけ見ればEndless Bag of WineのC5より早いItemです。

しかし最初の一個にはN3 Mageが必要です。

```text
Research条件：早い
Path条件：高い
```

という入口です。

Nationに、

- native N3 Mage
- Random込みでN3へ届くMage
- Pretender
- Hero
- Summon
- Booster込みのN3 Forger

がいるかを確認します。

N2までしかないNationでは、C3へ到達してもCauldronを作れません。

---

# Endless Bag of Wineとの入口条件は逆

二つのSupply Itemは、ResearchとPathの条件が逆転しています。

| Item | Research | Forge要求 | Base cost | Supply | Slot |
|---|---:|---:|---:|---:|---|
| Enormous Cauldron of Broth | C3 | N3 | 15N | +150 | Misc |
| Endless Bag of Wine | C5 | N1 | 5N | +75 | Misc |

```text
高Nature Mageが早期からいる
→ CauldronをC3で投入しやすい

高Nature MageはいないがN1は多い
→ C5後にBagを量産しやすい
```

という違いです。

「CauldronはBagの上位Item」とだけ覚えると、Forge accessとGem効率を見落とします。

---

# 一個の大軍か、複数の小軍か

Cauldronは一つの大軍へSupplyを集中させるのが得意です。

一方、Armyを二方向へ分けると、Cauldronを持つCommanderは一方にしか同行できません。

```text
主力一軍を維持
→ Cauldronの+150をまとめて使える

二軍へ分割
→ 片方だけがCauldronを持つ
```

となります。

複数戦線では、

- Bagを各Armyへ配る
- Cauldronを複数作る
- 一軍だけ補給難Routeへ送り、他方はSupplyの良いRouteを使う
- Army規模そのものを調整する

必要があります。

---

# Carrierは軍団のLogistics node

Cauldronを持つCommanderは、単なる荷物持ちではなく、Armyの補給計画を支えるnodeになります。

向くCarrierは、

- 主力Armyから離れない
- Battleで前線へ出ない
- Rout・暗殺・Rear attackで失いにくい
- Misc Slotの戦闘需要が低い
- Armyの分割・合流時にItemを受け渡しやすい
- Map Moveが軍団へ追従できる

Commanderです。

高いNature MageがForgeした後、そのMage自身が持ち続ける必要はありません。より安全で安価なArmy Commanderへ渡せるなら、ForgerをResearch・Ritual・別Forgeへ戻せます。

---

# 高Path MageのForge turnもCost

CauldronのCostは15Nだけではありません。

N3 Mageの一Turnを使います。

そのTurnにN3 Mageができた可能性がある仕事は、

- Research
- Site Search
- Ritual
- Summon
- Battlefield preparation
- 別ItemのForge
- 前線移動

です。

```text
Cauldronで防ぐ補給損失
>
15N + N3 Mageの一Turn + Misc Slot
```

となるかを見ます。

特にN3 Mageが希少なNationでは、Supply不足がまだ発生していない段階で予備Cauldronを量産すると、Magic economy全体を遅らせます。

---

# Supply +150を使い切る必要はない

効果を完全に使い切れなくても、Armyを守れるならItemは有効です。

ただし、常にSupply不足が30程度なら、5NのBagで十分な可能性があります。

判断は、

- 現在の不足量
- Armyが今後さらに増えるか
- Winterにどれだけ悪化するか
- Siegeで何Turn停滞するか
- 次のProvinceのSupply
- Armyを分割する予定

で行います。

Supply +150という大きな数字自体を価値とせず、**任務成功に必要な不足分**だけを評価します。

---

# 名前から移動Penaltyを推測しない

Item名は「Enormous Cauldron」ですが、6.35固定データ上、Cauldron固有のMap Move penaltyやEncumbrance fieldをSupply +150とは別に確認していません。

そのため、

```text
巨大だからCommanderが遅くなるはず
```

とは書きません。

装備前後のMap Move、Army movement、Battle statsに差があるかはTest gameで確認します。

名前やFlavorと、固定fieldを分けることが重要です。

---

# Siege Armyとの相性

Fort前では、

- Armyが同じProvinceへ長く留まる
- 増援が合流する
- 敵の救援を待つ
- Storm準備中にTurnが増える

ため、補給問題が顕在化しやすくなります。

Cauldronは、短期の進軍だけでなく、**停滞する大型Armyを維持するItem**として価値があります。

ただし、Siegeの勝敗を直接早めるSiege Bonusはありません。

Supplyを確保してもFortを破る速度が不足しているなら、別のItem・Unit・Army構成が必要です。

---

# Battle用の防御を一枠失う

CauldronはMisc Slotを一つ使います。

CarrierがBattleへ参加する場合、

- MR
- Resistance
- Regeneration
- Reinvigoration
- Path Booster
- Penetration

のどれかを装備できなくなる可能性があります。

主力Mageへ持たせるなら、補給を得た結果、Battle Scriptを完遂できなくなっていないかを確認します。

Cauldronを安価なCommanderへ移せるなら、戦闘MageのSlot競合を避けられます。

---

# Forgeする条件

次が揃うほど価値が高くなります。

- Construction 3へ到達済み
- N3 Forgerを確保できる
- Nature Gem 15を回せる
- 実際のSupply不足が大きい
- 一つの主力ArmyへSupplyを集中させる
- Winter・荒地・敵地・Siegeで複数Turn使う
- CarrierをArmyと同行させられる
- Bag一個では不足が残る
- Armyを小さく分けると戦術上の強みを失う

特に「大軍であること自体が勝ち筋」のArmyでは、CauldronがArmy分割を避けるための投資になります。

---

# Forgeしない・後回しにする条件

- N3 accessがなく、Booster chainが重い
- Supply不足が75以下でBagが安い
- Armyを複数戦線へ分ける予定
- Nature GemがSummon・Battle magic・別Itemに必要
- N3 MageのForge turnが希少
- Province routeを変えれば補給できる
- ArmyがFort前へ長く留まらない
- CarrierのMisc Slotに必須Itemがある
- 補給不足以外の敗因が先にArmyを止める

Cauldronは強いSupply Itemですが、Supplyが敗因でない戦争では15Nの荷物になります。

---

# Counter：大容量Supplyを一人へ集中する弱点を突く

敵がCauldron一個で大型Armyを維持しているなら、Carrierの喪失がArmy全体へ影響する可能性があります。

Counterは、

- Cauldron Carrierを暗殺・Rear attack・遠隔攻撃で狙う
- Armyを複数方向へ対応させ、分割を強いる
- 補給の悪いProvinceで停滞させる
- Fort救援を遅らせ、Siege Turnを伸ばす
- 増援合流後のSupply peakを狙う
- Retreat routeを乱し、CarrierとArmyを離す
- Nature Gem incomeやForge拠点をRaidする

です。

ただしCarrierが安価でも、Army内部の位置・Guard・Bodyguard・Formationによって狙いにくい場合があります。Battle Replayで実際の配置を確認します。

---

# よくある失敗

## C3なので誰でも早く作れると思う

最初のCauldronにはN3が必要です。ResearchとMagic accessを別々に確認します。

## Supply +150を兵数150と読む

Supply consumptionはUnitごとに異なります。Army表示とProvince Supplyを見ます。

## 小軍へ分けた後も全軍が恩恵を受けると思う

Itemを持つCommanderは一方のArmyにしか同行できません。

## N3 Mageへ持たせ続ける

Forger自身がCarrierである必要はありません。安全なArmy Commanderへ受け渡せるか確認します。

## Supply問題がないのに作る

大きい数字でも、補給が足りているArmyには直接の戦闘価値がありません。

## Misc Slot競合を見ない

CarrierがBattlefield casterなら、MR・Resistance・Boosterを失うCostがあります。

---

# Test game checklist

```text
[ ] C3・N3でForge可能か確認
[ ] Base costが15Nであることを確認
[ ] Item 341 / Misc Slotであることを確認
[ ] Supply +150が装備後に反映されることを確認
[ ] CarrierとArmyが同じProvinceにいる場合を確認
[ ] Carrierが別Provinceへ移動した場合を確認
[ ] Army分割時のSupply表示を確認
[ ] Winter / Waste / Enemy territory / Siegeで比較
[ ] Endless Bag of Wineとの不足解消量を比較
[ ] 複数CauldronまたはBag併用時のStackを確認
[ ] Map MoveやBattle statsに固有Penaltyがないか確認
[ ] Carrier死亡・Retreat後の次Turnの補給を確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 341](../../data/items/by-id/341.md)
- [Endless Bag of Wine](endless-bag-of-wine.md)
- [用途別Magic Item辞典](../purpose-dictionary.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [初心者Q&A：内政・補給・自動化](../../getting-started/logistics-faq.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- BaseI: C3 / N3 / Misc / Supply +150
- generated Item record: Base cost 15N
- Item名から移動Penalty等を推測せず、Supply scope、Stack、Army分割時の挙動はゲーム内表示とTurn resultを優先