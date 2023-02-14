import pygsheets
import openpyxl

import config
from src.constants import *
from src.regex import *
from src.utils import *
from src.sheet_template import *

# gc = pygsheets.authorize(service_file='./python-itmo-gsheets-10befb7519fa.json')
#
#
# gc.open_by_url("https://docs.google.com/spreadsheets/d/1NmI37ZWsFR9wj9Jg3OvI79rYpHTpqswLML9Hr8N5-nc")
#
# wks = gc.sheet1
# print(wks)






# print("Total Rows:", max_row)
# print("Total Columns:", max_column)

if __name__ == "__main__":
    ensure_file_sheet(config.sheet_dir, config.sheet_target_name)
    get_raw_sheet_data()
