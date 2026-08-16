---
title: 初心者Q&A：内政・補給・自動化
page_type: guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# 初心者Q&A：内政・補給・自動化

[初心者Q&A](faq.md)の続編として、Expansion Armyが増え、Fort・Mage・Gem・大軍を管理し始めた頃に起きやすい疑問へ答えます。

Dominions 6では、戦闘に勝てるArmyを作るだけでは国家は伸びません。

> **Goldを毎Turnの生産へ変える**
> → **ArmyへSupplyを届ける**
> → **Unrestを抑える**
> → **MageへGemとItemを配る**
> → **繰り返し作業を自動化する**
> → **自動化が止まった理由を確認する**

という後方管理が必要です。

このページは、数式をすべて暗記するための記事ではありません。画面で見えた症状から、最初に確認する項目と詳しい基準記事へ移動するための入口です。

!!! note "Versionと操作表記"
    本文はDominions 6.35を基準にしています。ShortcutやButton配置はOptions、Platform、画面によって変わる場合があります。本文と異なる場合は、現在の画面で`?`を押して表示されるHelpを優先してください。

---

## まず困りやすい十二問

- Goldがあったはずなのに、次Turnほとんど残っていない
- 取ったProvinceのIncomeが国庫へ入っていない
- Resourcesが余ったので、別のFortへ送りたい
- ArmyにStarving表示が出た
- 大軍のSupplyをどう確保すればいい？
- Unrestが高くてRecruitできない
- Patrolすれば全部解決する？
- GoldがあるのにProvince Defenceを増やせない
- MageへGemをどう渡すの？
- Mageが予定外のGemを使った
- 毎Turn同じRitualやForgeを設定するのが大変
- Monthly orderが突然止まった

右側のページ内目次から、現在の症状に近い質問へ移動してください。

---

# Gold・Income・Local資源

## Q. Goldがあったはずなのに、次Turnほとんど残っていない

**A.** Incomeだけでなく、今Turnの支出と毎TurnのUpkeepを分けて確認します。

主な支出は、

- Unit・Commander・MageのRecruit
- 既存UnitのUpkeep
- Fort・Lab・Temple・Road等の建設
- Province Defence
- Mercenary
- Event・Diplomacy・特殊国家能力
- Repeat Recruitmentで継続しているQueue

です。

Dominions 6にはIncomeとUpkeepのSummary、今Turnに使ったGoldのSummaryがあります。Nation OverviewやIncome関連画面を開き、

```text
今Turnに入ったGold
－ 今Turnに使ったGold
－ 次Turn以降も続くUpkeep
```

へ分解してください。

「Goldが足りない」ではなく、**何へ継続的に流れているか**を特定します。詳しくは[Province](../systems/province.md)と[Forts](../systems/forts.md)を参照してください。

## Q. 取ったProvinceのIncomeが国庫へ入っていない

**A.** 所有しているだけでは、通常のGold税収が必ず国庫へ届くとは限りません。

まず次を確認します。

- Owned Provinceだけを通ってFriendly Fortへつながっているか
- 敵Raidで税収経路を切られていないか
- Unrestが高くないか
- Provinceを本当に自国が所有しているか
- Fortが敵に包囲されていないか
- 特殊国家・Commander・Siteの例外がないか

敵が中継Provinceを一つ取るだけで、その奥にある複数Provinceの税収が止まる場合があります。

なお、Gold税収経路とMagic SiteのGem incomeは同じ仕組みではありません。税収が切れたから、すべてのGem incomeも同じ理由で止まるとは考えないでください。

