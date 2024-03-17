def hollow_square_pattern(n):
    print("* " * n)
    for i in range(n - 2):
        print("* " + "  " * (n - 2) + "* ")
    print("* " * n)

# Example usage
hollow_square_pattern(5)
