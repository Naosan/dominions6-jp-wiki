---
title: 最初の12ターン
page_type: guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-15"
---

# 最初の12ターン

このページは、国家固有の最適手順ではなく、**初回プレイで判断漏れを減らすための標準進行表**です。

Turn数は締切ではありません。地形、Independent、Map size、Awake Pretender、国家のRecruit制約、近隣Playerによって数Turn以上ずれます。重要なのは、各段階で何を完成させるかです。

!!! warning "国家記事を優先する"
    Sacred rush、Awake Expander、Underwater、Blood、Undead、Population依存国家、Capital-only依存国家では順序が大きく変わります。詳細な国家攻略がある場合は、そのExpansion・Research・Fort計画を優先してください。

---

## Turn 1：国家の生産装置を起動する

Turn 1の目的は、強い行動を一つ選ぶことではなく、**Recruit・Research・Expansion・偵察の四つを同時に動かし始めること**です。

### 1. CapitalのRosterを読む

最初に、Capitalで雇えるものを四つへ分類します。

- 前線を維持する兵
- Damageを出す兵
- Armyを率いるCommander
- ResearchまたはBattle Magicを担うMage

個々のStatsをすべて覚える必要はありません。[国家ページの読み方](../nations/how-to-read.md)と国家の[Recruitデータ](../data/recruitment/index.md)を使い、Recruit-anywhereとCapital-onlyを分けます。

### 2. Recruit Queueを設定する

初期Armyの補充だけでなく、次のExpansion Armyを作るつもりで雇用します。

多くの国家では、毎TurnのMage生産を止めるとResearch差が長期間残ります。ただし、Expansion Armyが弱すぎて領土を取れないなら、最初の数Turnは兵士とCommanderを優先する判断もあります。

確認するもの：

- Gold
- Resources
- Recruitment Points
- Commander Points
- Capital-only枠
- 次Turnに雇いたいMageの費用

### 3. Prophetを決める

まだProphetがいない場合、序盤に任命するのが標準です。

誰をProphetにするかは、単にHoly能力だけでなく、次を見ます。

- Expansion Armyへ同行するか
- Blessを必要とするSacredがいるか
- Commanderとして失いたくない個体か
- 前線で生存できるか
- PreachやThrone Claimへ使う予定があるか

Prophet化したCommanderを、無防備な最前列や射撃の正面へ置かないようにします。

### 4. 最初のResearch Breakpointを決める

「とりあえず全Schoolを1にする」のではなく、最初の戦争またはExpansionを助ける到達点を一つ選びます。

候補は国家によって異なりますが、考え方は共通です。

```text
使用Mage
＋ Spell / Item
＋ 対象
＋ 必要Gem
＋ 使う予定Turn
```

この五つを書けない場合は、[Researchと研究ルート](../magic/research.md)を読み直します。

### 5. 初期Armyを配置する

初期配置のまま攻撃しないで、最低限次を確認します。

- 盾兵または硬い兵が最初に接敵するか
- 高Damage兵が敵へ届くか
- Archerが自軍を撃ちやすい位置にいないか
- Commanderが最前列にいないか
- SacredへBlessが届くか
- Attack orderが敵構成と合っているか

詳しくは[命令とBattle Script](../basics/orders.md)を参照してください。

### 6. 最初の攻撃先を選ぶ

隣接ProvinceのIncomeだけでなく、Independentの種類、数、地形、接続、退却先を見ます。

情報が不足している強敵へ無理に出るより、偵察して一Turn待つ方が安いことがあります。特にCavalry、Barbarian、Crossbow、大型Tramplerなどは、見た目の人数だけでは危険度を判断しにくい相手です。

### Turn 1終了前Checklist

- [ ] Recruit Queueがある
- [ ] CommanderまたはMageの雇用を検討した
- [ ] Research目標が一つ決まっている
- [ ] Prophet方針が決まっている
- [ ] Scoutへ命令を出した
- [ ] 初期Armyの配置とAttack orderを確認した
- [ ] 攻撃先から退却できるProvinceがある

---

## Turn 2–3：最初の戦闘を教材にする

この段階の目的は、領土数を最大化することではなく、**自国のExpansion Armyが何に強く、何に損失を出すかを知ること**です。

