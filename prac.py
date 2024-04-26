def print_lower_upper_triangular(arr):
    n = len(arr)
    
    # Lower triangular matrix
    print("Lower Triangular Matrix:")
    for i in range(n):
        for j in range(n):
            if j <= i:
                print(arr[i][j], end=" ")
            else:
                print(0, end=" ")
        print()
    
    # Upper triangular matrix
    print("\nUpper Triangular Matrix:")
    for i in range(n):
        for j in range(n):
            if j >= i:
                print(arr[i][j], end=" ")
            else:
                print(0, end=" ")
        print()

# Example array
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print_lower_upper_triangular(arr)
