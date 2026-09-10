"""
Lecture 02 Example — Strings and print()
"""

first_name = "Anna"
last_name = "Smith"

full_name = first_name + " " + last_name

print(full_name)
print(len(full_name))
print(full_name[0])
print(full_name[-1])
print(full_name[:3])

print("Python" * 3)

name = "Anna"
age = 22

print(name, age)
print(name, age, sep=" | ")

print("Python", end=" ")
print("Programming")

text = "  Python Programming Course  "

clean_text = text.strip()

print(clean_text)
print(clean_text.lower())
print(clean_text.upper())
print(clean_text.replace("Course", "Lab"))

print(clean_text.startswith("Python"))
print(clean_text.endswith("Course"))