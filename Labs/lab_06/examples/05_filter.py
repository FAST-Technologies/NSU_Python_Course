"""Filtering values."""

numbers = [1, 2, 3, 4, 5, 6]

evens = filter(
    lambda number: number % 2 == 0,
    numbers,
)

print(evens)
print(list(evens))
