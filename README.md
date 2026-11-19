# Australian Corporate Credit Risk Analysis

A public-disclosure-based credit analysis of real Australian listed businesses. The project extracts reported financial information, calculates transparent screening ratios and compares issuer-level credit risk indicators across sectors.

## Scope and data integrity

**This is an issuer-level credit analysis, not a bank's loan book.** Public annual reports disclose company financial statements, borrowings, liquidity, interest costs and selected credit-risk information. They generally do not disclose a lender's facility-level drawn exposure, internal PD, LGD, EAD, credit grade or IFRS 9 stage for each borrower.

Accordingly:
- Company identities and reported figures relate to real ASX-listed businesses.
- Reported metrics are transcribed from public FY2026 company disclosures.
- Calculated ratios are labelled as analyst calculations and show their formulas.
- Undisclosed lender-specific measures are left blank/not available; they are not fabricated.
- No synthetic company names or synthetic borrower financials are used.

## Initial issuer universe

| Issuer | ASX code | Reporting period | Sector |
|---|---|---|---|
| SGH Limited | SGH | Year ended 30 June 2026 | Industrial services / diversified |
| ALS Limited | ALQ | Year ended 31 March 2026 | Testing, inspection and certification |
| Lindsay Australia Limited | LAU | Year ended 30 June 2026 | Transport and logistics |

## Initial analytical coverage

- Revenue, EBITDA, EBIT and net profit
- Net debt and company-reported leverage where disclosed
- Interest coverage calculated from reported EBIT and net finance costs where comparable
- Cash flow, liquidity and debt maturity indicators where disclosed
- Credit-risk disclosures, receivables quality and impairment information
- Sector concentration and comparative issuer screening

## Repository structure

```text
.
├── data/
│   └── asx_issuer_financials_fy2026.csv
├── docs/
│   ├── data_dictionary.md
│   ├── methodology.md
│   └── sources.md
└── README.md
```

## Important limitations

These issuers are operating companies, not a disclosed portfolio of bank borrowers. A public-company credit screen is not an IFRS 9 ECL model. PD and LGD estimation would require a defined default dataset, rating methodology, recovery evidence and forward-looking calibration. EAD requires actual facility and commitment information. IFRS 9 staging requires the lender's origination-date and reporting-date credit-risk information and SICR policy.

The analysis is educational and is not a credit rating, investment recommendation, lending decision or substitute for professional credit assessment.

## Sources

See [source register](docs/sources.md) and [methodology](docs/methodology.md).
