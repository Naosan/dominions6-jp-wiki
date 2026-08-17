#!/usr/bin/env python3
from __future__ import annotations
import base64, json, sys, zlib
from pathlib import Path


def main() -> int:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
    chunk_dir = Path(__file__).resolve().parent / 'wave3_chunks'
    encoded = ''.join(path.read_text(encoding='ascii').strip() for path in sorted(chunk_dir.glob('*.txt')))
    payload = json.loads(zlib.decompress(base64.b85decode(encoded)).decode('utf-8'))
    changed: list[str] = []

    for rel, pairs in payload['replacements'].items():
        path = repo / rel
        text = path.read_text(encoding='utf-8')
        original = text
        for idx, (old, new) in enumerate(pairs, 1):
            if text.count(new) == 1:
                continue
            old_count = text.count(old)
            new_count = text.count(new)
            if old_count != 1:
                raise RuntimeError(
                    f'{rel} replacement {idx} ambiguous: old={old_count} new={new_count}'
                )
            text = text.replace(old, new, 1)
        if text != original:
            path.write_text(text, encoding='utf-8')
            changed.append(rel)

    for rel, content in payload['files'].items():
        path = repo / rel
        if path.exists() and path.read_text(encoding='utf-8') != content:
            raise RuntimeError(f'existing file differs: {rel}')
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
            changed.append(rel)

    print('changed files:')
    for rel in changed:
        print(' -', rel)
    if not changed:
        print(' - none (already applied)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
