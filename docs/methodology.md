# Methodology — public-company credit screening

## 1. Objective

Assess the capacity of real Australian listed businesses to service debt using publicly disclosed financial information. This is a company-level credit screening exercise, not a reconstruction of confidential bank facilities or internal borrower ratings.

## 2. Source hierarchy

1. Audited annual financial statements and notes.
2. ASX Appendix 4E and company results announcements.
3. Investor presentations, used with clear identification of non-IFRS measures.

Every quantitative observation must be linked to a source URL and reporting period. Where a value is not available or definitions are unclear, leave it blank and explain the limitation.

## 3. Core screening measures

- Revenue growth: current-period revenue / prior-period revenue - 1.
- EBITDA margin: EBITDA / revenue.
- EBIT margin: EBIT / revenue.
- Net leverage: use the issuer's disclosed net debt / EBITDA only where its definition is documented.
- Interest cover: EBIT / net finance costs, only where both inputs use compatible definitions.
- Cash conversion: operating cash flow / EBITDA, only where the cash flow definition and EBITDA basis are comparable.

These are screening ratios, not a formal rating methodology. Interpret them alongside business cyclicality, customer concentration, liquidity, debt maturity, security, covenants, foreign exchange and contingent liabilities.

## 4. PD, LGD and EAD boundaries

Public financial statements do not normally disclose the lender's borrower-level:
- Probability of default (PD) or internal risk grade;
- Loss given default (LGD) or collateral recovery assumptions;
- Exposure at default (EAD), including committed undrawn facilities;
- Origination-date credit risk and reporting-date SICR assessment.

Do not label a proxy as an actual bank PD, LGD, EAD or IFRS 9 stage. A future analytical model may develop an explicitly labelled proxy score, but it must be kept separate from reported data and supported by a documented calibration approach.

## 5. IFRS 9 boundary

IFRS 9 ECL is measured by a lender on its financial assets and commitments. A corporate issuer's own annual report may disclose ECL on its trade receivables, but that is not the same as the lender's ECL on loans to that company. This project will distinguish issuer-reported receivables impairment from hypothetical lender-side credit modelling.

## 6. Quality controls

- Preserve source units and reporting dates.
- Record whether each figure is statutory, underlying or company-adjusted.
- Recalculate ratios from disclosed inputs and retain formulas.
- Never convert missing disclosures to zero.
- Flag cross-company metric-definition differences.
- Update the source register when new annual or half-year reports are added.
