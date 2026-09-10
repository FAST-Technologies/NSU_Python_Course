"""
Lecture 02 Example — Built-in Functions
"""

values = [12, 7, 19, 5, 14]

print(f"Count: {len(values)}")
print(f"Minimum: {min(values)}")
print(f"Maximum: {max(values)}")
print(f"Total: {sum(values)}")

mean = sum(values) / len(values)
print(f"Mean: {mean:.2f}")

temperature_change = -7.438
print(abs(temperature_change))

price = 19.87654
print(round(price, 2))
