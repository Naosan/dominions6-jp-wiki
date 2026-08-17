---
title: EA Niefelheim
page_type: nation-guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
nation_id: 33
era: "EA"
epithet: "Sons of Winter"
---

# EA Niefelheim — Sons of Winter

EA Niefelheimは、**少数の巨人をただ正面へ並べる国家ではありません。**

国家の中心は、

> **高HP・高StrengthのJotun**
> ＋ **Cold環境で性能を伸ばすNiefel Giant**
> ＋ **SkrattiとGygjaによるWater・Death・Glamour・Blood**
> ＋ **巨人の損耗を補う召喚・Blood・小型部隊**

を一つの戦争機械へ組み合わせることです。

巨人は一体あたりの戦闘力が高く、Independent Provinceや通常兵の前線を力で押し切れます。しかし、

- 一体が高価で、損失の補充に時間がかかる
- Sizeが大きく、一Squareに入る人数が少ない
- 多数の攻撃を受けるとHarassmentとFatigueで崩れる
- Shock、AN、MR attack、即死・Controlへ弱点を持つ
- Siege、Scout、PD処理、補給を巨人だけで賄うと非効率

という制約があります。

> **Niefelheimの上達は、「強い巨人を作ること」ではなく、「巨人が戦うべきBattleだけを選び、巨人以外へ安い仕事を移すこと」です。**

- [自動生成Recruitデータ](../../data/recruitment/ea/niefelheim.md)
- [国家別Site Search能力](../../data/site-search/ea/niefelheim.md)
- [Extended Magic Access](../../data/extended-magic-access/ea/niefelheim.md)
- [Magic Access Route](../../data/magic-access-routes/ea/niefelheim.md)
- [Pretender設計サンプル](../../pretender/samples.md)

!!! note "このページの精度範囲"
    本文はDominions 6.35の固定データ、ゲーム内Nation・Unit・Spell・Item表示、公式Documentation、現行Inspector、現行Community資料を照合し、実戦判断へ再構成しています。Cold Recruit、国家Site、Recruit limit、形態変化、Blood、Hero、Pretender、Map、Patch、MODには例外があります。正確なUnit Cost・Path・Recruit条件はゲーム内表示と上記自動生成データを優先してください。

!!! warning "自動生成Recruit欄と国家固有条件"
    国家Site、Cold Recruit、Holy Point、首都条件等を持つUnitは、自動生成索引の分類と実際のRecruit画面が一致しない場合があります。Niefel Giant、Niefel Jarl等の供給計画は、現在のゲーム内Recruit画面を正本にしてください。

---

# 一言でいうと

```text
巨人で序盤の土地を取る
→ 高価な損失を避ける
→ Skratti・Gygjaを増やす
→ Cold・Water・Death・Bloodで戦場条件を変える
→ 召喚・小型兵・Raidへ安い仕事を移す
→ 巨人は決戦とFort攻略へ集中する
```

国家です。

Niefelheimを「HPが多いから初心者向け」と考えると危険です。

HPが高いことは、

- 通常Damageへ数回耐える
- Regenerationや回復の価値が高い
- 一撃でRoutしにくい

という長所ですが、

- ShockやANでProtectionを無視される
- Fatigue 100以降に防御が崩れる
- MR attackでHPを使わず倒される
- 高価な一体を失う経済損失が大きい

ことは防ぎません。

---

# 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | Early Age |
| Nation ID | 33 |
| Epithet | Sons of Winter |
| Preferred Temperature | 強いCold寄り |
| 軍事の中心 | Size 6前後のJotun、より大型のNiefel Giant、巨人Commander |
| 確実なMagicの軸 | Water、Death、Glamour、Blood、Holy |
| 主要Mage | Jotun Skratti、Gygja、国家SiteのNiefel Jarl |
| 戦略上の特徴 | Cold環境、巨人、Sacred、Blood access、Shapeshift、国家召喚 |
| 操作量 | 中～高。巨人損耗、形態、Gem、Blood、Random Pathを管理 |
| 主な弱点 | Shock、AN、MR attack、Fatigue、包囲要員不足、経済損失 |

