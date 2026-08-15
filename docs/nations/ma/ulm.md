---
title: MA Ulm
page_type: nation-guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
nation_id: 60
era: "MA"
epithet: "Forges of Ulm"
---

# MA Ulm — Forges of Ulm

MA Ulmは、**優秀な黒鋼兵を並べるだけの国家ではありません。**

本当の国家エンジンは、

> **Resourceの高いFort**
> ＋ **役割を分けた重装兵**
> ＋ **量産できるMaster Smith**
> ＋ **Earth魔法と安価な鍛造**

を同時に増やすことです。

重装兵が敵を受け止めている間にMageが拘束・強化・Armor対策・国家固有Spellを重ね、そこで得た主導権を第二Fort、第三Fort、さらに多くのMageへ変換します。

- [自動生成Recruitデータ](../../data/recruitment/ma/ulm.md)
- [国家別Site Search能力](../../data/site-search/ma/ulm.md)
- [Extended Magic Access](../../data/extended-magic-access/ma/ulm.md)
- [Magic Access Route](../../data/magic-access-routes/ma/ulm.md)
- [国家別Recruit装備Profile](../../data/equipment-usage/nations.md)

!!! note "記事とデータ索引の役割"
    Unitの正確な能力値、Gold・Resource、Weapon、Armor、Mount、固定Path、Random Pathは自動生成ページを参照してください。このページでは、それらをどう組み合わせて勝つかを扱います。

!!! warning "古い攻略情報について"
    MA Ulmは旧作でも人気国家ですが、Dom4・Dom5の研究レベルをそのまま使わないでください。たとえばDom6.35では、Strength of Giants、Earth Meld、Weapons of Sharpness、Legions of Steelなどの研究位置が旧Guideと異なります。本文のBreakpoint表は固定6.35データに合わせています。

---

## 一言でいうと

**高Protectionの人間兵を、Master SmithのEarth魔法・鍛造・研究量で段階的に強化し、早～中盤の正面戦闘で国力差を作る国家。**

### 勝ち筋

1. 半黒鋼兵と役割分担で、序盤拡張を低損失に進める
2. 第二Fortを建て、Master Smithの継続生産を始める
3. 低～中ResearchのEarth魔法で第一戦争を有利にする
4. Forge BonusをBooster、Resistance、Research、専用装備へ変換する
5. 相手がProtection対策を出す前に、別の防御層とDamage手段を追加する
6. Late gameへ入る前に、Pretender・Independent Mage・召喚でMagic diversityを確保する

MA Ulmは、序盤に強いから何もしなくても勝てる国家ではありません。

**序盤の軍事的余裕を、研究所とMage生産へ変換できたときに強い国家**です。

---

## 国家の特徴

### 強み

- 人間兵として非常に高いProtection
- 盾、長武器、複数攻撃、高Damage、射撃、騎兵、対Sacredなど役割別の兵種
- F1E2を土台とするMaster Smithを各Fortで量産可能
- Forge BonusによりGemを効率よくItemへ変換
- Master SmithのResource Bonusで重装兵生産を支援
- Earth魔法と重装兵の相性がよい
- 国家固有のIron Darts、Iron Blizzard、Tempering the Will
- Capital-onlyのMaster MasonによるFort・Siege面の強化
- 通常兵Expansionが安定しやすく、Pretenderを軍事以外へ回しやすい

黒鋼兵の説明にも、通常のPlateより強く軽い黒鋼装備、重装訓練、一般人間兵より高い耐久性、そして魔法への脆弱性が国家像として明示されています。

### 弱み

- 一般兵のMagic Resistanceが低い
- 高Protectionへ投資しているため、AN、Poison、MR攻撃、Fatigueに価値を否定されやすい
- InfantryのDefenceが低く、命中・Repel・拘束の影響を受けやすい
- Armyの戦略・戦術移動が重くなりやすい
- 重装兵はResource依存が強く、Fort配置が悪いと生産量が伸びない
- Native MagicがEarth中心で、Air・AstralはRandom、Nature・Death・Water・Glamour・Bloodは外部Accessへ依存しやすい
- Earth GemをBooster、Battle Spell、Item、Ritualで奪い合う
- Late gameでは人間兵のHPと狭いMagic diversityが問題になりやすい

### 初心者向けか

**国家の第一案は分かりやすいが、第二案を作る練習が必要な国家**です。

学びやすいもの:

- ProtectionとDamageの関係
- Shield、Repel、Weapon Length
- ResourceとFort配置
- Mage量産とResearch
- Army Buff
- BoosterとForge economy
- 敵のCounterへDamage typeを切り替える考え方

誤解しやすいもの:

- Protectionが高ければ全てに強い
- 一番高価な兵だけ雇えばよい
- Forge BonusがあるからItemを大量に作ればよい
- Earthだけ研究すればLate gameまで十分

---

# 国家運営の基本

## 三つの生産物

MA UlmのFortは、三種類のものを生産します。

1. **現在の戦争を戦う兵士**
2. **将来の戦争を解禁するMaster Smith**
3. **前線を支えるCommander・Siege要員**

一つのFortへ全役割を詰め込むと、ResourceとCommander Pointが競合します。

### 首都

首都は、

- Capital-only Commander・Priest
- Master Mason
- Guardian
- Priest Smith
- Black Priest

