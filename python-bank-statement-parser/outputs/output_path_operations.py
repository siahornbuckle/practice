########################################################################
#    ____   ___    _
#   / ___| |_ _|  / \
#   \___ \  | |  / _ \
#    ___) | | | / ___ \
#   |____/ |___/_/   \_\
#
#   File:        output_path_operations.py
#   Author:      SIA
#   Description: update..
########################################################################

from pathlib import Path
import os

def save_pdf_path():
    # things I know I need update later
    count = 0
    statement_str = "/Statements"
    # Get the current working directory as an object
    base_cwd = str(Path.cwd())
    Statements_cwd = base_cwd + statement_str

    # Specify the directory path
    directory = Path(Statements_cwd)

    # Loop through all items in the directory
    for item in directory.iterdir():
        # Filter out subdirectories
        if item.is_file():
            file_path = Path(item)
            # Look for .pdf files in directory
            if file_path.suffix == ".pdf":
                count +=1
                # Save string of file name
                PDF_FILE = str(item)



    # print("DEBUG count:", count)

    return PDF_FILE

