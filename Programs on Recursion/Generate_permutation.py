def permutations(s):
    if len(s) == 1:
        return [s]
    perms = []
    for i, char in enumerate(s):
        for perm in permutations(s[:i] + s[i+1:]):
            perms.append(char + perm)
    return perms

print(permutations("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
