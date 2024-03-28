sample_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_remove = 'b'
if key_to_remove in sample_dict:
    del sample_dict[key_to_remove]
    print(f'{key_to_remove} removed from the dictionary.')
else:
    print(f'{key_to_remove} not found in the dictionary.')
