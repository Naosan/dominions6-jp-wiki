---
title: "国家ページの読み方"
status: guide
verified_version: "6.35"
last_verified: "2026-08-14"
---

# 国家ページの読み方

国家攻略ページを読むときは、個々の強いUnitより、**何をどこで毎ターン生産できるか**を先に見ます。

## 自動生成データと攻略本文を使い分ける

このWikiでは、国家情報を二層に分けます。

### Recruitデータ

[国家Recruitデータ](../data/recruitment/index.md)には、Dom6 Inspectorの固定スナップショットから次を自動生成します。

- Fort / Capital / Fort不要 / Coastで雇えるUnitとCommander
- Unit ID
- HP、Protection、MR、Morale、Strength、Attack、Defence
- 固定Magic Path
- Random Path pool
- Sacred、Flying、Stealthyなどの主要属性

### 国家攻略

国家攻略記事では、自動生成データを解釈して次を扱います。

- どの兵を何の役割で雇うか
- MageをどのFortで量産するか
- Pretender、Scales、Bless
- Expansion
- Research Breakpoint
- Army構成、Battle Script
- Counter、戦争Timing、外交

数値索引は「事実確認」、攻略記事は「意思決定」と考えると読みやすくなります。

## 1. Recruit-anywhereとCapital-onlyを分ける

### Recruit-anywhere

必要施設を建てた各Provinceで雇えるUnitです。Fortを増やすほど生産量が伸びるため、国家の長期的な量産力になります。

### Capital-only

首都でしか雇えません。強力でも、毎Turnの生産量に上限があります。

Cap-only Sacredを主力にする場合は、次を確認します。

- Recruitment Point / Resource制約
- 首都包囲時の代替戦力
- Bless投資を中盤以降も回収できるか
- 戦死した兵を補充できる速度

!!! note "自動分類について"
    Recruit索引のCapital-only分類は、抽出データの `capitalhome` 属性に基づきます。イベント、特殊Site、地形、季節、Planeなどの条件は個別確認が必要です。

## 2. Mageは固定PathとRandom Pathを分ける

国家のMagic Accessは、最高値だけでなく**確率と量産場所**で評価します。

| 種類 | 攻略上の意味 |
|---|---|
| 固定Path | 毎回確実に利用できる国家の基礎 |
| 100% Random | 何らかのPathは付くが、個体別の役割分担が必要 |
| 10–20% Random | 出れば重要だが、戦略の前提にしすぎない |
| Cap-only Mage | 質は高くても量に上限 |
| Recruit-anywhere Mage | Fort数がResearchとBattle Magicへ直結 |
| Slow-to-recruit | Commander Point以外の生産制約を持つ |

全国家の固定Path最大値とRandom poolは、[Mage access早見表](../data/mage-access.md)で比較できます。ただし、表の最大値が同じ一体のMageに同時搭載されているとは限りません。必ず国家別Commander表も確認してください。

### Random表記

`1×20% +1 [F/A/W/E]` は、20%の確率でFire / Air / Water / Earthのいずれか一つを1レベル得るRandom pickを1回持つ、という読み方です。

### Path到達点を段階で見る

```text
素のPath
→ Booster Item
→ 戦闘中の自己Boost
→ Gem boost
→ Communion / Sabbath
→ Empowerment
→ Summon Mage
```

「E2しかない」ではなく、**E2を何人雇え、Earth BootsやSummon Earthpower後に何へ届くか**を見ます。

## 3. 一般兵は役割で見る

一般兵を一つの総合点で評価せず、次へ分けます。

- **Line holder** — 盾・Protection・Defence・Moraleで前線を維持
- **Damage dealer** — 高Damage、複数攻撃、AP/AN、特殊武器
- **Repel unit** — 長武器とAttack/Moraleで接近を妨害
- **Chaff** — 安価に攻撃を吸収しMageの時間を作る
- **Archer / Crossbow** — 接敵前の損害、後衛圧力
- **Flanker / Raider** — 高Map Move、Flying、Stealth、Cavalry
- **Siege / Patrol** — 戦闘外のProvince制圧
- **Sacred** — BlessとHoly leadership込みで評価

自動生成表は基礎能力値を示しますが、Weapon、Armor、Mount、Recruit cost、特殊攻撃の最終評価はゲーム内Popupと国家攻略で確認します。

## 4. 国家固有の制約を見る

強みより先に、国家が何へ制約されるかを確認すると運用を理解しやすくなります。

- Gold
- Resources
- Recruitment Points
- Commander Points
- Capital-only
- Population
- Supply
- Dominion
- Temperature
- Terrain
- Blood Slave物流
- Undead / Demon leadership
- Underwater access

たとえば強力な重歩兵がいても、Resourcesが不足すれば数を作れません。優秀なMageがいてもSlow-to-recruitならResearch量は伸びにくくなります。

## 5. Expansionと対人戦を分ける

Independent Provinceに強い構成が、そのまま対人戦でも強いとは限りません。

### Expansionで重視

- 損失率
- 二軍・三軍へ分割できる価格
- Archer、Cavalry、BarbarianなどIndie別の安全性
- Awake Pretenderへの依存度

### 対人戦で重視

- BuffとBattle Script
- 敵のResistance
- Mage密度
- RaidとMap Move
- Research Timing
- Counterを見せた後の第二案

## 6. 国家ページの標準構造

このWikiでは国家ページを原則として次の順で書きます。

1. 一言でいうと
2. 強み・弱み
3. 兵士・Sacred
4. Commander / Mage
5. Magic Path
6. Pretender方針
7. Expansion
8. Research
9. Spell・Item
10. Army構成とScript
11. Counter
12. Multiplayer
13. 検証情報

## 7. 数値と評価を分離する

### 仕様

Unit ID、能力値、Path、Research Levelなど、Patchで確認可能な事実。

### 攻略評価

「この兵は前衛向き」「このBreakpointで攻める」といった状況依存の判断。

数値が正しくても評価はMapや相手で変わります。逆に、良い戦術評価でもPatchで数値が変われば再検証が必要です。

## 8. 自動生成表で意図的に省いているもの

現在のRecruit索引では、誤解を避けるため次を原則表示しません。

- 自動計算を伴う最終Gold cost
- Mount込みCostとMount側の全能力
- Weapon / Armorの完全な内訳
- Shape change後の全形態
- Hero、Event、Freespawn、国家固有召喚
- Booster後・Communion後の到達Path

これらは次段階のデータ索引または国家攻略で追加します。
