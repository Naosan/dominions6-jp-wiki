---
title: Site Search運用Playbook
status: expanding
verified_version: "6.35"
last_verified: "2026-08-15"
---

# Site Search運用Playbook

このページは、[Site Search完全ガイド](site-search.md)の仕組みを、実際のTurn運用へ落とし込むための手順書です。

Site Searchでは、理論的な完全探索よりも、

- 誰をSearchへ回すか
- どのProvinceをどの順で回るか
- いつResearchへ戻すか
- どのPathだけRemoteで仕上げるか
- 戦争が始まったら何を中止するか

が重要です。

---

## 参照ページ

- [Site Search完全ガイド](site-search.md)
- [Search Level分布](../data/sites/search-levels.md)
- [Remote Site Search Spell](../data/spells/site-search.md)
- [Magic Site総合索引](../data/sites/index.md)
- [Terrain・Location](../data/sites/terrain.md)
- [国家別Mage access](../data/mage-access.md)

---

# 一つの原則

Site Searchの基本単位はProvinceではなく、**Search coverage**です。

悪い記録：

```text
Province 18：Search済み
```

良い記録：

```text
Province 18：F2 A1 W0 E2 S1 D2 N0 G0 B0 H1
```

前者では、誰で再探索すべきか分かりません。

後者なら、

```text
W2・N2・G2が未確認
```

と判断できます。

---

# Searcherの三役

## Broad Rover

複数Pathを持ち、領土を歩きながら広くManual SearchするMageです。

理想：

- 三Path以上
- 主要PathがL1–2
- Recruit-anywhere
- 安価
- 高Map Move
- SurvivalまたはStealth
- Research値が極端に高くない

役割：

- 新領土の初回Search
- Search coverageの土台作り
- Fort候補の事前調査

## Deep Specialist

一PathをL3以上で持ち、取りこぼしを埋めるMageです。

役割：

- 国家の主力Gem Pathを深くSearch
- 高Level Site候補の確認
- 水中・Cave・Holyなど特殊領域の補完

原則として、全Provinceを回らせるのではなく、候補地と重要地へ限定します。

## Remote Operator

LabからRemote SearchをCastするMageです。

理想：

- 要求Pathを自然に満たす
- Research値が低め、または一時的に余る
- Ritual casterとして安全
- Gem stockへアクセスできる
- 他の重要Ritualと競合しない

役割：

- 前線・遠隔地・島・海のSearch
- Manual Searchの不足Path補完
- L3–4の取りこぼし確定
- 新規征服地の高速確認

---

# Turn 1–5：Search計画を作る

序盤はまだ領土が少なく、Mage一人のResearch価値が高い時期です。

## やること

1. 国家のRecruitable Mageを一覧化する
2. 各Mageの固定PathとRandom Pathを確認する
3. 首都周辺のTerrainを確認する
4. 首都Start Siteから得るGemを確認する
5. 不足Gem Pathを一つ決める
6. 最初のBroad Rover候補を決める

確認先：

- [国家Recruitデータ](../data/recruitment/index.md)
- [Mage access早見表](../data/mage-access.md)
- [国家Start Site](../data/sites/national.md)

## まだしないこと

- 首都限定最高級Mageを即座に長距離Searchへ出す
- 全PathをL3以上で揃えるまで待つ
- Remote Search解禁前提でResearchを歪める
- Searcher用だけにPretender Pathを決める

---

# Turn 6–12：Expansionの後ろを追う

Expansion Armyが新Provinceを取った後、その後方をSearcherが追います。

## 基本Route

```text
首都
  ↓
Province AをSearch
  ↓
Province Bへ移動
  ↓
Province BをSearch
  ↓
Province Cへ移動
```

SearcherはSearchと移動を同じTurnに行えないため、一本道よりも、

```text
A — B — C — D
```

のような連続Routeを作ります。

## Route選択基準

優先：

- 安全な後方
- Forest / Mountain / Waste / Swamp / Cave / Sea
- Fort候補
- 多方向へ接続する中心Province
- Expansion Armyが既に通過した地域

後回し：

- 敵国境
- 孤立Province
- 次Turnに失いそうなProvince
- Searcherが往復を強いられる袋小路

## Searcherを出す目安

序盤Researchが非常に重要な国家では、Expansion直後に一人だけ出し、二人目はResearchへ残します。

Mageが安く量産できる国家では、Broad Roverを複数Routeへ分けます。

---

