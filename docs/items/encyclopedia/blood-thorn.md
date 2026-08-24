---
title: "Blood Thorn"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 94
---

# Blood Thorn

**Blood MageのBlood Pathを+1し、命中した相手から生命を吸収する、Construction 7の片手武器型Booster。**

Blood Thornは後方Mageへ持たせるだけのPath Itemでも、誰に渡しても回復する万能武器でもありません。攻略上は、**Blood +1とHit依存のHP sustainを一つの手Slotへまとめた、Caster / melee hybrid向けItem**として評価します。

- [Dominions 6.35固定データ — Item 94](../../data/items/by-id/94.md)
- [Magic Item攻略辞典](index.md)
- [Magic Path Booster](../boosters.md)
- [Brazen Vessel](brazen-vessel.md)
- [Ring of Regeneration](ring-of-regeneration.md)

---

# まず何ができるか

6.35固定データでは、Blood Thornは、

- Construction 7
- Forge要求 **B3**
- 片手武器
- Weapon record 688
- **Blood +1**

を持ちます。

Weapon record 688は、

- Attack +2
- Defence 0
- Length 0
- 1 attack

の近接武器です。

Item descriptionでは、

- 命中した相手の生命を吸収し、装備者の生命力へ加える
- Blood Mageが使うとBlood magic skillを高める

と説明されています。

したがって、

```text
Blood +1
＋
命中時の生命吸収
＋
片手武器としての近接攻撃
```

を同時に持つItemです。

---

# BoosterとWeaponを別々に評価する

Blood Thornには二つの用途があります。

```text
Booster用途
→ Blood +1でSpell / Ritual / Forgeの閾値を越える

Weapon用途
→ 近接Hitから生命を吸収してCarrierを維持する
```

両方を使えるCarrierでは複合価値が高くなります。

一方、後方Blood Mageへ持たせるだけなら生命吸収はほぼ使いません。

近接Carrierへ持たせても、そのUnitがBlood MageでなければBlood +1部分を利用できない可能性があります。Item descriptionはBlood skill上昇の対象をBlood Mageとしているため、Pathless bearerの表示はTest gameで確認します。

---

# Blood +1は新しい仕事で評価する

Path Boosterとして見る場合、装備前後で、

- 新しくCastできるBattle spell
- 新しく実行できるBlood Ritual
- 新しくForgeできるBlood Item
- 同じSpellを高PathでCastした場合のFatigue
- Sabbathなしで届くPath
- 高位Demon・Commander summonへの到達
- 次のBooster chain

がどう変わるかを確認します。

```text
B3 Mage
→ Blood ThornをForge・装備
→ B4として目的Ritual / Spell / Forgeへ到達
```

が基本です。

B+1しても現在のResearchやBlood Slave incomeでは役割が増えないなら、その時点ではBooster部分が寝ています。

---

# C7・B3という入口条件

Blood ThornはB3でForgeできますが、Construction 7まで必要です。

[Brazen Vessel](brazen-vessel.md)はC5で解禁される一方、B5を要求します。

```text
Blood Thorn
→ C7
→ B3 Forger
→ 片手武器
→ 生命吸収

Brazen Vessel
→ C5
→ B5 Forger
→ Misc Slot
→ 後方運用しやすい
```

という違いがあります。

国家がB3へは届くがB5へ届かない場合、C7 Researchを進めてBlood Thornを最初の恒常Boosterにする価値があります。

逆に、Pretender、Hero、Summon等ですでにB5 Forgerがいるなら、C5のBrazen Vesselを先に作れる場合があります。

---

# 生命吸収は「命中して初めて働く」

Blood Thornの生命吸収は、装備しただけで毎Round HPを回復する効果として考えません。

重要なのは、

- Carrierが接敵できるか
- Attackが敵Defenseへ届くか
- 一Roundに何回Hitを作れるか
- 相手から吸収できる有効な生命があるか
- Hitする前に倒されないか
- 敵を倒し切った後も次のTargetへ届くか

です。

```text
命中する
→ 生命吸収が発生
→ CarrierのHP sustainへ変換

命中しない / 接敵しない
→ 生命吸収部分はゼロ
```

