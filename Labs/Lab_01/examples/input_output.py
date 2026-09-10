"""
Example of input, output, and type conversion.
"""

name = input("Enter your name: ")

age_text = input("Enter your age: ")

print("Value returned by input():", age_text)
print("Type before conversion:", type(age_text))

age = int(age_text)

print("Type after conversion:", type(age))

next_year_age = age + 1

print("Hello,", name)
print("Next year you will be", next_year_age)