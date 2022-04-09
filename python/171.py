from typing import List

"""
You are given two arrays of integers as arguments. 
Return an array of integers which represents the intersection - the common elements from the original two arrays.

Requirements: 
    -Must return an array of integers
    -The returned array must follow the same ordering as the first array.
    -Should work with both positive and negative integers
"""


def solve(arr_one: List, arr_two: List):
    # List comperhesion with an if statement
    return [num[1] for num in enumerate(arr_one) if num[1] in arr_two]


print(solve([1, 2, 3, 4, 5], [4, 2]))
