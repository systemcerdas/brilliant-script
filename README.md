# BrillianScript

Kumpulan skrip utilitas BrillianLabs.

Repo: [github.com/BrillianLabs/BrillianScript](https://github.com/BrillianLabs/BrillianScript)

| Folder | Deskripsi |
|--------|-----------|
| [script-laporan-bulanan](script-laporan-bulanan/) | Generator laporan bulanan Tenaga Teknis (Python + Word) |
| [script-spmb-bot](script-spmb-bot/) | Bot registrasi & login SPMB Kab. Bogor (Playwright) |
| [script-decoder](script-decoder/) | Decoder PHP terenkripsi (php-encryptor) |
| [script-getcontact](script-getcontact/) | Bot cek tag GetContact |

## Quick start

### Laporan bulanan

```powershell
cd script-laporan-bulanan
pip install -r generator/requirements.txt
python generator/generate.py 202605
```

### SPMB bot

```powershell
cd script-spmb-bot
copy .data.example .data
# edit .data

.\run.ps1 --check-login
.\run.ps1
```

Dokumentasi: [script-spmb-bot/README.md](script-spmb-bot/README.md)

### PHP decoder

```powershell
cd script-decoder
python script/decode_php.py
```

Dokumentasi: [script-decoder/README.md](script-decoder/README.md)

### GetContact bot

```powershell
cd script-getcontact
php script/bot.php
```

Dokumentasi: [script-getcontact/README.md](script-getcontact/README.md)
