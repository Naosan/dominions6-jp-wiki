---
title: EA Ulm
page_type: nation-guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
nation_id: 13
era: "EA"
epithet: "Enigma of Steel"
---

# EA Ulm — Enigma of Steel

EA Ulmは、**高性能な人間兵を正面戦闘とStealthの両方で運用し、広いが浅いMagic Accessを鍛造とResearchで実戦へ変える国家**です。

中世Ulmのような重装甲一辺倒ではありません。EA Ulmの中心は、

> **Forest・Mountainでも集められる戦士**
> ＋ **複数回攻撃と高いStrength**
> ＋ **Shield役とDamage役の分担**
> ＋ **Stealthy Commander・Mageによる機動戦**
> ＋ **Forge Bonusを持つWarrior Smith**

です。

序盤は国家兵の性能でIndependent Provinceを取り、中盤はEarth・Natureを中心としたArmy Buff、鍛造、Stealth Raid、Ulm固有のReanimationで戦力を拡張します。

一方、

- 盾を持たない主力が多く射撃へ弱い
- Recruitable MageのPathは広いが高Pathが安定しない
- 兵士のMagic Resistanceが低め
- Late gameの大規模魔法へ自然には届きにくい

という制約があります。

> **EA Ulmは、序盤の兵質で作った領土差を、Fort・Mage・Item・Stealthへ変換できるかが勝負です。**

- [自動生成Recruitデータ](../../data/recruitment/ea/ulm.md)
- [国家別Site Search能力](../../data/site-search/ea/ulm.md)
- [Extended Magic Access](../../data/extended-magic-access/ea/ulm.md)
- [Magic Access Route](../../data/magic-access-routes/ea/ulm.md)
- [Pretender設計サンプル](../../pretender/samples.md)

!!! note "このページの精度範囲"
    本文はDominions 6.35の固定データ、ゲーム内Nation・Unit・Spell・Item表示、公式Documentation、現行Inspector、および既存Community検証を照合し、実戦向けに再構成しています。Random Pathの個体差、Map、Independent構成、Pretender、Patch、MODによって最適解は変わります。正確なUnit Cost・装備・Random率は上記の自動生成データを優先してください。

---

# 一言でいうと

```text
強い国家兵で先に土地を取る
→ Shield役とDamage役を分ける
→ Warrior Smithを量産する
→ Earth・Nature Buffと安価なItemを揃える
→ 正面ArmyとStealth Armyを使い分ける
```

という国家です。

MA Ulmとの違いを短く表すと、

```text
EA Ulm
＝ 軽～中装、複数攻撃、Stealth、広いRandom Path

MA Ulm
＝ Blacksteel重装、Resource経済、均質なEarth Smith
```

です。同じUlmでも、Armyの組み方とMagic運用は別物です。

---

# 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | Early Age |
| Nation ID | 13 |
| Epithet | Enigma of Steel |
| Preferred Temperature | Cold寄り |
| 軍事の中心 | 高Strength人間兵、複数攻撃、Stealth、地形Recruit |
| 確実なMagicの軸 | Earth、Nature、Holy |
| Randomで広がるPath | Fire、Air、Water、Death等 |
| Priest | 主にH1、特殊個体・Heroに上位Holy |
| 経済特徴 | FortのResource生産に国家Bonus |
| Capitalの重要要素 | Steel Warrior、Antlered Shaman、複数Gemの開始Site |
| 操作量 | 中程度。Stealth ArmyとRandom Mage管理で増える |
| 主な弱点 | 射撃、AoE、MR攻撃、Magic Accessの再現性 |

---

# 国家エンジン

EA Ulmの強さは、一つのElite Unitや一つのSpellではなく、次の循環から生まれます。

```text
高性能な国家兵でExpansion
        ↓
Forest・Mountainを含む広いRecruit網
        ↓
GoldとFort候補を増やす
        ↓
Warrior Smith・Shamanを量産
        ↓
Buff・Forge・Site Search・Reanimation
        ↓
正面ArmyとStealth Armyを増やす
        ↓
敵Fort・Tax route・後方へ同時圧力
```

この循環が止まる典型例は、

- 初期兵を高損失で使い潰す
- MageをRandom結果だけ見て役割分担しない
- Fortを建ててもMageを継続雇用しない
- Stealth Unitを正面戦だけに使う
- Late game AccessをPretender・Summon・Boosterで準備しない

場合です。

---

# 強み

## 1. Goldに対して強い国家兵

EA Ulmの一般兵は、人間としては高いStrength・Attack・Moraleを持つものが多く、二本の武器や投擲武器を使う兵種もあります。

