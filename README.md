# Dominions 6 日本語攻略Wiki

Dominions 6 - Rise of the Pantokrator の日本語攻略Wikiです。

## ローカルで確認する

```bash
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
pip install zensical
zensical serve
```

### macOS / Linux

```bash
source .venv/bin/activate
pip install zensical
zensical serve
```

ブラウザで `http://localhost:8000` を開きます。

## 公開

GitHub Pages の Source を **GitHub Actions** に設定してください。
`main` ブランチへ push すると `.github/workflows/docs.yml` が自動でビルド・公開します。

## 記事を書く

記事は `docs/` 配下の Markdown (`.md`) です。

例:

```text
docs/
  basics/weapons-and-shields.md
  magic/paths/earth.md
  nations/ma/ulm.md
```
