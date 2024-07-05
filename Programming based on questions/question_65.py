#Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
def divisible_by_5_and_7_generator(n):
    for i in range(n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

def main():
    try:
        n = int(input("Enter a non-negative integer n: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return

        numbers = list(divisible_by_5_and_7_generator(n))
        print(", ".join(map(str, numbers)))
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()
