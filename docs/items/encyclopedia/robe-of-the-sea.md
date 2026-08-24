---
title: "Robe of the Sea"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 251
---

# Robe of the Sea

**Water MageのWater Pathを+1し、装備者本人を陸上・水中の両方で呼吸可能にするConstruction 5のArmor型Booster。**

Robe of the Seaは単なるWater +1ではありません。攻略上は、**Magic accessの閾値越えと、海陸をまたぐMage物流を一つのArmor SlotへまとめるItem**として評価します。

- [Dominions 6.35固定データ — Item 251](../../data/items/by-id/251.md)
- [Magic Item攻略辞典](index.md)
- [Magic Path Booster](../boosters.md)
- [Water Bracelet](water-bracelet.md)
- [海・Underwater・Amphibious](../../systems/underwater.md)

---

# まず何ができるか

6.35固定データでは、Robe of the Seaは、

- Construction 5
- Forge要求 **W3**
- Armor Slot
- Armor record 230
- **Water +1**

を持ちます。

Armor record 230はMagic Robesで、Defence 0、Encumbrance 0の軽装です。

Item descriptionでは、

- Water MageのWater magicを助ける
- 装備者が水中でも陸上でも呼吸できる

と説明されています。

つまり、

```text
Water +1
＋
装備者本人の海陸呼吸
－
Armor Slot
```

を一つにしたItemです。

---

# Water +1は閾値で評価する

RobeのBooster価値は、Water表示が1増えたこと自体ではありません。

装備前後で、

- 新しくCastできるBattle spell
- 新しく実行できるRitual
- 新しくForgeできるItem
- 同じSpellを高PathでCastした場合のFatigue
- Water summonへの到達
- 次のBooster chain
- Underwaterで担当できる役割

がどう変わるかを確認します。

```text
W3 Mage
→ Robe of the SeaをForge・装備
→ W4として目的Spell / Ritual / Forgeへ到達
```

が基本です。

W+1しても現在のResearchで役割が増えないなら、RobeはGem、Forge turn、Armor Slotを寝かせています。

---

# W3 Forgeが最初の入口

Robe of the Seaを最初に作るにはW3 Forgerが必要です。

Water BraceletはW1でForgeできますがC7です。RobeはC5で解禁される代わりにW3を要求します。

```text
Robe of the Sea
→ C5
→ W3 Forgerが必要
→ Armor Slot
→ 海陸呼吸も得る

Water Bracelet
→ C7
→ W1 Forgerで作れる
→ Misc Slot
→ Water +1が中心
```

という違いがあります。

国家のWater accessが、

- W1～2中心
- W3を一人だけ持つ
- RandomでW3へ届く
- 海中Site MageやSummonでW3を得る

のどれかによって、最初のRobeの作りやすさが大きく変わります。

「Water Mageがいる」だけでなく、**誰が最初の一着をForgeするか**まで確認します。

---

# 海陸呼吸はCarrier本人の接続

Robe of the Seaの重要な固有用途は、装備者本人が水中でも陸上でも呼吸できることです。

これにより、

- 陸上Water Mageを水中Labへ入れる
- 水中Mageを陸上Fortへ出す
- 海中でForge・Ritualを担当する
- 海岸Frontの両側で同じBooster carrierを使う
- Underwater戦へ地上の高Water accessを持ち込む

といった運用が可能になります。

ただしItem descriptionが明示しているのは**装備者**です。

```text
Robeを着たCommander本人が海陸を行き来できる
≠
配下のArmy全体が水中へ入れる
```

ことに注意します。

同行Unit、Army size、Water breathing transport能力は別に確認します。

---

# Amulet of the Fishとの違い

[Amulet of the Fish](amulet-of-the-fish.md)は、主にAquatic Commanderを陸上へ出す接続Itemです。

Robe of the SeaはItem description上、装備者を水中・陸上の両方で呼吸可能にし、さらにWater +1を与えます。

```text
Amulet of the Fish
→ Misc Slot
→ Aquatic CommanderのLandfallを主目的にする
→ Path Boosterではない

Robe of the Sea
→ Armor Slot
→ 海陸の双方向接続
→ Water +1も得る
```

