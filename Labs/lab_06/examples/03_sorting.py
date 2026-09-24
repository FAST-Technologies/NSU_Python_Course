"""sorted() and list.sort()."""

numbers = [8, 3, 10, 1]

ordered = sorted(numbers)

print("Original:", numbers)
print("New sorted list:", ordered)

numbers.sort(reverse=True)

print("Changed original:", numbers)
