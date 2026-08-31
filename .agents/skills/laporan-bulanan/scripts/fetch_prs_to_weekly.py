import json
import subprocess
import datetime
import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Fetch PRs and generate raw weekly_report.md")
    parser.add_argument("period", help="YYYYMM contoh 202608")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent.parent.parent.parent / "script-laporan-bulanan"
    config_path = root / "input" / args.period / "config.json"
    
    if not config_path.exists():
        print(f"Error: Config {config_path} tidak ditemukan.")
        sys.exit(1)

    with open(config_path, encoding='utf-8') as f:
        config = json.load(f)

    repo = config.get("github", {}).get("repo")
    author = config.get("github", {}).get("author")
    tahun = str(config.get("tahun"))
    bulan_str = args.period[-2:]
    
    # ex: 2026-08-01..2026-08-31
    date_query = f"merged:{tahun}-{bulan_str}-01..{tahun}-{bulan_str}-31"
    
    print(f"Fetching PRs from {repo} for author {author} in {date_query}...")
    cmd = ['gh', 'pr', 'list', '-R', repo, '-S', f'author:{author} {date_query}', '--state', 'merged', '--json', 'number,title,mergedAt,url,body', '-L', '150']
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        prs = json.loads(result.stdout)
    except Exception as e:
        print(f"Error executing gh: {e}")
        sys.exit(1)
        
    prs.sort(key=lambda x: x['mergedAt'])

    rows = []
    for pr in prs:
        dt = datetime.datetime.fromisoformat(pr['mergedAt'].replace('Z', '+00:00'))
        day = dt.day
        
        if 1 <= day <= 10:
            cat = "W1"
            drange = "1-10"
        elif 11 <= day <= 20:
            cat = "W2"
            drange = "11-20"
        else:
            cat = "W3"
            drange = "21-31"
            
        title = pr['title'].replace('|', '-')
        body = pr.get('body', '').strip()
        
        if body:
            # Clean up newlines so it fits in one table row
            body = ' '.join(body.split())
            body = body.replace('|', '-')
        else:
            body = f"Implementasi {title}"
            
        rows.append(f"| {cat} | {drange} | {day} | {title} | {body} | Lutfi | {pr['url']} |")

    md_content = "# Weekly Report\n\nPic: Data\n\n| Weekly_ cat | date_range | date | activity | output | user | reltd_doc_link |\n| ----- | ----- | ----- | ----- | ----- | ----- | ----- |\n"
    md_content += "\n".join(rows) + "\n"

    out_path = root / "input" / args.period / "weekly_report.md"
    out_path.write_text(md_content, encoding='utf-8')
    print(f"Sukses! {len(prs)} PR telah diekstrak ke {out_path}.")
    print("Gunakan AI Prompt (PROMPT_POLES_WEEKLY.md) untuk merapikan tabel sebelum di-convert ke DOCX.")

if __name__ == "__main__":
    main()
