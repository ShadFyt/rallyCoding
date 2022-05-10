from typing import List


def solve(str_arr):
    words = str_arr.split()

    print(("".join(list(reversed(words[0])))))


print(solve("How are you?"))
