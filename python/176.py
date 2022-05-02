"""
You are given a lowercase string as an argument. 
Return true if each character in the string is shown an even number of times, false if not.

return: bool
"""
from collections import Counter
from typing import Dict


def solve(string: str) -> bool:
    counted = Counter(string)
    counted_str = counted.most_common()
    return all(letter[1] == 2 for letter in counted_str)


def solve_v2(str_arg: str) -> bool:
    letters_dict: Dict = {}
    for l in str_arg:
        if l in letters_dict:
            letters_dict[l] += 1
        else:
            letters_dict[l] = 1
    return all(letters_dict[l] == 2 for l in letters_dict)


print(solve_v2("aabbccdd"))
print(solve_v2("abcdeffgg"))