## Recruitデータで最初に見る値

自動生成データでは、通常Jotun兵は概ね、

- Size 6
- HP 31～38前後
- Strength 19～22前後
- MR 12前後

を持ちます。

Niefel Giantはさらに大きく、HP・Strength・MRが上がります。一方、Sizeが大きいほど、同じ前線幅へ入れる人数は減ります。

```text
一体が強い
≠
同じ幅での総攻撃回数が常に多い
```

ことを忘れないでください。

---

# 国家エンジン

Niefelheimの国力は、次の循環から生まれます。

```text
巨人兵でIndependentを低損失攻略
        ↓
IncomeとCold適地を増やす
        ↓
FortとMage生産を増やす
        ↓
Skratti・Gygja・Priestを役割別に配備
        ↓
Cold・Buff・Summon・Bloodで巨人の交換効率を改善
        ↓
Field Battleに勝つ
        ↓
巨人のStrengthとSiege要員でFortを破る
        ↓
新しい生産拠点とGemを得る
```

この循環が止まりやすい場所は三つです。

1. Expansionで巨人を少数ずつ失い、二軍が作れない
2. 巨人RecruitへGoldを使いすぎ、MageとFortが増えない
3. 巨人Armyへすべてを集中し、Raid・Scout・Siege補助が足りない

Niefelheimは、兵質で得た余裕を経済へ変換できれば伸びます。兵質が高いからといって、毎TurnすべてのGoldを巨人へ変える必要はありません。

---

# 強み

## 1. 通常兵を力で押し切る基礎Stats

Jotunは高HP、高Strength、高Damageを持ち、一般的な人間兵に対して一体ずつの交換で優位を取りやすいです。

- 低Damage武器をHPで受ける
- 高StrengthでProtectionを抜く
- 大型Unitの一撃で小型兵を減らす
- Moraleが比較的安定する

という基本性能があります。

## 2. Coldを戦場資源へ変えられる

Niefel系UnitはCold環境と相性がよく、敵だけがCold・Fatigue・移動へ苦しむ状況を作れます。

重要なのは、Coldを単なる国家Flavorではなく、

```text
自軍の適性
－
敵軍の適性
```

という差として使うことです。

敵もCold ResistanceやCold Powerを持つなら、Coldだけで勝利条件にはなりません。

## 3. Water・Death・Bloodを同じ国家で扱える

SkrattiとGygjaにより、

- Water：自己強化、Cold、Elemental、移動・補助
- Death：Undead、疲労・生命・恐怖・召喚
- Glamour：幻惑、Luck、Stealth、認識操作
- Blood：Blood Hunt、Battle buff、Demon・特殊召喚

へ入れます。

ただしRandom Pathの出方は毎Game異なります。保証Pathを基準計画にし、Randomは上限を広げるLayerとして扱います。

## 4. Mage自身が戦闘Unitになり得る

SkrattiはMagicだけでなく、形態、Sacred、巨人Statsを活かし、装備・Self Buff後にThug、Raider、Battle Mageとして使えます。

しかし、

> Mageとして高価値
> ＋ 戦闘Unitとして高価値

だからこそ、死亡時の損失も二重です。

## 5. Giant StrengthはSiegeへ変換しやすい

巨人は壁を破る役割へ向きます。Field Battleに勝った後、兵数が少なくてもStrengthの高いUnitがSiegeへ大きく寄与します。

ただしSiege中のSupply、Relief Army、Storm用編成は別に準備します。

---

# 弱み

## 1. 一体の損失が重い

Jotun一体の死亡は、通常兵一体の死亡より、

- Gold
- Resource
- Recruit turn
- 前線幅
- Siege strength
- 経験

を多く失います。

Battleに勝っても毎回数体ずつ失うなら、国家経済では負けている場合があります。

## 2. 大型Unitは攻撃回数を受けやすい

