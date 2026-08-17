---
title: Flying・Storm・Air機動戦
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
---

# Flying・Storm・Air機動戦

Flying国家は、地形を無視して速く動くだけの国家ではありません。

> **敵が安全だと思う後方へ戦力を集中し、通常Armyより短い経路で局地的多数を作り、Stormで戦場条件を再設定する国家**

です。

一方でFlying Unitは、

- HP・Protectionが低い場合がある
- ArcherやAoEへ弱い
- Attack Rearで孤立する
- Stormで飛行を失う
- Supply・Retreat・Fort攻略は別問題

という制約があります。

このページでは、[MA Caelum — Reign of the Seraphim](../nations/ma/caelum.md)を主要例として、Strategic Flying、Battle Flying、Storm、Air Magic、迎撃、Raidを整理します。

!!! warning "RiderとMountは別"
    Dominions 6ではRiderとMountが別Statsを持ちます。RiderにFlying表示があっても、Mountを含む実際のMap Move・Battle挙動が同じとは限りません。Army Setup、Map arrow、Unit詳細を正本にしてください。

---

## 最初に覚える十項目

| 項目 | 最初の理解 |
|---|---|
| Strategic Flying | Map上で多くの地形Costを越えて移動経路を短縮する能力 |
| Battle Flying | 戦場で障害・前衛を越え、後方へ接近できる能力 |
| Attack Rear | 敵後方を狙うが、孤立・Target変化・迎撃Riskがある |
| Storm | 飛行・射撃・Air Spell等へ大きく影響するBattlefield条件 |
| Storm Immunity | Storm中も飛行等を維持する重要能力 |
| Storm Power | Storm中に性能が変化するUnit特性 |
| Air Magic | Lightning、Wind、Storm、Arrow対策、Mobilityを扱う |
| Friendly reinforcement | 自領への移動が侵攻より先に合流する場合がある |
| Destination battle | 飛行経路の途中ではなく、処理後の同一ProvinceでBattleになる |
| Retreat | 飛行できても、安全な退却先がなければArmyを失う |

---

# Strategic Flying

## 地形を越える

Flying Unitは、通常兵が苦手とする、

- Mountain
- Forest
- Swamp
- River
- Choke point

を短い経路で越えられる場合があります。

ただし、

```text
Flying
≠
無限距離
≠
敵Fortを無視
≠
海・Planeを自由に越える
≠
Supply不要
```

です。

Map画面のArrowとMove costを確認します。

## Armyは最も遅いUnitへ引かれる

Flying Commanderへ非Flying兵を同行させると、Army全体の移動が通常経路になる場合があります。

```text
Flying Commander
＋ 地上兵
＝ Flying Armyとは限らない
```

Squad、Bodyguard、Summon、Mountを確認します。

## 途中でBattleは起きない

二つのArmyのArrowがMap上で交差しても、経路上でBattleになるとは限りません。

Battleは、Movement処理後に同じ敵対Provinceへ存在したときに発生します。

飛行Armyを迎撃するには、

- 現在地を追う
- Arrowの途中へ立つ

より、

- 次のTargetを予測する
- Fort・Throneを守る
- Friendly reinforcementを集める
- Chokeではなく価値の高いDestinationを守る

方が確実です。

---

# Flying Armyの役割

## 1. 集中

離れたFortから一つのBattleへMage・兵を集めます。

```text
北のFlying Army ┐
中央のFlying Army├→ Border Fort
南のFlying Army ┘
```

通常兵より広い範囲から局地的多数を作れます。

## 2. Raid

- 低PD
- Lab
- Temple
- Tax route
- Fort建設中
- Retreat route

を狙います。

## 3. Relief

包囲されたFortやThroneへ、地上Armyより短い経路で救援します。

## 4. Retreat route切断

敵が退却しそうなProvinceを先に取ります。

## 5. Mage delivery

Air MageやPriestを必要な戦線へ移します。

ただし高価なMageを単独で飛ばすと、敵Scout・Assassin・PDに失うRiskがあります。

---

# Battle Flying

## Attack Rear

Attack Rearは、敵後方のArcher・Mage・Commanderへ接近するためのOrderです。

