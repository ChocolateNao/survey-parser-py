from sheet_data_target import write_teacher_data

from src.utils.constants import init_sheet_max_row, init_sheet_max_column, target_sheet_max_column, target_sheet_max_row
from src.sheet_template_target import *
from utils.file_handler import ensure_file_workbook

if __name__ == "__main__":
    # # ENSURE FILE
    ensure_file_workbook(config.WORKBOOK_DIR, config.WORKBOOK_NAME_TARGET)

    # # READ FROM INIT
    subjects_count = get_subjects(counter=True)
    print(f"Found {subjects_count} subjects")

    teachers_count = get_teachers(counter=True)
    print(f"Found {teachers_count} teachers")

    # # COMPOSE TARGET HEADER
    insert_target_teachers_header()
    # compose_target_subjects_header()

    # # FILL IN THE DATA
    write_teacher_data()
    # # SAVE

    print("Total Rows Init:", init_sheet_max_row(0))
    print("Total Columns Init:", init_sheet_max_column(0))
    print("Total Rows Target SUBJECT:", target_sheet_max_row(0))
    print("Total Columns Target SUBJECT:", target_sheet_max_column(0))
    print("Total Rows Target TEACHER:", target_sheet_max_row(1))
    print("Total Columns Target TEACHER:", target_sheet_max_column(1))


