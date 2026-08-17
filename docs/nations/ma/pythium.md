---
title: MA Pythium
page_type: nation-guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-17"
nation_id: 56
era: "MA"
epithet: "Emerald Empire"
---

# MA Pythium — Emerald Empire

MA Pythiumは、**Communionを組めば自動的に高位Spellを連打できる国家ではありません。**

国家の中心は、

> **Tower Shieldを持つLegion infantry**
> ＋ **Gladiator・Retiarius・Serpent Cataphractの役割火力**
> ＋ **Theurg Acolyte・Theurg・CommunicantによるCommunion**
> ＋ **首都Arch Theurgの高位Air・Astral・Holy**
> ＋ **高いAstral incomeをResearchとBattleへ変換するFort network**

です。

Legionは敵を一気に倒す兵ではなく、Mageが準備する時間を買う兵です。Communionは低Path Mageを高位Casterへ変えますが、SlaveのFatigue、Master数、Path差、Resistance、Spell順を誤ると、敵より先に自軍Mageが崩壊します。

> **Pythiumの上達は、Communionの最大Pathを上げることではなく、「必要なSpellを、必要なRoundだけ、Slaveを生かしたまま使うこと」です。**

- [自動生成Recruitデータ](../../data/recruitment/ma/pythium.md)
- [国家別Site Search能力](../../data/site-search/ma/pythium.md)
- [Extended Magic Access](../../data/extended-magic-access/ma/pythium.md)
- [Magic Access Route](../../data/magic-access-routes/ma/pythium.md)
- [Pretender設計サンプル](../../pretender/samples.md)
- [Communion・Sabbath](../../magic/communions.md)

!!! note "このページの精度範囲"
    本文はDominions 6.35の固定データ、ゲーム内Nation・Unit・Spell・Item表示、公式Documentation、現行Inspector、現行Community資料を照合し、実戦判断へ再構成しています。CommunionのFatigue分配、Grand Communicant、国家Site、Hydra、Capital recruit、Spell AI、Battlefield condition、Patch、MODには例外があります。正確なUnit Cost・Path・Recruit条件・Spell requirementはゲーム内表示と上記自動生成データを優先してください。

!!! warning "CommunionはPath表だけでは評価できない"
    `8 Slaveで+3`のような表は到達Pathを示すだけです。Slaveが何Round生きるか、Masterが何Spell唱えるか、Slave自身のPath・Encumbrance・Resistance・HPを別に計算してください。

---

# 一言でいうと

```text
Legionで戦線を固定する
→ CommunicantとAcolyteでCommunion基盤を作る
→ TheurgがAir・Water・Astral・Holyを役割分担する
→ 必要なMasterだけ高Path化する
→ Fortを増やしMage数とResearchを伸ばす
→ Missing PathはPretender・Site Mage・外交・召喚で補う
```

国家です。

Pythiumの失敗は、大きく二つに分かれます。

```text
Communionを使わない
→ LegionのDamage不足をMageで補えない

Communionを使いすぎる
→ Slaveが過労死し、次のBattleでMage engineが消える
```

目標はその中間です。

---

# 基本データ

| 項目 | 内容 |
|---|---|
| 時代 | Middle Age |
| Nation ID | 56 |
| Epithet | Emerald Empire |
| 軍事の中心 | Legion infantry、Gladiator、Serpent Cataphract、Hydra等の特殊兵 |
| 確実なMagicの軸 | Air、Water、Astral、Holy |
| 主要Mage | Theurg Acolyte、Theurg、Arch Theurg |
| Communion基盤 | Grand Communicant、Theurg Communicant、Astral Mage量産 |
| 国家特徴 | Order寄り、Fortified City開始、豊富なAstral Gem、Communion国家 |
| 操作量 | 高い。Mage分類、Script、Slave数、Gem、Fort生産を管理 |
| 主な弱点 | 低Damage兵、Magic Duel、Communion Fatigue、Missing Path、Mage集中 |

