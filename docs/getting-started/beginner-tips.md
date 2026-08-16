---
title: 初心者向けTips
page_type: guide
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-16"
---

# 初心者向けTips

Dominions 6で最初に必要なのは、全ルールの暗記ではなく、毎Turnの判断を整理する少数の原則です。

ここでは、国家が変わっても使える考え方をまとめます。

---

## まず操作で迷わないために

Dominions 6は、Map、Recruit、Army Setup、Research、Battle Replayで使える操作が変わります。最初から全Shortcutを暗記する必要はありません。

最優先で覚えるのは、**分からない画面で`?`を押すこと**です。その画面で利用できるShortcut一覧が表示されます。Keyboard配列によっては`Shift`＋`/`で`?`を入力します。

| 操作 | Key / Mouse | 用途 |
|---|---|---|
| 画面別Help | `?` | 現在の画面で使えるShortcutを確認する |
| 詳細確認 | 右Click | Unit、Commander、Spell、Itemなどの詳細を見る |
| Message | `M` | 前Turnの戦闘、Event、建設結果を読む |
| Recruit | `R` | 選択Provinceで兵士・Commanderを雇う |
| Army Setup | `T` | UnitをCommanderへ配属し、FormationとScriptを設定する |
| Commander命令 | `Space` | Research、Site Search、Forgeなどの命令Menuを開く |
| Research | `F5` | Research Schoolと進行状況を確認する |
| End Turn | `E` | Turnを提出する。最後に使う |

Army Setupでは、Double Clickで同種Unitをまとめて選び、`Shift`＋Clickで範囲選択できます。Recruitした兵士は自動でSquadへ入らないため、次TurnにArmy Setup上部の未配属PoolからCommanderへ割り当てます。

!!! warning "RecruitとEnd Turnの誤操作"
    `R`と`E`は近くにあります。慣れるまでは、End Turn前Checkを終えてから`E`を使ってください。

Mouse操作、一Turnの操作順、Recruit、Army Setup、Script複製、Battle Replay操作は[操作方法・ショートカット](shortcuts.md)にまとめています。

---

## 1. 「強いUnit」ではなく役割を見る

Unitを総合点で比較せず、何を担当するかで見ます。

- Line holder：最初の接敵を受ける
- Damage dealer：敵の主防御を破る
- Chaff：攻撃と時間を買う
- Archer：接敵前に削る
- Flanker / Raider：後衛・後方Provinceを狙う
- Commander：Leadershipと命令を維持する
- Mage：ResearchとBattle Magicを担う
- Siege / Logistics：Fort攻略と補給を担う

高価でStatsが高いUnitでも、必要な役割と合わなければArmy全体は強くなりません。

[国家ページの読み方](../nations/how-to-read.md)では、Recruitを役割へ分ける方法を詳しく説明しています。

---

## 2. Mageの継続雇用を止める理由を持つ

多くの国家では、Mage数がResearch速度と中盤以降の戦闘力を決めます。

兵士を一体増やすためにMage雇用を止めると、目の前のArmyは少し強くなっても、数Turn後のResearchとBattle Magicが遅れます。

ただし、次のような状況では兵士やCommanderを優先することがあります。

- Expansion Armyが作れない
- CapitalがRushされる
- Mageが高価でGoldを圧迫する
- Commander Pointを別の必須Commanderへ使う
- Fort建設資金を確保する

大切なのは、Mageを必ず雇うことではなく、**雇わない理由と再開Turnを決めること**です。

---

## 3. Researchは一つのBreakpointへ集める

Schoolを均等に上げても、勝利条件が完成しないことがあります。

研究目標は、次の形式へします。

```text
Spell / Item：
使用Mage：
対象：
必要Gem：
使う予定Turn：
```

「Evocation 5まで」ではなく、「このMageがこのSpellを使い、敵のこの兵を倒す」と書きます。

詳しくは[Researchと研究ルート](../magic/research.md)を参照してください。

---

## 4. Scoutは戦力である