しかし実際のTargetは、

- 敵配置
- Unit speed
- Battlefield obstacle
- 最寄り敵
- Bodyguard
- Target消滅
- Rout

で変化します。

```text
Attack Rear
＝ 必ず敵Mageを攻撃する
```

ではありません。

## 孤立

飛行Unitだけが先に敵後方へ到達すると、

- 敵前衛
- Bodyguard
- Rear guard
- Archer
- Commander

から集中攻撃を受けます。

正面Armyが接敵するTimingと合わせます。

## Hold and Attack

飛行部隊を数Round待たせることで、

- 敵前衛を正面へ引き付ける
- Mage Scriptを進める
- Buffを受ける
- 後方を空ける

ことができます。

ただし待ちすぎると射撃を受けます。

---

# Storm

StormはBattlefield全体へ影響する重要条件です。

一般に、

- 多くのFlying Unitが飛べなくなる
- 射撃が不利になる
- Air Magicの一部Spellと能力が変化する
- Storm ImmunityやStorm Powerの価値が上がる

という効果があります。

正確な現行挙動はSpell descriptionとUnit traitを確認してください。

## 自軍がStormを使う理由

- 敵Flyingを止める
- 敵Archerを弱める
- Storm Power Unitを強化する
- Lightning・Air Spell計画へ接続する
- 自軍Storm-immune部隊だけを飛ばす

ためです。

## 自軍がStormで困る場合

Flying国家だからといって、常にStormが有利とは限りません。

- 自軍の大半も飛べない
- Attack Rear計画が壊れる
- Archerが弱くなる
- Buff前提が崩れる
- Friendly reinforcementの構成と噛み合わない

場合があります。

```text
Stormを唱えられる
≠
Stormを唱えるべき
```

です。

## Storm casterの保護

Storm等のBattlefield Spellを一人へ依存すると、

- Assassination
- Arrow
- Magic Duel
- Fatigue
- Script failure

で作戦全体が壊れます。

Casterを分散し、第二Scriptを用意します。

---

# Air Magicの役割

## Lightning

Shock damageとFatigueを与え、高Protectionへも有効な場合があります。

敵Shock Resistanceを確認します。

## Windと射撃

Air Magicは、

- 自軍射撃強化
- 敵射撃対策
- Precision
- Projectile defence
- Storm

へ関わります。

LA Manのような射撃国家に対し、Air Magicは兵を直接倒すだけでなく射撃Engineを止めます。

## Defence・Mobility

Air Spellは、

- Defence
- Quickness系
- Flying
- Movement
- Battlefield positioning

へも関わります。

## Battlefield enchantment

Storm、Wrathful Skies等のBattlefield-wide effectは、味方にも影響し得ます。

Resistance、Gem、Caster fatigue、Battle lengthを確認します。

---

# Cold・Ice装備とCaelum

Caelum系国家では、Ice weapon・Ice armor・Cold適性がArmy性能へ関わります。

見るものは、

```text
現在Temperature
Ice armorの現在Protection
自軍Cold Resistance
敵Cold Resistance
Winter移動
Stormとの併用
```

です。

Cold Scaleを取っただけで勝つのではなく、

```text
自軍の環境適性
－
敵軍の環境適性
```

を利用します。

---

# MammothとFlying兵

MammothはTrample・高HPを持つ一方、

- Morale
- MR
- Control
- Size
- Friendly Trample
- Retreat

へ弱点があります。

Flying兵と同じArmyへ入れても、移動・接敵Timingは同じにならない場合があります。

MammothをFlying Armyへ混ぜる場合は、Map ArrowとArmy Setupを必ず確認します。

---

# 飛行Raid

## 最小部隊

```text
Flying Commander
＋ PDを抜ける兵
＋ 必要ならPriest / Mage
＋ Retreat先
```

です。

## Target

- Tax route
- Lab・Temple
- Blood Hunt拠点
- Fort建設中
- Throne隣接
- 山越えの後方Province
- Retreat route

を狙います。

## 迎撃されたら

Flying Raiderは高価なことがあります。

Raid一回のIncomeより、

