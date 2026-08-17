---
title: Undead・Reanimation・Popkill
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
---

# Undead・Reanimation・Popkill

Undead国家を理解するときは、次の三つを分けます。

```text
Undead
＝ Unit分類と戦闘上の性質

Reanimation / Freespawn
＝ Unitを得る生産方法

Popkill
＝ Dominion等がPopulationと通常経済を破壊する国家構造
```

三つは関連しますが、同じ意味ではありません。

- Undead Unitを普通にRecruitする国家
- PriestがLongdeadをReanimateする国家
- Dominionが自動でUndeadを発生させる国家
- Populationを殺すがLiving Unitも使う国家

では、経済・Army・研究・外交が異なります。

このページは、特に[MA Ermor — Ashen Empire](../nations/ma/ermor.md)のようなPopkill国家を中心に、Undeadの共通運用を整理します。

!!! warning "Unitごとの差を優先"
    `Undead`であっても、Mindless、Inanimate、Ethereal、Spirit Sight、Magic Resistance、Never Heals、Amphibious等はUnitごとに異なります。分類名だけから全耐性を推測せず、ゲーム内Unit popupと[Unitデータ](../data/units/index.md)を確認してください。

---

## 最初に覚える十項目

| 項目 | 最初の理解 |
|---|---|
| Population | Popkill Dominion下では減少し、通常Income・Recruit基盤が失われる |
| Gold | Populationが死ぬほど通常税収は弱くなる |
| Supply | 多くのUndeadは食料不要だが、同行するLiving Unitは別 |
| Recruitment | Popkill国家は通常RecruitよりFreespawn・Reanimation・Ritualへ依存しやすい |
| Leadership | Undead LeadershipがないCommanderへ大量のUndeadを預けられない |
| Morale | Mindlessと非Mindless UndeadではRout・命令挙動が異なる |
| Priest | Reanimation、Unholy支援、Banishmentへの対抗、Dominion管理の中心 |
| Corpse | Soulless等、一部Reanimationは未埋葬Corpseを消費する |
| Counter | Banishment、Holy、Anti-undead、Control、Fire、MR攻撃等 |
| Economy | Gold国家ではなく、Temple・Lab・Fort・Gem・Commander turnの国家へ変わる |

---

# Undead分類を読む

## Undead

Undeadは死者として扱われ、Holy・Anti-undead効果の対象になります。

よく見られる性質は、

- Need Not Eat
- Poison Resistance
- Cold Resistance
- Spirit Sight
- Diseaseへの異なる反応
- Undead Leadershipの要求

です。

ただし、すべてのUndeadが同じではありません。

```text
Longdead
→ Mindless・Inanimate寄りの消耗兵

Wight / Lictor
→ 非Mindlessで比較的高性能なElite

Ghost / Spectral Mage
→ Ethereal・高Defence・Magic Weapon等を持つ場合がある

Ghoul
→ Livingから変化したUndeadで、別の弱点と役割を持つ
```

## Mindless

Mindless Unitは通常のMorale運用と異なり、命令・Leadership・Routの扱いに特殊性があります。

攻略上は、

- Fearへ強い場合がある
- Commanderを失うと制御不能・消滅等のRiskがある
- 複雑な命令を期待できない
- Charm・Mind effectへ異なる耐性を持つ場合がある

という意味を持ちます。

## Inanimate / Lifeless

Inanimateは生命体ではないため、Poison、Disease、Life Drain、疲労等との相互作用が通常のLiving Unitと異なることがあります。

ただし、

> Inanimateだから全Damageへ強い

ではありません。

高Damage、Armor Negating、Holy、Shatter系、Control等、別の防御層を狙われます。

## Never Heals

一部Undeadは通常回復せず、受けたDamageやAfflictionが長期的な消耗になります。

大量Freespawnを使う国家では一体ごとの回復より交換効率が重要ですが、

- Rare Mage
- 高位Priest
- Booster holder
- Unique Commander
- Sacred Elite

は別です。

---

# Popkillとは何か

Popkillは、国家Dominionや特殊効果がPopulationを継続的に減らす構造です。

概念的には、

```text
自国Dominionが広がる
        ↓
Populationが減る
        ↓
Income・Resources・Recruitment capacity・Supplyが弱くなる
        ↓
代わりにUndead Freespawnや国家効果を得る
```

という交換です。

Popkill国家は、通常国家のように、

> 取ったProvinceを長く育てて税収を増やす

ことが主目的ではありません。

Province価値を、

