def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    """Return a list of prime numbers in the given range [start, end]."""
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Example usage
start_range = 10
end_range = 50
print(f"Prime numbers between {start_range} and {end_range}: {prime_numbers_in_range(start_range, end_range)}")