### Battle Replayを見る

勝敗にかかわらず、次を確認します。

1. どのSquadが最初に接敵したか
2. 最初に死んだUnitは何Damageを受けたか
3. 盾・Protection・Defenceのどこが突破されたか
4. Commanderが危険な位置にいなかったか
5. Routしたのか、全滅したのか

詳しい見方は[Battle Replayの読み方](battle-replay.md)を参照してください。

### 次の攻撃を即決しない

最初の戦闘で勝ったArmyが、そのまま次も安全とは限りません。

- 損失を補充できるか
- HP・Affliction・Fatigue上の問題が残っていないか
- 次のIndependentは同じ種類か
- CommanderのLeadershipが足りるか
- 退路があるか

を確認します。

### 第二Commanderを準備する

兵士だけを増やしても、率いるCommanderがいなければ第二Armyになりません。

- Army leader
- Scout
- Priest
- Mage
- Builder

のどれが不足しているかを見ます。

### Expansion記録を始める

短いMemoで十分です。

```text
相手：Heavy Infantry 約n体
自軍：盾兵＋高Damage兵
結果：勝利、前衛損失大
原因：長期戦で疲労、Damage不足
次回：攻撃役を増やす
```

同じ失敗を繰り返さないことが、数Province早く取ることより重要です。

---

## Turn 4–6：Expansionを二本へ分ける

この段階では、最初のArmyだけで地図を回る状態から抜けます。

### 第二Expansion Army

第二Armyは第一Armyの完全な複製でなくても構いません。

- 第一Army：盾・重装中心で安定した正面戦
- 第二Army：Archer、Cavalry、Sacred、Pretender等で別の標的を担当

のように、得意なIndependentを分ける方が効率的な場合があります。

ただし、弱いArmyを二つ作るより、確実なArmy一つを維持する方がよい状況もあります。分割の基準は「兵数」ではなく、**それぞれが安全な標的を一つ以上持つか**です。

### Borderと敵位置を調べる

Scoutは領土を増やすUnitではなく、損失と奇襲を減らす投資です。

- 近隣Playerの旗
- Expansion速度
- 主力兵
- Pretenderの活動
- FortとThrone
- 地形とChoke point

を記録します。

Multiplayerでは接触時点から外交も始まります。境界の認識が違うだけで、準備していない戦争が起こります。

### 第二Fort候補を比較する

Fort候補はIncomeだけで決めません。

- Mageを毎Turn雇えるか
- Resources
- Capitalからの距離
- 前線への増援路
- Choke point
- Throne・重要Site
- 防衛可能性

を見ます。

Fort資金を貯め始めても、Expansion Armyが止まるなら早すぎる可能性があります。逆にGoldを毎Turn使い切り、いつまでも第二Fortを建てられないのも問題です。

### Researchを再確認する

最初の数Turnで新しい敵情報を得たら、研究目標がまだ適切か見直します。

- 高Protectionが見えた
- ShockやPoisonが見えた
- 大量Chaffが見えた
- MRが低い／高い
- Flying・Stealthが多い

など、敵の防御層によってBreakpointの価値は変わります。

---

## Turn 7–9：第二生産拠点と最初の戦争準備

この段階の目的は、取ったProvinceを将来のResearchと軍事生産へ変換することです。

### Fort建設を始める

Expansionが安定し、建設中のCommanderを守れるなら、第二Fortを始めます。

Fortは防壁だけではなく、将来のCommander Point、Mage、国家兵、Resourcesを生む施設です。詳しくは[Forts](../systems/forts.md)を参照してください。

### LabとTempleを計画する

すべてのFortに同時に両方を建てる必要はありません。

- Mageを雇う拠点ならLab
- SacredやPriest、Dominionが重要ならTemple
- 前線補給とGem移動が必要ならLab
- Throneや宗教戦の要所ならTemple

というように、役割から優先順位を決めます。

### Mageを役割分担する

Mageを一つの塊として見ず、次へ分けます。

- Researcher
- Battle caster
- Site Searcher
- Forger
- Ritual caster
- Rare Path保持者

全員を前線へ出すとResearchが止まり、全員を研究させると最初の戦争で魔法を使えません。

### First-war Folderを作る

