########################################################################
#    ____   ___    _
#   / ___| |_ _|  / \
#   \___ \  | |  / _ \
#    ___) | | | / ___ \
#   |____/ |___/_/   \_\
#
#   File:        parser.py
#   Author:      SIA
#   Description: <brief description of the file>
#   Created:     <date>
########################################################################

import pandas as pd
import pdfplumber
import re
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# ---------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------

# Path to your bank statement PDF
PDF_FILE = "bank_statement.pdf"

# Output Excel file
OUTPUT_FILE = "bank_transactions.xlsx"

# ---------------------------------------------------
# FUNCTION: Extract text from PDF
# ---------------------------------------------------

def extract_text_from_pdf(pdf_path):
    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

    # pdf to a text file
    with open("file.txt", "w", encoding="utf-8") as f:
        f.write(full_text)

    return full_text


# ---------------------------------------------------
# FUNCTION: Parse transactions
# ---------------------------------------------------

def parse_transactions(text):
    """
    Adjust the regex below depending on your bank format.

    Expected example format:
    US Bank:
    Jan 30 Electronic Deposit From Pizza Hut $ 400.00
    Feb 5 Ext Tfr Deposit TRN #= 3C56466A6839113 170.00-

    Chase Bank
    01/22 Dept Education Student Ln 6Rk0Avphcs1 Web ID: 099008
    -281.72 52.12
    01/30 Pizza Hut Dir Dep PPD ID: 98989 1,908.39 1,960.51
    """

    transactions = []

    # # Regex pattern: US Bank
    # # Month | Day | Description | amount and optional -
    # pattern = re.compile(
    #     r'(?P<month>[A-Za-z]{3})\s+'
    #     r'(?P<day>\d{1,2})\s+'
    #     r'(?P<description>.*)'
    #     r'\s+\$?\s*'
    #     r'(?P<amount>-?\d+\.\d{2}-?)'
    # )

    # Regex pattern: Chase Bank
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


# ---------------------------------------------------
# FUNCTION: Save to Excel
# ---------------------------------------------------

def save_to_excel(df, output_file):
    wb = Workbook()
    ws = wb.active
    ws.title = "Transactions"

    # Add dataframe rows
    for row in dataframe_to_rows(df, index=False, header=True):
        ws.append(row)

    # Auto-size columns
    for column_cells in ws.columns:
        length = max(len(str(cell.value)) if cell.value else 0 for cell in column_cells)
        ws.column_dimensions[column_cells[0].column_letter].width = length + 5

    wb.save(output_file)

# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

def main():

    print("Reading PDF statement...")

    text = extract_text_from_pdf(PDF_FILE)

    print("Parsing transactions...")

    df = parse_transactions(text)

    print (df)

    if df.empty:
        print("No transactions found.")
        return

    print(f"\nSaving to Excel: {OUTPUT_FILE}")

    save_to_excel(df, OUTPUT_FILE)

    print("Done!")


if __name__ == "__main__":
    main()