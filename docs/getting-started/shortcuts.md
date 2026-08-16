---
title: 操作方法・ショートカット
page_type: guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# 操作方法・ショートカット

Dominions 6は、画面上のButtonだけでも遊べます。しかし、Strategic Map、Recruit、Army Setup、Research、Battle Replayでは操作方法が変わるため、最初は「何をクリックすればよいか」が分かりにくいゲームです。

このページでは、単なるKey一覧ではなく、**一Turnを進める操作順、遠距離移動、複数Commanderへの一括命令、Mouse操作、画面別Shortcut、よくある誤操作**をまとめます。

!!! warning "最も重要な操作は `?`"
    Dominions 6のShortcutは画面ごとに変わります。分からない画面では、まず`?`を押してください。その画面で使えるShortcut一覧が表示されます。Keyboard配列によっては`Shift`＋`/`で`?`を入力します。

!!! note "表記とVersion"
    このページはDominions 6.35を基準にしています。本文と画面内Helpが異なる場合は、現行Game内の`?`表示とOptions / Preferencesの説明を優先してください。

---

# 遠い目的地を一度で指定する

## Multi-turn movement

数Province先へ移動するたびに、毎Turn隣接Provinceを指定し直す必要はありません。

Options / Preferencesで **Multi-turn movement** を有効にすると、通常の移動操作で遠方Provinceを最終目的地として指定できます。Gameが経路を作り、Commanderと同行Armyは複数Turnかけて目的地へ向かいます。

```text
Options / Preferencesを開く
→ Multi-turn movementを有効化
→ Commanderを選択
→ 数Province先の目的地を指定
→ Map上の経路・Arrow・最終目的地を確認
```

これは一Turnで瞬間移動する機能ではありません。実際に一Turnで進める距離は、Commanderと同行UnitのMap Move、Terrain、Road、River、Water、Flyingなどの移動条件で決まります。

!!! tip "この機能の使いどころ"
    後方から前線への増援、Scoutの長距離移動、Mageの集結、Fort間の定期移動など、途中で命令を変える可能性が低い移動に向いています。

!!! warning "戦争中は自動操縦にしない"
    敵Army、Province所有者、包囲、Terrain、Plane接続、途中のBattleによって計画が崩れることがあります。Multi-turn routeを設定していても、各Turnに経路と現在Orderを確認してください。新しい命令を出すと、以前の経路は置き換えられます。

## 複数Commanderを同じ場所へまとめて動かす

複数Commanderへ同じ移動命令を一括で出すこともできます。

```text
最初のCommanderを選択
→ `Ctrl`＋Clickで個別に追加・除外
  または`Shift`＋Clickで範囲選択
→ Modifier keyを離す
→ 目的地Provinceを指定
→ 全CommanderのArrowとOrderを確認
```

選択されたCommanderは白く強調され、同じ命令を受けます。移動だけでなく、状況に応じて同じStrategic orderをまとめて設定するときにも使えます。

ただし、これはCommanderを一つの恒久的なGroupへ統合する機能ではありません。各Commanderが率いるArmyの移動能力が違えば、Multi-turn movementで別経路を選んだり、到着Turnがずれたりすることがあります。

```text
同じ目的地を指定した
≠
同じ速度・同じ経路・同じTurnに到着する
```

同時到着が重要な場合は、前線の一歩手前を集合地点にし、到着後に`Y`で編成を確認してから最終移動を出します。

!!! warning "Stealthy Commander"
    Stealthy Commanderでは、Provinceを`Ctrl`＋ClickするとSneakではなく通常移動を指定する場面があります。複数選択に`Ctrl`を使った後は一度Keyを離し、目的地を通常Clickしてください。意図した移動種別になっているかOrder表示を確認します。

## Map Move Costを表示する

`Ctrl`＋`M`で、Map上に移動Costを表示できます。

目的地へ届くか分からないときは、UnitのMap Move値だけで判断せず、実際の経路Costを見ます。Terrainや敵領、移動能力によって同じ距離でもCostは変わります。

## Province番号への移動と画面移動を区別する

`G`または`#`でProvince番号を指定する操作は、主に**Mapの表示位置をそのProvinceへ移す操作**です。選択Commanderへ移動Orderを出したことにはなりません。