など、他Fortで代替しにくい生産を担当します。

### 通常Fort

通常Fortは、

- Master Smith
- 主力Infantry
- Commander
- 必要に応じたBlack Knightや射撃兵

を生産します。

### Mage Fort

GoldはあるがResourcesが低いFortでも、Master Smith生産には価値があります。

全Fortで黒鋼兵を最大生産する必要はありません。

> **Resource Fortは兵士を作る。低Resource FortはMageを作る。**

と役割を分ける方が国家全体は伸びます。

---

## Gold・Resource・Commander Point

### Gold

Goldは兵士、Master Smith、Fort、Lab、Templeの全てに必要です。

序盤に黒鋼兵を買いすぎると、第二Fortが遅れます。逆にFort資金を守りすぎるとExpansionが止まります。

### Resource

MA UlmはResourceを実際の軍事力へ変換しやすい国家です。

そのため、

- Productivity
- Mountain / Highland
- Fortの周辺Province
- Master SmithのResource Bonus
- Fort同士のResource競合

を重視します。

### Commander Point

Master Smithは高品質ですが、Commander Pointを使います。

Fort数とFort品質が、

- Research量
- Battle Mage数
- Forge turn
- Site Search能力

を決めます。

兵士の数だけでなく、**毎Turn何人のMaster Smithを増やせるか**を国力指標にします。

---

# Pretender方針

MA Ulmは国家兵だけでもExpansionしやすいため、Awake Expanderを必須としません。

Pretenderでは、国家にない役割を補います。

## 第一候補：Scales＋Magic diversity

最も標準的な方向です。

### 目的

- GoldとResourceを増やす
- FortとMaster Smithを早く増やす
- Nativeに薄いNature、Air、Astralなどを補う
- Site SearchとBoosterの入口を作る
- Poison、Shock、MR攻撃への回答を用意する

### 向く状況

- 国家兵Expansionが安定するMap
- 中盤のMage数とResearch差を重視
- Heavy Blessを必要としない
- Long gameを想定

### 特に考えたいPath

#### Nature

MA UlmのProtectionを無視するPoison対策へ直結します。

N2以上をPretenderで確保すると、Nature Booster、Poison Resistance、回復、召喚への入口を作りやすくなります。

#### Air

Shock対策、移動、射撃防御、Air Itemへの入口になります。

Air RandomのMaster Smithだけへ国家計画を依存させない保険です。

#### Astral

MR支援、Communion、Teleport、Booster、Magic Duel対策を考えるPathです。

Astral Random Master Smithは重要ですが、出現時期が不確定です。

#### Earth

国家の得意Pathをさらに高くし、Global、上位Forge、Contact Iron Angelなどへ到達します。

ただしEarthだけを伸ばすと、国家の既存長所は強くなっても弱点は残ります。

---

## 第二候補：Dormant Support / Global Caster

序盤は国家兵で戦い、Pretender登場後に、

- Booster Forge
- Global
- Ritual
- Magic diversity
- Resistance
- 高Path Army Spell

を担当させます。

AwakeよりDesign Pointを確保しつつ、最初の本格戦争へ間に合わせやすい構成です。

---

## Awake Expander

使用するなら、目的を明確にします。

### 採用理由

- Mapが狭く初動速度が重要
- 首都周辺Independentが黒鋼兵に不利
- 第二Fortを極端に急ぐ
- 国家兵を首都防衛・第二Armyへ回したい

### 問題

- ScalesまたはMagic diversityを失う
- Pretender死亡時に国家の外部Pathを失う
- MA Ulmは元々Expansion能力が高く、投資が過剰になりやすい

Awakeを採る場合も、Pretenderだけで全Expansionを行わず、通常兵の第二Armyを早く作ります。

---

## Bless

MA UlmはHeavy Bless国家ではありません。

SacredなPriest・CommanderへBlessが作用しても、国家全体の主力である通常兵には作用しません。Guardianの対Sacred性能もHeavy Blessを必要としません。

Blessを取る場合は、

- Pretender本人
- Sacred Priest / Commander
- 特定の召喚
- ResistanceやMR補助

など、国家全体へ別の形で価値があるものを選びます。

---

## Scalesの考え方

### Productivity

重装兵の生産量へ直結しやすく、優先度が高いScaleです。

### Order / Turmoil

Gold安定、Event、Recruit需要、Map条件から決めます。

MA UlmはFortとMageへGoldを大量投入するため、安定収入には価値があります。

### Growth / Death

長期Gold、Supply、Population、Eventとの交換です。

短期戦だけを想定してDeathを深く取ると、戦争が長引いたときにFort生産とSupplyで苦しくなります。

### Magic / Drain

Master SmithはMundane Researcherとして、通常Mageとは異なるResearch特性を持ちます。

このためDrainを採用しやすい国家ですが、

- 自国Dominion内外
- MR環境
- PretenderやIndependent MageのResearch
- Magic SiteやSpellの運用

も含めて判断します。

「昔からUlmはDrain」という理由だけで固定せず、現在のGame設定とTooltipを確認してください。

詳しくは [Pretender God](../../pretender/index.md) と [Scales](../../pretender/scales.md) を参照してください。

---

# 序盤拡張

MA UlmのExpansionは、**最も高価な兵を最も多く並べる作業ではありません。**

