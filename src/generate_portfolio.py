#!/usr/bin/env python3
"""Generate a deterministic synthetic Australian business loan portfolio.

Uses only the Python standard library. All records and assumptions are fictional.
Run from the repository root: python src/generate_portfolio.py
"""
from __future__ import annotations

import csv
from datetime import date, timedelta
from pathlib import Path

SEED = 20261119
ROWS = 1000
OUTPUT = Path(__file__).resolve().parents[1] / "data" / "synthetic_loan_portfolio.csv"

SECTORS = [
    "Agriculture", "Construction", "Healthcare", "Manufacturing",
    "Professional Services", "Retail Trade", "Transport and Logistics",
    "Accommodation and Food", "Wholesale Trade", "Technology",
]
PRODUCTS = ["Term Loan", "Business Overdraft", "Commercial Property Loan"]
SIZES = ["SME", "Mid-market"]

class LCG:
    """Small deterministic linear congruential generator shared with the CSV build."""
    def __init__(self, seed: int):
        self.state = seed

    def next(self) -> float:
        self.state = (1664525 * self.state + 1013904223) % 4294967296
        return self.state / 4294967296

    def integer(self, low: int, high: int) -> int:
        return low + int(self.next() * (high - low + 1))

    def choice(self, values):
        return values[min(int(self.next() * len(values)), len(values) - 1)]

    def uniform(self, low: float, high: float) -> float:
        return low + self.next() * (high - low)


def main() -> None:
    rng = LCG(SEED)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "facility_id", "customer_id", "sector", "business_size", "product_type",
        "origination_date", "maturity_months", "drawn_balance_aud",
        "undrawn_commitment_aud", "credit_conversion_factor", "original_pd_12m",
        "current_pd_12m", "original_lifetime_pd", "current_lifetime_pd", "lgd",
        "days_past_due", "default_flag", "collateral_value_aud",
        "effective_interest_rate", "risk_grade",
    ]
    report_date = date(2026, 10, 31)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for i in range(1, ROWS + 1):
            size = rng.choice(SIZES)
            product = rng.choice(PRODUCTS)
            sector = rng.choice(SECTORS)
            grade = rng.integer(1, 10)
            original_pd = min(0.18, 0.0015 * (1.62 ** (grade - 1)))
            deterioration = rng.uniform(0.65, 2.8)
            current_pd = min(0.45, original_pd * deterioration)
            original_life = min(0.55, original_pd * rng.uniform(2.0, 4.2))
            current_life = min(0.75, current_pd * rng.uniform(2.0, 4.2))
            lgd = rng.uniform(0.18, 0.65)
            drawn = rng.uniform(25000, 2500000 if size == "SME" else 12000000)
            undrawn = rng.uniform(0, drawn * 0.65)
            ccf = rng.uniform(0.2, 0.75)
            dpd = rng.choice([0, 0, 0, 0, 5, 12, 20, 35, 55, 75, 95, 125])
            default_flag = 1 if dpd >= 90 and rng.next() < 0.75 else 0
            if default_flag:
                dpd = max(dpd, 90)
            collateral = drawn * rng.uniform(0.0, 1.35)
            months = rng.integer(6, 120)
            age_days = rng.integer(30, 2500)
            origination = report_date - timedelta(days=age_days)
            eir = rng.uniform(0.045, 0.115)
            writer.writerow({
                "facility_id": f"FAC{i:05d}",
                "customer_id": f"CUST{((i - 1) // 2) + 1:05d}",
                "sector": sector,
                "business_size": size,
                "product_type": product,
                "origination_date": origination.isoformat(),
                "maturity_months": months,
                "drawn_balance_aud": f"{drawn:.2f}",
                "undrawn_commitment_aud": f"{undrawn:.2f}",
                "credit_conversion_factor": f"{ccf:.4f}",
                "original_pd_12m": f"{original_pd:.6f}",
                "current_pd_12m": f"{current_pd:.6f}",
                "original_lifetime_pd": f"{original_life:.6f}",
                "current_lifetime_pd": f"{current_life:.6f}",
                "lgd": f"{lgd:.4f}",
                "days_past_due": dpd,
                "default_flag": default_flag,
                "collateral_value_aud": f"{collateral:.2f}",
                "effective_interest_rate": f"{eir:.4f}",
                "risk_grade": grade,
            })
    print(f"Wrote {ROWS:,} synthetic facilities to {OUTPUT}")

if __name__ == "__main__":
    main()
