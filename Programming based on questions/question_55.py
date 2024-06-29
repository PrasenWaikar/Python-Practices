#Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.



def get_username(email):
    try:
        username = email.split('@')[0]
        return username
    except IndexError:
        return "Invalid email format"

# Example usage:
email = "username@companyname.com"
print("The username is:", get_username(email))
