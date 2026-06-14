########################################################################
#    ____   ___    _
#   / ___| |_ _|  / \
#   \___ \  | |  / _ \
#    ___) | | | / ___ \
#   |____/ |___/_/   \_\
#
#   File:        output_google_sheet.py
#   Author:      SIA
#   Description: out put data in Google sheets
########################################################################

# Google Sheets
import gspread
from google.oauth2.service_account import Credentials

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