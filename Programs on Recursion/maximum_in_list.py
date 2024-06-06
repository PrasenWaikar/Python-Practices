def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], find_max(lst[1:]))

print(find_max([1, 5, 3, 9, 2]))  # Output: 9
