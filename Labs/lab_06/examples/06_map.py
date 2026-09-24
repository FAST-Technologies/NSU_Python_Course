"""Transforming values with map()."""

numbers = [1, 2, 3, 4]

doubled = map(
    lambda number: number * 2,
    numbers,
)

print(list(doubled))


prices = [100, 250, 80]

with_tax = map(
    lambda price: price * 1.10,
    prices,
)

print(list(with_tax))
