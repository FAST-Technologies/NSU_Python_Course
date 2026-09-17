"""Defining and calling functions."""

def greet(name):
    """Return greeting."""
    print(f"Hello, {name}")


def rectangle_area(width, height):
    """Return area."""
    area = width * height
    return area


greet("Anna")
greet("Boris")

result = rectangle_area(5, 3)
print(result)
