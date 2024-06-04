def product_of_list(lst):
    if len(lst) == 0:
        return 1
    return lst[0] * product_of_list(lst[1:])

print(product_of_list([1, 2, 3, 4]))  # Output: 24
