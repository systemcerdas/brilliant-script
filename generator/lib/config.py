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
    return json.loads(config_path.read_text(encoding="utf-8"))

def input_dir(period):
    return project_root() / "input" / period

def output_dir(period):
    path = project_root() / "output" / period
    path.mkdir(parents=True, exist_ok=True)
    return path

def template_dir():
    return project_root() / "template"