# Turn 10–20：coverageを広げる

この時期は、

- Fort建設
- First war準備
- Research Breakpoint
- Gem income開始

が重なります。

Site Searchへ無制限にMageを出すと戦争準備が壊れるため、役割を分けます。

## Search budgetを決める

例：

```text
Mage turn配分
60%：Research
15%：Manual Search
10%：Forge / Ritual
10%：Army support
 5%：Preach / Fort / utility
```

固定比率ではありませんが、Searchへ何人出しているかを明示します。

## Broad Roverの終了条件

次のいずれかでResearchへ戻します。

- 安全な後方Provinceを一巡した
- First warまで3–5Turn
- 必要Researchが遅れている
- 主要Gem incomeが立ち上がった
- Remote Searchが解禁された
- SearcherがBattle Mageとして必要になった

Searcherは永久職ではありません。

---

# First War前：探索を軍事へ変換する

Site Searchの目的はGemを貯めることではなく、戦争能力へ変換することです。

## 戦争前に確認する

```text
現在のGem income：F / A / W / E / S / D / N / G
主力Battle Spell一戦の消費：
Booster作成Cost：
三連戦に必要な在庫：
未探索の主力Path：
SearcherをBattle Mageへ戻すTurn：
Frontline Siteの守備：
```

## First War前にRemote Searchする基準

Castする価値が高い：

- 主力Spell用Gemが不足
- Manual Searcherが戦場へ戻る
- 安全な後方Provinceが多数未完成
- 一PathだけSearch coverageが空白
- 重要なFort候補を確定したい

後回しにする：

- Gem在庫が戦争準備ぎりぎり
- Ritual casterが主力Battle Mage
- Research Breakpointを一Turn遅らせる
- 対象Provinceを失う可能性が高い

---

# Mid game：ManualからRemoteへ移行する

領土が広がると、Manual Searchの移動Costが増えます。

この段階では、

```text
Broad Rover
→ 新規領土だけを浅くSearch

Remote Operator
→ 既存領土の不足Pathを深くSearch
```

へ役割を変えます。

## Remote Search queue

優先順位を付けます。

### 優先度1：Gem bottleneck Path

例：

```text
Earth Boosterを作りたいがE incomeが1
Air Battle Mageが多いがA incomeが0
Astral Communion国家なのにS incomeが不足
```

### 優先度2：重要Province

- Throne
- Fort候補
- Cave / Sea / Plane接続
- 特殊Recruit Province
- 大規模後方Clusterの中心

### 優先度3：Manual coverageがほぼ完成

例：

```text
F2 A2 W1 E2 S1 D2 N2 G0
```

なら、GlamourだけRemoteで埋める方が、別の多Path Mageを一周させるより安い場合があります。

### 優先度4：完全Searchの価値が高い場所

Acashic Knowledgeの候補です。

- 多Pathが完全未探索
- 地理的に遠い
- 高価値Terrain
- 重要な恒久拠点
- Manual Searcherを送るのが危険

---

# Late game：回収Turnより即時効果を見る

終盤は、1 Gem/TurnのSiteを見つけても回収期間が短くなります。

Search価値は、

```text
長期Gem income
```

から、

```text
即座に使える特殊Recruit・Ritual bonus・Throne効果・戦略情報
```

へ移ります。

## 終盤にSearchする場所

- 新しく奪った敵首都周辺
- Throne Province
- Unique Site候補
- EnemyがFort化していたProvince
- Lab / Temple /高PDがあるProvince
- 異Planeの重要接続点
- Final warで使うGem Pathの不足地

## 終盤にSearchしない場所

- 守れない後方
- Game終了前に回収できない低価値Province
- SearcherをFinal battleから外す必要がある場所
- 敵へすぐ奪還される場所

---

# Search coverage ledger

Spreadsheetを使わなくても、Turn fileのメモで次を管理できます。

| Province | Terrain | F | A | W | E | S | D | N | G | B | H | Remote | Next action |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 12 | Forest | 2 | 1 | 0 | 2 | 0 | 1 | 2 | 0 | 0 | 1 | — | W/G/Sを補完 |
| 18 | Mountain | 2 | 2 | 1 | 3 | 1 | 2 | 1 | 1 | 0 | 0 | E | Blood/Holy後回し |
| 25 | Sea | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | W | Tiamat候補 |

数字はそのProvinceで確認済みの最大Search Levelです。

Remote SearchでPath全体を確認した場合は、数字の代わりに、

