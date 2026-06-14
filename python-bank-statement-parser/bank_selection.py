########################################################################
#    ____   ___    _
#   / ___| |_ _|  / \
#   \___ \  | |  / _ \
#    ___) | | | / ___ \
#   |____/ |___/_/   \_\
#
#   File:        bank_selection.py
#   Author:      SIA
#   Description: code to select which bank type
########################################################################


from enum import Enum

# ---------------------------------------------------
# CLASS: Enum to hold user input for Bank
# ---------------------------------------------------
class Bank(Enum):
    US      = 1
    CHASE   = 2
    MARCUS  = 3

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