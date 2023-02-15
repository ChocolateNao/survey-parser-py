import openpyxl
# import dotenv
import config


def load_init_sheet_by_id(sheet_index: int):
    if sheet_index < 0:
        raise ValueError("Sheet ID can not be negative")
    init_wb_obj = openpyxl.load_workbook(config.SHEET_DIR + config.SHEET_NAME_INIT)
    init_wb_obj.active = sheet_index
    return init_wb_obj.active


def load_target_sheet_by_id(sheet_index: int):
    if sheet_index < 0:
        raise ValueError("Sheet ID can not be negative")
    target_wb_obj = openpyxl.load_workbook(config.SHEET_DIR + config.SHEET_NAME_TARGET)
    target_wb_obj.active = sheet_index
    return target_wb_obj.active


def init_sheet_max_row(sheet_index: int):
    if sheet_index < 0:
        raise ValueError("Sheet ID can not be negative")
    sheet = load_init_sheet_by_id(sheet_index)
    return sheet.max_row


def init_sheet_max_column(sheet_index: int):
    if sheet_index < 0:
        raise ValueError("Sheet ID can not be negative")
    sheet = load_init_sheet_by_id(sheet_index)
    return sheet.max_column


def target_sheet_max_row(sheet_index: int):
    if sheet_index < 0:
        raise ValueError("Sheet ID can not be negative")
    sheet = load_init_sheet_by_id(sheet_index)
    return sheet.max_row


def target_sheet_max_column(sheet_index: int):
    if sheet_index < 0:
        raise ValueError("Sheet ID can not be negative")
    sheet = load_target_sheet_by_id(sheet_index)
    return sheet.max_column



