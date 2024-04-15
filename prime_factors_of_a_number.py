num = int(input("Enter a number: "))
factors = []
divisor = 2
while divisor <= num:
    if num % divisor == 0:
        factors.append(divisor)
        num //= divisor
    else:
        divisor += 1
print("Prime factors:", factors)
