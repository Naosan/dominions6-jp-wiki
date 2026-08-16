---
title: 初心者Q&A：最初の戦争・外交・Raid・迎撃
page_type: guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# 初心者Q&A：最初の戦争・外交・Raid・迎撃

[初心者Q&A](faq.md)と[初心者Q&A：内政・補給・自動化](logistics-faq.md)の続編です。

最初の対Player戦で起こりやすい疑問を、

> **接触・外交**
> → **開戦判断**
> → **同時移動と迎撃**
> → **Raidと対Raid**
> → **Fort包囲とStorm**
> → **撤退・停戦・戦後処理**

の順に整理します。

Dominionsの戦争は、強いArmy同士を正面衝突させるだけではありません。

- 相手が次にどこへ動くか
- どのFort・Throne・生産拠点を取るか
- 何Turnで壁を破るか
- 誰がGemを補給するか
- 敗北時にどこへRetreatするか
- 第三国が何を得るか

まで含めて戦争です。

!!! note "外交とLobby rule"
    Dominions 6にはOptionalなFormal Diplomacyがあり、Game設定によりBindingまたはNon-bindingの協定を使えます。しかし、Community GameではDiscord等の合意、独自のNAP表記、禁止行為、敗北時の方針が別に定められることがあります。Game内UI、Game Info、Host説明、Lobby ruleを本文より優先してください。

!!! note "Versionと処理順"
    本文はDominions 6.35と、このWikiの[ターン処理順](../reference/turn-resolution.md)、[最初の戦争](first-war.md)、[Fort・Siege・Storm](../systems/forts.md)を基準にしています。同一Phase内のRandom順、特殊Spell、別Plane、Stealth、特殊国家、三国以上の介入には例外があります。

---

## まず困りやすい十二問

- 隣国と接触したら、最初に何を話せばいい？
- BindingとNon-binding Diplomacyは何が違う？
- NAP3とは何？ いつ攻撃可能になる？
- 最初の戦争相手はどう選ぶ？
- 開戦準備が終わったか、何で判断する？
- 敵Armyを追っても捕まえられない
- 自領へ防衛Armyが先に集まるのはなぜ？
- 複数Armyを同じTurnに到着させたい
- 小Armyに後方Provinceを取り続けられる
- Raid命令と普通の小規模侵攻は同じ？
- Field Battleに勝ったのにFortを取れない
- 壁を0にしたのに同じTurnにStormできない

右側のページ内目次から、現在の症状に近い質問へ移動してください。

---

# 接触・外交・境界

## Q. 隣国と接触したら、最初に何を話せばいい？

**A.** まず、境界、危険な共通目標、連絡方法の三つを確認します。

最初のMessageは長い同盟交渉でなくて構いません。

```text
接触した方向：
こちらが想定する境界：
係争中のThrone・Cave入口・海岸：
今後の連絡方法：
```

を明確にします。

良い最初の連絡は、相手の善意を前提にするものではなく、**誤解から予定外の戦争が始まる確率を下げるもの**です。

次のような情報は、必要以上に渡さない方が安全です。

- 正確なResearch Level
- Rare MageのPath
- Main Armyの現在地
- Gem在庫
- Pretenderの弱点
- 他国との密約

礼儀正しく、しかし確認済み情報と交渉材料を分けます。

## Q. 境界はどう決めればいい？

**A.** Province数を半分にするのではなく、地形・接続・Fort候補・Throneを含めて線を引きます。

境界候補を決めるときは、

- Capitalからの距離
- Expansion Armyの到着Turn
- Choke point
- High-income Province
- High-resource Province
- Throne
- Cave・Sea・Plane入口
- Retreat route
- 将来のBorder Fort

を見ます。

「このProvinceは自分が取る」だけでは不十分です。

```text
Province 34はこちら
Province 35は相手
Throne 41は未決定
Cave入口42は軍を置かず、再協議
```

のように、曖昧な場所を曖昧なまま隠さず、係争地として明記します。

## Q. 相手が境界の話へ返事をしない

**A.** 返事がないことを合意と解釈しないでください。

```text
合意済み
交渉中
未回答
```

を分けます。

未回答の地域へExpansion Armyを進める場合は、

- Scoutを先行させる
- Armyを一Turnで集結できる位置へ置く
- Fort資金を温存する
- 相手が同じProvinceへ入った場合の退却先を確認する
- Messageを記録する

必要があります。

沈黙は平和でも宣戦でもありません。**情報不足の状態**です。

## Q. Formal Diplomacyとは何？

**A.** Dom6で追加された、Game内の正式な外交協定です。

Game設定によっては、PlayerまたはAIとNon-Aggression Pact等をGame内で結べます。

ただし、Formal Diplomacyがあるからといって、

- 境界線
- Gem・Gold交換
- 共同戦争
- Throneの分配
- Scout通行
- Remote Ritual
- Stealth活動

まで自動的に定義されるわけではありません。

Formal Pactは契約の一部です。細部はMessageまたはLobby ruleで補います。

