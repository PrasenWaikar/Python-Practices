mat = [[1, 3, 5],
       [2, 6, 9],
       [3, 6, 9]]

arr = []

for i in range(3):
    for j in range(3):
        arr.append(mat[i][j])

arr.sort()

print("Median of the given matrix is :", arr[4])