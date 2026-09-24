"""
NSU Python — Lab 06
Functions as Values: lambda, Sorting, Filtering, and map

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 06 and earlier lectures.
"""
from typing import Callable, List, Any, Tuple, Dict

# ============================================================
# Task 1 — Functions as values
# ============================================================
# Create a function:
#
#   square(number)
#
# that returns number ** 2.
#
# Then:
# 1. assign the function object to a new variable called operation;
# 2. call square(5);
# 3. call operation(5);
# 4. print whether operation is square.
#
# Expected final comparison:
# True
#
# Important:
# operation = square
# stores the function object.
#
# operation = square()
# would call the function immediately.

# Write your code below:
print("Task 1 — Functions as values")

def square(number: float) -> float:
    """Function that returns a square of number."""
    return number ** 2

operation: Callable[[float], float] = square
print(f"square(5) = {square(5)}")
print(f"operation(5) = {operation(5)}")
print(f"operation is square: {operation is square}")

print()

# ============================================================
# Task 2 — Passing a function as an argument
# ============================================================
# Create:
#
#   double(number)
#   triple(number)
#
# Then create:
#
#   apply(operation, value)
#
# apply() should call operation(value) and return the result.
#
# Examples:
# apply(double, 5) -> 10
# apply(triple, 5) -> 15
#
# Pass the function names WITHOUT parentheses.

# Write your code below:
print("Task 2 — Passing a function as an argument")

def double(number: float) -> float:
    """Function that returns a double number."""
    return number * 2

def triple(number: float) -> float:
    """Function that returns a triple number."""
    return number * 3

def apply(operation: Callable[[float], float], value: float) -> float:
    """Function that calls double or triple operation and returns the result."""
    return operation(value)

print(f"apply(double, 5) = {apply(double, 5)}")
print(f"apply(triple, 5) = {apply(triple, 5)}")

print()

# ============================================================
# Task 3 — Higher-order function
# ============================================================
# Create:
#
#   transform(values, operation)
#
# It should:
# - create an empty result list;
# - loop through values;
# - apply operation() to each value;
# - append each result;
# - return the new list.
#
# Then create:
#
#   square(number)
#
# Test:
# transform([1, 2, 3, 4], square)
#
# Expected:
# [1, 4, 9, 16]

# Write your code below:
print("Task 3 — Higher-order function")

def transform(values: List[float], operation: Callable[[float], float]) -> List[float]:
    """Function that transform a value using operations."""
    result: List[float] = []
    for value in values:
        result.append(operation(value))
    return result

print(f"transform([1, 2, 3, 4], square) = {transform([1, 2, 3, 4], square)}")

print()

# ============================================================
# Task 4 — Lambda expressions
# ============================================================
# Create these lambda functions:
#
#   double
#   add
#   is_even
#
# Requirements:
# double(5)    -> 10
# add(3, 4)    -> 7
# is_even(8)   -> True
# is_even(7)   -> False
#
# Each lambda must contain only one expression.

# Write your code below:
print("Task 4 — Lambda expressions")

double_lambda = lambda x: x * 2
add_lambda = lambda x, y: x + y
is_even_lambda = lambda x: x % 2 == 0

print(f"double_lambda(5) = {double_lambda(5)}")
print(f"add_lambda(3, 4) = {add_lambda(3, 4)}")
print(f"is_even_lambda(8) = {is_even_lambda(8)}")
print(f"is_even_lambda(7) = {is_even_lambda(7)}")

print()

# ============================================================
# Task 5 — sorted() versus list.sort()
# ============================================================
# Start with:
#
# numbers = [8, 3, 10, 1, 6]
#
# Part A:
# Use sorted() to create a NEW list called ordered.
#
# Print:
# - numbers
# - ordered
#
# Confirm that numbers did not change.
#
# Part B:
# Call numbers.sort().
# Print numbers again.
#
# Expected sorted order:
# [1, 3, 6, 8, 10]
#
# Also store the result of numbers.sort() in a variable:
#
#   result = numbers.sort()
#
# Print result.
#
# What does list.sort() return?

# Write your code below:
print("Task 5 — sorted() versus list.sort()")

numbers_5: List[int] = [8, 3, 10, 1, 6]

