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


# import classes
from parsers.parser_us_bank             import UsParser
from parsers.parser_chase_bank          import ChaseParser
from parsers.parser_marcus_bank         import MarcusParser

# import functions
from bank_selection                     import select_bank
from pdf_reader                         import extract_text_from_pdf
from outputs.output_excel               import save_to_excel
from outputs.output_google_sheet        import save_to_google_sheet
from outputs.output_path_operations     import save_pdf_path


# ---------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------

# Path to your bank statement PDF
PDF_FILE = save_pdf_path()

# Output Excel file
OUTPUT_FILE_EXCEL = "bank_transactions.xlsx"

# Output Google Sheets
OUTPUT_FILE_GOOGLE = "Bank Transactions"


# ---------------------------------------------------
# FUNCTION: Parse transactions
# ---------------------------------------------------

def parse_transactions(text, pattern_selection):

    match pattern_selection:
        case 1:
            return UsParser.parse_transactions(self=UsParser,
                                                  text=text)
        case 2:
            return ChaseParser.parse_transactions(self=ChaseParser,
                                                  text=text)
        case 3:
            return MarcusParser.parse_transactions(self=MarcusParser,
                                                  text=text)


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

    if filetype_selection == 1:

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