
"""
Lab 01 — Python Basics

Complete all tasks below.

Topics:
- variables
- basic data types
- input and output
- type conversion
- arithmetic operators
- basic PEP 8
"""

from typing import List, Dict, Tuple, Set, Any

# ============================================================
# Task 1 — Personal Information
# ============================================================

print("Task 1 — Personal Information")

# TODO:
# Ask the user to enter their name.
name: str = input("Enter your name: ")

# TODO:
# Ask the user to enter their age.
# Remember that input() returns a string.
age: int = int(input("Enter your age: "))

# TODO:
# Print:
# Hello, <name>!
# Next year you will be <age + 1> years old.
print(f"Hello, {name}")
print(f"Next year you will be {age + 1} years old.")

print()

# ============================================================
# Task 2 — Rectangle
# ============================================================

print("Task 2 — Rectangle")

# TODO:
# Ask the user to enter width and height.
width: float = float(input("Enter the width of the rectangle: "))
height: float = float(input("Enter the height of the rectangle: "))

# TODO:
# Calculate the area.
area: float = width * height

# TODO:
# Calculate the perimeter.
perimeter: float = 2 *  width + 2 * height

# TODO:
# Print the results.
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

print()


# ============================================================
# Task 3 — Temperature Converter
# ============================================================

print("Task 3 — Temperature Converter")

# Formula:
# Fahrenheit = Celsius * 9 / 5 + 32

# TODO:
# Read Celsius temperature.
celsius: float = float(input("Enter temperature in Celsius: "))

# TODO:
# Calculate Fahrenheit temperature.
fahrenheit: float = (9.0 * celsius) / 5.0 + 32.0

# TODO:
# Print the result.
print(f"{celsius}°C is equal to {fahrenheit}°F")

print()


# ============================================================
# Task 4 — Purchase Calculator
# ============================================================

print("Task 4 — Purchase Calculator")

# TODO:
# Ask for the number of items.
quantity: int = int(input("Enter the number of items: "))

# TODO:
# Ask for the price of one item.
price: float = float(input("Enter the price of one item: "))

# TODO:
# Calculate the total price.
total_price: float = quantity * price

# TODO:
# Apply a 10% discount.
discounted_price: float = total_price * 0.90

# TODO:
# Print both results.
print(f"Total price: {total_price}")
print(f"Discounted price (10% off): {discounted_price:.3f}")

print()


# ============================================================
# Task 5 — Arithmetic Operators
# ============================================================

print("Task 5 — Arithmetic Operators")

a: int = 17
b: int = 5

# TODO:
# Print the result of each operation:
#
# a + b
# a - b
# a * b
# a / b
# a // b
# a % b
# a ** b

print(f"a + b  = {a + b}")   # Addition
print(f"a - b  = {a - b}")   # Subtraction
print(f"a * b  = {a * b}")   # Multiplication
print(f"a / b  = {a / b}")   # True division (float)
print(f"a // b = {a // b}")  # Floor division (integer)
print(f"a % b  = {a % b}")   # Modulo (remainder)
print(f"a ** b = {a ** b}")  # Exponentiation

# ============================================================
# Task 6 — Data Types
# ============================================================

print("Task 6 — Data Types")

integer_value: int = 42
float_value: float = 3.14
complex_value = 2 + 3j
text_value: str = "Python"
boolean_value: bool = True

# TODO:
# Use type() to print the type of every variable above.
#
# Example:
# print(type(integer_value))
print(f"Type of integer: {type(integer_value)}")
print(f"Type of float: {type(float_value)}")
print(f"Type of complex_value: {type(complex_value)}")
print(f"Type of string: {type(text_value)}")
print(f"Type of bool: {type(boolean_value)}")

print()


# ============================================================
# Task 7 — Comparisons and Boolean Logic
# ============================================================

print("Task 7 — Comparisons and Boolean Logic")

age: int = 22
is_master_student: bool = True

# TODO:
# Print the result of the following expressions:
#
# age >= 18
# age < 30
# age == 22
# age != 25
#
# age >= 18 and is_master_student
# age < 18 or is_master_student
# not is_master_student
#
# Predict each result before running the program.
print(f"The result of 1-st comparison: {age >= 18}") # True
print(f"The result of 2-nd comparison: {age < 30}") # True
print(f"The result of 3-rd comparison: {age == 22}") # True
print(f"The result of 4-th comparison: {age != 25}") # True
print(f"The result of 5-th comparison: {age >= 18 and is_master_student}") # True
print(f"The result of 6-th comparison: {age < 18 or is_master_student}") # True
print(f"The result of 7-th comparison: {not is_master_student}") # False

print()


# ============================================================
# Task 8 — Python Collections
# ============================================================

print("Task 8 — Python Collections")

