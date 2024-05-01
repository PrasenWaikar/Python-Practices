"""  
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
"""
class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

# Example usage
n = 50
divisible_by_seven = DivisibleBySeven(n)
generator = divisible_by_seven.generate_divisible_by_seven()

for num in generator:
    print(num)
