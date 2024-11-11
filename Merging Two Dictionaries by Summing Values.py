dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 3, 'c': 4}
merged_dict = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}
print(merged_dict)  # {'a': 4, 'b': 2, 'c': 4}