```text
ALL
```

またはSpell名を記録します。

---

# Search Routeの作り方

## Step 1：未探索ProvinceをCluster化

Map上で隣接する未探索Provinceを、3–6個程度のClusterにまとめます。

## Step 2：入口と出口を決める

Searcherが同じ道を戻らなくてよいRouteを作ります。

悪い例：

```text
A → B → A → C → A → D
```

良い例：

```text
A → B → C → D → Fort
```

## Step 3：FortまたはLabで終える

Route終了後に、

- Researchへ戻る
- Gemを渡す
- Forgeする
- Battle Armyへ合流する

ことができます。

## Step 4：Frontlineを最後にする

Searcherを国境へ向かわせるなら、Routeの最後にします。

Frontline Search後は、

- Fortへ退避
- Armyへ合流
- Teleport
- Remote operatorへ転換

します。

---

# 複数Searcherの分業

## Pathの重複を減らす

例：

```text
Mage A：F2 A1 E1
Mage B：W2 S1 N2
Mage C：D2 G2
```

三人を同じRouteへ順番に送ると、全Path coverageを作れます。

ただし移動とSearchが三倍になるため、

- Aを北Cluster
- Bを南Cluster
- CはRemote Spell

のように分けた方がよい場合もあります。

## Broad + Specialist

実用的な形：

```text
Broad Rover：F1 A1 W1 E1 S1
Deep Specialist：D3 N2 G2
```

Broad Roverが全域を浅く探し、Specialistは重要Provinceだけ回ります。

## Manual + Remote

```text
Manual：F2 W2 E2 N2
Remote：A / S / D / G / B
```

国家のMage rosterに合わせて、歩かせやすいPathとRitual化するPathを分けます。

---

# Remote Spellの実務

正確なResearch・Path・Costは[Remote Site Search Spell](../data/spells/site-search.md)を参照してください。

## Augury

Fireを全Level確認します。

Fire Mageを戦場へ戻したい時期や、Fire incomeが低い国家で有力です。

## Auspex

Air Siteを確認します。

Air MageはCloud Trapeze、Storm、Lightning、Army supportなど競合任務が多いため、Search用Mageを固定しすぎないようにします。

## Voice of Apsu

地上Water Siteを確認します。

対象Province内へ発見情報が伝わる特殊性を考慮します。

## Voice of Tiamat

海ProvinceのElemental Siteをまとめて確認します。

一Castが高価なため、

- 海領土が十分ある
- Water incomeがある
- Elemental Gem全体が必要
- Casterを水中Labへ置ける

場合に使います。

## Gnome Lore

Earth Siteを確認します。

Earth GemはBooster・Forge・Army buffへ使うため、SearchとForgeが同じMage turnを競合しやすい点に注意します。

## Arcane Probing

Astral Siteを確認します。

低要求ですが、Pearlは用途が多いので、全Provinceへ自動連打するよりSearch queueを作ります。

## Dark Knowledge

Death Siteを確認します。

D1 Mageで届くため、低Path MageをRemote operatorへしやすいSpellです。

## Haruspex

Nature Siteを確認します。

Nature MageがSupply supportやArmy buffへ必要になる前に、後方を一巡させるかRemoteへ切り替えます。

## At the End of the Rainbow

Glamour Siteを確認します。

Glamour MageをScout・Raider・Battle supportへ使いたい国家で、Manual Searchの代替になります。

## Bowl of Blood

Blood Siteを確認します。

Blood Slaveを消費するため、Blood Huntの収益、Summon、Sabbath、戦争用Slaveと予算を分けます。

## Acashic Knowledge

全Pathを確認します。

使うProvinceを選ばないと25 Pearlを回収できません。

候補：

- Path coverageがほぼゼロ
- 高価値Terrain
- 遠距離・危険地
- 重要なThrone / Fort
- 多数のManual Searcherを送るより安い

---

# ケーススタディ

## ケース1：多Path Mageが安い国家

```text
Recruit-anywhere：F1 A1 W1 E1 Mage
Gold：安い
Research：普通
```

運用：

1. 二人をResearch
2. 三人目をBroad Rover
3. Expansion後方をL1で一巡
4. First war前にResearchへ戻す
5. 中盤はF/A/W/E不足PathをRemoteで補完

狙いは完全Searchではなく、低Costで四PathのGem economyを始動することです。

## ケース2：首都限定高Path Mageしかいない

