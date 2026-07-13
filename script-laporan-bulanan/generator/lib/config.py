# -*- coding: utf-8 -*-
import json
from pathlib import Path

def project_root():
    return Path(__file__).resolve().parent.parent.parent

def load_config(period):
    root = project_root()
    config_path = root / "input" / period / "config.json"
    if not config_path.exists():
        raise FileNotFoundError("Config tidak ditemukan: " + str(config_path))
    cfg = json.loads(config_path.read_text(encoding="utf-8"))
    cfg["period"] = period
    return cfg

def input_dir(period):
    return project_root() / "input" / period

def output_dir(period):
    path = project_root() / "output" / period
    path.mkdir(parents=True, exist_ok=True)
    return path

def template_dir():
    return project_root() / "template"

def weekly_report_path(period):
    """Cari weekly report: coba YYYYMM_weekly_report.md dulu, fallback ke weekly_report.md"""
    inp = input_dir(period)
    timestamped = inp / f"{period}_weekly_report.md"
    if timestamped.exists():
        return timestamped
    return inp / "weekly_report.md"
