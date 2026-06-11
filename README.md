# BrillianScript

Kumpulan skrip utilitas BrillianLabs.

Repo: [github.com/BrillianLabs/BrillianScript](https://github.com/BrillianLabs/BrillianScript)

| Folder | Deskripsi |
|--------|-----------|
| [script-laporan-bulanan](script-laporan-bulanan/) | Generator laporan bulanan Tenaga Teknis (Python + Word) |
| [script-spmb-bot](script-spmb-bot/) | Bot registrasi & login SPMB Kab. Bogor (Playwright) |

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

.\run.ps1 --check-login   # cek login (disarankan dulu)
.\run.ps1                 # registrasi SD
```

Dokumentasi lengkap: [script-spmb-bot/README.md](script-spmb-bot/README.md)
