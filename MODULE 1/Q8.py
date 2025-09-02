import re

# Program to validate passwords

# Take comma-separated input
passwords = input("Enter passwords separated by commas: ").split(",")

valid_passwords = []

for pwd in passwords:
    pwd = pwd.strip()  # remove spaces
    
    if (6 <= len(pwd) <= 12
        and re.search("[a-z]", pwd)   # at least one lowercase
        and re.search("[A-Z]", pwd)   # at least one uppercase
        and re.search("[0-9]", pwd)   # at least one digit
        and re.search("[$#@]", pwd)): # at least one special char
        valid_passwords.append(pwd)

# Print valid passwords in comma-separated format
print(",".join(valid_passwords))