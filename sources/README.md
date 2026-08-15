# Generated-data source lock

`sources/dom6inspector.toml` is the authoritative lock file for every upstream
Dom6 Inspector file consumed by the canonical Wiki build.

The lock records:

- upstream repository, commit, tree, and Dominions game version;
- the complete set of CSV/JavaScript inputs used by generators;
- each input's expected Git blob SHA;
- its stable local cache name and the generator groups that consume it.

## Normal build

```bash
python scripts/build_wiki.py
```

The build begins by running `scripts/audit_sources.py`. Missing files are
fetched from the pinned commit, every cache entry is verified against its Git
blob SHA, and `build/source-audit.json` is written. All generators then run with
`--offline`, so no later stage can silently fetch different bytes.

## Offline and refresh modes

```bash
# Require a complete, valid cache and make no network requests.
python scripts/build_wiki.py --offline

# Re-download every locked input, verify it, then build offline.
python scripts/build_wiki.py --refresh
```

The source audit can also be run independently:

```bash
python scripts/audit_sources.py --report build/source-audit.json
python scripts/audit_sources.py --offline --report build/source-audit.json
```

## Updating the pinned snapshot

A source-version change is an explicit lock-file review, not a replacement of a
single commit constant.

1. Change `source.commit`, `source.tree`, and `source.game_version`.
2. Re-enumerate all consumed files and update their `blob` values.
3. Run `python scripts/build_wiki.py --refresh`.
4. Review `build/source-audit.json` and the generated Wiki diff.
5. Re-run the Wiki audit and review hand-written pages whose
   `verified_version` may now be stale.

GitHub Actions compares the current manifest with the base revision and writes
source metadata, added/removed/changed inputs, and every verified SHA-256 to the
job summary. Validation runs also upload `build/*-audit.json` as an artifact.

During migration, several direct generator entry points still expose their old
module-level `COMMIT` constant. `scripts/audit_sources.py` parses those modules
and fails when any value differs from the manifest. The canonical build remains
the source of truth and performs all network access through the manifest audit.
