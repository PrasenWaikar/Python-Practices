dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'b': 200, 'd': 400}

common_keys = dict1.keys() & dict2.keys()
print(common_keys)
