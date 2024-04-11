def generate_series(n):
    series = [1,1,2,3,4,7,8,15,9,24,16,40,32,72,104,27]
    for i in range(0, n):
        if i % 2 == 0:  # Prime position
            series.append(2 ** (i // 2))
        elif i % 2 != 0 and int(i ** 0.5) ** 2 == i:  # Perfect square position
            series.append(3 ** (i // 2))
        else:  # Sum of previous 2 values
            series.append(series[-1] + series[-2])
    return series[n - 1]


n = int(input("enter value for n : "))
result = generate_series(n)
print(f"The {n}th term in the series is: {result}")
