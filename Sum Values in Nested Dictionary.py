def sum_nested(d):
    total = 0
    for value in d.values():
        if isinstance(value, dict):
            total += sum_nested(value)
        elif isinstance(value, int):
            total += value
    return total
nested = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
print(sum_nested(nested))  # 6
