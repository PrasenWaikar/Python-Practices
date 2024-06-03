num_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
sum_positive = sum(x for x in num_list if x > 0)
product_negative = 1
for x in num_list:
    if x < 0:
        product_negative *= x
print("Sum of positive numbers:", sum_positive)
print("Product of negative numbers:", product_negative)
