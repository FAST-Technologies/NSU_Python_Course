"""
NSU Python — Lab 04
while Loops, Typing, Identity, and Functions

Complete Tasks 1–13.
Tasks 14–15 are optional bonus tasks.

Use only concepts covered in Lecture 04 and earlier lectures.
"""
from typing import List, Tuple, Optional

# ============================================================
# Task 1 — Countdown with while
# ============================================================
# Ask the user for a positive integer.
#
# Use a while loop to print from that number down to 1.
# Then print:
#   Go!
#
# Example:
# Input: 5
# Output:
# 5
# 4
# 3
# 2
# 1
# Go!
#
# Make sure the loop variable changes.

# Write your code below:
print("Task 1 — Countdown with while")
number: int = int(input("User, type a positive value: "))

if number <= 0:
    while number <= 0:
        required_number = int(input("The number is less or equal zero. Please retype it: "))

while number >= 1:
    print(number)
    number -= 1
print("Go!")

print()

# ============================================================
# Task 2 — Repeat until zero
# ============================================================
# Repeatedly ask the user to enter an integer.
#
# Stop when the user enters 0.
#
# Before 0 is entered:
#   count how many non-zero numbers were entered;
#   calculate their sum.
#
# At the end print:
#   Count: ...
#   Sum: ...
#
# Example:
# Input: 5, -2, 7, 0
# Count: 3
# Sum: 10

# Write your code below:
print("Task 2 — Repeat until zero")
counter: int = 0
total_sum: int = 0

while True:
    number: int = int(input("User, enter an integer (0 to stop): "))
    if number == 0:
        break
    counter += 1
    total_sum += number

print(f"Count: {counter}")
print(f"Sum: {total_sum}")

print()

# ============================================================
# Task 3 — Valid input with while True
# ============================================================
# Repeatedly ask the user for an integer from 1 to 10.
#
# If the value is outside this range:
#   print "Invalid value"
#   ask again.
#
# When the user enters a valid value:
#   print "Accepted"
#   stop the loop with break.
#
# Required:
# Use:
#   while True
#   break

# Write your code below:
print("Task 3 — Valid input with while True")

while True:
    value: int = int(input("User, enter an integer (from 1 to 10): "))
    if value <= 0 or value > 10:
        print("Invalid value")
    else:
        print("Accepted")
        break

print()

# ============================================================
# Task 4 — continue in a while loop
# ============================================================
# Use a while loop to process numbers from 1 through 20.
#
# Skip numbers divisible by 3 using continue.
# Print all other numbers.
#
# IMPORTANT:
# Update the loop variable correctly so you do not create
# an infinite loop.

# Write your code below:
print("Task 4 — continue in a while loop")

i: int = 1
while i <= 20:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1

print()

# ============================================================
# Task 5 — Search with loop else
# ============================================================

# Search for the first odd number.
#
# If an odd number is found:
#   print "First odd number: <value>"
#   stop using break.
#
# If the loop finishes without finding any odd number:
#   print "All values are even"
#
# Required:
# Use:
#   for
#   break
#   else

# Write your code below:
print("Task 5 — Search with loop else")
numbers: List[int] = [4, 8, 12, 16, 21, 24]
flag: bool = False

for number in numbers:
    if number % 2 == 1:
        print(f"First odd number: {number}")
        flag = True
        break

if flag is not True:
    print("All values are even")

print()


# ============================================================
# Task 6 — Multiplication table with nested loops
# ============================================================
# Use nested for loops to print a 5 x 5 multiplication table.
#
# Rows: 1 through 5
# Columns: 1 through 5
#
# Example first row:
# 1 2 3 4 5
#
# Example second row:
# 2 4 6 8 10
#
# Hint:
# Build each row using print(..., end=" ") and print().

# Write your code below:
print("Task 6 — Multiplication table with nested loops")

for rows in range(1, 6):
    for cols in range(1, 6):
        print(rows * cols, end=" ")
    print()
print()

