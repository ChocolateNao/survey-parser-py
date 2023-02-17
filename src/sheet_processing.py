import re
from typing import Any

from utils.constants import init_sheet_max_column, load_init_sheet_by_id
from utils.regex import regex_braces_find, regex_name_find, regex_braces_remove


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


def get_subjects(counter=False) -> int | list[str]:
    """
    :param counter: If true, instead, returns subjects count (int)
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

    if counter:
        return subjects_counter

    return subjects_result


def get_teachers(counter=False) -> int | list[Any]:
    """
    :param counter: If true, instead, returns teachers count (int)
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
    for teacher in regex_match:
        teacher_str = teacher[0]
        regex_braces_remove(teacher_str)
        teachers_result.append(teacher_str)

    if counter:
        return teachers_counter

    return teachers_result


def get_dictionary_by_subject(header_data: list[list], subjects: list) -> dict:
    """
    :param subjects: A list of subjects
    :param header_data: A list[list] of [[data, column_index], [data, column_index]...]
    :return: A dictionary {subject: [data, column_index], [data, column_index]....}
    """
    questions = {subject: [] for subject in subjects}

    for item in header_data:
        match = re.search(r'\((.*?)\)', item[0])
        if match:
            subject = match.group(1)
            if subject in subjects:
                questions[subject].append(item)

    return questions


def get_dictionary_by_teacher(header_data: list[list], teachers: list) -> dict:
    """
    :param teachers: A list of teachers
    :param header_data: A list[list] of [[data, column_index], [data, column_index]...]
    :return: A dictionary {teacher}: [data, column_index], [data, column_index]....}
    """
    questions = {teacher: [] for teacher in teachers}

    for item in header_data:
        match = re.search(r'[А-Я][а-я]{1,30}\s[А-Я]\.[А-Я]\.', item[0])
        if match:
            teacher = match.group(0)
            if teacher in teachers:
                questions[teacher].append(item)

    return questions


def get_subject_feedback(subject: str) -> list[list]:
    """
    :param subject: The SINGLE name of a subject, could be an item from get_subjects()
    :return: A list[list] of question associated with the subject and their column indexes in the table
    [[column_name, column_index], [column_name, column_index]...]
    """
    header_data = get_header_data()
    questions = []
    for question in header_data:
        if subject in question[0]:
            questions.append(question)

    return questions


def get_subject_list(last=False) -> list:
    questions = []
    header_data = get_header_data()
    subjects_name = get_subjects()
    for header_item in header_data:
        for subject in subjects_name:
            if subject in header_item:
                if header_item not in questions:
                    questions.append(header_item)
    questions_len = len(questions)
    last_col = questions[questions_len - 1][1]
    if last:
        return questions

    questions = []

    for item in header_data:
        if last_col >= item[1] >= 4:
            questions.append(item)

    return questions


def get_subjects_dict() -> dict:
    data = get_subject_list(last=False)
    subjects = get_subjects()

    questions = {subject: [] for subject in subjects}
    for item in data:
        if '[' in item[0]:
            subject = item[0].split('[')[-1].strip(']')
        else:
            subject = item[0]
        if questions[subject] is not None:
            questions[subject].append(item)
        else:
            questions[subject] = item

    return questions
