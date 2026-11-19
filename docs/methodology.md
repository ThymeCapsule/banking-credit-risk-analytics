# Credit screening methodology

## Purpose and scope

The model screens the financial resilience of real ASX-listed issuers using public FY2026 disclosures. It is not a bank internal rating, borrower-level PD model or IFRS 9 ECL engine.

## Input hierarchy

1. Audited annual financial statements and notes.
2. ASX results announcements and investor presentations.
3. Company-defined non-IFRS measures, only where explicitly labelled.

Every issuer input has a source URL and notes. Company-defined measures are retained as reported. Statutory and adjusted metrics are not silently mixed.

## Base ratios

- EBITDA margin = reported EBITDA / revenue.
- EBIT margin = reported EBIT / revenue.
- Statutory NPAT margin = statutory NPAT / revenue.
- Operating cash flow conversion = operating cash flow / EBITDA, only shown as a screening indicator and interpreted cautiously.
- Net leverage = company-reported net leverage. The underlying EBITDA denominator is documented separately where known.
- Interest cover = company-reported interest cover where available. If not reported, an analyst calculation is shown only when its numerator and denominator are explicitly identified.

## Downside sensitivity

The illustrative downside scenario applies:
- EBITDA reduction: 20%.
- Finance-cost increase: 20%.
- Net debt held constant.
- No management actions, asset sales, refinancing, tax effects or working-capital offsets.

Stressed leverage = base reported leverage / (1 - EBITDA decline), assuming the reported leverage denominator declines in line with EBITDA and net debt is unchanged.

Stressed interest cover = base interest cover × (1 - EBITDA decline) / (1 + finance-cost increase).

These are mechanical sensitivities, not forecasts or probabilities. The scenario does not replace a full integrated cash flow, debt maturity, liquidity and covenant model.

## Interpretation guardrails

- SGH's 1.8x is adjusted net debt / EBITDA as disclosed by the company.
- ALS's 1.5x is net debt / adjusted underlying EBITDA on a pre-IFRS16 basis. Its 13.5x reported interest cover uses adjusted underlying EBITDA divided by net finance expense on loans and borrowings.
- Lindsay Australia's 1.92x is company-reported net leverage. The 5.93x model base cover is an analyst calculation using reported EBITDA divided by segment net finance costs; it is not a company covenant metric.
- Company leverage definitions are not perfectly comparable.
- For Lindsay Australia, borrowings less cash exclude lease liabilities; do not equate this arithmetic net bank debt with company-reported net leverage.
- No company-specific PD, LGD, EAD, internal rating or lender-side IFRS 9 stage is inferred.

## Model limitations

The current issuer set is small and spans different industries and reporting dates. The scorecard is a screening aid, not a statistically calibrated rating model. A fuller credit memorandum should incorporate debt maturity ladders, committed facilities, covenant headroom, security, refinancing risk, working capital, customer concentration, industry outlook and management actions.