## 通常RecruitのMagic

自動生成データで計画しやすい保証Accessは、

```text
Air 1
Water 1
Astral 2
Holy 2
```

です。

首都Arch Theurgは、

```text
Air 2
Water 1
Astral 3
Holy 3
＋ Elemental / Astral random
```

へ伸びます。

## CommunionによるBattle Path

通常TheurgをMasterとして使う場合、到達値の目安は、

| Slave数 | Bonus | TheurgのBattle Path目安 |
|---:|---:|---|
| 2 | +1 | A2 W2 S3 H3 |
| 4 | +2 | A3 W3 S4 H4 |
| 8 | +3 | A4 W4 S5 H5 |
| 16 | +4 | A5 W5 S6 H6 |

です。

これは安全性を保証しません。必要なSpellがA3なら、A5まで上げるためにSlaveを増やす必要はありません。

---

# 国家エンジン

```text
Legionで低損失Expansion
        ↓
FortとCommander Pointを増やす
        ↓
Acolyte・Theurg・Communicantを量産
        ↓
Research Breakpointへ到達
        ↓
Communionで必要Pathを一時的に作る
        ↓
Air・Water・Astral・HolyでArmy全体を強化
        ↓
Field Battleに勝つ
        ↓
Fortを取り、さらにMageを生産
```

この循環が止まりやすい場所：

1. Legionだけで敵を倒そうとし、戦闘が長引く
2. Theurgを全員MasterにしてSlaveが崩壊する
3. Capital Arch Theurgへ依存しすぎる
4. Communionを組むためのMage数はあるがResearchが散っている
5. F・E・D・N・G・Bの不足を放置し、Counterへ回答できない

---

# 強み

## 1. Tower Shieldを持つ安定した前衛

Hastatus、Principe、Triarius等は、

- Tower Shield
- Javelin
- 重装備
- Morale
- Formation

で戦線を維持します。

Legionの価値は、敵を短時間で全滅させることより、Mageへ数Roundを渡すことです。

## 2. Mageを各Fortで量産できる

Theurg AcolyteとTheurgを首都以外でもRecruitでき、Fort数が、

- Research
- Communion Slave
- Communion Master
- Site Search
- Holy support

へ直接変わります。

## 3. Astral Gem incomeとAstral utility

Astralは、

- Communion
- Antimagic
- Body Ethereal / Luck系
- MR attack
- Magic Duel
- Teleport・Ritual
- Booster

へ広く使えます。

Astral Pearlを何となく貯めず、BattleとStrategic spellへ分けます。

## 4. Air・WaterをCommunionで高位化できる

通常A1W1でも、CommunionでArmy-wide support、Control、Battlefield effectへ届きます。

## 5. HolyがCommunionと同時に伸びる

TheurgはHolyも持ち、Communion bonusでHolyが上がります。

- Bless
- Sermon
- Anti-Undead / Demon
- Holy battlefield support
- Throne

へ役割があります。

## 6. 多様な通常兵

Legion、Gladiator、Retiarius、Cataphract、Hydra等を役割で選べます。

一種類を量産する国家ではなく、Mage planへ必要な時間とTargetを作るCombined Arms国家です。

---

# 弱み

## 1. 通常兵のDamage不足

Tower ShieldとArmorで耐えても、高Protection、Regeneration、Giantを倒すDamageが足りない場合があります。

- Gladiator
- Cataphract Charge
- Mage Damage
- Strength / Quickness等のBuff
- MR attack

を追加します。

## 2. Communion崩壊

Masterが高PathSpellを長く唱えるほど、SlaveへFatigueが流れます。

Slaveが、

- Fatigue 100超過
- HP Damage
- Elemental Damage
- Spell side effect

で死亡すると、Communion全体が連鎖的に崩れます。

## 3. Magic Duel

Astral Mageを多く使うため、敵Astral MageのMagic Duelを警戒します。

