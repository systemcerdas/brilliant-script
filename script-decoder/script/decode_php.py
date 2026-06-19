#!/usr/bin/env python3
"""Decode PHP files obfuscated with php-encryptor (hex + remote decrypt + eval)."""

import argparse
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

DECODER_ROOT = Path(__file__).parent.parent
BAHAN_DIR = DECODER_ROOT / "bahan"
OUTPUT_DIR = DECODER_ROOT / "output"
API_URL = "https://php-encryptor.vercel.app/api/run"


def decode_php_hex_string(s: str) -> str:
    return re.sub(r"\\x([0-9a-fA-F]{2})", lambda m: chr(int(m.group(1), 16)), s)


def extract_quoted_assignments(content: str, var_name: str) -> list[str]:
    pattern = rf'\${var_name}\s*=\s*"((?:\\x[0-9a-fA-F]{{2}}|[^"\\]|\\.)*?)"\s*;'
    return [decode_php_hex_string(m.group(1)) for m in re.finditer(pattern, content)]


def reconstruct_payload(content: str) -> dict:
    rqhpcko_vals = extract_quoted_assignments(content, "_rqhpcko")
    qrlbsfy_vals = extract_quoted_assignments(content, "_qrlbsfy")

    if len(rqhpcko_vals) < 4 or len(qrlbsfy_vals) < 4:
        raise RuntimeError(
            f"Expected >=4 assignments each, got rqhpcko={len(rqhpcko_vals)}, qrlbsfy={len(qrlbsfy_vals)}"
        )

    return {
        "scriptId": rqhpcko_vals[2] + qrlbsfy_vals[2],
        "data": rqhpcko_vals[0] + qrlbsfy_vals[0],
        "iv": rqhpcko_vals[3] + qrlbsfy_vals[3],
        "mac": rqhpcko_vals[1] + qrlbsfy_vals[1],
    }


def call_decrypt_api(payload: dict) -> str:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if not result.get("code"):
        raise RuntimeError(f"API error: {result}")
    return result["code"]


def beautify_php_strings(content: str) -> str:
    def decode_match(m):
        raw = m.group(0)
        decoded = decode_php_hex_string(raw[1:-1])
        if all(32 <= ord(c) < 127 or c in "\n\r\t" for c in decoded):
            escaped = decoded.replace("\\", "\\\\").replace('"', '\\"')
            return f'"{escaped}"'
        return raw

    return re.sub(r'"(?:\\x[0-9a-fA-F]{2}|[^"\\]|\\.)*"', decode_match, content)


def format_php_clean(source: str, source_label: str) -> str:
    lines = source.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if lines and lines[0].strip().startswith("<?php"):
        body_lines = lines
    else:
        body_lines = [
            "<?php",
            "/**",
            f" * Decoded PHP — source: {source_label}",
            " */",
            "",
            *lines,
        ]

    out: list[str] = []
    indent = 0
    for raw in body_lines:
        line = raw.strip()
        if not line:
            out.append("")
            continue
        if line.startswith(("}", ")", "];")):
            indent = max(indent - 1, 0)
        out.append("\t" * indent + line)
        if line.endswith("{"):
            indent += 1
        if line == "}":
            indent = max(indent - 1, 0)

    return "\n".join(out).rstrip() + "\n"


def output_dir_for(input_path: Path) -> Path:
    try:
        rel = input_path.resolve().relative_to(BAHAN_DIR.resolve())
    except ValueError:
        rel = Path(input_path.stem)

    if len(rel.parts) > 1:
        return OUTPUT_DIR / Path(*rel.parts[:-1])
    return OUTPUT_DIR / rel.stem


def build_report(input_path: Path, payload: dict, obfuscated_len: int, decrypted_len: int) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    label = input_path.as_posix()
    return f"""# Decode Report — {input_path.name}

> Source: `{label}`  
> Tanggal: {now}  
> Tool: `script/decode_php.py`

## Ringkasan

| Item | Nilai |
|------|-------|
| File input | `{input_path.name}` |
| Ukuran terenkripsi | {obfuscated_len:,} byte |
| Ukuran setelah decode | {decrypted_len:,} karakter |
| API | `{API_URL}` |

## Payload

| Field | Nilai |
|-------|-------|
| `scriptId` | `{payload["scriptId"]}` |
| `iv` | `{payload["iv"]}` |
| `mac` | `{payload["mac"]}` |
| `data` | {len(payload["data"]):,} karakter |

## Lapisan obfuscation

1. **Hex escape** — string `\\xNN`
2. **Noise code** — variabel/fungsi acak (`_vcgehlul` = concat, `_dnmxhumc` = API call)
3. **Enkripsi + eval** — POST ke php-encryptor, `eval()` hasil response

## Output

```
output/
└── ...
    ├── decoded.php          # mentah dari API
    ├── hex_readable.php     # hex string terbaca
    ├── payload.json
    └── clean/
        └── decoded.php      # versi rapih
```
"""


def decode_file(input_path: Path) -> Path:
    if not input_path.is_file():
        raise FileNotFoundError(input_path)

    result_dir = output_dir_for(input_path)
    clean_dir = result_dir / "clean"
    result_dir.mkdir(parents=True, exist_ok=True)
    clean_dir.mkdir(parents=True, exist_ok=True)

    content = input_path.read_text(encoding="utf-8", errors="replace")
    source_label = str(input_path.relative_to(DECODER_ROOT))

    hex_readable = beautify_php_strings(content)
    (result_dir / "hex_readable.php").write_text(hex_readable, encoding="utf-8")

    comment_match = re.search(r"/\*\s*((?:\\x[0-9a-fA-F]{2})+)\s*\*/", content)
    if comment_match:
        (result_dir / "comment.txt").write_text(
            decode_php_hex_string(comment_match.group(1)), encoding="utf-8"
        )

    payload = reconstruct_payload(content)
    (result_dir / "payload.json").write_text(
        json.dumps({k: (v[:80] + "..." if len(v) > 80 else v) for k, v in payload.items()}, indent=2),
        encoding="utf-8",
    )
    (result_dir / "payload_full.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    decrypted = call_decrypt_api(payload)
    (result_dir / "decoded.php").write_text(decrypted, encoding="utf-8")

    clean = format_php_clean(decrypted, source_label)
    (clean_dir / "decoded.php").write_text(clean, encoding="utf-8")
    (clean_dir / "hex_readable.php").write_text(hex_readable, encoding="utf-8")

    report = build_report(input_path, payload, len(content), len(decrypted))
    (result_dir / "REPORT.md").write_text(report, encoding="utf-8")

    return clean_dir / "decoded.php"


def collect_inputs(args: argparse.Namespace) -> list[Path]:
    if args.inputs:
        return [Path(p).resolve() for p in args.inputs]

    if not BAHAN_DIR.exists():
        return []

    files = sorted(BAHAN_DIR.rglob("*.php"))
    return [f.resolve() for f in files]


def main():
    parser = argparse.ArgumentParser(description="Decode PHP obfuscated with php-encryptor")
    parser.add_argument(
        "inputs",
        nargs="*",
        help="File PHP input (default: semua bahan/**/*.php)",
    )
    args = parser.parse_args()

    inputs = collect_inputs(args)
    if not inputs:
        print("Tidak ada file input. Letakkan file .php di bahan/ atau beri path argumen.")
        sys.exit(1)

    for path in inputs:
        print(f"Decode: {path}")
        try:
            out = decode_file(path)
            print(f"  -> {out}")
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            sys.exit(1)

    print("Selesai.")


if __name__ == "__main__":
    main()
