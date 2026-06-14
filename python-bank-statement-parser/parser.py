########################################################################
#    ____   ___    _
#   / ___| |_ _|  / \
#   \___ \  | |  / _ \
#    ___) | | | / ___ \
#   |____/ |___/_/   \_\
#
#   File:        parser.py
#   Author:      SIA
#   Description: This file will read in data from a PDF
#                parse the data and export the data into
#                an excel file or a google sheet. This file
#                takes 2 inputs from the user (Bank and file type).
########################################################################

import pandas as pd
import pdfplumber
import re

# Excel
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Google Sheets
import gspread
from google.oauth2.service_account import Credentials

from enum import Enum

# ---------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------

# Path to your bank statement PDF
PDF_FILE = "bank_statement.pdf"

# Output Excel file
OUTPUT_FILE_EXCEL = "bank_transactions.xlsx"

# Output Google Sheets
OUTPUT_FILE_GOOGLE = "Bank Transactions"

# ---------------------------------------------------
# CLASS: Enum to hold user input for Bank
# ---------------------------------------------------
class Bank(Enum):
    US      = 1
    CHASE   = 2
    MARCUS  = 3

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

def parse_transactions(text, pattern_selection):
    """
    Adjust the regex below depending on your bank format.

    Expected example format:
    US Bank:
    Jan 30 Electronic Deposit From Pizza Hut $ 400.00
    Feb 5 Ext Tfr Deposit TRN #= 3C56466A6839113 170.00-

    Chase Bank:
    01/22 Dept Education Student Ln 6Rk0Avphcs1 Web ID: 099008
    -281.72 52.12
    01/30 Pizza Hut Dir Dep PPD ID: 98989 1,908.39 1,960.51

    Marcus Bank:
    04/10/2026 ACH Deposit pizza hut $150.00 $4,695.64
    04/15/2026 ACH Withdrawal stuff $620.00 $4,225.64

    """

    transactions = []

    match pattern_selection:
        case 1: # Regex pattern: US Bank
            # Month | Day | Description | amount and optional -
            pattern = re.compile(
                r'(?P<month>[A-Za-z]{3})\s+'
                r'(?P<day>\d{1,2})\s+'
                r'(?P<description>.*)'
                r'\s+\$?\s*'
                r'(?P<amount>-?\d+\.\d{2}-?)'
            )
        case 2: # Regex pattern: Chase Bank
            # Month | Description | Amount | Balance
            pattern = re.compile(
                r'(?P<date>\d{2}/\d{2})\s+'
                r'(?P<description>.*?)\s+'
                r'(?P<amount>-?\d+(?:,\d{3})*\.\d{2})\s+'
                r'(?P<balance>\d+(?:,\d{3})*\.\d{2})'
            )
        case 3: # Regex pattern: Marcus Bank
            # Month | Description | Credits/Debts | Balance
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
# FUNCTION: Save to Google Sheets
# ---------------------------------------------------

def save_to_google_sheet(df, sheet_name):

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=scopes
    )

    client = gspread.authorize(creds)

    sheet = client.open(sheet_name)

    worksheet = sheet.sheet1

    worksheet.clear()

    data = [df.columns.tolist()] + df.values.tolist()

    worksheet.update(data)

    print(f"Data written to Google Sheet: {sheet_name}")

# ---------------------------------------------------
# FUNCTION: Select Bank
# ---------------------------------------------------
def select_bank(bank_selection):
    # Match the day to predefined patterns
    match bank_selection:
        case 1: # US Bank
            print("Bank Selected: ", Bank.US.name)
            # New Line
            print()
        case 2: # Chase Bank
            print("Bank Selected: ", Bank.CHASE.name)
            # New Line
            print()
        case 3: # Marcus Bank
            print("Bank Selected: ", Bank.MARCUS.name)
            # New Line
            print()
        case _: # Defatult
            print("That's not a valid bank Selection")

# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

def main():

    # Capture text from the user
    print("What type of file you like")
    # New Line
    print()

    print("Excel ............ 1")
    print("Google Sheet ..... 2")

    # New Line
    print()
    filetype_selection = int(input("Enter file type: "))

    # Capture text from the user
    print("Please Enter the number that corresponds to the bank statement")
    # New Line
    print()

    print("US Bank ........ 1")
    print("Chase Bank ..... 2")
    print("Marcus Bank .... 3")

    # New Line
    print()

    bank_selection = int(input("Enter bank selection: "))
    select_bank(bank_selection)

    print("Reading PDF statement...")

    text = extract_text_from_pdf(PDF_FILE)

    print("Parsing transactions...")

    df = parse_transactions(text, bank_selection)

    print (df)

    if df.empty:
        print("No transactions found.")
        return

    if filetype_selection:

        print(f"\nSaving to Excel: {OUTPUT_FILE_EXCEL}")

        save_to_excel(df, OUTPUT_FILE_EXCEL)
    else:

        print("\nSaving to Google Sheets...")

        save_to_google_sheet(
        df,
        OUTPUT_FILE_GOOGLE)

    print("Done!")


if __name__ == "__main__":
    main()