"""Functions can be stored and passed like other objects."""


def square(number):
    return number ** 2


operation = square

print(square)
print(operation)
print(operation(5))
print(operation is square)


def apply(function, value):
    return function(value)


print(apply(square, 6))
