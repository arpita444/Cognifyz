input("password must be at least 10 characters long, contain uppercase and lowercase letters, digits, and one special character i.e. @ or _ ")
def check_password(password):
        errors = []  #list to hold user input errors
        if len(password) < 10:
            errors.append("- Must be at least 10 characters long")
        if not any(char.isdigit() for char in password):
            errors.append("- Missing a digit")
        if not any(char.isupper() for char in password):
            errors.append("- Missing a uppercase letter")
        if not any(char.islower() for char in password):
            errors.append("- Missing a lowercase letter")
        if ("@" in password) == ("_" in password):
            errors.append("- Must contain either '@' or '_', but not both")
        if not errors:
            return "Strong"
        else:
            return errors
password = input("Enter a password: ")
result = check_password(password)
if result == "Strong": 
    print("✅ Password is strong and valid!") 
else: 
    print("❌ Password has the following issues:") 
    for error in result: 
        print(error)