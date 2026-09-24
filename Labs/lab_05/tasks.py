"""
NSU Python — Lab 05
Functions in Practice: Arguments, Recursion, math, and List Methods

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 05 and earlier lectures.
Do not use lambda, sorted(), filter(), or map() in this lab.
"""
import math
from typing import List, Tuple, Optional

# ============================================================
# Task 1 — Positional and keyword arguments
# ============================================================
# Create a function:
#
#   describe_student(name, age, city)
#
# The function should print:
#   Name: ...
#   Age: ...
#   City: ...
#
# Call the function three times:
# 1. using only positional arguments;
# 2. using only keyword arguments in a different order;
# 3. using one positional argument and the rest as keyword arguments.
#
# Example:
# describe_student("Anna", 23, "Novosibirsk")
#
# Output:
# Name: Anna
# Age: 23
# City: Novosibirsk

# Write your code below:
print("Task 1 — Positional and keyword arguments")

def describe_student(name: str, age: int, city: str) -> None:
    """Funtion that describes name, age and city of the student."""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

# Positional
describe_student("Anna", 23, "Novosibirsk")
print()

# Keyword (different order)
describe_student(city="Moscow", age=20, name="Boris")
print()

# Mixed (one positional, rest keyword)
describe_student("Mira", city="Omsk", age=22)
print()

# ============================================================
# Task 2 — Default arguments
# ============================================================
# Create a function:
#
#   shipping_cost(weight, rate=2.5)
#
# It should return:
#   weight * rate
#
# Call it:
# 1. with only weight;
# 2. with a custom rate;
# 3. with rate passed as a keyword argument.
#
# Example:
# shipping_cost(4)
# returns 10.0

# Write your code below:
print("Task 2 — Default arguments")

def shipping_cost(weight: float, rate: float = 2.5) -> float:
    """Funtion that returns a reswult of shipping cost."""
    return weight * rate

print(shipping_cost(4))          # Only weight
print(shipping_cost(4, 3.0))     # Custom rate (positional)
print(shipping_cost(4, rate=3.0)) # Custom rate (keyword)
print()

# ============================================================
# Task 3 — Early return
# ============================================================
# Create a function:
#
#   safe_divide(a, b)
#
# If b is 0, return None immediately.
# Otherwise return a / b.
#
# Test:
# safe_divide(10, 2)  -> 5.0
# safe_divide(10, 0)  -> None

# Write your code below:
print("Task 3 — Early return")

def safe_divide(a: float, b: float) -> Optional[float]:
    """Funtion that returns None if b is 0 and a / b otherwise."""
    if b == 0:
        return None
    return a / b

print(f"safe_divide(10, 2): {safe_divide(10, 2)}")
print(f"safe_divide(10, 0): {safe_divide(10, 0)}")
print()


# ============================================================
# Task 4 — *args: total score
# ============================================================
# Create a function:
#
#   total_score(*scores)
#
# Return the sum of all scores.
#
# The function must work with any number of arguments,
# including zero arguments.
#
# Examples:
# total_score(10, 20, 30) -> 60
# total_score(5)          -> 5
# total_score()           -> 0
#
# Inside the function, scores is a tuple.

# Write your code below:
print("Task 4 — *args: total score")

def total_score(*scores: float) -> float:
    """Funtion that returns the sum of all scores."""
    return sum(scores)

print(f"total_score(10, 20, 30): {total_score(10, 20, 30)}")
print(f"total_score(5): {total_score(5)}")
print(f"total_score(): {total_score()}")
print()

# ============================================================
# Task 5 — *args: average score
# ============================================================
# Create a function:
#
#   average_score(*scores)
#
# If no scores are given, return None.
# Otherwise return the arithmetic mean.
#
# Examples:
# average_score(80, 90, 100) -> 90.0
# average_score()             -> None

# Write your code below:
print("Task 5 — *args: average score")

def average_score(*scores: float) -> Optional[float]:
    """Funtion that returns the average score."""
    if not scores:
        return None
    return sum(scores) / len(scores)

print(f"average_score(80, 90, 100): {average_score(80, 90, 100)}")
print(f"average_score(): {average_score()}")
print()

# ============================================================
# Task 6 — **kwargs: profile
# ============================================================
# Create a function:
#
#   show_profile(**details)
#
# Print each key and value in this form:
#   key: value
#
# Example call:
# show_profile(name="Anna", city="Novosibirsk", year=1)
#
# Possible output:
# name: Anna
# city: Novosibirsk
# year: 1

