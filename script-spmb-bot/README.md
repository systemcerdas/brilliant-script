# SPMB Bogor Kab — Bot Registrasi & Login

Bot otomatis registrasi & login [SPMB Kabupaten Bogor](https://spmb.bogorkab.go.id). Tersedia dua implementasi:

| Versi | Folder | Runtime |
|-------|--------|---------|
| JavaScript | [javascript/](javascript/) | Node.js + Playwright |
| Python | [python/](python/) | Python + Playwright |

Bagian dari [BrillianScript](../README.md)

## Struktur

```
script-spmb-bot/
├── javascript/          # Versi Node.js
│   ├── spmb_register.mjs
│   ├── run.ps1
│   └── package.json
├── python/              # Versi Python (+ VPS watcher)
│   ├── spmb_bot.py
│   ├── spmb_watcher.py
│   └── app.py
└── .gitignore
```

## Quick start

### JavaScript

```powershell
cd script-spmb-bot/javascript
copy .data.example .data
.\run.ps1 --check-login
```

### Python

```powershell
cd script-spmb-bot/python
copy .data.example .data
.\setup_python.ps1
python spmb_bot.py --check-login
```

## File sensitif (gitignored)

| File | Keterangan |
|------|------------|
| `.data` | NIK, nama, password |
| `.curl` | Capture DevTools (JS) |
| `.cred` | Kredensial VPS (Python) |
| `spmb_output/` | Log & screenshot |

## Dokumentasi

- [javascript/README.md](javascript/README.md)
- [python/README.md](python/README.md)
