# Source register

## SGH Limited (ASX: SGH)

- FY26 investor presentation, 11 August 2026.
- Revenue A$10,564m; EBITDA A$2,084m; EBIT A$1,554m; statutory NPAT A$655m; underlying operating cash flow A$2,072m; adjusted net debt/EBITDA 1.8x.
- FY26 annual report: drawn facility weighted-average maturity 4.6 years; undrawn committed facilities A$1,225m; additional liquidity A$359.7m; contractual principal maturity buckets are recorded in the maturity CSV.
- No financial covenant thresholds or covenant calculations were identified in the reviewed annual-report disclosure.
- Sources:
  - https://announcements.asx.com.au/asxpdf/20260811/pdf/072m7t1wrttdft.pdf
  - https://financialfilings.com/filings/sgh-limited/annual-report/2026/55622911/
- The presentation separately shows NPAT A$920m; the dataset uses statutory NPAT A$655m.

## ALS Limited (ASX: ALQ)

- FY26 annual report for year ended 31 March 2026.
- Revenue A$3,320.1m; statutory EBITDA A$778.3m; EBIT A$524.9m; statutory NPAT A$318.7m; net debt A$1,069.5m; loans and borrowings A$1,219.2m; cash A$149.7m; lease liabilities A$352.7m; net operating cash flow A$485.7m.
- Company-reported leverage 1.5x using adjusted underlying EBITDA A$730.8m on a pre-IFRS16 basis; company-reported interest cover 13.5x using adjusted underlying EBITDA and net finance expense on loans and borrowings.
- Disclosed covenant thresholds: interest cover greater than 3.75x and financial leverage below 3.25x. Simple arithmetic headroom versus reported FY26 ratios is 9.75x and 1.75x respectively.
- Contractual maturity schedule separates long-term notes, bank loans and lease liabilities. Weighted-average debt maturity was 3.9 years at 31 March 2026; pro forma 4.0 years after the 8 May 2026 refinancing.
- Sources:
  - https://www.alsglobal.com/en-in/news-and-publications/2026/05/als-limited-delivers-record-fy26-result
  - https://financialfilings.com/filings/als-limited/annual-report/2026/48507202/

## Lindsay Australia Limited (ASX: LAU)

- FY26 annual report for year ended 30 June 2026.
- Operating revenue A$1,072.695m; statutory EBITDA A$123.908m; EBIT A$54.462m; NPAT A$22.872m; net finance costs A$20.905m (net of bank interest received); operating cash flow A$75.213m.
- Borrowings A$135.562m; cash A$57.754m; lease liabilities A$238.409m.
- Company-reported net leverage 1.92x. Analyst calculation EBITDA / segment net finance costs = 5.93x; this is not the company's covenant interest-cover ratio.
- Disclosed covenants: gross leverage below 3.50x; interest cover above 2.50x; debt service cover above 1.20x. Company states it complied throughout FY26, but actual covenant calculation values are not disclosed in the reviewed note.
- Contractual maturity schedule is recorded separately for bank loans, equipment finance, equipment loans and property/other lease liabilities.
- Source: https://financialfilings.com/filings/lindsay-australia-limited/annual-report/2026/57389127/

## Structured data files

- `data/asx_issuer_financials_fy2026.csv`: issuer financials and source notes.
- `data/debt_maturity_fy2026.csv`: disclosed contractual cash flow maturity buckets.
- `data/covenant_disclosures_fy2026.csv`: covenant thresholds, reported ratios, calculated headroom where comparable, and disclosure limitations.
