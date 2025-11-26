"""Small math utility functions used for pytest demo."""


def add(a, b):
    """Return the sum of two numbers.

    This is intentionally simple so tests can exercise basic behavior.
    """
    return a + b


def subtract(a, b):
    """Return the difference of two numbers.

    This is intentionally simple so tests can exercise basic behavior.
    """
    return a - b


def sum_list(numbers):
    """Return the sum of an iterable of numbers.

    - If `numbers` is None, raise TypeError to make invalid input explicit.
    - An empty iterable returns 0.
    """
    if numbers is None:
        raise TypeError("numbers must be an iterable of numbers")

    total = 0
    for n in numbers:
        total += n
    return total
