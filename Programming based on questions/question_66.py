#Please write assert statements to verify that every number in the list [2,4,6,8] is even.
numbers = [2, 4, 6, 8]

for number in numbers:
    assert number % 2 == 0, f"{number} is not an even number"

print("All numbers are even.")
