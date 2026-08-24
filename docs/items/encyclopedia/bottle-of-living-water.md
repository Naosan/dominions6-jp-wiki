---
title: "Bottle of Living Water"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 404
---

# Bottle of Living Water

**Bearerが戦闘へ参加すると、封じられたWater Elementalを味方として解放するConstruction 7のBattle-summon Item。**

Bottle of Living WaterはCarrier本人のStatsを強化する装備ではありません。攻略上は、**Misc Slot一つを、毎回の戦闘へ追加のElemental一体を持ち込む権利へ変えるItem**として評価します。

そのため価値は「Elementalが強いか」だけでなく、Carrierの安全、戦闘規模、配置、敵の対Elemental手段まで含めて決まります。

- [Dominions 6.35固定データ — Item 404](../../data/items/by-id/404.md)
- [Magic Item攻略辞典](index.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Ring of Regeneration](ring-of-regeneration.md)

---

# まず何ができるか

6.35固定データでは、Bottle of Living WaterはConstruction 7、Forge要求**W2**のMiscellaneous Itemです。

Item descriptionでは、BottleにWater Elementalが封じられており、戦闘で解放されてBottleのOwner側として戦うと説明されています。

つまり、

```text
Bearerが戦闘へ入る
→ BottleからWater Elementalが解放される
→ 追加Unitとして戦う
```

というItemです。

CasterがWater Elemental召喚SpellをScriptするItemではありません。BearerのMagic Path、Spell slot、戦闘Gemとは別のBattle-start資産として考えます。

---

# Carrier強化ではなく「追加の駒」

通常の装備はCarrier一人を強くします。

Bottle of Living Waterは、Carrierとは別に戦うUnitを追加します。

この違いにより、

- 敵の攻撃対象を分散する
- 敵Formationへ別方向の圧力を掛ける
- ChaffやBodyを一つ増やす
- Carrierが直接近接戦へ入らなくても戦力を供給する
- 小規模戦で初期のUnit数差を作る

ことができます。

ただしElementalがCarrierの命令を細かく再現するとは限りません。Spawn位置、行動、目標選択はBattle Replayで確認します。

---

# 小規模戦ほど一体の比重が大きい

Bottleが持ち込むElementalは、戦闘規模にかかわらずItem一個から得る追加戦力です。

そのため、

```text
5体 vs 5体の戦闘へ1体追加
```

と、

```text
500体 vs 500体の戦闘へ1体追加
```

では相対的価値が大きく異なります。

Bottleは、

- Raider同士の小規模戦
- Assassin対策を含む少人数戦
- PD処理
- Small armyの先頭戦
- Carrierを守るための追加Targetが欲しい場面

で価値を見つけやすくなります。

大規模Battleでは、Elemental一体がBattlefield spellや集中火力へ埋もれる可能性があります。

---

# Battle-only資産として考える

Item descriptionが保証するのは、Elementalが**battleで解放されて戦うこと**です。

恒久的にArmy rosterへ加わる召喚Unitとして計画するのではなく、まずはBattleごとに現れる一時的戦力として扱います。

確認すべきなのは、

- Battle終了後にUnitが残るか
- Bottleが消費されるか
- 次のBattleでも再び発動するか
- BearerがRetreat / Deathした時の扱い

です。

固定Itemとして繰り返し使える想定でも、Test gameで一連の挙動を確認してから高価なCarrierへ渡します。

---

# Carrierは前線へ出す必要がない

Bottleの主目的はElementalを戦場へ追加することです。

Carrier本人に近接能力が不要なら、

- 後方Mage
- 安全なCommander
- Scout系Carrier
- Armyを指揮するが前線へ出ない指揮官

へ持たせる選択肢があります。

ただし「後方に置けば安全」とは限りません。

敵の、

- Flying / Fast raider
- Missile
- Battlefield-wide spell
- Flanking
- Assassination

でCarrierが倒されると、Bottle本体まで失う可能性があります。

Elemental一体のために重要MageをBattleへ出すかは別途判断します。

---

# Spawn位置とFormationの相互作用

Battle-summon Itemは、追加Unitがどこへ現れるかで役割が変わります。

- Carrierの近くに現れるか
- Formation前方へ出るか
- 後衛を守れる位置か
- 敵へすぐ接触するか
- 自軍の射線やSpell targetへ干渉するか

を確認します。

BottleをBodyguard Itemとして採用しても、Elementalが期待した位置に留まらないなら、後衛防御としては不安定です。

**「Unitが増える」ことと「必要な場所を守る」ことは同じではありません。**

---

# Elementalの役割を先に決める

BottleをForgeする時は、Elementalへ何を期待するかを明示します。

## Damage source

敵Unitを倒す役割です。敵Protection、Resistance、Elementalの命中・攻撃方法をTestします。

## Damage sponge

敵の攻撃を受け、Carrierや主力へのDamageを減らす役割です。何Round耐えるかを測ります。

## Formation disruption

敵の進路やTarget selectionを乱す役割です。Spawn位置と敵AIに依存します。

## Tempo gain

Battle開始時から一体追加されることで、敵の最初の数Roundを遅らせる役割です。

