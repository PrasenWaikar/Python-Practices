from collections import defaultdict
items = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot')]
grouped = defaultdict(list)
for key, value in items:
    grouped[key].append(value)
print(grouped)  # {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']}
