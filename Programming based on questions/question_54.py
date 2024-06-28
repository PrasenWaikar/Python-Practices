#Define a custom exception class which takes a string message as attribute.



class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Example usage:
try:
    raise CustomException("This is a custom exception message.")
except CustomException as e:
    print(f"Caught an exception: {e.message}")
