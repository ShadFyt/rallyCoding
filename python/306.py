"""
You are given an array of integers and an integer K as arguments. Return the product of every integer in the array except for K.
K is guaranteed to always be present in the argument array

Requirements:
    -Must return an integer

"""
from typing import List


def solve(int_array: List[int], k: int) -> int:
    # first i reverse the order of the list
    int_array.reverse()
    # 2nd i check if k(element) is in the array and if it is then remove it from list
    if k in int_array:
        int_array.remove(k)
    num = 1
    # I loop through the reversed array and multiply num to each item in the array
    for number in int_array:
        num *= number
    return num


print(solve([1, 2, 3, 4, 5], 3))
