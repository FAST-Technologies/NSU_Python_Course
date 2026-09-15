"""Using break and continue."""

names = ["Anna", "Boris", "Sasha", "Maria"]

for name in names:
    if name == "Sasha":
        print("Found Sasha")
        break

numbers = [4, -2, 0, 7, -5, 3]

print("Squares of positive numbers:")
for number in numbers:
    if number <= 0:
        continue

    print(number ** 2)