相手に必要な耐久とDamageだけを用意し、第二Armyと第二Fortの資金を残します。

## 基本編成

### 盾兵

役割:

- Archer・CrossbowからDamage役を守る
- 最初に敵を受ける
- 接敵後の戦線を維持する
- Commanderへ敵を通さない

### 高Damage兵

役割:

- Heavy Infantry
- Cavalry
- Giant
- 高HP Independent

を倒します。

盾を持たない兵は、敵射撃とRepelへ弱くなりやすいため、前へ出しすぎません。

### Flail / 複数攻撃兵

役割:

- 大量の軽装兵
- 高Defence兵
- 攻撃回数で押す相手

へ向きます。

Strength Buffと相性がよい一方、低Defenceと短いWeaponによるRepelに注意します。

### Pikeneer

役割:

- Cavalry
- 長Weapon
- Repel
- 高Damageの少数兵

への前線です。

Damageは他兵種に劣るため、全軍をPikeneerだけにしません。

### Black Knight

Blacksteel Bardingを持つ重騎兵で、少数でもExpansion、側面攻撃、PD Raidへ使えます。

ただし、

- GoldとResource
- Lance後の継続戦闘
- Shock・Poison・MR攻撃
- Mountを失った後

まで見て評価します。

Black Knightを量産しすぎると、Master SmithとFortが遅れます。

---

## Independent別の注意

### Bow・Sling

盾兵を前へ置き、Damage役を後方へ置きます。

### Crossbow・Arbalest

高Protectionでも危険です。

射線、盾、Sparse配置、接敵速度を調整します。

### Heavy Infantry

Protection対Protectionの長期戦になります。

高Damage、複数攻撃、拘束、疲労差を使います。

### Cavalry

Lance Chargeを盾・Pikeで受け、Damage役を後から接敵させます。

### Barbarian

命中すれば重装兵にも大Damageを出します。

兵数を減らしすぎず、射撃または複数攻撃で接敵前後に数を落とします。

### Elephant / Trampler

高Protectionだけでは止まりません。

Morale、Size、Pike、射撃、配置を確認します。

### 高Defence

攻撃が当たらないなら、Flail等の攻撃回数、Earth Meld、射撃、魔法を使います。

---

## 第一Armyの役割

第一Armyは、

- 安全なProvinceを取り続ける
- 首都周辺Resourceを解放する
- 第二Fort候補へ道を作る
- Scoutへ敵情報を与える

ためのものです。

不利なIndependentへ無理に入って損失を出すより、別方向へ曲がる方がよい場合があります。

## 第二Armyを作るTiming

次が揃ったら、第一Armyを大きくし続けるより第二Armyを作ります。

- 第一Armyが通常Independentへ安定して勝てる
- Commanderを追加できる
- 首都生産が一軍の補充だけで埋まっていない
- 第二方向に安全な標的がある
- 第二Fort資金を完全には潰さない

[序盤拡張](../../getting-started/expansion.md)の記録Templateを使い、兵種別の損失を確認してください。

---

# CommanderとMage

## Master Smith

Master SmithはMA Ulmの国家エンジンです。

基本のF1E2に加えて、個体によって追加Fire、Earth、Air、Astralを得ます。正確なRandom率は[Recruitデータ](../../data/recruitment/ma/ulm.md)で確認してください。

主な役割:

- Research
- Earth支援
- Fire ElementalなどのFire活用
- Forge
- Booster
- Site Search
- Rare RandomによるMagic diversity

Master SmithはForge BonusとResource Bonusを持ちます。ゲームデータ上の説明でも、Ulmの武器・Armor生産を担い、魔法資源が乏しいため少ないGemでItemを作る技術を発達させた存在として扱われています。

### 量産個体

大半のMaster Smithは、

- Research
- 基本Earth Spell
- 日常的なForge

を担当します。

### Specialist

Air、Astral、追加Earth、追加Fireを得た個体は、通常Researcherと混ぜずに名前変更して保護します。

例:

```text
A-Smith / Air Item担当
S-Smith / Crystal・Communion担当
E3-Smith / 高Earth Forge担当
F2-Smith / Fire Battle・Forge担当
```

Rare Randomを前線の雑なEvocation役として失うと、国家全体のMagic Accessを失います。

### Forge Bonusの使い方

Forge Bonusは、Gemを節約する能力です。

**目的のないItemを作る権利ではありません。**

優先順位:

1. 新Spell・新Forgeを開くBooster
2. Army全体の弱点を補うResistance
3. Research投資を回収できるResearch Item
4. 重要Casterの生存装備
5. 明確な標的を持つBlack Lord装備
6. 便利だが勝利条件へ直結しないItem

---

## Priest Smith

Capital-onlyのF1E2H1 Mageです。

主な用途:

- 国家固有Iron Spell
- Earth支援
- Priest役
- Forge
- Sacred Commanderとしての役割

Iron Blizzardは高Fatigueなので、継続Castさせる場合はPath、Reinvigoration、Gem、配置を考えます。

## Black Priest

Capital-onlyのEarth・Holy Priestです。

主な用途:

- Iron Darts / Iron Blizzard
- Inquisitor / Preach
- Undead対策
- Throne・Dominion戦
- Iron Cultの宗教戦

