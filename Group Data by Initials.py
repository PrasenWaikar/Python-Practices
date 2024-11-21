names = ['Alice', 'Anna', 'Bob', 'Charlie']
initials = defaultdict(list)
for name in names:
    initials[name[0]].append(name)
