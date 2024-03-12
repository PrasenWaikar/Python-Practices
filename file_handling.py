def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of {filename}:")
            print(content)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Successfully wrote to {filename}.")

def append_to_file(filename, content):
    with open(filename, 'a') as f:
        f.write(content)
    print(f"Successfully appended to {filename}.")

# Example usage
file_name = "sample.txt"
write_to_file(file_name, "Hello, this is a sample file.\n")
append_to_file(file_name, "This is additional content.\n")
read_file(file_name)