# TODO:
# Create:
#
# 1. A list containing three programming languages.
# 2. A tuple containing three numbers.
# 3. A set containing several city names.
# 4. A dictionary describing a student with:
#       name
#       age
#       university

programming_languages: List[str] = ["Java", "Python", "C++"]
numbers: Tuple[int, ...] = (2, 3, 6)
cities: Set = set({"Novosibirsk", "Moscow", "Kazan", "Omsk", "Saint-Peterburg"})
student: Dict[str, Any] = {
    "name": "Vladimir",
    "age": 22,
    "university": "Novosibirsk State University (NSU)",
}

# TODO:
# Print all four variables.
print(f"Printing List: {programming_languages}")
print(f"Printing Tuple: {numbers}")
print(f"Printing set: {cities}")
print(f"Printing Dict: {student}")
#
# TODO:
# Use type() to print the type of each collection.
print(f"Printing type of List: {type(programming_languages)}")
print(f"Printing type of Tuple: {type(numbers)}")
print(f"Printing type of Set: {type(cities)}")
print(f"Printing type of Dict: {type(student)}")

print()


# ============================================================
# Task 9 — Indexing and Slicing
# ============================================================

print("Task 9 — Indexing and Slicing")

numbers: List[int] = [0, 1, 2, 3, 4, 5, 6, 7]

# TODO:
# Print the first element.
print(f"The first elem of List: {numbers[0]}")

# TODO:
# Print the last element.
print(f"The last elem of List: {numbers[-1]}")

# TODO:
# Print elements from index 1 up to index 4.
#
# Expected:
# [1, 2, 3]
print(f"Elements from index 1 up to index 4: {numbers[1:4]}")

# TODO:
# Print every second element.
#
# Expected:
# [0, 2, 4, 6]
print(f"Every second element of List: {numbers[0:8:2]}")

word: str = "Python"

# TODO:
# Print the first character.
print(f"The first character of String: {word[0]}")

# TODO:
# Print the last character.
print(f"The last character of String: {word[-1]}")

# TODO:
# Print:
# Pyt
print(word[:3])

print()


# ============================================================
# Task 10 — Dictionaries and Membership
# ============================================================

print("Task 10 — Dictionaries and Membership")

student: Dict[str, Any] = {
    "name": "Anna",
    "age": 22,
    "city": "Novosibirsk",
}

# TODO:
# Print the student's name.
print(f"Student's name: {student['name']}")

# TODO:
# Print the student's age.
print(f"Student's age: {student['age']}")

# TODO:
# Check whether "age" exists in the dictionary.
# Print the result.
print(f"Student's age existance: {"age" in student}")

# TODO:
# Check whether "email" exists in the dictionary.
# Print the result.
print(f"Student's email existance: {"email" in student}")

numbers: List[int] = [10, 20, 30, 40]

# TODO:
# Check whether 20 is in numbers.
print(f"20 existance in the List: {20 in numbers}")

# TODO:
# Check whether 50 is in numbers.
print(f"50 existance in the List: {50 in numbers}")


print()


# ============================================================
# Task 11 — Formatted Output
# ============================================================

print("Task 11 — Formatted Output")
import math

# TODO:
# Ask the user to enter the radius of a circle.

radius: float = float(input("Enter the radius of a circle: "))

# Use:
# area = 3.14159 * radius ** 2

area: float = math.pi * radius ** 2

# The second variant is just area: float = 3.14159 * radius ** 2

# TODO:
# Print the radius and area using an f-string.
#
# Example:
# Radius: 10.0
# Area: 314.16
#
# Print the area with exactly two digits after the decimal point.
#
# Hint:
# {value:.2f}
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")

print()


# ============================================================
# Task 12 — Trip Cost Calculator
# ============================================================

print("Task 12 — Trip Cost Calculator")

# A car consumes a certain number of liters of fuel
# for every 100 kilometers.

# TODO:
# Ask the user to enter:
#
# distance in kilometers
# fuel consumption in liters per 100 km
# fuel price per liter

distance: float = float(input("Enter the distance in kilometers: "))
fuel_consumption: float = float(input("Enter the fuel consumption in liters per 100 km: "))
fuel_price: float = float(input("Enter the fuel price per liter: "))

# TODO:
# Calculate how many liters of fuel are required.
#
# Formula:
# liters_needed = distance / 100 * fuel_consumption

liters_needed: float = (distance / 100) * fuel_consumption

# TODO:
# Calculate the total cost of the trip.

trip_cost: float = liters_needed * fuel_price

# TODO:
# Print something similar to:
#
# Distance: 450.0 km
# Fuel required: 36.00 liters
# Trip cost: 2160.00
#
# Use f-strings and two decimal places where appropriate.
print(f"Distance: {distance:.1f} km")
print(f"Fuel required: {liters_needed:.2f} liters")
print(f"Trip cost: {trip_cost:.2f}")