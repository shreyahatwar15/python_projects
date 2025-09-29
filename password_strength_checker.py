"""
A python script that checks the strength of a password.
- hide password input using 'getpass' (no echo on screen)
"""

import string
import random
import getpass

def check_password_strength(password):
    issues = []

    if len(password) < 8:
        issues.append(f"Too short(minimum 8 characters)")
    if not any(c.islower() for c in password):
        issues.append(f"Missing lower character")
    if not any(c.isupper() for c in password):
        issues.append(f"Missing upper character")  
    if not any(c.isdigit() for c in password):
        issues.append(f"Missing digit")
    if not any(c in string.punctuation for c in password):
        issues.append(f"Missing punctuation")
    return issues

def get_strong_password(length = 12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

password = getpass.getpass(f"Enter your password")
issues = check_password_strength(password)

if not issues:
    print(f"Strong password, Good to go!\n")
else:
    print(f"You have weak password")
    for issue in issues:
        print(f" - {issue}")

suggestion = get_strong_password()
print(f"Suggesting you a strong password") 
print(suggestion)
              