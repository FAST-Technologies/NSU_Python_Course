"""Positional, keyword, and default arguments."""


def greet(name, message="Hello"):
    """Something."""
    return f"{message}, {name}"


print(greet("Anna"))
print(greet("Anna", "Welcome"))
print(greet(name="Boris", message="Good morning"))


def power(base, exponent):
    """Something."""
    return base ** exponent


print(power(2, 3))
print(power(exponent=2, base=3))
