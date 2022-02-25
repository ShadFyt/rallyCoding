from typing import List


def solve(int_array: List[int], range) -> List[int]:
    return [num for num in int_array if num > range[0] and num < range[1]]


print(solve([1, 2, 3, 5, 6, 7], [2, 6]))
print(solve([1, 2, 3, 4, 5, 10, 20], [4, 7]))
