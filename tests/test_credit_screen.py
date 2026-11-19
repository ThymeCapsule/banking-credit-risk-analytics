import unittest

from src.credit_screen import ratio, fmt


class CreditScreenTests(unittest.TestCase):
    def test_ratio(self):
        self.assertAlmostEqual(ratio(100, 50), 2.0)

    def test_ratio_handles_missing_denominator(self):
        self.assertIsNone(ratio(100, None))
        self.assertIsNone(ratio(100, 0))

    def test_format_preserves_missing_values(self):
        self.assertEqual(fmt(None), "")
        self.assertEqual(fmt(1.23456, 2), "1.23")

    def test_downside_sensitivity_arithmetic(self):
        base_leverage = 1.5
        base_cover = 13.5
        ebitda_shock = 0.20
        finance_cost_shock = 0.20
        stressed_leverage = base_leverage / (1 - ebitda_shock)
        stressed_cover = base_cover * (1 - ebitda_shock) / (1 + finance_cost_shock)
        self.assertAlmostEqual(stressed_leverage, 1.875)
        self.assertAlmostEqual(stressed_cover, 9.0)


if __name__ == "__main__":
    unittest.main()