# ============================================================
# Task 7 — Dynamic typing
# ============================================================
# Create a variable named value.
#
# First assign:
#   42
# Print the value and its type.
#
# Then assign:
#   3.14
# Print the value and its type.
#
# Then assign:
#   "Python"
# Print the value and its type.
#
# Finally assign:
#   [1, 2, 3]
# Print the value and its type.
#
# Observe that the same variable name can refer to objects
# of different types during program execution.

# Write your code below:
print("Task 7 — Dynamic typing")

value = 42
print(f"Value: {value}, type: {type(value)}")

value = 3.14
print(f"Value: {value}, Type: {type(value)}")

value = "Python"
print(f"Value: {value}, Type: {type(value)}")

value = [1, 2, 3]
print(f"Value: {value}, Type: {type(value)}")

print()

# ============================================================
# Task 8 — Equality, identity, and references
# ============================================================

# Before running the program, predict:
#
# a == b
# a is b
# a == c
# a is c
#
# Print all four results.
#
# Then print:
#   id(a)
#   id(b)
#   id(c)
#
# Finally:
#   append 30 to c
#   print a
#   print b
#   print c
#
# Explain to yourself why a changes but b does not.

# Write your code below:
print("Task 8 — Equality, identity, and references")
a: List[int] = [10, 20]
b: List[int] = [10, 20]
c: List[int] = a

print(f"a == b: {a == b}") # True  — values are equal
print(f"a is b: {a is b}") # False — разные объекты в памяти
print(f"a == c: {a == c}") # True  — values are equal
print(f"a is c: {a is c}") # True  — одна и та же ссылка

print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")

c.append(30)
print(f"a: {a}")  # [10, 20, 30] — changed, because a and c — one object
print(f"b: {b}")  # [10, 20]     — not changed, this is another object
print(f"c: {c}")  # [10, 20, 30]

print()

# ============================================================
# Task 9 — Function: is_even
# ============================================================
# Write a function:
#
#   is_even(number)
#
# It should return:
#   True  if number is even
#   False otherwise
#
# Then call it with:
#   4
#   7
#   0
#
# Print the returned results.
#
# IMPORTANT:
# The function must return the Boolean result.
# Do not print from inside the function.

# Write your code below:
print("Task 9 — Function: is_even")

def is_even(number: int) -> bool:
    """Return True if number is even, False otherwise."""
    return number % 2 == 0

print(f"is_even(4): {is_even(4)}")
print(f"is_even(7): {is_even(7)}")
print(f"is_even(0): {is_even(0)}")

print()

# ============================================================
# Task 10 — Function: calculate_discount
# ============================================================
# Write a function:
#
#   calculate_discount(price, percent)
#
# It should return the final price after the discount.
#
# Formula:
# final_price = price - price * percent / 100
#
# Test it with:
#   calculate_discount(1000, 15)
#   calculate_discount(250, 20)
#
# Print each returned result.

# Write your code below:
print("Task 10 — Function: calculate_discount")

def calculate_discount(price: float, percent: float) -> float:
    """Return the final price after the discount."""
    return price - percent * price / 100

print(f"calculate_discount(1000, 15): {calculate_discount(1000, 15)}")
print(f"calculate_discount(250, 20): {calculate_discount(250, 20)}")

print()

# ============================================================
# Task 11 — return versus print
# ============================================================
# The function below is not useful if later code needs
# to reuse the calculated value:
#
# def rectangle_area(width, height):
#     print(width * height)
#
# Rewrite it so that it RETURNS the area.
#
# Then:
#   store the result for width=5, height=4
#   print the result
#   calculate result * 2 and print it
#
# Goal:
# Demonstrate why return is different from print.

# Write your code below:
print("Task 11 — return versus print")

def rectangle_area(width: float, height: float) -> float:
    """Return the area of the rectangle."""
    return width * height

widths: float = 5
heights: float = 4
area: float = rectangle_area(widths, heights)
print(f"Area of rectangle: {area}")
area *= 2
print(f"Area of rectangle  * 2: {area}")

print()