```text
PopulationとIncome
```

だけでなく、

```text
Temple
Lab
Fort
Magic Site
Gem income
Choke point
Retreat route
Throne
Plane入口
Freespawn production
```

で評価します。

## Populationが死ぬ前と後

新しく取ったProvinceは、Populationが残っている短期間だけ、

- Income
- Independent Recruit
- Supply
- PD上限
- Blood Hunt対象

として価値を持つことがあります。

しかし自国Dominionが広がると、その価値は失われます。

したがって、

```text
今すぐTempleを建てDominionを広げる
```

ことと、

```text
一時的にPopulation・Independent Recruit・Incomeを利用する
```

ことの間にTiming判断があります。

!!! warning "国家固有処理"
    Population減少速度、Freespawn量、Scale制限、Dominion効果は国家ごとに異なります。[Dominion](dominion.md)、国家記事、Game Infoを優先してください。

---

# Popkill経済

## Goldを何に使うか

通常国家では、Goldを主に兵士とMageへ使います。

Popkill国家では、Goldの主な用途が変わります。

```text
Temple
Lab
Fort
Independent Commander / Mage
Mercenary
Province Defence
建設・修理
外交上の取引
```

通常Recruitがほぼない国家では、Goldを残しすぎてもArmyへ変換できません。

一方、Incomeが将来減るため、早期のTemple・Lab・Fort投資を逃すと後から建てにくくなります。

## Gemが実質的な生産資源になる

Death Gem等は、

- Mage revival
- Commander召喚
- Undead召喚
- Booster
- Ritual
- Global
- Battle Gem

へ変換されます。

したがってSite Searchは、単なる収集ではなく、国家のMage・Commander・Army生産能力です。

```text
Site Search
→ Gem income
→ Mage / Commander
→ Research / Reanimation / Ritual
→ さらにSite Search
```

という循環を作ります。

## Fortの価値

Populationが少なくてもFortは、

- 防衛Turnを買う
- LabとTempleを守る
- Commanderの安全な集合点
- Retreat・Relief route
- Siegeを強制する

価値を持ちます。

ただし通常Recruitを増やせないなら、すべてのFortがMage工場になるわけではありません。

Fortは、

```text
重要Siteを守るFort
Borderを遅延するFort
Throneを守るFort
Ritual・Gem輸送拠点
```

として配置します。

---

# Freespawn

Freespawnは、Goldを直接払わず、Dominion・Scale・Temple・Commander能力等からUnitを得る仕組みです。

## 強み

- Gold不足でも数を増やせる
- Siege bodyを大量に用意できる
- PD処理・Raid・Screenを安く行える
- 損失を通常Recruit queueへ返さない

## 弱み

- 欲しいUnitを欲しいTurnに選べない場合がある
- CommanderとUndead Leadershipが不足する
- 低品質UnitがArmy speed・Formationを悪化させる
- 大量Unitの移動・編成・Siege管理が必要
- Holy AoEへ密集すると交換効率が逆転する

## Commander不足

Freespawn国家では、兵数よりCommanderが不足しやすくなります。

毎Turn確認するものは、

```text
新しく増えたUndead数
Undead Leadership総量
前線へ輸送するCommander
予備Commander
Retreat後に拾うCommander
```

です。

Armyを一つへまとめすぎると、Commander一人の死亡で巨大な部隊が機能停止します。

---

# Reanimation

ReanimationはPriest等のCommander turnを使い、Undeadを生産します。

## Longdead

Longdeadは一般的な骨兵です。

- 数を作りやすい
- Supplyを消費しない場合が多い
- Siege・Screen・消耗戦へ使える
- 装備差が大きい

一体の性能より、

```text
何TurnのPriest turnで
どの前線へ
何体を輸送できるか
```

を見ます。

## Soulless

Soullessは未埋葬Corpseを必要とする場合があります。

Battle後のCorpse、Disease・Event・Population等の状況により生産可能数が変わります。

```text
CorpseがあるProvince
→ Soulless生産

CorpseがないProvince
→ 別Reanimationへ切替
```

とします。

## Ghoul

Ghoul ReanimationはPopulationを消費する場合があります。

Popkill国家では、

- Populationがまだある時期に作る
- Incomeを先に使う
- Dominion spreadとの順序を考える

必要があります。

## Longdead Horseman

一部国家では高位PriestがLongdead HorsemanをReanimateできます。

騎兵型Undeadは、

- Map速度
- Flank
- Raid
- 後衛圧力

