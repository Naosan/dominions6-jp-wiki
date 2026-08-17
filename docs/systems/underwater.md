---
title: 海・Underwater・Amphibious攻略
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
---

# 海・Underwater・Amphibious攻略

海を扱うときは、単に「水中へ入れるか」だけでは足りません。

```text
移動できるか
→ 兵を連れて行けるか
→ 水中で武器・Spellが働くか
→ Fort・Lab・Templeを生産拠点にできるか
→ 陸へ出た後も同じArmyが戦えるか
→ Retreat先があるか
```

まで一つの作戦として考えます。

このページでは、Aquatic、Amphibious、Poor Amphibian、Water Breathing、Coastal Recruit、海陸侵攻を整理し、[MA Atlantis — Kings of the Deep](../nations/ma/atlantis.md)を主要例にします。

!!! warning "現在のUnit popupを優先"
    Underwaterで使用できるWeapon、射撃、Fire系効果、Mount、形態、Poor Amphibian penalty等は個別Unit・Spellで異なります。分類名だけで決めず、現在のゲーム内popupとBattle Replayを確認してください。

---

## 最初に覚える十項目

| 項目 | 最初の理解 |
|---|---|
| Aquatic | 水中を本拠とし、通常は陸上行動へ強い制限がある |
| Amphibious | 海と陸の両方へ自力で移動できる |
| Poor Amphibian | 両環境へ行けるが、不適環境で能力Penaltyを受ける |
| Water Breathing | 非Amphibious Unitを水中へ同行させる輸送能力 |
| Gift of Water Breathing | Commanderが一定量の兵へ水中呼吸を与える能力 |
| Coastal Recruit | Coast Province等、地形・接続条件で得るRecruit |
| Underwater Fort | 海中のRecruit・Mage・Lab・Templeを守る拠点 |
| Darkvision | 深海・暗いBattlefieldでの能力低下を軽減する |
| Retreat | 海陸境界・敵支配・接続により安全な退却先が変わる |
| Landfall | 海から陸へ出る作戦。占領後の補充・Mage・Supplyまで必要 |

---

# Unit分類

## Aquatic

Aquatic Unitは水中活動を前提とします。

攻略上は、

- 水中で本来性能を発揮する
- 陸上へ出られない、または特殊手段が必要
- 陸上Fort攻略へそのまま使えない
- 海中防衛では高い価値を持つ

という意味です。

Aquatic Armyだけで海を制圧しても、陸上Throneや敵Capitalへ届かない場合があります。

## Amphibious

Amphibious Unitは海陸を自力で移動できます。

しかし、

> Amphibiousだから海でも陸でも同じ性能

とは限りません。

- Weaponが環境で変わる
- 射撃が水中で使えない
- Mountや形態が変わる
- Darkvisionが必要
- Armor Encumbranceが異なる
- Map Moveと接続が違う

場合があります。

## Poor Amphibian

Poor Amphibianは不適環境でPenaltyを受けます。

使用前に、

```text
Attack
Defence
Combat Speed
Precision
Encumbrance
Map Move
```

を海・陸の両方で確認します。

Poor Amphibian Mageを陸へ出せても、Battle Mageとして予定したSpellを撃つ前に疲労・射撃で失う場合があります。

## Water Breathing

Water Breathingを持つUnitは自分だけ水中へ行けます。

Gift of Water Breathingを持つCommanderは、一定量の同行Unitへ水中呼吸を与えられます。

重要なのは、

```text
Commander本人が入れる
≠
全Squadを連れて入れる
```

ことです。

Army Setupと移動Arrowで、同行可能数を確認します。

---

# 海へ入る前のChecklist

```text
□ Commander本人はAquatic / Amphibious / Water Breathingか
□ 全Squadへ十分なGift of Water Breathingがあるか
□ Mount・Shapeが水中対応か
□ 水中で使えないWeapon・射撃へ依存していないか
□ MageのSpellがUnderwaterで使用可能か
□ Retreat先となるFriendly Sea Provinceがあるか
□ 敵のWater Mage・Poison・Cold・MR攻撃をScoutしたか
□ 占領後にFort・Lab・Templeを建てられるか
```

一項目でも未確認なら、小規模Test Armyで移動とBattleを確認します。

