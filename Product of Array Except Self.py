def product_except_self(arr):
    n = len(arr)
    result = [1] * n
    left_product = 1

    for i in range(n):
        result[i] = left_product
        left_product *= arr[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= arr[i]

    return result

arr = [1, 2, 3, 4]
print("Product of array except self:", product_except_self(arr))