Sizeが大きいUnitは、同じSquare内で占める容量が大きく、少数で戦線を作ります。

敵の小型兵が多数なら、

- 周囲から多く殴られる
- HarassmentでDefenceが下がる
- 敵Chaffを倒し切る前にFatigueが増える

ことがあります。

## 3. Shockが重大なCounterになりやすい

Niefel・Jotun系はColdへ強くても、Shockへ弱い個体を多く含みます。

Shockは、

- Armorの価値を下げる
- Fatigueを増やす
- 高HP巨人を行動不能へ近づける

ため、単なるElemental Damage以上に危険です。

敵Air Mageを見たら、Research、Gem、Resistance、射程、Stormを確認します。

## 4. MR attackとControl

巨人のHP・Protectionを無視する、

- Soul系
- Charm・Control
- Paralysis
- MR Negates
- 即死

は、少数高価値Armyへ効率的です。

MRを一括した数字として見るだけでなく、Antimagic、Spell target、Mindless Summon、Mage狙いを組み合わせます。

## 5. GoldとCommander Pointが詰まりやすい

巨人兵も巨人Mageも高価です。

```text
兵を増やす
→ Mageが止まる

Mageを増やす
→ Expansion・防衛兵が足りない

高価なMageを前線へ出す
→ Researchが止まる
```

という競合が起きます。

---

# 兵士

## Jotun Bondi

安価な巨人枠として、

- 低脅威Province
- Siege補助
- 兵数の穴埋め
- 高価なHirdmanを使うほどでない戦線

へ使えます。

しかしArmorと技能はEliteではありません。高Damage・射撃・MR攻撃へ無理に出さないでください。

## Jotun Warrior：Spear＋Shield

長めの武器とShieldを持つ、標準的なLine holderです。

- 最初の接敵
- 小型兵のCharge受け
- Shieldによる射撃軽減
- 後ろのDamage役へ時間を作る

用途があります。

## Jotun Warrior：Axe＋Javelin＋Shield

接敵前にJavelinを投げ、近接ではAxeを使います。

Javelin二発は決戦火力ではありませんが、

- 軽装兵
- Elephant・Large target
- 盾のない敵

へ接敵前Damageを作れます。

## Jotun Hurler

Boulder投擲とSiege Bonusを持つ補助兵です。

- Siege
- 大型・低Defence target
- 接敵前の高Damage

へ価値があります。

命中率、弾数、敵Shieldを確認し、主力射撃として過大評価しないでください。

## Jotun Huskarl・Godihuskarl

中間～上位のShield兵です。

Huskarlは通常Jotunより前線維持力を持ち、GodihuskarlはSacred ArmyやPriestと合わせやすい役割があります。

## Jotun Hirdman

通常Jotunの中で高い技能と装備を持つElite前衛です。

強い一方、損耗を許容できる価格かを確認します。Independent相手に毎回Hirdmanを失うなら、編成かTarget選択を直します。

## Niefel Giant

Niefelheimを象徴する大型Sacredです。

- 高HP
- 高Strength
- Cold適性
- Chill・Ice系の国家能力
- Bless適用

によって、通常兵へ大きな圧力をかけます。

一方、

- Recruit limit・Holy Point・首都・Cold等の供給制約
- Anti-Sacred
- Shock
- Fatigue
- 高価なAttrition

を受けます。

Heavy Blessを取る場合は、毎Turn何体増えるかを先に数えてください。

---

# Commander・Mage

## Jotun Scout

巨人国家でもScoutは必要です。

Main Armyが高価なほど、誤情報へ突入した損害が大きくなります。

- 敵Mage
- Shock source
- MR attack
- Fort・Throne
- Retreat route

をMain Armyより先に確認します。

## Jotun Herse・Jarl

通常Leadershipを持つArmy Commanderです。

JarlはPriestも兼ね、Sacred部隊のBless、Morale、Throne関連へ役割を持ちます。

## Jotun Gode

上位Holyを持つPriestとして、

