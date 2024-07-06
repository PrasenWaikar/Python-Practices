#Please write a program which accepts basic mathematic expression from console and print the evaluation result.
def main():
    try:
        expression = input("Enter a mathematical expression: ")
        result = eval(expression)
        print(f"The result of '{expression}' is: {result}")
    except Exception as e:
        print(f"Error evaluating expression: {e}")

if __name__ == "__main__":
    main()