---

# 海から陸へ出る

Underwater国家にとって、Landfallは国家の転換点です。

海中で勝っていても、陸上へ出られなければ、

- Land Throne
- Enemy Capital
- 高Income Land Province
- 多くの外交対象

へ影響できません。

## Landfallの五段階

```text
1. CoastをScoutする
2. 上陸Armyを海中で編成する
3. 同Turn到着するMage・Commanderを確認する
4. Coastを占領する
5. 陸上Fort・Lab・補充経路を作る
```

## 最初のCoast

最初の陸上Provinceは、Incomeだけでなく、

- 隣接Sea数
- Retreat route
- Fort候補
- Lab建設
- Coastal Recruit
- 敵Capitalまでの距離
- Throne・Choke

で選びます。

## 一歩後ろの海を残す

すべてのArmyを陸へ出すと、敗北時のRetreat先を失います。

```text
上陸Army
＋ 海中予備Army
＋ 海側の補給・輸送Commander
```

を分けます。

## 陸上Recruitの確保

Amphibious国家でも、陸上では、

- Independent Commander
- Archer
- Cheap Patrol
- Siege unit
- Nature / Air等のIndependent Mage

が重要です。

海中Rosterだけで全役割を賄わず、Land Recruitを国家へ取り込みます。

---

# 陸から海へ攻める

通常陸上国家が海へ入る場合、輸送能力が主制約です。

## Commanderを先に用意する

```text
水中呼吸を与えるCommander
→ Squad capacity
→ Gift量
→ Escort
→ Gem・Item
```

を確認します。

Commander一人へ全ArmyのWater Breathingを依存すると、Commander死亡で退却・再侵攻が難しくなります。

## ItemとSpell

Water Breathing Item、Transformation、Summon、Ritual等で侵攻できます。

ただしItemを装備できるCommander数と、同行可能兵数は別です。

```text
Item一個
→ Army全体が海へ入れる
```

とは限りません。

## 海中Battle用の再Script

陸上で機能した、

- Fire
- Archer
- Cavalry charge
- Flying rear attack
- Mount

が水中で同じように働くとは限りません。

海へ入る前にScriptを複製せず、Underwater専用Scriptを作ります。

---

# Movementと接続

## 海陸境界

Map上で隣接して見えても、実際の移動接続、River、Plane、Cave、特殊Map ruleにより移動できない場合があります。

Arrowを出し、Map Move Costを確認します。

## Multi-turn movement

遠方Sea ProvinceへMulti-turn movementを使えますが、

- 中継Provinceの所有変更
- Sea Battle
- Blocker
- Commander能力差

で経路が変わります。

戦争中は毎Turn経路を再確認します。

## `Y`で到着予定Armyを確認

複数Sea ArmyをRally pointへ集める場合、`Y`で到着予定Armyを確認します。

同じ目的地を指定しても、

- Map Move
- Poor Amphibian
- 同行Unit
- Magic Phase movement

で到着Turnがずれることがあります。

---

# Retreat

Underwater戦で最も見落としやすいのがRetreatです。

## 安全な退却先

Battle前に、

```text
Friendly Sea Provinceがあるか
敵が同Turnに奪わないか
Commanderがその環境へ移動できるか
同行Unitが退却可能か
```

を確認します。

## 海陸の混成Army

Commanderは退却できても、同行Unitの一部が環境制限で失われる場合があります。

混成Armyでは、

- Amphibious Squad
- Gift対象Squad
- Aquatic Squad
- Poor Amphibian Squad

を分けておきます。

## Fort内のStorm

Underwater Fortでも、Storm戦の守備側Retreatは通常Field Battleと異なる危険があります。

壁、Relief Army、Break Siege、Storm Timingは[Forts](forts.md)を参照してください。

---

# Underwater Battle

## Darkvision

深海・暗いBattlefieldではDarkvision差が重要です。

敵がDarkvisionを持たないなら、

- Attack
- Defence
- Precision

の差を作れる場合があります。

一方、Atlantian、Aboleth、Deep One等は暗所適性を持つことが多く、Darknessを撃てば必ず有利とは限りません。

## 射撃

水中では使用できるMissile Weaponが限られます。

