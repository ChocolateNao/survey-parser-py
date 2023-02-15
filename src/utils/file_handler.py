import os.path
import openpyxl

import config


def ensure_file_sheet(directory: str, filename: str):
    try:
        if os.path.exists(directory):
            if os.path.isfile(os.path.join(directory, filename + '' if filename.endswith('.xlsx') else filename + '.xlsx')):
                print(f"File {config.SHEET_NAME_TARGET} exists! Let's roll!")
            else:
                # Create a new workbook
                workbook = openpyxl.Workbook()
                workbook.save(os.path.join(directory, filename + '' if filename.endswith('.xlsx') else filename + '.xlsx'))
                print("The specified file cannot be found so it was created.")
    except Exception as e:
        print("An error occurred:", e)