高S Master、Arch Theurg、重要Booster holderを一か所へ集めないでください。

## 4. Missing Path

通常計画ではFire、Earth、Death、Nature、Glamour、Bloodが欠けます。

Communionは、Mageが持っていないPathを0から作れません。

```text
E0のMage
＋ Communion bonus
≠ E1
```

です。

## 5. Mage集中へのCounter

- Archer
- Flying / Attack Rear
- Assassin
- Remote attack
- Battlefield-wide damage
- Silence / Anti-magic

により、国家Engineをまとめて失うRiskがあります。

## 6. 操作量

Mageの数が増えるほど、

- Master / Slave分類
- Script保存
- Gem配布
- Communion規模
- BattleごとのResistance

が増えます。

---

# 兵士

## Slinger

安価な射撃とSiege補助です。

重装敵へ主Damageにはなりにくいですが、

- Chaff処理
- Archer exchange
- Fort・PD補助
- Siege人数

に使えます。

## Velite

軽装のJavelin＋Tower Shield兵です。

- Expansion補助
- 前方Screen
- 安価な投射

用途があります。

重装Legionと同じ耐久を期待しないでください。

## Alae Legionnaire

Spear・Javelin・Tower Shieldを持つ標準Lineです。

## Hastatus

Short Sword・Javelin・Tower Shieldを持ち、接敵後の通常近接を担います。

## Principe

Hastatusより技能とMoraleが高い中核前衛です。

ExpansionとFirst warの基準兵にしやすい一方、高Damage不足はMageで補います。

## Triarius

Long Spear、重装、Formation Fighterを持つ後列・密集Lineです。

- 長武器
- Repel
- Formation
- 重装

を活かし、前列を支えます。

重いEncumbranceによるFatigueに注意します。

## Emerald Guard

高技能・高MoraleのElite guardです。

Commander保護、重要戦線、Storm等へ使います。通常Lineへ混ぜて消耗させる価値を確認します。

## Standard

Army Moraleを支える旗兵です。

一体のDamageではなく、Squad全体の継戦へ価値があります。

## Serpent Cataphract

重装騎兵とArmored Serpentの複合Unitです。

- Charge
- 機動
- Poisonous Bite
- Flank

を持ちます。

ただし高価で、MountとRiderのHP・Protection・攻撃が別です。[Unit装備・Mountの読み方](../../data/unit-loadouts.md)も参照してください。

## Retiarius

NetとTridentを使う拘束・対大型補助です。

Netが成功すれば、高Defence・大型Targetの動きを止め、LegionとMageへ時間を作ります。

## Gladiator

二回攻撃のFlailを持つ高Moraleの使い切り火力です。

- Shield兵
- 低～中Protection
- Expansionの難敵
- First warのBurst

へ使えます。

高価な長期戦力ではなく、交換前提のDamageとして評価します。

## Theurg Communicant

Sacredで、Communion Slaveとして国家Engineを支える特殊Unitです。

戦闘力ではなく、

- Slave数
- Recruit limit
- HP
- Resistance
- Slave死亡Risk

で評価します。

## Hydra

首都・国家Siteの特殊戦力として、

- 多頭攻撃
- Regeneration
- Poison
- Area denial

を提供します。

しかしPoison Cloudや大型Unit、Command、Supply、Friendly Fireを管理します。自軍LegionとMageがPoisonへ耐えられるか確認してください。

---

# Commander・Mage

## Centurion / Legatus Legionis

通常Leadershipを持つArmy Commanderです。

MageをLeadershipへ拘束せず、Legionを管理します。

## Emerald Lord / Serpent Lord

Elite・Cavalryを率いる高価なCommanderです。

前線Commander、Thug、Bodyguard中心の編成へ使いますが、通常兵のCommandだけなら安価なCommanderと比較します。

## Battle Deacon

H1 Priestで、

- Bless
- Sermon
- Preach
- Undead / Demon対策