Scoutは戦闘Statsをほとんど増やしませんが、次を防ぎます。

- 危険なIndependentへの突入
- 敵主力との不意の正面衝突
- 空のFortを見逃す
- Raid経路を見失う
- 敵ResearchとMage構成を誤認する

情報不足で失うArmyと比べれば、Scoutの費用は小さいことがあります。

偵察情報は、

```text
確認済み
推定
不明
```

へ分けます。不明なものを都合よく仮定しないようにします。

---

## 5. 勝ったBattle Replayも見る

勝利していても、次が起きている場合があります。

- Commanderが危険な位置へ出た
- Capital-only Unitを多く失った
- Mageが予定Spellを使わなかった
- Gemを不要に消費した
- 一SquadがRoutして消えた
- 敵がResistanceを持っていなかっただけ

勝利は、Script全体が正しかった証明ではありません。

Replayの具体的な読み方は[Battle Replayの読み方](battle-replay.md)を参照してください。

---

## 6. 最初の崩壊点を探す

Armyが全滅した最後の瞬間より、計画が最初に壊れた瞬間を探します。

- 盾兵よりDamage役が先に接敵
- Buff前に敵が到着
- Commander死亡
- Fatigue 100
- Resistanceで主力Spellが無効化
- Fearまたは損失でRout開始

この最初の原因を直す方が、兵数を無計画に増やすより効果的です。

---

## 7. Defenceは一つの数字ではない

Unitの耐久をProtectionだけで判断しません。

```text
攻撃させない
→ 命中させない
→ Shieldで受ける
→ Protection / Resistanceで軽減
→ HP・Regeneration等で耐える
→ MoraleとFatigueで戦闘を続ける
```

という複数層があります。

高Protection兵がPoisonやAN Damageで死ぬのは、Protectionが弱いのではなく、別の防御層を攻撃されているためです。

詳しくは[戦闘ルール](../basics/combat-rules.md)を参照してください。

---

## 8. Commanderを消耗品にしない

Commander死亡は、一体分のCost以上の損害です。

- SquadがLeadershipを失う
- Scriptが消える
- GemとItemを失う
- Retreatが崩れる
- Rare Pathを失う

ためです。

Commanderは後方へ置き、Bodyguard、射撃対策、Attack Rear対策を用意します。全Commanderを同じ場所へ固めると、AoEやFlankで同時に失うRiskがあります。

---

## 9. Attack orderは敵に合わせる

すべてを`Attack Closest`へすると、最も近いScreenへ全戦力を使います。

- Cavalry
- Archers
- Rear
- Large Monster
- Closest

など、敵構成と自軍役割に応じて分けます。

ただしTarget orderは絶対命令ではなく、移動経路、距離、敵の位置によって結果が変わります。Replayで実際の動きを確認します。

詳しくは[命令とBattle Script](../basics/orders.md)を参照してください。

---

## 10. Goldを「使い切る」か「貯める」かでは考えない

Goldには三種類の用途があります。

### 現在戦力

兵士、Commander、Province Defence等。

### 生産力

Fort、Lab、Temple、将来のMage生産。

### 予備

緊急Recruit、Mercenary、修復、予定外の戦争。

毎Turn使い切るとFortが建たず、貯め続けるとExpansion Armyが不足します。

```text
今使うGold
＋ 数Turn後に使うGold
＋ 緊急予備
```

へ分けます。

---

## 11. 第二Fortは壁ではなく毎Turnの生産量

第二Fortを建てる意味は、守りを一つ増やすことだけではありません。

- Mage
- Commander Point
- 国家兵
- Resources
- Lab・Temple
- 増援経路

を増やします。

Fort候補はIncome、Resources、位置、守りやすさ、Mage生産価値で比較します。

詳しくは[Forts](../systems/forts.md)を参照してください。

---

## 12. Gemは勝利条件へ割り当てる

Gemを貯めることも使うことも、それ自体は正解ではありません。

- Site Search
- Battle Spell
- Summon
- Booster
- Resistance Item
- Global

