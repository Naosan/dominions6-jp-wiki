---
title: "Stone Sphere"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-25"
item_id: 391
---

# Stone Sphere

**Astral Windowによる遠隔偵察をMisc Slotへ持ち込み、敵Army・Fort周辺・進軍経路の情報へGemとCommander actionを変換するConstruction 5のScrying Item。**

Stone Sphereは、持っているだけで全Mapを見せるItemでも、毎Turn自動的に敵情報を更新するScoutでもありません。攻略上は、**必要なProvinceを選んで詳しく見るための情報装置**として評価し、Item spellの使用条件とTaint 3のRiskを同時に管理します。

- [Dominions 6.35固定データ — Item 391](../../data/items/by-id/391.md)
- [Magic Item攻略辞典](index.md)
- [用途別Magic Item辞典](../purpose-dictionary.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Bane Venom Charm](bane-venom-charm.md)

---

# まず何ができるか

6.35固定データでは、Stone Sphereは、

- Construction 5
- Forge要求 **G2E1**
- Base Gem cost **10G + 5E**
- Miscellaneous Slot
- Item spell **Astral Window**
- **Taint 3**

を持ちます。

Item descriptionでは、黒い布で日光から守られた黒い石球が月光を受けると透明になり、遠方の場所の像を映すと説明されています。

Itemの固定fieldは、

```text
Astral Windowを使う情報機能
＋
Taint 3というRisk field
```

です。

---

# Astral Windowは一つのProvinceを詳しく見るRitual

Astral WindowのSpell descriptionは、CasterがArcane riftを開いて遠方の土地を観察し、**一回のCastingで一つのProvinceをScryする**と説明しています。

また、通常のScoutより正確な情報を得られるとされています。

通常Spell recordでは、Astral Windowは、

- Thaumaturgy 4
- S2
- Gem cost 3

のRitualです。

Stone Sphere側は`Item spell: Astral Window`を持ちますが、

- Carrierに必要なPath
- Research requirementをItemがどこまで代替するか
- 実際に払うGem
- extra Gem投入のUI
- 使用可能なCommander種別

はItem使用時のゲーム内表示を正本にします。

Item spell fieldがあることだけから、

```text
誰でも無料でResearch不要
```

とは断定しません。

---

# 情報は「見るProvinceを選ぶ」ことで価値になる

Stone Sphereの価値は、Scry回数だけでは決まりません。

有効なTargetは、

- 敵主力Armyの現在地
- Fort救援軍が集結しそうなProvince
- Border Fortの守備・Commander構成
- Raid route上のChokepoint
- Throne周辺
- Magic Phase移動の着地点候補
- 海岸・山岳・河川等、進軍Routeを制限するProvince
- 敵の増援が合流する中継点

です。

```text
見た結果、進軍・迎撃・撤退・外交判断が変わるProvince
```

を優先します。

何も行動が変わらない遠隔ProvinceへScryを繰り返すと、Commander actionとGemを情報へ変えただけで終わります。

---

# Scoutの代替ではなく、Scout網の穴を埋める

通常Scoutは、

- 現地へ移動する
- 捕捉・Patrol Riskを負う
- 情報取得までTurnがかかる
- 継続して同じ地域を追える

という性質があります。

Stone Sphereは、

- 遠方を選択して見る
- C5とCrosspath Forgeを必要とする
- Item spellの使用Costを払う
- Carrierを安全な後方へ置ける可能性がある
- 一回ごとにTarget Provinceを選べる

点が異なります。

```text
Scout
→ 継続的な現地観測

Stone Sphere
→ 重要地点への選択的な遠隔観測
```

として併用します。

Scoutを全廃すると、Scryしていない周辺Provinceの移動や小規模Raidを見落とす可能性があります。

---

# 情報は次Turnには古くなる

Scryで得た情報は、その時点のSnapshotです。

敵は次のTurnに、

