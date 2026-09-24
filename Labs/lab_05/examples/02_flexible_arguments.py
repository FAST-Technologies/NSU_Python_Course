"""Examples of *args and **kwargs."""


def total(*numbers):
    """Something."""
    return sum(numbers)


print(total(1, 2, 3))
print(total())


def show_profile(**details):
    """Something."""
    for key, value in details.items():
        print(f"{key}: {value}")


show_profile(
    name="Anna",
    city="Novosibirsk",
    year=1,
)


def report(title, *scores, **options):
    """Something."""
    print("Title:", title)
    print("Scores:", scores)
    print("Options:", options)


report(
    "Exam",
    80,
    92,
    75,
    rounded=True,
    scale=100,
)
