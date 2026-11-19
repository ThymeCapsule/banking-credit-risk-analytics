#!/usr/bin/env python3
"""Summarise disclosed FY2026 debt maturities and covenant disclosures.

Run from repository root: python src/debt_covenant_analysis.py
Uses only the Python standard library. Does not infer undisclosed covenant headroom.
"""
from __future__ import annotations
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUT = ROOT / "outputs"

def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

def main():
    maturity_rows = read_csv(DATA / "debt_maturity_fy2026.csv")
    covenant_rows = read_csv(DATA / "covenant_disclosures_fy2026.csv")

    maturity_totals = defaultdict(float)
    for row in maturity_rows:
        amount = row["contractual_cash_flows_aud_m"].strip()
        if amount:
            maturity_totals[(row["company"], row["asx_code"], row["instrument"], row["maturity_bucket"])] += float(amount)

    maturity_output = []
    for (company, code, instrument, bucket), amount in sorted(maturity_totals.items()):
        maturity_output.append({
            "company": company,
            "asx_code": code,
            "instrument": instrument,
            "maturity_bucket": bucket,
            "contractual_cash_flows_aud_m": f"{amount:.3f}",
            "basis": "Undiscounted contractual cash flows; not carrying value",
        })

    covenant_output = []
    for row in covenant_rows:
        covenant_output.append({
            "company": row["company"],
            "asx_code": row["asx_code"],
            "covenant_name": row["covenant_name"],
            "threshold": row["threshold"],
            "reported_metric": row["reported_metric"],
            "metric_value": row["metric_value"],
            "headroom": row["headroom"],
            "compliance_status": row["compliance_status"],
            "notes": row["notes"],
        })

    OUTPUT.mkdir(exist_ok=True)
    for filename, rows in [
        ("debt_maturity_summary.csv", maturity_output),
        ("covenant_summary.csv", covenant_output),
    ]:
        with (OUTPUT / filename).open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    print(f"Processed {len(maturity_rows)} maturity disclosure rows and {len(covenant_rows)} covenant disclosure rows.")
    print(f"Outputs written to {OUTPUT}")

if __name__ == "__main__":
    main()