複数攻撃は、単にDamageを二倍にするだけではありません。

- 高Defence相手へ試行回数を増やす
- Harassmentを早く蓄積する
- Sizeの大きい敵へ一Square当たりの攻撃数を増やす
- Strength Buff・追加Damageを複数回利用する

という価値があります。

Early Ageに多いGiantや高HP Unitに対しても、十分なDamageと攻撃密度を作りやすい国家です。

## 2. 兵種を役割へ分けやすい

EA Ulmには、

- Shieldで射撃と接敵を受ける兵
- 二刀・二斧で攻撃密度を作る兵
- 高Damage武器でProtectionを抜く兵
- Archer・投擲で接敵前に圧力を掛ける兵
- Stealth Raidへ使う兵
- Capital-only Sacred

がいます。

一種類の兵を大量生産するより、相手に応じて比率を変えることで損失を抑えられます。

## 3. Stealthを国家規模で使える

Stealthyな兵、Commander、Shamanを組み合わせられるため、

```text
兵だけStealth
→ Mageが同行できず、正面戦では弱い
```

という問題を避けられます。

EA UlmのStealth Armyは、

- 空いたProvinceの奪取
- Tax route切断
- Scout・Lab・Templeへの圧力
- 敵Main Armyの迂回
- Fort包囲の補助
- 開戦前の位置偽装

に使えます。

ただしStealth値、Army規模、Patrol、Glamour・True Sight等により発見Riskは変わります。[最初の戦争・外交・Raid・迎撃Q&A](../../getting-started/war-faq.md)も参照してください。

## 4. Forest・MountainでLocal戦力を増やせる

一部のWarrior・CommanderをForestやMountainでRecruitできます。

これは単なるFlavorではなく、

- Fort建設前からScout・Commanderを補充する
- Capitalから遠い戦線でStealth Armyを形成する
- Choke pointやCave入口へ早く指揮官を置く
- FortのCommander PointをMageへ残す

という経済・物流上の強みです。

## 5. Warrior SmithのForge Bonus

Warrior SmithはEarthを軸に複数Pathへ広がり、Forge BonusとResource Bonusを持ちます。

そのため、

- Booster
- Resistance Item
- Counter用武器
- Thug装備
- Research Item
- Supply・移動補助

を通常より効率よく用意できます。

EA Ulmでは、Itemは少数Commanderを飾るものではありません。

> **広く浅いMagic Accessを、国家全体が使える技術へ変換する装置**

です。

## 6. Earth・NatureをArmy全体へ掛けやすい

Antlered ShamanはCapital-onlyですが、EarthとNatureを確実に持つ重要なSupport Mageです。通常ShamanにもEarth・Nature・Death・Fire等の組合せが生まれます。

これにより、

- Protection
- Strength
- Regeneration・回復
- Poison対策
- Supply
- Summon・Chaff

を国家兵へ加えられます。

元のStatsが高い兵ほど、Army Buffの回収率も高くなります。

---

# 弱み

## 1. 盾を持たない兵が多い

複数武器を持つ代わりにShieldを持たない兵が多く、

- Archer
- Crossbow
- Sling
- Precision Buff
- 長い接敵距離

へ損失が出やすくなります。

対射撃では、

```text
Shield Maidenを前へ
→ 主力Damage兵を後ろへ
→ Hold・配置で接敵Timingを揃える
→ Mageで射撃・防御を補助
```

とします。

## 2. Magic Resistanceが低め

高Protectionや高Damageは、MR Negates系のControl、Soul attack、Charm、Paralyze等を止めません。

Astral・Death・Glamour等のMR攻撃を見たら、

- MR Buff
- Antimagic
- Mage・Commander分散
- Mindless Summon
- 高価値兵を一Squadへ集中しない
- 敵CasterへRaid・Assassination圧力

を検討します。

## 3. Pathは広いが高Pathが安定しない

Warrior SmithとShamanはRandomによって多様なCrosspathを得ますが、欲しい個体を毎Game同じTurnに得られるとは限りません。

したがって、Magic Accessは、

```text
確実に毎Game使える
条件付きで使える
Rare Randomが出れば使える
Pretender・Hero・Site・Summonが必要
```

へ分けます。

[Magic Access Route](../../data/magic-access-routes/ea/ulm.md)を使い、Rare Randomを標準Planへ入れないでください。

## 4. Late gameの上限が自然には伸びない

序盤・中盤の兵とBuffは強力ですが、Global、最上位Battlefield Spell、複雑なBooster chainへはPretender・Summon Mage・Empowerment・Hero等が必要になります。

Early leadを作ったら、Turn 20以降に、

