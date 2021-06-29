import math


def add(a, b) -> int:
    return math.floor(a + b)


def to_sentence(s) -> str:
    s = s.capitalize()

    if to_sentence("."):
        return s
    else:
        return s + "."
