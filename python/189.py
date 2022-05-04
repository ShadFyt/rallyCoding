def solve(int_arr):
    # convert numbers into type str and split into a list
    new_list = list(str(int_arr))
    print(new_list)
    # convert type str back into int and sum list of numbers
    return sum(int(num) for num in new_list)


print(solve(6368206))