# ============================================================
# Task 12 — Function returning multiple values
# ============================================================
# Write a function:
#
#   min_max(numbers)
#
# It receives a list of numbers.
#
# Use loops and conditions to find:
#   the minimum value
#   the maximum value
#
# Return both values.
#
# Do NOT use:
#   min()
#   max()
#
# Test with:
# values = [7, 2, 9, -1, 5, 12, 3]
#
# Unpack the result into:
#   smallest
#   largest
#
# Then print them.

# Write your code below:
print("Task 12 — Function returning multiple values")

def min_max(numbers: List[int]) -> Tuple[int, int]:
    """Return the minimum and maximum value from a List."""
    smallest: int = numbers[0]
    largest: int = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
    return smallest, largest

values: List[int] = [7, 2, 9, -1, 5, 12, 3]
min_val: int
max_val: int
min_val, max_val = min_max(values)
print(f"Smallest value: {min_val}")
print(f"Largest value: {max_val}")

print()

# ============================================================
# Task 13 — Integrated task: validated average
# ============================================================
# Write a function:
#
#   average(total, count)
#
# Rules:
#   if count == 0:
#       return None
#   otherwise:
#       return total / count
#
# Then write a loop that asks the user for count until
# the user enters a value >= 0.
#
# Ask once for total.
#
# Call average(total, count).
#
# If the returned result is None:
#   print "Cannot calculate average"
#
# Otherwise:
#   print the average with 2 decimal places.
#
# Required:
# Use:
#   function
#   while loop
#   condition
#   return
#   is None

# Write your code below:
print("Task 13 — Integrated task: validated average")

def average(total: float, count: int) -> Optional[float]:
    """Return the average result."""
    if count == 0:
        return None
    return total / count

total_input: float = float(input("Enter total: "))

while True:
    count_input: int = int(input("Enter count (>= 0): "))
    if count_input >= 0:
        break
    print("Count must be >= 0")

average_result: Optional[float] = average(total_input, count_input)
if average_result is None:
    print("Cannot calculate average")
else:
    print(f"Average: {average_result:.2f}")

print()

# ============================================================
# BONUS Task 14 — Guess the number
# ============================================================
# Use:
# secret_number = 37
#
# Repeatedly ask the user to guess the number.
#
# Print:
#   Too low
#   Too high
#   Correct
#
# Stop only when the guess is correct.
#
# Also count how many attempts were needed.
#
# Required:
# Use a while loop.

# Write your code below:
print("Task 14 — Guess the number")

secret_number: int = 37
attempts: int = 0

while True:
    guess_num: int = int(input(f"Enter your guess (attempt {attempts + 1}/inf): "))
    attempts += 1
    if guess_num < secret_number:
        print("Too low")
    elif guess_num > secret_number:
        print("Too high")
    else:
        print("Correct")
        break

print(f"Attempts needed: {attempts}")

print()

# ============================================================
# BONUS Task 15 — Function-based number statistics
# ============================================================
# Write a function:
#
#   number_statistics(numbers)
#
# It should use a loop to count:
#   positive numbers
#   negative numbers
#   zeros
#
# Return all three counts.
#
# Test with:
# data = [3, -1, 0, 8, -5, 0, 2, -9]
#
# Print:
#   Positive: ...
#   Negative: ...
#   Zero: ...
#
# Do not use list comprehensions.

# Write your code below:
print("BONUS Task 15 — Function-based number statistics")

def number_statistics(numbers: List[int]) -> Tuple[int, int, int]:
    """Return the ammount of positive, negative and zero values in a list."""
    positive_vals: int = 0
    negative_vals: int = 0
    zero_vals: int = 0
    for number in numbers:
        if number > 0:
            positive_vals += 1
        elif number < 0:
            negative_vals += 1
        else:
            zero_vals += 1
    return positive_vals, negative_vals, zero_vals

data: List[int] = [3, -1, 0, 8, -5, 0, 2, -9]
positive_count: int = 0
negative_count: int = 0
zero_count: int = 0
positive_count, negative_count, zero_count = number_statistics(data)

print(f"Positive: {positive_count}")
print(f"Negative: {negative_count}")
print(f"Zero: {zero_count}")

print()