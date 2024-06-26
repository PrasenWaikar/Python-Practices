def is_perfect(n):
    """Check if a number is a perfect number."""
    if n < 1:
        return False
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

def perfect_numbers_in_range(start, end):
    """Return a list of perfect numbers in the given range [start, end]."""
    perfect_numbers = []
    for num in range(start, end + 1):
        if is_perfect(num):
            perfect_numbers.append(num)
    return perfect_numbers

# Example usage
start_range = 1
end_range = 10000
print(f"Perfect numbers between {start_range} and {end_range}: {perfect_numbers_in_range(start_range, end_range)}")
