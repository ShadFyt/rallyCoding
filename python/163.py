"""
You are given two arrays of integers as arguments. Return true if they contain the exact same elements in any order.
"""

from typing import List


def solve(arr_one: List, arr_two: List):
    # sort the two list then compare
    return sorted(arr_one) == sorted(arr_two)


print(solve([1, 2, 7], [7, 1, 2]))
print(solve([5, 7], [7, 1]))