## Q. BindingとNon-binding Diplomacyは何が違う？

**A.** Bindingでは、有効な協定中のHostile orderがGame側に制限される場合があります。Non-bindingでは、協定を記録できても、同じ機械的保護を前提にしない方が安全です。

最初にGame Infoで、

```text
Formal Diplomacy：Binding / Non-binding / 使用しない
```

のどれかを確認します。

Bindingで特に重要なのは、

> **攻撃できるつもりで出したOrderが、協定違反として実行されない可能性がある**

ことです。

Non-bindingで重要なのは、

> **Gameが止めないことと、Lobby rule上許されることは別**

という点です。

宣戦前には、現在の協定、解除通知、残りTurn、対象NationをUIで確認してください。

## Q. NAPとは何？

**A.** Non-Aggression Pact、つまり相互不可侵の合意です。

しかし「攻撃しない」の範囲は、Gameごとに確認が必要です。

- ArmyによるProvince侵攻
- Raid・Pillage
- Remote attack Ritual
- Assassin・Seduction
- Stealth Unitの侵入
- Scout通行
- Border Provinceの奪取
- Throne rushへの介入

のどこまで含むかを決めます。

曖昧なNAPは、破られたときではなく、**締結した時点で問題を抱えています。**

## Q. `NAP3`とは何？

**A.** Communityでは、解約通知後に一定の猶予Turnを置くNAPを`NAP3`等と書くことがあります。

ただし、Turnの数え方にはLobby差があります。

```text
通知したTurnを1と数えるか
次のTurnから数えるか
攻撃Orderを出せるTurnか
Battleが解決してよいTurnか
```

で解釈がずれます。

そのため、略語だけで終わらせず、

```text
Turn 27に解約通知
最初にHostile orderを出せるTurn：
最初にBattleが起きてよいTurn：
```

を絶対Turn番号で確認します。

Formal Diplomacyを使う場合は、Game内に表示される解除状態と残り期間を優先してください。

## Q. NAPを解除したい。どう伝える？

**A.** 相手を非難する文章ではなく、日時と条件を明確にします。

```text
このMessageをNAP解除通知とします。
Game内協定の解除操作も行いました。
最初にHostile orderを出せるTurnは○○という理解です。
解釈が違う場合は、このTurn中に返信してください。
```

を基本にします。

境界、Scout、既に移動中のMulti-turn route、Remote Ritualも確認します。

新しい攻撃Orderを出す前に、以前のMulti-turn movementが敵領へ向かっていないか見直してください。

## Q. Game内NAPとDiscord上の約束が食い違っている

**A.** 勝手に都合の良い方を採用せず、Hostまたは当事者へ確認します。

優先順位はGameごとに異なります。

```text
Lobby rule
→ Host裁定
→ Game内Formal agreement
→ 当事者間Message
```

のどれを正本とするかを、開始時に決めるのが理想です。

食い違いを発見したTurnには、攻撃Orderを保留し、Screenshot・Message・Game Turnを保存します。

## Q. 共同戦争を提案された。乗るべき？

**A.** 「敵が弱い」だけでなく、戦後に誰が何を得るかを見ます。

確認するもの：

- 自分が取るFort・Throne
- 相手が取るFort・Throne
- 敵Capitalを誰が包囲するか
- Main Armyを誰が引き受けるか
- 戦争終了条件
- 片方だけが撤退した場合
- 第三国の利益

悪い共同戦争は、

```text
自分：敵Main Armyと戦ってGem・Mageを失う
相手：空いたFortとThroneを取る
```

という形になります。

共同戦争は善意の証明ではなく、**役割と利益を分配する契約**として考えます。

## Q. 同盟を結べば安全？

**A.** Standardの非Team Gameでは、共同攻撃の約束が恒久Team化や自動共同防衛を意味するわけではありません。

相手にも、

- 別戦線
- Research計画
- Throne勝利
- 自国防衛
- 他国との協定

があります。

「助ける」と言われた場合も、

```text
どのProvinceへ
何Turnに
どの規模で
何を攻撃するか
```

まで確認します。

Teamとしての共有勝利を使うDisciple Gameは、通常の外交協力とは別です。[Disciple Game](../systems/disciple-game.md)を参照してください。

## Q. 相手の情報はどこまで信じる？

**A.** 外交情報もScout情報と同じく三段階へ分けます。

```text
確認済み：Replay、Scout、Score、Mapで確認
推定：国家Roster・Research Timingから推測
主張：他Playerがそう言っている
```

第三国から、

> あの国はあなたを攻める

と言われても、それだけでMain Armyを移動しません。

ただし、完全に無視するのでもなく、Scout、Rally point、Gem配備を早める材料にします。

---

# 開戦相手と戦争目的

## Q. 最初の戦争相手はどう選ぶ？

**A.** 一番近い国、一番弱そうな国、外交で嫌いな国、のどれか一つだけで選びません。

比較するもの：

