"""
Lab 02 — Python Basics II

Complete all tasks below.

Topics:
- built-in functions
- assignment and augmented assignment
- operator precedence
- type conversion
- strings
- print() options
- collections
- mutable and immutable objects
- formatted output
- basic PEP 8
- reading common errors

Do not use:
- if
- for
- while
- user-defined functions
"""
# pylint: disable=invalid-name

from typing import List, Dict, TypedDict, Any

# ============================================================
# Task 1 — Built-in Functions
# ============================================================

print("Task 1 — Built-in Functions")

values: List[int] = [12, 7, 19, 5, 14]

# Using built-in functions, calculate and print:
# number of values, smallest value, largest value, total, mean
# Do not calculate these manually.

count: int = len(values)
smallest: int = min(values)
largest: int = max(values)
total: int = sum(values)
mean: float = sum(values) / len(values)

# Print the results using f-strings.
print(f"Number of values: {count}")
print(f"Smallest value: {smallest}")
print(f"Largest value: {largest}")
print(f"Total: {total}")
print(f"Mean: {mean}")

print()


# ============================================================
# Task 2 — Absolute Value and Rounding
# ============================================================

print("Task 2 — Absolute Value and Rounding")

temperature_change: float = -7.438
measurement: float = 19.87654

# Print the absolute value of temperature_change.
# Expected numerical value: 7.438
print(f"Absolute value of temperature_change: {abs(temperature_change)}")

# Round measurement to 1, 2, and 3 decimal places using round().
print(f"Rounded to 1 decimal place: {round(measurement, 1)}")
print(f"Rounded to 2 decimal places: {round(measurement, 2)}")
print(f"Rounded to 3 decimal places: {round(measurement, 3)}")

print()


# ============================================================
# Task 3 — Assignment and Augmented Assignment
# ============================================================

print("Task 3 — Assignment and Augmented Assignment")

balance: float = 1000.0

# Perform the following operations using augmented assignment:
# 1. Add 250 to the balance.
# 2. Subtract 120.
# 3. Multiply the remaining balance by 1.05.

balance += 250
balance -= 120
balance *= 1.05

# Print the final balance with two decimal places.
print(f"Final balance: {balance:.2f}")

print()


# ============================================================
# Task 4 — Operator Precedence
# ============================================================

print("Task 4 — Operator Precedence")

# Before running the program, predict each result.

expression_1: int = 2 + 3 * 4
expression_2: int = (2 + 3) * 4
expression_3: float = 20 / 5 + 3  # Division always results in float
expression_4: float = 20 / (5 + 3)
expression_5: int = 2 ** 3 ** 2

# Print each expression and its result.
print(f"2 + 3 * 4 = {expression_1}")
print(f"(2 + 3) * 4 = {expression_2}")
print(f"20 / 5 + 3 = {expression_3}")
print(f"20 / (5 + 3) = {expression_4}")
print(f"2 ** 3 ** 2 = {expression_5}")

print()


# ============================================================
# Task 5 — Time Conversion
# ============================================================

print("Task 5 — Time Conversion")

# Ask the user to enter a number of seconds.
total_seconds_input: str = input("Enter a number of seconds: ")

# Convert the input to int.
total_seconds: int = int(total_seconds_input)

# Calculate whole minutes and remaining seconds.
# Example: 135 seconds -> 2 minutes and 15 seconds
minutes: int = total_seconds // 60
remaining_seconds: int = total_seconds % 60

# Print the result.
print(f"{total_seconds} seconds = {minutes} minute(s) and {remaining_seconds} second(s)")

print()


# ============================================================
# Task 6 — Conversion Is Not Always Reversible
# ============================================================

print("Task 6 — Type Conversion")

value: float = 17.95

# Convert value to int and print it.
# Note: int() does NOT round the value; it truncates the decimal part.
integer_value: int = int(value)
print(f"Integer value: {integer_value}")

# Convert integer_value back to float and print it.
float_value: float = float(integer_value)
print(f"Float value: {float_value}")

# Convert integer_value to str and print value and type.
text_value: str = str(integer_value)
print(f"Value as text: {text_value}")
print(f"Type: {type(text_value)}")

print()


# ============================================================
# Task 7 — Basic String Operations
# ============================================================

print("Task 7 — Basic String Operations")

first_name: str = input("First name: ")
last_name: str = input("Last name: ")

# Create full_name using string concatenation.
full_name: str = first_name + " " + last_name

# Print full name details.
print(f"Full name: {full_name}")
print(f"Number of characters: {len(full_name)}")
print(f"First character: {full_name[0]}")
print(f"Last character: {full_name[-1]}")
print(f"First three characters: {full_name[:3]}")

# Print full_name three times using string repetition.
print(full_name * 3)

print()


# ============================================================
# Task 8 — Useful print() Options
# ============================================================

print("Task 8 — Useful print() Options")

language: str = "Python"
course: str = "AI and Big Data Analytics"
university: str = "NSU"

# Print the three values on one line separated by " | ".
print(language, course, university, sep=" | ")

# Use two print() calls and end= to print "Python Programming".
print("Python", end=" ")
print("Programming")

print()


# ============================================================
# Task 9 — Collections and Choosing Data Structures
# ============================================================

print("Task 9 — Collections")


class StudentInfo(TypedDict):
    """Typed dictionary representing student information."""
    name: str
    age: int
    skills: List[str]
    university: str


student_name: str = "Anna"
student_age: int = 22
student_skills: List[str] = ["Python", "Mathematics", "Machine Learning"]
student_university: str = "NSU"

# Create a dictionary named student with the specified keys.
student: StudentInfo = {
    "name": student_name,
    "age": student_age,
    "skills": student_skills,
    "university": student_university
}

