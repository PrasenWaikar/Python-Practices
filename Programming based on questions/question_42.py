#Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
# Accept input from the user
user_input = input("Enter a string: ")

# Check if the input matches "yes" in any case
if user_input.lower() == "yes":
    print("Yes")
else:
    print("No")