- 失った兵
- 失ったCommander
- 次のRaid能力
- 敵Reserveを動かした価値

で評価します。

---

# Anti-Flying

敵Flyingへは、次を組み合わせます。

## Rear guard

Mage・Archerの後ろへ、近接SquadやBodyguardを置きます。

## Hold timing

Flying Unitが到着するRoundへ合わせます。

## Storm

飛行を止められる場合があります。

## Archer・AoE

軽装Flying兵へ有効です。

## Entangle・Web・Fatigue

高Defenceを無視して行動を止めます。

## Fear・Morale

少数精鋭Flying RaiderをRoutさせます。

## Important province defence

全Provinceではなく、Mage Fort、Throne、Lab、Tax routeを重点防衛します。

---

# Friendly reinforcementと迎撃

自領Provinceへ複数Armyを集めるMovementは、敵侵攻より先に処理される場合があります。

```text
北の友軍 → 中央自領
南の友軍 → 中央自領
敵飛行Army → 中央自領
```

なら、防衛Armyが先に合流して迎える構造を作れます。

詳細は[ターン処理順](../reference/turn-resolution.md)を参照してください。

---

# Magic Phase移動とFlying

Teleport、Cloud Trapeze等のMagic Phase移動は、Strategic Flyingと別Timingです。

```text
Magic Phase Battle
→ 通常Movement
→ 通常Battle
```

となる場合があります。

同じProvinceへ向かっても、同じBattleへ参加する保証はありません。

Flying ArmyとMagic Phase strikeを組み合わせる場合は、

```text
先発部隊の目的：
単独で勝てるか：
本隊が到着するTiming：
退却先：
```

を決めます。

---

# Siege・Storm・Fort

Flying ArmyはField Battleで機動的でも、Fort wallを即座に無視できません。

```text
Province外側を取る
→ Siege
→ Wallを0
→ Storm
```

が必要です。

飛行兵のStrength、兵数、Supply、Relief Armyを確認します。

StormというSpellと、Fortを攻める`Storm` Orderは別です。

---

# Battle Replayで見るもの

```text
飛行開始Round：
Target：
Attack Rearが実際に向かった場所：
Storm発動Round：
飛べなくなったUnit：
射撃命中率：
Shock Resistance：
Fatigue：
Rout：
Retreat先：
```

「飛行部隊が消えた」場合、Damageだけでなく孤立とRoutを確認します。

---

# よくある失敗

## 1. Flying表示だけでArmy全体が飛ぶと思う

非Flying兵・Mountを確認します。

## 2. Attack RearをMage指定だと思う

Targetは戦場状況で変わります。

## 3. Stormを常に自軍有利と思う

自軍飛行・射撃も止まる場合があります。

## 4. 軽装兵を正面から撃たせ続ける

射撃対策、Timing、配置が必要です。

## 5. 飛行Raidで高価な兵を交換する

敵Reserveを動かした価値と損失を比べます。

## 6. Retreat routeを考えない

飛行できても退却先がなければ全滅します。

## 7. FlyingとMagic Phaseを同じTimingと思う

別Battleになる場合があります。

---

# Test checklist

```text
[ ] Army全体が実際に飛べるかMap Arrowで確認した
[ ] Attack Rearの到達RoundをReplayで確認した
[ ] Stormあり・なしの両ScriptをTestした
[ ] Shock Resistanceを敵別に確認した
[ ] Archer・AoEへの回答がある
[ ] RaiderのRetreat先がある
[ ] Fort攻略用のSiegeとSupplyがある
[ ] Magic Phase部隊が単独でも役割を果たせる
[ ] TemperatureとIce armorを現在画面で確認した
[ ] Mage FortへFriendly reinforcementを集められる
```

---

# 関連ページ

- [MA Caelum — Reign of the Seraphim](../nations/ma/caelum.md)
- [Magic Path: Air](../magic/paths/air.md)
- [戦闘ルール](../basics/combat-rules.md)
- [命令とBattle Script](../basics/orders.md)
- [ターン処理順](../reference/turn-resolution.md)
- [最初の戦争・外交・Raid・迎撃Q&A](../getting-started/war-faq.md)
