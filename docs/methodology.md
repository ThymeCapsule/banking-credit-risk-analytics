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

## Debt maturity analysis

The FY2026 maturity dataset is sourced from the contractual liquidity-risk disclosures in each annual report. It preserves each issuer's disclosed maturity buckets and separates instruments such as bank loans, notes and lease liabilities.

- Contractual cash flows are undiscounted and may include interest, derivatives or other contractual payments; they are not equivalent to balance-sheet carrying values.
- Maturity buckets differ between issuers because the underlying annual-report disclosures differ.
- Foreign currency amounts are represented using the issuer's AUD reporting presentation.
- Where the annual report provides weighted-average debt maturity, it is quoted separately and not reverse-engineered from maturity buckets.

## Covenant analysis

Covenant thresholds and compliance statements are transcribed from annual-report disclosures. Headroom is calculated only where the published ratio is sufficiently aligned with the disclosed covenant definition.

- ALS: disclosed thresholds are interest cover greater than 3.75x and financial leverage below 3.25x. The company's 13.5x cover and 1.5x leverage are aligned to the pre-IFRS16 covenant basis. Simple arithmetic headroom is shown, but is not represented as a lender-certified covenant calculation.
- Lindsay Australia: disclosed thresholds are gross leverage below 3.50x, interest cover above 2.50x and debt service cover above 1.20x. The company states compliance, but actual facility calculation values are not disclosed. The model does not substitute its 1.92x net leverage or analyst-calculated 5.93x interest cover.
- SGH: financial covenant thresholds and calculations were not identified in the reviewed FY2026 annual-report disclosure; they are marked not publicly quantified.

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
- ALS's 1.5x is net debt / adjusted underlying EBITDA on a pre-IFRS16 basis. Its 13.5x reported interest cover uses adjusted underlying EBITDA and net finance expense on loans and borrowings.
- Lindsay Australia's 1.92x is company-reported net leverage. The 5.93x model base cover is an analyst calculation using reported EBITDA divided by segment net finance costs; it is not a company covenant metric.
- Company leverage definitions are not perfectly comparable.
- For Lindsay Australia, borrowings less cash exclude lease liabilities; do not equate this arithmetic net bank debt with company-reported net leverage.
- No company-specific PD, LGD, EAD, internal rating or lender-side IFRS 9 stage is inferred.

## Model limitations

The current issuer set is small and spans different industries and reporting dates. The scorecard is a screening aid, not a statistically calibrated rating model. Public disclosure does not provide complete facility agreements, covenant certificates, waiver terms, amortisation schedules or lender-specific definitions. A full credit memorandum should also incorporate working capital, security, refinancing risk, customer concentration, industry outlook and management actions.