となります。

正確なDamage・吸収・回復量は、Targetの性質とBattle処理を含むためBattle Replayで確認します。

---

# Regenerationとは別のSustain

[Ring of Regeneration](ring-of-regeneration.md)は、条件を満たすCarrierへ継続的なRegenerationを与えます。

Blood ThornはHitが必要です。

```text
Ring of Regeneration
→ 攻撃が外れても回復機会がある
→ Misc Slot
→ Inanimate等の制限を確認

Blood Thorn
→ 命中した時だけ生命吸収
→ Weapon Slot
→ Damageと回復を同じ行動へまとめる
```

という違いです。

高Attackで継続的に殴れるCarrierならBlood ThornのSustainが機能しやすくなります。

Kite、高Defense、Control、遠距離攻撃で接敵を拒否される相手にはRing等の方が安定する場合があります。

---

# 片手武器であることの価値

Blood Thornは1-h weaponなので、もう一方の手へShieldを装備できます。

典型的には、

```text
Blood Thorn
＋ Shield
＋ Armor / MR / Resistance
```

とし、

- ThornでBlood +1と生命吸収
- Shieldで被Hitを減らす
- ArmorやMiscでBurst・MR・Fatigueを補う

役割分担を作ります。

ただしHand Slotには、

- 別のPath Booster
- 高Damage Weapon
- Range Weapon
- 両手Booster
- Staff / Matrix系Item

も入ります。

Blood +1だけが目的なら、Weapon Slotを使うことが本当に安いかを比較します。

---

# Carrierは「Blood Mageだから」だけで選ばない

Blood Thornと相性が良いCarrierは、

- 素でBlood accessを持つ
- B+1で具体的な仕事が増える
- 近接へ入っても生存できる
- Attackが十分高い
- Shield等で防御を組める
- Fatigueで止まりにくい
- 生命吸収を使うHit数を確保できる

Unitです。

高Blood Mageでも、

- HPが低い
- Protectionが低い
- Attackが低い
- 高価で失えない
- 後方Scriptだけで仕事が完結する

なら、近接へ入れず単なるBoosterとして使います。

「Blood MageだからThornで殴らせる」のではなく、**Mage本体がmelee Carrierとして成立するか**を先に見ます。

---

# 後方Boosterとして使う

Blood Thornを殴らないMageへ持たせても、Blood +1は利用できます。

Ritual・Forge用なら、

- Hand Slotの戦闘上のCostが小さい
- 一本を複数Mageで共有できる
- B3からB4へ上げて次の仕事へ届く
- 前線喪失Riskを避けられる

ため、安定したInfrastructureになります。

```text
LabでThornを装備
→ Ritual / Forge
→ 使用後に別Mageへ渡す
```

という運用です。

この場合、生命吸収は使わなくても問題ありません。Itemの二つの効果を必ず同時に使う必要はありません。

---

# Brazen Vesselとの違い

[Brazen Vessel](brazen-vessel.md)もBlood +1を与えます。

| Item | 解禁 | Forge要求 | Slot | 固有効果 |
|---|---:|---|---|---|
| Blood Thorn | C7 | B3 | 片手Weapon | 命中時の生命吸収 |
| Brazen Vessel | C5 | B5 | Misc | 手を空けた後方Booster |

攻略上は、

```text
Blood Thorn
→ B5へ届かない
→ C7まで進める
→ Weapon Slotを使える
→ 近接Hitも価値に変える

Brazen Vessel
→ B5 Forgerがいる
→ C5から使いたい
→ Hand Slotを別装備へ残したい
→ 後方Ritualistへ持たせる
```

と使い分けます。

両方を同時装備できるBlood MageならPathをさらに伸ばせますが、目的RitualとSlave costを先に決めます。

---

# Blood economyとの接続

Blood +1で高位Ritualへ届いても、Blood Slaveが不足していれば実行できません。

確認するのは、

- 毎TurnのBlood Slave income
- Huntへ使うMage数
- Unrest管理
- Ritual一回のSlave cost
- 前線へのSlave輸送
- Thornを持つMageの本来の仕事

です。