- Bless
- Preach
- Anti-Undead
- Throne Claim準備
- Sacred ArmyのMorale支援

を担います。

## Jotun Skratti

国家の中心Mageです。

保証PathはWater・Blood・Holyで、RandomによりWater・Death・Glamour・Bloodへ伸びます。

主な役割：

- Water Battle Mage
- Blood Hunter / Blood ritual
- Booster・Item
- Site Search
- Shapeを使うThug・Raider
- Sacred support

### Skrattiを分類する

Recruit後に、少なくとも次へ分けます。

```text
W高Path：Water spell・Elemental・Cold
D個体：Undead・Death spell・召喚
G個体：Glamour utility・Stealth・Luck
B高Path：Blood Hunt・Battle buff・召喚
戦闘用：Thug装備とSelf Buff
研究用：前線へ出さない
```

Rare個体を一括して同じScriptへ入れないでください。

## Gygja

Death・Glamour・Bloodを基礎に、Astral・Death・Nature・Glamour・BloodへRandomが広がるMageです。

国家のMagic diversityを大きく広げますが、個体差が大きいので、

- Booster route
- Remote Search
- Summon Mage
- Communion可能性
- Global候補

をRecruit後に分類します。

## Niefel Jarl

国家Siteから得る高位Water・Death・Holyの重要Mage / Commanderです。

量産Mageと同じ扱いをせず、

- 高位Spell
- Global・Ritual
- Army leadership
- Sacred commander
- 戦闘装備

のどこへ使うかを事前に決めます。

---

# Magic Access

## 保証Access

通常Recruitから計画しやすい軸は、

```text
Water 2
Death 1
Glamour 1
Blood 2
Holy 2
```

です。

国家Site MageによりWater・Death・Holyはさらに上がります。

## Random Access

GygjaとSkrattiのRandomにより、

- Astral
- Nature
- 高位Death
- 高位Glamour
- 高位Blood

へ伸びます。

Random込み理論最大を国家保証Accessとして書かないでください。

## Booster

保証経路ではWaterが最も伸ばしやすいPathです。

Water Bracelet、Robe、上位Boosterへ進む場合でも、

- Construction
- Gem income
- Forge担当
- 装備Slot
- そのCasterがBattleへ行くか

を確認します。

## 国家にないPath

Fire、Air、Earthは通常Recruitの保証Accessにありません。

特にShock対策のためAirが欲しいからといって、Air Pretenderを選べば自動的に問題が解決するわけではありません。

```text
必要なResistance Spell / Item
→ 必要Path
→ 必要Research
→ 必要Gem
→ 何Turnに間に合うか
```

まで書きます。

---

# Pretender方針

Niefelheimでは、Pretenderの選択が、

- Niefel GiantのBless
- Shock対策
- Magic diversity
- Expansion速度
- Scalesと巨人供給

へ直接つながります。

## 1. Medium / Heavy Bless

Niefel GiantやSacred Skrattiを主力にする設計です。

### 解決するもの

- 命中
- Damage
- Defence
- Reinvigoration
- MR
- Shock Resistance
- Regeneration

などです。

### 注意

Heavy Blessの対象が、供給制約のあるNiefel Giantだけなら、国家全体へ働く割合は低くなります。

Sacred Commander・Mage・召喚にもBlessが働くかを確認します。

## 2. Imprisoned Scales

通常JotunとMageを多数生産し、長期経済へ寄せます。

向く条件：

- 通常JotunだけでExpansionできる
- Niefel Giantを補助戦力として扱う
- 第二FortとMage量産を急ぐ
- PretenderなしでFirst warを戦える

Productivity、Order、Growth、Magic、Dominionのどこが国家のBottleneckかをTestします。

## 3. Diversity / Resistance Pretender

Fire・Air・Earth・Nature等の不足を補い、

- Resistance
- Booster
- Crosspath Item
- Summon Mage
- Global

へ入ります。

単にPathを広く取るのではなく、最初に作るItem・最初に使うSpellを書きます。

