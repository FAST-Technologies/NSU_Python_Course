"""Sorting with key functions."""

words = ["pear", "watermelon", "fig"]

print(sorted(words, key=len))

students = [
    ("Anna", 82),
    ("Boris", 95),
    ("Mira", 88),
]

ranked = sorted(
    students,
    key=lambda student: student[1],
    reverse=True,
)

print(ranked)