安価なHoly役とBattle casterを兼ねられますが、Capital Commander Pointとの競合があります。

## Master Mason

Capital-onlyの戦略Commanderです。

- Fort upgrade
- Siege Bonus
- Castle Defence

を担当します。

MA UlmはField Battleに勝っても、Fortを取れなければ優位を国土へ変換できません。

Master Masonを使い、

- 前線Fortを早く割る
- 重要Fortを強化する
- Commander Pointを増やす

という戦略価値を得ます。

## Black Lord

Black Lordは完成済みの重装騎兵Commanderです。

向く用途:

- Black Knight部隊の指揮
- 弱いPDへのRaid
- Rear / Flank対策
- 専用Counter装備
- 主力Armyの追加打撃力

向かない用途:

- 目的のない高価なFull gear
- 強力なMage Thugとの正面戦闘
- AN、Soul Slay、Charm、Fatigueへの無対策突撃
- 国家唯一のBoosterを持たせた使い捨てRaid

Black LordのItemは、

```text
倒す対象
→ 必要Damage
→ 必要Resistance / MR
→ Retreat方法
```

の順で決めます。

[Thug・SC装備](../../items/thug-equipment.md)も参照してください。

---

# 兵種の使い分け

正確なWeapon・Armorは[Recruitデータ](../../data/recruitment/ma/ulm.md)と[装備Profile](../../data/equipment-usage/nations.md)を参照してください。

## 半黒鋼兵

- Resource効率がよい
- Expansion Armyを分割しやすい
- 通常Independentには十分なProtectionを持つ
- 完全黒鋼兵より補充しやすい

序盤の領土拡張では、最も重いArmorだけを買うより、半黒鋼兵を含めてArmy数を増やす方が強い場合があります。

## 完全黒鋼兵

- 正面戦闘のLine holder
- 通常物理への高い耐久
- Earth Buffの土台
- Resource負担が大きい

相手が通常物理中心なら強力ですが、Protectionを参照しない攻撃へは価格分の耐久を得られません。

## 盾兵

- 射撃対策
- 前線維持
- Commander防衛
- Damage役の時間作り

## 両手・高Damage兵

- 高Protection
- Giant
- 高HP
- Armorを削った後の処理

へ使います。

## Flail・複数攻撃兵

- Chaff
- High Defence
- Mirror Image等の回数消費

へ使います。

## Pikeneer

- Repel
- Cavalry
- 長Weapon
- 高Damage少数兵

を受けます。

## Crossbow / Arbalest

高Protection相手へ届く一方、発射間隔とFriendly Fireに注意します。

自軍の重装兵を敵より射ち抜くこともあります。

## Guardian

Capital-onlyの対Sacred兵です。

敵Sacredの正面へ当てる価値がありますが、

- Capital生産
- 高Resource
- 補充速度

を考え、通常前衛として消耗させすぎません。

## Sapper

Siege Bonusを持つ射撃兵です。

戦闘火力だけでなく、Fort壁を早く壊すために必要数を準備します。

---

# Research方針

Researchは「EarthだからAlterationだけ」と決めません。

MA Ulmの研究は、

1. **兵士を当てる**
2. **兵士のDamageを通す**
3. **Protection以外を守る**
4. **MageのPathとFatigueを改善する**
5. **Fort戦を終わらせる**

ために組みます。

## Dom6.35の主要Breakpoint

| School | Level | Spell | 要求 | 役割 |
|---|---:|---|---|---|
| Enchantment | 1 | Strength of Giants | E2 | InfantryのDamageを上げる早期Buff |
| Conjuration | 3 | Summon Earthpower | E2 | 戦闘中E+1とReinvigorationを得る基礎 |
| Alteration | 3 | Earth Meld | E2 | 高Defence・高Damage敵を拘束する |
| Evocation | 3 | Iron Darts | E1H1 | AP投射。Magic Beingへ特に有効 |
| Alteration | 4 | Destruction | E3 | Armorを壊し通常兵のDamageを通す |
| Alteration | 5 | Maws of the Earth | E3・1E Gem | Damageと拘束を同時に行う |
| Enchantment | 5 | Weapons of Sharpness | E3 | 武器をAP化し重装へDamageを通す |
| Thaumaturgy | 5 | Tempering the Will | E3 | 国家兵のMR弱点を補う全体支援 |
| Evocation | 6 | Iron Blizzard | E1H1 | 多数のAP投射。高Fatigue |
| Construction | 6 | Legions of Steel | E4・1E Gem | Armor Protectionを広く強化 |
| Alteration | 7 | Marble Warriors | E3・1E Gem | ArmyへStoneskin系防御を与える |
| Alteration | 8 | Iron Warriors | E4・2E Gem | ArmyへIronskin系防御を与える |
| Conjuration | 8 | Contact Iron Angel | E5S2・25E Gem | Flyingの対Sacred Commanderを召喚 |

!!! warning "研究レベルのVersion差"
    上表はDom6.35固定Spellデータに基づきます。旧作GuideではStrength of GiantsやLegions of Steelなどの位置が異なります。研究開始前に[Spellデータ](../../data/spells/index.md)を確認してください。

---

## Route A：最初の戦争を早くする

```text
Enchantment 1
→ Conjuration 3
→ Alteration 3～4
→ 敵に合わせてEvocation 3 / Enchantment 5 / Thaumaturgy 5
```

