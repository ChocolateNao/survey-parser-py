import config


def to_fixed(number, digits=0) -> str:
    return f"{number:{config.DELIMETER}{digits}f}"