```text
Mapを目的地へ移した
→ 画面が移動しただけ

Commanderを選択して目的地を指定した
→ 移動ArrowとOrderが出る
```

遠方Provinceを表示した後は、Commanderが選択されたままか、移動Arrowが出たか、最終目的地が正しいかを確認します。

---

# 初心者向け推奨Options

最初のGameを始める前に、Options / Preferencesを一度確認します。項目名や配置がVersion・Platformで少し異なる場合があります。

| 設定 | 初心者向けの意味 |
|---|---|
| Multi-turn movement | 遠方の最終目的地を一度で指定する |
| Warn on End Turn | Idle Commanderなどの見落としを警告する |
| Give Orders to new commanders automatically | 新規Mageなどを自動でResearch等へ割り当て、放置を減らす |
| Magic Path and Map Move tokens for commanders | Commander一覧からPathと移動能力を読みやすくする |
| Right Click to Move | 一般的なStrategy Gameに近いMouse操作へ切り替える。好みで選ぶ |

`Right Click to Move`を変更すると、左Clickと右Clickの役割が本文の説明と逆になる場合があります。自分の設定を把握し、画面内Helpを基準にしてください。

---

# 最初に覚える九つ

| 操作 | Key / Mouse | 何ができるか |
|---|---|---|
| 画面別Help | `?` | 現在の画面で使えるShortcutを表示する |
| 詳細確認 | 右Click | Unit、Commander、Spell、Item等の詳細を見る |
| Message | `M` | 戦闘、Event、建設、発見など今Turnの結果を読む |
| Recruit | `R` | 選択ProvinceのRecruit画面を開く |
| Army Setup | `T` | 選択Provinceに現在いるArmyを編成する |
| 複数Commander選択 | `Ctrl`＋Click / `Shift`＋Click | 個別追加・除外、または範囲選択を行う |
| Commander命令 | `Space` | 選択Commanderの命令Menuを開く |
| Research | `F5` | Research画面を開く |
| End Turn | `E` | Turnを提出し、次の処理へ進む |

`E`は最後に使います。Recruitの`R`と近いため、慣れるまでは画面右上のEnd Turn Buttonを使っても構いません。

---

# Mouse操作と選択の基本

## 左Click：選択と実行

標準設定では、Map上でCommanderを選び、目的地ProvinceをClickして移動Orderを出します。各画面ではButton、Unit、Squad、命令を選びます。

```text
Commanderを選択
→ 目的地Provinceを指定
→ Map上のArrowとCommanderのOrder表示を確認
```

`Right Click to Move`を有効にしている場合は、移動指定に使うButtonが変わります。

## 右Click：詳細を見る

Unit、Commander、Spell、Magic Itemなどは、名前やIconを右Clickすると詳細を確認できる場面が多くあります。

初心者は、知らないUnitをすぐ閉じず、少なくとも次を見ます。

- HP、Protection、Defence、Magic Resistance
- WeaponとDamage type
- Map Move
- Magic Path
- Leadership
- 特殊能力
- Affliction

右Clickは「命令を出す操作」だけでなく、**対象が何者か確認する操作**として覚えます。

## Commanderを複数選択する

| 操作 | 効果 |
|---|---|
| `Ctrl`＋Click | Commanderを一人ずつ選択へ追加、または選択から除外 |
| `Shift`＋Click | 最初と最後の間に並ぶCommanderを範囲選択 |
| `Enter` | 選択を解除 |
| `<` / `>` | Map左側のCommander tokenを縮小・拡大 |
| `?` | 現在のCommander選択Shortcutを確認 |

Mageだけ、Scoutだけ、同じArmyのCommanderだけをまとめて選び、同じ目的地やOrderを出すと操作量を減らせます。

## Army SetupでUnitをまとめて選ぶ

| 操作 | 効果 |
|---|---|
| Double Click | 同じ種類のUnitをまとめて選択 |
| `Shift`＋Click | 一定範囲のUnitをまとめて選択 |
| Drag box | 複数CommanderやSquadの配置Boxを囲んでまとめて選択・移動 |
| `Enter` | 選択解除 |
| `?` | Army Setup専用Shortcutを表示 |

Drag boxは、複数のCommanderやSquadを同じ距離だけ後方へ下げたいときに便利です。