という違いです。

Aquatic Mageを一度だけ陸へ出すならAmuletの方が早く・軽く済む場合があります。

Water +1と海陸往復を同じCarrierへ必要とするならRobeの複合価値が高まります。

---

# Water Braceletとの違い

[Water Bracelet](water-bracelet.md)もWater +1を与えますが、解禁、Forge要求、Slotが異なります。

| Item | 解禁 | Forge要求 | Slot | 固有Utility |
|---|---:|---|---|---|
| Robe of the Sea | C5 | W3 | Armor | 装備者の海陸呼吸 |
| Water Bracelet | C7 | W1 | Misc | Water +1を低Path Forgerから供給 |

攻略上は、

```text
Robe
→ C5から使いたい
→ W3がいる
→ Armor Slotを使える
→ 海陸接続も必要

Bracelet
→ C7まで進む
→ W1しかいない
→ Armorを別防具へ残したい
```

と使い分けます。

両方を装備できるMageならWaterをさらに伸ばせますが、ArmorとMiscを同時に使う価値がある目的Spellを先に決めます。

---

# Armor Slotが最大の機会費用

Robe of the SeaはArmor Slotを占有します。

Armor recordは軽いMagic Robesで、重装Carrierを作る防具ではありません。

前線へ出すと、

- 高Protection Armor
- Elemental Resistance Armor
- [Elemental Armor](elemental-armor.md)
- [Shroud of the Battle Saint](shroud-of-the-battle-saint.md)
- 特殊防御・再生・変身系Armor

と競合します。

```text
Water +1と海陸接続で得る役割
vs
Battle Armorを失うCost
```

を比較します。

後方Ritualist、Forger、Site Search担当ならArmor Slotの防御Costは軽くなります。

前線Battle Mageでは、Robeを着たまま敵のMissile・Assassin・Flankerへ耐えられるかを確認します。

---

# 「水中へ行ける」と「水中で安全」は別

Robeで水中へ入れても、そこで安全に働けるとは限りません。

確認するのは、

- Underwaterで使えるSpell
- 水中で変わるWeapon・Missile・Fire系effect
- 敵のAquatic / Amphibious Army
- CarrierのProtection、MR、Resistance
- Retreat可能な隣接Province
- Lab・Fort・Supplyの位置
- Item受け渡し経路

です。

移動資格を得ただけで、Underwater combat適性、Army command、護衛まで自動的に得るわけではありません。

---

# 後方Infrastructureとしての価値

Robeは戦闘装備ではなく、海中と陸上のLabをつなぐ共有Infrastructureとして使えます。

たとえば、

```text
陸上Lab
→ W3 MageがRobeを着る
→ 海中Labへ移動
→ Ritual / Forge / Site Search
→ 別のMageへ受け渡す
```

という運用です。

海中でしか得られないMage、Site、Gem incomeを陸上のMagic economyへ接続するとき、Robe一着の価値が複数Turnにわたって続きます。

一方、Robeの所在を見失うとCarrierが海岸の反対側へ移動できなくなる場合があります。受け渡し先と帰路を先に決めます。

---

# Battle Mageへ持たせる場合

前線で使うなら、Water +1がScriptをどう変えるかを具体化します。

- 目的SpellのWater requirement
- 現在のResearch
- 必要Water Gem
- 装備前後のFatigue
- UnderwaterでSpellが使えるか
- Robeの低Protectionを護衛・配置で補えるか
- Battle後の撤退先が海陸どちらか

を確認します。

Water +1で強いBattle spellへ届いても、Carrierが初撃で倒れるならArmor Slotの選択が間違っています。

---

# Robeを共有する

Ritual・Forge用なら、一着を複数Mageで共有できます。

- 高Path Ritualを使うTurnだけ装備
- Water ItemをForgeするTurnだけ装備
- 海陸移動のTurnだけ装備
- 移動後に別Mageへ渡す

ことで在庫を減らせます。

ただし、海中Labと陸上Labの間ではItem輸送が地形資格に依存します。

