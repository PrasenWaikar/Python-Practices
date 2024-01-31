# Write a program to find all pairs of elements in a list that sum up to a given target value.
# numbers = [2, 4, 5, 3, 1, 6, 8, 9, 7]
# target_sum = 10
# Output: [(4, 6), (5, 5), (3, 7), (1, 9)]
n=[2, 4, 5, 3, 1, 6, 8, 9, 7]
t=10
for i in n:
    for j in n:
        if (i,j)==(j,i):
            break;
        if i + j == 10:
            print(i, j)


