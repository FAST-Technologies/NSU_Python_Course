"""Names can refer to objects of different types."""

value = 10
print(value, type(value))

value = "Python"
print(value, type(value))

value = [1, 2, 3]
print(value, type(value))

# Python is dynamically typed, but operations still respect object types.
# The following would raise TypeError:
# print("5" + 2)