- Borderまでの距離
- Fort・Throne・Capitalの位置
- 敵Main ArmyとMage
- 自軍Damageと敵防御の相性
- Research Timing
- Siegeに必要なTurn
- Supply
- Retreat route
- 他国が介入する可能性
- 戦後に守れる国境線

良い相手とは、単にBattleで勝てる国ではなく、

> **目的を達成し、戦後に得たFort・Throne・Incomeを保持できる相手**

です。

## Q. 戦争目的は「相手を倒す」ではだめ？

**A.** どこで止まるか決まらないため不十分です。

最初の戦争では、Map上の対象へ落とします。

```text
Border Fortを取る
ThroneをClaimできる状態にする
敵のMage Fortを一つ止める
Cave入口を確保する
Main Armyを自国Fort前で迎撃する
```

目的が決まると、必要なSiege、Supply、Gem、外交期間が決まります。

## Q. 敵Capitalを最初から狙うべき？

**A.** Capitalが最短勝利条件なら候補ですが、常に最初の目標ではありません。

Capital攻撃には、

- Capital-only Recruit
- 高いPD・Fort守備
- 敵の最短増援
- Home Dominion
- 大量Mage
- 長期Siege
- 第三国による後方侵入

が伴います。

Border Fortや重要Throneを取り、敵生産と移動を削ってからCapitalへ進む方が安定することがあります。

## Q. 開戦準備が終わったか、何で判断する？

**A.** 次の五文を書けるか確認します。

```text
目的：
敵の主力：
自軍の勝利条件：
進行経路：
撤退・終了条件：
```

さらに、

- 使用Spellを研究済み、または開戦Host前に完成する
- Casterがいる
- Gemがある
- 前衛とDamage役がいる
- Siege要員がいる
- Retreat先がある
- 後方のRaid対策がある

ことを確認します。

詳細なTemplateは[最初の戦争](first-war.md)を参照してください。

## Q. 兵数で上回っていれば準備完了？

**A.** 兵数だけでは判断できません。

```text
前衛
Damage dealer
Mage core
Commander protection
Siege
Supply
Raider
Reserve
```

が揃っているか見ます。

100体の低Damage兵が、高Protection兵とBattle Mageへ正面から入るより、40体の役割分担されたArmyの方が機能する場合があります。

## Q. 研究をもう一Level待つべき？

**A.** そのLevelが戦争目的を変えるかで決めます。

待つ価値が高い例：

- 敵主力DamageへのResistance
- 高Protectionを破るSpell
- Battlefield-wide Buff
- Booster完成
- Siege・SummonのBreakpoint

待つ価値が低い例：

- Casterがまだいない
- Gemがない
- Armyが弱い
- 敵が先にBorder Fortを完成する
- 第三国が同じTargetへ動いている

第一Breakpointを開戦条件、第二Breakpointを敵Counter後の切替として分けます。

## Q. Gemは何Battle分持たせる？

**A.** 予定Battle数とSpell用途から逆算します。

```text
Border Battle
Main Battle
Relief Battle
Storm
Emergency Retreat
```

をすべて同じMage一人のGemで賄おうとすると、前半で使い切るか、死亡時に大量損失します。

- Main Battle用
- Storm用
- 補給用
- Reserve

へ分けます。

詳しくは[初心者Q&A：内政・補給・自動化](logistics-faq.md)と[Gem](../magic/gems.md)を参照してください。

## Q. 一種類のDamageで押し切れない？

**A.** 最初は勝てても、Resistanceまたは専用Counter一つで止まるRiskがあります。

```text
主Damage：通常物理
副Damage：Shock

主Damage：Fire
副Damage：Strength Buff近接

主Damage：MR攻撃
副Damage：Poison・物理
```

のように、相手が主Damageへ対策した後の切替を用意します。

## Q. 宣戦してからArmyを集める？

**A.** 協定・Lobby ruleを守ったうえで、開戦可能TurnにはArmyが機能する状態へ近づいている方がよいです。

ただしBorderへ全軍を早く集めると、意図が見え、Supplyを消費し、別方向が空きます。

- 一Turnで合流できるRally point
- Fort内Reserve
- Stealth・Scout
- Gemを持たない移動段階
- 最終Turnだけの集結

を使います。

## Q. Surprise attackは卑怯？

**A.** Game setting、Formal agreement、Lobby rule、当事者間の約束に従います。

協定がなく、Hostile actionが許可されているGameでも、Communityごとに宣戦通知の慣習は異なります。

重要なのは、自分に都合の良い「普通」を後から持ち出さないことです。

開始前に、

- NAPの扱い
- 宣戦通知
- Scout通行
- Remote Ritual
- Throne rush
- Player surrender

のRuleを確認します。

---

# 同時移動・迎撃・合流

## Q. 敵Armyを追っても捕まえられない

**A.** 敵の現在地ではなく、次に価値があるProvinceを予測します。

Dominionsは同時Turnです。

```text
自軍：敵の現在地へ移動
敵軍：次のProvinceへ移動
```