### 得るもの

- Strength of Giants
- Summon Earthpower
- Earth Meld
- Destruction
- Iron Darts

### 向く相手

- 通常兵中心
- Giant
- High Defence
- Heavy Infantry
- Early Sacred

### Script例

```text
Summon Earthpower
→ Strength of Giants / Earth Meld / Destruction
→ Battlefield状況に合うSpell
```

全Mageへ同じScriptを入れず、

- Buff担当
- Control担当
- Armor破壊担当

へ分けます。

---

## Route B：Iron Spell中心

```text
Evocation 3
→ 基礎Earth研究
→ Evocation 6
```

### 得るもの

- Iron Darts
- Iron Blizzard
- 通常Earth Evocation

### 向く相手

- Magic Being
- 高ProtectionだがAP投射に弱い敵
- 密集Army
- 後衛へ投射を通せる戦場

### 注意

- Shield
- Range
- Precision
- Friendly Fire
- Fatigue
- Enemy Arrow protection
- Caster数

Iron Blizzardは強力でも、全ての敵に最適ではありません。

敵が盾・高HP・投射対策を用意したら、Destruction、Maws、Weapons of Sharpness、Fire Elementalなどへ切り替えます。

---

## Route C：対MR攻撃

```text
基礎Earth研究
→ Thaumaturgy 5
```

Tempering the Willは、MA Ulmの低MRを補う国家固有Spellです。

向く相手:

- Mind Blast
- Charm / Enslave
- Soul系Spell
- MR Negatesの大量投射
- Fear以外の精神・魂攻撃

### 注意

Tempering the Willへ寄ること自体にResearch Costがあります。

敵がMRを攻撃しないなら、別Schoolを先に取る方が戦争へ直結します。

また、MRを上げてもAN Shock、Poison、通常Damageは防げません。

---

## Route D：Midgame Army Buff

```text
Enchantment 5
＋ Alteration 5～7
＋ 必要に応じてConstruction 6
```

### 得るもの

- Weapons of Sharpness
- Group Stoneskin
- Maws of the Earth
- Marble Warriors
- Legions of Steel
- Resistance Warrior系Spell

### 考え方

Protectionをさらに高くするだけでなく、

- DamageをAP化する
- 敵を拘束する
- Shock / Fire等のResistanceを付ける
- MRを補う

という複数層を用意します。

### E4への到達

通常のE2 Master Smithは、

```text
E2
→ Earth BoosterでE3
→ Summon Earthpowerで戦闘中E4
```

という形で上位Battle Spellへ届きます。

Forge・Ritualで必要なPathと、戦闘中だけ得られるPathを混同しないでください。

---

## Constructionを上げる理由

Constructionは、黒鋼装備をさらに量産するためだけではありません。

- Earth Booster
- Resistance Item
- Reinvigoration
- Research Item
- Crystal Matrix / Slave Matrix
- Caster保護
- 専用Black Lord装備

を解禁します。

Forge Bonusを持つMA Ulmでは、Constructionの価値が高い一方、Battle Spellが遅れる危険もあります。

> **そのItemを作ることで、次の戦争の何が変わるか**

を答えてから研究します。

---

# Magic Access

## Native Access

国家の土台はEarth、次にFireです。

AirとAstralはMaster SmithのRandomへ依存します。

詳細は次を参照してください。

- [Recruitable Mage](../../data/recruitment/ma/ulm.md)
- [Extended Magic Access](../../data/extended-magic-access/ma/ulm.md)
- [Magic Access Route](../../data/magic-access-routes/ma/ulm.md)

## Earth

最も安定したPathです。

用途:

- Army Buff
- Control
- Armor破壊
- Siege
- Booster
- Forge
- Earth summon
- Global

## Fire

F1を基礎に、

- Self boost
- Fire Elemental
- Fire Resistance
- Fire Item
- Evocation

へ進みます。

Fire Gemを一戦で大量消費すると、Forgeと将来の召喚が止まります。

## Air Random

確保したら名前を付けて保護します。

用途:

- Shock Resistance
- Air Item
- Arrow対策
- Mobility
- 将来のAir climb

## Astral Random

用途:

- Crystal Item
- MR支援
- Communion
- Booster
- Magic Duel関連

Air / Astral Randomを一体引いただけで国家全体の戦略を固定せず、死亡・暗殺・事故への代替を考えます。

## Nature不足

MA Ulmの代表的弱点です。

Natureを得る方法:

- Pretender
- Independent Mage
- Magic Site
- Hero / Event
- Summon
- Empowerment

最初のN1を得た後、BoosterでN2へ上げ、Poison対策や召喚へ接続できるかを確認します。

## Communion / Matrix

Astral RandomやIndependent Astral Mageに加え、Crystal Matrix / Slave Matrixで非Astral MageをCommunionへ接続する方法があります。

ただし、

- Construction投資
- Item Forge turn
- Slave Fatigue
- Master死亡
- Matrix回収

が必要です。

通常のEarth Scriptで十分な戦闘へ、無理にCommunionを持ち込みません。

[Communion・Sabbath](../../magic/communions.md)も参照してください。

---

# Battle Script

以下は固定Scriptではなく、役割ごとのTemplateです。

## 基本Earth Support