Robeを運ぶCourier自身がどちらの地形へ入れるかまで確認します。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- W3 Forgerがいる
- Water +1で具体的なSpell・Ritual・Forgeが解禁される
- 陸上Mageを水中へ、または水中Mageを陸上へ出したい
- Armor Slotを防御装備へ使わなくても任務が成立する
- 海中Lab・Site・Frontを継続利用できる
- 一着を複数Turn・複数Mageで共有できる
- Water BraceletのC7を待てない

最も強いForge理由は、

```text
Robeがあることで、新しいWater閾値と新しい地形の両方へ同時に届く
```

場合です。

---

# Forgeしない・別Itemを選ぶ条件

- W3 Forgerを確保できない
- Water +1しても今のResearchでは役割が増えない
- 海陸移動が不要
- Carrierに高Protection Armorが必須
- Amulet of the FishだけでLandfall目的を満たせる
- C7のWater BraceletをW1から量産できる
- 同行Armyが水中へ入れず、Commanderだけ移動しても仕事がない
- 海中でCarrierを守るEscortがいない
- Robeを失うと海中access全体が止まるほど一着へ依存する

複合Itemは効果が多い分、**両方の効果を使わないと割高**になることがあります。

---

# Counter：海陸接続点とArmor不足を狙う

敵のRobe of the Sea Carrierを見たら、

- 素WaterとRobe込みWater
- 新しく届いたSpell / Ritual
- 海陸のどちらから来たMageか
- 同行Armyも水中適性を持つか
- Robe以外のArmorを外しているか
- その一着が敵の唯一の海陸接続か

を確認します。

Counterは、

- 海岸Provinceを押さえて移動routeを狭める
- CarrierをAssassination・Raidで狙う
- 低ProtectionをMissile・Flanker・Burst damageで突く
- Gem carrierを落として高Water Scriptを止める
- 水中ArmyとCommanderを分断する
- 別Frontを攻め、Robe Carrierの往復を強制する
- Item物流を乱して必要TurnにRobeを使わせない

など、**Path Boosterと地形接続の両方へPressureを掛ける**形になります。

---

# よくある失敗

## W+1だけを見て作る

目的Spell・RitualがなければRobeのPath部分が寝ます。

## Commander本人だけ水中へ入れることを忘れる

同行Unitの水中適性は別です。

## Armor Slotを軽視する

前線MageがRobeを着た結果、Protection不足でScript前に倒れます。

## Amulet of the Fishと同じ方向だけだと思う

Robeは説明文上、装備者を水中・陸上の両方で呼吸可能にします。

## W1で作れると思う

Robeの最初の一着にはW3が必要です。W1 ForgeはWater Braceletです。

## 帰路を決めずに海へ入る

Robeの受け渡しやCarrier喪失後に、別Mageが地形の反対側へ取り残されます。

---

# Test game checklist

```text
[ ] C5・W3でRobe of the SeaがForge可能か確認
[ ] Item 251 / Armor record 230であることを確認
[ ] 装備前後でWaterが+1されることを確認
[ ] Defence 0・Encumbrance 0のArmorであることを確認
[ ] 陸上Commanderが水中へ移動できるか確認
[ ] Aquatic Commanderが陸上へ移動できるか確認
[ ] 同行Unitが自動的に地形資格を得ないことを確認
[ ] W0のPathless bearerでWater表示がどうなるか確認
[ ] 目的Battle spell・Ritual・Forgeが新しく選べるか確認
[ ] Underwaterで目的Spellが使用可能か確認
[ ] Water BraceletとのSlot・Research・Forge条件を比較
[ ] Robeを別Mageへ渡した後の海陸移動routeを確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 251](../../data/items/by-id/251.md)
- [Magic Path Booster](../boosters.md)
- [Water Bracelet](water-bracelet.md)
- [Amulet of the Fish](amulet-of-the-fish.md)
- [海・Underwater・Amphibious](../../systems/underwater.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / armors / protections_by_armor / Item description
- Dominions 6 Main Manual — Underwater / Aquatic / Amphibious / Magic Path / Forge Item
- 海陸移動、同行Unit、Underwater spell、Pathless bearerの実挙動はゲーム内Map・Unit画面・Test gameを最終確認