なら、Battleにならず追い続けることがあります。

迎撃候補：

- Fort
- Lab・Temple
- Tax routeの中継
- Retreat route
- Choke point
- Throne
- 高Income Province
- 合流地点

敵が取りたい場所へ先に防衛Armyを置きます。

## Q. 防衛Armyが侵攻Armyより先に自領へ集まるのはなぜ？

**A.** 通常のTurn処理では、Friendly Province間のMovementがHostile Provinceへの侵攻より先に処理されます。

```text
北の自軍 → 中央自領
南の自軍 → 中央自領
敵Army   → 中央自領
```

の場合、北・南の友軍が先に中央へ集まり、その後に敵侵攻を迎えます。

この前後関係により、Fort networkと中央Reserveが強くなります。[ターン処理順](../reference/turn-resolution.md)を参照してください。

## Q. 敵と自軍が互いのProvinceへ動き、すれ違った

**A.** 同じ最終Provinceへ入らなければ、必ず途中でBattleになるとは限りません。

移動Arrowが交差して見えても、Battleは道路上で起こるのではなく、処理後に敵対Armyが同じProvinceへ存在するかで決まります。

相手の侵攻を止めたいなら、

- 守るProvinceへ留まる
- Friendly reinforcementを集める
- Chokeへ先回りする
- Fortで時間を買う

方が確実です。

## Q. 複数Armyを同じTurnに到着させたい

**A.** 一歩手前のFriendly Rally pointへ集め、最後の一移動だけを同じTurnに出します。

```text
後方Army A ┐
後方Army B ├→ Rally point
Mage core  ┘
        ↓
`Y`で到着予定Armyを確認
        ↓
次Turnに最終侵攻
```

Multi-turn movementで同じ目的地を指定しても、Map Move、Terrain Survival、同行Unitにより経路と到着Turnがずれる場合があります。

`Y`は選択Provinceへ到着予定のArmy Setupです。現在いるArmyの`T`と区別してください。

## Q. Teleport Mageと徒歩本隊を同じBattleへ入れたい

**A.** 自動的に同時参加するとは限りません。

Magic MovementによるBattleは通常Movementより先に解決される場合があります。

```text
Ritual
→ Magic Phase Battle
→ Friendly / Hostile Movement
→ Main Battle
```

となるため、Teleport Mageが本隊より先に単独戦闘するRiskがあります。

- Magic Phaseで敵がいるか
- Attack Current ProvinceするStealth部隊
- Retreat先
- 本隊が本当に到着するか

を確認します。

## Q. Armyへ移動を出したのに動かなかった

**A.** Orderだけでなく、Host中に成立条件が残ったか確認します。

よくある原因：

- Binding agreementによりHostile orderが制限された
- 唯一のCommanderがAssassinationで死亡した
- 中継ProvinceをMagic Phaseで失った
- Map Move・Terrain条件を満たさない
- Siege状態
- Stealthy CommanderがSneakになっていた
- 新しいOrderでMulti-turn routeを上書きした
- 目的地のPlane・接続が通常移動では使えない

Message、Commander Order、Arrow、Battle Replayを確認します。

## Q. Assassinで敵Armyを止められる？

**A.** 唯一のCommanderをMovement前に失わせれば、Army移動を止められる場合があります。

Assassinationは通常Movementより先です。

ただし、

- Commanderが複数いる
- Assassinが失敗する
- Bodyguard
- Target選択
- Mindless・特殊Leadership
- Armyが別Commanderへ移る

場合があります。

Assassin一人へ戦争全体を依存させず、成功した場合に侵攻ArmyまたはRaidが利益を得る計画にします。

## Q. Multi-turn movementを戦争中も使っていい？

**A.** 後方増援には便利ですが、前線では毎Turn確認してください。

経路は、

- Province所有者の変化
- Magic Phase Battle
- 敵Army
- Terrain
- Siege
- 新Order

で崩れます。

前線Commanderに数Turn先の目的地を入れたままにすると、敵Fort・Main Army・NAP解除状態が変わっても進み続けるRiskがあります。

## Q. Retreat先はいつ確認する？

**A.** Battleを出す前です。

- 隣接Friendly Province
- Enemy ownership
- Fort
- River・Mountain・Sea・Plane接続
- 同Turnの別Battle
- Siege

で退却可能性が変わります。

Battleに勝てる確率が同じでも、退路のない侵攻は期待損失が大きくなります。

---

# Raidと対Raid

## Q. 「Raid」とは何？

**A.** 二つの意味を分けます。

### 一般的なRaiding

小規模で高速なArmyが、守りの薄いProvince、Tax route、Lab、Temple、Scout、後方Fortを狙う戦術です。

### Game内の`Raid` order

Pillager等の条件を持つCommander・Unitが使う専用Orderです。

Dom6の公式変更点では、専用Raid commandは旧作と同じ往復型ではなく、**move + pillageとなり、出発Provinceへ戻らない**形へ変更されたと説明されています。

