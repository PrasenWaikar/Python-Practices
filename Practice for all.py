def evaluate_postfix(postfix_exp):
    stack = []

    for char in postfix_exp:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 // operand2  # Integer division for simplicity
            else:
                raise ValueError("Invalid operator")

            stack.append(result)

    return stack.pop()

# Example usage
postfix_exp1 = "481*+3-"
result1 = evaluate_postfix(postfix_exlp1)
print("Result 1:", result1)  # Output should be 9

postfix_exp2 = "51*3+"
result2 = evaluate_postfix(postfix_exp2)
print("Result 2:", result2)  # Output should be 8
