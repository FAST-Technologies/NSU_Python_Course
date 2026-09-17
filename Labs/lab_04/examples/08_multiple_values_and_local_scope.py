"""Multiple return values and local variables."""

def rectangle_info(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter


area, perimeter = rectangle_info(5, 3)

print("Area:", area)
print("Perimeter:", perimeter)

# width and height are parameters local to the function.
# area and perimeter inside the function are also local names.