```text
Summon Earthpower
→ Strength / Protection / Resistance Buff
→ Earth Meld等のControl
```

### 配置

- Infantryの後方
- 敵Flyingから離す
- Bodyguardを検討
- Retreat先を確認

## Armor Break

```text
Summon Earthpower
→ Destruction
→ Maws of the Earth / 通常攻撃支援
```

高Protection敵へ、黒鋼兵同士で殴り合うより効率的です。

## Anti-Defence / Anti-Giant

```text
Summon Earthpower
→ Earth Meld
→ Maws of the Earth
```

敵の高Damage攻撃を止めること自体が防御になります。

## Iron Darts部隊

```text
必要なSelf Buff
→ Iron Darts
→ Range内の適切なTarget
```

少数Casterなら、敵のShieldや高HPへ吸われる可能性があります。

## Iron Blizzard部隊

```text
Fatigue対策
→ Iron Blizzard
→ 予定Cast数後のFallback
```

Mageが高Fatigueで気絶する前提で、Infantryが戦線を維持できるか確認します。

## Tempering the Will

```text
Tempering the Will担当
＋ 通常Buff担当
＋ Damage / Control担当
```

全MageをMR Buffへ回すと火力とControlが不足します。

## Fire Elemental

```text
Fire Path boost
→ Summon Fire Elemental
→ Earth系MageがElementalを支援
```

Chaff処理や別Damage typeとして使います。

敵のFire Resistanceが高い場合は投資を止めます。

---

# Army構成

## 標準正面Army

- 盾兵：最初に敵を受ける
- Pikeneer：長Weapon・Cavalry対策
- 高Damage兵：重装・Giant処理
- Flail兵：Chaff・高Defence処理
- Mage：Buff、Control、Armor破壊
- Priest：Iron Spell、Morale、Dominion役
- Sapper / Mason：Fort戦
- Scout：敵増援と退路確認

## 対Sacred Army

- Guardianを敵Sacredへ当てる
- Shield lineで突撃を受ける
- MageでDefence / Armor / Resistanceを崩す
- Enemy Priest・Bless Casterを狙う
- Sacred以外の支援兵も処理する

## 対Heavy Infantry

- Destruction
- Weapons of Sharpness
- 高Damage武器
- Maws of the Earth
- Fire Elemental
- Iron Spell

を組み合わせます。

## 対Chaff / Undead

- Flail等の攻撃回数
- AoE
- Fire Elemental
- Priest
- Fatigue回復

を増やします。

敵Chaffを倒しても後続Summonが続くなら、Casterを倒す方法が必要です。

## 対Raider

主力重装Armyで追い回さず、

- Black Knight
- Black Lord
- Local Commander
- Province Defence
- Scout
- Fort網

で対応します。

---

# 最初の戦争

MA Ulmの第一戦争では、正面戦闘だけでなくFort戦まで計画します。

## 宣戦前の確認

- 目的のFort / Throne / Choke
- 敵の主力Damage type
- 敵のMR攻撃
- Poison / Shock access
- Sacred数
- Flying / Stealth Raider
- Siege力
- Reinforcement route
- Retreat route
- 必要Gem

## 勝利条件

例:

```text
敵前線Fortを取り、Mage生産を一つ止める
```

```text
Throneを確保してFort化する
```

```text
敵主力を倒し、二ProvinceのChokeまで前線を短くする
```

「敵を弱らせる」だけでは終戦条件になりません。

## Field Battle

MA Ulmは正面戦闘へ強いですが、敵はそれを知っています。

想定するCounter:

- Shock
- Poison
- MR攻撃
- Armor破壊
- Fatigue
- FlyingによるCaster assassination
- Raidで補給線を切る

Protectionだけを重ねず、敵の第一Counterへの回答を一つ持ち込みます。

## Fort戦

Armyに、

- Sapper
- Master Mason
- Siege Commander
- Supply
- Gem補給
- Relief ArmyへのScout

を含めます。

Field Battle勝利後に壁を壊せず停滞すると、敵のResearchと増援が追いつきます。

[最初の戦争](../../getting-started/first-war.md)も参照してください。

---

# Magic Item

## 第一優先：Booster

Earth Boosterは、

- E3 Forge
- 戦闘中E4
- 上位Army Spell
- Ritual

への入口です。

Air / Astral / Nature Boosterは、Rare Accessを国家技術へ変えます。

[Magic Path Booster](../../items/boosters.md)と[自動生成Booster一覧](../../data/items/boosters.md)を参照してください。

## 第二優先：Resistance

敵が示したCounterへ対応します。

- Shock
- Poison
- Fire
- Cold
- MR

Caster一人を守るItemと、Army全体へResistanceを配るSpellを分けて考えます。

[Resistance Item](../../data/items/resistance.md)も参照してください。

## 第三優先：Reinvigoration

Iron Blizzard、Earth Spell、重装Casterの継続Castを支えます。

## 第四優先：Research

Research Itemは長期的に強いですが、第一戦争に間に合わないほどConstructionへ寄り道しないようにします。

[Research Item](../../data/items/research.md)を参照してください。

## Black Lord装備

Black Lordは素のArmorが強いため、防具を総入れ替えするより、

- Magic Weapon
- AoE Damage
- MR
- Elemental Resistance
- Reinvigoration
- Mobility / Escape

