sample_dict = {'banana': 3, 'apple': 2, 'orange': 1, 'grapes': 4}

sorted_dict = dict(sorted(sample_dict.items()))

print("Sorted dictionary by key in ascending order:")
for key, value in sorted_dict.items():
    print(f"{key}: {value}")
