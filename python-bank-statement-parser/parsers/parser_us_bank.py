import re
import pandas as pd
from parsers.parser_bank import BankParser

class UsParser(BankParser):

    def parse_transactions(self, text):
        """
        US Bank:
        Jan 30 Electronic Deposit From Pizza Hut $ 400.00
        Feb 5 Ext Tfr Deposit TRN #= 3C56466A6839113 170.00-
        """
        transactions = []

        # Month | Description | Amount | Balance
        pattern = re.compile(
            r'(?P<month>[A-Za-z]{3})\s+'
            r'(?P<day>\d{1,2})\s+'
            r'(?P<description>.*)'
            r'\s+\$?\s*'
            r'(?P<amount>-?\d+\.\d{2}-?)'
        )

        matches = pattern.findall(text)

        for match in matches:
            transactions.append(match)

        return pd.DataFrame(transactions)