# Part A: sorted() creates a NEW list
ordered: List[int] = sorted(numbers_5)
print(f"Original numbers: {numbers_5}")
print(f"New ordered list: {ordered}")

# Part B: list.sort() modifies the list IN PLACE
result_sort: Any = numbers_5.sort()
print(f"Numbers after .sort(): {numbers_5}")
print(f"Result of .sort() assignment: {result_sort}")

print()

# ============================================================
# Task 6 — Descending order
# ============================================================
# Start with:
#
# scores = [82, 95, 73, 88, 61]
#
# Use sorted() with reverse=True.
#
# Store the result in:
#
#   high_to_low
#
# Expected:
# [95, 88, 82, 73, 61]
#
# The original scores list should remain unchanged.

# Write your code below:
print("Task 6 — Descending order")

scores_6: List[int] = [82, 95, 73, 88, 61]

high_to_low: List[int] = sorted(scores_6, reverse=True)
print(f"high_to_low: {high_to_low}")
print(f"Original scores (unchanged): {scores_6}")

print()

# ============================================================
# Task 7 — Sorting with key
# ============================================================
# Start with:
#
# words = ["pear", "watermelon", "fig", "banana", "kiwi"]
#
# Create:
#
#   shortest_first
#   longest_first
#
# shortest_first:
# sort by string length from shortest to longest.
#
# longest_first:
# sort by string length from longest to shortest.
#
# Use key=len for at least one of the two results.
#
# Do not manually calculate the lengths.

# Write your code below:
print("Task 7 — Sorting with key")

words: List[str] = ["pear", "watermelon", "fig", "banana", "kiwi"]

shortest_first: List[str] = sorted(words, key=len)
longest_first: List[str] = sorted(words, key=len, reverse=True)

print(f"shortest_first: {shortest_first}")
print(f"longest_first: {longest_first}")

print()

# ============================================================
# Task 8 — Case-insensitive sorting
# ============================================================
# Start with:
#
# cities = [
#     "berlin",
#     "Algiers",
#     "cairo",
#     "Amsterdam",
#     "zurich"
# ]
#
# Sort the list alphabetically without treating uppercase
# and lowercase letters as separate groups.
#
# Use:
#
#   key=str.lower
#
# Store the result in:
#
#   ordered_cities
#
# The original capitalization must stay unchanged.

# Write your code below:
print("Task 8 — Case-insensitive sorting")

cities: List[str] = ["berlin", "Algiers", "cairo", "Amsterdam", "zurich"]

ordered_cities: List[str] = sorted(cities, key=str.lower)
print(f"ordered_cities: {ordered_cities}")

print()

# ============================================================
# Task 9 — Sorting tuples with lambda
# ============================================================
# Start with:
#
# students = [
#     ("Anna", 82),
#     ("Boris", 95),
#     ("Mira", 88),
#     ("Daniel", 73)
# ]
#
# Sort students by score from highest to lowest.
#
# Use:
#
#   sorted()
#   key=lambda ...
#   reverse=True
#
# Expected first item:
# ("Boris", 95)

# Write your code below:
print("Task 9 — Sorting tuples with lambda")

students_9: List[Tuple[str, int]] = [
    ("Anna", 82),
    ("Boris", 95),
    ("Mira", 88),
    ("Daniel", 73)
]

sorted_by_score: List[Tuple[str, int]] = sorted(
    students_9, 
    key=lambda student: student[1], 
    reverse=True
)
print(f"sorted_by_score: {sorted_by_score}")

print()


# ============================================================
# Task 10 — Filtering values
# ============================================================
# Start with:
#
# scores = [45, 70, 82, 39, 91, 60, 58]
#
# Use filter() and a lambda to keep only scores >= 60.
#
# Convert the filter result to a list.
#
# Expected:
# [70, 82, 91, 60]

# Write your code below:
print("Task 10 — Filtering values")

scores_10: List[int] = [45, 70, 82, 39, 91, 60, 58]

passing_scores: List[int] = list(filter(lambda x: x >= 60, scores_10))
print(f"passing_scores: {passing_scores}")

print()

# ============================================================
# Task 11 — Transforming values with map()
# ============================================================
# Start with:
#
# prices = [100, 250, 80, 40]
#
# Use map() and a lambda to increase every price by 10%.
#
# Convert the result to a list.
#
# Expected:
# [110.0, 275.0, 88.0, 44.0]
#
# Note:
# Floating-point output may sometimes contain small
# representation differences.