画面のOrder名、移動Arrow、対象条件を`?`で確認し、一般的な小規模侵攻と混同しないでください。

## Q. Raidの目的はProvinceを永久保持すること？

**A.** 必ずしもそうではありません。

Raidの主目的は、

- Incomeを止める
- Tax routeを切る
- Lab・Templeを危険にする
- Mage・Scoutを移動させる
- Main Armyを後方へ戻させる
- Fort建設を止める
- 情報を取る

ことです。

Provinceを一Turn保持しただけでも、敵の生産・移動計画を崩せる場合があります。

## Q. どのProvinceをRaidすればいい？

**A.** PDが低い場所ではなく、取ったときに複数の価値が止まる場所を優先します。

価値が高いTarget：

- Friendly FortへのTax route中継
- Lab・Temple
- 新設Fort予定地
- Cave・Sea・Plane入口
- Retreat route
- High-income Province
- Mage・Blood Hunterの集積地
- Main Armyの補給経路

価値が低いTargetへ毎Turn小Armyを失うと、Main Battleの兵力を削るだけです。

## Q. Raiderはどれくらい小さくてよい？

**A.** 目的ProvinceのPD・Patrol・近接Reserveを倒せる最小規模です。

小さすぎるとPDへ負け、大きすぎるとMain Armyが弱くなります。

```text
成功時の利益
－ RaiderのGold・Gem・Commander価値
－ 反撃で失う確率
```

を比較します。

Rare Mage、Booster、Capital-only Unitを、単なるPD狩りへ使わないようにします。

## Q. PDを上げればRaidは全部止まる？

**A.** 止まりません。

PDは、

- Scout
- 小規模Raider
- Event
- 情報取得
- 反撃までの時間稼ぎ

には役立ちますが、大きなRaiderやMage支援Armyには負けます。

対Raidは、

```text
Scout
＋ 適量PD
＋ Mobile Reserve
＋ Fort network
＋ 価値の高い場所の優先防衛
```

で作ります。

## Q. PDはいくつ入れる？

**A.** 固定値ではなく、敵の最小Raiderを倒すか、少なくとも情報を取れる値にします。

考えるもの：

- Province価値
- 敵の高速Unit
- Stealth・Flying・Sailing
- 近くのReserve
- PopulationによるPD上限
- Fortの有無
- 失った場合のTax route

すべてのProvinceへ高PDを買うより、Fort・Choke・中継Provinceへ重点配備する方がよい場合があります。

## Q. 小Armyに後方Provinceを取り続けられる。どう止める？

**A.** Raider本人を追うより、次の価値Targetと出口を制限します。

- ChokeへReserveを置く
- Fort間の中央Provinceを守る
- Scoutで次の移動候補を見る
- High-value ProvinceだけPDを上げる
- Flying・Cavalry等の迎撃部隊を用意する
- RaiderのRetreat routeを切る
- Main Armyを必要以上に戻さない

Raider一隊の目的は、Provinceよりも**あなたのMain Armyを後退させること**かもしれません。

## Q. Stealthy Raiderをどう見つける？

**A.** Scout情報だけでなくPatrolを使います。

Turn処理では、Stealthy Unitが移動した後、到着ProvinceでPatrol detectionを受ける場合があります。

```text
Sneak Movement
→ 到着
→ Patrol detection
```

です。

ただしPatrolはPopulationを減らす場合があり、すべての後方Provinceへ大量兵を置くのは高Costです。

- Fort
- Lab
- Blood Hunting拠点
- Throne
- Choke

へ重点配備します。

## Q. Scout一人もRaid扱い？

**A.** Scoutは情報Unitですが、空Provinceの占領、Tax route遮断、Fort外側の所有変更に使われる場合があります。

「戦闘力がないから無害」とは限りません。

一方でScoutを発見するために高価なArmyを固定すると、相手の目的を達成させます。

PD、Patrol、Mobile Reserveを使い分けます。

## Q. Fort ProvinceをRaidする価値はある？

**A.** Fortを取れなくても、外側を支配し包囲状態にできれば価値があります。

- Recruitment停止
- Mage生産停止
- Tax routeへの圧力
- Enemy Armyの拘束
- Relief強制

につながります。

ただしFortを破るSiege力がなく、敵Break Siegeに負けるなら、Raiderを捕まえる罠にもなります。

## Q. Raid commandを使えば安全に戻れる？

**A.** Dom6では旧作の「襲撃して出発地へ戻る」イメージで使わないでください。

現行のOrder説明とArrowを確認し、Raid後にどのProvinceへ残るか、Retreat先があるかを見ます。

Game内の`?`とCommander Order表示を最終基準にしてください。

## Q. Raidしない方がよいのはいつ？

**A.** Raiderを抜くことでMain Armyの勝利条件が崩れるときです。

- 前衛が不足
- Bless役が一人しかいない
- Siege要員が足りない
- Commanderが不足
- 敵Main Armyが目前
- Raiderが高価なRare Unit
- 反撃経路が一つしかない