# Write your code below:
print("Task 6 — **kwargs: profile")

def show_profile(**details: str | int) -> None:
    """Funtion that returns a profile of a person."""
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile(name="Anna", city="Novosibirsk", year=1)
print()

# ============================================================
# Task 7 — Combining fixed arguments, *args, and **kwargs
# ============================================================
# Create a function:
#
#   course_report(student, *scores, **options)
#
# It should print:
#   Student: ...
#   Scores: (...)
#   Options: {...}
#
# Example:
# course_report(
#     "Mira",
#     80, 92, 75,
#     rounded=True,
#     scale=100
# )
#
# Expected structure:
# Student: Mira
# Scores: (80, 92, 75)
# Options: {'rounded': True, 'scale': 100}

# Write your code below:
print("Task 7 — Combining fixed arguments, *args, and **kwargs")

def course_report(student: str, *scores: int, **options: bool | int) -> None:
    """Funtion that returns a report."""
    print(f"Student: {student}")
    print(f"Scores: {scores}")
    print(f"Options: {options}")

course_report("Mira", 80, 92, 75, rounded=True, scale=100)
print()

# ============================================================
# Task 8 — Scope
# ============================================================
# Create a global variable:
#
#   TAX_RATE = 0.20
#
# Create a function:
#
#   final_price(price)
#
# Inside the function:
# 1. calculate a LOCAL variable called tax;
# 2. return price + tax.
#
# Do not modify TAX_RATE.
#
# Example:
# final_price(100) -> 120.0
#
# Think about:
# - TAX_RATE is global.
# - tax exists only inside final_price().

# Write your code below:
print("Task 8 — Scope")

TAX_RATE: float = 0.20

def final_price(price: float) -> float:
    """Funtion that returns a final price using TAX_RATE constant."""
    tax: float = price * TAX_RATE
    return price + tax

print(f"final_price(100): {final_price(100)}")
print()

# ============================================================
# Task 9 — Recursive countdown
# ============================================================
# Create a recursive function:
#
#   countdown(n)
#
# If n == 0:
#   print("Go!")
#   stop the function.
#
# Otherwise:
#   print n
#   call countdown(n - 1)
#
# Do NOT use a loop.
#
# Example:
# countdown(3)
#
# Output:
# 3
# 2
# 1
# Go!

# Write your code below:
print("Task 9 — Recursive countdown")

def countdown(n: int) -> None:
    """Recursive countdown function."""
    if n == 0:
        print("Go!")
    else:
        print(n)
        countdown(n - 1)

countdown(3)
print()

# ============================================================
# Task 10 — Recursive factorial
# ============================================================
# Create a recursive function:
#
#   factorial(n)
#
# Rules:
# - if n < 0, return None;
# - if n == 0, return 1;
# - otherwise return n * factorial(n - 1).
#
# Do NOT use a loop.
#
# Examples:
# factorial(5)  -> 120
# factorial(0)  -> 1
# factorial(-2) -> None

# Write your code below:
print("Task 10 — Recursive factorial")

def factorial(n: int) -> Optional[int]:
    """Recursive factorial function."""
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5): {factorial(5)}")
print(f"factorial(0): {factorial(0)}")
print(f"factorial(-2): {factorial(-2)}")
print()


# ============================================================
# Task 11 — Recursive sum
# ============================================================
# Create a recursive function:
#
#   sum_to(n)
#
# It should return:
#   1 + 2 + 3 + ... + n
#
# Rules:
# - if n < 0, return None;
# - if n == 0, return 0;
# - otherwise use recursion.
#
# Do NOT use a loop and do NOT use sum().
#
# Examples:
# sum_to(4) -> 10
# sum_to(0) -> 0

# Write your code below:
print("Task 11 — Recursive sum")

def sum_to(n: int) -> Optional[int]:
    """Recursive sum function."""
    if n < 0:
        return None
    if n == 0:
        return 0
    return n + sum_to(n - 1)

print(f"sum_to(4): {sum_to(4)}")
print(f"sum_to(0): {sum_to(0)}")
print()

