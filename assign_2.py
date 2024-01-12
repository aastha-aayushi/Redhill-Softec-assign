import re

def is_valid_password(password):
    # Minimum 8 characters
    if len(password) < 8:
        return False

    # The alphabet must be between [a-z]
    if not re.search("[a-z]", password):
        return False

    # At least one alphabet should be of Upper Case [A-Z]
    if not re.search("[A-Z]", password):
        return False

    # At least 1 number or digit between [0-9]
    if not re.search("[0-9]", password):
        return False

    # At least 1 character from [ _ or @ or $ ]
    if not re.search("[_@$]", password):
        return False

    return True

# Example usage:
password_to_check = "MyPassword123@"
if is_valid_password(password_to_check):
    print("Password is valid.")
else:
    print("Password is not valid.")
