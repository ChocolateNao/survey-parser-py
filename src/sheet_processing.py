from utils.constants import init_sheet_max_column, load_init_sheet_by_id
from utils.regex import regex_brackets, regex_teacher_name


def get_header_data():
    """
    Returns two-dimensional list [[column_name, column_index], [column_name, column_index]...]
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
    Printing raw strings of header names directly into the terminal
    """
    max_column_init_sheet = init_sheet_max_column(0)
    init_sheet_obj = load_init_sheet_by_id(0)

    for col in range(max_column_init_sheet):
        if col >= 1:
            cell_obj = init_sheet_obj.cell(row=1, column=col)
            print(cell_obj.value)
            print(col)


def get_subjects():
    """
    Returns an array of subjects
    """
    header_data = get_header_data()
    regex_match = []
    for header in header_data:
        regex_row = regex_brackets(header[0])
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
    print(f"Found {subjects_counter} subjects")
    return subjects


def get_teachers():
    """
    Returns an array of teachers
    """
    header_data = get_header_data()
    regex_match = []
    teachers_counter = 0
    for header in header_data:
        regex_row = regex_teacher_name(header[0])
        if len(regex_row) != 0 and regex_row not in regex_match:
            regex_match.append(regex_row)
            teachers_counter += 1
    print(f"Found {teachers_counter} teachers")
    return regex_match


def get_questions():
    pass
