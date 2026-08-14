---
title: Wiki編集方針
---

# Wiki編集方針

## 1. 仕様と攻略評価を分ける

記事では、可能な限り次を区別します。

### 仕様

ゲーム内で確認できる数値・効果・ルール。

### 攻略上の意味

その仕様が実戦でどう強いか、何に弱いか。

## 2. バージョンを残す

数値や研究レベルに依存する記事ではFront Matterに記録します。

```yaml
---
status: draft
verified_version: "6.xx"
last_verified: "YYYY-MM-DD"
---
```

## 3. 一次情報を優先

優先順位の目安:

1. ゲーム内表示
2. Illwinter公式Manual・Patch notes
3. ゲームデータ抽出ツール
4. Community Wiki
5. 実戦検証・プレイヤー知見

## 4. 古いDom5情報をそのまま移さない

Dominions 6ではMagic Path、Spell、研究レベル、騎乗、戦場地形など多くの変更があります。
