"""Defining and calling functions."""

def greet(name):
    print(f"Hello, {name}")


def rectangle_area(width, height):
    area = width * height
    return area


greet("Anna")
greet("Boris")

result = rectangle_area(5, 3)
print(result)
