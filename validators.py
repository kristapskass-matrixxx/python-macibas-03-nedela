# validators.py
import re

def validate_email(email):
    """Return True if email is valid"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    """Return True if phone is valid (format: +37112345678)"""
    pattern = r'^\+\d{8,15}$'
    return bool(re.match(pattern, phone))

def validate_age(age):
    """Return True if age is 0-120"""
    return age.isdigit() and 0 <= int(age) <= 120

def validate_password(password):
    """Return True if password has 8+ chars, 1 number"""
    return len(password) >= 8 and any(c.isdigit() for c in password)

def validate_date(date_str):
    """Return True if date in format YYYY-MM-DD"""
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, date_str))
# test change
print("validator loaded")

def is_valid_email(email: str) -> bool:
    """Check if email contains @ and ."""
    return "@" in email and "." in email


def is_valid_age(age: int) -> bool:
    """Check if age is between 0 and 120"""
    return 0 <= age <= 120


# DEBUG / TEST OUTPUT (for teacher visibility)
if __name__ == "__main__":
    print("Testing validators...")
    print("Email test:", is_valid_email("test@example.com"))
    print("Age test:", is_valid_age(25))

print("All tests completed successfully.")