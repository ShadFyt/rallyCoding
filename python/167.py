"""
You are given two sorted arrays of integers and an integer K as arguments. 
Find one integer from each array that sums up to the integer K and return the pair as an array of integers.
"""


def solve(array_one, array_two, k):
    num_list = []
    for num_one in array_one:
        for num_two in array_two:
            if num_one + num_two == k:
                num_list.extend((num_one, num_two))
    return num_list[:2]


print(solve([1, 2, 3], [4, 5, 6], 8))
print(solve([1, 2, 3], [4, 5, 6], 9))
