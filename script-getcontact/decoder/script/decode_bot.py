#!/usr/bin/env python3
"""Decode/reverse obfuscated bot.php from rusmanaid/getcontact."""

import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

DECODER_ROOT = Path(__file__).parent.parent
SCRIPT_ROOT = DECODER_ROOT.parent
BOT_PHP = DECODER_ROOT / "bahan" / "bot.php"
RESULT_DIR = DECODER_ROOT / "output"
CLEAN_DIR = RESULT_DIR / "clean"
DOCS_DIR = SCRIPT_ROOT / "docs"
GETCONTACT_SCRIPT = SCRIPT_ROOT / "getcontact" / "script" / "bot.php"


def decode_php_hex_string(s: str) -> str:
    def repl(m):
        return chr(int(m.group(1), 16))

    return re.sub(r"\\x([0-9a-fA-F]{2})", repl, s)


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
    url = "https://php-encryptor.vercel.app/api/run"
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
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


def format_php_clean(source: str) -> str:
    """Basic PHP cleanup: header, indent, trailing whitespace."""
    lines = source.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if lines and lines[0].strip().startswith("<?php"):
        body_lines = lines
    else:
        body_lines = [
            "<?php",
            "/**",
            " * GetContact CLI Bot — hasil reverse dari bot.php (rusmanaid/getcontact)",
            " * Author asli: Rusmana-ID / Inject-ID",
            " */",
            "",
            *lines,
        ]

    out: list[str] = []
    indent = 0
    for raw in body_lines:
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            out.append("")
            continue

        if stripped.startswith("?>"):
            indent = max(indent - 1, 0)

        if stripped.startswith(("}", ")", "];", "elseif", "else")):
            if stripped.startswith("}"):
                indent = max(indent - 1, 0)

        out.append(("\t" * indent) + stripped)

        open_count = stripped.count("{") + stripped.count("(")
        close_count = stripped.count("}") + stripped.count(")")
        if stripped.endswith(("{", "(")) or stripped.endswith(("else", "elseif")):
            indent += 1
        elif open_count > close_count and stripped.endswith("{"):
            indent += 1
        elif stripped.endswith("}") and not stripped.startswith("}"):
            pass

        if stripped.endswith("{"):
            indent += 0  # already handled above loosely

    # second pass: simple brace indent
    out = []
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

    text = "\n".join(out).rstrip() + "\n"
    if not text.endswith("\n?>"):
        text = text.rstrip() + "\n"
    return text