ゲーム内のArmy Setupまたは自分のMemo上で、最初の戦争用に次をまとめます。

- 主力Army
- Reinforcement
- Scout
- Siege要員
- Battle Mage
- Gem
- 退却先
- Rally point

まだ攻めなくても、何が足りないかが見えるようになります。

---

## Turn 10–12：最初の戦争を「目的付き」で始める

Turn 12までに必ず宣戦する必要はありません。ここで必要なのは、戦争を始める条件を言語化することです。

### 目的を一つ選ぶ

悪い目的：

```text
隣に敵がいるので攻める
```

良い目的：

```text
Border Fortを取り、相手のMage生産を一拠点止める
```

```text
Throne周辺を確保し、次のFort建設地を守る
```

```text
相手のExpansion Armyが分散したTurnに主力を破壊する
```

### 勝利条件を一文にする

```text
盾兵で接敵を受け、Earth Buff後の高Damage兵で重装歩兵を破る
```

```text
Chaffで時間を作り、MageのAoE Spellで密集兵を削る
```

この一文に対応するUnit、Research、Gem、Scriptが揃っているか確認します。

### Siegeと増援を忘れない

Field Battleに勝っても、Fortを包囲・攻略できなければ戦争目的を達成できません。

- 壁を破れる兵数・Strength・Siege能力
- 敵のRelief Army
- Supply
- Gem補給
- 追加Mage
- 自軍Fortからの距離

を確認します。

詳しくは[最初の戦争](first-war.md)を参照してください。

---

## 毎Turnの短縮Checklist

時間がないTurnでも、次だけは確認します。

| 分野 | 問い |
|---|---|
| Message | Commander死亡、Event、建設完了を見たか |
| Replay | 最初に崩れた場所を一つ説明できるか |
| Recruit | Mageまたは必要Commanderを雇い忘れていないか |
| Research | 次のBreakpointと使用者が決まっているか |
| Army | 全Squadに意図した位置・命令があるか |
| Scout | 次に戦うProvinceと敵Armyを見ているか |
| Economy | Fort・Lab・Temple用Goldを意図的に残しているか |
| Magic | Gemを必要Casterへ移したか |
| Retreat | 負けた場合に逃げられるか |

---

## 進行が遅れている兆候

### Provinceは増えたがMageが増えない

Fort建設またはCommander生産が遅れています。領土をResearchへ変換できていません。

### Mageは多いが戦争で何も起きない

Research Breakpoint、Gem、Script、Range、対象指定のいずれかが欠けています。

### Expansion Armyが毎戦補充待ちになる

敵選択、配置、Damage役、盾、Morale、Fatigueを見直します。[序盤拡張](expansion.md)へ戻ります。

### Goldを使い切るが国力が伸びない

短期兵力だけへ使い、Fort・Mage・Researchへの投資が不足している可能性があります。

### Goldを貯め続けて領土を失う

将来投資を優先しすぎて、現在のArmyが不足しています。Fort完成前にMapを失えば回収できません。

---

## 国家類型による例外

| 国家類型 | 標準手順から変わりやすい点 |
|---|---|
| Awake Expander | Pretenderの安全な標的、疲労、Resistance、退路が最優先 |
| Sacred中心 | Prophet、Bless、Temple、Sacred生産量がExpansion速度へ直結 |
| Capital-only依存 | 第二FortよりCapital防衛と代替戦力が重要になる場合がある |
| Communion国家 | Mage数、Research、Slave/Master構成を同時に準備する |
| Blood国家 | Blood Hunter、Unrest、Population、Slave輸送が通常経済へ加わる |
| Undead国家 | Leadership、Reanimation、Priest Counter、Supply不要等の条件が変わる |
| Underwater国家 | 海陸移行、Amphibious、地上Fortへの接続を早期に計画する |

---

## 次に読む

- Independent戦で損失が多い：[序盤拡張](expansion.md)
- 最初の対Player戦を準備する：[最初の戦争](first-war.md)
- 戦闘結果を分析する：[Battle Replayの読み方](battle-replay.md)
- 研究目標を決める：[Researchと研究ルート](../magic/research.md)
- 第二生産拠点を計画する：[Forts](../systems/forts.md)

## 主な参照先

- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
