"""
You are given an integer N as an argument. 
Return a two dimensional array containing arrays of integers that make up a multiplication table from 1x1 to NxN.

Requirements: Must return a two dimensional array containing arrays of integers
"""
from typing import List


def solve(n: int) -> List:
    # nested for loop
    return [[(num + 1) * (x + 1) for x in range(n)] for num in range(n)]