を担います。

## Theurg Acolyte

S1 H1の安価なSacred Mageです。

主な役割：

- Research
- Communion Slave
- Communion補助
- Astral utility
- Site Search
- Holy support

### AcolyteをSlaveだけにしない

戦争がないTurnはResearcherです。必要なBattle数だけ前線へ出します。

## Theurg

A1 W1 S2 H2の国家中核Mageです。

- Master
- Slave
- Air / Water support
- Astral defence・attack
- Holy
- Site Search

を一人で持ちます。

役割が多いため、全員をMasterにするとResearchとSlave数が不足します。

## Arch Theurg

首都の高位Mageです。

- A2 W1 S3 H3
- Elemental / Astral random
- 高位Communion Master
- Global・Ritual
- Throne / Holy

へ使います。

Capital-onlyのため、通常Theurgと同じ消耗品として扱わないでください。

## Assassin

敵Mage・Priest・Commanderへ圧力をかけます。

Pythium自身がMage集中国家なので、相手のCommunion・Battlefield casterを崩す価値を理解しやすいUnitです。

---

# Communionの設計

## Communionの目的を一文にする

悪い目的：

> 高Pathになるため

良い目的：

> A3でArmy-wide defenceを一回使い、その後Master二人が低Fatigue supportへ移る

```text
必要Spell：
必要Path：
Master数：
Slave数：
Masterが唱える総Round：
Slave保護：
終了後の行動：
```

を書きます。

## 小Communion

2～4 Slaveで、

- Path +1～2
- 少数Master
- 短いScript

を使います。

First warでは、小Communionの方が安全で再現しやすい場合があります。

## 中Communion

4～8 Slaveで、Army-wide Buffや中～高位Spellへ届きます。

Masterを増やしすぎるとSlave負担が急増します。

## 大Communion

16以上のSlaveは非常に高Pathへ届きますが、

- Mage数
- Script管理
- AoE被害
- Magic Duel
- Slave死亡連鎖
- Opportunity cost

が大きくなります。

必要Spellが明確でない大Communionは作りません。

## MasterとSlaveのPath差

Masterが使うPathをSlaveが持たない場合、Slave負担が重くなることがあります。

PythiumのTheurgはA/W/S/Hを共有しやすいことが強みです。それでもArch Theurgのrandom PathやItemで新PathをMasterへ加えた場合、Slave安全性を再計算します。

## Slave保護

- Elemental Resistance
- Antimagic / MR
- HP
- Regeneration / Relief
- Mage placement
- Bodyguard
- 敵AoE対策

を用意します。

## Master数を制限する

```text
Slave 8
Master 2
```

と、

```text
Slave 8
Master 8
```

は同じCommunionではありません。

## Spell順

Masterが最初にSlave保護を展開できるなら安全性が上がります。しかし、Buff前に敵が接敵するなら配置を後ろへ下げます。

---

# Magic Access

## Air

Communionで高位化し、

- Defence / Mist
- Arrow対策
- Storm
- Lightning / Control
- Battlefield-wide support

へ入ります。

## Water

- Quickness
- Defence
- Cold
- Elemental
- Fatigue support

へ使います。

## Astral

国家の基盤です。

- Communion
- Antimagic
- Luck / Ethereal
- MR attack
- Magic Duel
- Teleport / Strategic spell

を扱います。

## Holy

Priest-Mageとして、Sacred support、Undead対策、Throneへ使います。

## Booster

保証経路では、

- Water BraceletでW2
- Astral boosterでS4

へ進みやすいです。

Boosterを持つMageはMagic Duel・Assassinationの重要Targetになります。

## Missing Path

```text
Fire
Earth
Death
Nature
Glamour
Blood
```

が通常保証Accessにありません。

Communionでは0から生まれないため、

- Pretender
- Independent Mage
- Magic Site Mage
- Hero
- Summon
- Empowerment
- 交易・外交

で補います。

---