# ============================================================
# Task 12 — math module and list methods
# ============================================================
# Part A — math
#
# Import math.
#
# Ask the user for the radius of a circle.
# Calculate and print:
# - circumference = 2 * math.pi * radius
# - area = math.pi * radius ** 2
# - area rounded UP with math.ceil()
# - area rounded DOWN with math.floor()
#
# Example for radius 3:
# Circumference: 18.849...
# Area: 28.274...
# Area ceil: 29
# Area floor: 28
#
#
# Part B — list methods
#
# Start with:
# numbers = [10, 20, 20, 30]
#
# Perform these operations in order:
# 1. append 40
# 2. extend with [50, 60]
# 3. insert 15 at index 1
# 4. print how many times 20 appears
# 5. print the index of the first 30
# 6. remove the first 20
# 7. pop the last item and save it in removed
# 8. print numbers
# 9. print removed
#
# Do not use sorted() in this task.

# Write your code below:
print("Task 12 — math module and list methods")

# Part A
radius: float = float(input("Enter the radius of a circle: "))
circumference: float = 2 * math.pi * radius
area: float = math.pi * (radius ** 2)

print(f"Circumference: {circumference:.5f}")
print(f"Area: {area:.5f}")
print(f"Area ceil: {math.ceil(area)}")
print(f"Area floor: {math.floor(area)}")

# Part B
numbers_12: List[int] = [10, 20, 20, 30]
numbers_12.append(40)
numbers_12.extend([50, 60])
numbers_12.insert(1, 15)
print(f"Count of 20: {numbers_12.count(20)}")
print(f"Index of first 30: {numbers_12.index(30)}")
numbers_12.remove(20)
removed_12: int = numbers_12.pop()
print(f"Numbers: {numbers_12}")
print(f"Removed: {removed_12}")
print()

# ============================================================
# Task 13 — BONUS: Recursive digit sum
# ============================================================
# Create a recursive function:
#
#   digit_sum(n)
#
# Assume n is a non-negative integer.
#
# Return the sum of its digits.
#
# Hint:
# - last digit: n % 10
# - remaining digits: n // 10
#
# Base case:
# if n < 10, return n
#
# Examples:
# digit_sum(1234) -> 10
# digit_sum(7)    -> 7
#
# Do NOT convert the number to a string.
# Do NOT use a loop.

# Write your code below:
print("Task 13 — BONUS: Recursive digit sum")

