email=input("Enter your email address:")
def validate_email(email):
    if email.count("@") != 1:
        return "Invalid"
    username, domain = email.split("@")
    if not username or not domain:
        return "Invalid"
    if "." not in domain:
        return "Invalid"
    if domain.startswith(".") or domain.endswith("."):
        return "Invalid"
    else:
        return "Valid"
result = validate_email(email)
print("The email address is", result)