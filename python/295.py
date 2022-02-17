"""
    You are given a lowercase string as an argument. Return true if the string is a palindrome, false if it is not.
    Palindromes are strings that form the same word if it is reversed.

    Requirement:     
        -Must return true or false
        -Special characters should be considered part of the string
        -Must account for spaces
"""


def solve(str_arg: str) -> bool:
    # reversed() iterates the string and yields the characters in reverse order,
    # the yielded character then gets passed into .join() as an argument
    reversed_str = "".join(reversed(str_arg))
    print(reversed_str)
    return reversed_str == str_arg


print(solve("racecar!"))
print(solve("ab ba"))
print(solve("race car"))
