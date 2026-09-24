"""Common list methods."""

numbers = [10, 20]

numbers.append(30)
print(numbers)

numbers.extend([40, 50])
print(numbers)

numbers.insert(1, 15)
print(numbers)

numbers.remove(20)
print(numbers)

last = numbers.pop()
print("Removed:", last)
print(numbers)

items = ["a", "b", "a", "c"]
print("Index of a:", items.index("a"))
print("Count of a:", items.count("a"))