なら、本隊へ残します。

---

# 防衛戦・Capital rush・二正面戦争

## Q. 敵が国境を越えた。最初に何をする？

**A.** 全Armyを敵の現在地へ投げず、目的と速度を確認します。

最初の一Turnで、

1. MessageとScout情報を読む
2. 敵Armyの構成・Mage・Gemらしい動きを確認
3. 次に狙われるFort・Throne・Tax routeを推定
4. Friendly movementで防衛Armyを集める
5. Capital・Mage FortのRecruitを戦時へ切り替える
6. Research Breakpointを再確認
7. 外交連絡を行う

を進めます。

## Q. どのProvinceを捨て、どこを守る？

**A.** Mapの色ではなく、失ったときに国家機能が止まる場所を守ります。

優先候補：

- Capital
- Mage Fort
- Throne
- Lab・Temple
- Cave・Plane入口
- Tax route中継
- Retreat route
- Relief route

Low-incomeの袋小路を守るためにMain Armyを分割し、Border Fortを失わないようにします。

## Q. 防衛ArmyはFort内と外、どちらへ置く？

**A.** 目的で分けます。

### Fort外

- Field Battleで侵攻を止める
- PDと一緒に戦う
- 侵攻後すぐ反撃する
- Retreat先を持つ

### Fort内

- Main Armyを避けて時間を買う
- Siege Defence
- Break Siege
- Storm防衛
- Mage・Rare Unit保護

Fort内へ入れすぎるとRecruitが止まり、Supplyが悪化し、外側を自由に使われます。

外へ出しすぎると一度のField BattleでFort防衛まで失います。

## Q. Capital rushを受けた。Expansionを続ける？

**A.** Capitalを失うRiskと、Expansion Armyが敵後方へ圧力をかける価値を比較します。

Capitalは通常、

- Capital-only Recruit
- Pretender・Prophet
- 高Income
- Lab・Temple
- Mage生産
- Dominion

の中心です。

救援が間に合うならExpansion Armyを戻します。

戻しても間に合わない場合は、

- 敵後方Fortを包囲
- Tax route切断
- 別FortでMage生産継続
- 外交支援
- Capital内Storm防衛

を組み合わせます。

## Q. 敵Armyが大きすぎて正面から戦えない

**A.** 一戦で全滅させる以外の勝利条件を作ります。

- FortでTurnを買う
- Supplyを悪化させる
- Raiderで後方を切る
- AssassinでCommanderを狙う
- Resistance完成まで撤退する
- Chokeで戦線幅を狭める
- 第三国へ圧力を依頼する
- Enemy MageへRemote attack

ただし一種類の奇策だけへ依存せず、最終的にどのArmyでFortを守るか決めます。

## Q. Remote RitualやAssassinationは通常Armyより先に来る？

**A.** 多くのRitual、Horror attack、Assassinationは通常Movementより前に処理されます。

そのため、

```text
Commanderを暗殺
→ Armyが移動不能

Remote attack
→ Mage・PDを削る
→ 後から通常侵攻
```

という連携が可能です。

防衛側は、

- Commander複数化
- Bodyguard
- Gem分散
- Lab・Mage分散
- Scout
- Remote attack Replay

で被害を限定します。

## Q. 二正面戦争になった

**A.** 二国を同じ強さで押し返そうとせず、片方を時間稼ぎへ変えます。

```text
戦線A：Fort・PD・Scoutで遅延
戦線B：Main Armyで決着
```

のように役割を分けます。

外交では、

- 停戦
- Border Fortだけ譲る
- Throne以外の撤退
- 第三国への共同圧力

を検討します。

二戦線へMage・Gemを半分ずつ分け、どちらの勝利条件も完成しない状態を避けます。

## Q. 第三国が戦争へ介入しそう

**A.** Main Armyの勝敗だけでなく、戦後のPower balanceを見ています。

第三国が狙いやすいもの：

- 空いたBorder
- 消耗したWinner
- Siege中の後方
- Claim直前のThrone
- Capitalから遠い新領土

開戦前から、

- 戦争終了条件
- Reserve
- 新Border Fort
- Throne Claim担当
- 第三国との連絡

を用意します。

---

# Field BattleからSiege・Stormへ

## Q. Field Battleに勝ったのにFortを取れない

**A.** Province外側を取っただけで、Fort内部は防御側が保持しています。

```text
Field Battle勝利
→ 外側支配
→ Siege
→ Wallを0へ
→ 次Turn以降にStorm
→ Storm勝利
```

が基本です。

敵生産を止められる価値はありますが、Fortを所有したわけではありません。

## Q. 包囲したFortで敵がRecruitを続けている？

**A.** 通常、包囲中のFortではRecruitmentが停止します。

ただし、

- 包囲開始Timing
- 既にRecruitされたUnit
- Fort外と内の位置
- 特殊国家・Site
- Messageの表示

を確認します。

