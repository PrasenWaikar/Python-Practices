#Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i

def main():
    try:
        n = int(input("Enter a non-negative integer n: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return

        even_numbers = list(even_numbers_generator(n))
        print(", ".join(map(str, even_numbers)))
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()
