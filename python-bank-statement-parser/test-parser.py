########################################################################
#    ____   ___    _
#   / ___| |_ _|  / \
#   \___ \  | |  / _ \
#    ___) | | | / ___ \
#   |____/ |___/_/   \_\
#
#   File:        test-parser.py
#   Author:      SIA
#   Description: <brief description of the file>
#   Created:     <date>
########################################################################

import unittest
import pandas as pd
from parser import parse_transactions


class TestParser(unittest.TestCase):

    def test_single_transaction(self):
        text = "01/15/2026 AMAZON PURCHASE -45.67"

        df = parse_transactions(text)

        self.assertEqual(len(df), 1)

        self.assertEqual(df.iloc[0]["Date"], "01/15/2026")
        self.assertEqual(df.iloc[0]["Description"], "AMAZON PURCHASE")
        self.assertEqual(df.iloc[0]["Amount"], -45.67)

    def test_multiple_transactions(self):
        text = """
        01/15/2026 AMAZON PURCHASE -45.67
        01/16/2026 STARBUCKS -8.99
        01/17/2026 PAYROLL DEPOSIT 1500.00
        """

        df = parse_transactions(text)

        self.assertEqual(len(df), 3)

        self.assertEqual(df.iloc[1]["Description"], "STARBUCKS")
        self.assertEqual(df.iloc[2]["Amount"], 1500.00)

    def test_empty_input(self):
        text = ""

        df = parse_transactions(text)

        self.assertTrue(df.empty)

    def test_invalid_format(self):
        text = """
        RANDOM TEXT
        THIS IS NOT A TRANSACTION
        """

        df = parse_transactions(text)

        self.assertTrue(df.empty)

    def test_dollar_sign_amount(self):
        text = "01/18/2026 TARGET PURCHASE $89.22"

        df = parse_transactions(text)

        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["Amount"], 89.22)

    def test_negative_amount(self):
        text = "01/19/2026 ATM WITHDRAWAL -200.00"

        df = parse_transactions(text)

        self.assertEqual(df.iloc[0]["Amount"], -200.00)


if __name__ == "__main__":
    unittest.main()