Fortを包囲する価値は、壁を削るだけでなく、毎TurnのMage・Commander生産を止めることです。

## Q. 壁を0にしたのに同じTurnにStormできない

**A.** Fort StormがSiege damageより先に処理されるためです。

概念的には、

```text
Field Battle
→ Fort Storm
→ Retreat
→ Siege damage
```

です。

そのHostの最後に壁を0へしても、Storm Phaseは既に終わっています。

次Turn提出時にStorm Orderを出します。

## Q. 壁が0ならすぐStormするべき？

**A.** Relief Army、守備Mage、自軍損耗、Storm geometryを比較します。

すぐStormする利点：

- 敵救援前に取る
- Recruitment停止を占領へ変える
- 自軍Supply消耗を短くする

待つ利点：

- Gem補給
- Storm専用Army到着
- Resistance完成
- Scout・Remote attack
- Main Army回復

ただし待つほど、敵もRelief、Wall強化、Mage Script、外交支援を準備します。

## Q. Break Siegeと外部Relief Armyは同じBattleへ入る？

**A.** 同TurnにFort内部がBreak Siegeし、外部友軍が到着すれば、同じ外側Field Battleへ参加できる場合があります。

```text
Fort内Army ─ Break Siege ┐
                         ├→ Siege ArmyとのField Battle
外部Army ─ Relief ───────┘
```

防御側の重要な連携です。

攻撃側は、

- Fort内部Army
- 外部Relief
- Magic・Remote support

の三つを別にScoutします。

## Q. Relief Armyが来るTurnにStormを出したらどうなる？

**A.** 外側のField Battleが先です。

1. Siege ArmyとRelief / Break SiegeのBattle
2. 攻撃側が外側を保持していればStorm

の順になります。

外側BattleでSiegerが敗北すれば、予定したStormは成立しません。

## Q. Siegeに強いUnitをそのままStormへ出せばいい？

**A.** Siege力とStorm戦闘力は別です。

- 高Strength
- Flying
- Siege Bonus
- 大量Chaff

は壁を早く壊しますが、狭いGate、Wall defender、AoE、高Morale守備兵へ強いとは限りません。

```text
Siege chaff
Storm screen
Storm damage
Mage
Flanker
```

へ分けます。

## Q. Storm戦でArmyが詰まる

**A.** 突破口が狭く、Field Battleより戦線幅が小さいためです。

- 大型Unit
- 密集Formation
- 後列Damage dealer
- 重装Chaff

を詰め込みすぎると、後方が攻撃できません。

AoE、Long weapon、Repel、Fear、MoraleもField Battleと違う価値になります。[Fort・Siege・Storm](../systems/forts.md)を参照してください。

## Q. Fort守備側はStormでRetreatできる？

**A.** Besieged側CommanderがStorm戦でRetreatすると死亡する扱いがあります。

通常Field Battleのように安全な隣接Provinceへ逃げられると考えないでください。

- Morale
- Leadership
- Fear対策
- Commander分散
- Bodyguard

が特に重要です。

## Q. Main ArmyをFort包囲へ全部残す？

**A.** 壁を破る速度、Relief Risk、別戦線を比較します。

残す理由：

- Break Siegeへ備える
- Relief Armyを倒す
- Storm用Gem・Mageを守る

分ける理由：

- 周辺Provinceを取る
- Tax routeを切る
- 次Fortを包囲
- 後方Raidを止める

Siege Bonus Unitと最低限の護衛だけで壁を削り、Main Armyを一歩後ろへ置く方法もあります。ただし敵Sallyに各個撃破されないようにします。

## Q. Fortを取った直後、何をする？

**A.** 前進前に占領地を生産拠点へ変えます。

- Lab・Temple・Fort damage
- Recruit可能Mage
- Gem・Item
- Dominion
- Unrest
- Supply
- Tax route
- Retreat route
- 敵Counterattack
- Throne Claim

を確認します。

勝利直後のArmyは損耗し、Gemを使い、後方から遠くなっています。次のProvinceへ自動的に進ませないでください。

---

# 撤退・停戦・戦争終了

## Q. いつ撤退すべき？

**A.** 一戦負けた後ではなく、戦争目的を達成できない条件が成立した時点です。

撤退条件の例：

- 必須Researchが間に合わない
- Enemy second Armyが合流
- Resistance不足
- SiegeがRelief前に終わらない
- Capitalが脅かされる
- 第三国が参戦
- Rare Mage・Commanderを失う
- Retreat routeが消える

撤退は敗北の承認ではなく、Armyを次の防衛線へ保存するOrderです。

## Q. 一度勝った。どこまで追う？

**A.** 最初に決めた終了条件までです。

```text
Border Fort取得
Throne確保
Main Army撃破
敵Mage Fort停止
```

を達成したら、

- Supply
- Gem
- 補充
- 新Border
- 第三国
- Enemy Capital defence

を再評価します。

勝利後の無計画な前進は、最も起こりやすい反撃機会です。

