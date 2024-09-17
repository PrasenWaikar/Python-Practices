# Sample dictionary
my_dict = {'a': 3, 'b': 1, 'c': 2, 'd': 4}

# Sorting in ascending order by value
asc_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sorting in descending order by value
desc_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Output the results
print("Original dictionary:", my_dict)
print("Dictionary sorted in ascending order by value:", asc_sorted_dict)
print("Dictionary sorted in descending order by value:", desc_sorted_dict)