## 4. Awake Expander

国家兵も強いため、Awake Expanderが必須とは限りません。

採用するなら、

- Niefel Giant供給とは別方向へExpansionする
- Capital周辺の危険Provinceを処理する
- 早期に第二Fort候補を確保する

役割を持たせます。

AwakeにしたのにCapitalでResearchだけする設計は、Point交換を再検討します。

---

# Scales

## Productivity

巨人装備のResource負担を支えます。

ただしResourceが余ってGold不足なら、さらにProductivityを上げても兵数は増えません。

## Order

高価な兵とMage、Fortを支える安定Incomeに価値があります。

## Growth

長期Income、Supply、Blood Hunt基盤、老齢Mageの国家運用へ寄与します。

## Cold

国家の得意環境です。

ColdをPoint源としてだけでなく、戦場・移動・敵への圧力と結びつけます。

## Magic

高価なMage数が少ない段階では、Research Scaleの価値が大きくなります。

一方、BlessへPointを集中する場合はMagicを削ることもあります。第一Research Breakpointへの到達Turnで比較します。

---

# 序盤拡張

## 標準方針

Expansion Armyは、

```text
Shieldを持つJotun前衛
＋ 高Damage Jotun
＋ Commander
＋ 必要ならPriest / Bless
```

を基本にします。

兵数が少ないため、一SquadがRoutするとArmy全体への影響が大きくなります。Squad数、Morale、Commander位置を確認します。

## 攻めやすい相手

一般に、

- 低Damage軽歩兵
- Shieldのない通常兵
- 少数の人間重歩兵
- 低Morale部隊

は巨人Statsで押しやすいです。

## 危険な相手

### 大量Archer・Crossbow

巨人はTargetとして大きく、盾のない個体は集中射撃を受けます。

### Cavalry・Lance

高Damage Chargeで高価な一体を失うRiskがあります。

### Barbarian・高Damage両手武器

HPが高くても、大Damageを連続で受ければ崩れます。

### Elephant・Trample

Size差とMorale、周囲の兵数を確認します。

### Poison

高HPはPoison蓄積の影響を長く受けます。戦闘後の傷とDiseaseも確認します。

### Undead・特殊兵

通常武器、Fear、Mindless、Darkness、Magic Weapon条件を確認します。

## Expansionで見る指標

```text
Province数
＋ 第二Army完成Turn
＋ 巨人損失数
＋ Commander損失
＋ Affliction
＋ 次の補充Turn
```

単に勝敗だけで評価しません。

---

# Economy・Fort計画

## 第一のBottleneckを特定する

毎Turn、Recruit画面で、

- Gold
- Resources
- Recruitment Points
- Commander Points
- Holy Points / Recruit limit

のどこが止めているかを見ます。

## 第二Fort

第二Fortの価値は、

- 巨人兵の追加生産
- Skratti・Gygjaの追加生産
- 前線Supply
- Retreat route
- Siege・Gem補給拠点

です。

Resourceだけでなく、毎TurnどのMageを雇うかで場所を決めます。

## Fort密度

巨人国家は一FortあたりのGold消費が大きいため、Fortだけ増やしてもRecruitできない場合があります。

```text
Fort数
× 毎Turn雇うMage・兵のCost
```

をIncomeと比較します。

## Blood Hunting Province

Bloodへ移行する場合、Mage FortとBlood Hunt Provinceを分けると管理しやすくなります。

- Population
- Unrest
- Patrol
- Slave輸送
- Enemy Raid

を一つの収支として見ます。

---

# Research

NiefelheimのResearchは、単一Schoolを盲目的に上げるより、

```text
巨人の交換効率を上げる
＋
巨人だけでは解決できないTargetを作る
```

ことが目的です。

## 第一Breakpoint：生存と接敵

候補：

- Water系Self Buff
- Defence・Protection補助
- Cold利用
- GlamourのLuck・幻惑
- Deathの召喚・Chaff

