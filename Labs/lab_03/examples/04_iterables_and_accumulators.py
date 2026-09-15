"""Iterating over strings, lists, and dictionaries."""

word = "Python"
vowel_count = 0

for character in word.lower():
    if character in "aeiou":
        vowel_count += 1

print("Vowels:", vowel_count)

scores = [80, 95, 70, 88]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print(f"Average: {average:.2f}")

student_scores = {"Anna": 90, "Boris": 82}

for name, score in student_scores.items():
    print(name, score)
