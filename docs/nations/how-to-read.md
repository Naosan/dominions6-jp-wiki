---
title: "国家ページの読み方"
status: guide
verified_version: "6.35"
last_verified: "2026-08-14"
---

# 国家ページの読み方

国家攻略ページを読むときは、個々の強いUnitより、**何をどこで毎ターン生産できるか**を先に見ます。

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

Gold cost、Resource cost、Path、Research Levelなど、Patchで確認可能な事実。

### 攻略評価

「この兵は前衛向き」「このBreakpointで攻める」といった状況依存の判断。

数値が正しくても評価はMapや相手で変わります。逆に、良い戦術評価でもPatchで数値が変われば再検証が必要です。
