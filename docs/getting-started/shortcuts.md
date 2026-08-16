---
title: 操作方法・ショートカット
page_type: guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# 操作方法・ショートカット

Dominions 6は、画面上のButtonだけでも遊べます。しかし、Map、Recruit、Army Setup、Research、Battle Replayでは操作方法が異なり、最初は「何をクリックすればよいか」が分かりにくいゲームです。

このページでは、単なるKey一覧ではなく、**一Turnを進めるための操作順、Mouse操作、画面ごとの主要Shortcut、よくある誤操作**をまとめます。

!!! warning "最も重要な操作は `?`"
    Dominions 6のShortcutは画面ごとに変わります。分からない画面では、まず`?`を押してください。その画面で使えるShortcut一覧が表示されます。Keyboard配列によっては`Shift`＋`/`で`?`を入力します。

!!! note "表記とVersion"
    このページはDominions 6.35を基準にしています。画面内Helpの表示が本文と異なる場合は、現行Game内の`?`表示を優先してください。

---

## 最初に覚える七つ

| 操作 | Key | 何ができるか |
|---|---|---|
| 画面別Help | `?` | 現在の画面で使えるShortcutを表示する |
| Message | `M` | 戦闘、Event、建設、発見など今Turnの結果を読む |
| Recruit | `R` | 選択ProvinceのRecruit画面を開く |
| Army Setup | `T` | 選択Provinceに現在いるArmyを編成する |
| Commander命令 | `Space` | 選択Commanderの命令Menuを開く |
| Research | `F5` | Research画面を開く |
| End Turn | `E` | Turnを提出し、次の処理へ進む |

`E`は最後に使います。Recruitの`R`と近いため、慣れるまでは画面右上のEnd Turn Buttonを使っても構いません。

---

# Mouse操作の基本

## 左Click：選択と実行

Map上ではProvinceやCommanderを選択し、各画面ではButton、Unit、Squad、命令を選びます。

Commanderへ移動命令を出す基本形は、

```text
Commanderを選択
→ 移動先Provinceを選ぶ
→ Map上の移動Arrowと命令表示を確認
```

です。選択したCommanderとProvinceが意図どおりか、Arrowが出た後に確認します。

## 右Click：詳細を見る

Unit、Commander、Spell、Magic Itemなどは、名前やIconを右Clickすると詳細を確認できる場面が多くあります。

初心者は、知らないUnitをすぐ閉じず、少なくとも次を見ます。

- HP、Protection、Defence、Magic Resistance
- WeaponとDamage type
- Magic Path
- Leadership
- 特殊能力
- Affliction

右Clickは「命令を出す操作」よりも、**その対象が何者か確認する操作**として覚えると分かりやすくなります。

## Double Click：同種をまとめて選ぶ

Army Setupでは、同じ種類のUnitをDouble Clickすると、同種Unitをまとめて選択できます。

大量の兵士を一体ずつ選ぶ必要はありません。

## Shift＋Click：範囲選択

Army Setupなどでは、最初のUnitを選び、`Shift`を押しながら最後のUnitを選ぶと、その間をまとめて選択できます。

Recruit画面では、`Shift`を押しながらUnitを選ぶと、同じUnitを十体単位でQueueへ追加できます。

## Enter：選択解除

Army Setupで選択状態が分からなくなった場合は、`Enter`で選択を解除してからやり直します。

## Esc：閉じる・戻る

PopupやMenuを閉じたいときは`Esc`を使います。画面によって動作が異なるため、閉じない場合は画面内のBack / Exit Buttonを使います。

---

# 一Turnの操作順

## 1. Messageを開く

`M`でMessage画面を開きます。

確認するものは、

- Battle結果
- Commanderや重要Unitの死亡
- Event
- Magic Site発見
- Fort、Lab、Templeの建設完了
- RitualやForgeの結果
- Multiplayerの外交Message

です。

Battle MessageからReplayを開き、勝った戦闘も一度は確認します。

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

を確認します。

## 3. Recruitを設定する

Provinceを選択し、`R`でRecruit画面を開きます。

Recruit画面では、兵士とCommanderのQueueを分けて確認します。

- Gold
- Resources
- Recruitment Points
- Commander Points
- Recruit limit

のどれが不足しているかを見ます。

Unitを右Clickして能力を確認し、`Shift`＋Clickで十体単位の追加を使うと操作が速くなります。

## 4. Researchを設定する

`F5`でResearch画面を開きます。

Schoolを均等に上げるのではなく、次に使うSpellやItemのBreakpointへResearchを集めます。Researchを変更した後は、予定しているSpellのSchoolとLevelをもう一度確認します。

## 5. Army Setupを行う

選択Provinceに現在いるArmyは`T`で編成します。

Army Setupでは、

