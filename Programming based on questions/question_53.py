#Write a function to compute 5/0 and use try/except to catch the exceptions.



def divide_by_zero():
    try:
        result = 5 / 0
    except ZeroDivisionError as e:
        return f"Caught an exception: {e}"
    return result

# Example usage:
print(divide_by_zero())