詳しくは[Province：Incomeと税収経路](../systems/province.md#incomeと税収経路)を参照してください。

## Q. Resourcesが余ったので、別のFortへ送りたい

**A.** 通常は送れません。

Resources、Recruitment Points、Commander Points、SuppliesはLocal capacityです。GoldやGemのような全国Stockではなく、毎TurnそのProvinceで使います。

```text
Gold       ：国家全体で使う
Gem        ：国家Treasuryと個人所持を行き来する
Resources  ：そのProvinceの生産力
RP / CP    ：そのProvinceの雇用枠
Supplies   ：そのProvinceの補給力
```

を分けます。

余ったResourcesを活かしたい場合は、

- そのProvinceまたは隣接Fortで重装兵をRecruitする
- FortのAdministrationで隣接Provinceから引き込む
- Resource feederとして残す
- 既存Fortと新Fortが同じResourceを奪い合わないよう配置する

という設計が必要です。

## Q. GoldもResourcesもあるのにMageが毎Turn完成しない

**A.** Commander Pointsを確認します。

Mage・Priest・Commanderは兵士用Recruitment Pointsではなく、Commander Pointsを使います。2 CP以上を必要とするMageは、Fortが小さいと完成まで複数Turnかかる場合があります。

```text
兵士が作れない
→ Gold / Resources / Recruitment Points

Mageが作れない
→ Gold / Commander Points / Lab・Temple・Site条件
```

と分けます。

第二Fortを建てる価値は、壁を一つ増やすことだけではありません。Commander PointとMage生産拠点を増やすことです。

## Q. 新しいProvinceで何を最初に確認すればいい？

**A.** PD 1だけ入れて終わらせず、用途を決めます。

```text
Income / 税収経路
Resources / Fort候補
Local Scout・Priest・Mage
Supplyと中継地点
Magic Site Search
Choke point・Retreat route
Temple・Dominion
Throne・Plane入口
```

のどれに価値があるProvinceかを確認します。

新領土をすべて同じように扱うと、Fortを建てる場所、守る場所、捨ててもよい場所が分からなくなります。[Province](../systems/province.md)を参照してください。

---

# Supply・Starvation・大軍の移動

## Q. ArmyにStarving表示が出た。何が起きている？

**A.** そのProvinceのSuppliesより、滞在UnitのSupply Usageが大きくなっています。

Starving UnitはMoraleが下がり、Supply不足が続くとDiseaseへつながります。戦闘をしていなくても、Armyの質が毎Turn落ちていく状態です。

最初に、Province画面の、

```text
Supplies
Supply Usage
```

を比較します。

不足している場合は、

- Armyを複数Provinceへ分ける
- Supplyの多い経路へ変更する
- Friendly Fort付近へ移す
- Supply Bonusを持つUnit・Item・Mageを使う
- Gluttonous Unitや大型Unitを別行動させる
- Siegeを長引かせない

ことで対処します。

Starving表示が消えても、すでに付いたDiseaseが自動で治るとは限りません。

## Q. 大軍のSupplyをどう確保すればいい？

**A.** 出発地ではなく、到着先と滞在予定地のSupplyを見ます。

Armyは全国Stockから一か月分の食料を持ち運ぶのではなく、基本的に現地のPopulation、Scales、Terrain、Fort、Site、Supply Bonusへ依存します。

```text
Army Supply Usage
≤
目的ProvinceのSupplies
＋ Fort・Item・Unit等のSupply補助
```

を目標にします。

戦争前には、

- 前線集合地点
- Siege予定Province
- Winterや極端なTemperature
- Death Scaleや低Population
- Sea・Cave・Void等のTerrain
- Retreat先

まで見ます。

強いArmyを一つへ詰め込みすぎるより、隣接Provinceへ分けて同時侵攻する方が補給上安全な場合があります。

## Q. Supply Usageが負の数字になっている。Bug？

**A.** Supply BonusがArmyの消費量を上回っている可能性があります。

Supplyを生むUnit・Item等が十分にいると、表示上のSupply Usageが負になることがあります。Armyが食料を消費していないというより、補給Bonusが差し引かれた結果です。

ただし、別Armyと合流したり、Bonus担当Commanderが死亡・移動したりすると一気に不足へ転じます。現在値だけでなく、次Turnの編成も確認します。

## Q. 移動し続ければStarvationは無視していい？

**A.** 無視しない方がよいです。

次のProvinceへ移ればSupply不足が解消する場合はありますが、Starving状態のMorale低下や、すでに発生したDiseaseは戦闘へ持ち越されます。

特に、

- 敵領深部へ進む
- Retreat先が少ない
- 大型・Gluttonous Unitが多い
- Siegeへ入る
- Rare MageやSacredが同行する

Armyでは、数TurnのSupply不足が戦争全体を壊します。

「次へ動くから大丈夫」ではなく、次の到着先のSupplyまで確認してください。

## Q. Fortへ籠もったら、なぜ補給が悪化した？

**A.** Siege中のFort内部は、通常のProvince外部と同じ補給条件ではありません。

敵に包囲されると外部からのSupplyが制限され、Fort内部の守備兵・民間人・大型Unitが貯蔵Supplyを消費します。

守備側は、

- Fortへ入れるUnit数を絞る
- Need Not Eatや低Supply Usage Unitを使う
- Supply Itemを準備する
- Relief Armyを用意する
- 不要なArmyを包囲前に退避させる

必要があります。

攻撃側も、長期Siege中は外側ArmyのSupplyとDiseaseを確認します。詳しくは[Forts](../systems/forts.md)を参照してください。

## Q. Terrain Survivalは移動だけの能力？

**A.** 移動以外にも意味があります。

Forest、Mountain、Swamp、Wasteland等のSurvival能力は、対応TerrainのMap Move負担を軽減し、Starvation時の影響を受けにくくする場合があります。

同じArmyにSurvival持ちと非所持Unitが混在すると、最も遅い・不向きなUnitが経路と到着Turnを決めることがあります。Commanderだけでなく同行Unitも右Clickして確認します。

詳しくは[Province：SuppliesとSupply Usage](../systems/province.md#suppliesとsupply-usage)を参照してください。

---

# Unrest・Patrol・Province Defence

## Q. Unrestが高いと何が困る？

**A.** Incomeだけでなく、Provinceの生産能力全体が落ちます。

Unrestは主に、

- Income
- Resources
- Recruitment Points
- Commander Points
- Blood Hunt
- Patrol効率
- Event・Rebellion Risk

へ悪影響を与えます。

Unrest 100付近ではRecruitment capacityが実質的に失われ、Goldがあっても兵士やMageを予定どおり完成させられません。

新しく占領したProvince、Blood Hunt拠点、Pillageされた後方、敵Spyが活動している地域では毎Turn確認します。

## Q. Unrestはどう下げる？

**A.** 原因を止める方法と、数値を下げる方法を分けます。

数値を下げる手段には、

- 自然減少
- Order Scale
- Friendly Dominion
- Province Defenceの一定効果
- Patrol
- Reduces Unrest能力
- Event・Spell・Magic Site

があります。

しかし、敵Spy、Blood Hunt、Pillage、悪性Site、Global等が原因なら、Patrolだけを続けても毎Turnまた増えます。

```text
原因を止める
＋
現在のUnrestを下げる
```

の両方を行います。

## Q. Patrolすれば全部解決する？

**A.** PatrolにはCostがあります。

PatrolはUnrest低下、Stealthy Unit発見、Siege外周の警戒に使えますが、住民を殺してPopulationを減らします。

Populationが減ると、将来の、

- Income
- Recruitment Points
- Supplies
- Province Defence上限
- Blood Hunt対象

も減ります。

特にBlood economyでは、

```text
Blood Slave income
－ Unrestによる経済損失
－ PatrolによるPopulation損失
```

を一つの収支として見ます。

Patrol Armyを大きくする前に、Unrestの原因と必要な低下量を確認してください。

## Q. PatrolしたTurnにIncomeはすぐ戻る？

**A.** 同じHostで完全に回復するとは限りません。

Income計算は、能動的なPatrolでUnrestを下げる処理より先に行われます。

```text
このTurnのIncome計算
→ PatrolでUnrest低下
→ 次TurnのIncomeが改善
```

と考えます。

今TurnのGold不足を解決するためにPatrolを追加しても、そのGoldを同じTurnに受け取れるとは期待しないでください。

## Q. GoldがあるのにProvince Defenceを増やせない

**A.** PopulationによるPD上限を確認します。

Province Defenceは通常最大100ですが、低Population Provinceでは、概念的に、

```text
Population / 10
```

がより低い上限になります。

Population 300なら、特殊例外がなければ高PDを購入できる上限はおおむね30です。Popkill Nation、Event、Pillage、Blood Hunt等で人口が減ったProvinceでは、以前よりPD上限が下がる場合があります。

Goldだけを見ず、Province情報のPopulationを確認してください。

## Q. Province Defenceはどこまで上げれば安全？

**A.** PDだけで安全になる固定値はありません。

PDは、

- Scoutや小規模Raidへの抵抗
- 敵編成の確認
- Stealthy Unitの発見補助
- Fort・Reserve Armyが来るまでの時間稼ぎ

には使えますが、主力Armyの代わりではありません。

高PDへ大量Goldを入れる前に、

```text
そのProvinceの価値
敵Raidの規模
近くの反撃Army
Fort・Choke point
PDで何Turn買えるか
```

を考えます。

詳しくは[Province：Unrest](../systems/province.md#unrest)と[Province Defence](../systems/province.md#province-defencepd)を参照してください。

---

# Gem・Blood Slave・Magic Itemの受け渡し

## Q. MageへGemをどう渡すの？

**A.** 基本はLaboratoryのあるProvinceで、CommanderのPersonal Magic Gems画面から渡します。

代表的な手順は、

```text
LabのあるProvinceへMageを置く
→ Mageを右Clickして詳細を開く
→ Personal Magic Gems欄を開く
→ National Treasuryから必要数を渡す
→ Battle Scriptと所持数を再確認する
```

です。

Dominions 6.30以降は、多くの画面でCommanderへMouseを置き、`Alt`＋Magic Pathの文字Keyを押して対応Gemを一個渡せます。たとえば`Alt`＋`F`はFire Gemの例です。`Alt`＋`Backspace`はGemを一個戻す操作として追加されています。

Pathごとの正確なKeyと、現在の画面で利用できる操作は`?`で確認してください。

## Q. Gemを一個ずつ配るのが大変

**A.** 6.30以降のGem Shortcutと、Gem transfer画面を使い分けます。

少数のBattle Mageへ、

```text
Fire Gemを2個
Earth Gemを1個
```

のように配る場合は、CommanderへMouseを置いたShortcutが速くなります。

大量配布、複数Path、Blood Slave、所持数の比較には、Personal Magic GemsまたはMagic Resource Treasuryの画面を使います。

配布後は、

- 何Battle分か
- 何Spell用か
- Retreat・Assassinationで失ってよい数か
- CasterのPathとFatigue

を確認します。

## Q. Commanderが持つGemを国庫へ戻したい

**A.** LaboratoryのあるProvinceで、Gem transfer画面からNational Treasuryへ戻します。

Blood Slaveには、Labへ送る・Poolする専用OrderやShortcutが使える場面があります。Commanderを選択した画面で`?`を押し、現行のOrderを確認してください。

前線から戻したRare Mage、大量Gemを持つ撤退Army、Blood Hunterについては、

```text
Labへ到着
→ Gem / SlaveをPool
→ ItemをTreasuryへ戻す
→ 次の任務を設定
```

までを一つの帰還手順にします。

## Q. Mageが予定外のGemを使った

**A.** ScriptしたSpellのCostだけでなく、Path上昇やFatigue軽減にもGemを使う場合があります。

確認するものは、

- SpellのGem Cost
- Casterの基礎Path
- Spellを唱えるために一時的なPath上昇が必要か
- Fatigueを下げるために追加Gemを使ったか
- Communion・Booster・Battlefield effect
- Conservative Gem Useの設定
- 敵が有効Targetだったか

です。

Conservative Gem Useは無駄遣いを減らすための設定ですが、必要なSpellのためにGemを絶対使わない設定ではありません。

ReplayとBattle logで、実際に何を唱え、戦闘後に何Gem残ったかを確認します。[GemとBlood Slave](../magic/gems.md)と[命令とBattle Script](../basics/orders.md)を参照してください。

## Q. MageへGemを持たせたのにSpellを使わない

**A.** Gemを持つだけではCast条件を満たしたことになりません。

- Researchが未完成
- Magic Pathが不足
- Gemで上げられる範囲を超えている
- Range内に有効Targetがいない
- Battlefield条件・Terrain条件が違う
- Fatigueが高い
- Script位置まで生存していない
- Spell AIが合法な別行動へ切り替えた

可能性があります。

「Gem不足」と決めつけず、CasterのPath、Script、位置、Replayをまとめて見ます。

## Q. Magic Itemを誰が持っているか分からなくなった

**A.** Magic Item TreasuryとItem所在地を確認する画面を使います。

Dominions 6では、各Magic Itemが現在どこにあるかを探すための画面が用意されています。`F8`のMagic Item Treasuryを入口にし、現在の画面で`?`を押してSort・Search・Transfer操作を確認してください。

Item管理では、

- National Treasury
- Commander装備
- Commanderの所持品
- 前線・後方の所在地
- Unique / Artifact
- Mount用Barding

を分けます。

Rare BoosterやResistance Itemを「作ったはず」だけで済ませず、次の使用者と使用Turnを決めます。[Magic Item総論](../items/index.md)を参照してください。

## Q. LabのないProvinceでItemやGemを動かしていい？

**A.** National Treasuryとの安全な受け渡しは、原則としてLabのあるProvinceで行う方がよいです。

Labがない場所では、交換できる範囲や、外した装備の扱いが制限される場合があります。前線で装備を組み替える前に、

- 外したItemを誰が持つか
- Slotが空いているか
- Labへ戻せるか
- Commanderが死亡・Routしたとき何を失うか

を確認します。

---

# Repeat Recruitment・Monthly order・作業の自動化

## Q. 毎Turn同じRecruit Queueを設定するのが大変

**A.** Repeat Recruitmentを使います。

Mage、Scout、Capital-only兵、定型的な補充兵など、毎Turn同じものを雇うFortで便利です。

ただしRepeat Recruitmentは、

- Fort建設資金を貯めるTurn
- Commander Pointを別Mageへ使うTurn
- Resourcesが不足したTurn
- 敵Rushへ緊急兵を出すTurn

でもGoldを継続的に使います。

End Turn前に、QueueだけでなくRepeatの有無も確認してください。

## Q. 毎Turn同じRitualを選び直すのが大変

**A.** Ritual選択画面のMonthly Ritualを使います。

Monthly Ritualを有効にしてRitualを選ぶと、Casterは新しいOrderを受けるか、Gem・Path・Target等の条件を満たせなくなるまで、同じRitualを繰り返します。

設定後は、

```text
毎月のGem Cost
残りGem
Target条件
Range・Plane・Terrain
Casterを何Turn拘束するか
```

を確認します。

一度設定したから永久に成功するわけではありません。

## Q. 毎Turn同じItemをForgeしたい

**A.** Forge画面のMonthly Forgeを使います。

Research Item、Supply Item、定型Resistance Item等を量産するときに便利です。

ただし、

- Gemが尽きる
- Unique / Artifactを作ろうとする
- Casterが移動する
- Labを失う
- Boosterを外す
- Forge BonusやSite Bonusが変わる

と停止・失敗します。

Monthly Forgeを使う前に、何個必要かと、何Turn後に止めるかを決めます。

## Q. Site Search Ritualも自動化できる？

**A.** Monthly Ritualとして設定できる遠隔Site Search Spellがあります。

対象選択はSpell、Range、探索済み情報、Plane、所有権等に依存します。同じProvinceへ無意味に使い続けないよう自動Targetする場合がありますが、すべてのProvinceを理想順で完全に探索してくれるとは限りません。

毎TurnMessageで、

- どのProvinceを調べたか
- 何Path・何Levelで調べたか
- すでに探索済みではないか
- 敵領や危険地域へTargetしていないか

を確認します。

詳しくは[Site Search](../magic/site-search.md)と[Site Search実戦手順](../magic/site-search-playbook.md)を参照してください。

## Q. 新しく雇ったMageが最初からResearchしている

**A.** OptionsのGive Orders to New Commanders Automaticallyが有効になっている可能性があります。

Research拠点では便利ですが、新規Mageを、

- Battle caster
- Site Searcher
- Forger
- Builder
- Prophet候補
- Gem運搬役

へ使う予定でも、自動Researchのまま見落とすことがあります。

自動OrderがあるCommanderは、Idle Commander警告から外れる場合があります。Recruit予定と役割表を別に確認してください。

## Q. Battle Scriptを何十人分も入力したくない

**A.** Script保存・貼り付けと、直前Orderの繰り返しを使います。

代表的には、

- `Ctrl`＋`1`～`9`：Script保存
- `1`～`9`：保存Scriptの貼り付け
- `X`：直前のSpell・Orderを繰り返す
- `?`：現在画面の正確な操作を表示

です。

ただし、同じScriptを貼っても、

- Magic Path
- Gem
- Fatigue
- Range
- Caster位置
- Communion役割

が違えば結果は同じになりません。

Scriptをコピーした後に、各Casterの合法性を確認します。[操作方法・ショートカット](shortcuts.md)を参照してください。

## Q. 自動化したからEnd Turn前に見なくていい？

**A.** 自動化は確認を不要にする機能ではありません。

自動化が特に危険になる変化は、

- GoldをFortへ回したい
- Gem incomeが減った
- Lab・Fortを失った
- CasterがAffliction・Diseaseを受けた
- Booster・Itemを移した
- Target Provinceの所有者が変わった
- 敵のCounterが見えた
- Armyが別Terrainへ移動した

です。

RepeatとMonthly orderは、**同じ前提が続く間だけ正しい**と考えます。

---

# 自動Orderが止まった・命令が実行されない

## Q. Monthly RitualやMonthly Forgeが突然止まった

**A.** Caster本人だけでなく、環境条件を確認します。

主な原因は、

- Gem不足
- Path不足、Boosterを外した
- Labがない、または失った
- Targetが無効になった
- Range外へ移動した
- Plane・Terrain条件が変わった
- Unique / Artifactがすでに存在する
- Casterへ別Orderを出した
- Siege・Event・特殊能力で行動できない

です。

MessageとCommanderの現在Orderを確認し、前Turnと何が変わったかを探します。

## Q. Research済みなのにRitualを選べない

**A.** Research LevelだけではCastできません。

確認するものは、

```text
CasterのMagic Path
Labの有無
必要Gem
Casting ProvinceのTerrain
Target ProvinceのTerrain
Range
同じPlaneか
Caster・Targetの特殊条件
```

です。

Grey表示のSpellを右Clickし、不足条件のTooltipを読みます。Ritualが研究済みでも、Casterが実際にそのPathへ届いていなければ使えません。

## Q. Research済みなのにItemをForgeできない

**A.** Construction Level以外の条件を確認します。

- 必要Magic Path
- 必要Gem
- Lab
- Item Slot・Barding等の種類
- Unique / Artifact制限
- National discount・特殊Forge条件
- CasterのForge Bonus・Booster

が関係します。

同じ名前に見えるItemでもTypeやSlotが違う場合があります。[Magic Itemデータ](../data/items/index.md)と[Magic Boosting](../magic/boosting.md)を参照してください。

## Q. CommanderのOrderが勝手に変わったように見える

**A.** まずMessageとUnitの特殊能力を確認します。

Orderが変わる主な理由には、

- Monthly orderが条件不足で解除された
- 新しいOrderで上書きした
- 移動先でBattle・Siege状態が変わった
- Charm・Control change等で所属が変わった
- Insane、Shattered Soul等の特殊能力
- Event・Affliction・特殊Site

があります。

Commander tokenやPortraitが通常と違う色・表示になっている場合は、右Clickして特殊能力と現在Orderを読みます。

## Q. 見えない敵からProvinceを攻撃された

**A.** Remote attack RitualやEventの可能性があります。

Dominions 6では、遠隔攻撃Ritualの多くがMessageとBattle Replayを生成します。

- Messageの発生源
- Target Province
- Damage type
- 生存者とAffliction
- 同じ攻撃が再び来る可能性
- Casterを特定できるScout・Scrying

を確認します。

通常Armyが見えないから安全とは限りません。重要Fort、Throne、Global中心Provinceには遠隔攻撃も含めた防御が必要です。

## Q. 自動ResearchにしたMageを前線へ出し忘れた

**A.** 自動Orderと役割計画を分けます。

自動ResearchはIdleを減らしますが、必要なBattle Mageを自動的に前線へ送る機能ではありません。

First War前には、Mageを、

```text
Research継続
Battle参加
Site Search
Forge
Ritual
Reserve
```

へ分類し、必要CasterへGem・Item・Script・移動Orderを設定します。

詳しくは[Researchと研究ルート](../magic/research.md)と[最初の戦争](first-war.md)を参照してください。

---

# End Turn前の後方管理Checklist

最初は毎Turnすべてを最適化する必要はありません。次の項目を同じ順で確認します。

```text
Gold
  ├─ Income / Upkeep
  ├─ Repeat Recruitment
  └─ Fort・Lab・Temple資金

Province
  ├─ 税収経路
  ├─ Unrest
  ├─ Population / PD上限
  └─ 新領土の役割

Army
  ├─ Supplies / Supply Usage
  ├─ Starving / Disease
  ├─ Multi-turn route
  └─ Siege予定

Mage
  ├─ 現在Order
  ├─ Monthly Ritual / Forge
  ├─ Gem / Blood Slave
  ├─ Item
  └─ Scriptと役割
```

次の一文を説明できれば、Turnを進めて構いません。

> **このGold、Gem、Mage、Armyは、次の数Turnで何を完成させるために使っているか。**

---

## 関連ページ

- [初心者Q&A](faq.md)
- [初心者ガイド](index.md)
- [操作方法・ショートカット](shortcuts.md)
- [初心者向けTips](beginner-tips.md)
- [Province](../systems/province.md)
- [Forts](../systems/forts.md)
- [GemとBlood Slave](../magic/gems.md)
- [Site Search](../magic/site-search.md)
- [Researchと研究ルート](../magic/research.md)
- [命令とBattle Script](../basics/orders.md)
- [Magic Item総論](../items/index.md)
- [ターン処理順](../reference/turn-resolution.md)

## 主な参照先

- Game内の画面別Shortcut Help（`?`）
- Game内のOptions / Preferences
- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
- Dominions 6.30公式更新情報（Gem transfer shortcut）
- [Dominions 4 Wiki - Beginner Information](https://wikiwiki.jp/dominions4/Beginner%20Information)（質問構成の参考。回答内容はDom6用に再構成）
