"""  
 Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function
"""
# Print documentation for built-in functions
print("Documentation for abs():")
help(abs)

print("\nDocumentation for int():")
help(int)

# Define your own function with documentation
def my_function():
    """This function does something."""
    pass

print("\nDocumentation for my_function():")
help(my_function)