- Armyを移動する
- CommanderをTeleport等で追加する
- Gemを配る
- Armyを分割する
- Fort内外を入れ替える
- PretenderやSummonを合流させる
- Retreat routeを変える

ことができます。

したがって、

```text
Stone Sphereで見えた
→ 未来のBattleまで同じ編成
```

ではありません。

情報を使う時は、

- ScryしたTurn
- 実際に接触するTurn
- 敵のMap Move
- Magic Phase移動の有無
- 周辺Fortからの増援

を同時に考えます。

---

# G2E1 Crosspathが最初の壁

Stone SphereはC5で解禁されますが、Forge要求はG2E1です。

```text
国家全体にG2とE1がいる
≠
同じMageがG2E1を持つ
```

ため、最初のForgerを確認します。

候補は、

- native G2E1 Mage
- RandomでCrosspathへ届くMage
- Pretender
- Hero
- Summon
- Booster込みで条件を満たすMage

です。

ForgeのためだけにEmpowermentや長いBooster chainを使うと、情報Item一個の入口Costが急増します。

---

# Base costだけで終わらない

Stone Sphereの初期投資は10G + 5Eです。

さらに実際の運用では、

- Forgerの一Turn
- CarrierのRitual action
- Astral Window使用時のGem
- Carrier用の安全なLab
- Taint Risk
- Misc Slot

が発生する可能性があります。

そのため、

```text
情報によって避けた損失・得た戦果
>
Forge + 運用Cost
```

となるかを見ます。

敵主力を一度正確に把握して大敗を避ければ、十分に回収できます。

一方、毎Turn惰性で遠方を見るだけならCostが積み上がります。

---

# Carrierは「貴重なMage」より「安全に繰り返せるOperator」

Stone SphereのCarrierに必要なのは、前線Combat能力ではなく、

- Item spellを使用できる
- 安全なLabで行動できる
- 毎Turnの別任務を失ってもよい
- Taint Riskを集中させても国家全体が崩れない
- Gemを管理できる
- 敵Raidから守られている

ことです。

Unique Mage、Pretender、主力Researcherへ持たせると、

- Ritual actionの競合
- Taintの集中
- RaidでItemごと失うRisk
- Misc Slot競合

が大きくなります。

Item spellの使用条件を満たす範囲で、代替可能なOperatorへ任せられるかをTestします。

---

# Taint 3をFlavorとして無視しない

6.35固定recordには**Taint 3**が明示されています。

ただし、固定field名だけから、

- 毎Turn何%で何が起こる
- 何回使うと確定でAfflictionが付く
- 装備中だけ増える
- Casting時だけ判定する
- どのUnit classificationへ効く

といった式は断定しません。

攻略上は、

```text
Stone Sphereには情報機能と別にCarrier Riskがある
```

ことを前提にします。

Test gameでは、装備Turn数、使用回数、Unit詳細、Affliction・Insanity・その他変化を記録します。

---

# 一個を複数Operatorで共有できるか

Stone SphereはLabで受け渡せるItemです。

理論上は、

```text
今Turn使うOperatorへ装備
→ Astral Window
→ 次Turnに別Operatorへ渡す
```

運用が考えられます。

これにより、

- 一人へTaintを集中させない
- 忙しいMageを別任務へ戻す
- Gemを持つOperatorを替える

ことが可能かもしれません。

ただし、Taintが装備・使用・保持のどのTimingで作用するかによって有効性が変わります。共有を安全策として断定せず、Test対象にします。

---

# Forgeする条件

次が揃うほど価値が上がります。

- Construction 5へ到達済み
- G2E1 Forgerを無理なく確保できる
- 10G + 5Eを情報投資へ回せる
- Scoutが入りにくい重要地点がある
- 敵主力の位置で進軍判断が大きく変わる
- Throne・Fort・Chokepoint等、見る価値の高いTargetがある
- Operatorと使用Gemを継続確保できる
- Taint Riskを許容・分散できる
- Multiplayerで情報優位が外交・迎撃へ直結する