```text
Capital only：F3 E3
Recruit-anywhere：研究Mageのみ
```

悪い運用：

```text
首都限定Mageを10Turn歩かせる
```

良い運用：

- 首都周辺の高価値ProvinceだけManual
- 研究を進めてAugury / Gnome Lore
- 低級Indie MageをBroad Roverへ使う
- PretenderをSearchへ使うならExpansion・Global計画と比較

## ケース3：海国家

```text
海Province：多数
W2 Mage：量産可能
```

運用：

- 最初の海ClusterはManual W2
- 海領土が広がったらVoice of Tiamat
- Cave / Coast / Underwater Mountain等のTerrainを別Pathでも確認
- Land footholdはVoice of Apsuと地上Searcherへ分離

## ケース4：Astral Pearl不足

```text
S1 Mage多数
Pearl income：1
Communion・Teleport・Dispelが必要
```

運用：

- S1多Path MageでManual Searchできる場所を先に回る
- Arcane Probingは高価値Provinceへ限定
- Acashic Knowledgeは原則後回し
- Pearl budgetをCombat / Booster / Searchに分ける

## ケース5：戦争直前

```text
First warまで3Turn
Searcher 2人
必要Researchまで40 RP
```

判断：

- Search Routeを中断
- 一人をResearchへ戻す
- 一人を最後の重要ProvinceだけSearch
- 不足Pathは戦争後Remote Search

Site Searchは戦争を遅らせてまで続ける自動作業ではありません。

---

# Searchを中止する条件

- Enemy raiderが後方へ侵入
- First warのResearchが遅延
- SearcherがBattle Mageとして必要
- Gem stockがRemote Searchを許容しない
- Search対象Provinceを維持できない
- Search済みcoverageが十分
- Game残りTurnが少ない
- 新しいSiteよりThrone・Fort防衛が優先

中止は失敗ではありません。

Opportunity costが変わったため、投資を止める判断です。

---

# Search後の処理

Site発見messageを読んだら、次を実行します。

## 1. Site効果を確認

- Gem
- Recruit
- Research / Ritual bonus
- Economy
- Scale / Dominion
- Enter effect
- Negative effect
- Event relation

個別情報は[Magic Site総合索引](../data/sites/index.md)から確認できます。

## 2. 利用条件を確認

- Labが必要か
- Fortが必要か
- 特定国家だけRecruit可能か
- 特定Path Mageが必要か
- Enter order対象が限定されるか
- Throne Claimが必要か

## 3. 守備を決める

- PD
- Fort
- Lab
- Temple
- Scout ring
- Mobile reserve
- Dome

## 4. Research・Gem planを更新

新しいIncomeによって、

- Booster chain
- Summon
- Combat script
- Global
- Remote attack

の優先度を変えます。

---

# 毎Turnのチェックリスト

```text
[ ] 新しく獲得したProvinceはどこか
[ ] Search coverageを記録したか
[ ] Broad Roverの次のRouteは連続しているか
[ ] 同じPath・Levelを重複Searchしていないか
[ ] First war / Researchを遅らせていないか
[ ] Remote Search queueはGem bottleneck順か
[ ] Searcherは前線で安全か
[ ] 発見Siteの利用条件を確認したか
[ ] 重要SiteをFort / PD / Scoutで守るか
[ ] Gem budgetを更新したか
```

---

# 国家別Site Searchテンプレート

```text
## Site Search計画

### Broad Rover
Unit：
固定Path：
Random Path：
Recruit制限：
Gold / RP：
Map Move / Survival：
標準Search深度：

### Deep Specialist
Unit：
Path：
対象Province：
戦場へ戻すTurn：

### Remote Search
最初に解禁するSpell：
Caster：
Research：
Gem予算：
優先Path：

### Route
北Cluster：
南Cluster：
海 / Cave：
国境：

### 戦争前条件
最低Gem income：
Search終了Turn：
Battle Mageへ戻す人数：
```

---

## 関連ページ

- [Site Search完全ガイド](site-search.md)
- [Search Level分布](../data/sites/search-levels.md)
- [Remote Site Search Spell](../data/spells/site-search.md)
- [Magic Site総合索引](../data/sites/index.md)
- [国家Recruitデータ](../data/recruitment/index.md)
- [Mage access早見表](../data/mage-access.md)
- [GemとBlood Slave](gems.md)
- [Researchと研究ルート](research.md)
- [Province](../systems/province.md)
- [Throne of Ascension](../systems/thrones.md)
