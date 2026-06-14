########################################################################
#    ____   ___    _
#   / ___| |_ _|  / \
#   \___ \  | |  / _ \
#    ___) | | | / ___ \
#   |____/ |___/_/   \_\
#
#   File:        pdf_reader.py
#   Author:      SIA
#   Description: code to read .pdf file
########################################################################

import pdfplumber

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