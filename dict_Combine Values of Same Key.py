list_of_dicts = [{'a': 10}, {'b': 20}, {'a': 30}]

combined_dict = {}
for d in list_of_dicts:
    for key, value in d.items():
        combined_dict[key] = combined_dict.get(key, 0) + value

print(combined_dict)
