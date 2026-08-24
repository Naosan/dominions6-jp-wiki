---
title: "Skull Mentor"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 374
---

# Skull Mentor

**Death GemとForge turnをResearch +14の継続出力へ変え、Construction 5以降の研究速度を押し上げるDeath系Research Item。**

Skull Mentorは戦闘Itemではありません。攻略上は、**一度Forgeした後、研究を続ける各Turnに固定Researchを生む生産設備**として評価します。

- [Dominions 6.35固定データ — Item 374](../../data/items/by-id/374.md)
- [Magic Item攻略辞典](index.md)
- [Owl Quill](owl-quill.md)
- [Lightless Lantern](lightless-lantern.md)
- [Research Item](../research-items.md)

---

# まず何ができるか

6.35固定データでは、Skull MentorはConstruction 5、Forge要求**D2**のMiscellaneous Itemで、装備者へ**Research Bonus +14**を与えます。

Item descriptionでは、死んだMageの頭蓋が所有者の魔法研究を助けると説明されています。

このItemの価値は、

```text
完成したTurnに一度だけ+14
```

ではなく、

```text
研究へ使い続ける各Turnに+14
```

を積み重ねる点にあります。

---

# Research Itemは継続収入

Skull Mentorを装備した研究者がLabでResearchを続けると、ItemのResearch Bonusが毎Turnの研究出力へ加わります。

したがって総価値は、概念的には、

```text
Research +14
×
実際にResearchへ使えたTurn数
```

で増えます。

早くForgeして長く使うほど総Researchは大きくなります。

一方、ゲーム終了直前や目的Research完了直前にForgeしても、回収できるTurnが少なくなります。

---

# 「何Turn使うか」を先に決める

Skull Mentorを作る前に、少なくとも次を数えます。

- 完成するTurn
- 目的Researchへ到達する予定Turn
- 研究者が前線へ出るTurn
- Researchを止める可能性
- Gameが決着する可能性

たとえば、

```text
完成後20Turn研究する
→ +14 × 20Turn分の追加Research
```

と、

```text
完成後3Turnで研究計画が終わる
→ 回収期間が短い
```

では価値が大きく違います。

Gemだけでなく、**残りResearch Turn**が投資判断の中心です。

---

# Construction 5到達後に次の研究を加速する

Skull Mentor自身がConstruction 5を要求するため、研究開始直後から使うItemではありません。

主な役割は、C5到達後に、

- Construction 7・9へ進む
- 別Schoolの中盤・終盤Spellへ進む
- 戦争中もResearch速度を維持する
- Mageを追加Recruitせず研究出力を増やす

ことです。

```text
C5まで研究
→ Skull MentorをForge
→ 以後のResearchを加速
```

という投資曲線になります。

C5を取る理由がSkull Mentorだけなら、他Schoolを遅らせるCostも含めて判断します。

---

# Research +14はCarrierの価値を変える

Skull MentorはResearch Bonusが固定値なので、装備後の研究者は元のResearch能力に+14を加えた役割になります。

候補は、

- 安全な後方Labに常駐できる
- 今後長くResearchを続ける
- 前線に呼び出されにくい
- Misc Slotを戦闘Itemへ使わない
- Disease・Old Age等で早期離脱しにくい

Commanderです。

高価なBattle Mageへ持たせても、すぐ戦争へ出てResearchを止めるなら稼働率が下がります。

**最も強いMageではなく、最も長く研究できるCarrier**を選びます。

---

# 誰でも研究者になるとは限らない

Skull MentorはResearch Bonusを与えますが、装備できるCommanderなら必ずResearch commandを実行できる、と断定して計画するのは危険です。

確認するのは、

- そのCommanderがLabでResearchを選べるか
- 装備前後でResearch値が+14されるか
- Itemを二つ持たせた場合の表示
- Shape changeや特殊状態でResearch可能か

です。

Carrierは実際のCommand画面で確認します。

---

# Owl Quillとの違い

[Owl Quill](owl-quill.md)は低いResearch帯から使いやすいResearch Itemで、Research +6を与えます。

Skull MentorはResearch +14です。

```text
Owl Quill
→ 小さい初期投資
→ 早いTimingから長く回す

Skull Mentor
→ C5・D2が必要
→ 一個あたりのResearch出力が高い
```

という違いです。

比較では、Research Bonusだけでなく、

- 解禁Timing
- Forge access
- 使用Gem種類
- Forge Mageの機会費用
- 残り研究Turn

を見ます。

Owl Quillをすでに量産している国家でも、Air GemとDeath Gemの在庫差によってSkull Mentorを追加する価値があります。

---

# Lightless Lanternとの違い

[Lightless Lantern](lightless-lantern.md)はConstruction 7、F1でResearch +12を与え、Item descriptionではHorror-related riskが警告されています。

Skull MentorはC5・D2でResearch +14です。

pin済み6.35のSkull Mentor descriptionと主要fieldには、Lightless Lanternと同じHorror警告は示されていません。

```text
Skull Mentor
→ C5で高出力
→ Death accessとDeath Gemが必要

Lightless Lantern
→ C7・F1で作りやすい国家が多い
→ Horror-related carrier riskを管理する
```

という比較になります。

ただしSkull Mentorにも、Carrier死亡、Lab raid、Item奪取、Death Gemの機会費用はあります。

---

# Death Gemの機会費用

Skull MentorはDeath系のForge Itemです。

Death Gemは、

- Summon
- Battlefield magic
- Ritual
- Booster
- Weapon・Armor
- 他のResearch Item

にも使います。

そのため、Research +14を得る代わりに、次の戦争で必要なDeath magicを遅らせないかを確認します。