を補いますが、通常Longdeadと同じ感覚で大量生産できるとは限りません。

## Lictor等の高位Reanimation

MA ErmorではH4以上のPriestがLictorをReanimateできる国家Ruleがあります。

高位Priest turnは、

```text
高品質Sacred Undeadを作る
Dominionを管理する
ThroneをClaimする
Battleへ参加する
```

間で競合します。

Lictor一体の性能だけでなく、H4 CommanderのTurn価値を含めて判断します。

[Reanimation・Freespawnデータ](../data/units/reanimation.md)と[国家Freespawn・Reanimation能力](../data/units/nation-generation.md)も参照してください。

---

# Undead Leadership

Undead Armyは、Undead Leadershipを持つCommanderが必要です。

## 読む順番

```text
CommanderのUndead Leadership
→ Squad上限
→ Mindless / 非Mindless
→ Map Move
→ Battle時のCommander保護
```

## Commanderを分散する

一つのArmyを、

```text
Commander A：前衛Longdead
Commander B：後衛・予備
Commander C：Mage護衛
Commander D：退却先で再編
```

へ分けます。

Commander一人へ全兵を預けると、

- Assassination
- Flying rear attack
- Remote attack
- Arrow
- Rout

でArmy全体が崩れます。

## Living Commanderとの混成

Living Commanderが通常Leadershipだけを持つ場合、Undeadを十分に指揮できません。

逆にUndead CommanderはLiving兵のLeadershipが低い場合があります。

混成Armyでは、

```text
Living兵用Commander
Undead用Commander
Magic Being用Commander
```

を分けます。

---

# Undead Armyの役割分担

## Screen

Longdead・Soulless等が、敵の最初の攻撃を受けます。

目的はKillではなく、

- 敵を固定する
- MageへRoundを渡す
- Archerの射線を乱す
- Elite Undeadを守る

ことです。

## Damage dealer

Lictor、Wight、騎兵、Summon、Mage spellが敵を倒します。

大量Chaffだけでは、

- 高Protection
- Regeneration
- Fire Shield
- Trample
- AoE Holy

へ勝てません。

## Siege body

大量UndeadはFort Siegeへ強い一方、壁を破った後のStorm Armyは別に設計します。

```text
壁を削る大量Freespawn
≠
Fort内のElite・Mageを倒すStorm部隊
```

です。

## Raider

Supply不要・低Gold損失を活かし、薄いProvinceを取ります。

ただしCommanderが高価なら、兵が無料でもRaidは無料ではありません。

---

# PriestとUnholy支援

Undead国家のPriestは、宗教だけでなくArmy supportです。

代表的な役割は、

- Reanimation
- Unholy Protection
- Unholy Power
- Unholy Blessing
- Dominion管理
- Throne Claim
- Enemy Priestへの圧力

です。

高位Priestを一か所へ集めると強力ですが、

- Assassination
- Magic Phase attack
- Remote ritual
- Battlefield wipe

で国家生産力ごと失います。

高位Priestを、

```text
生産担当
Battle担当
Throne担当
予備
```

へ分けます。

---

# Undeadの代表的Counter

## Banishment・Holy AoE

大量の低HP Undeadへ特に有効です。

対策は、

- Priestを先に狙う
- Lineを広げる
- 高MR・高HP Eliteを混ぜる
- Flying・Cavalryで後衛へ圧力
- Remote・AssassinでPriest数を減らす

です。

## Anti-undead Spell・Weapon

Unit popupやWeapon propertyで、Undeadへ追加効果を持つ攻撃を確認します。

通常物理へ強いUnitでも、分類Counterへ弱い場合があります。

## Control Undead

敵がUndeadを奪う場合、単なる損失ではなく敵Armyの増加になります。

- MR
- Mindless / Commander構造
- TargetになるEliteの分散
- Antimagic

を確認します。

## Fire

Dry・Inanimate・低Fire ResistanceのUndeadへFireが効く場合があります。

ただしUndead分類だけからFire Vulnerabilityを決めず、UnitごとのResistanceを見ます。

## Magic WeaponとEthereal対策

Ghost・Spectral UnitがEtherealなら、通常Nonmagical兵だけでは処理が遅れます。

Magic Weapon、Spell、Holy、MR attack等を用意します。

## Trample・AoE

低品質Undeadを密集させるほど、TrampleやAoEの効率が上がります。

Formation、Size、前線幅を調整します。

---

# Popkill国家を攻める側

## Populationを守る戦争ではない

