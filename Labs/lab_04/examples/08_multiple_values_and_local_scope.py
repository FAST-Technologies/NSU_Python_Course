"""Multiple return values and local variables."""

def rectangle_info(width, height):
    """Return reactangle info."""
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter


areas, perimeters = rectangle_info(5, 3)

print("Area:", areas)
print("Perimeter:", perimeters)

# width and height are parameters local to the function.
# area and perimeter inside the function are also local names.
