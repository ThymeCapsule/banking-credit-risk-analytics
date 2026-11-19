# Business Banking Credit Risk & IFRS 9 Analytics

A reproducible, synthetic business-banking loan portfolio designed as the foundation for a credit-risk and IFRS 9 expected credit loss (ECL) analytics project.

## Project status

**Stage 1 — Portfolio dataset:** complete.

This repository currently contains a 1,000-facility synthetic Australian business lending portfolio and the script used to regenerate it. Subsequent stages will add staging, PD/LGD/EAD calculations, ECL measurement, portfolio reporting, SQL analysis and automated tests.

## Portfolio coverage

- 1,000 fictional lending facilities across Australian business sectors
- SME and mid-market borrowers
- Term loans, revolving business facilities and commercial property loans
- Drawn balances and undrawn commitments
- Origination and current probability-of-default measures
- Lifetime PD indicators, loss-given-default assumptions and collateral values
- Days past due, default flags, maturity and effective interest rates

All amounts are in Australian dollars (AUD). The dataset is entirely synthetic; it contains no customer, bank or commercially confidential information.

## Repository structure

```text
.
├── data/
│   └── synthetic_loan_portfolio.csv
├── docs/
│   └── data_dictionary.md
├── src/
│   └── generate_portfolio.py
└── README.md
```

## Reproduce the dataset

Requires Python 3.9+ and uses only the Python standard library.

```bash
python src/generate_portfolio.py
```

The script writes `data/synthetic_loan_portfolio.csv` using a fixed seed, so the output is reproducible.

## Methodology and limitations

The portfolio is a controlled demonstration dataset, not a statistical sample of the Australian lending market. PD, LGD, credit grades, collateral and facility characteristics are illustrative assumptions. They are not calibrated to a financial institution's observed defaults, recovery experience or regulatory models.

The presence of input risk indicators does not itself constitute an IFRS 9 staging or ECL calculation. Those calculations will be implemented and documented in later project stages. This project is educational and analytical; it is not an approved accounting, regulatory capital or credit decisioning model.

See [the data dictionary](docs/data_dictionary.md) for field definitions.
