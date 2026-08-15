---
title: 開発方針と完成条件
status: reviewed
page_type: project
last_reviewed: "2026-08-15"
---

# 開発方針と完成条件

このWikiの完成は、単にページ数や抽出データ件数が増えた状態ではありません。

> 利用者が必要な情報へ到達し、仕様と攻略上の判断を区別して理解でき、情報の確度と対象Versionを確認でき、その状態をPatch後にも再構築できること。

この定義に基づき、データ生成、手書き記事、検索導線、検証、継続運用を一つの製品として開発します。

## 1. 三つの情報層

### データ層

Unit、Nation Recruit、Mage access、Spell、Magic Item、Magic Site、Weapon、Armor、Summon、Shape、Eventなど、**何が存在するか**を扱います。

原則として機械生成し、主観的なTier評価やおすすめを混ぜません。未解決参照は推測で埋めず、Data qualityとして残します。

### リファレンス層

Combat、Orders、Turn resolution、Province、Dominion、Fort、Pretender、Research、Fatigue、Morale、Resistanceなど、**ゲームがどう動くか**を扱います。

仕様、条件、例外、具体例、攻略上の意味の順に整理し、公式資料、ゲーム内表示、抽出データ、実機検証の境界を明示します。

### ストラテジー層

国家攻略、Pretender方針、Expansion、Research route、Army構成、Battle Script、Counter、Thug装備、敗戦分析など、**実戦でどう判断するか**を扱います。

能力値の再掲載ではなく、データ層とリファレンス層を組み合わせて意思決定を説明します。

## 2. 優先順位

開発は次の順序で進めます。

1. 再現可能なBuildと品質検査
2. 初心者が最初の戦争まで進める縦導線
3. Combatを中心とする基幹ルール
4. Magic・Pretender・Magic Accessの統合
5. 代表国家の完成版攻略
6. 全国家への展開
7. 比較・逆引き・Patch追従の高度化

新しいデータFieldを抽出できること自体は、追加理由になりません。具体的な利用者の問いへ答える機能を優先します。

## 3. 開発原則

### 一本の利用経路を完成させてから横へ広げる

トップページから初心者ガイド、最初の12ターン、戦闘ルール、Research、国家攻略、Battle Replay分析まで、一連の利用経路を先に完成させます。

### 仕様・解釈・攻略評価を混ぜない

記事では可能な限り、次の順に記述します。

1. 仕様
2. 条件と例外
3. 具体例
4. 攻略上の意味
5. Counter
6. 関連データ
7. 未検証事項

### 記事の長さではなく検索意図で分割する

総合記事は全体像を担当し、個別記事は計算、例外、検証Caseなど独立更新が必要な内容を担当します。細分化そのものを目的にしません。

### 存在と発見可能性を別々に検査する

ページを追加しただけでは完成としません。Navigation、上位索引、関連記事から到達できることを確認します。孤立ページはAudit reportへ記録します。

### CoverageとConfidenceを分離する

「項目を扱っている」こと「現行Versionで確認済み」であることを同一視しません。記事状態と検証情報をFront Matterへ記録します。

### 不明点を品質情報として残す

Negative Monster Number、Montag、Event owner、Temporary Unit、未知のLocation bitなどを、安全な根拠なしに単一結果へ結び付けません。未解決状態を可視化できる方が、見かけ上の完全性より信頼できます。

### Patch更新を通常運用にする

Patch対応は例外的な大作業ではなく、Source version更新、再生成、差分確認、影響記事の再検証という定常作業として設計します。

## 4. 記事状態

Front Matterの`status`には次を使用します。

| Status | 意味 |
|---|---|
| `stub` | 自動生成または見出し中心の入口。攻略本文は未執筆 |
| `draft` | 読める本文はあるが、構成または検証が未完 |
| `reviewed` | 読者向け記事として構成と主要記述をレビュー済み |
| `verified` | 高重要度の数値・挙動を記載Versionで検証済み |
| `needs-update` | Patchや新しい根拠により再確認が必要 |

