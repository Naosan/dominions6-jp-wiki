---
title: 初心者Q&A
page_type: guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# 初心者Q&A

Dominions 6を始めた人が、実際のPlay中に抱きやすい疑問へ短く答えるページです。

旧Dominions 4 WikiのBeginner Informationと同じく、最初から体系的なManualを読ませるのではなく、

> **今、何が分からないのか**
> → **まず何を確認するか**
> → **詳しくはどの記事を読むか**

という順で探せる構成にしています。

各回答は最初の入口です。国家固有の例外、特殊能力、Turn処理、Spellの細部は、回答末尾の専門記事を優先してください。

!!! warning "Dominions 4 / 5の情報について"
    旧作Wikiの質問の立て方は参考になりますが、数値、研究Level、Magic Path、移動、Mount、Battlefield terrain、国家構成などはDominions 6で変わっています。このページの回答はDom6 6.35と現在のWiki記事を基準にしています。

---

## まず困りやすい十二問

- 何を目標に進めればいい？
- 最初はどの国家を選べばいい？
- Pretender設計が分からない
- Turn 1に何をすればいい？
- どのButton・Keyで操作するの？
- 遠いProvinceへ一度で移動指示を出せる？
- Recruitした兵がArmyにいない
- 雇える兵の種類が多すぎる
- どのIndependent Provinceを攻めればいい？
- 何をResearchすればいい？
- MageがScriptしたSpellを使わない
- 勝ったのに損失が多すぎる

右側のページ内目次から、現在の疑問に近い質問へ移動してください。

---

# ゲームを始める前

## Q. Dominions 6は、結局何をするゲーム？

**A.** Provinceを取り、Gold・Resources・Fort・Mage・Research・Gemを増やし、その国力を戦争とThrone獲得へ変えるTurn制Strategyです。

勝利は敵Armyを一度倒すことではなく、設定された勝利条件を満たすことです。標準的には、敵国を滅ぼす、敵Dominionを消す、必要なAscension Pointを持つThroneをClaimする、という経路があります。

最初は、

```text
偵察する
→ Recruitする
→ Armyを編成する
→ Provinceを取る
→ Replayを見る
→ 一つ修正する
```

という一周を覚えれば十分です。

詳しくは[初心者ガイド](index.md)、[Throne of Ascension](../systems/thrones.md)、[Dominion](../systems/dominion.md)を参照してください。

## Q. 400ページ以上あるManualを全部読まないと遊べない？

**A.** 全部読んでから始める必要はありません。

まず小さめのSingle Player Gameを実際に触り、分からない画面では`?`を押し、疑問が出た部分だけManualとWikiで調べる方が理解しやすくなります。

最初に必要なのは、全数式の暗記ではなく、Recruit、Army Setup、Research、移動、Battle Replayの五つです。[操作方法・ショートカット](shortcuts.md)と[最初の12ターン](first-12-turns.md)をゲームと並べて使ってください。

## Q. 最初のGame設定はどうすればいい？

**A.** 学習目的なら、複雑さを減らします。

- Vanillaで始める
- 陸上の一般的な国家を選ぶ
- AIは標準以下でもよい
- Mapと参加国数を極端に大きくしない
- Disciple、特殊な勝利条件、複雑なMODは後回しにする
- 勝敗より最初の戦争までを一度経験する

AIを弱くすることは失敗ではありません。UI、Expansion、Research、Fort、Replayを一度つなげることが最初の目的です。

## Q. 初心者向けの国家はどれ？

**A.** 「最強国家」より、役割が読みやすく、国家兵だけでExpansionでき、極端な固有Ruleが少ない国家を選びます。

最初は、

- 陸上国家
- 通常Leadershipを使う
- Recruit-anywhereの兵とMageがいる
- 前衛とDamage役を分けやすい
- Blood、Underwater、Population消費、特殊Dominionへ全面依存しない

国家が扱いやすい傾向です。

ただし、興味を持てる国家を選ぶことも重要です。具体的な候補は[国家選択ガイド](../nations/choose-a-nation.md)を参照してください。

## Q. EA・MA・LAは難易度？

**A.** 難易度ではなく時代です。

- EA：Early Age
- MA：Middle Age
- LA：Late Age

同じ名前を持つ国家でも、Ageが違えばRoster、Magic、装備、宗教、国力が大きく変わります。`Ulm`だけでなく、`EA Ulm`、`MA Ulm`、`LA Ulm`として別国家だと考えてください。

## Q. 最初はどんなPretender Godを作ればいい？

