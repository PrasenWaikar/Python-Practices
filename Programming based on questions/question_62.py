# Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
# with a given n input by console (n>0).

def compute_f(n):
    if n == 0:
        return 1
    else:
        return compute_f(n - 1) + 100

def main():
    try:
        n = int(input("Enter a positive integer n: "))
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
            return

        result = compute_f(n)
        print(f"f({n}) = {result}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