の不足を補います。

専用装備は、PD Raid、対Sacred、対Thugなど目的を一つ決めます。

---

# Midgame

MA UlmのMidgameは、黒鋼兵が突然強くなるのではなく、**同じ兵士へ複数の技術層が加わる**ことで始まります。

- Strength
- AP Weapon
- Protection
- Resistance
- MR
- Control
- Armor破壊
- Mage数
- Forge economy

この段階で重要なのは、Army一個を最大強化することだけではありません。

- 複数FrontへMageを分配
- Fortごとの役割分担
- Boosterの後方・前線分離
- Gem補給網
- Raider対応

を整えます。

## 優位を国力へ変換する

戦争に勝ったら、

1. 敵Fortを取る
2. 自国Fortを追加する
3. Labを建てる
4. Master Smith生産を増やす
5. Site Searchを広げる
6. 次のCounterを研究する

まで行います。

領土だけ増えてMage生産が増えていないなら、優位の変換が不十分です。

---

# Late game

Late gameでは、黒鋼兵のProtectionだけでは足りません。

問題:

- Battlefield-wide AN Damage
- Soul・Control
- Mass Poison
- Fatigue Aura
- Global
- Teleport / Magic Phase
- 高HP Summon
- SC
- Army-wide Resistance

## 必要な準備

- Pretenderまたは召喚Mageによる外部Path
- NatureでPoison・回復
- AirでShock・移動・射撃防御
- AstralでMR・Communion・Teleport
- 高Earth Ritual / Global
- Gem income
- Magic Weapon
- 複数Damage type

## Contact Iron Angel

Dom6.35では、Conjuration 8、E5S2、25 Earth Gemの国家固有Ritualです。

Iron Angelは、

- Flying
- Reinvigoration
- Elemental Resistance
- Halt Heretic

を持つ対Sacred寄りのCommanderですが、Mageではありません。

高価な万能SCではなく、

- SacredへのPressure
- 高機動Commander
- 特定戦場の補助

として評価します。

E5S2へどう到達するかは[Magic Access Route](../../data/magic-access-routes/ma/ulm.md)で確認してください。

---

# Counterされる方法と回答

| 敵のCounter | なぜ効くか | MA Ulm側の回答 |
|---|---|---|
| AN Shock | Armorを無視する | Shock Resistance、Caster kill、分散、別Army |
| Poison / Foul Vapors | Protectionを参照しない | Nature access、Poison Resistance、短期決戦、Caster kill |
| MR Negates | 一般兵の低MRを狙う | Tempering the Will、MR Item、Drain / Dominion管理、数の分散 |
| Armor破壊 | 黒鋼兵の投資を剥がす | 先にCasterを倒す、射撃、機動、別防御層 |
| AP・AN物理 / 魔法 | 高Protectionの効率を落とす | Resistance、Shield、HP、先制Control |
| Fatigue / Chaff | 重装兵を長時間拘束する | Reinvigoration、AoE、Fire Elemental、Caster kill |
| Repel | 低Defence・短Weapon兵を止める | Pikeneer、射撃、Earth Meld、複数攻撃 |
| High Defence | 攻撃が当たらない | Earth Meld、Flail、AoE、Magic |
| Flying / Attack Rear | MageとCommanderを狙う | Bodyguard、後方Guard、配置、迎撃部隊 |
| Raid / Mobility | 重装主力が追いつけない | Black Knight、Scout、Fort網、Local Army |
| Supply攻撃 | 大Armyを停滞させる | Supply計画、分割、Fort、補給Commander |
| Gem bait | 高価なBattle Spellを空撃ちさせる | Scout、Gem量調整、Fallback Script、複数Army |

## Counterを見せられた後

MA Ulmの悪い反応は、

> もっと黒鋼兵を増やす

だけで答えることです。

良い反応は、敵がどの防御層を迂回しているかを確認することです。

```text
Protectionを迂回
→ Resistance / MR / HP / Caster対策

正面Armyを迂回
→ 機動部隊 / Fort / Scout

兵士を迂回してMageを狙う
→ 配置 / Bodyguard / Counter-flank
```

---

# よくある失敗

## 完全黒鋼兵だけを雇う

ResourceとGoldを一軍へ集中し、第二Armyと第二Fortが遅れます。

## 盾兵だけを雇う

戦線は維持できても、高Protection・高HP敵を倒せません。

## 両手武器兵を最前列へ置く

射撃とRepelでDamage役を先に失います。

## Master Smith生産を止める

現在の兵数を増やす代わりに、将来のResearch、Battle Mage、Forge turnを失います。

## Rare Randomを雑に前線へ出す

Air・Astral accessを一戦で失います。

## Forge Bonusで不要Itemを作る

安く作れることと、必要であることを混同します。

## Constructionだけを上げる

Itemは増えますが、第一戦争のBattle Spellがありません。

## Protection Buffだけを重ねる

Shock、Poison、MR攻撃への弱点は残ります。

## Siege要員を忘れる

Field Battleに勝ってもFortを取れません。

## 重装主力でRaiderを追う

前線を失い、別方向も守れません。

## Dom5の研究順を使う

Dom6.35ではSpellのSchoolとLevelが変わっています。

---

# 最初の12ターンの考え方

これは固定Build Orderではありません。

