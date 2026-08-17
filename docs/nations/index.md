---
title: "国家攻略"
status: catalog
verified_version: "6.35"
last_verified: "2026-08-17"
---

# 国家攻略

Dominions 6のvanilla国家を、**Early Age 35・Middle Age 37・Late Age 31、合計103国家**に分けて整理します。

| 時代 | 国家数 | 一覧 |
|---|---:|---|
| Early Age | 35 | [EA国家一覧](ea/index.md) |
| Middle Age | 37 | [MA国家一覧](ma/index.md) |
| Late Age | 31 | [LA国家一覧](la/index.md) |

## 最初に読むページ

- [国家選択ガイド](choose-a-nation.md) — 自分の好みと国家の制約を照合する
- [国家ページの読み方](how-to-read.md) — 兵・Mage・Random Path・Capital-onlyの評価方法
- [Pretender設計サンプル](../pretender/samples.md) — 国家の不足から設計骨格を二案選ぶ
- [国家攻略テンプレート](../templates/nation-template.md) — 新規記事の共通構造

## 手書き攻略の基準記事

最初の第1陣として、各Ageに一つずつ異なる学習テーマを持つ基準記事を用意しています。

| Age | 国家 | 主に学べること |
|---|---|---|
| EA | [EA Ulm — Enigma of Steel](ea/ulm.md) | 高性能一般兵、複数攻撃、Stealth、地形Recruit、鍛造、広いRandom Magic |
| MA | [MA Ulm — Forges of Ulm](ma/ulm.md) | Blacksteel重装、Resource経済、Earth Mage、Forge economy、対Armor戦 |
| LA | [LA Man — Towers of Chelms](la/man.md) | Longbow・Crossbow、Drain研究、Random Mage、Mason、Fort network、Friendly Fire |

三記事は「最強国家の推薦」ではありません。

```text
EA Ulm：兵質とMap Control
MA Ulm：生産と重装Army
LA Man：Combined Armsと研究・Fort管理
```

という異なる国家エンジンを、同じ記事構造で比較するための基準です。

## 国家攻略で重視するもの

国家は「最強兵がいるか」だけでは評価できません。少なくとも次を組み合わせて見ます。

1. **Expansion** — 独立州を損失少なく取れるか
2. **Recruitment** — どのFortでも雇える兵・Mageは何か
3. **Capital依存** — Cap-only SacredやMageへどれだけ依存するか
4. **Magic Access** — 固定Path、Random Path、Booster後の到達点
5. **Research Timing** — 最初の戦争で使えるBreakpoint
6. **Economy** — Gold、Resources、Recruitment Points、Commander Points
7. **Map Control** — Stealth、Flying、Sailing、Magic Phase移動、Raid
8. **Counter耐性** — AP/AN、MR攻撃、毒、Fatigue、Holyなどへの弱点
9. **Late-game Ceiling** — Summon Mage、Global、Blood、Communion、Legendary Spell
10. **操作量** — Blood Hunt、Communion、Stealth ArmyなどのMicro負荷

## 国家記事の読み方

国家記事では、次を分離します。

```text
事実
→ Roster、Path、Cost、国家能力

攻略上の意味
→ 何を主力にし、どこで交換するか

設計例
→ Pretender、Research、Army、Script

失敗条件
→ Counter、Timing、供給、操作量
```

数値は自動生成データとゲーム内表示を正本とし、手書き記事は判断と運用を扱います。

## 記事状態

| 状態 | 意味 |
|---|---|
| `stub` | 公式メタデータと見出しのみ |
| `draft` | 主要な兵・Mage・研究方針を執筆中 |
| `reviewed` | 実戦記事があり、記載Versionのデータ・主要挙動を確認済み |
| `verified` | 記載Versionで追加の実験・再現確認まで終えた記事 |
| `catalog` | 一覧・索引ページ |

!!! warning "Tier表について"
    国家の強さはMap、人数、Research設定、外交、勝利条件、Patchで大きく変わります。このWikiでは単一Tierより、**勝ち筋・必要条件・Counter**を記述します。

## 次に増やす国家類型

第1陣の次は、国家記事を書く過程で共通システムの不足も検出できるよう、次の類型を優先します。

- Giant国家
- Sacred・Heavy Bless国家
- Communion国家
- Undead・Popkill国家
- Blood国家
- Underwater国家

## データ更新

国家名、Epithet、Nation IDはDominions 6 Mod Inspectorのvanilla nation dataと照合しています。個別の兵種・Mage・Spell・数値は、ゲーム内表示と現行Patchを優先します。