- どのPathを国家の第二軸にするか
- 何Gemを残すか
- どのBoosterを誰がForgeするか
- どのSummon Mageへつなぐか

を決めます。

## 5. 高火力ゆえに損失も出やすい

EA Ulmの兵は敵を速く倒しますが、防御を削って攻撃へ寄せた兵種も多く、勝っても高損失になることがあります。

特に、

- Capital-only Steel Warrior
- Rare Random Mage
- Antlered Shaman
- Booster所持Commander

を通常のAttritionへ混ぜないでください。

---

# 国家固有要素

## Fort Resource Bonus

EA UlmのFortはResource生産に国家Bonusを持ちます。

Fort候補を選ぶときは、表示Resourcesだけでなく、

- 隣接するHigh Resource Province
- Mountain・Forest
- 既存FortとのResource競合
- 何を生産するFortか
- Warrior SmithのResource Bonus

を見ます。

```text
Fort A：兵士・重装備を生産
Fort B：Mage中心
Fort C：Stealth Armyの中継
```

へ役割分担すると、全Fortで同じ兵を作るより効率が上がります。

## National Longdead

EA UlmはReanimation系の処理からUlmish装備を持つLongdeadを得られます。

主な用途は、

- Goldを使わない前衛・Chaff
- Siege要員
- Supply負担の軽い増援
- 高価な国家兵の損失分散
- Darkness・Undead支援との組合せ

です。

ただしPriest・Holy Damage・Banishmentへ弱く、通常兵とLeadership typeも異なります。

## Capital-only Steel Warrior

Steel WarriorはSacredで強い攻撃を持ちますが、Capital-onlyかつ高価です。

Heavy Blessを当然の選択とせず、

```text
毎Turnの供給数
Gold・Resources
Expansionで失う数
中盤のAnti-Sacred
通常兵との比較
Sacred MageへのBless価値
```

を見ます。

多くのGameでは、Light BlessまたはScalesを優先し、Steel Warriorを限定的なShock troopとして使う方が国家全体を伸ばしやすくなります。

---

# 兵士

正確なCost・装備・Statsは[Recruitデータ](../../data/recruitment/ea/ulm.md)を参照してください。ここでは役割で整理します。

## Warrior・Axe Warrior

安価な基礎兵で、Forest・Mountainからも供給できます。

主な役割：

- Expansion Armyの数
- Stealth Raid
- Defence Harassment
- Siege要員
- Elite兵の損失分散

二本の武器や投擲を持つ型は攻撃密度に優れますが、Shield不足と被射撃Damageに注意します。

## Archer・Warrior Maiden

接敵前にDamageと疲労を与える射撃役です。

### Archer

- 安価に射撃数を増やす
- 軽装・大型・ShieldなしTargetへ有効
- Counter-fireで失いやすい

### Warrior Maiden

- 一般Archerより前線耐性がある
- Stealth Armyへ射撃を追加できる
- 高価なので単純な弾数では不利

射撃はFriendly Fireを含むため、近接主力が接敵した後まで無条件に撃たせないようReplayを確認します。

## Forest Warrior・Mountain Warrior

通常Warriorより高性能なDamage役です。

- 高いStats
- 複数攻撃
- 対Giant・対重装への圧力
- Buffとの相性

が強みです。

一方、Stealthを持たない型があるため、Stealth Armyへ混ぜるとArmy全体の移動・潜伏計画が変わる点に注意します。

## Shield Maiden

EA Ulmで最重要のScreen候補です。

- Shieldで射撃を受ける
- 最初の接敵を受ける
- MageとDamage役の時間を作る
- 高価な兵の前へ置く

役割があります。

Damageだけを比べると他兵種に劣りますが、Army全体の損失を下げる価値があります。

> **Shield Maidenが敵を倒す必要はありません。後ろの兵とMageが働く時間を買えば成功です。**

## Iron Warrior

単発の高Damage武器を使う対Protection・対Large Unit役です。

- 高Protection Infantry
- Giant
- Regenerationを一撃で上回りたい相手

へ向きます。

高Defence相手には攻撃回数が少ないため、複数攻撃兵、拘束、Attack Buffと組み合わせます。

## Steel Maiden

Stealthと複数攻撃を両立する汎用Damage兵です。

- Raider
- 高Defence相手
- 通常Armyの側面
- Stealth Shamanと組む小軍

に向きます。

Shieldを持たないため、正面から射撃Armyへ走らせる運用は避けます。

## Steel Warrior

Capital-only Sacredの高価なShock troopです。

- 高Damageの一撃
- Bless対応
- Elite Targetの処理
- Bodyguard・Throne戦

