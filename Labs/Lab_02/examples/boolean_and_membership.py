age = 22
score = 85
is_master_student = True

print(age >= 18)
print(score >= 60 and is_master_student)
print(score < 60 or age < 18)
print(not is_master_student)

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2]))

numbers = [10, 20, 30]

print(20 in numbers)
print(50 not in numbers)

text = "Python Programming"

print("Python" in text)
print("Java" not in text)

student = {"name": "Anna", "age": 22}

print("age" in student)
print("email" in student)