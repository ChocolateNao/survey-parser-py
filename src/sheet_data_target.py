import os

import openpyxl

import config
from sheet_processing import get_teacher_questions, get_subjects, get_teachers


def load_teacher_data():
    subjects = get_subjects()
    teachers = get_teachers()
    teacher_questions = get_teacher_questions(teachers[1])
    print(teacher_questions)

    workbook_path = os.path.join(config.WORKBOOK_DIR, config.WORKBOOK_NAME_INIT)
    workbook = openpyxl.load_workbook(workbook_path)
    # выбрать индекс из всей таблицы, потом выбрать строки по этому индексу, если это числа - высчитать среднее
    for feedback in teacher_questions:
        cell_obj = init_sheet_obj.cell(row=1, column=col)