に使えます。

大量生産できる通常兵と異なり、交換不能な資産として扱います。

---

# Commander・Mage

## Warrior Scout

Forest・Mountainで供給しやすいStealthy Scoutです。

- Border偵察
- Raid経路確認
- Stealth Armyの前方観測
- Gem・Itemを持たない安全な情報役

として数を用意します。

## Warrior Chief

Stealth Armyを率いる実用Commanderです。

- 通常兵のLeadership
- Formation
- 地方Recruit
- Raider指揮

に使います。

Mageを単なる運搬役へ使わず、Warrior Chiefへ兵を預けることでMageの行動Turnを守れます。

## Warrior Smith

EA Ulmの国家エンジンです。

主な役割：

- Research
- Forge
- Earth系Army Buff
- Fire・Air・Water等のRandom Path利用
- Resource Bonus
- Counter Item作成

個体ごとにPathが違うため、雇用後に役割を付けます。

```text
Smith A：確実なEarth Battle Mage
Smith B：Booster Forger
Smith C：Air / WaterのRare role
Smith D：Site Search
Smith E：Research Item量産
```

と分けます。

## Shaman

Earth・Holyを軸に、Nature・Death・Fire等へ広がるStealthy Mageです。

主な役割：

- Stealth Army支援
- Bless・Preach
- Nature・DeathのCrosspath
- Reanimation
- Site Search
- Upkeep効率のよい後方Mage

Inept Researcherであるため、Research Pointだけを見ればWarrior Smithに劣る場合があります。ただしSacredによるUpkeep、Stealth、Holy、Crosspathを含めると別の価値があります。

## Antlered Shaman

Capital-onlyのEarth・Nature主力Mageです。

- Army-wide Protection・Strength・Nature Buff
- Supply
- 高位Natureへの入口
- Site Search
- Ritual・Summon
- Stealth Armyの高級Support

を担当します。

Capital-onlyかつ高価なので、毎Turn無条件に雇うのではなく、

```text
次のResearch Breakpoint
必要なBattle数
現在のN2以上個体数
Capital Commander Point
```

で判断します。

---

# Magic Access

## 確実なLayer

- Earth：Warrior Smith・Shamanの基礎
- Nature：Antlered Shamanの確実な軸
- Holy：Shaman系

## Randomで広がるLayer

- Fire
- Air
- Water
- Death
- 追加Earth・Nature

Random個体は、出現前から必須Planへ入れません。

## 役割別に見る

| Path | 主な国家内役割 | 注意 |
|---|---|---|
| Earth | Protection、Strength、Forge、Siege、Summon | 最も再現性が高い |
| Nature | Regeneration、Poison対策、Supply、Summon | 確実な高めPathはCapital依存 |
| Fire | 範囲Damage、Fire Resistance、Forge | Random個体数とGemを確認 |
| Air | Precision、射撃対策、Shock、移動 | 高Pathは不安定 |
| Water | Quickness、Cold、Elemental、海進出 | 希少個体を失わない |
| Death | Reanimation、Skeleton、Fear、Summon Mage | Shamanの役割と競合 |
| Astral | Recruitableでは基本的に不足 | Pretender・Hero・Site等で補う |
| Glamour | Recruitableでは基本的に不足 | Dom6のCounter環境で弱点になり得る |
| Blood | 標準経済の外 | Empowerment・外部Accessが必要 |

## Pretenderで補う候補

Pretenderへ全部の欠落Pathを載せるのではなく、最初の一段を買います。

候補：

- Astral：MR防御、Crosspath、Ring系への入口
- Glamour：Stealth国家との相乗、Illusion・Counter
- 高Earth・Nature：Global・Summon・Forge bridge
- Air・Water：Rare Randomへの依存を下げる

[Extended Magic Access](../../data/extended-magic-access/ea/ulm.md)と[Pretender設計サンプル](../../pretender/samples.md)を併用してください。

---

# Pretender方針

固定Buildではなく、国家の問題から二案を比較します。

## Plan A：Imprisoned Scales

### 向く状況

- 国家兵だけでExpansionできる
- FortとMageを増やすほど強くなる
- Steel WarriorへHeavy Blessを必要としない
- Long gameを想定

### 買うもの

- Gold・Resources
- Population・Supply
- Research
- Fort・Mage数

### 犠牲

- Pretenderの早期行動
- Early Site Search
- 欠落Pathへの早期到達

### Test

- 二軍完成Turn
- 第二Fort開始Turn
- First war Research
- Pretender不在中のAstral・Glamour対策

## Plan B：Awake Expander

### 向く状況