敵が接敵する前にBuffが終わる配置とScriptを作ります。

## 第二Breakpoint：高Protection・大軍対策

候補：

- Cold / Water Damage
- Deathの疲労・生命攻撃
- Elemental summon
- BloodのBattle support
- MR attack

通常巨人の高Damageだけで抜けない防御へ第二のDamage typeを用意します。

## Construction

Skratti・Niefel Jarl・Gygjaへ、

- Resistance
- Reinvigoration
- Protection
- Regeneration
- Magic Weapon
- Booster

を与えます。

Thug装備を作る前に、敵のCounterとCarrierの役割を一文にします。

## Conjuration・Enchantment

Summon、Undead、Elemental、Cold battlefield、Army supportへつながります。

Goldで補充しにくい仕事をGemへ移すために使います。

## Blood

Blood economyを始めるTimingを決めます。

```text
Blood Hunter数
→ Slave収入
→ Patrol cost
→ Population損失
→ 何を召喚・Castするか
```

を先に書きます。

---

# Army構成

## 1. Jotun Line

Shield Jotunで最初の攻撃と射撃を受けます。

## 2. Damage Jotun / Niefel Giant

少し後ろへ置き、敵がScreenへ固定された後に接敵させます。

## 3. Mage Core

Skratti・Gygjaを、

- Resistance
- Buff
- Summon
- Damage
- Control

へ分けます。

全員に同じ五枠Scriptを貼らないでください。

## 4. Cheap Work Unit

Independent、Summon、Undead等へ、

- Chaff
- Siege
- Patrol
- Bodyguard
- PD処理

を担当させます。

## 5. Raider / Thug

Skrattiや特殊Commanderを小規模部隊として使う場合、Main ArmyのMagicを減らす交換条件を確認します。

---

# Script例の考え方

固定Spell名より目的で記録します。

```text
Skratti A：自己Path補助 → Resistance → Army Buff → Cast Spells
Skratti B：Summon → Summon → Damage / Control
Gygja A：Luck / Defence → Control → Cast Spells
Priest：Bless → Sermon / Holy support
```

## Scriptが壊れる条件

- Gem不足
- Random Path個体を取り違えた
- Shapeが違う
- EnemyがResistanceを持つ
- Buff前に接敵
- Mageが射撃・Flankを受ける
- Cold環境が想定と違う

Replayで最初に崩れた条件を確認します。

---

# Siege・Storm

## Siege

巨人Strengthは壁破壊へ有効です。

ただし、Main Army全体をSiegeへ固定すると、Raidへ対応できません。

- Siege担当
- 周辺Provinceを取るRaider
- Relief迎撃Army
- Gem補給

へ分けます。

## Storm

Storm戦では前線幅が狭く、大型Unitが詰まりやすくなります。

- Gateへ入る順番
- Chaff
- AoE
- Fear
- Fatigue
- Wall defender射撃

を通常Field Battleと別にScriptします。

## Defence

巨人少数をFort内へ入れるだけでは、長期SupplyとStormの両方を解決できません。

Need Not Eat Summon、Supply Item、Relief Armyを準備します。

---

# Counterと対応

## Shock

### なぜ危険か

- Armorを頼りにくい
- Fatigueを増やす
- 大型高価値Unitへ効率がよい

### 対応

- Shock Resistance
- Mage分散
- Air MageへのRaid・Assassination
- Storm / Range対策
- Chaffで初弾を受ける

## AP・AN・高Damage

Protectionだけで耐えず、Defence、Luck、HP、Regeneration、射撃妨害を重ねます。

## MR attack

Antimagic、MR装備、Mindless Summon、Caster killを使います。

## Fatigue

Reinvigoration、戦闘時間短縮、Chaff排除、Cold環境差を使います。

## Poison

Poison Resistance、戦闘時間短縮、Healer、再生、敵Caster狙いを用意します。

##大量Chaff

多段攻撃、AoE、Summon、Fear、Battlefield effectで処理し、巨人が一体ずつ殴り続ける状態を避けます。

