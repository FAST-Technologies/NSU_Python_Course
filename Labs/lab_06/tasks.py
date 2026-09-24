"""
NSU Python — Lab 06
Functions as Values: lambda, Sorting, Filtering, and map

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 06 and earlier lectures.
"""

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
