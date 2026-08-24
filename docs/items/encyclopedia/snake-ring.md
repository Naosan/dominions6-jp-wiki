---
title: "Snake Ring"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-25"
item_id: 315
---

# Snake Ring

**Poison Resistance +30とItem spellのPoison TouchをMisc Slotへまとめ、Poison戦の防御と接触時の反撃手段を得るConstruction 1の複合Ring。**

Snake RingはDisease対策でも、常時Poison Auraでもありません。攻略上は、**重要Commander一体をPoison damageから守ることを主目的とし、近距離で行動できるCarrierだけPoison Touchも利用するItem**として評価します。

- [Dominions 6.35固定データ — Item 315](../../data/items/by-id/315.md)
- [Magic Item攻略辞典](index.md)
- [Resistance Item](../resistance-items.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Elemental Armor](elemental-armor.md)

---

# まず何ができるか

6.35固定データでは、Snake Ringは、

- Construction 1
- Forge要求 **N1**
- Miscellaneous Slot
- **Poison Resistance +30**
- Item spell **Poison Touch**

を持ちます。

Item descriptionも、

- 装備者をPoisonからほぼ完全に守る
- 接触した敵をPoisonにする能力を与える

と説明しています。

したがって、二つの役割を分けて読みます。

```text
防御
→ Poison Resistance +30

攻撃
→ Poison Touchという接触Item spell
```

防御部分は装備中に働きますが、Poison Touchは自動Auraや自動反撃と決めつけず、Battleでの選択・発動条件を確認します。

---

# 主役はPoison Resistance +30

Snake Ringの最も安定した価値は、Poison damageへの防御です。

候補になる脅威は、

- Foul Vapors
- Poison cloud
- Poison weapon
- Snake / Spider等のPoison attack
- Poisonを伴うSummon
- 長期戦で蓄積するPoison damage

です。

高HP・高ProtectionのCarrierでも、Poisonが蓄積し続ければ通常攻撃とは別の敗因になります。

```text
物理HitをArmorで耐える
＋
Poison componentをSnake Ringで抑える
```

という防御層を作れます。

ただし、実際の軽減は装備前後のPoison Resistance表示とBattle Replayで確認します。

---

# Diseaseは別

Poison Resistance +30を持っていても、Diseaseを自動的に防ぐItemとして扱いません。

- Disease
- Plague
- Disease Cloud
- 老化や病気による長期劣化
- Healerが対象とするAffliction

はPoison damageとは別の問題です。

```text
Poison damage
→ Poison Resistance

Disease
→ Disease固有の防御・Healer・発生源除去
```

と分けます。

Snake Ringを付けて病気になったとしても、固定効果と矛盾しているわけではありません。

---

# Poison Touchは接触が必要

Poison TouchのSpell descriptionでは、

- TargetへTouchする
- 命中には成功したAttack rollが必要
- ArmorはProtectionを提供しない

と説明されています。

したがって、

```text
接触できる
＋ Attack rollが成功する
→ Poison TouchがTargetへ届く

接触できない / Attack rollが失敗
→ Offensive valueは出ない
```

という条件付きの攻撃です。

Armorを無視することと、必ず命中することは別です。

高Defense、距離、Bodyguard、Chaff、移動阻害でTouchを拒否されると、攻撃部分は働きません。

---

# Passive Poison Auraではない

Snake Ringを装備しただけで、周囲の敵へ毎Round自動的にPoisonを撒くItemとして扱いません。

BaseIではPoison Touchが`itemspell`として記録されています。

そのため、Test gameでは、

- Spell selectionへ表示されるか
- Pathを持たないBearerでも使用できるか
- Scriptで選択できるか
- AIがいつ使用するか
- 一回の使用に何Action / Fatigueを払うか
- Melee attackとどちらを選ぶか

を確認します。

攻略記事では、未確認のAI優先順位や自動発動を固定仕様にしません。

---

# Construction 1でFoul Vapors準備を始められる

Snake RingはC1・N1で作れます。

Foul Vapors等の高位Battle planそのものより早く、Carrier用のPoison対策在庫を用意できます。

これは、

- 自国が後でPoison battlefieldを使う
- 敵Nature NationがPoison戦へ進む
- Poison cloud持ちのSummonと戦う
- ThugをPoison sourceへ接触させる

計画で価値があります。

ただし、将来使うかもしれないという理由だけで大量生産すると、Nature GemとForge turnが長く寝ます。

直近の戦場とCarrier数から必要個数を決めます。

---

# 自国のPoison戦を成立させる

