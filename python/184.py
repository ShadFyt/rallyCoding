def solve(str_arr):
    # sort each word in the list
    sorted_list = ["".join(sorted(word.lower())) for word in str_arr]
    # compare each word in the list and return True if same else return False
    return all(sorted_list[0] == word for word in sorted_list)


print(solve(["act", "cat", "tac"]))
print(solve(["act", "cat", "garden"]))
print(solve(["UPPERCASE", "praepuces"]))
