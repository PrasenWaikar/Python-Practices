num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 >= num3:
    print("Numbers in descending order:", num1, num2, num3)
elif num1 >= num3 >= num2:
    print("Numbers in descending order:", num1, num3, num2)
elif num2 >= num1 >= num3:
    print("Numbers in descending order:", num2, num1, num3)
elif num2 >= num3 >= num1:
    print("Numbers in descending order:", num2, num3, num1)
elif num3 >= num1 >= num2:
    print("Numbers in descending order:", num3, num1, num2)
else:
    print("Numbers in descending order:", num3, num2, num1)
