def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items
nested_dict = {'a': {'b': 1, 'c': {'d': 2}}}
print(flatten_dict(nested_dict))  # {'a_b': 1, 'a_c_d': 2}