期待する役割が曖昧だと、Elementalが強く見えても勝敗への寄与を判断できません。

---

# Water ElementalへのCounterを受ける

追加Unitは万能ではありません。

敵が、

- Elementalへ有効なDamage type
- 高Damage / Armor Negating
- Control
- Banishではなく適切なMagic attack
- 大量のChaff
- Battlefield spell

を持つ場合、Elementalは短時間で処理される可能性があります。

Bottleの評価は「一般的なElementalの強さ」ではなく、**次に戦う敵が一体をどれだけ安く処理できるか**で行います。

---

# Misc Slotの機会費用

BottleはMisc Slotを一つ使います。

同じSlotには、

- Amulet of Antimagic
- Ring of Regeneration
- Girdle of Might
- Spell Focus
- Path Booster
- Resistance Item

を置けます。

Carrier本人がMR不足で倒されるなら、Elemental一体よりAmulet of Antimagicの方がArmy全体の価値を守ることがあります。

比較は、

```text
追加Elementalの価値
vs
Carrierから外れるMisc Itemの価値
```

です。

特にRare Mageへ持たせる場合、Carrier防御を削るCostを重く見ます。

---

# 複数Bottleの価値

複数のBottleを別Carrierへ配れば、複数のBattle-summonを得られる可能性があります。

ただし、

- 同じBattleで重複発動するか
- Spawn位置が競合しないか
- Water Gem投資に見合うか
- Carrier数とMisc Slotが足りるか
- 大規模戦で一体あたりの価値が薄れないか

を確認します。

一個目が強かったからといって、二個目・三個目が同じ限界価値を持つとは限りません。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 7へ到達済み
- W2 Forge Mageを確保できる
- 小規模戦へ追加Unit一体の比重が大きい
- Elementalへ明確な役割がある
- Carrierを比較的安全にBattleへ参加させられる
- Misc Slotを使ってもCarrierの必須防御が残る
- 敵がElementalを安く処理しにくい
- Bottleを複数Battleで再利用できる見込みがある
- Test gameでSpawn位置と行動を確認済み

C7まで研究して作るため、**今すぐ必要な一戦だけの戦力か、繰り返し使うCampaign assetか**を分けます。

---

# Forgeしない・別Itemを選ぶ条件

- 大規模Battleで一体の影響が小さい
- 敵がElementalを簡単に処理できる
- CarrierのMR / Resistance Itemを外せない
- Rare MageをBattleへ出すRiskが高い
- W2・C7へ届く研究とForge turnが重い
- Water GemをBattle magicやBoosterへ回す必要がある
- Spawn位置が任務と噛み合わない
- 恒久的なArmy Unitを求めている

BottleはArmy生産Itemではなく、**Battleごとに追加の駒を買うItem**として判断します。

---

# Counter：ElementalとBearerを分けて考える

敵がBottle of Living Waterを使っている場合、Counter対象は二つあります。

## Elementalを処理する

- 有効なDamage typeを当てる
- Chaffで拘束する
- Controlで無力化する
- 高火力を集中する
- 主力から離れた位置へ誘導する

## BearerとBottleを狙う

- AssassinでBattle前にCarrierを狙う
- Flying / Flankingで後衛へ到達する
- MissileやRemote damageを使う
- Bottleを持つRare Mageへ出戦Riskを強制する

Elemental一体へ過剰なCounterを投入するより、**高価なItemを持つCarrierを危険に晒す**方が効率的な場合があります。

---

# よくある失敗

## 恒久Summonだと思う

Item descriptionはBattleで解放されて戦うことを説明しています。戦略Map上の永久Unitとは分けます。

## Carrier自身も強くなると思う

主効果は別Unitの追加です。BearerのMRやProtectionは別途必要です。

## Spawn位置を確認しない

追加Unitが期待したBodyguardや前衛として動くとは限りません。

## 大規模戦で一体を過大評価する

戦闘規模が大きいほど相対的なUnit数差は小さくなります。

## Rare Mageへ無防備に持たせる

BottleだけでなくCarrier本体まで失うRiskがあります。

## 一個目が強かったので量産する

Water Gem、Carrier slot、敵Counterを含む限界価値を確認します。

---

# Test game checklist

```text
[ ] C7・W2でBottle of Living WaterがForge可能か確認
[ ] Item 404であることを確認
[ ] BearerがBattleへ入るとWater Elementalが解放されることを確認
[ ] Spell scriptや戦闘Gemを使わず発動するか確認
[ ] ElementalのSpawn位置と初期行動を確認
[ ] Battle終了後にElementalが残るか確認
[ ] Bottleが消費されず次のBattleで再発動するか確認
[ ] BearerがRetreat / Deathした場合の扱いを確認
[ ] 複数Bottleが同じBattleで重複発動するか確認
[ ] 小規模戦と大規模戦で勝率差を比較
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 404](../../data/items/by-id/404.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Girdle of Might](girdle-of-might.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Spell Focus](spell-focus.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- Water ElementalがBattleで解放され味方として戦うことはItem descriptionを正本とする
- Spawn位置、Battle後の存続、再利用、複数発動、Bearer死亡時の挙動はBattle Replayと連続Test battleを優先
