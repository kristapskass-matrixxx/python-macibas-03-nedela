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