陸上でJavelinを使うUnitが水中では近接だけになる場合もあります。

Battle Replayで、

```text
射撃Weaponが表示されたか
Ammoを使ったか
射撃命令が別Orderへ変換されたか
```

を確認します。

## Fire・Heat

Fire系Spell・Weapon・Auraは水中で制限や挙動差を持つ場合があります。

Fire国家が水中へ入るときは、Spell listでCast可能か確認し、第二Damageを準備します。

## Poison

海中国家はPoison Weapon・Poison Barbsを持つ場合があります。

MA AtlantisのCoral weaponは追加Poisonを与え、Coral armorは接触した敵へPoison Barbsで反撃します。

対策は、

- Poison Resistance
- 射程を取る
- Undead・Inanimate等の適性Unit
- 高Damageで接触時間を短くする

です。

## SizeとSquare

Shambler、Lobster、Large Aquatic Unitは一Squareを大きく使います。

高HPでも、

- 前線幅
- 攻撃回数
- Harassment
- AoE被害
- Friendly Unitの詰まり

を確認します。

---

# Underwater Armyの役割分担

## Shield Screen

Shield BearerやCoral Guardが、

- 最初の接敵
- Javelin
- Poison Barbs
- Mageへの時間

を担当します。

## Damage dealer

Glaive、Shambler、Lobster、Elemental、Mage SpellがDamageを出します。

Shield兵だけでは高Protection・Regenerationへ不足します。

## Mage support

Water Mageは、

- Quickness
- Cold
- Water Elemental
- Protection・Defence支援
- Underwater summon

へ接続します。

Random Fire・Earth・Astralがある国家では、敵防御に合わせてCrosspathを使います。

## Transport・Logistics

Gift of Water Breathing Commanderは戦闘Mageと同じくらい重要です。

Transport Commanderを前衛へ置かず、Bodyguard・後方配置・予備を用意します。

---

# Coastal Recruitment

Coastal Recruitは、Coast Provinceや海陸条件で得られるUnit・Mageです。

## 価値

- 海中国家が陸上Mageを得る
- 陸上国家が海侵攻Commanderを得る
- Water / Astral accessを広げる
- Land Armyの補充を作る

## MA Atlantisの例

MA AtlantisはCoastで、

- Atlantian Light Infantry
- Soldier of the Deep
- Shambler Chief
- Initiate of the Deep
- Witness of the Deep

等を得られます。

特にWitness of the DeepはWater・Astralを陸側で供給する入口になります。

ただしCoastal MageがPoor Amphibianか、陸上でどのPenaltyを受けるかを確認します。

---

# Underwater Fort・Lab・Temple

## Fort

Sea Fortは、

- Mage生産
- Army保護
- Sea route control
- Retreat point
- Landfall準備

の中心です。

海は接続が少なくChokeになりやすいため、一Fortの価値が高い場合があります。

## Lab

Labは、

- Water Gem集約
- Booster
- Ritual
- Water Breathing Item
- Sea summon

へ必要です。

Landfall前に、海側Labと陸側LabのどちらでMageを再編するか決めます。

## Temple

TempleはDominion、Sacred Recruit、Priest、Throneへ関係します。

海中Templeが破壊されると、陸側へDominionをつなぐNetworkも弱くなります。

---

# Underwater経済

## Sea Provinceの価値

Sea Provinceは、

- Income
- Water Gem Site
- Sea-specific Site
- Coast接続
- Fort位置
- Retreat route

で評価します。

陸上国家から攻めにくいこと自体が防衛価値です。

## Site Search

Water Siteだけでなく、海中限定Site、Elemental Site、Mage Recruit Siteが国家上限を変えます。

Water Mageを一人だけ高位Ritualへ固定せず、Manual Search・Remote Search担当を分けます。

## Supply

Aquatic UnitでもSupplyを消費する場合があります。Need Not Eatとは別です。

Armyが大きくなる前にProvince SuppliesとUnit能力を確認します。

---

# MA Atlantisを例にした国家Engine

MA Atlantisは、

- AmphibiousなAtlantian兵
- Coral WeaponのPoison
- Coral ArmorのPoison Barbs
- Shield InfantryとGlaive Guard
- Shambler・Lobster
- Any-fort King of the Deep
- Any-fort Coral Queen H3
- Coast Mage
- 深いWater Magic

