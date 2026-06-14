import re
import pandas as pd
from parsers.parser_bank import BankParser

class MarcusParser(BankParser):

    def parse_transactions(self, text):
        """
        Marcus Bank:
        04/10/2026 ACH Deposit pizza hut $150.00 $4,695.64
        04/15/2026 ACH Withdrawal stuff $620.00 $4,225.64
        """

        transactions = []

        # Month | Description | Amount | Balance
        pattern = re.compile(
            r'(?P<date>\d{2}/\d{2}/\d{4})\s+'
            r'(?P<description>.*?)\s+'
            r'(?P<amount>\$\d+(?:,\d{3})*\.\d{2})\s+'
            r'(?P<balance>\$\d+(?:,\d{3})*\.\d{2})'
        )

        matches = pattern.findall(text)

        for match in matches:
            transactions.append(match)

        return pd.DataFrame(transactions)