数値やゲーム挙動へ依存する記事では、必要に応じて次も記録します。

```yaml
---
title: 戦闘ルール
page_type: reference
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-15"
known_gaps:
  - exact-shield-edge-cases
---
```

`reviewed`は自動的に`verified`を意味しません。また、文章を編集した日を根拠なく`last_verified`へ記録しません。

## 5. Phase 0 — 完成できる開発基盤

最初のMilestoneでは次を整えます。

- PythonとBuild toolのVersion固定
- LocalとCIで共有するBuild pipeline
- Front Matter、内部Link、Navigation、孤立PageのAudit
- Build結果とCoverageの可視化
- README、Workflow、実際の生成処理の同期
- Contributor向け手順とReview checklist
- Data source versionと更新手順の集約

### 完了条件

- 同じCommitから同じ手順でBuildできる
- Navigation targetと内部Linkに未解決Errorがない
- 手書き記事のStatusと検証情報を集計できる
- 生成処理の追加・削除を一か所で管理できる
- Local確認手順とGitHub Actionsが同じPipelineを使う

## 6. Phase 1 — 初心者の縦導線

次を一連の学習経路として完成させます。

- 国家選択
- Pretender入門
- 最初の12ターン
- Expansion
- Research開始
- Fort・Lab・Temple
- 最初の戦争
- Battle Replayの読み方
- よくある敗因

完了条件は、初心者がWikiを読みながら国家選択から最初の戦争と敗戦分析まで進められることです。

## 7. Phase 2 — 基幹ルール

Combat、Orders、Turn resolution、Damage、Protection、Shield、Repel、Fatigue、Morale、Resistance、MR、Mounted、Province、Dominion、Fort、Throne、Discipleを優先します。

既存の総合記事を全面的に置き換えず、検証Matrixを作り、一節ずつ精度を上げます。

## 8. Phase 3 — Magic統合

国家、Recruitable Mage、Random Path、Booster、Summon、Communion、Site Search、Research、Spellを跨いで、次の問いへ答えられる導線を作ります。

> この国家は、どの経路で必要Pathへ到達し、どのResearchと資源で目的のSpellを使えるか。

戦略Map上の到達値とBattle限定のCommunion到達値は分離します。

## 9. Phase 4 — 国家攻略

最初に一つの国家記事を完成Templateとして仕上げ、異なる国家設計を代表する記事へ広げます。

国家記事の標準項目は次です。

- 一言でいうと、勝ち筋、強み、弱み
- Expansion、経済、Fort計画
- 重要Unit、Commander、Mage
- Research、Magic Access、Pretender、Bless
- Army構成、Battle Script、重要Spell、重要Item
- 中盤、終盤、Counter、よくある失敗
- 関連する自動生成データとPatch履歴

基礎能力値は生成データへ委ね、手書き記事では判断を扱います。

## 10. Release条件

### v1.0

- 再現可能なBuildとAuditが運用されている
- 初心者の縦導線が完成している
- Combatを含む主要リファレンスがレビュー済み
- 全Magic Pathの入口がある
- 代表国家の完成版攻略がある
- 全国家にデータと最低限の入口がある
- Patch更新手順が確立している

### v2.0

- 全国家に最低限の攻略記事がある
- 主要国家にResearch、Script、Counterがある
- 国家比較と代表Matchupを確認できる
- Patch後の再検証対象を追跡できる

## 11. 当面行わないこと

- 利用目的が不明な索引を増やし続ける
- 全国家を同時並行で執筆する
- Dom4・Dom5の文章を現行仕様として移す
- 未確認の数式や内部処理を断定する
- 自動生成ページ数を完成度と見なす
- 未解決参照を推測で消す
- データページへ主観的なTier評価を混ぜる

## 関連

- [Wiki編集方針](editing-policy.md)
- [情報源と確認方針](sources.md)
- [国家記事Template](../templates/nation-template.md)
