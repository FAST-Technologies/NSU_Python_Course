"""Base case and recursive case."""


def countdown(n):
    """Something."""
    if n == 0:
        print("Go!")
        return

    print(n)
    countdown(n - 1)


countdown(3)


def sum_to(n):
    """Something."""
    if n == 0:
        return 0

    return n + sum_to(n - 1)


print(sum_to(4))
