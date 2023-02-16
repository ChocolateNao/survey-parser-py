import os

import openpyxl

import config
from sheet_processing import get_teacher_questions, get_teachers
from utils.constants import sheet_teachers_header
from utils.regex import regex_braces_find, regex_remove_braces


def compose_target_subjects_header():
    workbook = openpyxl.load_workbook(os.path.join(config.WORKBOOK_DIR, config.WORKBOOK_NAME_TARGET))
    worksheet = workbook.active
    pass


# Факультет
# Курс
# Группа
# ФИО преподавателя
# Дисциплина
# Количество ответов
# Удовлетворены ли Вы реализацией дисциплины? (0 - полностью НЕ удовлетворен, 1-скорее не удовлетворен, 2-скорее удовлетворен, 3-полностью удовлетворен)
# Были ли  вы проинформированы о целях курса, его  месте в образовательной программе и о критериях оценивания?
#     да, в начале семестра
#     да, перед промежуточной аттестацией
#     нет
# Оцените сложность курса (1 - очень легко, 5 - очень сложно)
# Оцените сложность домашних заданий (1 - очень простые, 5 - очень сложные)
# Сколько часов в неделю (кроме аудиторных) Вы тратите на курс?
#     0 - 2
#     2 - 4
#     4 - 6
#     6 - 8 > 10
# Открытые комментарии


def get_teachers_header(questions_list: list) -> list:
    header_items = []
    init_header = questions_list
    for item in init_header:
        item = regex_braces_find(item[0])
        if len(item) != 0:
            item = regex_remove_braces(item[0])
            header_items.append(item)

    return header_items


# def get_subjects_header(questions_list: list) -> list:
#     header_items = []
#
#     return header_items


def compose_target_teachers_header():
    try:
        workbook_path = os.path.join(config.WORKBOOK_DIR, config.WORKBOOK_NAME_TARGET)
        workbook = openpyxl.load_workbook(workbook_path)
        worksheet_teachers = workbook[config.TARGET_SHEET_TEACHERS_NAME]

        teachers = get_teachers()
        teacher_questions = get_teacher_questions(teachers[1])

        header = get_teachers_header(teacher_questions)
        header = sheet_teachers_header + header + ['Комментарии']

        for i, col_name in enumerate(header, start=1):
            cell = worksheet_teachers.cell(row=1, column=i)
            cell.value = col_name
            cell.font = openpyxl.styles.Font(bold=True)
            cell.alignment = openpyxl.styles.Alignment(horizontal='center')

        workbook.save(os.path.join(workbook_path))
    except PermissionError as e:
        print(f"Permission error while working with '{workbook_path}'! The workbook may be opened in another editor\n{e}")

# Факультет
# Курс
# Группа
# ФИО преподавателя
# Дисциплина
# Тип
# Количество ответов
# Общая удовлетворенность преподаванием (0 - полностью НЕ удовлетворен, 1 - скорее не удовлетворен, 2 - скорее удовлетворен, 3 - полностью удовлетворен)
# Уровень владения преподаваемым материалом
# Планирование и организация дисциплины
# Коммуникация (доступность преподавателя лично и по почте)
# Четкость и структурированность изложения материала
# Вовлечение студентов в изучение дисциплины
# Комфортная атмосфера на занятиях
# Использование цифровых инструментов преподавателем
# Открытые комментарии
