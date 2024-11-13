data = {'a': {'b': {'c': 1}}}
def get_nested_value(d, keys, default=None):
    for key in keys:
        d = d.get(key, default)
        if d is default:
            return default
    return d
print(get_nested_value(data, ['a', 'b', 'c']))  # 1
