from itertools import permutations

def number_permutations(number):
    number_str = str(number)
    perms = permutations(number_str)
    return [int(''.join(perm)) for perm in perms]

number = 123
perms = number_permutations(number)
print(f"Permutations of {number}: {perms}")