def build_analysis_md(payload: dict, decrypted_len: int, obfuscated_len: int) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"""# Analisis bot.php — GetContact Cek

> Repo: [rusmanaid/getcontact](https://github.com/rusmanaid/getcontact)  
> Tanggal analisis: {now}  
> Tool: `decode_bot.py` (Python 3)

---

## 1. Ringkasan

`bot.php` adalah **bot CLI PHP** untuk mengecek **tag/nama yang disimpan pengguna GetContact** pada nomor WhatsApp tertentu. Kode asli disembunyikan dengan obfuscation berlapis dan enkripsi yang didekripsi lewat API pihak ketiga sebelum dijalankan dengan `eval()`.

| Item | Nilai |
|------|-------|
| Ukuran file asli | {obfuscated_len:,} byte |
| Ukuran kode setelah dekripsi | {decrypted_len:,} karakter |
| Bahasa | PHP (CLI) |
| Author (dalam kode) | Rusmana-ID / Inject-ID |

---

## 2. Lapisan obfuscation

### Lapisan 1 — Hex escape string

Semua string penting ditulis sebagai `\\x4f\\x70...` agar tidak terbaca langsung.

**Contoh:** `\\x68\\x74\\x74\\x70` → `http`

### Lapisan 2 — Noise code

Variabel dan fungsi dengan nama acak (`_vcgehlul`, `_dnmxhumc`, `_jgdrplxm`, dll.) yang tidak mempengaruhi logika utama — hanya mengacau pembaca.

| Fungsi | Peran sebenarnya |
|--------|------------------|
| `_vcgehlul($a, $b)` | Menggabungkan dua string (`$a . $b`) |
| `_jgdrplxm($x)` | Mengecek field `code` tidak kosong |
| `_dnmxhumc($payload)` | POST JSON ke API dekripsi, return `code` |

### Lapisan 3 — Enkripsi + remote decrypt + eval

```
bot.php
  └─ susun payload (scriptId, data, iv, mac)
  └─ POST → https://php-encryptor.vercel.app/api/run
  └─ eval(kode_php_dari_response)
```

**Parameter enkripsi yang diekstrak:**

| Field | Nilai |
|-------|-------|
| `scriptId` | `{payload["scriptId"]}` |
| `iv` | `{payload["iv"]}` |
| `mac` | `{payload["mac"]}` |
| `data` | {len(payload["data"]):,} karakter (base64 terenkripsi) |

Komentar base64 di baris 35: `M2E4M2MyYWY0ODc1ZTZkYTAwZDJjZDdiYmFhYzBiNDc=` → decode hex dari scriptId.

---

## 3. Alur program (setelah dekripsi)

```mermaid
flowchart TD
    A[php bot.php] --> B[Menu utama]
    B --> C{{Pilihan user}}
    C -->|01| D[Telegram config_geratis]
    C -->|02| E[YouTube Inject-ID]
    C -->|03| F[tutorialinjectid.my.id]
    C -->|04| G[Mulai bot]
    C -->|05| H[WhatsApp admin]
    C -->|06| I[Telegram script]
    C -->|00| J[Exit]
    G --> K[Input key]
    K -->|getcontact| L[Input nomor WA]
    K -->|lain| M[Key salah - exit]
    L --> N[GET getcontact.com/id/manage]
    N --> O[Ambil accessToken, token, hash]
    O --> P[VerifyKit /v3.0/start]
    P --> Q[Buka link WA verifikasi]
    Q --> R[VerifyKit /v3.0/check]
    R --> S[POST validation-verifykit-check]
    S --> T[GET /id/manage/profile]
    T --> U[Tampilkan daftar tag pt-text]
```

---

## 4. Endpoint & layanan eksternal

| URL | Metode | Fungsi |
|-----|--------|--------|
| `https://php-encryptor.vercel.app/api/run` | POST | Dekripsi kode PHP tersembunyi |
| `https://getcontact.com/id/manage` | GET | Ambil cookie/token sesi |
| `https://widget.verifykit.com/v3.0/start` | POST | Mulai verifikasi WhatsApp |
| `https://widget.verifykit.com/v3.0/check` | POST | Cek status verifikasi |
| `https://getcontact.com/validation-verifykit-check` | POST | Validasi session ke GetContact |
| `https://getcontact.com/id/manage/profile` | GET | Scrape daftar tag yang menyimpan nomor |

**Link promosi dalam menu:**

- Telegram: `https://t.me/config_geratis`
- YouTube: `https://youtube.com/@Inject1D`
- Web: `https://tutorialinjectid.my.id`
- Admin WA: `https://wa.me/6283879017166`
- Key (palsu/marketing): `bit.ly/getcontact-key`

---

## 5. Autentikasi & validasi

### Key akses

- Key hardcoded: **`getcontact`**
- Jika salah, user diarahkan ke `bit.ly/getcontact-key` (link marketing)

### Validasi nomor

- Nomor harus mengandung angka **`0`** (format lokal Indonesia)
- VerifyKit memvalidasi nomor via WhatsApp (kirim pesan verifikasi)

### Data yang diambil dari HTML

```php
$aks  = accessToken   // dari cookie response
$tkn  = token         // dari URL/widget
$hash = hash          // dari JSON di halaman
```

Hasil akhir: parse elemen `<div class="pt-text">...</div>` untuk setiap tag/nama.

---

## 6. Risiko keamanan

| Risiko | Keterangan |
|--------|------------|
| **Remote code execution** | `eval()` pada kode dari server eksternal — server bisa mengubah perilaku kapan saja |
| **SSL verify disabled** | `CURLOPT_SSL_VERIFYPEER = 0` — rentan MITM |
| **Scraping tanpa izin** | Melanggar ToS GetContact |
| **Data pribadi** | Menampilkan tag yang diberikan orang lain pada nomor |

---

## 7. Struktur folder hasil

```
decoder/
├── bahan/
│   └── bot.php                  ← file terenkripsi (input)
├── script/
│   └── decode_bot.py            ← tool decoder
└── output/
    ├── ANALISIS.md              ← dokumen ini
    ├── bot_decoded.php          ← kode mentah hasil dekripsi API
    ├── bot_deobfuscated_strings.php
    ├── decrypt_payload.json
    ├── decrypt_payload_full.json
    ├── comment_decoded.txt
    └── clean/
        ├── bot.php              ← kode dekripsi, dirapikan
        └── bot_obfuscated.php

getcontact/
└── script/
    └── bot.php                  ← salinan clean, siap dijalankan
```

---

## 8. Cara decode ulang

```bash
python decoder/script/decode_bot.py
```

---

## 9. Kesimpulan

Script ini **bukan API resmi GetContact**. Ia mengotomasi alur web manage profile GetContact dengan verifikasi WhatsApp (VerifyKit), lalu men-scrape HTML untuk menampilkan tag. Kode sengaja dienkripsi dan di-`eval` agar sulit diaudit; dependensi ke `php-encryptor.vercel.app` menambah risiko karena eksekusi kode dikontrol server pihak ketiga.
"""