「Scryできるから」ではなく、**Scry結果で具体的に変えるOrderがある時**にForgeします。

---

# Forgeしない・後回しにする条件

- Scout網だけで必要情報が足りている
- G2E1 accessのために重いEmpowermentが必要
- 10G + 5EをBattle magic・Booster・Thug gearへ回したい
- Astral Windowの使用Gemを継続供給できない
- OperatorのactionがResearch・Ritualで埋まっている
- 見ても次Turnに攻撃・迎撃できない
- 敵の高速移動で情報がすぐ古くなる
- Taint Riskを負わせられるCarrierがいない
- Borderが広すぎて一Provinceずつ見る方法が合わない

Stone Sphereは情報量を増やしますが、情報を活用する機動力・Army・外交がなければ勝ち筋には変わりません。

---

# Counter：情報を古くし、価値を下げる

Stone Sphereそのものを正面から無効化する方法を断定せず、Scry情報の運用価値を下げます。

- Scry後にArmyを分割・再合流する
- 複数Routeから圧力をかける
- Fast movementやMagic Phaseで編成を変える
- Fort内外のCommanderを入れ替える
- Visible Armyを囮にして別部隊を動かす
- Stone SphereのCarrierやLabをRaidする
- Gem routeへ圧力をかけ、継続Scryを難しくする
- Scryされた可能性を前提に、次TurnのOrderを固定しない

ただし「Scryされたことを相手が通知で知るか」「特定能力で防げるか」はTest・現行仕様を確認します。

---

# よくある失敗

## 持っているだけで自動偵察すると思う

Item spellを使う行動が必要です。使用UIとCostを確認します。

## 誰でも無料で使えると思う

Carrier Path、Research、Gem、Lab等の条件をゲーム内表示で確認します。

## Scoutを全て置き換える

一Provinceずつ選ぶScryと、継続的なScout網は役割が違います。

## 情報を未来の確定編成として扱う

敵は次Turnに移動・合流・Gem配布を変えられます。

## Taint 3を無視する

正確な式が不明でも、Risk fieldがあること自体は固定データで確認できます。

## 高価なUnique Mageへ持たせる

情報Item、Carrier、Gem、国家固有能力を一度に失うRiskがあります。

## 見るProvinceを選ばない

Scry結果でOrderが変わらないTargetへ使うと、情報Costを回収できません。

---

# Test game checklist

```text
[ ] C5・G2E1でForge可能か確認
[ ] Base costが10G + 5Eであることを確認
[ ] Item 391 / Misc Slotであることを確認
[ ] Item spell Astral Windowが表示されることを確認
[ ] 使用可能なCommander・Path条件を確認
[ ] Research requirementの扱いを確認
[ ] Lab requirementを確認
[ ] 一回の使用Gemとextra Gem投入UIを確認
[ ] 一回で一ProvinceをScryすることを確認
[ ] Scoutと得られる情報項目を比較
[ ] 情報の継続Turn・更新Timingを確認
[ ] Taint 3の装備・使用・Turn経過時の挙動を記録
[ ] Operatorを交代した時のTaintと使用可否を確認
[ ] Carrier死亡・Item移動時の情報継続を確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 391](../../data/items/by-id/391.md)
- [用途別Magic Item辞典](../purpose-dictionary.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Bane Venom Charm](bane-venom-charm.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description / Spell record / Spell description
- Item 391: C5 / G2E1 / Misc / Item spell Astral Window / Taint 3
- generated Item record: Base cost 10G + 5E
- Astral Window record: Thaumaturgy 4 / S2 / Gem cost 3。Stone Sphere経由のPath・Research・Gem・Lab条件はゲーム内Item commandを優先
- Taintの式・発動Timing・結果は固定field名から推測せず、Test gameで確認