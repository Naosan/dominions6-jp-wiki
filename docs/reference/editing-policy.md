---
title: Wiki編集方針
page_type: project
status: reviewed
last_reviewed: "2026-08-15"
---

# Wiki編集方針

## 1. 仕様と攻略評価を分ける

記事では、可能な限り次を区別します。

### 仕様

ゲーム内で確認できる数値・効果・ルール。

### 攻略上の意味

その仕様が実戦でどう強いか、何に弱いか。

仕様、条件と例外、具体例、攻略上の意味、Counter、関連データ、未検証事項の順に整理すると、事実と判断を混同しにくくなります。

## 2. 記事状態を残す

手書き記事ではFront Matterへ`status`を記録します。

| Status | 意味 |
|---|---|
| `stub` | 自動生成または入口だけのPage |
| `draft` | 本文はあるが構成・検証が未完 |
| `reviewed` | 読者向け記事としてReview済み |
| `verified` | 高重要度の数値・挙動を記載Versionで検証済み |
| `needs-update` | Patch等により再確認が必要 |

## 3. Versionを残す

数値や研究Levelに依存する記事では、確認したVersionと日付を記録します。

```yaml
---
title: 記事名
page_type: reference
status: draft
verified_version: "6.xx"
last_verified: "YYYY-MM-DD"
---
```

文章を編集した日を、実機確認なしに`last_verified`へ記録しません。`reviewed`と`verified`も区別します。

## 4. 一次情報を優先する

優先順位の目安:

1. ゲーム内表示と実際の挙動
2. Illwinter公式Manual・Patch notes
3. ゲームData抽出Tool
4. Community Wiki
5. 実戦検証・Player知見

情報源の種類が異なる場合は、どの部分を何で確認したか分かるように記述します。

## 5. 古いDom5情報をそのまま移さない

Dominions 6ではMagic Path、Spell、Research Level、Mounted、Battlefieldなど多くの変更があります。旧作記事は論点の発見には使えますが、現行仕様の根拠にはしません。

## 6. 自動生成Dataと手書き攻略を分ける

Unit、Spell、Item、SiteなどのRecordと関係はGeneratorが扱います。戦術、Research順、Pretender、Script、Counterは手書き記事で扱います。

生成Pageを直接修正すると再生成時に失われます。Data側の誤りはGenerator、入力Data、または安全なPatch処理で直してください。

## 7. 不明点を推測で消さない

負のMonster Number、Montag、Eventの相対Nation、Temporary Unit、未知のLocation bitなどを、確実な対応根拠なしに単一Recordへ接続しません。未解決参照はData qualityへ残します。

## 8. Pageを孤立させない

新しいPageは、Navigation、上位Index、関連記事のいずれかから到達できるようにします。内部Linkと孤立Pageは`python scripts/audit_wiki.py`で確認できます。

## 関連

- [開発方針と完成条件](development-policy.md)
- [情報源と確認方針](sources.md)
- [国家記事Template](../templates/nation-template.md)
