---
title: "Igor Könhelm's Tome"
status: reviewed
verified_version: "6.35"
item_id: 431
---

# Igor Könhelm's Tome

**Corporeal Undeadの長期運用と、Storm下でのCarrier強化を一つにまとめるConstruction 9 Artifact。**

普通の「MageのPathを+1する本」ではありません。価値の中心は、**Corpse Stitcherとして傷んだcorporeal undeadを維持できること**と、**Storm Power 5を戦闘へ持ち込めること**です。

- [Dominions 6.35固定データ — Item 431](../../data/items/by-id/431.md)
- [Artifact・Unique Item攻略](../artifacts.md)
- [Flying・Storm・Air機動戦](../../systems/flying-storm.md)
- [Undead・Reanimation・Popkill](../../systems/undead-popkill.md)

---

# まず何ができるか

6.35固定データと現行Manualでは、Igor Könhelm's TomeはConstruction 9のMiscellaneous Artifactで、要求Pathは**A2D2**、主要能力は**Corpse construction Bonus 20**と**Storm Power 5**です。

Dominions 6.30のPatchでは、このItemが**Corpse Stitcher abilityを与える**よう変更されています。

ここで二つの用途を分けて考えます。

```text
後方で装備
→ Corporeal UndeadのAffliction maintenance

戦場へ持ち込む
→ Storm下でStorm Power 5を利用
```

同じItemですが、必要なCarrierとRiskはかなり違います。

---

# Corpse Stitcherとして使う

Corpse Stitcherは、同じProvinceにいる**corporeal undead**のAfflictionを自動的に治療する能力です。

つまりこのItemは、単発の戦闘力ではなく、

- 高価なUndead Commander
- 長期間使うUndead combatant
- Afflictionが蓄積したcorporeal undead
- 再生産しにくいUndead資産

を**次の戦争でも使える状態へ戻すmaintenance infrastructure**として評価できます。

DisposableなSoullessを大量に治すためだけにC9 Artifactを確保するのは投資が重すぎます。

価値が大きいのは、

> 「失いたくないcorporeal undeadが、勝った戦闘のたびにAfflictionで劣化していく」

という国家やArmyです。

---

# Spiritformには使えない

重要な例外です。

Corpse Stitcherが治療できるのは**corporeal undead**で、Spiritformのような非実体のUndeadは対象外です。

したがって、

```text
Undeadだから治る
```

とは考えません。

このItemをForgeする前に、治したいUnitの能力欄を確認します。

「Wraith系を直すために作ったが対象外だった」は、C9 Artifactとして非常に重い失敗です。

---

# Storm Power 5の意味

Storm Powerは、戦闘中にStormまたはBlizzardが存在するときに働くPower abilityです。

Storm Power 5は、Storm条件下でCarrierの、

- Strength
- Attack Skill
- Defence Skill
- Combat Speed

を大きく押し上げます。

そのためTomeを前線へ持ち出す場合、単なるUndead healerではなく**Storm戦専用の戦闘強化Item**としても機能します。

特に、元からStatsが高く、+5を有効に使えるCommanderほど伸びます。

---

# 「Storm Powerがある＝Storm Immunity」と思わない

ここは実戦で事故になりやすい点です。

Tomeの6.35 Item表示はStorm Powerを持ちますが、**Item自身がStorm Immunityまで与えるとは書かれていません**。

Stormは通常、Storm Immunityを持たないUnitへ、

- Flyingの禁止
- Precision低下

などの影響を与えます。

したがって、Flying Raiderや射撃・精密Spellを使うCarrierへTomeを持たせる場合は、

> Storm Powerの利益とStormそのものの不利益を別々に確認する

必要があります。

「Storm Power 5だからStormと完全に相性がよい」と一行で片付けないのが重要です。

---

# Stormを誰が用意するか

Storm PowerはStormがなければ働きません。

そのため戦闘用途では、Tome単体ではBuildが完成していません。

代表的な入口は、

- `Storm`
- Stormを戦闘開始時から作るItem / effect
- `Perpetual Storm`等、戦場へStormを持ち込める環境

です。

実戦では、

```text
Stormを作る役
＋
Tome carrier
＋
Stormで不利を受けにくいArmy
```

までを一つのpackageとして設計します。

---

# 誰に持たせるか

## 後方maintenanceなら

前線へ出す必要はありません。

- 安全なFort
- Laboratory
- 治療対象のcorporeal undead
- Patrol / Bodyguard

を揃え、Artifactそのものを守ります。

この用途ではCarrierの戦闘Statsより、**死なずに同じProvinceへ居続けられること**が重要です。

## 戦闘用途なら

Storm Power 5を使い切れる、