Popkill国家のProvinceを奪っても、Populationがすでに死んでいる場合、通常国家には低価値です。

攻撃目標は、

- Temple
- Lab
- Fort
- Magic Site
- Throne
- Commander production
- Gem route

です。

## Templeを壊す

DominionとFreespawnのNetworkを弱めます。

ただし、Templeを一つ壊しても既存Armyは消えません。

```text
前線Armyを止める
＋ 後方Temple・Labを壊す
```

を並行します。

## Mage・Priest生産を狙う

無料兵を倒し続けるだけでは、敵の生産Engineを止められません。

- Revival caster
- 高位Priest
- Death Mage
- Booster holder
- Gem輸送

を狙います。

## 戦争を長引かせすぎない

Popkill国家は時間とDominionから兵を得る場合があります。

一方で通常経済は弱いので、

- Temple・Labを連続破壊する
- Gem incomeを切る
- 複数方向からCommanderを狙う

と、再建を難しくできます。

---

# Battle Replayで見るもの

Undead Armyが負けたら、次を順に見ます。

```text
1. Commanderはいつ死んだか
2. Banishment・Holy Damageは何体へ当たったか
3. Mindless Unitは命令どおり進んだか
4. Damage役がScreenの後ろで詰まっていないか
5. Ethereal相手へMagic Weaponが足りたか
6. Control・MR attackでEliteを失っていないか
7. MageがGemを使い切ったか
8. Rout・崩壊はCommander死亡とどちらが先か
```

大量Armyでは総損失だけを見ず、

```text
失ったCommander turn
失ったPriest turn
失ったGem
失ったRare Unit
```

を重視します。

---

# MA Ermorを例にした運用

MA Ermorは、

- 通常Recruitがない
- DominionがPopulationを殺しUndeadを発生させる
- Priest Reanimationを持つ
- H3+でLongdead Horseman、H4+でLictorをReanimateできる
- National revival ritualでPriest・Spectator・Dusk Elder等を得る

という極端な国家です。

したがって国家計画は、

```text
PretenderでDeath accessを確保
→ National revivalでCaster・Priestを増やす
→ Temple・Labを広げる
→ FreespawnとReanimationをCommanderへ束ねる
→ Gem incomeをMage・Ritualへ戻す
```

という形になります。

詳しくは[MA Ermor国家攻略](../nations/ma/ermor.md)を参照してください。

---

# 毎Turn Checklist

```text
□ 新しいFreespawnをCommanderへ配属した
□ Undead Leadership上限を超えていない
□ 高位PriestをReanimation・Battle・Throneへ割り振った
□ Temple・Lab・Fort資金を確保した
□ Populationが残るProvinceの用途を決めた
□ Site SearchとGem輸送を確認した
□ 敵Priest・Holy Mage・Anti-undead兵をScoutした
□ Retreat先と予備Commanderを用意した
□ 壁削りArmyとStorm Armyを分けた
```

---

# よくある失敗

## 無料兵なので損失を気にしない

Commander、Priest turn、Gem、移動Turnは無料ではありません。

## 全Undeadを一Armyへ集める

AoE Holy、Leadership崩壊、Supplyを必要とする同行Living Unit、移動遅延が悪化します。

## Populationが死ぬ前のGoldを使わない

後からTemple・Lab・Fortを建てるIncomeが残りません。

## Freespawnだけで高Protectionを殴る

Damage sourceが不足し、敵Mageへ時間を与えます。

## 高位Priestを全員前線へ出す

国家のReanimation・Dominion・Throne能力を同時に失います。

## Banishment対策が「兵を増やす」だけ

敵Priest一人あたりの交換効率をさらに上げる場合があります。

## Popkill Provinceを通常国家の価値観で評価する

Incomeが低くてもTemple、Lab、Site、Choke、Throneには高い価値があります。

---

## 関連ページ

- [MA Ermor — Ashen Empire](../nations/ma/ermor.md)
- [Dominion](dominion.md)
- [Province](province.md)
- [Forts](forts.md)
- [Death](../magic/paths/death.md)
- [Holy](../magic/paths/holy.md)
- [特殊能力](../reference/special-abilities.md)
- [戦闘ルール](../basics/combat-rules.md)
- [命令とBattle Script](../basics/orders.md)
- [Reanimation・Freespawnデータ](../data/units/reanimation.md)
- [国家Freespawn・Reanimation能力](../data/units/nation-generation.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [MA Ermor community reference](https://illwiki.com/dom5/dom6/ermor-ma)