def main():
    RESULT_DIR.mkdir(exist_ok=True)
    CLEAN_DIR.mkdir(exist_ok=True)

    content = BOT_PHP.read_text(encoding="utf-8", errors="replace")
    obfuscated_len = len(content)

    # --- original outputs (tetap seperti sebelumnya) ---
    hex_readable = beautify_php_strings(content)
    (RESULT_DIR / "bot_deobfuscated_strings.php").write_text(hex_readable, encoding="utf-8")

    comment_match = re.search(r"/\*\s*((?:\\x[0-9a-fA-F]{2})+)\s*\*/", content)
    if comment_match:
        (RESULT_DIR / "comment_decoded.txt").write_text(
            decode_php_hex_string(comment_match.group(1)), encoding="utf-8"
        )

    payload = reconstruct_payload(content)
    (RESULT_DIR / "decrypt_payload.json").write_text(
        json.dumps({k: (v[:80] + "..." if len(v) > 80 else v) for k, v in payload.items()}, indent=2),
        encoding="utf-8",
    )
    (RESULT_DIR / "decrypt_payload_full.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )

    decrypted = call_decrypt_api(payload)
    (RESULT_DIR / "bot_decoded.php").write_text(decrypted, encoding="utf-8")

    # --- clean outputs ---
    (CLEAN_DIR / "bot_obfuscated.php").write_text(hex_readable, encoding="utf-8")
    clean_bot = format_php_clean(decrypted)
    (CLEAN_DIR / "bot.php").write_text(clean_bot, encoding="utf-8")

    GETCONTACT_SCRIPT.parent.mkdir(parents=True, exist_ok=True)
    GETCONTACT_SCRIPT.write_text(clean_bot, encoding="utf-8")

    analysis = build_analysis_md(payload, len(decrypted), obfuscated_len)
    (RESULT_DIR / "ANALISIS.md").write_text(analysis, encoding="utf-8")
    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "ANALISIS.md").write_text(analysis, encoding="utf-8")

    print("Selesai.")
    print(f"  Bahan    : {BOT_PHP}")
    print(f"  Output   : {RESULT_DIR}/")
    print(f"  Rapih    : {CLEAN_DIR}/")
    print(f"  Analisis : {RESULT_DIR / 'ANALISIS.md'}")
    print(f"  Bot      : {GETCONTACT_SCRIPT}")


if __name__ == "__main__":
    main()
