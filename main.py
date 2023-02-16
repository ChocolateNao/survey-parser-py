import config
from sheet_data_target import load_teacher_data
from sheet_processing import get_header_data, get_header_data_raw, get_subjects, get_teachers, \
    get_teacher_questions, get_subject_questions
from src.utils.constants import init_sheet_max_row, init_sheet_max_column, target_sheet_max_column, target_sheet_max_row
from src.utils.regex import *
from src.utils import *
from src.sheet_template_target import *
from utils.file_handler import ensure_file_workbook

if __name__ == "__main__":
    # # ENSURE FILE
    ensure_file_workbook(config.WORKBOOK_DIR, config.WORKBOOK_NAME_TARGET)

    # # READ FROM INIT
    # subjects = get_subjects()
    # teachers = get_teachers()
    # print(subjects)
    # print(teachers)
    # teacher_questions = get_teacher_questions(teachers[1])

    # # COMPOSE TARGET HEADER
    compose_target_teachers_header()
    compose_target_subjects_header()

    # # FILL IN THE DATA

    # # SAVE


    # get_header_data_raw()


    # teachers_data = get_teachers()
    # for teachers_name in teachers_data:
    #     print(get_teacher_questions(teachers_name[0]))


    # subject_questions = get_subject_questions(subjects[1])

    # teachers = get_teachers()
    # teacher_questions = get_teacher_questions(teachers[1])
    # for teacher in teachers:
    #     merge = merge_teacher(teacher)
    #     print(merge)

    # print(get_teachers_header(subject_questions))
    # print(teacher_questions)
    # print(get_teachers_header(teacher_questions))

    # print(get_subjects())
    # print(get_teachers())

    load_teacher_data()

    print("Total Rows Init:", init_sheet_max_row(0))
    print("Total Columns Init:", init_sheet_max_column(0))
    print("Total Rows Target SUBJECT:", target_sheet_max_row(0))
    print("Total Columns Target SUBJECT:", target_sheet_max_column(0))
    print("Total Rows Target TEACHER:", target_sheet_max_row(1))
    print("Total Columns Target TEACHER:", target_sheet_max_column(1))