# Write your code below:
print("Task 11 — Transforming values with map()")

prices: List[float] = [100, 250, 80, 40]

increased_prices: List[float] = list(map(lambda x: x * 1.10, prices))
print(f"increased_prices: {increased_prices}")

print()

# ============================================================
# Task 12 — Filter, sort, and map together
# ============================================================
# Start with:
#
# students = [
#     {"name": "Anna", "score": 82},
#     {"name": "Boris", "score": 55},
#     {"name": "Mira", "score": 91},
#     {"name": "Daniel", "score": 67},
#     {"name": "Sara", "score": 48}
# ]
#
# Step 1:
# Use filter() to keep students with score >= 60.
#
# Step 2:
# Use sorted() to order the passing students from
# highest score to lowest score.
#
# Step 3:
# Use map() to create a list containing only their names.
#
# Expected names:
# ["Mira", "Anna", "Daniel"]
#
# Use lambda expressions for the filter, sorting key,
# and map transformation.

# Write your code below:
print("Task 12 — Filter, sort, and map together")

students_12: List[Dict[str, Any]] = [
    {"name": "Anna", "score": 82},
    {"name": "Boris", "score": 55},
    {"name": "Mira", "score": 91},
    {"name": "Daniel", "score": 67},
    {"name": "Sara", "score": 48}
]

# Step 1: Filter
passed_students = list(filter(lambda s: s["score"] >= 60, students_12))

# Step 2: Sort
sorted_passed = sorted(passed_students, key=lambda s: s["score"], reverse=True)

# Step 3: Map
final_names: List[str] = list(map(lambda s: s["name"], sorted_passed))

print(f"final_names: {final_names}")

print()

# ============================================================
# Task 13 — BONUS: Sort records by multiple ideas
# ============================================================
# Start with:
#
# products = [
#     {"name": "Keyboard", "price": 70},
#     {"name": "Mouse", "price": 25},
#     {"name": "Monitor", "price": 220},
#     {"name": "USB Cable", "price": 10}
# ]
#
# Create:
#
#   by_price
#   by_name_length
#
# by_price:
# sort from cheapest to most expensive.
#
# by_name_length:
# sort by the length of the product name,
# from shortest to longest.
#
# Use lambda expressions as sorting keys.

# Write your code below:
print("Task 13 — BONUS: Sort records by multiple ideas")

products: List[Dict[str, Any]] = [
    {"name": "Keyboard", "price": 70},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 220},
    {"name": "USB Cable", "price": 10}
]

by_price: List[Dict[str, Any]] = sorted(products, key=lambda p: p["price"])
by_name_length: List[Dict[str, Any]] = sorted(products, key=lambda p: len(p["name"]))

print(f"by_price: {by_price}")
print(f"by_name_length: {by_name_length}")

print()

# ============================================================
# Task 14 — BONUS: Student ranking pipeline
# ============================================================
# Start with:
#
# students = [
#     ("Anna", 82),
#     ("Boris", 55),
#     ("Mira", 91),
#     ("Daniel", 67),
#     ("Sara", 48),
#     ("Omar", 76)
# ]
#
# Build this pipeline:
#
# 1. filter() -> keep scores >= 60
# 2. sorted() -> highest score first
# 3. map() -> convert each tuple to a string:
#
#       "Name: score"
#
# Expected:
# [
#     "Mira: 91",
#     "Anna: 82",
#     "Omar: 76",
#     "Daniel: 67"
# ]
#
# Store the final result in:
#
#   ranking
#
# Print ranking.

# Write your code below:
print("Task 14 — BONUS: Student ranking pipeline")

students_14: List[Tuple[str, int]] = [
    ("Anna", 82),
    ("Boris", 55),
    ("Mira", 91),
    ("Daniel", 67),
    ("Sara", 48),
    ("Omar", 76)
]

# 1. filter()
passed_14 = filter(lambda s: s[1] >= 60, students_14)

# 2. sorted()
sorted_14 = sorted(passed_14, key=lambda s: s[1], reverse=True)

# 3. map()
ranking: List[str] = list(map(lambda s: f"{s[0]}: {s[1]}", sorted_14))

print(f"ranking: {ranking}")

print()