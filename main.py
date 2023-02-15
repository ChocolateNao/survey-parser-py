import config
from sheet_processing import get_header_data, get_header_data_raw, get_subjects, get_teachers
from src.utils.constants import init_sheet_max_row, init_sheet_max_column
from src.utils.regex import *
from src.utils import *
from src.sheet_template_target import *
from utils.file_handler import ensure_file_sheet

if __name__ == "__main__":

    ensure_file_sheet(config.SHEET_DIR, config.SHEET_NAME_TARGET)

    # get_header_data_raw()
    print(get_subjects())
    print(get_teachers())
    print("Total Rows:", init_sheet_max_row(0))
    print("Total Columns:", init_sheet_max_column(0))