## Esc：閉じる・戻る

PopupやMenuを閉じたいときは`Esc`を使います。画面によって動作が異なるため、閉じない場合は画面内のBack / Exit Buttonを使います。

---

# 一Turnの操作順

## 1. Messageを開く

`M`でMessage画面を開きます。

- Battle結果
- Commanderや重要Unitの死亡
- Event
- Magic Site発見
- Fort、Lab、Templeの建設完了
- RitualやForgeの結果
- Multiplayerの外交Message

を確認します。Battle MessageからReplayを開き、勝った戦闘も一度は見ます。

## 2. Strategic Mapを確認する

Arrow KeyでMapを移動し、`Page Up` / `Page Down`でZoomを調整します。`Home`でCapital付近へ戻れます。

Provinceを選択して、

- 所有者
- IncomeとResources
- Fort、Lab、Temple
- Dominion
- 接続Province
- 見えている敵Army
- 自軍Commander
- Retreat先

を確認します。

## 3. Recruitを設定する

Provinceを選択し、`R`でRecruit画面を開きます。

兵士とCommanderのQueueを分け、Gold、Resources、Recruitment Points、Commander Points、Recruit limitのどれが不足しているかを見ます。

Recruit画面ではArrow Keyや`Ctrl`＋Arrow KeyでFort・Recruit可能Provinceを順番に切り替えられる場合があります。正確な対象と方向は、その画面で`?`を押して確認してください。

## 4. Researchを設定する

`F5`でResearch画面を開きます。

Schoolを均等に上げるのではなく、次に使うSpellやItemのBreakpointへResearchを集めます。変更後は、予定SpellのSchoolとLevelをもう一度確認します。

## 5. Army Setupを行う

選択Provinceに現在いるArmyは`T`で編成します。

1. 画面上部の未配属Unitを選ぶ
2. CommanderのPortraitまたは既存Squadへ割り当てる
3. FormationとBattle orderを設定する
4. 緑色の配置BoxからBattlefield上の開始位置を決める
5. CommanderのSpell ScriptとMain orderを設定する
6. Leadership、Squad数、Unit数の上限を確認する

移動先で合流するArmyを組みたい場合は、Map画面の`Y`を使います。`T`は現在いるArmy、`Y`は選択Provinceへ到着予定のArmyを扱います。Dominions 6では、`Y`の到着予定編成にMagic phaseのTeleport等が含まれる場合もあります。

## 6. CommanderへStrategic orderを出す

Commanderを選択し、`Space`で命令Menuを開きます。

- Research
- Search for Magic Sites
- Forge Magic Item
- Cast Ritual Spell
- Preach
- Patrol
- Build Fort / Lab / Temple
- Defend
- Wait

などを設定します。複数Commanderを選択している場合は、同じOrderをまとめて出せる場面があります。実行後は各Commander名付近のOrderを確認します。

## 7. 移動経路を確認する

Multi-turn movementを使っている場合は、最終目的地だけでなく途中経路も見ます。

- 敵領を通っていないか
- 遅いUnitが混ざっていないか
- River、Mountain、Cave、Sea等を通れるか
- Commanderごとに経路が分かれていないか
- 同じTurnに到着する必要があるか
- Retreat routeが残るか

必要なら`Ctrl`＋`M`でMap Move Costを表示します。

## 8. End Turn前に確認する

`E`を押す前に、最低限次を見ます。

```text
Messageを読んだ
Battle Replayを確認した
Recruitを設定した
Research目標を確認した
全Commanderの移動・仕事を確認した
Multi-turn routeと目的地を確認した
Army SetupとScriptを確認した
大きなGold・Gemの使い忘れがない
```

End TurnはTurn提出・Host処理へ進む操作です。誤って押した場合に戻せない状況があるため、最後に使います。

---

# Strategic Mapの主要Shortcut

## Province・Turn操作

| Key | 操作 |
|---|---|
| `M` | Messageを読む |
| `R` | Recruit画面を開く |
| `T` | 現在のProvinceのArmy Setup |
| `Y` | 選択Provinceへ到着予定のArmy Setup |
| `B` | Mercenary画面 |
| `I` | Province Chronicle / Province情報 |
| `D` | Province DefenceのRecruit |
| `F` | Fort情報 |
| `O` | Temple・Dominion関連画面 |
| `Ctrl`＋`M` | Map Move Costを表示 |
| `E` | End Turn |
| `H` | Map上のInterface表示を切り替える |
| `?` | Map画面のShortcut一覧 |