# Print student details using dictionary access, indexing, and len().
print(f"Name: {student['name']}")
print(f"University: {student['university']}")
print(f"First skill: {student['skills'][0]}")
print(f"Number of skills: {len(student['skills'])}")

print()


# ============================================================
# Task 10 — Mutable and Immutable Objects
# ============================================================

print("Task 10 — Mutable and Immutable Objects")

# List example — mutable
numbers: List[int] = [10, 20, 30]
same_numbers: List[int] = numbers

# Change the first item in numbers to 99.
numbers[0] = 99

print(f"numbers: {numbers}")
print(f"same_numbers: {same_numbers}")
# Observation: Both show [99, 20, 30] because lists are mutable 
# and both variables reference the same object in memory.

# String example — immutable
text: str = "Python"
same_text: str = text

# Create a new string by adding " Course" to text.
text = text + " Course"

print(f"text: {text}")
print(f"same_text: {same_text}")
# Observation: 'text' is now "Python Course", but 'same_text' 
# remains "Python". Strings are immutable, creating a new object.

print()


# ============================================================
# Task 11 — Small Statistics Report
# ============================================================

print("Task 11 — Small Statistics Report")

scores: List[int] = [78, 92, 85, 69, 88]

# Calculate statistics using built-in functions.
score_count: int = len(scores)
minimum_score: int = min(scores)
maximum_score: int = max(scores)
total_score: int = sum(scores)
mean_score: float = sum(scores) / len(scores)

# Print a clean report, formatting the mean to two decimal places.
print(f"Number of scores: {score_count}")
print(f"Minimum: {minimum_score}")
print(f"Maximum: {maximum_score}")
print(f"Mean: {mean_score:.2f}")

print()


# ============================================================
# Task 12 — PEP 8 Cleanup
# ============================================================

print("Task 12 — PEP 8 Cleanup")

# Rewrite using meaningful variable names, snake_case, spaces, 
# intermediate variables, and formatted output.

price: int = 1250
quantity: int = 3
discount_percent: int = 10

total_cost: int = price * quantity
final_amount: float = total_cost - (discount_percent / 100) * total_cost

print(f"Final: {final_amount}")

print()


# ============================================================
# Optional Challenge — Student Score Summary
# ============================================================

print("Optional Challenge — Student Score Summary")

# Ask the user for student name and three test scores.
student_name_input: str = input("Enter student name: ")
score1: float = float(input("Enter first test score: "))
score2: float = float(input("Enter second test score: "))
score3: float = float(input("Enter third test score: "))

# Store the three scores in a list.
scores_list: List[float] = [score1, score2, score3]

# Calculate minimum, maximum, and mean score.
min_score: float = min(scores_list)
max_score: float = max(scores_list)
mean_score_challenge: float = sum(scores_list) / len(scores_list)

# Print a clean summary.
print(f"Student: {student_name_input}")
print(f"Scores: {scores_list}")
print(f"Minimum: {min_score:.2f}")
print(f"Maximum: {max_score:.2f}")
print(f"Mean: {mean_score_challenge:.2f}")

print()


# ============================================================
# Task 13 — Multiple Assignment
# ============================================================

print("Task 13 — Multiple Assignment")

# Assign these three values using ONE statement.
x: int
y: int
z: int
x, y, z = 10, 20, 30

# Print x, y, and z.
print(f"x: {x}, y: {y}, z: {z}")

# Swap a and b using one Python statement.
a: int
b: int
a, b = 5, 10
a, b = b, a  # Swapping in one statement

print(f"After swapping -> a: {a}, b: {b}")

print()


# ============================================================
# Task 14 — String Methods
# ============================================================

print("Task 14 — String Methods")

text_methods: str = "  Python Programming Course  "

# Print the text with various string methods.
print(f"1. Without surrounding spaces: '{text_methods.strip()}'")
print(f"2. Lowercase: {text_methods.lower()}")
print(f"3. Uppercase: {text_methods.upper()}")
print(f"4. Replaced: {text_methods.replace('Course', 'Lab')}")

# Check and print whether the cleaned text starts/ends with specific words.
cleaned_text: str = text_methods.strip()
print(f"Starts with 'Python': {cleaned_text.startswith('Python')}")
print(f"Ends with 'Course': {cleaned_text.endswith('Course')}")

print()


# ============================================================
# Task 15 — Boolean Expressions
# ============================================================

print("Task 15 — Boolean Expressions")

age: int = 22
score: int = 85
is_master_student: bool = True

# Print the result of boolean expressions.
print(f"age >= 18: {age >= 18}")
print(f"score >= 60: {score >= 60}")
print(f"score >= 60 and is_master_student: {score >= 60 and is_master_student}")
print(f"score < 60 or age < 18: {score < 60 or age < 18}")
print(f"not is_master_student: {not is_master_student}")

# Predict and then print bool() conversions.
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f'bool(""): {bool("")}')
print(f'bool("Python"): {bool("Python")}')
print(f"bool([]): {bool([])}")
print(f"bool([1, 2]): {bool([1, 2])}")

print()


# ============================================================
# Task 16 — Membership
# ============================================================

print("Task 16 — Membership")

numbers_list: List[int] = [10, 20, 30]
text_membership: str = "Python Programming"
student_dict: Dict[str, Any] = {
    "name": "Anna",
    "age": 22,
}

# Print the result of membership tests.
print(f"20 in numbers: {20 in numbers_list}")
print(f"50 not in numbers: {50 not in numbers_list}")
print(f"'Python' in text: {'Python' in text_membership}")
print(f"'Java' not in text: {'Java' not in text_membership}")
print(f"'age' in student: {'age' in student_dict}")
print(f"'email' in student: {'email' in student_dict}")

print()