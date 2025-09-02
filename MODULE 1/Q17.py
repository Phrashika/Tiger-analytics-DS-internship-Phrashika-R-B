import re

def validate_email(email):
    # Rule: only one '@'
    if email.count('@') != 1:
        return False

    # Regex: only lowercase letters, digits, . , _ , and one '@'
    pattern = r'^[a-z0-9._]+@[a-z0-9._]+$'
    
    if re.match(pattern, email):
        return True
    return False

# --- Example Usage ---
emails = ["test_email123@domain.com",
          "Test@domain.com",
          "hello.world@domain_com",
          "abc@xyz"]

for e in emails:
    if validate_email(e):
        print(e, "✅ Valid")
    else:
        print(e, "❌ Invalid")
