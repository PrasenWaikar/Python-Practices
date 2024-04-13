year = int(input("Enter a year: "))
century = (year // 100) + 1 if year % 100 != 0 else year // 100
print("Century:", century)