1. 画面上部の未配属Unitを選ぶ
2. CommanderのPortraitまたは既存Squadへ割り当てる
3. SquadのFormationとBattle orderを設定する
4. 緑色の配置BoxからBattlefield上の開始位置を決める
5. CommanderのSpell ScriptとMain orderを設定する
6. Leadership、Squad数、Unit数の上限を確認する

という順で進めます。

移動先で合流するArmyを組みたい場合は、Map画面の`Y`を使います。`T`は現在いるArmy、`Y`は選択Provinceへ到着予定のArmyを扱うため、混同しないようにします。

## 6. CommanderへStrategic orderを出す

Commanderを選択し、`Space`で命令Menuを開きます。

代表的な命令は、

- Research
- Search for Magic Sites
- Forge Magic Item
- Cast Ritual Spell
- Preach
- Patrol
- Build Fort / Lab / Temple
- Defend
- Wait

です。

命令を出した後は、Commander名の近くに表示されるOrderを確認します。何も命令していないCommanderがいても、それが意図的な待機なら問題ありません。

## 7. End Turn前に確認する

`E`を押す前に、最低限次を見ます。

```text
Messageを読んだ
Battle Replayを確認した
Recruitを設定した
Research目標を確認した
全Commanderの移動・仕事を確認した
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
| `E` | End Turn |
| `H` | Map上のInterface表示を切り替える |
| `?` | Map画面のShortcut一覧 |

Shortcutは、選択しているProvinceやCommanderによって使えない場合があります。反応しないときは、まず対象Provinceを選択します。

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

Game設定により、他国情報やScore Graphが制限される場合があります。

## Map移動・表示

| Key | 操作 |
|---|---|
| Arrow Key | MapをScroll |
| `Page Up` | Zoom in |
| `Page Down` | Zoom out |
| `Home` | Capital付近へ移動 |
| `G` または `#` | Province番号を指定して移動 |
| `H` | Interfaceの表示・非表示 |
| `?` | 現在使える表示Shortcutを確認 |

Map filterには、軍、旗、Dominion、Income、Throne、Province接続などを表示する機能があります。数字Keyと`Ctrl`の組合せは表示設定によって分かりにくいため、最初は`?`で一覧を開いて必要なものだけ試します。

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

## Unit選択を速くする

| 操作 | 効果 |
|---|---|
| Double Click | 同じ種類のUnitをまとめて選択 |
| `Shift`＋Click | 範囲選択 |
| `Enter` | 選択解除 |
| `?` | Army Setup専用Shortcutを表示 |

SquadへMouse cursorを置いた状態で使える、Affliction、Disease、Experienceなどの選別Shortcutもあります。正確なKeyは現行画面の`?`で確認してください。

## 配置を変更する

SquadやCommander横の緑色BoxをClickすると、Battlefield上の初期配置を変更できます。

- 前衛は敵側へ寄せる
- ArcherとMageは後方へ置く
- Flankerは上下の端へ置く
- Buff時間が必要なら全体を後ろへ下げる
- Commanderを一箇所へ重ねすぎない

というのが基本です。

ただし、敵のAttack order、飛行、Stealth、Map terrainによって安全地帯は変わります。

## Battle Scriptを複製する

同じScriptを多数のCommanderへ設定する場合は、Script保存を使います。

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

兵士はGoldだけでなく、ResourcesとRecruitment Pointsを消費します。

同じGoldがあっても、重装兵はResources不足、Sacredや特殊兵はRecruit limit不足で作れない場合があります。

## Commander Queue

Commander、Mage、PriestはCommander Pointsを使います。

兵士Queueに余裕があっても、Commander Pointが不足しているとMageを追加できません。Fortの種類とCommander PointはResearch速度にも影響します。

## 右Clickで購入前に確認する

Recruit画面でUnitを右Clickし、

- Gold / Resource Cost
- Recruitment Point
- Map Move
- Strategic特殊能力
- Leadership
- Magic Path
- Equipment

を確認します。

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

## `R`のつもりで`E`を押す

RecruitとEnd Turnが近いため、慣れるまでは特に注意します。Turn終了前Checkを習慣にします。

## `T`と`Y`を混同する

`T`は現在ProvinceにいるArmy、`Y`はそのProvinceへ移動してくるArmyを編成します。合流戦や迎撃では`Y`が重要です。

## Unitを買ったのにArmyへいない

Recruitされた兵士は自動的にSquadへ入りません。次Turn、Army Setup上部の未配属PoolからCommanderへ割り当てます。

## Commanderを動かしたが兵士が付いてこない

兵士がそのCommanderのSquadに所属しているか確認します。未配属、別Commander、Leadership type不一致が原因になることがあります。

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
M   Message
R   Recruit
F5  Research
T   Army Setup
Space  Commander order
右Click  詳細確認
?   画面別Help
E   End Turn
```

Shortcutをすべて暗記する必要はありません。**同じ操作を何度もする場面で、一つずつ置き換える**方が覚えやすくなります。

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
- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
