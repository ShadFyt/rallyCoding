"""
Find the sum of two integers represented as strings.
For example, given the string "123" and the string "111", your code should return the string "234".
"""


def solve(str_one, str_two):
    # convert str type into int add both then convert back to str type
    return str(int(str_one) + int(str_two))


print(type(solve("10", "20")))
