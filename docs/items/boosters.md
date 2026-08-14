---
title: Magic Path Booster
status: expanding
verified_version: "6.35"
last_verified: "2026-08-14"
---

# Magic Path Booster

Magic Path Boosterは、装備中のMageのPathを上げるItemです。

その本当の価値は「Spellを少し強くする」ことではなく、

> **新しいSpell → 新しい召喚 → 新しいMage → 次のBooster → Global**

という技術連鎖を開くことです。

---

# Boosterでできること

- 高級Ritualへ届く
- Army-wide Battle Spellへ届く
- Spell Fatigueを減らす
- 上位ItemをForgeする
- Mage召喚からMagic diversityを得る
- Empowermentを回避する
- Global casterを作る

---

# Booster Chain

例：

```text
E2 Mage
→ Earth Boots等でE3
→ E3 Item / Summon / Ritual
→ 高Earth Mageまたは次のBooster
→ E4～5の戦略魔法
```

```text
N1 independent Mage
→ Thistle Mace等でN2
→ Poison Ward / Summon / Site Search
→ 召喚Nature Mage
→ N3～4へ
```

最初のBooster自体より、**最終的に何へ到達するか**を評価します。

---

# Path別の代表的な考え方

!!! note
    Item名、Construction level、要求Path、Gem costはPatchで変わり得ます。下記はBooster chainを理解するための代表例です。Forge前にゲーム内またはMod Inspectorで確認してください。

## Fire

代表的なFire BoosterやFire Gem補助Itemから、

- 高級Fire Elemental
- Fire Storm
- Global
- Fire Artifact

へ進みます。

Fire MageはBattlefield spellのFatigueが重いため、要求Pathへ届いた後もさらにPathを上げる価値があります。

## Air

Winged Helmet、Bag / Wind系Booster等から、

- Storm
- Arrow Fend
- Fog Warriors
- Wrathful Skies
- Air Queen / high summon

へ進みます。

Storm Powerは戦闘中だけなので、Forge / RitualのA要求には使えません。

## Water

Water Bracelet、Robe of the Sea等を組み合わせ、複数段階上げやすいPathです。

- 高級Water Elemental
- Grip of Winter
- Sea King / underwater summon
- Water Global

へ進みます。

装備Slot競合に注意します。

## Earth

Earth Bootsは代表的な低級Boosterです。

E2 MageをE3へし、Forge discount、上位Armor、Earth summon、Globalへ進めます。

戦闘中はさらにSummon Earthpowerで上げられますが、Ritual / Forgeには使えません。

## Astral

Crystal Coin、Starshine Skullcap等から高Astralへ進みます。

AstralはItemだけでなくCommunionによって大幅に上げられるため、

- 戦略Ritual：Item Booster
- 戦闘：Communion

と分担します。

## Death

Skull Staff等から、

- Darkness / Rigor
- Wraith / Lich
- Tartarian級召喚
- Death Global

へ進みます。

召喚したDeath Mageが次のBoosterをForgeする連鎖が重要です。

## Nature

Thistle Mace等でN1 independentを実用化できます。

- Poison Ward
- Foul Vapors
- Mass Regeneration
- Nature Mage召喚
- Gift of Health

へ進みます。

## Glamour

GlamourはDom6で追加されたため、古いAir / Illusion Item表を使わず現行データを確認します。

Luck、Dream、Illusion、Stealth系Boosterから高級Glamour Spellへ進みます。

## Blood

Blood BoosterはBlood Hunt、Demon召喚、高級Ritualへ影響します。

SabbathとHell Powerは戦闘中Boostなので、Forge / RitualではItem・Empowerment・高Path召喚を使います。

## Holy

Holy levelを上げるItem・Artifactは希少で、国家・Unique Item依存です。

Throne claim、Divine Spell、Priest能力への影響を確認します。

---

# Item BoosterとCombat Boost

