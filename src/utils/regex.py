import re


def regex_braces_find(input_text):
    pattern = re.compile(r"\[[^\]]*]", re.IGNORECASE)
    return pattern.findall(input_text)


def regex_name_find(input_text):
    pattern = re.compile(r"[А-Я][а-я]{1,20}\s[А-Я]\.[А-Я]\.", re.IGNORECASE)
    return pattern.findall(input_text)