Shortcutは、選択しているProvinceやCommanderによって使えない場合があります。反応しないときは、Popupを閉じ、対象ProvinceまたはCommanderを選択し直します。

## Overview・Magic画面

| Key | 画面 |
|---|---|
| `F1` | Nation Overview |
| `F2` | Score Graph |
| `F3` | Hall of Fame |
| `F4` | Pretenders of the World |
| `F5` | Research |
| `F6` | Global Enchantments |
| `F7` | Magic Resource Treasury |
| `F8` | Magic Item Treasury |
| `F9` | Thrones of Ascension |

`F1`のNation Overviewは、Commanderと所在地を一覧で確認し、命令漏れや分散したMageを探す入口として便利です。Game設定により、他国情報やScore Graphが制限される場合があります。

## Map移動・表示

| Key | 操作 |
|---|---|
| Arrow Key | MapをScroll |
| `Page Up` | Zoom in |
| `Page Down` | Zoom out |
| `Home` | Capital付近へ移動 |
| `G` または `#` | Province番号を指定してMap表示を移動 |
| `H` | Interfaceの表示・非表示 |
| `?` | 現在使える表示Shortcutを確認 |

数字Keyや`Ctrl`との組合せにはMap filterがあります。最初から暗記せず、`?`を開いて必要な表示だけ試します。

---

# Army Setupの操作

## UnitをCommanderへ配属する

新しくRecruitされた兵士は、Army Setup上部の未配属Poolへ入ります。

```text
Unitを選択
→ CommanderのPortraitをClickして新しいSquadを作る
```

または、

```text
Unitを選択
→ 既存Squadの欄をClickして追加する
```

ことで配属します。

CommanderのLeadership typeと上限によって、通常兵、Undead、Demon、Magic Beingなどを指揮できない場合があります。

## 配置をまとめて変更する

SquadやCommander横の緑色BoxをClickすると、Battlefield上の初期配置を変更できます。複数BoxをDragで囲めば、まとめて同じ方向へ移動できます。

- 前衛は敵側へ寄せる
- ArcherとMageは後方へ置く
- Flankerは上下の端へ置く
- Buff時間が必要なら全体を後ろへ下げる
- Commanderを一箇所へ重ねすぎない

というのが基本です。ただし、敵のAttack order、飛行、Stealth、Battlefield terrainによって安全地帯は変わります。

## Battle Scriptを複製する

| Key | 操作 |
|---|---|
| `Ctrl`＋`1`～`9` | 現在のBattle Scriptを番号へ保存 |
| `1`～`9` | 保存したScriptを貼り付ける |
| `X` | 直前のSpell / Orderを繰り返す |
| `Q` または `Delete` | Scriptを削除する画面で使用 |
| `?` | その画面の正確な操作を確認 |

貼り付けた後は、使用MageのMagic Path、Gem、Fatigue、Spell rangeが同じか確認します。Scriptが同じでも、Casterが違えば実行結果は同じになりません。

---

# Recruit画面の見方

Recruitでは、購入可能であることと、今Turnに生産可能であることを分けて考えます。

## 兵士Queue

兵士はGoldだけでなく、ResourcesとRecruitment Pointsを消費します。重装兵はResources不足、Sacredや特殊兵はRecruit limit不足で作れない場合があります。

## Commander Queue

Commander、Mage、PriestはCommander Pointsを使います。兵士Queueに余裕があっても、Commander Point不足ではMageを追加できません。

## 右Clickで購入前に確認する

- Gold / Resource Cost
- Recruitment Point
- Map Move
- Strategic特殊能力
- Leadership
- Magic Path
- Equipment

を確認します。

## Recruit拠点を順番に確認する

Fortが増えたら、Mapへ戻って一つずつ探すより、Recruit画面のArrow系Shortcutで次のRecruit拠点へ移る方が速くなります。Fortだけを巡回する操作と、Recruit可能な全Provinceを巡回する操作があるため、`?`で現行Bindingを確認します。

---

# Battle Replayの操作