```text
Skull Mentorを作る
→ 将来Researchが増える

Death Gemを温存する
→ 直近の戦争・Summonが強くなる
```

という時間軸の違う投資です。

戦争が目前なら、将来出力より即時戦力が優先される場合があります。

---

# Forge turnの機会費用

D2 MageがSkull MentorをForgeするTurn、そのMageは、

- Research
- Ritual
- Site Search
- 別ItemのForge
- 前線移動

を行えません。

一個目だけでなく量産時には、Forge turnの総数が大きくなります。

特にD2 Mageが希少なら、Death accessを研究設備へ使うことが他の重要任務を圧迫します。

Forge Bonusがある場合でも、Gem costとForge turnは別々に評価します。

---

# Labに置く共有設備として扱う

Skull Mentorは研究者個人へ永続的に固定する必要はありません。

- 前線へ出るMageから外す
- 新しくRecruitした研究者へ渡す
- DiseaseやOld Ageで離脱する前に移す
- 攻撃されそうなFortから退避する

ことで稼働率を維持できます。

```text
Skull Mentor一個
→ 常に誰かがResearch中に装備
```

という状態を目標にします。

F8やItem一覧で所在を管理し、空のLabや移動中Commanderへ置いたままにしないようにします。

---

# Research Fortの安全性

Skull Mentorの価値は長期間の稼働で積み上がるため、CarrierとLabの安全性が重要です。

確認するのは、

- Border Fortではないか
- Stealth Raiderが侵入できるか
- Assassination対策があるか
- Labが破壊・占領されるRisk
- Retreat先があるか
- Itemを後方へ移せるか

です。

高出力Research Itemを一つの前線Fortへ集中すると、そのProvinceを失った時の損失が大きくなります。

生産効率とRisk分散を両立します。

---

# 量産する条件

Skull Mentorを一個作る判断と、複数個量産する判断は別です。

量産価値が高いのは、

- Death Gem incomeが安定している
- D2 Forgerを複数確保できる
- 研究者が十分いる
- 残りResearch量が大きい
- 直近の戦争でDeath Gemを大量消費しない
- 安全なResearch Fortがある
- Itemを常時稼働できる

場合です。

研究者が不足している、または前線動員でResearch commandを維持できないなら、Itemだけ増やしても稼働しません。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- D2 Forge Mageがいる
- 完成後に長いResearch期間が残る
- Research +14を常時使えるCarrierがいる
- Death Gem incomeに余裕がある
- 次の重要Research breakpointが明確
- Forge MageのTurnを払える
- 安全なLabで運用できる
- Owl Quill / Lightless Lanternより資源事情に合う

特に、

```text
Skull Mentorで目的Researchが何Turn早まるか
```

をTest gameやResearch表示から見積もれると判断しやすくなります。

---

# Forgeしない・後回しにする条件

- 直近の戦争でDeath Gemが必要
- D2 MageがRitual・Summon・前線で忙しい
- C5到達後の残りResearchが少ない
- Research commandを続けられるCarrierがいない
- Research FortがRaidされやすい
- 目的Spellへすでに間に合う
- Gold不足でMage Recruitの方が優先
- Owl Quill等の別Gem Research Itemが資源事情に合う
- ゲーム決着が近く回収Turnがない

高いResearch Bonusでも、**稼働期間が短ければ投資効果は小さい**です。

---

# Counter：Research設備として狙う

敵がSkull Mentorを量産している場合、個々のItemは直接戦闘へ出てこなくても、将来のResearch差を作ります。

Counterは、

- Research FortをRaidする
- D2 ForgerをAssassinationで狙う
- Death Gem income provinceを奪う
- Labを破壊・占領する
- 前線圧力を掛け、研究者を戦争へ動員させる
- Item carrierの退路を塞ぐ
- 研究差が開く前に戦争Timingを早める

ように、**Skull Mentorが稼働するTurn数を減らす**方向で考えます。

Item自体を奪えなくても、Research commandを止めれば出力を失わせられます。

---

# よくある失敗

## Research +14だけを見て即量産する

Death Gem、D2 Forge turn、Carrier、残りResearch Turnを同時に確認します。

## 前線Mageへ持たせたまま出兵する

Research Itemが戦場へ出て稼働を止め、Carrier死亡で失われるRiskも増えます。

## 研究できないCommanderへ渡す

実際のResearch commandと装備後表示を確認します。

## 終盤に作りすぎる

目的Researchが終わる前に回収できるTurnが少なくなります。

## 一つのBorder Fortへ集中する

Raid一回で研究設備とCarrierをまとめて失う可能性があります。

## Death Gemの即時戦力を無視する

Research投資のために、必要Summon・Battle magic・Boosterが間に合わなくなることがあります。

---

# Test game checklist

```text
[ ] C5・D2でSkull MentorがForge可能か確認
[ ] Item 374であることを確認
[ ] 装備前後でResearchが+14されることを確認
[ ] CarrierがResearch commandを選べることを確認
[ ] 一Turn後のResearch進捗差を確認
[ ] Owl Quill / Lightless Lanternとの出力を比較
[ ] 複数Research Item装備時の表示を確認
[ ] 前線移動・Battle時にResearchが止まることを確認
[ ] Carrier間で受け渡して稼働を継続できるか確認
[ ] 目的Research到達Turnが何Turn変わるか記録
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 374](../../data/items/by-id/374.md)
- [Owl Quill](owl-quill.md)
- [Lightless Lantern](lightless-lantern.md)
- [Skull Staff](skull-staff.md)
- [Research Item](../research-items.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- Dominions 6 Main Manual — Research / Forge Item / Lab
- Research command・装備Bonus・到達Turnはゲーム内Research表示を最終確認
