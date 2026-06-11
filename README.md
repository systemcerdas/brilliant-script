# BrillianScript

Kumpulan skrip utilitas BrillianLabs.

| Folder | Deskripsi |
|--------|-----------|
| [script-laporan-bulanan](script-laporan-bulanan/) | Generator laporan bulanan Tenaga Teknis (Python + Word) |
| [script-spmb-bot](script-spmb-bot/) | Otomasi registrasi SPMB Kab. Bogor (Playwright) |

## Quick start

**Laporan bulanan**
```powershell
cd script-laporan-bulanan
pip install -r generator/requirements.txt
python generator/generate.py 202605
```

**SPMB bot**
```powershell
cd script-spmb-bot
copy .data.example .data
npm install
npx playwright install chromium
npm run spmb
```
