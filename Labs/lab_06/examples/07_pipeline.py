"""Combining filter(), sorted(), and map()."""

students = [
    {"name": "Anna", "score": 82},
    {"name": "Boris", "score": 55},
    {"name": "Mira", "score": 91},
]

passed = filter(
    lambda student: student["score"] >= 60,
    students,
)

ranked = sorted(
    passed,
    key=lambda student: student["score"],
    reverse=True,
)

names = list(
    map(
        lambda student: student["name"],
        ranked,
    )
)

print(names)