- 高い基礎Stats
- 十分なMR / Protection / Resistance
- Misc slotに余裕がある
- Stormの不利益を許容できる

Commanderが候補です。

ただしArtifactを前線へ持ち込む時点で、maintenance資産まで同時にRiskへ晒します。

---

# 二役を同時にさせる必要はない

このItemは能力が二つあるため、つい

> Corpse StitcherもStorm combatも一人で使わなければ損

と考えがちです。

しかしArtifactの価値は「全部の能力を毎Turn使うこと」ではなく、**今の勝ち筋に必要な能力を確実に使うこと**です。

Undead Commanderのmaintenanceが国家全体の価値なら後方へ置く。

決戦でStorm Power 5が勝敗を変えるなら、そのTurnだけ前線へ移す。

役割を切り替えてよいItemです。

---

# Forgeする条件

次の条件が重なるほど価値が上がります。

- Construction 9へ行く理由が他にもある
- A2D2へ無理なく届く
- 長く使いたいcorporeal undeadがいる
- Affliction蓄積が実際の損失になっている
- Stormを戦術の中心にしている
- C9 Artifact raceで先に確保できる
- Misc slotの競合が小さい

逆に、Undead maintenanceもStorm戦も使わないなら、能力が派手でも優先度は落ちます。

---

# Forgeしない・後回しにする条件

- 治療対象がほぼSpiritform
- UndeadがDisposableで治す価値が低い
- Stormを使わない
- Stormで自軍のFlying / Precisionが大きく崩れる
- A2D2を作るためのBooster / Empowermentが重い
- C9研究より直近のBattle magicが必要
- 他のArtifactを先に確保したい

Artifactなので「作れるから作る」ではなく、**C9 Research、Forge turn、Gem、先着権を何へ変換するか**で判断します。

---

# Counter：敵がmaintenanceに使っている

敵が後方でCorpse Stitcherとして使っているなら、真正面からUndead Armyを削り続けても、重要CommanderのAfflictionが回復して消耗戦の意味が薄くなる場合があります。

狙いはTomeそのもの、またはCarrierです。

- Assassin
- Remote attack
- Fortへの圧力
- Magic phase attack
- Raiderで治療拠点を脅かす

などで、**回復拠点を安全な後方に置けなくする**と価値を下げられます。

---

# Counter：敵がStorm戦へ持ち込む

まずBattle Replayで、敵の強さが、

```text
TomeのStorm Power
Stormそのもの
別のBuff
Carrier本体
```

のどこから来ているか分解します。

Storm Power carrierだけを見て「Statsが高すぎる」と判断せず、Stormがない戦闘でも同じ性能かを確認します。

また、TomeがStorm Immunityを保証するItemではない点は、敵側にも同じです。Stormで発生しているPrecision・Flying制約が敵Buildの弱点になっていないかを見ます。

---

# よくある失敗

## 「Undeadなら全部治る」と思う

Spiritformを見落としています。

## Stormを用意せず戦闘Itemとして持つ

Storm Power 5が起動しません。

## Stormの副作用をCarrier側で確認しない

Power bonusだけ見てFlyingやPrecisionを失います。

## C9 ArtifactをDisposable carrierへ渡す

一戦の強化と引き換えに、世界uniqueのmaintenance資産まで失います。

## 20という数だけ見て大量SoullessのためにForgeする

治療対象の**価値**とArtifactの機会費用を比較していません。

---

# Test game checklist

実戦投入前に小さなTest gameで確認します。

```text
[ ] Tomeを装備したときCorpse Stitcher表示を確認
[ ] 治療対象がcorporeal undeadか確認
[ ] Spiritformが対象外であることを確認
[ ] 1 Turn後にAffliction治療が発生するか確認
[ ] StormなしのCarrier Statsを記録
[ ] StormありのCarrier Statsを記録
[ ] Strength / Attack / Defence / Combat Speedの変化を確認
[ ] CarrierがStorm Immunityを別途持つか確認
[ ] Flying / PrecisionへのStorm影響を確認
[ ] Tomeを失った場合の代替planを用意
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 431](../../data/items/by-id/431.md)
- [Artifact・Unique Item攻略](../artifacts.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Flying・Storm・Air機動戦](../../systems/flying-storm.md)
- [Undead・Reanimation・Popkill](../../systems/undead-popkill.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI
- Dominions 6 Main Manual — Magic Items / Affliction treatment
- Dominions 6.30 Patch notes — Igor Könhelm's TomeへCorpse Stitcher追加
- Dominions 6 Modding Manual — Corpse Stitcher / `#autocorpsehealer`

正確なForge costやPatch後の現在値は、ゲーム内Forge画面とgenerated recordを優先してください。