- Capital周辺に危険なIndependentが多い
- 国家兵の損失を抑えたい
- 早い第二Fortが国力を大きく変える
- Pretenderが少ない装備で複数Matchupを処理できる

### 犠牲

- Scales
- Magic diversity
- Pretender死亡Risk

### Test

- Archer・Cavalry・Barbarian・Poison
- FatigueとAffliction
- Friendly Dominion依存
- 国家兵二軍との同時Expansion

## Plan C：Dormant / Rainbow Bridge

### 向く状況

- 国家兵Expansionは十分
- First war以降にAstral・Glamour・高Pathが必要
- Booster・Summon chainをPretenderから始めたい

### 買うもの

- 国家にないResistance
- Strategic Magic
- Global・Forge route

### 犠牲

- Strong ScalesまたはAwake速度

### Test

```text
登場後最初の仕事：
最初のForge：
最初のRitual：
最初のGlobal候補：
First warに間に合うか：
```

を埋めます。

---

# 序盤拡張

## Expansion Armyの基本形

標準形は、

```text
前：Shield Maidenまたは損失を受けるScreen
中：Forest / Mountain / Iron Warrior等のDamage役
後：必要に応じてArcher
Commander：安価なWarrior Chief
```

です。

Shaman・Warrior Smithを毎回同行させる必要はありません。国家兵だけで取れるProvinceにはMage turnを使わず、危険な相手へ限定します。

## Independent別の考え方

### Light Infantry・Militia

複数攻撃兵の得意相手です。

- 広いFormation
- 接敵を早める
- Archerがいるなら前列をShieldで保護

します。

### Heavy Infantry

単発高DamageのIron Warrior、Strength Buff、複数攻撃によるHarassmentを使います。

低Damage兵だけで長期戦にするとFatigueで損失が増えます。

### Cavalry・Lance

最初のChargeを低価値Screenへ受けさせます。

Damage役を最前列へ置かず、Hold・後方配置でCharge後に接敵させます。

### Barbarian

高Damageの一撃でShield役も死ぬため、人数だけで安全と判断しません。

- 射撃で先に減らす
- Defence・Attackで先に倒す
- Retreat routeを確保

します。

### Archer・Crossbow

Shield Maiden比率を上げ、主力を後方へ置きます。

盾なしの複数攻撃兵を最前列へ置くと、接敵前に国家の長所を失います。

### Elephant・Trample

Size、Morale、高Damage、射撃、拘束を組み合わせます。

細い一列で受けず、CommanderのMoraleとRoutも確認します。

### Undead

ShamanのHoly、Morale、長期戦を意識します。

通常兵は強いですが、Fear・Need Not Eat・Mindless等により想定と違う戦闘になる場合があります。

## 二軍への分割

分割条件：

- 両ArmyにCommanderがいる
- 両ArmyにScreenとDamage役がいる
- それぞれ安全な標的がある
- 敗北時のRetreat先がある

兵数が増えただけで半分にしないでください。

```text
一軍：危険Provinceを取る精鋭
二軍：低Risk Provinceを量産兵で取る
```

と難易度を分けます。

---

# Economy・Fort計画

## Capital

Capitalは、

- Steel Warrior
- Antlered Shaman
- 開始Gem
- 初期兵生産

を同時に担います。

Commander PointとResourcesを何へ使うか毎Turn明確にします。

## 第二Fort

候補は、

1. High ResourceのMountain・Forest周辺
2. 前線へ近いRecruit中継
3. Mageを安全に量産できる後方
4. Choke・Throne・Plane入口

です。

Fort Resource Bonusがあるため、良い立地では通常より多くの兵を生産できます。

ただしFortを密集させると隣接Resourceを奪い合うため、[Forts](../../systems/forts.md)のResource drawも確認します。

## Mage生産優先

一般的には、

```text
Warrior Smithを継続
＋ 必要なShaman
＋ Timingに合わせたAntlered Shaman
```

です。

兵士を一体増やすためにMage雇用を止める場合は、再開Turnを決めます。

## Gold配分

```text
Expansion補充
＋ Mage継続雇用
＋ 第二Fort
＋ 緊急予備
```

へ分けます。

Stealth Raidが得意だからといって、正面ArmyとFort投資を削りすぎないようにします。

---

# Researchルート

ResearchはSchool名ではなく、次の戦争で何を成立させるかから逆算します。

## Route A：Earth・Nature Army Buff

目的：国家兵のStatsをArmy-wideに増幅する。

優先する役割：

- Protection
- Strength
- Reinvigoration
- Regeneration・回復
- Poison Resistance
- Battlefield-wide防御

このRouteは、元から強い兵を少数のMageで一段上へ押し上げます。

