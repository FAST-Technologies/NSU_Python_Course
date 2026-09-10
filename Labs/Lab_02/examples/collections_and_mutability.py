student = {
    "name": "Anna",
    "age": 22,
    "skills": ["Python", "Mathematics"],
}

print(student["name"])
print(student["skills"][0])

numbers = [10, 20, 30]
same_numbers = numbers

numbers[0] = 99

print(numbers)
print(same_numbers)

text = "Python"
same_text = text

text = text + " Course"

print(text)
print(same_text)