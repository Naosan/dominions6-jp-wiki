---
title: "Boots of Quickness"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 299
---

# Boots of Quickness

**装備者へQuicknessを与え、戦闘中の移動と近接攻撃のTempoを大きく上げる一方、Spell詠唱は速めず、加齢も早めるConstruction 7のBoots。**

Boots of Quicknessは単純な移動装備ではありません。攻略上は、**一RoundあたりにCarrierが行える近接行動を増やし、Weapon・proc・接敵Timingの価値を増幅するItem**として評価します。

- [Dominions 6.35固定データ — Item 299](../../data/items/by-id/299.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Thug・SC装備](../thug-equipment.md)
- [Magic Item総論](../index.md)

---

# まず何ができるか

6.35固定データでは、Boots of QuicknessはConstruction 7、Forge要求**W2**のBootsで、装備者へ**Quickness**を与えます。

Item descriptionでは、戦闘中に装備者が、

- 通常より大幅に速く移動する
- 通常より大幅に速く攻撃する
- Spell castingの速度は変わらない
- 通常より速く年を取る

ことが明記されています。

このため、

```text
近接Carrierの行動増幅Item
```

であって、

```text
Casterの詠唱回数を増やすItem
```

ではありません。

---

# 一撃を強くするのではなく、行動密度を上げる

Boots of QuicknessはWeapon Damageを直接増やしません。

代わりに、Carrierが有効に動ける時間の中へ、より多くの移動と攻撃を詰め込みます。

したがって価値は、

- 一回の攻撃がどれだけ強いか
- Weaponへsecondary effectがあるか
- Carrierが命中できるか
- 敵へ到達するまで何Round掛かるか
- 増えた攻撃を支えるFatigue余力があるか

で決まります。

弱い攻撃を増やしても、高Protectionの敵へ通らない場合があります。

逆に、強いWeaponやHit時効果を持つCarrierでは、**Hit機会の増加がDamage総量を大きく変える**ことがあります。

---

# 接敵TimingもDamageの一部

近接Carrierは、敵へ到達するまで攻撃できません。

Bootsによって戦場移動が速くなると、

- Missileを受ける時間を短くする
- 後衛へ早く圧力を掛ける
- 敵のBuff完了前に接触する
- 退却する敵へ追いつく
- 目的のSquadへ到達する

可能性が変わります。

ただし最短距離で動くことが常に有利とは限りません。

Carrierだけが先行してArmyから孤立すると、集中攻撃を受けることがあります。FormationとBattle orderを含めてTestします。

---

# Spell castingは速くならない

Item descriptionが特に重要なのは、**Spell castingはQuicknessの影響を受けない**と明記している点です。

詠唱には魔力を集める時間が必要で、Bootsの身体的な速度では短縮されません。

そのため、

- 後方でSpellだけを唱えるMage
- Boosterが必要なCaster
- PenetrationやRangeを伸ばしたいMage

へ装備しても、期待した「一Roundに二回詠唱」は得られません。

Combat Casterへ使うなら、

```text
Self-buffを唱える
→ 接敵後は近接戦を行う
```

という後半の役割に価値があるかを確認します。

---

# Fatigue管理がさらに重要になる

行動が増えるBuildでは、Fatigue推移を再確認する必要があります。

Carrierが、

- 高Encumbrance Armor
- 複数のSelf-buff
- 重いWeapon
- 長期戦
- 敵のFatigue attack

を抱えている場合、攻撃Tempoが上がっても早く機能停止することがあります。

[Girdle of Might](girdle-of-might.md)等のReinvigoration sourceと組み合わせ、

```text
攻撃回数が増えたか
＋
有効に攻撃できるRoundが維持できたか
```

を両方確認します。

---

# 相性の良いCarrier

特に相性が良いのは、

- 既に命中率とDamageを確保している
- WeaponやHit時効果の一回あたりの価値が高い
- 近接戦へ入る生存力がある
- Fatigueを管理できる
- 敵へ早く到達する意味がある
- Boots Slotを他の必須Itemへ使わない

Carrierです。

BootsはCarrierの基礎性能を増幅します。

基礎Buildが成立していないCommanderへ履かせても、**早く敵へ到達して早く倒される**だけになり得ます。

---

# Frost Brand等のHit時効果を増幅する

[Frost Brand](frost-brand.md)のように、一回の命中へsecondary damageが重なるWeaponは、Hit機会が増えるほど総効果も増えやすくなります。

同様に、

- 高Damageの片手Weapon
- Contact時の追加効果
- Life drain等のSustainを伴う攻撃
- 敵を早く減らすことで被Damageも減るBuild

ではQuicknessの価値が上がります。

ただし敵のDefenseやResistanceで攻撃が通らない場合、回数だけ増やしても期待値は伸びません。