## Turn 1–3

- 敵Independentを確認
- 盾兵とDamage役を分けてRecruit
- Master Smith継続雇用を検討
- Researchの最初のBreakpointを決める
- 初戦Replayで射撃、Repel、損失位置を見る

## Turn 4–6

- 第一Armyを過剰に大きくしない
- 第二Commanderを用意
- 第二Expansion Armyを形成
- 第二Fort候補のIncome、Resource、位置を見る
- Air / Astral Random Master Smithを識別する

## Turn 7–9

- 第二Fort建設
- Lab資金を残す
- 敵Playerの位置と主力をScout
- Research Route A～Cから第一戦争案を選ぶ
- Sapper / Masonの必要性を判断

## Turn 10–12

- 第一戦争の目的を一つ決める
- MageをBuff / Control / Damageへ分ける
- GemとRetreat routeを確認
- Poison、Shock、MR攻撃の有無を確認
- Fortを取るSiege力を準備

詳細は[最初の12ターン](../../getting-started/first-12-turns.md)を参照してください。

---

# Battle Replayで見るもの

MA Ulmでは、勝った戦闘も次を確認します。

1. 盾兵が先に敵を受けたか
2. Damage役がRepelされていないか
3. Mageが予定SpellをCastしたか
4. Iron Blizzard後のFatigueはどうなったか
5. 敵DamageはProtectionを参照していたか
6. Shock / Poison / MR攻撃で誰が死んだか
7. CommanderがRear attackを受けなかったか
8. Rout後に退路を失わなかったか
9. Earth Gemを何個消費したか
10. 次の戦闘で一つだけ何を変えるか

[Battle Replayの読み方](../../getting-started/battle-replay.md)のTemplateへ記録してください。

---

# 対戦相手の類型

## Giant国家

有利な要素:

- Earth Meld
- Maws of the Earth
- 高Damage兵
- Weapons of Sharpness
- 数とFort生産

危険:

- 高Damageで黒鋼を貫く
- Trample
- Fear
- 高HPでIron Spellを耐える

## Sacred Rush

有利な要素:

- Guardian
- 盾とPike
- 国家兵の補充
- Earth Control

危険:

- Elemental Weapon
- Multiple attack
- Awe
- Magic Weapon
- 高機動

## Communion / MR攻撃国家

有利な要素:

- Tempering the Will
- Casterへの射撃・Raid
- 多数の安定兵

危険:

- Soul / Charm
- Mind Blast
- Magic DuelでAstral Randomを失う
- Battlefield-wide Control

## Poison国家

有利な要素:

- 早期正面圧力
- Casterを倒すBlack Knight / Raid
- 外部Natureを確保できた場合のWard

危険:

- Foul Vapors
- Poison Cloud
- 長期戦
- Chaffで拘束されること

## Archer / Crossbow国家

有利な要素:

- Shield
- 高Protection
- Heavy Cavalry

危険:

- AP射撃
- Friendly Fireを誘発する密集
- Commander射撃
- Storm /射撃環境の変化

## Undead / Chaff国家

有利な要素:

- Priest
- Flail
- AoE
- Fire Elemental

危険:

- Fatigue
- Supply
- Routしない前衛
- Endless summonでMageが気絶すること

---

# まとめ

MA Ulmの良いTurnは、単に黒鋼兵を一体多く雇ったTurnではありません。

> **安全なExpansionを続けながら、Fortを増やし、Master Smithを増やし、次のResearch Breakpointへ近づき、敵のProtection対策に対する第二案を作ったTurn**

です。

国家の強さは、

```text
Blacksteel
× Role分担
× Master Smith数
× Research Timing
× Forge economy
× Magic diversity
```

で決まります。

黒鋼は時間を作ります。その時間をResearchとMagic Accessへ変換できるかが、MA Ulmを単なる重装国家から強い戦略国家へ変える境目です。

---

## 関連ページ

- [国家Recruitデータ](../../data/recruitment/ma/ulm.md)
- [Magic Access Route](../../data/magic-access-routes/ma/ulm.md)
- [Research](../../magic/research.md)
- [Magic Path Boosting](../../magic/boosting.md)
- [Communion](../../magic/communions.md)
- [Magic Item](../../items/index.md)
- [Forts](../../systems/forts.md)
- [命令とBattle Script](../../basics/orders.md)
- [戦闘ルール](../../basics/combat-rules.md)
- [序盤拡張](../../getting-started/expansion.md)
- [最初の戦争](../../getting-started/first-war.md)
- [Battle Replay](../../getting-started/battle-replay.md)

## 情報源・検証

- Dominions 6.35固定Dom6 Inspectorデータ
- Dominions 6ゲーム内Nation・Unit・Spell表示
- Dominions 6 Manual / Change log
- [Dom6 Inspector](https://larzm42.github.io/dom6inspector/)
- [illwiki MA Ulm](https://illwiki.com/dom5/dom6/ulm-ma) — 戦略上の論点を参照し、Spell Level等は6.35固定データで再確認

!!! note "記事状態"
    Roster、Path、国家固有Spell、主要BreakpointはDom6.35データへ合わせています。Pretenderの具体的Point配分、Mapごとの最適Recruit比率、対国家戦の細部はGame設定と相手構成で変化するため、単一の固定Buildとしては扱いません。
