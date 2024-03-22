def matrix_row_column_sum(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    row_sums = [0] * num_rows
    col_sums = [0] * num_cols

    for i in range(num_rows):
        for j in range(num_cols):
            row_sums[i] += matrix[i][j]
            col_sums[j] += matrix[i][j]

    return row_sums, col_sums

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sums, col_sums = matrix_row_column_sum(matrix)

print("Row sums:", row_sums)
print("Column sums:", col_sums)
