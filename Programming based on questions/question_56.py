#Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
def get_company_name(email):
    try:
        company_name = email.split('@')[1].split('.')[0]
        return company_name
    except IndexError:
        return "Invalid email format"

# Example usage:
email = "username@companyname.com"
print("The company name is:", get_company_name(email))