Snake Ringは敵PoisonへのCounterだけではありません。

自国がPoison battlefieldを作る場合、

- Caster本人
- 前へ出るThug
- Communion / Sabbath Master
- Poison cloud内でScriptを続ける重要Mage
- Retreatを遅らせるCommander

を守るために使えます。

```text
敵だけをPoisonへ晒す
＋
自軍の中核だけResistanceで残す
```

という非対称を作ります。

ただしArmy全体を守るItemではないため、通常兵や未装備Mageが崩れる問題は別に処理します。

---

# 相性の良いCarrier

防御目的では、

- Foul Vapors下でCastを続けるMage
- Poison cloudへ入るThug
- 高HPでPoisonを長く蓄積しやすいCommander
- 高Protectionだが素Poison Resistanceが低いCarrier
- Poison weapon持ちへ接触するRaider
- Army-wide Resistanceから外れる単独行動Unit

が候補です。

Poison Touchまで使うなら、さらに、

- 接触まで生き残れる
- 移動速度が足りる
- Attack rollを通せる
- Touchへ行動を使う価値がある
- 通常WeaponやSpellよりPoison Touchが有効

必要があります。

防御Carrierと攻撃Carrierを同じ基準で選びません。

---

# Fragile MageをTouchのために前へ出さない

Snake Ringを後方Mageへ持たせるだけでも、Poison Resistance +30は働きます。

Poison Touchを持つからといって、

- HPが低い
- Protectionが低い
- Attackが低い
- 高価で失えない
- 後方Scriptで仕事が完結する

Mageを近接へ送る必要はありません。

```text
防御価値だけ使う
→ 十分に正しい

防御とTouchを両方使う
→ Carrierがmelee任務にも適合する時だけ
```

です。

Itemの全効果を毎戦闘使い切ることより、Carrierを失わないことを優先します。

---

# Ring of Regenerationとの違い

[Ring of Regeneration](ring-of-regeneration.md)は、受けたDamageを継続的に回復するItemです。

Snake RingはPoison ResistanceでPoison componentを抑えます。

```text
Snake Ring
→ Poisonの入口を減らす
→ Poison専門
→ Poison Touchも持つ

Ring of Regeneration
→ 受けたHP Damageを回復する
→ Poison以外の継続Damageにも役立つ場合がある
→ 生物Carrier等の適用条件を確認
```

Poison蓄積が大きい戦場では、Regenerationだけで追いつくとは限りません。

逆にPoisonが来ない戦場では、Snake Ringの防御部分は働かず、Regenerationの方が広い場合があります。

---

# Elemental ArmorではPoisonを守らない

[Elemental Armor](elemental-armor.md)はFire・Cold・Shock ResistanceをArmor Slotへまとめます。

Poison Resistanceはその三属性とは別です。

```text
Elemental Armor
→ Fire / Cold / Shock

Snake Ring
→ Poison
```

と役割が分かれます。

複数属性とPoisonを同時に受けるCarrierでは、Elemental ArmorとSnake Ringを組み合わせる余地があります。

ただし重装のFatigue、Misc Slot競合、MR不足を同時に確認します。

---

# 他のC1 Resistance Ringとの違い

- [Ring of Fire](ring-of-fire.md)：Fire Resistance +15
- [Ring of Tamed Lightning](ring-of-tamed-lightning.md)：Shock Resistance +15
- [Ring of Frost](ring-of-frost.md)：Cold Resistance +15
- Snake Ring：Poison Resistance +30とPoison Touch

Snake Ringは固定Resistance値が+30で、さらにItem spellを持つ点が異なります。

ただし「数値が大きいから上位」という意味ではありません。

Enemy Damage typeがFireならRing of Fireが働き、PoisonがなければSnake Ringの+30は使われません。

---

# Misc SlotのOpportunity Cost

Snake RingはMisc Slotを一つ使います。

競合するのは、

- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Amulet of Resilience](amulet-of-resilience.md)
- [Girdle of Might](girdle-of-might.md)
- Path Booster
- Mobility Item
- 他属性Resistance Ring

です。

Poisonを耐えても、

- MR-based Controlで止まる
- Fatigue 100へ達する
- 通常Damageを回復できない
- Boosterを外して必要SpellがCastできない

なら任務は失敗します。

Poisonが本当に最大の敗因かを先に確認します。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 1へ到達済み
- N1 Forgerを確保できる
- 敵がPoison damageを実際に使う
- 自国がPoison battlefieldを利用する
- 一体の重要Commanderを守れば戦術が成立する
- 素Poison Resistanceが不足している
- Army-wide対策のResearchが間に合わない
- Misc SlotをPoison対策へ割ける
- Poison Touchも使える近接Carrierがいる
- Ringを戦線間で持ち回せる