---

# Regenerationとの組み合わせ

[Ring of Regeneration](ring-of-regeneration.md)はCarrierの生存Roundを伸ばし、Boots of Quicknessは各Roundの行動密度を上げます。

```text
Ringで戦える時間を増やす
×
Bootsで時間あたりの攻撃を増やす
```

という組み合わせは強力になり得ます。

ただし、

- MR
- Elemental Resistance
- Fatigue
- Burst耐性

が不足していれば、二つの増幅効果を活かす前に倒されます。

---

# Boots Slotの機会費用

Boots Slotには、

- Winged Shoes
- Earth Boots
- Boots of the Messenger
- Terrain / movement utility
- Resistanceや特殊能力を持つBoots

を置けます。

Boots of Quicknessを採用すると、Flying、Path Booster、Reinvigoration、戦略移動等の別機能を失うことがあります。

**戦闘内のTempoと、戦闘へ到達するための戦略機動は別**に評価します。

---

# 加齢という長期Cost

Item descriptionでは、装備者が通常より速く年を取る副作用が明記されています。

一戦だけの装備では影響が見えにくくても、長期間持たせる場合は、

- Carrierの現在年齢
- Old Ageの開始時期
- DiseaseやAfflictionのRisk
- Itemを外して保管できるTurn
- 代替Carrierの有無

を考えます。

特に既に高齢のMageへ常時装備させる場合、戦闘性能だけでなくCampaign全体の寿命を確認します。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 7へ到達済み
- W2 Forge Mageを確保できる
- 強い近接Carrierが既にいる
- 一回の攻撃価値が高い
- 接敵Timingを早める意味がある
- Fatigueを管理できる
- Boots SlotへFlyingやBoosterが不要
- 加齢Riskを許容できる
- Test gameで攻撃回数と任務成功率が上がる

C7 Itemなので、研究投資とWater Gemの機会費用も含めます。

---

# Forgeしない・別Itemを選ぶ条件

- 純粋なSpell casterへ詠唱加速を期待している
- Carrierの命中率やDamageが不足している
- 接敵後すぐ倒される
- Fatigueで早期に機能停止する
- FlyingやPath Boosterが任務に必須
- 高齢Carrierへ長期間持たせたくない
- C7到達を別Schoolより優先する理由が薄い
- Water GemをBattle magicや別Forgeへ回す必要がある

Quicknessは強い増幅効果ですが、**増幅する基礎Buildが必要**です。

---

# Counter：速さを有効行動へ変えさせない

敵のBoots of Quickness Carrierへ正面から低密度の近接戦を挑むと、相手の行動回数を活かされます。

Counterは、

- Chaffや高Defenseで有効Hitを減らす
- Fatigue damageやControlで行動を止める
- Burst damageで増えた行動を使う前に倒す
- Missile / Battle magicで接敵前から削る
- Formationを広げ、重要Unitへ直進させない
- MR-based effectでHP以外を攻める
- Carrierを迂回してArmy・Mage・Provinceを狙う

のように、**速さを勝利へ変換できない状況**を作ります。

---

# よくある失敗

## Casterの詠唱が二倍になると思う

Item description上、Spell castingは速くなりません。

## 基礎性能の低いCommanderへ履かせる

弱い攻撃や低い生存力まで自動で改善するItemではありません。

## Fatigueを見ない

攻撃Tempoが上がっても、早期にFatigue 100へ達すれば総有効行動は伸びません。

## Carrierだけが先行する

Armyから孤立し、集中攻撃を受けることがあります。

## 加齢副作用を無視して常時装備する

高齢Mageや長期Campaignでは、戦闘外のCostが積み上がります。

---

# Test game checklist

```text
[ ] C7・W2でBoots of QuicknessがForge可能か確認
[ ] Item 299であることを確認
[ ] 装備後にQuicknessが表示されることを確認
[ ] Bootsなし／ありで一Roundの攻撃回数を比較
[ ] 敵へ接触するRoundを比較
[ ] Spell casting回数が増えないことを確認
[ ] RoundごとのFatigue推移を記録
[ ] Girdle of Might併用時のFatigueを比較
[ ] Winged Shoes等の代替Bootsと任務成功率を比較
[ ] Turn経過時の加齢をTest gameで確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 299](../../data/items/by-id/299.md)
- [Girdle of Might](girdle-of-might.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Frost Brand](frost-brand.md)
- [Winged Shoes](winged-shoes.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Thug・SC装備](../thug-equipment.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- Dominions 6 Main Manual — Quickness / Fatigue / Aging / Forge Item
- 攻撃回数・戦場移動・Fatigue・加齢の実挙動はゲーム内Unit画面、Battle Replay、Turn経過を優先
