def calculator(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case _:
            return "Invalid operation"

print(calculator(10, 5, '+'))  # Output: 15