# Pretender方針

## 1. Imprisoned Scales

LegionとMageをFortごとに増やす設計です。

PythiumはFort数がResearchとCommunion規模へ直結するため、Scalesの回収先が明確です。

向く条件：

- LegionでExpansionできる
- Missing Pathを急がない
- First warをA/W/S/Hで戦える

## 2. Diversity Rainbow

F・E・D・N・G・Bを補い、

- Booster
- Resistance
- Summon Mage
- Crosspath Item
- Global

へ入ります。

最初に必要な二Pathを優先し、全Pathを薄く取るだけにしません。

## 3. Dormant Midgame Caster

First war前後に、国家にないPathまたは高位Air / Astralを追加します。

PretenderのSpellとCommunionの役割が重複しないようにします。

## 4. Light Bless

Theurg、Acolyte、Communicant、Battle Vestal等のSacredへ、

- Reinvigoration
- MR
- Elemental Resistance
- HP / Defence

を与えます。

兵士Sacredの数より、Sacred Mageへ毎Battle働く価値を見ます。

## 5. Awake Expander

Legion Expansionが遅いMapや危険な周辺を補います。

Awake Pretenderが取った土地を第二Fortへ変換できるかをTestします。

---

# Scales

## Order

国家特性と安定Incomeを活かし、MageとFortを増やします。

## Productivity

Legion、Cataphract、Emerald GuardのResourceを支えます。

## Growth

長期Income、Supply、Mage老齢、Hydra・大軍運用へ価値があります。

## Magic

Research RaceとBattle Mage Fatigueへ有効です。

## Drain

Mage量産国家ではResearch低下が大きいため、Point源として安易に選びません。

## Luck

高価なMage・Capital依存への悪Event Riskと比較します。

---

# 序盤拡張

## 標準Army

```text
Tower Shield Legion
＋ Damage補助（Gladiator / Cataphract / Retiarius）
＋ Commander
＋ 必要ならPriest
```

です。

## Legionの役割

Legionだけで敵を瞬殺する必要はありません。

- Javelinで接敵前に削る
- Shieldで射撃を受ける
- Formationを維持する
- Routしない

ことが重要です。

## Gladiator Expansion

高いBurstを使い、危険なProvinceを低Turnで処理します。

消耗前提なので、貴重な長期兵と同じ基準で損失を見ません。

## Cataphract

Cavalry・高Damageへの圧力とFlankに使えます。

高価なので、低価値Indieへ毎回失わないようにします。

##危険なIndependent

- Crossbow / 高Damage射撃
- Barbarian
- Cavalry
- Elephant
-高Protection
- Poison

に対し、Legionの耐久とDamage補助の両方を見ます。

## ExpansionからMage Economyへ

兵士を増やし続けず、十分なExpansion Armyができたら第二FortとMageへGoldを移します。

---

# Economy・Fort

## Fort数が国家戦力

Pythiumでは、

```text
Fort
→ Commander Point
→ Acolyte / Theurg
→ Research
→ Communion
→ Battle spell
```

へ変換されます。

## Capital

Arch Theurg、Hydra、特殊兵、Communicant等の供給を管理します。

首都で通常Theurgだけを作り続けるより、首都限定価値を優先する場合があります。

## Mage Fort

Resourcesが低くても、Acolyte・Theurgを毎Turn雇えるなら高価値です。

## Troop Fort

High-resource地域でLegion・Cataphractを生産します。

##前線Fort

- Lab
- Gem補給
- Retreat
- Communion集合
- Siege defence

を作ります。

Mageを一Fortへ集めすぎず、Remote attack・Raidへ分散します。

---

# Research

Pythiumの研究は、

```text
どのCommunion規模で
どのSpellを
何Round使うか
```

から逆算します。

## 第一Breakpoint：低位Astral・Air・Water support

Communionなし、または小Communionで使える、

- Ethereal / Luck
- Defence
- Water utility
- Astral defence

