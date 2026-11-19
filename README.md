# Corporate Credit Risk Analysis

A public-disclosure-based corporate credit portfolio assessing real businesses across luxury goods and natural resources. The work combines company-reported financial information with transparent analyst calculations to evaluate business risk, leverage, cash generation, liquidity, refinancing exposure and downside resilience.

## Current credit memorandum programme

| Issuer | Listing | Sector | Status |
|---|---|---|---|
| LVMH | Euronext Paris: MC | Luxury goods | [FY2025 / H1 2026 credit memorandum](credit_memos/LVMH_FY2025_H1_2026_Credit_Committee_Memorandum.md) — completed |
| Richemont | SIX Swiss Exchange: CFR | Luxury goods | [FY2026 / H1 FY2027 credit memorandum](credit_memos/Richemont_FY2026_H1_FY2027_Credit_Committee_Memorandum.md) — completed |
| BHP | ASX: BHP | Mining and natural resources | [FY2026 / Q1 FY2027 credit memorandum](credit_memos/BHP_FY2026_Q1_FY2027_Credit_Committee_Memorandum.md) — completed |

### Comparative analysis

[Comparative Credit Analysis — LVMH, Richemont and BHP](credit_memos/Comparative_Credit_Analysis_LVMH_Richemont_BHP.md)

The comparative paper evaluates business risk, balance-sheet flexibility, cash generation, capital allocation, downside sensitivities and preliminary lender posture across all three issuers. It explicitly flags differences in reporting periods, currencies and company-defined financial measures.

## Existing ASX credit-screen dataset

The repository also retains a separate public-disclosure credit-screen dataset for three Australian listed issuers:

| Issuer | ASX code | Reporting period |
|---|---|---|
| SGH Limited | SGH | FY2026 |
| ALS Limited | ALQ | FY2026 |
| Lindsay Australia Limited | LAU | FY2026 |

These legacy issuer datasets and scripts are separate from the new LVMH / Richemont / BHP memorandum programme. They use actual company disclosures; they are not synthetic borrower portfolios.

## Existing model capabilities

- Calculates profitability margins, cash conversion and selected debt-service ratios where input definitions permit.
- Preserves company-reported leverage and interest-cover definitions.
- Runs transparent downside sensitivities using explicitly stated assumptions.
- Includes sourced contractual debt maturity schedules.
- Separates disclosed covenant thresholds, reported compliance statements and analyst-calculated headroom.
- Produces CSV outputs for the base credit screen and downside scenario.

## Run the existing ASX model

Requires Python 3.9+ and uses only the standard library.

```bash
python src/credit_screen.py
python src/debt_covenant_analysis.py
python -m unittest discover -s tests
```

Outputs:
- `outputs/base_credit_screen.csv`
- `outputs/downside_stress.csv`
- `outputs/debt_maturity_summary.csv`
- `outputs/covenant_summary.csv`

## Credit analysis boundaries

This is an **issuer-level corporate credit analysis**, not a bank's customer loan book or an internal credit rating. Public filings do not ordinarily disclose lender-specific facility exposure, borrower PD, LGD, EAD, internal risk grades or lender-certified covenant calculations. Those metrics are not fabricated.

Reported leverage, interest coverage and free cash flow definitions can differ between issuers. The analysis preserves those definitions and flags comparability limitations rather than forcing false like-for-like comparisons. Analyst sensitivities are illustrative scenarios, not company forecasts.

See [methodology](docs/methodology.md), [data dictionary](docs/data_dictionary.md) and [source register](docs/sources.md).