のどれが次の戦争を変えるかで決めます。

Battle MageへGemを持たせるときは、何Spell用で何Battle分かを書きます。大量に持たせるとRout・Assassinationで失うRiskも増えます。

---

## 13. 一種類のDamageへ依存しない

Fireだけ、Shockだけ、MR attackだけ、通常物理だけ、というArmyは、一つのResistanceやCounterで停止します。

最低でも、主Damageと副Damageを分けます。

例：

```text
主：通常兵の高Damage物理
副：MageのShock
```

```text
主：Poison
副：Strength Buffした近接
```

相手が主Damageへ対策した後に、何へ切り替えるかを考えます。

---

## 14. Fort戦はField Battleの続きではない

敵Armyを倒しても、Fortを取るには別の能力が必要です。

- Siege
- Supply
- Gem補給
- Storm Army
- Relief Army迎撃
- 後方Raid対策

最初の戦争では、勝つArmyだけでなく、戦争を終わらせるArmyを作ります。

詳しくは[最初の戦争](first-war.md)を参照してください。

---

## 15. Retreat routeを攻撃前に見る

負けた後に退路を考えても遅すぎます。

- 自領へ隣接しているか
- 敵領へ逃げる可能性
- Fortがあるか
- Choke pointやPlane接続
- 包囲状態

を見ます。

同じ勝率でも、退路のない戦闘は期待損失が大きくなります。

---

## 16. Rare MageとCommon Mageを同じように使わない

Rare Random、Capital-only、Hero、Site Mageなどは、国家のMagic Accessを一段広げる場合があります。

そのMageを通常Evocationの一人として前線へ出し、失うと、Booster、Summon、Resistance、Globalへの経路も失います。

- 量産Battle Mage
- Rare Path holder
- Forger
- Ritual caster
- Researcher

へ役割分担します。

---

## 17. 一戦の結果から国家全体を評価しない

一度の勝敗には、

- Independent構成
- Terrain
- DRN
- Script
- Gem
- Research差
- Scout不足

が混ざっています。

「このUnitは弱い」と結論する前に、同じ役割を別配置・別標的で試します。

---

## 18. 変更は一つずつ試す

敗戦後に全てを変えると、改善理由が分かりません。

```text
変更前：前衛がBuff前に接敵
変更：配置を後ろへ下げる
その他：同じ
```

のように、一つの仮説を試します。

敵も変化するため完全な実験にはなりませんが、学習速度が上がります。

---

## 19. End Turnを恐れすぎない

Dominionsは判断量が多いため、完璧なTurnを作ろうとすると進みません。

次を確認したらTurnを進めます。

- 重要MessageとReplayを見た
- Recruitを設定した
- Research目標がある
- 全Commanderに意図した命令がある
- 大きなGold・Gemの使い忘れがない
- Retreat routeを確認した

細部の最適化より、結果を得て次Turnで修正する方が学べます。

---

## 20. 勝敗より説明可能性を増やす

初回ゲームの目標は、次の文章を書けるようになることです。

```text
この戦闘は、前衛のProtection不足ではなく、Shock Resistance不足で崩れた。
```

```text
研究が遅い原因はMageの性能ではなく、第二Fortが遅れて生産数が少なかったこと。
```

```text
Expansion損失は兵数不足ではなく、Damage役が盾兵より先に接敵したこと。
```

原因を説明できれば、次の国家でも改善できます。

---

## 関連ページ

- [初心者ガイド](index.md)
- [操作方法・ショートカット](shortcuts.md)
- [最初の12ターン](first-12-turns.md)
- [序盤拡張](expansion.md)
- [最初の戦争](first-war.md)
- [Battle Replayの読み方](battle-replay.md)
- [国家ページの読み方](../nations/how-to-read.md)
- [戦闘ルール](../basics/combat-rules.md)
- [Researchと研究ルート](../magic/research.md)

## 主な参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Documentation](https://www.illwinter.com/dom6/docs.html)