### 必要確認

```text
使用Mage：Warrior Smith / Shaman / Antlered Shaman
Buff前に接敵しない配置：
必要Gem：
敵のAP・AN・Poison・MR攻撃：
```

## Route B：Construction・Forge Economy

目的：Forge Bonusを国家全体の技術へ変える。

- Booster
- Research Item
- Resistance Item
- Counter武器
- Supply・移動補助
- Thug・Commander保護

を優先します。

Constructionだけ上げてForgeするGemがない、装備者がいない、という状態を避けます。

## Route C：Death・Reanimation・Summon

目的：Gold兵の前へ低Upkeep・Need Not Eat系戦力を追加する。

- National Longdead
- Skeleton Chaff
- Siege要員
- Summon Mage route

を使います。

敵Priestが多い場合は、Undeadだけへ依存せず通常兵を残します。

## Route D：Random Pathの即応

良いAir・Water・Fire個体を得た場合、その個体のためだけに全Researchを曲げません。

```text
現在の第一Breakpoint
＋ Rare個体で開く短い追加Route
```

として利用します。

例：

- Air個体：射撃支援・Shock対策
- Water個体：Quickness・Cold・Elemental
- Fire個体：Fire Resistance・範囲Damage
- Death個体：Reanimation・Fear・Summon

研究レベルと要求Pathは[Spellデータ索引](../../data/spells/index.md)で現行値を確認してください。

---

# 重要Spell・運用テーマ

固定のSpell listではなく、役割で選びます。

| 目的 | 主なPath | 戦術上の意味 |
|---|---|---|
| 前衛のProtection | Earth / Nature | Shield役が時間を買う |
| Damage増加 | Earth / Fire | 複数攻撃と相乗 |
| 射撃対策 | Air / Earth | 盾なし主力を守る |
| Poison対策 | Nature | 持久戦を成立させる |
| Shock対策 | Air / Item | Air国家へ備える |
| Chaff追加 | Death / Nature | 高価な兵の損失分散 |
| Control | Earth / Nature / Glamour外部Access | 高Defence・Giantを止める |
| MR防御 | Astral外部Access / Item | 国家の主要弱点を補う |

---

# Magic Item

## Forgeの優先順位

1. 次のResearch Breakpointを使えるようにするBooster
2. 敵主DamageへのResistance
3. Rare Mage・Commanderの生存
4. Research加速
5. Thug・Counter Commander

です。

「安くForgeできるから作る」ではなく、何Battle・何Turnで回収するかを書きます。

## Rare RandomをItem Carrierにしすぎない

希少なAir・Water・Death個体へ、

- 高価なItem
- 大量Gem
- Main Army Leadership

をすべて集中させると、一度の暗殺・Routで複数の国家機能を失います。

Forger、Battle Caster、Carrierを可能な範囲で分けます。

## Counter-thug

Warrior SmithのForge Bonusを使い、敵Thugへ必要な一機能だけを持つCommanderを作れます。

```text
Magic Weapon
高Damage
Elemental Resistance
MR
Fatigue対策
Returning・退却
```

を敵に合わせます。

万能SCを目指すより安価です。

---

# Army構成

## 1. 標準正面Army

```text
前衛：Shield Maiden
第二線：Forest / Mountain / Iron Warrior
側面：Steel Maiden・Warrior
後衛：Archer / Warrior Maiden
Mage：Earth・Nature Buff、必要なResistance
Commander：後方分散
```

勝利条件：

> Shieldで最初の射撃と接敵を受け、Buff後の高Damage兵が敵前衛を短時間で崩す。

## 2. Stealth Army

```text
Commander：Warrior Chief
Support：Stealthy Shaman
兵：Warrior / Steel Maiden等のStealth部隊
目的：薄いProvince、Tax route、Lab、Retreat route
```

Main Armyとの正面決戦を避け、敵を分散させます。

## 3. Anti-Giant Army

- 高Damage単発兵
- 複数攻撃によるHarassment
- Strength Buff
- Chaffで攻撃回数を吸う
- Fatigue・Control

を組み合わせます。

GiantのHPだけを見ず、SizeによるSquare占有と攻撃密度差を利用します。

## 4. Anti-Archer Army

- Shield Maiden比率を増やす
- 配置を後方へ
- Wideではなく被弾密度を考えたFormation
- Air・Earth・Itemで射撃対策
- Stealth RaidでArcher生産地を狙う

とします。

---

# Battle Script

## Earth Support例

```text
Self Path boost
Protection / Strength Buff
Army support
Cast Spells
```

具体SpellはCaster PathとResearchに合わせます。

## Nature Support例

