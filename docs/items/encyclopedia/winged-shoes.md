---
title: "Winged Shoes"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 294
---

# Winged Shoes

**CommanderへFlyingを与え、戦略移動と戦闘内の位置取りを変えるConstruction 5の機動Item。**

Winged Shoesの価値はDamageやProtectionではなく、**行けなかった場所へ行ける／届かなかった相手へ届く**ことにあります。

- [Dominions 6.35固定データ — Item 294](../../data/items/by-id/294.md)
- [Flying・Storm・Air機動戦](../../systems/flying-storm.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

---

# まず何ができるか

6.35固定データでは、Winged ShoesはConstruction 5のBootsで、Forge要求は**A2**、基礎Costは**10A**、装備者へ**Flying**を与えます。

この能力は、

- Map上の移動
- Raid route
- Armyから独立したCommander機動
- 戦闘内の接敵・配置

を変える可能性があります。

ただし、**Commander一人がFlyingになっただけで、率いる通常部隊までFlyingになるわけではありません**。

---

# 機動Itemは「Stats」ではなく到達可能性を買う

Winged Shoesを評価するときは、装備前後のAttackやDefenceではなく、

```text
装備なしでは届かないProvinceへ届く？
装備なしでは間に合わない戦闘へ間に合う？
Armyと分離して価値を出せる？
敵Commanderへ戦闘中に接近しやすくなる？
```

を見ます。

一Province多く取れる、重要Mageを退避できる、予想外の方向からRaidできるなら、10A以上の戦略価値を生むことがあります。

---

# 誰に持たせるか

代表候補は、**単独または少数で仕事が完結するCommander**です。

- Raider
- Scout / mobile support
- Assassin系Commander
- Battlefield caster
- Gem / Item courier
- 独立して移動したいThug

などです。

大軍を率いるCommanderへ装備しても、そのArmyの移動は配下Unitの移動能力に制約されます。

したがって、靴のFlyingがArmy全体の機動へ変換されるかを事前に確認します。

---

# Raiderでの価値

Raiderでは、戦闘能力そのものだけでなく**どこへ攻撃を選べるか**が強さです。

Winged Shoesで移動選択肢が増えると、

- 薄いPDを選ぶ
- Fortを避ける
- Gem Siteを狙う
- 補給線・後方Provinceへ回る
- Enemy Armyと正面衝突しない

といった勝ち方が可能になります。

一方、移動先で囲まれて退却できなければ、機動ItemごとCarrierを失います。

**入るrouteだけでなく出るroute**まで確認します。

---

# Battlefield casterでの価値

Flyingは戦闘内でも位置取りへ影響します。

ただしCasterを敵へ近づけることが常に利益とは限りません。

- ScriptしたSpellのRange
- Enemy flyer / assassin-like threat
- Bodyguardから離れるRisk
- Fatigue後の生存
- Retreat方向

を見ます。

「飛べるから前へ出す」ではなく、**必要な射程と安全距離を作るための移動能力**として使います。

---

# Boots slot競合

Winged ShoesはBootsを使います。

Bootsには、

- Reinvigoration
- Strength
- Quickness
- Resistance
- 別のMobility

など重要効果が競合します。

そのため本当のCostは、

```text
10A
+
Forge turn
+
Boots slot
+
外したBootsの価値
```

です。

ThugがFlyingを得た代わりにReinvigorationを失い、長期戦でFatigue collapseするならBuild全体では弱くなります。

---

# Stormとの関係

Flyingを使うBuildではStormを必ず意識します。

通常、StormはStorm Immunityを持たないUnitのFlyingを制限します。

そのためWinged Shoesを、

- Storm戦へ投入する
- EnemyがStormを使う
- 自軍がStormを展開する

場合は、**靴を履いたから常に飛べる**と考えません。

Storm Immunity等の例外を含め、実際の戦闘条件は[Flying・Storm・Air機動戦](../../systems/flying-storm.md)とTest gameで確認します。

---

# Forgeする条件

次が多いほど価値が上がります。

- Construction 5へ到達している
- A2へ無理なく届く
- 単独行動するCommanderがいる
- Raid対象が地理的に広がる
- 地形・敵配置を飛び越える価値が高い
- Boots slotに余裕がある
- Air Gemを機動へ変換する明確な任務がある

「Flyingが強い」ではなく、**次Turnにどこへ行くために作るのか**が言えるときがForge時です。

---

# Forgeしない・後回しにする条件

- Carrierが常に非Flying Armyを率いる
- Boots slotへReinvigoration等が必須
- Air GemをBattle spellへ残したい
- EnemyがStormを常用する
- 飛んだ先でCarrierが単独では勝てない
- Retreat routeがない
- 通常移動で十分間に合う

Mobilityは選択肢を増やしますが、**選択肢を使う仕事がなければGemを生みません**。

---

# Counter：敵のFlying carrierを読む

Winged Shoesを見たら、そのCommanderが正面Armyと同じrouteを取るとは限りません。

警戒するのは、

- 後方PD
- Gem Site
- Lab / Fort周辺
- Retreat先
- 孤立したCommander

です。

Counterは、

- 着地点候補へ守備を置く
- Scoutで移動先を読む
- Raid後の退路を塞ぐ
- 単独Carrierを迎撃する
- Storm条件でFlyingを制約する

などです。

機動力へのCounterは「同じ速度で追う」だけでなく、**行きたい場所を危険にする**ことでも成立します。

---

# Army全体との切り分け

よくある誤解は、CommanderへWinged Shoesを装備すれば配下Armyも同じように飛べるというものです。

実際の戦略移動は、Commanderと率いるUnitの能力、地形、移動ルールを合わせて決まります。

したがって、

```text
Commander単独なら届く
Armyを率いると届かない
```

という差をTest gameで確認します。

この差こそ、Winged Shoesを**Raider / courier向け**と**main Army commander向け**で評価し分ける理由です。

---

# よくある失敗

## 飛べるProvinceだけ見て退路を見ない

Raid成功後に包囲され、CarrierとItemを失います。

## Army全体がFlyingになると思う

配下Unitの移動能力を確認していません。

## Boots slot競合を無視する

Reinvigoration等を失い、戦闘Buildが崩れます。

## Stormを忘れる

決戦で期待したFlyingが使えなくなる場合があります。

## 移動力を戦闘力と勘違いする

届いた先で勝てるStats・Script・Resistanceが別途必要です。

---

# Test game checklist

```text
[ ] C5・A2でWinged ShoesがForge可能か確認
[ ] 実際の支払CostをForge画面で確認
[ ] 装備前後のFlying表示を確認
[ ] Commander単独の到達可能Provinceを比較
[ ] 非Flying部隊を率いた場合の到達可能Provinceを比較
[ ] 戦闘内のFlying挙動を確認
[ ] Storm下でのFlying可否を確認
[ ] Boots slot競合を実Buildで確認
[ ] Raid後のRetreat / escape routeを確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 294](../../data/items/by-id/294.md)
- [Flying・Storm・Air機動戦](../../systems/flying-storm.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Thug / Supercombatant装備](../thug-equipment.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI
- Dominions 6 Main Manual — Flying / Movement / Magic Items
- Map移動とStorm下の挙動はCarrier・Army構成ごとにTest gameを優先
