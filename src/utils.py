import os.path
from src.constants import *
from src.regex import *


def ensure_file_sheet(directory: str, filename: str):
    try:
        if os.path.exists(directory):
            if os.path.isfile(os.path.join(directory, filename + '' if filename.endswith('.xlsx') else filename + '.xlsx')):
                print("File exists! Let's roll!")
            else:
                # Create a new workbook
                workbook = openpyxl.Workbook()
                workbook.save(os.path.join(directory, filename + '' if filename.endswith('.xlsx') else filename + '.xlsx'))
                print("The specified file cannot be found so it was created.")
    except Exception as e:
        print("An error occurred:", e)


# def load_sheets():
def get_raw_sheet_data():
    for col in range(max_column_init_sheet):
        if col >= 1:
            cell_obj = init_sheet_obj.cell(row=1, column=col)
            regex_match = regex_brackets(cell_obj.value)
            if len(regex_match) != 0:
                print(regex_match[0])
                print(col)
