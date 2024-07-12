# Please write a program which prints all permutations of [1,2,3]
import itertools

# List to be permuted
lst = [1, 2, 3]

# Get all permutations of the list
permutations = list(itertools.permutations(lst))

# Print each permutation
for perm in permutations:
    print(perm)