を持ちます。

国家Engineは、

```text
海中で安全にExpansion
→ King of the Deepを増やす
→ Water GemとSea Siteを確保
→ CoastへLandfall
→ Coastal Mage・Independent Recruitを取り込む
→ Water MagicとRandom Fire / Earth / Astralで陸戦へ適応
```

です。

詳しくは[MA Atlantis国家攻略](../nations/ma/atlantis.md)を参照してください。

---

# Underwater国家へのCounter

## CoastをFort化する

海中国家のLandfall候補を限定します。

## Poison Resistance

Coral weapon・Poison Barbsの交換効率を下げます。

## Sea routeをScoutする

海中Armyは見えにくく、Coastへ突然現れることがあります。

Scout、Remote Search、Patrol、Coast PDを組み合わせます。

## Transport Commanderを狙う

Water Breathingを与えるCommanderを倒すと、Army全体の移動計画を壊せます。

## Landfall直後を狙う

陸上Fort・Lab・Recruit networkが完成する前は、海中国家の補充が細い場合があります。

```text
Coastを取った直後
→ Fort建設中
→ Mage・補充が未整備
```

が反撃Timingです。

## Missing Pathを突く

MA AtlantisはWaterが深い一方、Air・Death・Nature・Glamour・Bloodへ自然には届きにくい構造です。

Shock、Poison Resistance、Disease、MR等、PretenderやSite Mageへ依存する防御を狙います。

---

# Battle Replayで見るもの

```text
1. 海・陸でUnit statsが変わっていないか
2. Missile Weaponが実際に使われたか
3. Poison damageが何Round後に効いたか
4. Poison Barbsが誰へ返ったか
5. Large Unitが前線で詰まっていないか
6. Darkvision差が命中へ影響したか
7. MageがUnderwater不可Spellを飛ばしていないか
8. Retreat時にどのUnitを失ったか
9. Transport Commanderが生存したか
10. Water Gemを予定以上に消費していないか
```

---

# 毎Turn Checklist

```text
□ SeaとLandのArmyを別に確認した
□ Water Breathing capacityを超えていない
□ CoastのScoutとPDを確認した
□ Landfall後のFort・Lab資金を確保した
□ Sea側のRetreat Provinceを残した
□ Coastal Recruitを確認した
□ Underwater用Scriptを使っている
□ Poison・Darkvision・Sizeの相性を確認した
□ Transport Commanderを前線へ出しすぎていない
□ Sea Site SearchとWater Gem輸送を確認した
```

---

# よくある失敗

## Commanderが水中へ入れるのでArmy全体も入れると思う

Gift of Water Breathing capacityが不足しています。

## Amphibiousなら同じScriptで戦えると思う

Weapon、射撃、Spell、Penaltyが環境で変わります。

## 海を統一してから陸を考える

Land Throne・外交・勝利条件へ遅れます。

## Landfall後にFortを建てない

補充とRetreatが細く、反撃で海へ押し戻されます。

## 高位Water Mageを全員Battleへ使う

Site Search、Booster、Ritual、Sea summonが止まります。

## Poison weaponだけで高Poison Resistanceを殴る

通常Damage、Cold、MR、Earth、Astral等の第二案が必要です。

## Giant LobsterやShamblerをHPだけで評価する

Size、Defence、MR、前線幅、補充費を見落とします。

## 海中Fortを安全だと思い込む

敵が侵攻手段を完成させると、接続の少なさが退却の少なさへ変わります。

---

## 関連ページ

- [MA Atlantis — Kings of the Deep](../nations/ma/atlantis.md)
- [Province](province.md)
- [Forts](forts.md)
- [戦闘ルール](../basics/combat-rules.md)
- [命令とBattle Script](../basics/orders.md)
- [Water](../magic/paths/water.md)
- [Magic Access到達経路](../magic/magic-access-routes.md)
- [特殊能力](../reference/special-abilities.md)
- [操作方法・ショートカット](../getting-started/shortcuts.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [MA Atlantis community reference](https://illwiki.com/dom5/dom6/atlantis-ma)