## Q. 停戦条件は何を話せばいい？

**A.** 「和平する」だけでなく、MapとTurnへ落とします。

```text
所有Province：
Fort・Throne：
撤退完了Turn：
Scout・Stealth Unit：
新しいNAP：
Gem・Gold・Item：
Claim中のThrone：
第三国との共同作戦：
```

曖昧な撤退経路は、同TurnのMovementで再戦を起こします。

## Q. 負けているが、何を残せば再建できる？

**A.** Province数より、生産と技術経路を残します。

優先して保存するもの：

- Mage Fort
- Rare Path holder
- Pretender・Prophet
- Booster
- Researcher
- Commander
- Safe Lab
- Gem reserve
- Retreat route

前線Provinceを守るために、国家の全Mageを失わないようにします。

## Q. Capitalを失ったら終わり？

**A.** 重大ですが、即敗北とは限りません。

- 他FortのMage生産
- Dominion
- Pretender
- Throne
- Field Army
- Gem income
- 外交

が残っていれば継戦できます。

ただしCapital-only Recruit、Income、Dominion、Research基盤を失うため、奪回計画または別拠点への国家機能移転が必要です。

## Q. 第三国がWinnerになりそう

**A.** 二国間の勝敗ではなく、戦後の相対国力を見ます。

```text
獲得Fort・Throne
残存Mage
Research
Gem income
Army損失
新Border長
```

を比較します。

敵を完全に滅ぼすまで消耗するより、限定目標で停戦し、第三国へ備える方が勝利条件へ近い場合があります。

## Q. Surrender・AI化・放置はどう扱う？

**A.** Lobby ruleへ従い、他Playerへ影響するため無断で決めないでください。

- Surrender可能条件
- AIへ渡すか
- Substituteを探すか
- Gem・Goldを送ってよいか
- Fortを意図的に譲ってよいか
- Throne勝利へ与える影響

をHostへ確認します。

負けが濃厚でも、無断放置はTurn進行とPower balanceを壊します。

## Q. 戦争後、何を記録する？

**A.** 勝敗ではなく、再現可能な原因を残します。

```text
目的：達成 / 未達
Main Battleの最初の崩壊点：
使用Gem：
失ったRare Unit：
Siegeに要したTurn：
敵Counter：
役立ったScout情報：
次のResearch：
新Borderの弱点：
```

勝ったBattleも[Battle Replayの読み方](battle-replay.md)で確認します。

---

# 最初の戦争を五文で書く

開戦前に、次を埋めます。

```text
目的：Border Fort 17を取り、敵Mage生産を一拠点止める。
敵主力：高Protection歩兵、Air Mage、少数Cavalry。
勝利条件：Shock Resistance後、高Damage近接で前衛を破る。
進行：Rally pointへ二Armyを集め、Scout確認後に一Turnで侵攻する。
撤退・終了：敵第二Army合流なら自国Fortへ戻り、Fort取得後は追撃しない。
```

五文にできない場合、

- 目的が曖昧
- 敵情報が不足
- 勝ち方が未完成
- 撤退基準がない

のいずれかです。

---

# 開戦Turn前Checklist

- [ ] GameのDiplomacy設定とNAP状態を確認した
- [ ] Border・Throne・Scout通行の合意を確認した
- [ ] 戦争目的をMap上のFort・Throne・Armyへ落とした
- [ ] 敵Main Army、Mage、移動経路を一度以上Scoutした
- [ ] 第一Research Breakpointを完成させた
- [ ] Caster、Gem、Itemを配備した
- [ ] 主Damageと副Damageがある
- [ ] 前衛、Damage、Commander、Siege、Supplyを確認した
- [ ] Rally pointと同時到着を`Y`で確認した
- [ ] Magic Phase部隊が単独戦闘しないか確認した
- [ ] Retreat Provinceがある
- [ ] Capitalと後方FortのRaid対策がある
- [ ] Stormまで何Turnか概算した
- [ ] 撤退条件と戦争終了条件を書いた
- [ ] 第三国が得る利益を考えた

---

## 関連ページ

- [初心者Q&A](faq.md)
- [初心者Q&A：内政・補給・自動化](logistics-faq.md)
- [操作方法・ショートカット](shortcuts.md)
- [最初の戦争](first-war.md)
- [序盤拡張](expansion.md)
- [Battle Replayの読み方](battle-replay.md)
- [ターン処理順](../reference/turn-resolution.md)
- [Fort・Siege・Storm](../systems/forts.md)
- [命令とBattle Script](../basics/orders.md)
- [戦闘ルール](../basics/combat-rules.md)
- [Researchと研究ルート](../magic/research.md)
- [GemとBlood Slave](../magic/gems.md)
- [Dominion](../systems/dominion.md)
- [Throne of Ascension](../systems/thrones.md)
- [Disciple Game](../systems/disciple-game.md)

## 主な参照先

- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
- Game内のGame Info、Formal Diplomacy、Message、画面別Help（`?`）