**A.** 「単体で最も強い神」ではなく、国家に足りない役割を補う神を作ります。

初回Playでは、次のどれを担当させるか一つか二つに絞ると分かりやすくなります。

- 国家兵でExpansionできないならAwake Expander
- 一般兵とMageが強いならScales
- Sacredが主力ならBless
- 国家Magicが狭いならRainbow・Magic diversity
- 後半のRitual・Globalを担当するCaster

分からない場合は、国家記事のSampleを使うか、経済とResearchを支えるScales寄りの設計から始めます。詳しくは[Pretender God](../pretender/index.md)、[Scales](../pretender/scales.md)、[Bless](../pretender/bless.md)を参照してください。

## Q. Vanillaって何？ MODは最初から入れていい？

**A.** Vanillaは、Gameplayを変えるMODを入れていない標準環境です。

最初の一戦はVanillaにすると、Manual、Wiki、Game内Dataの説明と実際の挙動を一致させやすくなります。UI補助やMapを含め、MODを使う場合は、問題がVanilla仕様なのかMOD変更なのかを区別してください。

---

# 操作とTurn進行

## Q. Turnが始まったら、何から見ればいい？

**A.** 毎Turn同じ順番で確認します。

```text
Message
→ Battle Replay
→ Strategic Map
→ Recruit
→ Research
→ Army SetupとScript
→ Commanderの移動・仕事
→ Gold・Gem・建設
→ End Turn前確認
```

順番を固定すると、重要Message、Mage雇用、Idle Commander、Gem、Retreat routeの見落としが減ります。詳しくは[初心者ガイド](index.md)を参照してください。

## Q. どのShortcutから覚えればいい？

**A.** 最初に覚えるべきKeyは`?`です。

DominionsのShortcutは画面ごとに変わります。Map、Recruit、Army Setup、Battle Replayなど、分からない画面で`?`を押すと、その画面で使える操作を確認できます。

次に、`M`、`R`、`T`、`Space`、`F5`、`E`を一つずつ覚えます。詳しくは[操作方法・ショートカット](shortcuts.md)を参照してください。

## Q. 数Province先の場所へ、一回で移動指示を出せる？

**A.** できます。

Options / PreferencesでMulti-turn movementを有効にし、Commanderを選択して、標準設定では`Alt`を押しながら遠方の目的地ProvinceをClickします。

これは一Turnで遠くまで進む機能ではなく、複数Turn分の経路を予約する機能です。各Turnに経路、Arrow、現在Orderを確認してください。

