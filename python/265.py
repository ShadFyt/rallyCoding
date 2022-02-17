def solve(str_arg):
    for i in range(len(str_arg)):
        count = str_arg.count(str_arg[i])
        if count == 2:
            return True
    return False


print(solve("terrific"))
print(solve("cats"))
print(solve("cats!!"))
