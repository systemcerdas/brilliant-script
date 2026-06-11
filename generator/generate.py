# -*- coding: utf-8 -*-
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.config import input_dir, load_config
from lib.docx_builder import build_report
from lib.github import load_or_fetch_prs


def main():
    parser = argparse.ArgumentParser(description="Generate Laporan Bulanan")
    parser.add_argument("period", help="YYYYMM contoh 202605")
    parser.add_argument("--fetch-prs", action="store_true", help="Paksa fetch ulang PR dari GitHub")
    args = parser.parse_args()

    config = load_config(args.period)
    if args.fetch_prs:
        config.setdefault("github", {})["fetch_always"] = True

    prs = load_or_fetch_prs(config, input_dir(args.period) / "prs.json")
    output = build_report(config, prs)
    print("Selesai:", output)
    print("Total PR:", len(prs))
    print("Buka di Word -> klik kanan Daftar Isi -> Update Field untuk nomor halaman.")


if __name__ == "__main__":
    main()
