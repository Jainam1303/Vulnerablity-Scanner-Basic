def check_password_strength(password):
    # Initialize password strength score
    score = 0

    # Check for length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters."

    # Check for uppercase letters
    has_uppercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
            break

    # Check for lowercase letters
    has_lowercase = False
    for char in password:
        if char.islower():
            has_lowercase = True
            break

    # Check for digits
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    # Check for special characters
    has_special_char = False
    for char in password:
        if not char.isalnum():
            has_special_char = True
            break

    # Check for repeated characters
    if len(set(password)) < len(password):
        return "Password contains repeated characters. Please use unique characters."

    # Check for password strength
    if not has_uppercase:
        score -= 1
    if not has_lowercase:
        score -= 1
    if not has_digit:
        score -= 1
    if not has_special_char:
        score -= 1

    if score < 3:
        return "Password is weak. It should have at least 3 different character types."
    elif score == 3:
        return "Password is medium. It should have more than 3 different character types."
    else:
        return "Password is strong!"

# Test the function
password = input("Enter a password: ")
print(check_password_strength(password))