Battle Replayでは、勝敗だけでなく「Scriptがどこで崩れたか」を観察します。

| Key | 操作 |
|---|---|
| `Space` | Pause / Resume |
| `F` | 早送り |
| `T` | さらに高速 |
| `S` | 通常速度 |
| `Z` | Slow motion |
| `Q` | Replayを終了 |
| `G` | Grid表示を切り替える |
| `V` | UnitのCombat logを確認する画面で使用 |
| `1`～`4` | Battle logの詳細度を変更 |
| `+` / `-` | Battle logをScroll |
| `?` | Replay画面のShortcut一覧 |

確認したい瞬間では`Space`で止め、Unitを選択してHP、Fatigue、Buff、Debuff、Affliction、Targetを見ます。

詳しい分析方法は[Battle Replayの読み方](battle-replay.md)を参照してください。

---

# よくある操作上の失敗

## 遠いProvinceをClickしても移動できない

Multi-turn movementが無効、未探索で接続が分からない、通過不能Terrain、移動能力不足などを確認します。Options / PreferencesとMap画面の`?`を開きます。

## 遠方へ指定したのに一Turnで着かない

Multi-turn movementは、複数Turn分の経路を一度で予約する機能です。一Turnの移動距離を増やす機能ではありません。

## 複数Commanderが別々に到着した

Commanderと同行UnitのMap MoveやTerrain適性が異なると、経路・到着Turnがずれます。同時到着が必要なら中継Provinceで集合させ、`Y`で到着予定編成を確認します。

## Province番号へ移動したのにArmyが動かない

`G`や`#`はMap表示位置を移す操作です。Commanderの移動Orderには、選択状態、目的地指定、Arrow表示が必要です。

## `R`のつもりで`E`を押す

RecruitとEnd Turnが近いため、慣れるまでは特に注意します。Warn on End TurnとTurn終了前Checkを使います。

## `T`と`Y`を混同する

`T`は現在ProvinceにいるArmy、`Y`はそのProvinceへ移動してくるArmyを編成します。合流戦や迎撃では`Y`が重要です。

## Unitを買ったのにArmyへいない

Recruitされた兵士は自動的にSquadへ入りません。次Turn、Army Setup上部の未配属PoolからCommanderへ割り当てます。

## Commanderを動かしたが兵士が付いてこない

兵士がそのCommanderのSquadに所属しているか確認します。未配属、別Commander、Leadership type不一致が原因になることがあります。

## Stealthy CommanderがSneakしてしまう

Stealthy Commanderは通常の移動指定でSneakになる場合があります。通常移動で攻撃・合流したい場合は、画面内`?`で`Ctrl`＋Clickの操作を確認し、Order表示を見ます。

## SpellをScriptしたのに使わない

操作ミスとは限りません。

- Research未完了
- Magic Path不足
- Gem不足
- Fatigue
- Range
- 有効Target不在
- Spell使用条件

を確認します。

## Shortcutが反応しない

DominionsのShortcutは画面依存です。

1. Popupを閉じる
2. 対象ProvinceまたはCommanderを選択する
3. `?`を押す
4. 表示された現行Shortcutを使う

の順で確認します。

---

# 初心者向けの最小操作表

最初の数Turnは、次だけで十分です。

```text
?          画面別Help
右Click     詳細確認
M          Message
R          Recruit
F5         Research
T          Army Setup
Space      Commander order
Ctrl+Click 複数Commanderの個別選択
Shift+Click 複数Commanderの範囲選択
Ctrl+M     Map Move Cost
E          End Turn
```

長距離移動を始める前に、Options / PreferencesでMulti-turn movementを有効にします。Shortcutをすべて暗記する必要はありません。**同じ操作を何度もする場面で、一つずつ置き換える**方が覚えやすくなります。

---

## 関連ページ

- [初心者ガイド](index.md)
- [初心者向けTips](beginner-tips.md)
- [最初の12ターン](first-12-turns.md)
- [命令とBattle Script](../basics/orders.md)
- [Battle Replayの読み方](battle-replay.md)
- [Researchと研究ルート](../magic/research.md)

## 主な参照先

- Game内の画面別Shortcut Help（`?`）
- Game内のOptions / Preferences
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
- [Dominions 6 New Features](https://www.illwinter.com/dom6/changes.html)
