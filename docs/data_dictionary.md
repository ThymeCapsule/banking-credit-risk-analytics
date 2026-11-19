# Data dictionary

File: `data/asx_issuer_financials_fy2026.csv`

All company names are real ASX-listed issuers. Monetary amounts are in AUD millions unless otherwise stated.

| Field | Definition |
|---|---|
| company | Legal issuer name |
| asx_code | ASX ticker |
| sector | Broad business sector |
| reporting_period | Financial year-end period covered |
| currency | Reporting currency |
| unit | Unit used for financial amounts |
| revenue_fy26 | FY26 reported revenue |
| ebitda_fy26 | FY26 EBITDA as disclosed in the cited source |
| ebit_fy26 | FY26 EBIT as disclosed |
| npat_fy26 | FY26 net profit after tax |
| net_debt_fy26 | Net debt, only where directly disclosed in the cited source |
| company_reported_leverage | Leverage measure reported by the company; definitions may differ by issuer |
| net_finance_cost_fy26 | Reported net finance/interest cost where available |
| interest_cover_ebit_to_net_finance_cost | Analyst calculation: EBIT divided by net finance cost; only populated where source definitions support the calculation |
| operating_cash_flow_fy26 | Operating cash flow, only where directly available in the source extract |
| source_type | Type of public disclosure used |
| source_url | Direct URL to the cited disclosure |
| notes | Comparability caveats and calculation notes |

## Missing values

An empty field means the relevant metric was not included in this initial extraction or was not sufficiently comparable. It does not mean zero. Do not impute missing figures without documenting the source and method.

## Comparability

- Financial year-ends differ: ALS reports to 31 March; SGH and Lindsay Australia report to 30 June.
- Company-defined leverage metrics may use adjusted EBITDA, lease-adjusted debt or other definitions. Do not assume they are directly comparable.
- EBIT/finance-cost coverage is an analyst calculation and is not necessarily the covenant interest cover used by lenders.
- Reported EBITDA may be underlying or statutory depending on the company's disclosure. Refer to the notes and source register.
