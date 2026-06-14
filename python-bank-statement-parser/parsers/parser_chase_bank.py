import re
import pandas as pd
from parsers.parser_bank import BankParser

class ChaseParser(BankParser):

    def parse_transactions(self, text):
        """
        Chase Bank:
        01/22 Dept Education Student Ln 6Rk0Avphcs1 Web ID: 099008
        -281.72 52.12
        01/30 Pizza Hut Dir Dep PPD ID: 98989 1,908.39 1,960.51
        """

        transactions = []

        # Month | Description | Amount | Balance
        pattern = re.compile(
            r'(?P<date>\d{2}/\d{2})\s+'
            r'(?P<description>.*?)\s+'
            r'(?P<amount>-?\d+(?:,\d{3})*\.\d{2})\s+'
            r'(?P<balance>\d+(?:,\d{3})*\.\d{2})'
        )

        matches = pattern.findall(text)

        for match in matches:
            transactions.append(match)

        return pd.DataFrame(transactions)
