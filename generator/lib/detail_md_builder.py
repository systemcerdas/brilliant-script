# -*- coding: utf-8 -*-
import re
from collections import defaultdict

from .module_mapper import build_module_intro, build_prolog, load_modules_config, match_module
from .pr_details import build_utama_from_prs, extract_pr_numbers, fetch_pr_detail, pr_files, pr_title


def parse_weekly_activities(path, user_filter="Lutfi"):
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "Weekly" in line or "-----" in line:
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) < 7:
            continue
        weekly, date_range, day, activity, output, user, links = cols[:7]
        if not activity.strip():
            continue
        if user_filter and user_filter.lower() not in user.lower():
            continue
        rows.append({
            "weekly": weekly,
            "date_range": date_range,
            "day": day,
            "activity": re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", activity).strip(),
            "output": re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", output).strip(),
            "links": links.strip(),
            "pr_numbers": extract_pr_numbers(links),
        })
    return rows


def group_activities_by_module(activities, modules_cfg):
    grouped = defaultdict(list)
    for act in activities:
        mod = match_module(act["activity"], act["output"], modules_cfg)
        grouped[mod["id"]].append((mod, act))
    return grouped


def _deskripsi_from_activity(act, repo):
    output = act["output"]
    if output and len(output) > 30:
        text = output[0].upper() + output[1:] if output else output
        if not text.startswith("Telah"):
            text = f"Telah dilakukan implementasi terkait {act['activity'].lower()}. {text}"
        return text
    pr_nums = act["pr_numbers"]
    if pr_nums:
        detail = fetch_pr_detail(repo, pr_nums[0])
        title = pr_title(detail)
        if title:
            return f"Telah dilakukan pekerjaan terkait {act['activity'].lower()}, dengan perubahan utama pada PR #{pr_nums[0]} ({title})."
    return f"Telah dilakukan pekerjaan terkait {act['activity'].lower()} pada sistem pengawasan SDKP."


def _collect_files(repo, pr_numbers):
    files = []
    seen = set()
    for num in pr_numbers:
        detail = fetch_pr_detail(repo, num)
        for f in pr_files(detail):
            if f not in seen:
                seen.add(f)
                files.append(f)
    return files


def render_activity_md(act, mod, modules_cfg, repo, sub_idx):
    prolog = build_prolog(act["activity"], mod, act["output"], modules_cfg)
    deskripsi = _deskripsi_from_activity(act, repo)
    files = _collect_files(repo, act["pr_numbers"])
    utama = build_utama_from_prs(repo, act["pr_numbers"])
    docs = []
    for num in act["pr_numbers"]:
        docs.append(f"https://github.com/{repo}/pull/{num}")
    for m in re.finditer(r"https://github\.com/[^\s\)]+/commit/[a-f0-9]+", act["links"]):
        url = m.group(0).rstrip(")")
        if url not in docs:
            docs.append(url)

    lines = [
        f"### {sub_idx} {act['activity']}",
        "",
        "**Prolog**",
        "",
        prolog,
        "",
        "**Deskripsi Pekerjaan**",
        "",
        deskripsi,
        "",
        "**Detail Perubahan**",
        "",
    ]
    if files:
        lines += ["**File yang Diubah:**"] + [f"- `{f}`" for f in files] + [""]
    if utama:
        lines += ["**Perubahan Utama:**"] + [f"- {u}" for u in utama] + [""]
    else:
        lines += [
            "**Perubahan Utama:**",
            "- <!-- ENRICH: jelaskan perubahan teknis dari diff PR -->",
            "",
        ]
    lines += [
        "**Manfaat:**",
        "- <!-- ENRICH: jelaskan manfaat bisnis/teknis -->",
        "",
        "**Dokumentasi**",
    ]
    if docs:
        lines += [f"- {d}" for d in docs]
    else:
        lines += ["- <!-- tambahkan link PR/commit -->"]
    lines += ["", "---", ""]
    return "\n".join(lines)


