# -*- coding: utf-8 -*-
import json
import re

def _clean_md(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.strip()

def parse_detail_github(path):
    content = path.read_text(encoding="utf-8")
    modules = []
    current = None
    for line in content.splitlines():
        if line.startswith("## ") and re.match(r"## \d+\.", line):
            if current:
                modules.append(current)
            title = re.sub(r"^\d+\.\s*", "", line[3:].strip())
            title = re.sub(r"^KEGIATAN TAMBAHAN —\s*", "", title)
            current = {"title": title, "intro": None, "activities": []}
            continue
        if line.startswith("### ") and current is not None:
            subtitle = re.sub(r"^\d+\.\d+\s*", "", line[4:].strip())
            current["activities"].append({
                "subtitle": subtitle, "prolog": "", "deskripsi": "", "files": [],
                "utama": [], "manfaat": [], "docs": [], "_section": None,
            })
            continue
        if not current or not current["activities"]:
            if current and line.strip() and not line.startswith(("#", "-", "|", "---", ">")):
                current["intro"] = (current["intro"] or "") + (" " if current["intro"] else "") + line.strip()
            continue
        act = current["activities"][-1]
        stripped = line.strip()
        if stripped == "**Prolog**":
            act["_section"] = "prolog"
        elif stripped == "**Deskripsi Pekerjaan**":
            act["_section"] = "deskripsi"
        elif stripped == "**Detail Perubahan**":
            act["_section"] = "detail"
        elif stripped.startswith("**File yang Diubah"):
            act["_section"] = "files"
        elif stripped.startswith("**Perubahan Utama"):
            act["_section"] = "utama"
        elif stripped.startswith("**Manfaat"):
            act["_section"] = "manfaat"
        elif stripped == "**Dokumentasi**":
            act["_section"] = "docs"
        elif stripped in ("---", "") or stripped.startswith("<!--"):
            pass
        elif act["_section"] == "prolog":
            act["prolog"] += (" " if act["prolog"] else "") + _clean_md(stripped)
        elif act["_section"] == "deskripsi":
            act["deskripsi"] += (" " if act["deskripsi"] else "") + _clean_md(stripped)
        elif act["_section"] == "files" and stripped.startswith("- "):
            act["files"].append(stripped[2:].strip("`"))
        elif act["_section"] == "utama" and stripped.startswith("- "):
            val = _clean_md(stripped[2:])
            if not val.startswith("<!--"):
                act["utama"].append(val)
        elif act["_section"] == "manfaat" and stripped.startswith("- "):
            val = _clean_md(stripped[2:])
            if not val.startswith("<!--"):
                act["manfaat"].append(val)
        elif act["_section"] == "docs" and (stripped.startswith("- ") or stripped.startswith("http")):
            act["docs"].append(_clean_md(stripped[2:] if stripped.startswith("- ") else stripped))
    if current:
        modules.append(current)
    for mod in modules:
        for act in mod["activities"]:
            act.pop("_section", None)
    return modules

def parse_weekly_report(path, user_filter="Lutfi"):
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "Weekly" in line or "-----" in line:
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) < 6:
            continue
        weekly, date_range, day, activity, output, user = cols[:6]
        if not activity.strip():
            continue
        if user_filter and user_filter.lower() not in user.lower() and "tim" not in user.lower():
            continue
        rows.append({
            "minggu": weekly, "tanggal": date_range, "hari": day,
            "aktivitas": _clean_md(activity), "dokumentasi": _clean_md(output)[:120],
        })
    return rows

def load_kegiatan_tambahan(path):
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8")).get("kegiatan", [])