| 方法 | Battle Spell | Ritual | Forge | 恒久性 |
|---|---:|---:|---:|---|
| Booster Item | ○ | ○ | ○ | 装備中 |
| Self boost Spell | ○ | × | × | 一戦 |
| Gem boost | ○ | × | × | 一Cast |
| Communion / Sabbath | ○ | × | × | Communion中 |
| Empowerment | ○ | ○ | ○ | 永続 |

「戦闘ではPathへ届くが、ItemをForgeできない」という違いに注意します。

---

# Boosterの優先順位

## S：国家の新Path accessを開く

例：

- N1をN2へしてPoison対策
- E2をE3へしてForge chain
- D3をD4へして高級召喚
- S4をS5へしてGateway / Global

## A：Army-wide Spell担当

一人のCasterが100人を強化するなら投資回収が早くなります。

## B：Battle MageのFatigue軽減

同じSpellを多くCastするMageへ有効です。

## C：通常攻撃Spellを少し強くするだけ

他のMageへ同じGemを使う方がよい場合があります。

---

# Boosterを保護する

BoosterはCarrier死亡時に失われ、敵に奪われる可能性があります。

## 後方専任

Forge / Ritual担当は前線へ出しません。

## 戦闘用と戦略用を分ける

同じPathのBoosterを二個作り、

- 後方Forge / Ritual
- 前線Army spell

へ分ける場合があります。

## 戦闘後に戻す

次の戦闘で不要ならLabへ戻し、Rare ItemをRaiderへ持たせ続けないようにします。

## MR / Elemental防御

高価なBooster carrierはSoul Slay、Magic Duel、Lightning、Assassinの標的になります。

---

# Booster回収計算

Booster作成には、

- Gem
- Forge turn
- Construction research
- 装備Slot
- Carrier Risk

が必要です。

次の式で考えます。

```text
Booster投資
<
Boosterで新しく得るSpell・Item・Summonの価値
× 使用回数
```

一戦だけ使うBoosterでも、ThroneやEnemy主力Armyを取れるなら十分回収できます。

---

# Empowermentとの比較

## Boosterが優れる

- 安い
- 他Mageへ移せる
- 死亡時に再利用・奪取の可能性
- Slotが空いている

## Empowermentが優れる

- 国家にPath自体がない
- Item slotが足りない
- Multiple boosterでも届かない
- Unique Mageを長期Global casterへする
- Booster chainの最初の一段が存在しない

Empowermentは高価ですが、一つの新Pathから複数Booster / Summonが開くなら戦略的投資になります。

---

# Booster計画表

| 項目 | 記入内容 |
|---|---|
| 最終目的 | Spell / Summon / Item / Global |
| 最終要求Path | 例：N4 |
| 現在のCaster | 例：N2 |
| Booster 1 | 要求Path / Gem / Slot |
| Booster 2 | 要求Path / Gem / Slot |
| 戦闘Boost | 使えるか |
| Communion | 必要Slave数 |
| Total Gem | 合計 |
| Carrier Risk | 後方 / 前線 |
| 代替 | Pretender / Summon / Indie / Empowerment |

---

# よくある失敗

## 使う目的なしにBoosterを作る

装備しても現在のResearchで新しいSpellへ届かなければ、GemとForge turnを寝かせます。

## 全Mageへ配る

Army-wide担当一人で足りる場合があります。

## Slot競合を忘れる

Boots、Helmet、Miscを使うと、Strength、Flying、MR、Resistance等を装備できません。

## Rare BoosterをThugへ渡す

国家のMagic accessと戦闘装備を同時に失います。

## Old guideのConstruction levelを使う

Dom6ではItemのSchool / level / Glamour分類が変わっています。

---

## 関連ページ

- [Magic Item](index.md)
- [Magic Path Boosting](../magic/boosting.md)
- [Research](../magic/research.md)
- [Gem](../magic/gems.md)
- [Communion](../magic/communions.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
