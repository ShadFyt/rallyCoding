from collections import Counter


def solve(str_arg: str, k: int):
    counted_str = Counter(str_arg)
    return counted_str.most_common()[k - 1]


print(solve("aaabbc", 2))
print(solve("bbbbxyyzzz", 3))