def digit_sum(n: int) -> int:
    """Recursive digital sum function."""
    if n < 10:
        return n
    return (n % 10) + digit_sum(n // 10)

print(f"digit_sum(1234): {digit_sum(1234)}")
print(f"digit_sum(7): {digit_sum(7)}")
print()

# ============================================================
# Task 14 — BONUS: Student result summary
# ============================================================
# Create a function:
#
#   result_summary(name, *scores, passing=60)
#
# Requirements:
# - if no scores are given, return:
#     "No scores"
# - calculate the average;
# - count how many scores are >= passing;
# - return a string in this form:
#
#   "Anna: average=80.0, passed=3/4"
#
# Example:
# result_summary("Anna", 80, 70, 50, 120, passing=60)
#
# returns:
# "Anna: average=80.0, passed=3/4"
#
# Use a loop to count passed scores.
# Do not use filter() or map().

# Write your code below:
print("Task 14 — BONUS: Student result summary")

def result_summary(name: str, *scores: float, passing: float = 60) -> str:
    """Returns a string of summary result."""
    if not scores:
        return "No scores"
    
    avg: float = sum(scores) / len(scores)
    passed_count: int = 0
    for score in scores:
        if score >= passing:
            passed_count += 1
            
    return f"{name}: average={avg}, passed={passed_count}/{len(scores)}"

print(result_summary("Anna", 80, 70, 50, 120, passing=60))
print()

# ============================================================
# Task 15 — Function with validation
# ============================================================
# Create a function:
#
#   calculate_discount(price, discount=10)
#
# Requirements:
# - price must be greater than 0;
# - discount must be between 0 and 100.
#
# If the values are invalid, return None.
#
# Otherwise return the final price after applying the discount.
#
# Formula:
# final_price = price - price * discount / 100
#
# Examples:
# calculate_discount(100)     -> 90.0
# calculate_discount(200, 25) -> 150.0
# calculate_discount(100, 120) -> None
# calculate_discount(-20, 10)  -> None

# Write your code below:
print("Task 15 — Function with validation")

def calculate_discount(price: float, discount: float = 10) -> Optional[float]:
    """Returns a calculated discount or None otherwise."""
    if price <= 0 or discount < 0 or discount > 100:
        return None
    return price - (price * discount / 100)

print(f"calculate_discount(100): {calculate_discount(100)}")
print(f"calculate_discount(200, 25): {calculate_discount(200, 25)}")
print(f"calculate_discount(100, 120): {calculate_discount(100, 120)}")
print(f"calculate_discount(-20, 10): {calculate_discount(-20, 10)}")
print()

# ============================================================
# Task 16 — Minimum and maximum with *args
# ============================================================
# Create a function:
#
#   score_range(*scores)
#
# If no scores are given, return None.
#
# Otherwise return the difference between
# the largest and smallest score.
#
# Do NOT use max() or min().
#
# Use a loop to find the smallest and largest values.
#
# Examples:
# score_range(10, 30, 20, 50) -> 40
# score_range(5)               -> 0
# score_range()                -> None

# Write your code below:
print("Task 16 — Minimum and maximum with *args")

def score_range(*scores: float) -> Optional[float]:
    """Returns score range result."""
    if not scores:
        return None
    
    smallest: float = scores[0]
    largest: float = scores[0]
    for score in scores:
        if score < smallest:
            smallest = score
        if score > largest:
            largest = score
            
    return largest - smallest

print(f"score_range(10, 30, 20, 50): {score_range(10, 30, 20, 50)}")
print(f"score_range(5): {score_range(5)}")
print(f"score_range(): {score_range()}")
print()

# ============================================================
# Task 17 — Count values above a limit
# ============================================================
# Create a function:
#
#   count_above(limit, *numbers)
#
# Return how many numbers are greater than limit.
#
# Examples:
# count_above(10, 5, 12, 30, 7, 20) -> 3
# count_above(100, 10, 20, 30)       -> 0
# count_above(5)                      -> 0
#
# Use a loop.

# Write your code below:
print("Task 17 — Count values above a limit")

def count_above(limit: float, *numbers: float) -> int:
    """Returns how many numbers are greater than limit."""
    count: int = 0
    for num in numbers:
        if num > limit:
            count += 1
    return count

print(f"count_above(10, 5, 12, 30, 7, 20): {count_above(10, 5, 12, 30, 7, 20)}")
print(f"count_above(100, 10, 20, 30): {count_above(100, 10, 20, 30)}")
print(f"count_above(5): {count_above(5)}")
print()

# ============================================================
# Task 18 — **kwargs: configuration
# ============================================================
# Create a function:
#
#   show_settings(**settings)
#
# If no settings are given, print:
#   No settings
#
# Otherwise print each setting:
#
#   key = value
#
# Example:
#
# show_settings(
#     language="Python",
#     version=3.12,
#     debug=True
# )
#
# Possible output:
# language = Python
# version = 3.12
# debug = True

# Write your code below:
print("Task 18 — **kwargs: configuration")

def show_settings(**settings: str | int | bool) -> None:
    """Returns the settings."""
    if not settings:
        print("No settings")
    else:
        for key, value in settings.items():
            print(f"{key} = {value}")

show_settings(language="Python", version=3.12, debug=True)
print()

# ============================================================
# Task 19 — math: distance between two points
# ============================================================
# Create a function:
#
#   distance(x1, y1, x2, y2)
#
# Calculate the Euclidean distance between two points.
#
# Formula:
#
# distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
#
# Use math.sqrt().
#
# Example:
# distance(0, 0, 3, 4) -> 5.0
#
# Import math.

# Write your code below:
print("Task 19 — math: distance between two points")

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Returns the Euclidean distance between 2 points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"distance(0, 0, 3, 4): {distance(0, 0, 3, 4)}")
print()

# ============================================================
# Task 20 — List operations: shopping list
# ============================================================
# Start with:
#
# shopping = ["bread", "milk", "eggs"]
#
# Perform these operations in order:
#
# 1. append "rice"
# 2. insert "coffee" at index 1
# 3. extend the list with ["tea", "sugar"]
# 4. remove "milk"
# 5. print the index of "eggs"
# 6. print how many times "bread" appears
# 7. pop the last item and store it in removed_item
# 8. print the final shopping list
# 9. print removed_item
#
# Expected final list:
# ["bread", "coffee", "eggs", "rice", "tea"]

# Write your code below:
print("Task 20 — List operations: shopping list")

shopping: List[str] = ["bread", "milk", "eggs"]
shopping.append("rice")
shopping.insert(1, "coffee")
shopping.extend(["tea", "sugar"])
shopping.remove("milk")
print(f"Index of 'eggs': {shopping.index('eggs')}")
print(f"Count of 'bread': {shopping.count('bread')}")
removed_item: str = shopping.pop()
print(f"Final shopping list: {shopping}")
print(f"Removed item: {removed_item}")
print()