```text
Self Path boost
Poison / Elemental Resistance
Regeneration・Protection
Control / Summon
Cast Spells
```

## Stealth Shaman例

```text
必要なBless / Sermon
前衛Buff
Summon / Control
Cast Spells
```

Stealth ArmyではGem補給が遅れやすいため、何Battle分を持たせるか明記します。

## Script確認

- Research済みか
- PathとGemが足りるか
- Buff前に接敵しないか
- Targetが存在するか
- Casterが射撃・Flankを受けないか
- Gemを別Spellへ使わないか

をReplayで確認します。

---

# Raid・Map Control

EA UlmのRaidは、Provinceを永久保持することだけが目的ではありません。

```text
敵Incomeを止める
Tax routeを切る
Scoutを消す
Temple・Labへ圧力
Main Armyを後退させる
Fort救援を遅らせる
```

ことで価値を得ます。

## Raid Targetの優先順位

1. Fort・Throneへの接続
2. Tax routeの中継
3. Lab・Temple
4. 高Income
5. Retreat route
6. 敵のScout網

## 退却計画

Stealthで入れたから安全とは限りません。

- Patrol
- Enemy Dominion
- 退却先
- River・Mountain接続
- 同Turnの敵Movement

を確認します。

---

# Siege

高Strength兵と多数の通常兵はSiegeへ貢献します。National LongdeadやBear等のSummonも壁破壊要員になります。

ただし、

```text
壁を壊すArmy
≠
Stormに勝つArmy
```

です。

Stormでは、

- Choke
- Wall defender
- AoE
- Morale
- Fatigue
- Commander生存

を別に準備します。

Stealth Armyを後方へ回し、Relief routeを切ることでMain Siege Armyを守るのもEA Ulmらしい戦い方です。

---

# Counterされるもの

| 相手の手段 | なぜ危険か | 対応 |
|---|---|---|
| Massed Archer・Crossbow | Shieldなし主力が接敵前に減る | Shield Maiden、配置、射撃対策、Raid |
| AoE Evocation | 密集した人間兵がまとめて死ぬ | Formation、Resistance、複数Army |
| MR Negates Control | 低めのMRを狙われる | MR Buff、Antimagic、Caster圧力 |
| Poison・Foul Vapors | Protectionを迂回し長期戦で崩す | Nature、Resistance、短期決戦 |
| AP・AN | BuffしたProtectionを破る | HP、Defence、Chaff、別防御層 |
| Fear・Morale attack | 人数が残っていてもRout | Priest、Leadership、Morale Buff |
| Fatigue戦術 | 重装・長期戦でStatsが落ちる | Reinvigoration、戦闘時間短縮 |
| Anti-Sacred | Steel Warriorへ効率よく交換 | 通常兵を主力にしSacredを限定運用 |
| Assassin・Remote attack | Rare Random Mageを失う | Bodyguard、分散、後方Fort |
| True Sight・Patrol | Stealth Raidを発見 | Scout、複数経路、正面圧力と同期 |

---

# 対主要Archetype

## 高Protection

- Iron Warrior等の高Damage
- Strength Buff
- AP・AN Item・Spell
- Fatigue・Poison等の別防御層

を用意します。

## 高Defence・Glamour

- 複数攻撃
- Attack Buff
- AoE
- True Sight外部Access
- ChaffでHarassment

を使います。

## Giant

一Square当たりの攻撃数、Chaff、Fatigue、Controlで優位を作ります。

## Undead・Demon

Shaman・Priestを増やし、通常兵だけで長期戦をしないようにします。

## Poison Army

Nature Accessを活かし、前衛だけでなくCommander・MageまでResistanceを確認します。

## Astral・MR攻撃

最重要Counterです。

- Antimagic
- MR Item
- Mindless Chaff
- Mage分散
- StealthでCaster後方を狙う

を複数用意します。

---

# First War Plan

EA Ulmは序盤の兵質を持つため、開戦を急ぎすぎることがあります。

戦争前に、

```text
目的Fort / Throne：
敵の主Damage：
敵の射撃量：
敵のMR攻撃：
自軍のScreen：
自軍のDamage役：
必要Buff：
必要Gem：
Stealth ArmyのTarget：
Siege要員：
Retreat Province：
撤退条件：
```

を埋めます。

## 開戦時の二層圧力

```text
Main Army
→ 敵主力・Fortへ圧力

Stealth Army
→ Tax route・後方・Relief routeへ圧力
```

を同時に行うと、敵はCounter Armyを一か所へ集中しにくくなります。

ただしMain Armyから必要な兵を抜きすぎないようにします。

---

# Midgame

