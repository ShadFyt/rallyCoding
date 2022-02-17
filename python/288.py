from typing import List


def solve(directions: List):
    cord = [0, 0]
    for m in directions:
        if m == "up":
            cord[1] += 1
        elif m == "down":
            cord[1] -= 1
        elif m == "right":
            cord[0] += 1
        else:
            cord[0] -= 1
    return cord


print(solve(["up", "up", "down", "left", "left", "right", "up"]))