# ============================================================
# Task 21 — CHALLENGE: Recursive power
# ============================================================
# Create a recursive function:
#
#   power(base, exponent)
#
# Assume exponent is a non-negative integer.
#
# Rules:
# - if exponent == 0, return 1;
# - otherwise:
#
#     base^exponent =
#     base * base^(exponent - 1)
#
# Examples:
# power(2, 5)  -> 32
# power(3, 3)  -> 27
# power(10, 0) -> 1
#
# Do NOT use **.
# Do NOT use math.pow().
# Do NOT use a loop.

# Write your code below:
print("Task 21 — CHALLENGE: Recursive power")

def power(base: float, exponent: int) -> float:
    """Recursive function that returns the power of the value."""
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(f"power(2, 5): {power(2, 5)}")
print(f"power(3, 3): {power(3, 3)}")
print(f"power(10, 0): {power(10, 0)}")
print()


# ============================================================
# Task 22 — CHALLENGE: Recursive digit counter
# ============================================================
# Create a recursive function:
#
#   count_digits(n)
#
# Assume n is a non-negative integer.
#
# Return the number of digits in n.
#
# Examples:
# count_digits(7)     -> 1
# count_digits(1234)  -> 4
# count_digits(10000) -> 5
#
# Hint:
# Remove the last digit with:
#
#   n // 10
#
# Base case:
# if n < 10:
#     return 1
#
# Do NOT convert n to a string.
# Do NOT use a loop.

# Write your code below:
print("Task 22 — CHALLENGE: Recursive digit counter")

def count_digits(n: int) -> int:
    """Recursive function that returns the number of digits."""
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(f"count_digits(7): {count_digits(7)}")
print(f"count_digits(1234): {count_digits(1234)}")
print(f"count_digits(10000): {count_digits(10000)}")
print()

# ============================================================
# Task 23 — CHALLENGE: Recursive list sum
# ============================================================
# Create a recursive function:
#
#   recursive_sum(numbers)
#
# Return the sum of all numbers in the list.
#
# Examples:
# recursive_sum([10, 20, 30]) -> 60
# recursive_sum([5])          -> 5
# recursive_sum([])           -> 0
#
# Hint:
#
# Base case:
# if the list is empty:
#     return 0
#
# Recursive idea:
#
# first element + sum of the remaining elements
#
# Do NOT use:
# - sum()
# - for
# - while

# Write your code below:
print("Task 23 — CHALLENGE: Recursive list sum")

def recursive_sum(numbers: List[float]) -> float:
    """Recursive function that returns the sum of all numbers in the list."""
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

print(f"recursive_sum([10, 20, 30]): {recursive_sum([10, 20, 30])}")
print(f"recursive_sum([5]): {recursive_sum([5])}")
print(f"recursive_sum([]): {recursive_sum([])}")
print()

# ============================================================
# Task 24 — CHALLENGE: Exam statistics
# ============================================================
# Create a function:
#
#   exam_statistics(student, *scores, passing=60)
#
# If no scores are provided, return:
#
#   "No scores"
#
# Otherwise calculate:
#
# - average score
# - highest score
# - lowest score
# - number of passed scores
# - number of failed scores
#
# Do NOT use:
# - min()
# - max()
# - sum()
#
# Calculate everything using a loop.
#
# Return a string like:
#
# "Anna: average=72.5, highest=90, lowest=50,
#  passed=3, failed=1"
#
# Example:
#
# exam_statistics(
#     "Anna",
#     80, 70, 50, 90,
#     passing=60
# )
#
# returns:
#
# "Anna: average=72.5, highest=90, lowest=50,
#  passed=3, failed=1"

# Write your code below:
print("Task 24 — CHALLENGE: Exam statistics")

def exam_statistics(student: str, *scores: float, passing: float = 60) -> str:
    """Function that returns the average/hisgest/lowest score and number of passed / failed scores of list."""
    if not scores:
        return "No scores"
    
    total: float = 0
    highest: float = scores[0]
    lowest: float = scores[0]
    passed: int = 0
    failed: int = 0
    
    for score in scores:
        total += score
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
        if score >= passing:
            passed += 1
        else:
            failed += 1
            
    avg: float = total / len(scores)
    return f"{student}: average={avg}, highest={highest}, lowest={lowest}, passed={passed}, failed={failed}"

print(exam_statistics("Anna", 80, 70, 50, 90, passing=60))
print()

