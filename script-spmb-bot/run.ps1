# Jalankan SPMB bot dari folder lokal (hindari node_modules rusak di Google Drive)
param(
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$Args
)

$ErrorActionPreference = 'Stop'
$src = $PSScriptRoot
$work = Join-Path $env:TEMP 'brillian-spmb-bot'

New-Item -ItemType Directory -Force -Path $work | Out-Null
Copy-Item (Join-Path $src '*.mjs') $work -Force
Copy-Item (Join-Path $src 'package.json') $work -Force
if (Test-Path (Join-Path $src 'package-lock.json')) {
  Copy-Item (Join-Path $src 'package-lock.json') $work -Force
}
if (Test-Path (Join-Path $src '.data')) {
  Copy-Item (Join-Path $src '.data') $work -Force
}

Push-Location $work
try {
  if (-not (Test-Path 'node_modules\playwright\package.json')) {
    npm install --silent
    npx playwright install chromium
  }
  node spmb_register.mjs @Args
  $code = $LASTEXITCODE
} finally {
  Pop-Location
}

if (Test-Path (Join-Path $work 'spmb_output')) {
  Copy-Item (Join-Path $work 'spmb_output\*') (Join-Path $src 'spmb_output') -Recurse -Force -ErrorAction SilentlyContinue
}

exit $code
