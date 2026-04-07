# utils.py

def greet(name):
    """Return a greeting string"""
    return f"Hello, {name}!"

def add(a, b):
    """Return the sum of two numbers"""
    return a + b

def multiply(a, b):
    """Return the product of two numbers"""
    return a * b

def square_list(numbers):
    """Return a list of squares"""
    return [x**2 for x in numbers]

def is_even(n):
    """Return True if n is even"""
    return n % 2 == 0

def reverse_string(s):
    """Return reversed string"""
    return s[::-1]

def list_length(lst):
    """Return length of list"""
    return len(lst)

def sum_list(lst):
    """Return sum of elements in list"""
    return sum(lst)