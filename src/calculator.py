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


def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The remainder of a / b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot compute modulo with divisor zero")
    return a % b
