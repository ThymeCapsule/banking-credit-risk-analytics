# Data dictionary

File: `data/asx_issuer_financials_fy2026.csv`. Monetary amounts are AUD millions unless stated otherwise.

| Field | Definition |
|---|---|
| company / asx_code | Issuer name and ASX ticker |
| sector | Broad issuer sector |
| reporting_period_end | Financial year-end date |
| currency / unit | Reporting currency and scale |
| revenue | Reported FY2026 revenue |
| ebitda_statutory | EBITDA from the financial statements or results presentation; check notes for issuer basis |
| ebit_reported | Reported EBIT |
| npat_statutory | Statutory NPAT |
| net_debt_reported | Net debt where explicitly reported and directly available |
| reported_net_leverage | Company-reported net leverage |
| leverage_ebitda_basis | EBITDA denominator used for the leverage measure, where identified |
| reported_interest_cover | Company-reported cover or a clearly labelled analyst calculation |
| interest_cover_basis | Exact definition and provenance of the coverage ratio |
| net_finance_cost | Net finance cost, with scope explained in notes |
| operating_cash_flow | Net operating cash flow where directly reported |
| borrowings / cash / lease_liabilities | Balance-sheet amounts where available |
| source_url | Direct source URL |
| notes | Definitions, scope and caveats |

Blank fields mean not available in the source extract; they do not mean zero. Do not replace missing data with estimates without adding a separately labelled derived field and documenting the formula.