# ============================================================
# Task 25 — Function with multiple return values
# ============================================================
# Create a function:
#
#   min_max(numbers)
#
# The function should return TWO values:
# - the smallest number
# - the largest number
#
# Do NOT use min() or max().
#
# Example:
# smallest, largest = min_max([5, 2, 9, 1, 7])
#
# smallest -> 1
# largest  -> 9
#
# Assume the list is not empty.

# Write your code below:
print("Task 25 — Function with multiple return values")

def min_max(numbers: List[float]) -> Tuple[float, float]:
    """Function that returns the tuple of min and max values."""
    smallest: float = numbers[0]
    largest: float = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

smallest, largest = min_max([5, 2, 9, 1, 7])
print(f"smallest: {smallest}")
print(f"largest: {largest}")
print()

# ============================================================
# Task 26 — Temperature converter
# ============================================================
# Create a function:
#
#   convert_temperature(value, unit="C")
#
# If unit == "C":
#   convert Celsius to Fahrenheit.
#
# Formula:
# F = C * 9 / 5 + 32
#
# If unit == "F":
#   convert Fahrenheit to Celsius.
#
# Formula:
# C = (F - 32) * 5 / 9
#
# For any other unit, return None.
#
# Examples:
# convert_temperature(0)       -> 32.0
# convert_temperature(100)     -> 212.0
# convert_temperature(32, "F") -> 0.0
# convert_temperature(10, "K") -> None

# Write your code below:
print("Task 26 — Temperature converter")

def convert_temperature(value: float, unit: str = "C") -> Optional[float]:
    """Function that converts Celsius to Fahrenheit or converts Fahrenheit to Celsius."""
    result: Optional[float]
    if unit == "C":
        result = value * 9 / 5 + 32
    elif unit == "F":
        result = (value - 32) * 5 / 9
    else:
        result = None
    return result

print(f"convert_temperature(0): {convert_temperature(0)}")
print(f"convert_temperature(100): {convert_temperature(100)}")
print(f"convert_temperature(32, 'F'): {convert_temperature(32, 'F')}")
print(f"convert_temperature(10, 'K'): {convert_temperature(10, 'K')}")
print()


# ============================================================
# Task 27 — Find a value manually
# ============================================================
# Create a function:
#
#   find_value(numbers, target)
#
# Return the index of the FIRST occurrence of target.
#
# If target does not exist, return -1.
#
# Do NOT use:
# - list.index()
#
# Examples:
# find_value([10, 20, 30, 20], 20) -> 1
# find_value([1, 2, 3], 5)          -> -1

# Write your code below:
print("Task 27 — Find a value manually")

def find_value(numbers: List[int], target: int) -> int:
    """Function that return the index of the FIRST occurrence of target."""
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

print(f"find_value([10, 20, 30, 20], 20): {find_value([10, 20, 30, 20], 20)}")
print(f"find_value([1, 2, 3], 5): {find_value([1, 2, 3], 5)}")
print()


# ============================================================
# Task 28 — Remove all occurrences
# ============================================================
# Create a function:
#
#   remove_all(numbers, value)
#
# Remove ALL occurrences of value from the list.
#
# Example:
#
# numbers = [10, 20, 20, 30, 20]
# remove_all(numbers, 20)
#
# numbers becomes:
# [10, 30]
#
# You may use:
# - while
# - remove()
# - count()
#
# Do NOT create a new list.

# Write your code below:
print("Task 28 — Remove all occurrences")

def remove_all(numbers: List[int], value: int) -> None:
    """Function that removes ALL occurrences of value from the list."""
    while value in numbers:
        numbers.remove(value)

nums_28: list[int] = [10, 20, 20, 30, 20]
remove_all(nums_28, 20)
print(f"nums_28 after remove_all: {nums_28}")
print()


# ============================================================
# Task 29 — Recursive multiplication
# ============================================================
# Create a recursive function:
#
#   multiply(a, b)
#
# Assume:
# - a is an integer
# - b is a non-negative integer
#
# Calculate a * b using addition and recursion.
#
# Do NOT use the * operator for multiplication.
# Do NOT use loops.
#
# Idea:
#
# a * 4 = a + a + a + a
#
# Base case:
# if b == 0:
#     return 0
#
# Examples:
# multiply(5, 3)  -> 15
# multiply(10, 0) -> 0
# multiply(-2, 4) -> -8

# Write your code below:
print("Task 29 — Recursive multiplication")

def multiply(a: int, b: int) -> int:
    """Recursive function that multiply numbers."""
    if b == 0:
        return 0
    return a + multiply(a, b - 1)

