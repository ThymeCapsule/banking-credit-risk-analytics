# Synthetic loan portfolio — data dictionary

## Scope

The CSV contains 1,000 fictional Australian business lending facilities. Monetary values are AUD. Rates and probabilities are decimals (for example, 0.025 means 2.5%). The dataset is deterministic and can be regenerated with `python src/generate_portfolio.py`.

| Field | Definition |
|---|---|
| facility_id | Unique facility identifier |
| customer_id | Synthetic borrower identifier; a borrower may have multiple facilities |
| sector | Borrower's illustrative industry sector |
| business_size | SME or Mid-market classification |
| product_type | Term Loan, Business Overdraft or Commercial Property Loan |
| origination_date | Illustrative facility origination date |
| maturity_months | Remaining contractual maturity in months at the reporting date |
| drawn_balance_aud | Amount currently drawn |
| undrawn_commitment_aud | Available undrawn commitment |
| credit_conversion_factor | Illustrative factor applied to undrawn commitments when estimating EAD |
| original_pd_12m | Illustrative 12-month PD at origination |
| current_pd_12m | Illustrative current 12-month PD |
| original_lifetime_pd | Illustrative cumulative lifetime PD at origination |
| current_lifetime_pd | Illustrative current cumulative lifetime PD |
| lgd | Illustrative loss-given-default assumption |
| days_past_due | Number of days contractually past due |
| default_flag | 1 indicates an illustrative default event; otherwise 0 |
| collateral_value_aud | Illustrative current collateral value |
| effective_interest_rate | Illustrative annual effective interest rate |
| risk_grade | Internal illustrative grade from 1 (lower risk) to 10 (higher risk) |

## Data-generation controls

- Fixed pseudo-random seed for reproducibility.
- Facility balances and commitments are non-negative.
- Credit conversion factors, PDs, LGDs and interest rates are bounded between 0 and 1.
- The default flag and days-past-due field are separate indicators; neither should be treated as a complete default definition without an explicit modelling policy.
- Risk grades and PDs are illustrative and are not empirically calibrated.

## Modelling cautions

- Do not interpret this synthetic portfolio as representative of any actual bank's portfolio.
- Do not infer IFRS 9 stages from the risk grade alone.
- A future ECL model should document SICR criteria, default definition, PD term structures, forward-looking scenarios, scenario weights, discounting, cure assumptions and write-off treatment.
- EAD should distinguish drawn exposure from expected utilisation of undrawn commitments; the supplied conversion factor is an illustrative input.
