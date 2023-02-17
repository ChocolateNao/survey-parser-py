import config


def to_fixed(number, digits=0) -> str:
    return f"{number:{config.DELIMETER}{digits}f}"


def replace_strings_with_zero(lst: list):
    return [0 if isinstance(elem, str) else elem for elem in lst]
