import re

from utils.constants import init_sheet_max_column, load_init_sheet_by_id
from utils.regex import regex_braces_find, regex_name_find


def get_header_data() -> list[list]:
    """
    :return: Two-dimensional list [[column_name, column_index], [column_name, column_index]...]
    """
    header_data = []
    max_column_init_sheet = init_sheet_max_column(0)
    init_sheet_obj = load_init_sheet_by_id(0)

    for col in range(max_column_init_sheet):
        if col >= 1:
            header_item = []
            cell_obj = init_sheet_obj.cell(row=1, column=col)
            header_item.append(cell_obj.value)
            header_item.append(col)
            header_data.append(header_item)

    return header_data


def get_header_data_raw():
    """
    :return: Printing raw strings of header names directly into the terminal
    """
    max_column_init_sheet = init_sheet_max_column(0)
    init_sheet_obj = load_init_sheet_by_id(0)

    for col in range(max_column_init_sheet):
        if col >= 1:
            cell_obj = init_sheet_obj.cell(row=1, column=col)
            print(cell_obj.value)
            print(col)


def get_subjects() -> list:
    """
    :return: An array of subjects
    """
    header_data = get_header_data()
    regex_match = []
    for header in header_data:
        regex_row = regex_braces_find(header[0])
        if len(regex_row) != 0:
            regex_match.append(regex_row)

    subjects = []
    subjects_counter = 0
    for item in regex_match:
        if item not in subjects:
            subjects.append(item)
            subjects_counter += 1
        else:
            break
    # Removing braces
    subjects_result = []
    braces = r'[\[\]]'
    for subject in subjects:
        subject_str = subject[0]
        subject_str = re.sub(braces, '', subject_str)
        subjects_result.append(subject_str)

    print(f"Found {subjects_counter} subjects")
    return subjects_result


def get_teachers() -> list:
    """
    :return: An array of teachers
    """
    header_data = get_header_data()
    regex_match = []
    teachers_counter = 0
    for header in header_data:
        regex_row = regex_name_find(header[0])
        if len(regex_row) != 0 and regex_row not in regex_match:
            regex_match.append(regex_row)
            teachers_counter += 1

    teachers_result = []
    braces = r'[\[\]]'
    for teacher in regex_match:
        teacher_str = teacher[0]
        teacher_str = re.sub(braces, '', teacher_str)
        teachers_result.append(teacher_str)

    print(f"Found {teachers_counter} teachers")
    return teachers_result


def get_general_questions():
    pass


def get_teacher_questions(teacher: str) -> list[list]:
    """
    :param teacher: The SINGLE name of a teacher, could be an item from get_teachers()
    :return: A list[list] of question associated with the teacher and their indexes in the table
    [[column_name, column_index], [column_name, column_index]...]
    """
    header_data = get_header_data()
    questions = []
    for teacher_question in header_data:
        if teacher in teacher_question[0]:
            questions.append(teacher_question)

    return questions


def get_subject_questions(subject: str) -> list[list]:
    """
    :param subject: The SINGLE name of a subject, could be an item from get_subjects()
    :return: A list[list] of question associated with the subject and their indexes in the table
    [[column_name, column_index], [column_name, column_index]...]
    """
    header_data = get_header_data()
    questions = []
    for question in header_data:
        if subject in question[0]:  # Since two-dimensional array and we don't need index yet, but it'll be there
            questions.append(question)

    return questions


# def merge_teacher(teacher: str) -> list[list]:
#     """
#     :param teacher: The SINGLE name of a teacher, could be an item from get_teachers()
#     :return: A list[list] of question associated with the teacher and their indexes in the table
#     """
#     header_data = get_header_data()
#     merged = []
#     for item in header_data:
#         if teacher in item[0]:  # Since two-dimensional array and we don't need index yet, but it'll be there
#             merged.append(item)
#     return merged