を揃えます。

## 第二Breakpoint：Army-wide Buff

A3～4、W3～4、S3～5程度へCommunionで届き、Legion全体を変えるSpellを選びます。

## 第三Breakpoint：Counter

- Archer / Missile
- High Protection
- Giant
- Undead
- MR
- Elemental Resistance

へ第二の戦術を用意します。

## Thaumaturgy

Astral Control、MR attack、Communion関連、Telestic等へつながります。

## Alteration / Enchantment

Army Buff、Defence、Resistance、Quickness、Antimagicへ価値があります。

## Conjuration

Elemental、Summon、Magic diversityへ進みます。

## Construction

Astral / Water booster、Resistance Item、Matrix、Research Itemを作ります。

Earthがないため、Matrix系のForge requirementを誰が満たすか確認します。

---

# Army構成

## Legion Line

Hastatus・Principe・Triarius等で戦線を固定します。

## Burst Damage

Gladiator、Cataphract、Retiarius、Hydra、Mageを使います。

## Communion Core

- Slave
- Master
- Slave保護Master
- Damage Master
- Emergency Master

へ分けます。

## Priest / Standard

MoraleとHoly supportを維持します。

## Reserve

Mage全員を一Battleへ出さず、第二ArmyとCapital defenceを残します。

---

# Script例の考え方

## 小Communion

```text
Slave 4：Communion Slave → Hold / Cast Spells
Master A：Communion Master → Slave保護 → Army Buff → Cast Spells
Master B：Communion Master → Army Buff → Control / Damage
```

## 非Communion support

すべてのTheurgをCommunionへ入れる必要はありません。

```text
Theurg C：低位Resistance → Cast Spells
Theurg D：Astral defence → Cast Spells
```

と分けます。

## Scriptが壊れる条件

- Master数過多
- Slave Path不足
- Slave Resistance不足
- Gem不足
- Buff前に接敵
- Magic Duel
- MageへFlank
- EnemyがSpell targetを持たない
- Communion Master死亡

Replayで、最初にFatigue 100へ達したSlaveと、その直前にMasterが唱えたSpellを確認します。

---

# Magic Duel対策

PythiumはAstral Mageが多いため、Magic Duelを使う側にも使われる側にもなります。

## 高S Master保護

- 低S囮
- Mage分散
- Concealment
- Battlefield position
- Enemy Astral MageへのAssassin

を使います。

## 自分が使う場合

敵の高価なAstral Mageと、自軍の交換してよい低S Mageを比較します。

Magic Duelを全AcolyteへScriptし、必要なCommunion基盤まで失わないでください。

---

# Siege・Storm

## Siege

Legionは兵数とStrengthで壁を削りますが、MageをSiege作業へ参加させるか、Research / Preachへ使うかを決めます。

## Storm

狭いGateでLegionが詰まりやすいため、

- AoE
- Quickness
- Morale
- Fatigue
- Hydra Poison
- Mage placement

を調整します。

## Defence

Fortified CityとMage密度を活かし、Relief Armyが来るまでTurnを買います。

CommunionをFort内へ全投入すると、Storm敗北時に国家Researchを失います。

---

# Counterと対応

## High Protection

通常LegionのDamage不足を、

- Gladiator / Cataphract
- Strength / Quickness
- Elemental / MR attack
- Retiarius拘束

で補います。

## Archer / Crossbow

Tower Shield、Arrow protection、Storm、Air supportを使います。

## Lightning / Elemental AoE

SlaveとMageへResistanceを配ります。Legionだけ耐えてMageが死ぬ状態を避けます。

## Magic Duel

高S Master分散、Assassin、低S交換、Astral defenceを使います。

## Anti-Communion

- Slave狙い
- Fatigue
- Battlefield-wide damage
- Silence / Drain
- Magic Duel

へ対し、小Communion、分散、非Communion Mageを残します。

## Undead・Demon