```text
Path requirementを越える
＋
Slaveを継続供給できる
→ 新しいBlood役割が成立
```

となります。

Blood ThornはBlood Slaveを自動生成するItemではありません。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 7へ到達済み、または明確に向かっている
- B3 Forgerを確保できる
- B+1で具体的なSpell・Ritual・Forgeが解禁される
- B5のBrazen Vesselへ届かない
- Weapon Slotが空いている
- 近接Carrierなら十分なAttackと生存力を持つ
- Blood Slaveを目的Ritualへ供給できる
- 一本を複数Turn・複数Mageで共有できる

近接用途なら、

```text
Thornありで任務成功率が上がる
```

ことを複数回のTest battleで確認します。

---

# Forgeしない・別Itemを選ぶ条件

- C7 Researchが他の重要Schoolを大きく遅らせる
- B+1しても役割が増えない
- Blood Slave incomeが目的Ritualを支えられない
- Carrierが近接へ入るとすぐ倒れる
- Attack不足で生命吸収が発生しない
- Hand Slotに別Booster・Shield・Weaponが必須
- B5 ForgerがいてC5のBrazen Vesselで足りる
- 生命吸収よりRegeneration・MR・Resistanceが敗因へ直結する
- 高価なBlood Mageを前線へ出すRiskが大きすぎる

Booster部分とWeapon部分のどちらも使わないなら、在庫にする理由はありません。

---

# Counter：殴らせない、または別軸で落とす

敵のBlood Thorn Carrierに対しては、生命吸収の回転を止めることが重要です。

- 高DefenseでHit数を減らす
- Glamour・Displacement等で攻撃を外させる
- Kite・Flying・Rangeで接敵を遅らせる
- Chaffを使う場合もCarrierを目的地へ通さない
- Fatigue・Stun・Paralyzeで攻撃回数を減らす
- MR-based Controlで近接能力以外を攻める
- Burst damageで吸収前に倒す
- Assassin・RaidでRitualistを戦場前に狙う
- Gem / Blood Slave carrierを落として高Blood Scriptを止める

ように、

```text
生命吸収を耐える
```

だけでなく、

```text
生命吸収を発生させない
```

Counterを考えます。

---

# よくある失敗

## 装備しただけで回復すると思う

生命吸収はHitが前提です。

## Blood Mageを無理に近接へ出す

高価なRitualistをWeapon効果のためだけに失うことがあります。

## Attackを確認しない

HitしなければDamageもSustainも発生しません。

## Blood +1でSlaveも増えると思う

Path BoosterとBlood Slave economyは別です。

## C7を忘れる

Forge要求はB3でも、Construction 7が必要です。

## Brazen VesselとSlotを比較しない

Hand SlotとMisc Slot、C7/B3とC5/B5で役割が大きく変わります。

---

# Test game checklist

```text
[ ] C7・B3でBlood ThornがForge可能か確認
[ ] Item 94 / Weapon record 688であることを確認
[ ] 1-h weaponとして片手Slotを使うことを確認
[ ] Attack +2、Length 0、1 attackの表示を確認
[ ] Blood Mage装備時にBloodが+1されることを確認
[ ] B0のPathless bearerでBlood表示がどうなるか確認
[ ] 命中時に生命吸収が発生することをBattle Replayで確認
[ ] Damage量とHP回復量を複数Targetで比較
[ ] Undead / Inanimate等のTargetで吸収挙動を確認
[ ] Shield併用Buildと両手・別Weapon Buildを比較
[ ] 後方Ritual / Forge用途で目的Pathへ届くか確認
[ ] Brazen VesselとのResearch・Forge要求・Slot差を比較
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 94](../../data/items/by-id/94.md)
- [Magic Path Booster](../boosters.md)
- [Brazen Vessel](brazen-vessel.md)
- [Ring of Regeneration](ring-of-regeneration.md)
- [Girdle of Might](girdle-of-might.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / weapons / effects_weapons / Item description
- Dominions 6 Main Manual — Blood Magic / Life Drain / Weapon / Forge Item
- 生命吸収のDamage・回復、Target制限、Pathless bearerの実挙動はゲーム内表示・Battle Replay・Test gameを最終確認