詳しくは[操作方法・ショートカット：遠い目的地を一度で指定する](shortcuts.md#遠い目的地を一度で指定する)を参照してください。

## Q. 複数Commanderへ同じ移動命令をまとめて出せる？

**A.** できます。

`Ctrl`＋Clickで個別に追加・除外し、`Shift`＋Clickで範囲選択してから目的地を指定します。

ただし、同じ目的地を指定しても、各ArmyのMap MoveとTerrain適性が違えば、経路や到着Turnは揃いません。同時到着が必要なら、中継Provinceで集合させ、`Y`で到着予定Armyを確認します。

## Q. Recruitした兵士がArmyにいない！

**A.** Recruitされた兵士は、自動的に既存Squadへ入るとは限りません。

次Turnに`T`でArmy Setupを開き、画面上部の未配属Poolから兵士を選び、Commanderまたは既存Squadへ割り当てます。

```text
Recruit
→ 次Turnに完成
→ Army Setupで配属
→ Formation・Order・配置を確認
```

までが一つの作業です。

## Q. Commanderを動かしたのに兵士が付いてこない

**A.** その兵士が本当にCommanderのSquadへ配属されているか確認します。

よくある原因は、

- 未配属Poolに残っている
- 別CommanderのSquadにいる
- Leadership上限を超えている
- Undead、Demon、Magic Being等のLeadership typeが合わない
- Commanderだけに別の移動Orderを出した

です。

Army SetupとCommanderのSquad表示を確認してください。

## Q. 部隊へ入れられないUnitがいるんだけど？

**A.** Leadershipの種類かSquad制限を確認します。

通常兵、Undead、Demon、Magic Beingなどは、必要なLeadershipが異なります。Mindless等の特殊能力を持つUnitには、Squadの混成や指揮方法に追加制限がある場合があります。

CommanderのLeadership詳細とUnitの特殊能力を右Clickで確認し、[特殊能力](../reference/special-abilities.md)も参照してください。

## Q. `T`と`Y`は何が違う？

**A.** `T`は現在そのProvinceにいるArmy、`Y`はそのProvinceへ到着予定のArmyを編成します。

複数方向から同時に移動するArmy、合流戦、Teleport等を含む到着予定編成では`Y`が重要です。

```text
T：今いるArmy
Y：次に到着するArmy
```

と覚えてください。

## Q. 一部のCommanderへ命令するのを忘れる

**A.** End Turn前にNation Overviewと警告設定を使います。

- `F1`でCommanderと所在地を一覧確認する
- OptionsのWarn on End Turnを使う
- 新規Commanderへの自動Orderを必要に応じて設定する
- Idleである理由を一人ずつ説明できるか確認する

何もしていないCommanderが必ず失敗とは限りません。待機、迎撃、退却先確保など、意図したIdleかどうかを区別します。

## Q. 毎Turn同じRecruitとScriptを設定するのが大変

**A.** Repeat RecruitmentとScript保存を使えます。

Repeat Recruitmentは同じRecruit Queueを継続し、`Ctrl`＋`1`～`9`と`1`～`9`はBattle Scriptの保存・貼り付けに使えます。

ただし自動化は確認を不要にする機能ではありません。GoldをFort用に貯めるTurn、CasterのPathやGemが違うArmy、敵構成が変わった戦闘では設定を見直します。

## Q. End Turnを押した後に戻せる？

**A.** 戻せない前提で操作してください。

Single PlayerとMultiplayer、Host前後、Game設定で状況は異なりますが、提出後に安全に撤回できることを期待しない方がよいです。

```text
Message
Recruit
Research
Commander Order
Multi-turn route
Army Setup
Gold・Gem
```

を確認してから`E`を使います。

---

# 序盤拡張と経済

## Q. Turn 1は何をすればいい？

**A.** Recruit、Research、Expansion、偵察の四つを同時に起動します。

- Capitalの兵・Commander・Mageを役割別に見る
- Recruit Queueを設定する
- Prophet方針を決める
- 最初のResearch Breakpointを一つ決める
- 初期Armyの配置とOrderを確認する
- Scoutへ命令を出す
- 最初の攻撃先と退却先を確認する

具体的な順番は[最初の12ターン](first-12-turns.md)を参照してください。

## Q. 偵察情報を見ても、どこを攻めればいいか分からない

**A.** 人数ではなく、自軍と相手の役割・装備・Damageの相性を見ます。

特に、

- Cavalry・Lance
- Barbarian等の高Damage兵
- Crossbow
- Heavy Infantry
- Trampleする大型Unit
- Poison
- Undead

は、人数だけでは危険度を判断しにくい相手です。

「勝てるか」だけでなく、「交換不能なUnitを何体失うか」「負けたときにどこへ退却するか」も考えます。詳しくは[序盤拡張](expansion.md)を参照してください。

## Q. 偵察報告と実際の敵が違った！

**A.** 偵察情報は完全なRoster一覧ではありません。

誤差、少数Unitの見落とし、Stealth・Glamour、同Turnの増援、特殊能力などにより、見えていなかった敵が戦闘へ参加することがあります。

Scoutを現地または周辺へ置き、

```text
確認済み
推定
不明
```

を分けます。不明を都合よく「いない」と扱わないことが重要です。

## Q. 地形は気にするべき？

**A.** 気にするべきです。

Terrainは、

- IncomeとResources
- Supply
- Map Move Cost
- Fort候補
- Magic Site傾向
- Battlefield terrain
- Survival能力
- 海・洞窟・別Planeへの進入

へ影響します。

同じ距離でも、Army構成によって到着Turnが変わります。`Ctrl`＋`M`でMap Move Costを表示し、[Province](../systems/province.md)も参照してください。

## Q. 洞窟・地下・別Planeへ入ったら急に苦戦した

**A.** 地上の平地と同じ条件だと考えないでください。

進入条件、移動Cost、Darkness、Battlefield terrain、退却先、補給、現地Unitの適性などが変わる場合があります。

まず小規模な偵察とReplayで条件を確認し、Darkvision、Terrain Survival、Amphibious等の関連能力を右Clickで調べます。Dom6では複数Planeもあるため、入口と退路を作戦の一部として扱います。

## Q. 雇える兵の種類が多すぎる！ どれを使えばいい？

**A.** 総合的な「強さ」ではなく役割で選びます。

- 最初に接敵するLine holder
- 敵防御を破るDamage dealer
- 攻撃と時間を買うChaff
- 接敵前に削るArcher
- 後衛・側面を狙うFlanker
- Siege・補給を担うUnit

一種類だけで全部を担当させるより、前衛とDamage役を分ける方が改善点を見つけやすくなります。[国家ページの読み方](../nations/how-to-read.md)と[初心者向けTips](beginner-tips.md)を参照してください。

## Q. Armyを率いるCommanderはどれを使えばいい？

**A.** Leadershipの数値だけでなく、種類、Map Move、生存性、Cost、Commander Pointを見ます。

重い歩兵を率いるArmyと、騎兵・飛行・Stealth Armyでは必要なCommanderが違います。Rare Mageを単なる運搬役として危険に晒すより、安価な専任Commanderを使った方がよい場合もあります。

## Q. 勝ったけど損失が多すぎる。勝利扱いでいい？

**A.** Provinceを取っても、補充不能なUnitを失ったなら高すぎる勝利です。

特に、

- 初期Commander
- Rare Mage
- Capital-only Sacred
- Awake Pretender
- Booster・大量Gemを持つCaster

の損失は、戦闘画面の勝敗表示以上に大きな影響を持ちます。

Replayで最初に崩れた場所を探し、次の戦闘では変更を一つだけ試します。[Battle Replayの読み方](battle-replay.md)を参照してください。

## Q. 第二Expansion Armyはいつ作る？

**A.** 兵数が一定に達したときではなく、二つのArmyがそれぞれ安全な標的を持てるときです。

Commander、Leadership、前衛、Damage役、Bless役、補充経路が揃っているか確認します。一軍を半分に割って両方とも何も倒せなくなるなら、まだ分ける時期ではありません。

## Q. 第二Fortはいつ、どこへ建てればいい？

**A.** Expansionが安定し、建設資金を確保しても主力ArmyとMage生産が止まらない頃が目安です。

場所は、

- Mage・国家兵の生産価値
- Resources
- Income
- Capitalと前線の距離
- 増援路
- Choke point
- Throne・重要Site
- 防衛可能性

で比較します。

Fortは壁だけでなく、毎TurnのCommander Point、Mage、兵、Resourcesを増やす生産装置です。[Forts](../systems/forts.md)を参照してください。

## Q. GoldもResourcesもあるのにRecruitできない！

**A.** Recruitには複数の制約があります。

- Recruitment Points
- Commander Points
- Holy Points
- Capital-only / Recruit limit
- Fort、Lab、Templeの有無
- Unrest
- 特殊な国家・Site条件

兵士QueueとCommander Queueも別です。Recruit画面で不足している項目を確認し、単にGoldだけを増やそうとしないでください。

## Q. Province Defenceはどれくらい上げればいい？

**A.** 固定の正解値はありません。

Province Defenceは、Scout・小規模Raidへの抵抗、敵情報の取得、CommanderやFortへの時間稼ぎには使えますが、主力Armyの代わりではありません。

高価なPDへGoldを入れる前に、

- そのProvinceを守る価値
- 敵Raidの規模
- Fort・Choke point
- 近くの反撃Army
- PDで何Turn買えるか

を考えます。

## Q. Goldは毎Turn使い切るべき？

**A.** 使い切ることも、貯め続けることも目的ではありません。

Goldを、

```text
今のArmyとMage
＋ 数Turn後のFort・Lab・Temple
＋ 緊急予備
```

へ分けます。

Repeat Recruitmentを使っている場合、建設資金を貯めるTurnにQueueを止め忘れないようにします。

## Q. 敵Armyを追っても追っても捕まえられない

**A.** Dominionsの移動は同時解決であり、敵の現在地へ行くだけでは捕まらないことがあります。

敵が次に欲しいProvince、退却路、Fort、Choke pointを予測し、自領側で迎撃する方が確実な場合があります。Scoutで周辺Provinceまで見て、複数出口を持つ敵を一本のArmyだけで追い回さないようにします。

Turn処理の詳細は[ターン処理順](../reference/turn-resolution.md)を参照してください。

## Q. 敵Provinceへ入ったのに戦闘しなかった

**A.** Stealthy CommanderがSneakしている、相手が同Turnに移動した、進入・Battleの処理が想定と違った、という可能性があります。

Stealthy Armyで通常侵攻したい場合は、Map画面の`?`で通常移動の指定方法を確認し、CommanderのOrder表示を見ます。移動Arrowだけでなく、`Move`、`Sneak`等の命令名を確認してください。

## Q. 侵攻を指示したArmyが動かず、防衛戦になった

**A.** 敵の同時移動、途中Battle、移動条件、経路変更などにより、予定どおり移動しない場合があります。

複数Armyの同時侵攻では、一部だけが到着して各個撃破されるRiskがあります。同時到着が絶対条件なら、自領の集合地点へ一度集め、`Y`で到着予定編成を確認してから攻めます。

## Q. Fortの包囲が長すぎる！

**A.** Field Battleに勝つ力と、Fortを破るSiege能力は別です。

ArmyのSiege strength、Unit数とSize、Engineer、Fort defence、守備側の修復、Supply、敵のRelief Armyを確認します。

戦争計画には、敵主力を倒すArmyだけでなく、Fortを破り、Stormし、後方を守る能力も含めます。[Forts](../systems/forts.md)と[最初の戦争](first-war.md)を参照してください。

## Q. 海へはどうやって侵攻する？ 船は必要？

**A.** 通常の陸上Armyは、そのまま海へ入れません。

Amphibious、Aquatic、Water Breathing、Sailing、特殊移動、Item、Ritual等の手段を確認します。Commander本人だけが海へ入れても、率いる兵が入れなければArmy全体は移動できません。

海への侵攻は最初の一戦で無理に覚えず、陸上Gameで基本を学んでからでも構いません。

## Q. 線がないProvinceや別Planeの場所へどうやって行く？

**A.** 通常接続だけでは入れないProvinceには、Plane入口、特殊接続、Terrain条件、Ritual、Teleport等が必要な場合があります。

Map filterとProvince情報を確認し、見た目だけで「隣だから歩ける」と判断しないでください。進入だけでなく、退却・補給・Claim担当の移動手段も同時に準備します。

---

# Mage・Research・Gem

## Q. Mageは何をしていればいい？

**A.** 全員を一つの役割へ固定せず、役割を分けます。

- Researcher
- Battle caster
- Site Searcher
- Forger
- Ritual caster
- Rare Path holder
- Communion master / slave

序盤は多くのMageがResearchを担当しますが、最初の戦争へ必要なCaster、Site Searcher、Forgerを少数ずつ抜きます。Rare Pathを通常Evocationの一人として失わないようにします。

## Q. 何をResearchすればいい？

**A.** School名ではなく、誰が何に使うかから決めます。

```text
Spell / Item：
使用Mage：
倒す対象・解決する問題：
必要Gem：
使用予定Turn：
```

「Evocationを何となく上げる」より、「このMageがこのSpellで敵の高Protection兵を倒す」のようにBreakpointを定義します。[Researchと研究ルート](../magic/research.md)を参照してください。

## Q. MageがScriptしたSpellを使ってくれない

**A.** Script入力ミスとは限りません。

- Researchが完成しているか
- CasterのMagic Pathが足りるか
- Gemがあるか
- Fatigueが高すぎないか
- Range内に有効Targetがいるか
- Battlefield条件を満たすか
- Spell AIが別の合法行動へ切り替えたか

を確認します。

Replayを止め、CasterのFatigue、Gem、位置、実際に唱えたSpellを見ます。[命令とBattle Script](../basics/orders.md)を参照してください。

## Q. Gemは何の役に立つ？

**A.** Gemは、Battle Spell、Ritual、Summon、Forge、Booster、Global、Empowerment等へ使うMagic資源です。

単なる貯金ではなく、国家のResearchを実戦へ変換する燃料です。何に使うか決めずに大量に前線Casterへ持たせると、Rout、暗殺、死亡で失うRiskも増えます。

詳しくは[Gem](../magic/gems.md)を参照してください。

## Q. Gemは貯めるべき？ すぐ使うべき？

**A.** 次の戦争を変える用途があるなら使い、まだ技術・Caster・目的がないなら残します。

比較する候補は、

- Site Search
- Booster
- Battle Spell
- Summon
- Resistance Item
- Global

です。

「余っているから使う」「怖いから永久に貯める」ではなく、何Turn後に何へ使うかを決めます。

## Q. Magic Siteはどうやって見つける？

**A.** Mageによる手動Search、遠隔Site Search Ritual、特殊能力等を使います。

すべてのProvinceを全Pathで調べるのはCostが高いため、Terrain、国家Path、未探索範囲、期待するGem、前線Riskで優先順位を付けます。

詳しくは[Site Search](../magic/site-search.md)と[Site Search実戦手順](../magic/site-search-playbook.md)を参照してください。

## Q. Magic Itemは何に使えばいい？

**A.** 最初は、役割を一つ解決するItemから使います。

- BoosterでSpell・Forgeへ到達する
- Resistanceで敵Damageへ対策する
- Research Itemで研究を加速する
- Supply・移動を補助する
- Thug / SCの防御層を作る

Itemを一式付けただけでCommanderが無敵になるわけではありません。敵のMagic Weapon、AN、MR attack、Fatigue、Soul attack等に対する穴を確認します。

[アイテム](../items/index.md)と[Magic Boosting](../magic/boosting.md)を参照してください。

## Q. Researchを早くするには？

**A.** 一人の高価なMageだけでなく、毎Turn雇えるMage数とFort数を見ます。

- Mage雇用を継続する
- 第二Fort以降でMage生産拠点を増やす
- Commander Pointを無駄にしない
- Research bonusとCostを比較する
- Research ItemをGem投資として評価する
- 前線へ出すMage数を目的付きで決める

Research速度はMageの能力だけでなく、生産拠点の数で決まります。

## Q. Communionは最初から覚えるべき？

**A.** 最初の一戦ですべて覚える必要はありません。

Communionは、複数MageでMagic PathとFatigue負担を共有し、高位Spellへ到達する仕組みですが、Slave死亡やFatigue崩壊のRiskがあります。

まず通常の五枠Script、Gem、Range、Fatigueを理解し、国家がAstralやCommunionへ強く依存する場合に[Communion](../magic/communions.md)へ進んでください。

## Q. Glamourって何？ 旧作のAirやIllusionと違う？

**A.** GlamourはDominions 6で追加されたMagic Pathです。

Illusion、Dream、Luck、Stealth、認識操作等に関わり、旧作のAirや他Pathにあった一部の役割が再編されています。Dom4 / Dom5のSpell・国家記事を読むときは、Pathが同じだと仮定しないでください。

[Dominions 5からの変更点](../reference/dom5-to-dom6.md)と[Glamour](../magic/paths/glamour.md)を参照してください。

---

# BattleとReplay

## Q. 高Protection兵なのに、すぐ死ぬのはなぜ？

**A.** Protectionは防御層の一つにすぎません。

Unitは、

```text
攻撃させない
→ 命中させない
→ Shieldで受ける
→ Protection / Resistanceで軽減する
→ HP・Regenerationで耐える
→ MoraleとFatigueで戦い続ける
```

という複数層で生き残ります。

Poison、Shock、AN Damage、MR attack、高Damage武器、Fatigue等は、Protectionだけでは止まりません。[戦闘ルール](../basics/combat-rules.md)を参照してください。

## Q. Archerを増やしたのに敵へDamageが通らない

**A.** 射撃は、敵のShield、Protection、Range、命中、Formation、Battlefield obstacleの影響を受けます。

Shieldと重装備を持つ敵へ低Damage射撃だけを増やしても、効率が上がらないことがあります。軽装・密集・大型Targetを狙う、Crossbow等の高Damageを使う、近接Damageと組み合わせるなど、役割を変えます。

## Q. Archerが味方を撃っている！

**A.** 接敵後も射撃を続けると、Friendly Fireが発生します。

射線、Target order、Range、味方と敵の密集、射撃を止めるTimingを確認します。Archerを置くだけでなく、どの敵を何Roundまで狙うかをScriptの一部として考えてください。

## Q. Commanderがすぐ死ぬ

**A.** Commanderの配置、射撃、Flank、Flying、Attack Rear、AoE、Bodyguardを確認します。

後方に置くだけでは安全とは限りません。全Commanderを同じ場所に重ねると、一つの突破やAoEで同時に失うRiskがあります。

Commander死亡はLeadership、Script、Gem、Item、Retreatをまとめて失うため、兵士一体より大きな損害です。

## Q. 兵が残っているのにArmyがRoutした

**A.** Routは全滅だけで起こるものではありません。

Morale、Army全体の損失、Commander死亡、Fear、Fatigue、孤立、特殊効果等が重なると、まだ兵が残っていても退却します。

Replayで、最初にMoraleが崩れたSquad、Commanderの状態、敵Fear source、損失が急増したRoundを確認します。

## Q. Fatigue 100って何が問題？

**A.** Fatigueが増えると戦闘能力が低下し、100付近では行動不能になりやすく、その後は非常に危険になります。

重装備、Spell、長期戦、Heat / Cold、特殊能力等がFatigueへ影響します。高Protection兵でも、敵を倒せず疲れ切れば防御が崩れます。

Mageでは、一Spellを唱えられるかだけでなく、その後何Round戦えるかを考えます。

## Q. APとANは何が違う？

**A.** どちらもArmorへの対処ですが、同じではありません。

- AP：Armor Piercing。Protectionの効果を弱める
- AN：Armor Negating。通常のArmor Protectionを無視する

ただしResistance、Magic Resistance、Shield、特殊防御等が別に働く場合があります。表示されたDamage属性と防御層を確認してください。

## Q. `Attack Closest`だけではだめ？

**A.** 全部隊を`Attack Closest`にすると、最も近いScreenへ全戦力を使い、Archer、Cavalry、Large Monster、Rear等の重要Targetを放置することがあります。

Squadの役割に応じてTarget orderを分けます。ただしOrderは絶対命令ではなく、距離、経路、敵位置、Battlefield terrainで結果が変わるため、Replayで確認します。

## Q. 勝ったBattle Replayも見る必要がある？

**A.** あります。

勝利していても、

- Rare Unitを失った
- Commanderが危険な位置へ出た
- Mageが予定Spellを使わなかった
- Gemを不要に使った
- 一SquadがRoutした
- 敵にResistanceがなかっただけ

という場合があります。

勝利は、Script全体が正しかった証明ではありません。[Battle Replayの読み方](battle-replay.md)を参照してください。

## Q. 負けた後、何を変えればいい？

**A.** 全部を一度に変えず、最初の崩壊点を一つ直します。

```text
盾兵よりDamage役が先に接敵した
→ 配置を変更する

Buff前に敵が到着した
→ 全体を後ろへ下げる

Shockで崩れた
→ Resistanceを用意する
```

最後の全滅場面ではなく、計画が最初に壊れた瞬間を探してください。

---

# Dominion・Throne・状態異常

## Q. Mapの白いCandleと黒いCandleは何？

**A.** Provinceの所有者ではなく、その土地でどのPretenderがどれだけ信仰されているかを表すDominionです。

```text
旗：Province所有者
Candle：Dominion
Scales：現在の環境
```

は別です。

自領でもEnemy Dominionになることがあり、世界から自国Candleが消えると、ArmyやFortが残っていても敗北します。[Dominion](../systems/dominion.md)を参照してください。

## Q. Templeを建てたのに、すぐCandleが増えない

**A.** TempleはDominionを広げるSourceですが、建てた瞬間に前線のCandleが最大になるわけではありません。

Passive spread、Preach、敵Dominionとの競合、Temple数、特殊国家Rule、Turn処理Timingが関係します。緊急にLocal Dominionを変えたい場合はPriestのPreachが意味を持つことがあります。

## Q. Prophetは誰にすればいい？

**A.** Holy levelだけでなく、どこで何を担当するかを見ます。

- Expansion Armyへ同行してBlessする
- Preachする
- ThroneをClaimする
- Battle Sermon等を使う
- 死なずに前線へ届く

Rare Mageや失いたくないCommanderを安易にProphetへして前列へ置かないようにします。最初のTurnで方針を決め、任命を忘れないことが重要です。

## Q. Throneを占領したのに勝利Pointが増えない

**A.** Province占領とThrone Claimは別です。

Claim可能者をThroneへ置き、Claim orderを実行する必要があります。通常、Pretender、Disciple、H3以上のPriestがClaimできます。Prophetは通常H3になるためClaim担当にできます。

Claim担当はTurn提出時点ですでにThroneへいる必要があり、歩いて到着した同TurnにClaimすることは通常できません。[Throne of Ascension](../systems/thrones.md)を参照してください。

## Q. Pretenderが死んだ！ もう負け？

**A.** Pretender死亡だけで、即座に国家が消滅するとは限りません。

自国Dominionが残っていれば国家は続き、PriestによるCall God等で復帰を進められる場合があります。ただし、Pretenderの戦闘力、Magic、Forge、Incarnate Bless、Dominion戦力を長期間失うため重大な損害です。

復帰方法と影響はChassis、Immortality、特殊能力、Game状態で異なるため、PretenderとOrderのTooltipを確認してください。

## Q. 敵Dominionが自領へ広がってきた。何をすればいい？

**A.** Candleだけを局所的に押し返す方法と、発生源を減らす方法を分けます。

- Templeを増やす
- PriestでPreachする
- 敵Temple・Throne・宗教拠点を奪う
- Enemy Dominion下でのPretender戦を避ける
- 自国Candleが消えそうな地域を優先する

Preachだけで敵のTemple Network全体に勝とうとせず、領土戦と宗教戦を接続します。

## Q. いきなりDiseaseになった。なぜ？

**A.** Old Age、Affliction、Poison、Event、Magic Site、Supply不足、国家・Dominion効果、敵工作等の可能性があります。

Message、Province履歴、UnitのAge・Affliction・特殊能力、滞在Provinceを確認します。原因が不明なまま重要Mageを同じProvinceへ集め続けないようにします。

## Q. Afflictionは放っておけば治る？

**A.** 多くは自然に簡単には治りません。

Healer、Disease Healer、Spell、Item、Global、特殊Site・国家能力等が必要になる場合があります。治療手段がないなら、重要任務から外す、後方任務へ回す、Riskの高い装備を渡さない、といった役割変更も必要です。

## Q. 老齢のMageは使わない方がいい？

**A.** 直ちに使えないわけではありませんが、DiseaseとAfflictionのRiskを生産計画へ入れます。

Rare Pathの老齢Mage一人だけに国家のBooster・Global計画を依存すると、突然の病死で技術経路が消えます。代替Caster、Item、Summon、Pretender accessを準備します。

---

# Multiplayerと学び方

## Q. 最初からMultiplayerへ参加してもいい？

**A.** 参加できますが、Single Playerにはない要素が増えます。

- 外交
- Turn期限
- 境界交渉
- Bluffと偵察妨害
- 人間によるCounter
- 一度提出したTurnの重さ

最初にSingle PlayerでRecruit、Army Setup、Research、Fort、Replayを一度触っておくと、Multiplayerで外交と戦略へ集中しやすくなります。

## Q. Dominions 4 / 5 Wikiの記事はそのまま使える？

**A.** 考え方の参考にはなりますが、そのまま現行仕様とは扱えません。

特に、

- SpellとResearch Level
- Magic Path
- Glamour
- Mount
- Battlefield terrain
- Resistance
- 国家Roster
- Item
- Throne・Turn処理

は版差を確認してください。

旧記事からは「何を調べるべきか」を学び、数値と現行挙動はDom6 Manual、Game内表示、このWikiの6.35記事で確認します。

## Q. 全Unit・Spell・Itemを暗記する必要がある？

**A.** ありません。

必要なのは、問題を正しい索引へ分けることです。

```text
兵が死ぬ
→ Damage typeと防御層

Mageが使えない
→ Research・Path・Gem・Fatigue

国力が伸びない
→ Fort・Mage生産・Gold配分
```

一つの国家と一つの研究ルートを使い、必要になったときに検索する方が学びやすくなります。

## Q. 情報が多すぎて、どの記事を読めばいいか分からない

**A.** 症状から入口を選びます。

| 今困っていること | 最初に読むページ |
|---|---|
| Button・Key・移動・編成 | [操作方法・ショートカット](shortcuts.md) |
| 最初のTurnの順番 | [最初の12ターン](first-12-turns.md) |
| Independentに大損する | [序盤拡張](expansion.md) |
| 国家Rosterが読めない | [国家ページの読み方](../nations/how-to-read.md) |
| Research目標がない | [Researchと研究ルート](../magic/research.md) |
| MageがScriptどおり動かない | [命令とBattle Script](../basics/orders.md) |
| Damage原因が分からない | [戦闘ルール](../basics/combat-rules.md) |
| 敗戦を分析したい | [Battle Replayの読み方](battle-replay.md) |
| Fortと生産拠点を増やしたい | [Forts](../systems/forts.md) |
| 最初の対人戦争を準備したい | [最初の戦争](first-war.md) |
| Candle・宗教戦が分からない | [Dominion](../systems/dominion.md) |
| Throneを取ったのに勝てない | [Throne of Ascension](../systems/thrones.md) |

## Q. 初回Gameの成功条件は勝つことだけ？

**A.** 勝利以外にも学習上の成功があります。

- 二つ目のExpansion Armyを作った
- 第二Fortを建てた
- Mage生産を増やした
- 目的付きのResearch Breakpointを選んだ
- Squadごとに役割とOrderを分けた
- Replayから最初の崩壊原因を説明した
- 次のBattleで変更点を一つ試した

「なぜ勝ったか、なぜ負けたか」を一つ説明できれば、次の国家でも改善できます。

---

## 関連ページ

- [初心者ガイド](index.md)
- [操作方法・ショートカット](shortcuts.md)
- [初心者向けTips](beginner-tips.md)
- [最初の12ターン](first-12-turns.md)
- [序盤拡張](expansion.md)
- [最初の戦争](first-war.md)
- [Battle Replayの読み方](battle-replay.md)
- [国家選択ガイド](../nations/choose-a-nation.md)
- [命令とBattle Script](../basics/orders.md)
- [戦闘ルール](../basics/combat-rules.md)

## 主な参照先

- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
- [Dominions 4 Wiki - Beginner Information](https://wikiwiki.jp/dominions4/Beginner%20Information)（質問構成の参考。回答内容はDom6用に再構成）
