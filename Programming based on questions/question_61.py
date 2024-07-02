#Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
def compute_series_sum(n):
    series_sum = 0
    for i in range(1, n + 1):
        series_sum += i / (i + 1)
    return series_sum

def main():
    try:
        n = int(input("Enter a positive integer n: "))
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
            return

        result = compute_series_sum(n)
        print(f"The sum of the series for n={n} is: {result:.6f}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
