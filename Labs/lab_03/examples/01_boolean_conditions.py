"""Boolean expressions and basic conditions."""

age = 20
score = 72

is_adult = age >= 18
passed = score >= 60
eligible = is_adult and passed

print("Adult:", is_adult)
print("Passed:", passed)
print("Eligible:", eligible)

if eligible:
    print("The student satisfies both conditions.")
else:
    print("At least one condition is false.")
