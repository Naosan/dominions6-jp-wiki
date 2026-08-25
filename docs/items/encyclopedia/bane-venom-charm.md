---
title: "Bane Venom Charm"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-25"
item_id: 375
---

# Bane Venom Charm

**装備者がいるProvinceを汚染し、そこへ集まるArmy・Commander・土地そのものへ長期的な損害を狙うConstruction 5のProvince sabotage Item。**

Bane Venom Charmは、Battle開始時に敵だけへPoison damageを与える装備でも、Carrierを安全に保つ暗殺道具でもありません。攻略上は、**安価な潜入CarrierとDeath Gemを、敵の集結地点へ持続的な病害Riskを送り込む特殊作戦Item**として評価します。

- [Dominions 6.35固定データ — Item 375](../../data/items/by-id/375.md)
- [Magic Item攻略辞典](index.md)
- [Stone Sphere](stone-sphere.md)
- [用途別Magic Item辞典](../purpose-dictionary.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

---

# まず何ができるか

6.35固定データでは、Bane Venom Charmは、

- Construction 5
- Forge要求 **D2**
- Base Gem cost **10D**
- Miscellaneous Slot
- 明示field **Disease**
- 明示field **Leper: 5**

を持ちます。

Item descriptionでは、

- Spyが敵Army付近の井戸を汚染するために使う
- 土地、作物、植物が病む
- 人間と獣もCharmの災いを受ける
- 強い保護RuneがあってもBearer自身が病に冒される
- Labから出されると、そのItemがあるProvinceを汚染し始める

と説明されています。

したがって、

```text
敵Provinceへ持ち込む妨害効果
＋
Carrier自身への副作用
＋
土地・Province規模のRisk
```

を一体として扱います。

---

# Combat ItemではなくProvince Item

Bane Venom Charmの主戦場はBattle画面ではありません。

目的は、

- 敵主力Armyの集結地点
- Fort救援軍の待機Province
- Siege camp
- 重要Mageが集まる研究・Forge拠点
- Reinforcementの中継点
- Throne防衛Armyの滞在地点

へCarrierを置き、時間を使って敵の運用を崩すことです。

```text
一回のBattleで敵を倒す
```

のではなく、

```text
敵が同じProvinceへ留まるCostを増やす
```

Itemとして考えます。

正確な発生率・対象・Population・Supply・Incomeへの影響は、固定field名とFlavorだけから数式化せず、Turn messageとProvince表示で確認します。

---

# 「敵だけに効く」とは限らない

Item descriptionは、Charmが**存在するProvinceそのもの**を汚染すると説明しています。

そのため、

- Carrier
- 同じProvinceにいる自軍
- 同盟相手や第三国
- Provinceの住民・土地

へ影響しないと決めつけません。

特殊作戦では、

```text
Target Provinceに敵がいる
≠
効果対象が敵だけ
```

です。

自軍のMain Army、重要Mage、PretenderがいるProvinceへ持ち込む前に、Friendly unitへの影響をTestします。

---

# Lab保管と装備状態を分けて確認する

説明文では「Labから出されると」汚染を始めるとされています。

しかし、

- LabのItem storageに置く
- Lab ProvinceでCommanderが装備する
- Lab Provinceから外へ移動する
- Commander inventoryに入れたままLabへ戻る

は別の状態です。

```text
Lab Provinceにいるから安全
```

とは断定しません。

Item storage内では発動しないのか、Commanderが装備した瞬間に発動するのか、Province移動後に始まるのかをTest gameで分けます。

この確認をせずにCapitalでCarrierへ渡すと、自国の重要拠点を汚染する可能性があります。

---

# Carrierは消耗前提で選ぶ

Item description自体がBearerも病に侵されると警告しています。

向くCarrierは、

- 安価で代替可能
- Stealthyまたは敵地へ入りやすい
- 失っても研究・外交・Army commandが止まらない
- 高価な装備を他に持たない
- 必要なProvinceへ到達できるMap Moveを持つ
- 捕捉されても国家全体の秘密を失わない

Commanderです。

Pretender、Hero、Unique Mage、高Path Forgerへ持たせると、Itemの副作用と敵Patrolの両方へ国家資産を晒します。

```text
CarrierはDelivery system
```

と割り切れるかが重要です。

---

# Stealthは安全保証ではない

Spy用途がFlavorで示されていても、Stealthy Carrierは無敵ではありません。

敵は、

- Patrolを増やす
- ProvinceへArmyを集める
- Scout / Spyを探す
- Movement routeを読む
- Borderを閉じる
- Detection能力を持つUnitを配置する

可能性があります。

Bane Venom Charmを持つCarrierが捕捉されると、

- Carrierを失う
- Itemを失う、または敵に渡る可能性がある
- 作戦意図が露見する
- 10DとForge turnを失う

Riskがあります。

Stealth値、Patrol強度、Province population、敵の対応をTestします。

---

# Targetは「敵が長く留まるProvince」

このItemは、敵がすぐ通過するProvinceより、長く滞在する地点で価値が高くなります。

候補は、

- Siege中の大軍
- Fort前の救援待機軍
- Research hub
- Blood Hunt拠点
- Summon集結地
- Throne防衛Province
- Chokepoint
- 冬季にArmyが止まりやすい地点

です。

```text
敵が一Turnで去る
→ 発動機会が少ない可能性

敵が複数Turn集結
→ 病害Riskを蓄積させる機会が増える
```

と考えます。

ただし、何Turnでどれだけ影響するかはTest結果を優先します。

---

# Disease fieldとLeper 5を勝手に数式化しない

generated recordには、

- Disease
- Leper: 5

が明示されています。

しかし、この二つだけから、

- 毎Turn5体がDiseaseになる
- Populationが必ず5%減る
- 全Living unitへ同じ確率で効く
- Undead / Inanimateへ完全無効
- CarrierのDiseaseが確定で一Turn目に付く

とは断定できません。

記事では、

```text
病害を起こすProvince-level Item
```

という用途を説明し、式・対象・Timingはゲーム内Testへ残します。

---

# 直接Damageより「選択を強いる」価値

Bane Venom Charmが強いのは、敵へ損害を出す時だけではありません。

敵に、

- Armyを移動する
- 重要Mageを分散する
- PatrolへUnitを割く
- Carrier捜索へTurnを使う
- 汚染された可能性のある拠点を放棄する
- Siege計画を短縮・中止する

選択を強いれば、作戦上の価値があります。

```text
実Damage
＋
敵の対応Cost
```

で評価します。

ただし敵が影響を受けにくいUnitだけで構成されている場合や、すぐ移動できる場合、圧力は小さくなります。

---

# C5・D2・10Dという入口

Bane Venom CharmはC5まで必要ですが、Forge要求はD2です。

多くのDeath Nationにとって、D2自体は高くない場合があります。

一方、10Dは、

- Skull Staff
- Skull Mentor
- Summon
- Death battlefield magic用Gem
- Reanimation・Ritual

と競合します。

```text
Charmが敵へ与える長期Cost
>
10D + Forge turn + Carrier
```

となるTargetがあるかを確認します。

敵Armyがすぐ移動する、Patrolが極端に強い、Targetが価値の低いProvinceなら回収しにくくなります。

---

# Carrierへ他の高価なItemを持たせない

潜入Carrierに、

- Booster
- MR Item
- Mobility Item
- Artifact
- 高価な防具

を追加すると、成功率が上がる場合があります。

しかし捕捉時の損失も増えます。

Bane Venom Charm作戦では、

```text
到達に必要な最小装備
```

を選びます。

Winged Shoes等でRouteを変える価値があっても、Item総額と敵Patrolを比較します。

---

# 自国Provinceでの受け渡しが最初の危険

作戦失敗は敵地へ入る前にも起きます。

- Capitalで装備する
- Friendly Fortで待機する
- Armyと同じProvinceを通る
- LabからCarrierへ渡した後、移動Orderを忘れる
- Borderで一Turn止まる

と、自国の価値あるProvinceへCharmを置くことになります。

安全な運用では、

1. 受け渡しProvinceを決める
2. CarrierのRouteを事前に確認する
3. 重要Armyと重ならないようにする
4. 装備したTurnから効果が始まるかTestする
5. 到達後の滞在Turnと撤退手段を決める

必要があります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- D2 Forgerを確保できる
- 10Dを特殊作戦へ回せる
- 敵が重要Army・Mageを一Provinceへ長く集める
- Stealthyまたは侵入可能な安価なCarrierがいる
- Target Provinceへ安全なRouteがある
- 自軍へのCollateral Riskを管理できる
- Enemy Patrolを突破できる見込みがある
- 通常戦闘では崩しにくい集結地点を間接攻撃したい

特に、敵がSiegeやThrone防衛で動けない時に価値が上がります。

---

# Forgeしない・後回しにする条件

- CarrierがTargetへ到達できない
- Enemy Patrolが強すぎる
- 敵Armyが毎Turn移動し、滞在しない
- 10DをBooster・Summon・Battle magicへ使う方が直接的
- 自国側の受け渡し・Routeで重要Provinceを汚染する
- 影響を受けるUnit分類が敵主力と噛み合わない
- 効果のTarget・TimingをTestしていない
- Short warで長期的な病害が間に合わない
- Carrierの損失が外交・研究・指揮を壊す

Bane Venom Charmは状況依存の特殊作戦Itemです。敵集結地点がない戦争では、通常装備より価値が低くなります。

---

# Counter：Carrierを探し、滞在をやめる

敵がBane Venom Charmを使っている可能性がある場合、

- ProvinceのPatrolを増やす
- 不審なDisease増加をTurnごとに記録する
- 重要Mageを一Provinceへ集中させすぎない
- Armyを短期間で移動させる
- Scout・Spy routeを監視する
- Border Provinceで潜入Carrierを捕捉する
- 汚染が疑われるProvinceから高価なCommanderを移す
- 敵Death Gem incomeとC5到達を情報として扱う

ことで対応します。

効果がCarrier・Itemの退去後も残るか、どのTurnで止まるかはTestします。分からない状態で「Carrierを殺せば即座に全て治る」とは断定しません。

---

# よくある失敗

## Battle Itemとして前衛へ持たせる

主効果はProvince sabotageです。Battle statsを直接上げるItemではありません。

## 敵だけに効くと思う

説明文はProvince全体とBearer自身への危険を示しています。Friendly影響をTestします。

## Lab Provinceなら装備しても安全と思う

Item storageとCommander装備は別状態です。発動Timingを確認します。

## 高価なSpyへ持たせる

Carrierは病害とPatrolの両方へ晒されます。消耗可能性を前提にします。

## 一Turnで大軍が壊れると思う

正確な速度・対象・確率は確認が必要です。長期作戦として計画します。

## Charmを持ったまま自軍へ戻る

帰還Route上のFriendly ProvinceもRiskになります。

## UndeadやInanimateへ必ず無効と決める

Unit classificationごとの対象をTestせず、古い知識で一般化しません。

---

# Test game checklist

```text
[ ] C5・D2でForge可能か確認
[ ] Base costが10Dであることを確認
[ ] Item 375 / Misc Slotであることを確認
[ ] generated recordのDisease / Leper 5を確認
[ ] Lab storage中にProvinceへ影響するか確認
[ ] Lab ProvinceでCommanderが装備した場合を確認
[ ] LabのないProvinceへ移動した場合を確認
[ ] Carrier本人へのDisease・Affliction Timingを確認
[ ] Friendly / Enemy / Neutral unitへの対象を確認
[ ] Living / Undead / Inanimate / Animal等で比較
[ ] Population / Income / Supply / Unrest表示をTurnごとに記録
[ ] 同じProvinceへ複数Charmを置いたStackを確認
[ ] Carrier・ItemがProvinceを離れた後の継続を確認
[ ] Stealth CarrierのPatrol捕捉率を比較
[ ] Carrier死亡・Retreat・捕捉時のItem処理を確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 375](../../data/items/by-id/375.md)
- [Stone Sphere](stone-sphere.md)
- [用途別Magic Item辞典](../purpose-dictionary.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- Item 375: C5 / D2 / Misc / Disease / Leper 5
- generated Item record: Base cost 10D
- Item descriptionはLab外でProvinceを汚染し、Bearerも病に冒されると説明
- Disease・Leperの式、対象、Stack、継続、Friendly影響は固定field名から推測せず、ゲーム内Turn resultとTest gameを優先