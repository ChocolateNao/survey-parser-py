import re


def regex_braces_find(input_text: str):
    pattern = re.compile(r"\[[^\]]*]", re.IGNORECASE)
    return pattern.findall(input_text)


def regex_parenthesis_find(input_text: str):
    pattern = re.compile(r"\([^)]*\)", re.IGNORECASE)
    return pattern.findall(input_text)


def regex_name_find(input_text: str):
    pattern = re.compile(r"[А-Я][а-я]{1,30}\s[А-Я]\.[А-Я]\.", re.IGNORECASE)
    return pattern.findall(input_text)


def regex_braces_remove(input_text: str) -> str:
    braces = r'[\[\]]'
    return re.sub(braces, '', input_text)


def regex_parenthesis_remove(input_text: str) -> str:
    parenthesis = r'\([^)]*\)'
    return re.sub(parenthesis, '', input_text)


def regex_class_type_find(input_text: str):
    pattern = r",\s*([^()]*)\("
    match = re.search(pattern, input_text)
    if match:
        return match.group(1)
    else:
        return None
