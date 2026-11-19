import csv
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class DebtCovenantAnalysisTests(unittest.TestCase):
    def test_disclosure_files_have_real_issuers_and_sources(self):
        for filename in ("debt_maturity_fy2026.csv", "covenant_disclosures_fy2026.csv"):
            with (ROOT / "data" / filename).open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertTrue(rows)
            self.assertTrue(all(row["company"] and row["asx_code"] for row in rows))
            self.assertTrue(all(row["source_url"].startswith("https://") for row in rows))

    def test_no_inferred_lindsay_covenant_headroom(self):
        with (ROOT / "data" / "covenant_disclosures_fy2026.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        lindsay = [row for row in rows if row["asx_code"] == "LAU"]
        self.assertEqual(len(lindsay), 3)
        self.assertTrue(all(row["headroom"] == "" for row in lindsay))
        self.assertTrue(all(row["compliance_status"] == "Compliant per company disclosure" for row in lindsay))

    def test_analysis_generates_outputs(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "src" / "debt_covenant_analysis.py")],
            cwd=ROOT, capture_output=True, text=True, check=True
        )
        self.assertIn("Processed", result.stdout)
        for filename in ("debt_maturity_summary.csv", "covenant_summary.csv"):
            self.assertTrue((ROOT / "outputs" / filename).exists())

if __name__ == "__main__":
    unittest.main()