Midgameの課題は、序盤の兵質をMagicへ接続することです。

優先順位：

1. FortとMage数
2. Earth・NatureのArmy-wide Buff
3. 必要Resistance
4. Forge economy
5. Stealth Armyの複数化
6. Death・SummonによるChaff
7. Astral・Glamour等の欠落Path

序盤に取ったProvinceが多いほど、Strong ScalesとFort投資を回収できます。

---

# Late game

Late gameでは通常兵だけでBattlefield-wide Spellへ突入しないようにします。

必要になるもの：

- Summon Mage
- Booster chain
- Global
- Remote Ritual
- Magic Phase移動
- Mindless・Elemental・Undead等のSummon Army
- MR・Elemental Resistance
- Thug・SC Counter

Pretenderを単なるDesign Point箱として終わらせず、国家にないStrategic Pathを担当させます。

EA UlmのLate game目標は、

> **序盤の兵国家から、安価なItemと複数Pathを使うCombined Arms国家へ移行すること**

です。

---

# Multiplayer

## 相手から見たEA Ulm

- 序盤の国家兵が強い
- StealthでBorderが読みづらい
- Forge BonusでCounter Itemを作る
- Magic Accessは個体差が大きい
- Late game前に止めたい

と見られます。

そのため、兵をBorderへ集めすぎると早期Coalitionを呼ぶ場合があります。

## 隠したい情報

- Rare Random MageのPath
- Stealth Armyの所在地
- Pretenderが補ったPath
- Booster chain
- Main ArmyとRaiderの分離

です。

## 見せてもよい圧力

Stealthの存在を完全に隠すだけでなく、

> どのBorderを空けると後方へ入られるか分からない

状態を作ること自体が外交・抑止になります。

---

# よくある失敗

## 1. 全兵をDamageだけで選ぶ

Shield役が不足し、射撃とChargeで接敵前に損失が出ます。

## 2. Stealth Unitを通常Armyへ混ぜるだけ

StealthのMap Control価値を使っていません。

## 3. Random Mageを確定Accessとして研究する

欲しい個体が来ず、Researchだけ完成して使えません。

## 4. Forge Bonusで不要Itemを量産する

GemがBooster・Battle Spell・Summonへ回りません。

## 5. Steel WarriorへHeavy Blessを掛ければよいと考える

供給量とScales損失が合っていません。

## 6. Antlered Shamanを通常研究者として消費する

Capital-only Support PathをFirst warで使えません。

## 7. 兵質だけでLate gameまで押す

MR攻撃とBattlefield-wide Magicに止められます。

## 8. Stealth Raidに退路がない

発見・迎撃されてArmyごと失います。

## 9. Fort Resource Bonusを見ずFortを建てる

兵士生産Fortとしての価値を回収できません。

## 10. 勝ったReplayを見ない

Capital-only兵、Mage、Commanderの不要損失を見逃します。

---

# 初回Play用チェックリスト

## Turn 1–12

- [ ] Shield役とDamage役を分けた
- [ ] Warrior Smithを止める理由がある
- [ ] Forest・Mountain Recruitを確認した
- [ ] 二軍を作る前にCommanderを用意した
- [ ] 射撃IndependentへShieldを増やした
- [ ] 第二Fort候補のResourcesを見た

## First war前

- [ ] 敵の射撃・MR攻撃・Poisonを確認した
- [ ] Earth・Nature BuffのCasterがいる
- [ ] Gemを何Battle分持たせるか決めた
- [ ] Stealth ArmyのTargetと退路がある
- [ ] Siege要員を別に数えた
- [ ] Rare Randomへ国家Planを依存していない

## Midgame

- [ ] Booster routeを一つ完成させた
- [ ] Death・Summon等で損失分散を始めた
- [ ] Astral・Glamour不足への回答がある
- [ ] Fortごとの役割を分けた
- [ ] Pretenderの次の仕事が決まっている

---

# 情報源・検証

- Dominions 6.35ゲーム内Nation Overview
- Unit・Commander・Spell・Item popup
- Battle Replay
- 固定したDominions 6 Mod Inspector data
- [Recruitデータ](../../data/recruitment/ea/ulm.md)
- [Magic Access Route](../../data/magic-access-routes/ea/ulm.md)
- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [Illwiki EA Ulm](https://illwiki.com/dom5/ulm-ea)（構成・既存Community知見の確認。数値はDom6 6.35側を優先）

## 更新履歴

| 日付 | Version | 内容 |
|---|---|---|
| 2026-08-17 | 6.35 | 初版。Roster、Expansion、Magic、Pretender、Research、Raid、Counterを統合 |
