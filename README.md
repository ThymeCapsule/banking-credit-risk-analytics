# Australian Corporate Credit Risk Analysis

A public-disclosure-based credit assessment of real ASX-listed businesses. The project uses company-reported FY2026 financials and transparent analyst calculations to assess leverage, debt-service capacity, cash generation, debt maturities, covenant compliance disclosures and downside resilience.

## Issuer universe

| Issuer | ASX code | Reporting period |
|---|---|---|
| SGH Limited | SGH | 30 June 2026 |
| ALS Limited | ALQ | 31 March 2026 |
| Lindsay Australia Limited | LAU | 30 June 2026 |

All issuers are real businesses. The dataset contains reported financial information extracted from public disclosures. No synthetic borrower or company financial data is used.

## What the model does

- Reads sourced company financials from `data/asx_issuer_financials_fy2026.csv`.
- Calculates profitability margins, cash conversion and selected debt-service ratios where the input definitions permit.
- Uses company-reported net leverage and interest cover, preserving each issuer's stated denominator and definition.
- Runs a transparent downside sensitivity: EBITDA falls 20% and finance costs rise 20%.
- Includes FY2026 contractual debt maturity schedules in `data/debt_maturity_fy2026.csv`.
- Separates disclosed covenant thresholds, reported compliance statements and analyst-calculated headroom in `data/covenant_disclosures_fy2026.csv`.
- Produces CSV outputs for the base credit screen and downside scenario.

## Run the model

Requires Python 3.9+ and uses only the standard library.

```bash
python src/credit_screen.py
python -m unittest discover -s tests
```

Outputs:
- `outputs/base_credit_screen.csv`
- `outputs/downside_stress.csv`

## Debt maturity and covenant work

See [debt maturity and covenant analysis](docs/debt_maturity_and_covenants.md) for issuer-level observations, covenant definitions, headroom treatment and limitations.

## Data and modelling boundaries

This is an **issuer-level corporate credit screen**, not a bank's customer loan book or an internal credit rating. Public filings do not ordinarily disclose each lender's facility-level exposure, borrower PD, LGD, EAD or lender-assigned IFRS 9 stage. Those metrics are not invented.

Reported leverage and interest coverage definitions differ between companies. The model retains those definitions and flags comparability limitations rather than forcing a false like-for-like comparison. Stress assumptions are analyst-selected sensitivities, not company forecasts.

See [methodology](docs/methodology.md), [data dictionary](docs/data_dictionary.md) and [source register](docs/sources.md).
