def inverted_pyramid_pattern(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)

# Example usage
inverted_pyramid_pattern(5)
