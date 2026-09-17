"""break, continue, and loop else."""

number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)

values = [2, 4, 6, 8]

for value in values:
    if value % 2 != 0:
        print("Odd value found")
        break
else:
    print("All values are even")
