from black import List


def solve(str_array: List[str]) -> List:
    str_array.reverse()
    print(str_array)


solve(["Cat", "Dog", "Skunk", "Bird"])
solve(["owl", "ferret", "Mouse!", "Eagle"])
