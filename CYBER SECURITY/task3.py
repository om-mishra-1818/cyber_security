def check_password(password):
    # Check conditions
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(char in "!@#$%^&*()" for char in password)
    
    # Check password length
    if len(password) < 8:
        return "Weak password: Too short!"
    
    # Check other conditions
    if upper and lower and digit and special:
        return "Strong password!"
    elif upper or lower or digit or special:
        return "Moderate password!"
    else:
        return "Weak password!"

# Test the function
password = input("Enter a password: ")
print(check_password(password))
