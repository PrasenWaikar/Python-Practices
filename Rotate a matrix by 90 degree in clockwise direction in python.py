def rotate_matrix_90_clockwise(matrix):
    # Transpose the matrix (swap rows with columns)
    transposed_matrix = list(zip(*matrix))
    
    # Reverse each row of the transposed matrix to get a 90-degree clockwise rotation
    rotated_matrix = [list(row)[::-1] for row in transposed_matrix]
    
    return rotated_matrix

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Rotate matrix
rotated = rotate_matrix_90_clockwise(matrix)

# Print the result
for row in rotated:
    print(row)