def build_from_weekly(weekly_path, config, user_filter="Lutfi"):
    modules_cfg = load_modules_config()
    repo = config["github"]["repo"]
    activities = parse_weekly_activities(weekly_path, user_filter)
    grouped = group_activities_by_module(activities, modules_cfg)

    bulan = config.get("bulan", "")
    tahun = config.get("tahun", "")
    period = config.get("period", "")
    nama = config.get("nama", "LUTFI IHSAN").upper()

    lines = [
        f"# DETAIL LAPORAN KEGIATAN GITHUB — {nama}",
        f"## Bulan {bulan} {tahun} (Periode Weekly Report)",
        "",
        f"Sumber data: `input/{period}/weekly_report.md`",
        "Format acuan: `template/contoh_format.docx`",
        "",
        "> **Catatan:** Bagian `<!-- ENRICH -->` perlu dilengkapi via Cursor AI.",
        "> Jalankan: `python generator/generate_detail_md.py {period} --prompt`",
        "",
        "---",
        "",
    ]

    mod_order = [m["id"] for m in modules_cfg["modules"]]
    mod_by_id = {m["id"]: m for m in modules_cfg["modules"]}
    module_num = 0

    for mod_id in mod_order:
        items = grouped.get(mod_id, [])
        if not items:
            continue
        module_num += 1
        mod = mod_by_id[mod_id]
        lines += [
            f"## {module_num}. {mod['title']}",
            "",
            build_module_intro(mod, modules_cfg),
            "",
        ]
        for sub_idx, (_, act) in enumerate(items, 1):
            lines.append(render_activity_md(act, mod, modules_cfg, repo, f"{module_num}.{sub_idx}"))

    lines += [
        "## RINGKASAN KEGIATAN",
        "",
        f"Total sub-kegiatan dari weekly report: **{len(activities)}**",
        "",
    ]
    return "\n".join(lines)


def inject_prologs(md_content, modules_cfg=None, refresh=False):
    modules_cfg = modules_cfg or load_modules_config()
    lines = md_content.splitlines()
    out = []
    i = 0
    current_mod = modules_cfg["modules"][0]

    while i < len(lines):
        line = lines[i]
        if line.startswith("### "):
            subtitle = re.sub(r"^\d+\.\d+\s*", "", line[4:].strip())
            out.append(line)
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            has_prolog = i < len(lines) and lines[i].strip() == "**Prolog**"
            if has_prolog and refresh:
                out.extend(["", "**Prolog**", "", build_prolog(subtitle, current_mod, "", modules_cfg), ""])
                i += 1
                while i < len(lines) and lines[i].strip() != "**Deskripsi Pekerjaan**":
                    i += 1
                continue
            if not has_prolog:
                out.extend(["", "**Prolog**", "", build_prolog(subtitle, current_mod, "", modules_cfg), ""])
            continue

        out.append(line)
        if line.startswith("## ") and re.match(r"## \d+\.", line):
            title = re.sub(r"^\d+\.\s*", "", line[3:].strip())
            title = re.sub(r"^KEGIATAN TAMBAHAN —\s*", "", title)
            for mod in modules_cfg["modules"]:
                if mod["title"].lower() in title.lower() or title.lower() in mod["title"].lower():
                    current_mod = mod
                    break
        i += 1

    return "\n".join(out)


def build_enrich_prompt(md_path, period):
    content = md_path.read_text(encoding="utf-8")
    return f"""# Prompt Enrichment Detail Laporan — {period}

Gunakan file `{md_path.name}` sebagai target edit.

## Tugas
Lengkapi setiap sub-kegiatan (`###`) yang masih berisi `<!-- ENRICH -->` atau prolog/deskripsi yang terlalu singkat.

## Format wajib per sub-kegiatan

```
### X.Y Judul Kegiatan

**Prolog**
[1-2 kalimat konteks: apa, modul apa, mengapa]

**Deskripsi Pekerjaan**
[Paragraf formal: Telah diimplementasikan/dilakukan...]

**Detail Perubahan**

**File yang Diubah:**
- `path/file.php`

**Perubahan Utama:**
- poin teknis spesifik

**Manfaat:**
- manfaat bisnis/operasional

**Dokumentasi**
- link PR
```

## Sumber data
1. Baca diff PR via `gh pr view <num> --repo setditjen-psdkp/api-sip`
2. Cross-check `weekly_report.md` dan `prs.json` di folder `input/{period}/`
3. Ikuti gaya penulisan file referensi `input/{period}/detail_github.md`

## Aturan penulisan
- Bahasa Indonesia formal (Tenaga Teknis Implementasi Logika Sistem)
- Prolog: konteks singkat sebelum deskripsi detail
- Hindari copy-paste judul PR mentah sebagai deskripsi
- Gabungkan PR terkait dalam satu sub-kegiatan jika satu aktivitas weekly

## File saat ini

```markdown
{content[:8000]}
{"..." if len(content) > 8000 else ""}
```
"""
