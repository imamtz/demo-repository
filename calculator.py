def add(x, y):
    """Adds two numbers and returns the result."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers and returns the result."""
    return x - y

def multiply(x, y):  # New function
    """Multiplies two numbers and returns the result."""
    return x * y

def divide(a, b):
    """Divides two numbers and returns the result.
    """
    """
    Raise ZeroDivisionError if the second number (y) is zero.
    """
    if y == 0:
        raise ZeroDivisionError('Division by zero is not allowed.')
    return a / b

# New feature: Power function
def power(a, b):
    return a ** b
