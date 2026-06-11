# -*- coding: utf-8 -*-
import json
import subprocess

def fetch_prs(repo, author, date_ranges):
    all_prs = []
    seen = set()
    for dr in date_ranges:
        result = subprocess.run(
            ["gh", "search", "prs", "--repo", repo, "--author", author,
             "--created", dr, "--limit", "100", "--json", "number,title,state"],
            capture_output=True, text=True, encoding="utf-8",
        )
        if result.returncode != 0:
            raise RuntimeError("gh search gagal (" + dr + "): " + result.stderr)
        for pr in json.loads(result.stdout or "[]"):
            if pr["number"] not in seen:
                seen.add(pr["number"])
                all_prs.append(pr)
    all_prs.sort(key=lambda x: x["number"])
    return all_prs

def load_or_fetch_prs(config, prs_path):
    gh = config.get("github", {})
    if prs_path.exists() and not gh.get("fetch_always", False):
        return sorted(json.loads(prs_path.read_text(encoding="utf-8")), key=lambda x: x["number"])
    if not gh.get("fetch_if_missing", True) and not gh.get("fetch_always", False):
        return []
    prs = fetch_prs(gh["repo"], gh["author"], gh["date_ranges"])
    prs_path.write_text(json.dumps(prs, ensure_ascii=False, indent=2), encoding="utf-8")
    return prs