print(f"multiply(5, 3): {multiply(5, 3)}")
print(f"multiply(10, 0): {multiply(10, 0)}")
print(f"multiply(-2, 4): {multiply(-2, 4)}")
print()


# ============================================================
# Task 30 — Recursive Fibonacci
# ============================================================
# Create a recursive function:
#
#   fibonacci(n)
#
# Rules:
# fibonacci(0) -> 0
# fibonacci(1) -> 1
#
# For n > 1:
#
# fibonacci(n) =
#     fibonacci(n - 1) + fibonacci(n - 2)
#
# Examples:
# fibonacci(0) -> 0
# fibonacci(1) -> 1
# fibonacci(6) -> 8
#
# Do NOT use loops inside the function.

# Write your code below:
print("Task 30 — Recursive Fibonacci")

def fibonacci(n: int) -> int:
    """Recursive function that findes a fibonacci number."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"fibonacci(0): {fibonacci(0)}")
print(f"fibonacci(1): {fibonacci(1)}")
print(f"fibonacci(6): {fibonacci(6)}")
print()

# ============================================================
# Task 31 — math: hypotenuse
# ============================================================
# Create a function:
#
#   hypotenuse(a, b)
#
# Return the length of the hypotenuse of a
# right triangle.
#
# Formula:
#
# c = sqrt(a^2 + b^2)
#
# Use math.sqrt().
#
# If a <= 0 or b <= 0:
#     return None
#
# Examples:
# hypotenuse(3, 4)  -> 5.0
# hypotenuse(5, 12) -> 13.0
# hypotenuse(-3, 4) -> None

# Write your code below:
print("Task 31 — math: hypotenuse")

def hypotenuse(a: float, b: float) -> Optional[float]:
    """Function that returns the length of the hypotenuse of a right triangle."""
    if a <= 0 or b <= 0:
        return None
    return math.sqrt(a ** 2 + b ** 2)

print(f"hypotenuse(3, 4): {hypotenuse(3, 4)}")
print(f"hypotenuse(5, 12): {hypotenuse(5, 12)}")
print(f"hypotenuse(-3, 4): {hypotenuse(-3, 4)}")
print()


# ============================================================
# Task 32 — Function that modifies a list
# ============================================================
# Create a function:
#
#   add_student(students, name)
#
# The function should append name to students.
#
# It should NOT return the list.
#
# Example:
#
# students = ["Anna", "Alex"]
#
# result = add_student(students, "Mira")
#
# print(students)
# print(result)
#
# Output:
#
# ['Anna', 'Alex', 'Mira']
# None
#
# Think about:
# - lists are mutable;
# - the function changes the original list;
# - a function without return returns None.

# Write your code below:
print("Task 32 — Function that modifies a list")

def add_student(students: List[str], name: str) -> None:
    """Function that adds student to the list."""
    students.append(name)
    # No return statement, so it implicitly returns None

students_32: List[str] = ["Anna", "Alex"]
result_32 = add_student(students_32, "Mira")
print(f"students_32: {students_32}")
print(f"result_32: {result_32}")
print()

# ============================================================
# Task 33 — Return versus print
# ============================================================
# Create TWO functions:
#
#   square_print(n)
#   square_return(n)
#
# square_print(n):
# - prints n ** 2
# - does not explicitly return anything
#
# square_return(n):
# - returns n ** 2
#
# Then run:
#
# a = square_print(5)
# b = square_return(5)
#
# print(a)
# print(b)
#
# Explain the difference between the outputs.
#
# This task is especially about understanding:
#
# print(...)
#
# versus
#
# return ...

# Write your code below:
print("Task 33 — Return versus print")

def square_print(n: float) -> None:
    """Function that prints a square of number."""
    print(n ** 2)

def square_return(n: float) -> float:
    """Function that returns a square of number."""
    return n ** 2

a = square_print(5)
b = square_return(5)

print(f"a (from square_print): {a}")
print(f"b (from square_return): {b}")
# Explanation: 'a' is None because square_print only prints and doesn't return a value.
# 'b' is 25.0 because square_return explicitly returns the calculated value.
print()


# ============================================================
# Task 34 — Empty return
# ============================================================
# Create a function:
#
#   check_age(age)
#
# If age < 0:
#     print("Invalid age")
#     return
#
# Otherwise:
#     print("Valid age")
#
# Test:
#
# result1 = check_age(-5)
# result2 = check_age(20)
#
# Print result1 and result2.
#
# Question:
# What value does the function return in both cases?
#
# Remember:
#
# return
#
# is equivalent to:
#
# return None

# Write your code below:
print("Task 34 — Empty return")

def check_age(age: int) -> None:
    """Function that validates an age of student."""
    if age < 0:
        print("Invalid age")
        return  # Equivalent to return None
    print("Valid age")

result1 = check_age(-5)
result2 = check_age(20)

print(f"result1: {result1}")
print(f"result2: {result2}")
# Explanation: Both return None. The first exits early, the second reaches the end of the function.
print()

# ============================================================
# Task 35 — Number statistics with *args
# ============================================================
# Create a function:
#
#   number_statistics(*numbers)
#
# If no numbers are provided:
#     return None
#
# Otherwise calculate:
# - total
# - average
# - smallest
# - largest
#
# Do NOT use:
# - sum()
# - min()
# - max()
#
# Return all four values.
#
# Example:
#
# total, average, smallest, largest = \
#     number_statistics(5, 10, 2, 13)
#
# Results:
# total    -> 30
# average  -> 7.5
# smallest -> 2
# largest  -> 13

# Write your code below:
print("Task 35 — Number statistics with *args")

def number_statistics(*numbers: float) -> Optional[Tuple[float, float, float, float]]:
    """Function that returns the number statistics."""
    if not numbers:
        return None
    
    total: float = 0
    smallest: float = numbers[0]
    largest: float = numbers[0]
    
    for num in numbers:
        total += num
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
            
    average: float = total / len(numbers)
    return total, average, smallest, largest

total, average, smallest, largest = number_statistics(5, 10, 2, 13)
print(f"total: {total}")
print(f"average: {average}")
print(f"smallest: {smallest}")
print(f"largest: {largest}")
print()

# ============================================================
# Task 36 — Recursive sum of list elements
# ============================================================
# Create:
#
#   recursive_sum(numbers)
#
# Examples:
#
# recursive_sum([1, 2, 3, 4]) -> 10
# recursive_sum([10])         -> 10
# recursive_sum([])           -> 0
#
# Use recursion only.
#
# Do NOT use:
# - sum()
# - for
# - while
#
# Hint:
#
# [1, 2, 3, 4]
#
# can be thought of as:
#
# 1 + sum([2, 3, 4])

# Write your code below:
print("Task 36 — Recursive sum of list elements")

def recursive_sum_36(numbers: List[float]) -> float:
    """Recursive function that finds sum of list numbers."""
    if not numbers:
        return 0
    return numbers[0] + recursive_sum_36(numbers[1:])

print(f"recursive_sum_36([1, 2, 3, 4]): {recursive_sum_36([1, 2, 3, 4])}")
print(f"recursive_sum_36([10]): {recursive_sum_36([10])}")
print(f"recursive_sum_36([]): {recursive_sum_36([])}")
print()

# ============================================================
# Task 37 — Reverse a list using list methods
# ============================================================
# Create a function:
#
#   reverse_list(numbers)
#
# Reverse the list IN PLACE using:
#
#   .reverse()
#
# The function should not explicitly return anything.
#
# Example:
#
# numbers = [1, 2, 3, 4]
#
# result = reverse_list(numbers)
#
# print(numbers)
# print(result)
#
# Output:
#
# [4, 3, 2, 1]
# None

# Write your code below:
print("Task 37 — Reverse a list using list methods")

def reverse_list(numbers: List[int]) -> None:
    """Function that reverses a list using list methods."""
    numbers.reverse()
    # No return statement

numbers_37: List[int] = [1, 2, 3, 4]
result_37 = reverse_list(numbers_37)
print(f"numbers_37: {numbers_37}")
print(f"result_37: {result_37}")
print()

# ============================================================
# Task 38 — Math: nearest integer
# ============================================================
# Import math.
#
# Create a function:
#
#   rounding_report(number)
#
# Print:
#
# Original: ...
# Floor: ...
# Ceil: ...
#
# Example:
#
# rounding_report(4.7)
#
# Output:
#
# Original: 4.7
# Floor: 4
# Ceil: 5
#
# Test also:
#
# rounding_report(-4.7)
#
# Pay attention to how floor() behaves
# with negative numbers.

# Write your code below:
print("Task 38 — Math: nearest integer")

def rounding_report(number: float) -> None:
    """Function that rounds a number using floor and ceil methods."""
    print(f"Original: {number}")
    print(f"Floor: {math.floor(number)}")
    print(f"Ceil: {math.ceil(number)}")

rounding_report(4.7)
print()
rounding_report(-4.7)
print()