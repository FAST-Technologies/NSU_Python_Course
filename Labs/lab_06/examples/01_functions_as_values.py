"""Functions can be stored and passed like other objects."""


def square(number):
    """Something."""
    return number ** 2


operation = square

print(square)
print(operation)
print(operation(5))
print(operation is square)


def apply(function, value):
    """Something."""
    return function(value)


print(apply(square, 6))
