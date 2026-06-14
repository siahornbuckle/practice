# Excel
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows


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