最初の三条件だけでも防御Itemとして成立します。Poison Touchを使えないことは、必ずしもForge失敗ではありません。

---

# Forgeしない・後回しにする条件

- 敵がPoison damageをほとんど使わない
- Carrierの素Poison Resistanceで十分
- Army-wide SpellやBlessで必要値へ届く
- 問題がDiseaseでありPoisonではない
- 敗因がPhysical、MR、Shock、Fire、Coldにある
- Misc Slotへ必須BoosterやMR Itemがある
- Army全体がPoisonで崩れ、一体だけ守っても勝てない
- Poison CasterやCloud sourceを先に倒す方が安い
- Nature GemとForge turnを別のTimingへ使う必要がある

Poison Touchだけを目的にFragile Mageへ作る優先度も低くなります。

---

# Counter：Touchを拒否し、Poison以外で攻める

敵CarrierがSnake Ringを持つ場合、二つの効果へ別々に対応します。

Poison ResistanceへのCounterは、

- Fire / Cold / Shock / AcidへDamage typeを変える
- 高Damage物理を使う
- MR-negates Controlや即死系を使う
- Fatigue、Morale、Positioningを攻める
- Ring装備で失われたMR / Regeneration / Boosterを突く

です。

Poison TouchへのCounterは、

- 距離を維持する
- ChaffやBodyguardで接触を遅らせる
- 高DefenseでAttack rollを通しにくくする
- Flying / Ranged / ControlでCarrierを先に止める
- 高Poison ResistanceまたはPoisonへ強いTargetを当てる
- Touchへ行動を使わせ、主任務を遅らせる

です。

ArmorはPoison TouchへのProtectionを提供しないと説明されていますが、命中拒否とResistanceは別の防御層です。

---

# よくある失敗

## Diseaseも防ぐと思う

PoisonとDiseaseは別です。

## 周囲へ自動でPoisonを撒くと思う

Poison TouchはItem spellとして記録されています。Auraや自動反撃とは限りません。

## Armor無視だから必中と思う

成功したAttack rollが必要です。

## Fragile MageをTouchのために前へ出す

防御価値だけ使う方が安全な場合があります。

## Army全体がFoul Vaporsへ耐えると思う

守られるのは装備者です。Army-wide対策は別です。

## Regenerationの代替として何にでも使う

Snake RingはPoison専門です。通常Damageや別属性には別防御が必要です。

## Poison TouchのAI使用を未確認でScriptへ組み込む

選択可否、使用Timing、Fatigue、TargetingをTestします。

---

# Test game checklist

```text
[ ] C1・N1でSnake RingがForge可能か確認
[ ] Item 315であることを確認
[ ] Poison Resistance +30が装備画面へ反映されることを確認
[ ] 装備前後のPoison Resistance合計を記録
[ ] Foul Vapors下のPoison蓄積と生存Roundを比較
[ ] Poison cloud / Poison weaponに対する結果を比較
[ ] Diseaseを防ぐItemではないことを確認
[ ] Poison TouchがItem spellとして表示されるか確認
[ ] Pathless Bearerでも使用できるか確認
[ ] Script選択とAI使用Timingを確認
[ ] Poison Touchに成功したAttack rollが必要か確認
[ ] ArmorがProtectionを提供しないことを比較
[ ] 高Defense Targetへの命中率を比較
[ ] TargetのPoison Resistanceで結果がどう変わるか確認
[ ] Poison Touch一回のAction / Fatigueを確認
[ ] Ring of Regenerationとの防御結果を比較
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 315](../../data/items/by-id/315.md)
- [Resistance Item](../resistance-items.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Elemental Armor](elemental-armor.md)
- [Ring of Fire](ring-of-fire.md)
- [Ring of Tamed Lightning](ring-of-tamed-lightning.md)
- [Ring of Frost](ring-of-frost.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Amulet of Resilience](amulet-of-resilience.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description / Poison Touch Spell description
- BaseI: C1 / N1 / Miscellaneous / Poison Resistance +30 / itemspell Poison Touch
- Item description: Poisonへの強い防御と、接触した敵をPoisonにする能力
- Poison Touch description: 成功したAttack rollが必要で、ArmorはProtectionを提供しない
- Item spellの選択可否、Pathless Bearer、AI使用Timing、Action / Fatigue、Target Resistanceとの相互作用はTest gameとBattle Replayを優先