## Anti-Sacred

Niefel GiantだけでArmyを組まず、通常Jotun、Summon、Mage Damageを混ぜます。

---

# Multiplayer

## 相手に見える脅威

Niefelheimは、

- 巨人Rush
- Heavy Bless
- Skratti Thug
- Blood scaling
- Cold battlefield

を警戒されます。

Pretender、Bless、Mage random、Blood移行をすべて早期に見せる必要はありません。

## 外交

高価なArmyが二正面へ分かれると弱くなります。

- Borderを短くする
- Cold適地・Throne・Fort候補を明確にする
- 第三国がShock・MR Counterを用意するTimingを見る

ことが重要です。

## 戦争目的

良い目標：

```text
Border Fortを取り、巨人補充とMage生産の前線拠点にする
```

悪い目標：

```text
敵Provinceを広く塗る
```

高価なArmyを長距離Raidへ使わず、Fort・Throne・Mage拠点を取ります。

---

# よくある失敗

## HPが高いのでScoutなしで攻める

Shock、MR attack、AN、Poisonで主力を失います。

## Giantだけで全役割を担当

Scout、Chaff、Patrol、Siege補助、Raidが高コストになります。

## Niefel GiantへHeavy Blessを取ったが供給数を数えていない

Design Pointが少数Unitへしか働きません。

## Skrattiを全員Thugにする

Research、Blood、Site Search、Battle supportが止まります。

## Random Mageを保証Accessとして扱う

必要個体が出ず、Research計画が成立しません。

## Shock対策が遅い

敵Air研究が完成した一戦でArmy全体を失います。

## 巨人の勝利後に追撃し続ける

Gem、Supply、補充、Afflictionを確認せずRelief Armyへ負けます。

## Bloodを始めたが用途がない

UnrestとPopulationだけを失います。

---

# Turnごとの確認

```text
1. 前Turnの巨人損失とAffliction
2. Niefel Giant・MageのRecruit bottleneck
3. Shock・MR Counterの偵察
4. Skratti・GygjaのPath分類
5. GemとBlood Slave
6. SupplyとRetreat
7. 第二Fort・前線Fort
8. Siege担当とMain Army
9. Pretender / Incarnate Bless状態
10. End Turn前のScoutとRaid
```

---

# Test Game Checklist

## Expansion

- Turn 4～12のProvince数
- Jotun損失数
- Niefel Giant供給
- 第二Army完成Turn
- Cavalry・Archer・Barbarian・Poisonへの結果

## Economy

- 毎TurnのJotun数
- 毎TurnのMage数
- 第二Fort開始・完成Turn
- GoldとResourceの余り方

## Research

- 第一Buff到達Turn
- Shock Resistance到達Turn
- Summon・Construction到達Turn
- Blood開始Turn

## First War

- ScreenとDamage役の接敵順
- Coldが敵へ効いたか
- MageがGemを使いすぎていないか
- Shock・MR attackへ回答があるか
- SiegeとSupplyが続くか

---

## 関連ページ

- [国家選択ガイド](../choose-a-nation.md)
- [Pretender設計サンプル](../../pretender/samples.md)
- [Bless](../../pretender/bless.md)
- [戦闘ルール](../../basics/combat-rules.md)
- [命令とBattle Script](../../basics/orders.md)
- [Researchと研究ルート](../../magic/research.md)
- [Gem](../../magic/gems.md)
- [Magic Access到達経路](../../magic/magic-access-routes.md)
- [Fort・Siege・Storm](../../systems/forts.md)
- [初心者Q&A：内政・補給・自動化](../../getting-started/logistics-faq.md)
- [初心者Q&A：最初の戦争・外交・Raid・迎撃](../../getting-started/war-faq.md)

## 主な参照先

- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [Illwiki — EA Niefelheim](https://illwiki.com/dom5/ea_niefelheim)（現行挙動の照合用。数値はゲーム内表示と6.35固定データを優先）
