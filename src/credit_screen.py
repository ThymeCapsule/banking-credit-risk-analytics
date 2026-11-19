#!/usr/bin/env python3
"""Issuer-level credit screening and mechanical downside sensitivity.

Run from repository root: python src/credit_screen.py
Uses only the Python standard library. No synthetic issuer data is generated.
"""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "asx_issuer_financials_fy2026.csv"
OUTPUT = ROOT / "outputs"
EBITDA_DOWNSIDE = 0.20
FINANCE_COST_UPSIDE = 0.20

def number(row, key):
    value = row.get(key, "").strip()
    return float(value) if value else None

def ratio(numerator, denominator):
    if numerator is None or denominator in (None, 0):
        return None
    return numerator / denominator

def fmt(value, decimals=3):
    return "" if value is None else f"{value:.{decimals}f}"

def main():
    with INPUT.open(newline="", encoding="utf-8") as handle:
        issuers = list(csv.DictReader(handle))
    base_rows, stress_rows = [], []
    for row in issuers:
        revenue = number(row, "revenue")
        ebitda = number(row, "ebitda_statutory")
        ebit = number(row, "ebit_reported")
        npat = number(row, "npat_statutory")
        ocf = number(row, "operating_cash_flow")
        leverage = number(row, "reported_net_leverage")
        cover = number(row, "reported_interest_cover")
        ebitda_margin = ratio(ebitda, revenue)
        ebit_margin = ratio(ebit, revenue)
        npat_margin = ratio(npat, revenue)
        cash_conversion = ratio(ocf, ebitda)
        base_rows.append({
            "company": row["company"], "asx_code": row["asx_code"],
            "reporting_period_end": row["reporting_period_end"],
            "revenue_aud_m": fmt(revenue, 1), "ebitda_aud_m": fmt(ebitda, 1),
            "ebit_aud_m": fmt(ebit, 1), "statutory_npat_aud_m": fmt(npat, 1),
            "ebitda_margin_pct": fmt(ebitda_margin * 100 if ebitda_margin is not None else None, 2),
            "ebit_margin_pct": fmt(ebit_margin * 100 if ebit_margin is not None else None, 2),
            "npat_margin_pct": fmt(npat_margin * 100 if npat_margin is not None else None, 2),
            "operating_cash_flow_aud_m": fmt(ocf, 1),
            "ocf_to_ebitda_pct": fmt(cash_conversion * 100 if cash_conversion is not None else None, 2),
            "company_reported_net_leverage_x": fmt(leverage, 2),
            "interest_cover_x": fmt(cover, 2),
            "interest_cover_definition": row["interest_cover_basis"],
            "source_url": row["source_url"],
        })
        stressed_leverage = leverage / (1 - EBITDA_DOWNSIDE) if leverage is not None else None
        stressed_cover = cover * (1 - EBITDA_DOWNSIDE) / (1 + FINANCE_COST_UPSIDE) if cover is not None else None
        stress_rows.append({
            "company": row["company"], "asx_code": row["asx_code"],
            "scenario": "EBITDA -20%; finance costs +20%; net debt held constant",
            "base_net_leverage_x": fmt(leverage, 2),
            "stressed_net_leverage_x": fmt(stressed_leverage, 2),
            "base_interest_cover_x": fmt(cover, 2),
            "stressed_interest_cover_x": fmt(stressed_cover, 2),
            "assumption": "Mechanical sensitivity only; not a forecast, probability or covenant test.",
        })
    OUTPUT.mkdir(exist_ok=True)
    for filename, rows in [("base_credit_screen.csv", base_rows), ("downside_stress.csv", stress_rows)]:
        with (OUTPUT / filename).open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    print(f"Processed {len(issuers)} real ASX issuers.")
    print(f"Outputs written to {OUTPUT}")

if __name__ == "__main__":
    main()
