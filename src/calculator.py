"""Simple calculator module for PETER framework demo."""


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b.
    
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Raise base to the exponent.

    Args:
        base: The base number.
        exponent: The exponent to raise to.

    Returns:
        base raised to the exponent.

    Raises:
        ValueError: If base is 0 and exponent is negative.
    """
    if base == 0 and exponent < 0:
        raise ValueError("Cannot raise 0 to a negative power")
    return base ** exponent


import math


def sqrt(n: float) -> float:
    """Return the square root of n.

    Args:
        n: The number to take the square root of.

    Returns:
        The square root of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(n)
