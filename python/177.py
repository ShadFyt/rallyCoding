import re
from typing import List


def solve(str_arg: str) -> List:
    list_of_words = re.split("\W", str_arg)
    return [word for word in list_of_words if word.isalpha()]


print(solve("Hi, how are you; I was quite curious!"))