Holy accessを活かしますが、Priestだけで全てを解決せず、通常DamageとMage supportを組み合わせます。

## Poison

Hydraを使う場合も敵Poisonの場合も、Legion・Slave・MageへResistanceを確認します。

## Giant

Retiarius、Cataphract、MR attack、Quickness、Controlを使い、低Damage Legionだけで殴り続けないようにします。

---

# Multiplayer

## 脅威認識

Pythiumは、

- Communion timing attack
- Astral control
- Army-wide Air / Water buff
- Magic Duel
- Mage scaling

を警戒されます。

## 情報管理

隠したいもの：

- Communion規模
- Arch Theurg random
- Missing Pathを補うPretender
- Research Breakpoint
- Astral Pearl在庫
- Matrix / Booster

## 外交

Mage scaling国家なので、Early rushを受けるとFort数が伸びません。

Border合意とScoutで、First warのResearch完成までTurnを買います。

## 戦争目的

敵Field Armyを倒すだけでなく、Fortを取り、相手Mage生産を止めます。

Pythium自身もFortを失う損害が大きいため、前進と後方防衛を分けます。

---

# よくある失敗

## Communion bonusだけを見る

Slave FatigueとMaster数を見ていません。

## Masterを増やしすぎる

高Pathになっても数RoundでSlaveが死にます。

## LegionだけでDamageを出そうとする

戦闘が長引き、敵MageとFatigueに負けます。

## Acolyteを全員Slaveにする

ResearchとAstral utilityが止まります。

## Arch Theurgを通常Mageとして失う

首都高位AccessとRandom Pathを失います。

## Missing PathをCommunionで作れると思う

Path 0は0のままです。

## Magic Duelを忘れる

高S MasterとBooster holderを失います。

## Mageを一Squareへ密集

AoE、Flying、Archerで国家Engineがまとめて崩れます。

## 大Communionを毎Battle使う

小BattleでMage turnとGemを浪費します。

---

# Turnごとの確認

```text
1. FortごとのAcolyte / Theurg生産
2. Capital限定Recruit
3. Master / Slave分類
4. Research Breakpoint
5. Astral PearlとGem配布
6. Slave Resistance・HP・Fatigue
7. Magic Duel threat
8. Missing Pathの取得計画
9. Legion Damage source
10. End Turn前のMage分散
```

---

# Test Game Checklist

## Expansion

- Legion損失
- Gladiator消費
- Cataphract供給
- 第二Army完成Turn
- 第二Fort開始Turn

## Research

- 小Communion用Breakpoint
- Army-wide Buff
- Astral defence
- Missile対策
- High Protection対策

## Communion

- Slave数
- Master数
- 最初のSlave Fatigue 100 Round
- Slave死亡数
- Master一人あたりのSpell数
- Gem消費

## First War

- Legionが何Round持ったか
- Buff完成前に接敵したか
- Enemy Magic Duel
- Missing Path Counter
- Siege後のMage残存数

---

## 関連ページ

- [国家選択ガイド](../choose-a-nation.md)
- [Pretender設計サンプル](../../pretender/samples.md)
- [Communion・Sabbath](../../magic/communions.md)
- [Astral](../../magic/paths/astral.md)
- [Air](../../magic/paths/air.md)
- [Water](../../magic/paths/water.md)
- [戦闘ルール](../../basics/combat-rules.md)
- [命令とBattle Script](../../basics/orders.md)
- [Researchと研究ルート](../../magic/research.md)
- [Gem](../../magic/gems.md)
- [Magic Access到達経路](../../magic/magic-access-routes.md)
- [Fort・Siege・Storm](../../systems/forts.md)
- [初心者Q&A：最初の戦争・外交・Raid・迎撃](../../getting-started/war-faq.md)

## 主な参照先

- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [Illwiki — MA Pythium](https://illwiki.com/dom5/ma_pythium)（現行挙動の照合用。数値はゲーム内表示と6.35固定データを優先）
