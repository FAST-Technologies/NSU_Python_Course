"""
NSU Python — Lab 03
Conditions and for Loops

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 03.
"""
from typing import List, Dict

# ============================================================
# Task 1 — Positive, negative, or zero
# ============================================================
# Ask the user to enter an integer.
# Print exactly one of:
#   Positive
#   Negative
#   Zero
#
# Example:
# Input: -7
# Output: Negative

# Write your code below:
print("Task 1 — Positive, negative, or zero")

num: int = int(input("Enter an integer: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print()

# ============================================================
# Task 2 — Age category
# ============================================================
# Ask the user for their age.
#
# Print:
#   Child      -> age < 13
#   Teenager   -> 13–17
#   Adult      -> 18–64
#   Senior     -> 65 or older
#
# Test boundary values: 12, 13, 17, 18, 64, 65.

# Write your code below:
print("Task 2 — Age category")

age: int = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 17:
    print("Teenager")
elif 18 <= age <= 64:
    print("Adult")
else:
    print("Senior")

print()

# ============================================================
# Task 3 — Grade classifier
# ============================================================
# Ask the user for a score.
#
# First check whether the score is between 0 and 100 inclusive.
#
# For a valid score:
#   A    -> 90–100
#   B    -> 75–89
#   C    -> 60–74
#   Fail -> below 60
#
# For an invalid score print:
#   Invalid score

# Write your code below:
print("Task 3 — Grade classifier")

score: float = float(input("Enter a score: "))

if 0 <= score <= 100:
    if score >= 90:
        print("A")
    elif score >= 75:
        print("B")
    elif score >= 60:
        print("C")
    else:
        print("Fail")
else:
    print("Invalid score")

print()

# ============================================================
# Task 4 — Access decision
# ============================================================
# Ask the user for:
#   age
#   whether they have a ticket: yes/no
#
# A person may enter only if:
#   age >= 18 AND they have a ticket.
#
# Print one of:
#   Access granted
#   Ticket required
#   Must be 18 or older

# Write your code below:
print("Task 4 — Access decision")

user_age: int = int(input("Enter your age: "))
has_ticket: str = input("Do you have a ticket? (yes/no): ").strip().lower()

if user_age < 18:
    print("Must be 18 or older")
elif has_ticket == "yes":
    print("Access granted")
else:
    print("Ticket required")

print()

# ============================================================
# Task 5 — Even numbers with range()
# ============================================================
# Print all even numbers from 2 through 30.
#
# Required:
# Use range(start, stop, step).

# Write your code below:
print("Task 5 — Even numbers with range()")

for i in range(2, 31, 2):
    print(i)

print()

# ============================================================
# Task 6 — Sum of multiples of 3
# ============================================================
# Calculate and print the sum of all multiples of 3
# from 3 through 99.
#
# Required:
# Use a for loop and an accumulator.
#
# Expected result:
# 1683

# Write your code below:
print("Task 6 — Sum of multiples of 3")

total_sum: int = 0
for i in range(3, 100, 3):
    total_sum += i

print(total_sum)

print()

# ============================================================
# Task 7 — Count number categories
# ============================================================
print("Task 7 — Count number categories")
numbers: List[int] = [4, -2, 0, 7, -5, 9, 0, -1, 8]

# Count how many values are:
#   positive
#   negative
#   zero
#
# Print all three counts.
# Do not manually count the values.

# Write your code below:
positive_count: int = 0
negative_count: int = 0
zero_count: int = 0

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Positive: {positive_count}")
print(f"Negative: {negative_count}")
print(f"Zero: {zero_count}")

print()

# ============================================================
# Task 8 — Count vowels
# ============================================================
# Ask the user to enter a word or short text.
# Count how many vowels it contains.
#
# Treat uppercase and lowercase equally.
# Vowels: a e i o u
#
# Example:
# Input: Artificial Intelligence
# Output: 10
#
# Hint:
# Iterate directly over the string.

# Write your code below:
print("Task 8 — Count vowels")

text: str = input("Enter a word or short text: ")
vowel_count: int = 0
vowels: str = "aeiouAEIOU"

for char in text:
    if char in vowels:
        vowel_count += 1

print(vowel_count)

print()

# ============================================================
# Task 9 — Student results
# ============================================================
print("Task 9 — Student results")

scores: List[int] = [85, 42, 67, 91, 58, 73, 100, 39]

# Count:
#   passed students: score >= 60
#   failed students: score < 60
#
# Also print the average score.
#
# Required:
# Use a loop to calculate the total.
#
# Expected:
# Passed: 5
# Failed: 3
# Average: 69.38

# Write your code below:
passed_count: int = 0
failed_count: int = 0
total_score: float = 0.0

for s in scores:
    total_score += s
    if s >= 60:
        passed_count += 1
    else:
        failed_count += 1

average_score: float = total_score / len(scores)

print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Average: {average_score:.2f}")

print()

# ============================================================
# Task 10 — Search and stop
# ============================================================
# Ask the user for a name.
# Search the list using a for loop.
#
# If found:
#   print "Found"
#   stop immediately with break
#
# If not found:
#   print "Not found"
#
# Do not use:
#   if target in names
#
# Hint:
# A Boolean variable such as found = False can help.

# Write your code below:
print("Task 10 — Search and stop")

names: List[str] = ["Anna", "Boris", "Sasha", "Maria", "Oleg", "Dina"]
target_name: str = input("Enter a name to search: ")

found: bool = False

for name in names:
    if name == target_name:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")

print()

# ============================================================
# Task 11 — Skip invalid scores
# ============================================================
# Valid scores are from 0 to 100 inclusive.
#
# Use continue to skip invalid scores.
# For valid scores:
#   print each valid score
#   calculate the average of valid scores
#
# At the end print:
#   Valid scores: ...
#   Average: ...
#
# Required:
# Use continue.

# Write your code below:
print("Task 11 — Skip invalid scores")

raw_scores: List[int] = [78, -5, 91, 120, 66, 0, 88, 101, 54]

valid_count: int = 0
valid_sum: int = 0

for s in raw_scores:
    if s < 0 or s > 100:
        continue
    
    print(s)
    valid_sum += s
    valid_count += 1

average_valid: float = valid_sum / valid_count if valid_count > 0 else 0.0

print(f"Valid scores: {valid_count}")
print(f"Average: {average_valid:.2f}")

print()

# ============================================================
# Task 12 — Dictionary iteration
# ============================================================
print("Task 12 — Dictionary iteration")
student_scores: Dict[str, int] = {
    "Anna": 92,
    "Boris": 58,
    "Sasha": 76,
    "Maria": 49,
    "Oleg": 84,
}

# Iterate using .items().
#
# Print:
#   Anna: Pass
#   Boris: Fail
#   ...
#
# Score >= 60 means Pass.
# Then print how many students passed.

# Write your code below:
passed_students: int = 0

for name, score in student_scores.items():
    if score >= 60:
        print(f"{name}: Pass")
        passed_students += 1
    else:
        print(f"{name}: Fail")

print(f"Total passed: {passed_students}")

print()

# ============================================================
# BONUS Task 13 — FizzBuzz
# ============================================================
# Print numbers 1 through 30.
#
# If divisible by both 3 and 5 -> FizzBuzz
# If divisible only by 3       -> Fizz
# If divisible only by 5       -> Buzz
# Otherwise print the number.
#
# Hint:
# Check the most specific condition first.

# Write your code below:
print("Task 13 — FizzBuzz")

for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

print()

# ============================================================
# BONUS Task 14 — Limited login attempts
# ============================================================
# Give the user at most 3 attempts to enter the PIN.
#
# Use:
#   for
#   range()
#   break
#
# Correct PIN:
#   Access granted
#
# Three wrong attempts:
#   Access denied
#
# Do NOT use a while loop.

# Write your code below:
print("Task 14 — Limited login attempts")

correct_pin: str = "4821"
access_grant: bool = False

for attempt in range(3):
    pin_input: str = input(f"Enter PIN (attempt {attempt + 1}/3): ")
    if pin_input == correct_pin:
        access_grant = True
        print("Access granted")
        break
if not access_grant:
    print("Access denied")

print()

# ============================================================
# EXTRA Task 15 — Largest of three numbers
# ============================================================
# Ask the user to enter three integers.
#
# Print the largest number.
#
# Do NOT use:
#   max()
#
# Example:
# Input:
# 12
# 7
# 19
#
# Output:
# Largest: 19
#
# Think carefully about equal values.
print("EXTRA Task 15 — Largest of three numbers")

print("Type 3 integer values: ")
numbers_list: List[int] = [int(input()) for _ in range(3)]

largest: int = numbers_list[0]
for num in numbers_list:
    if num > largest:
        largest = num

print(f"Largest: {largest}")
print()

# Write your code below:


# ============================================================
# EXTRA Task 16 — Number statistics
# ============================================================

# Using one for loop, calculate:
#   number of positive values
#   number of negative values
#   number of zeros
#   sum of positive values
#   sum of negative values
#
# Expected:
# Positive: 5
# Negative: 3
# Zero: 2
# Positive sum: 63
# Negative sum: -15
#
# Do not manually calculate the values.

# Write your code below:
print("EXTRA Task 16 — Number statistics")

numbers: List[int] = [12, -4, 7, 0, 15, -9, 8, -2, 0, 21]

positive_counter: int = 0
negative_counter: int = 0
zero_counter: int = 0
positive_sum: int = 0
negative_sum: int = 0

for value in numbers:
    if value > 0:
        positive_counter += 1
        positive_sum += value
    elif value < 0:
        negative_counter += 1
        negative_sum += value
    else:
        zero_counter += 1

print(f"Positive: {positive_counter}")
print(f"Negative: {negative_counter}")
print(f"Zero: {zero_counter}")
print(f"Positive sum: {positive_sum}")
print(f"Negative sum: {negative_sum}")
print()

# ============================================================
# EXTRA Task 17 — Highest and lowest score
# ============================================================
# Find the highest and lowest scores using a for loop.
#
# Do NOT use:
#   max()
#   min()
#   sorted()
#
# Hint:
# Start with:
# highest = scores[0]
# lowest = scores[0]
#
# Expected:
# Highest: 96
# Lowest: 42

# Write your code below:
print("EXTRA Task 17 — Highest and lowest score")

scores: List[int] = [71, 85, 42, 96, 58, 83, 67, 91]
highest: int = scores[0]
lowest: int = scores[0]

for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

print()

# ============================================================
# EXTRA Task 18 — Temperature analysis
# ============================================================
# Classify every temperature:
#
#   Cold -> below 10
#   Mild -> 10–19
#   Warm -> 20–29
#   Hot  -> 30 or above
#
# Example output:
# 12: Mild
# 18: Mild
# 25: Warm
# ...
#
# After processing all temperatures, print how many
# temperatures belong to each category.

# Write your code below:
print("EXTRA Task 18 — Temperature analysis")

temperatures: List[int] = [12, 18, 25, 31, 7, 22, 35, 16, 29, 4]
cold_values: int = 0
hot_values: int = 0
mild_values: int = 0
warm_values: int = 0
category: str = ""

for value in temperatures:
    if value < 10:
        category = "Cold"
        cold_values += 1
    elif 10 <= value <= 19:
        category = "Mild"
        mild_values += 1
    elif 20 <= value <= 29:
        category = "Warm"
        warm_values += 1
    else:
        category = "Hot"
        hot_values += 1
    print(f"{value}: {category}")

print()
print(f"Cold: {cold_values}")
print(f"Mild: {mild_values}")
print(f"Warm: {warm_values}")
print(f"Hot: {hot_values}")

# ============================================================
# EXTRA Task 19 — Running balance
# ============================================================
print("EXTRA Task 19 — Running balance")

transactions: List[int] = [500, -120, -80, 250, -700, 300, -200]

# The starting balance is:
balance: int = 1000

# Process every transaction in order.
#
# Positive numbers mean money added.
# Negative numbers mean money spent.
#
# After each transaction print the current balance.
#
# Example:
# Transaction: 500
# Balance: 1500
#
# At the end print:
# Final balance: ...
#
# Also count how many transactions were:
#   deposits
#   withdrawals

# Write your code below:
deposits: int = 0
withdrawals: int = 0

for transaction in transactions:
    balance += transaction
    print(f"Transaction: {transaction}")
    print(f"Balance: {balance}")
    
    if transaction > 0:
        deposits += 1
    elif transaction < 0:
        withdrawals += 1

print()
print(f"Final balance: {balance}")
print(f"Deposits: {deposits}")
print(f"Withdrawals: {withdrawals}")
print()


# ============================================================
# EXTRA Task 20 — Find first number divisible by 7 and 11
# ============================================================
# Search numbers from 1 through 500.
#
# Find the FIRST number that is divisible by both 7 and 11.
#
# Print the number and immediately stop the loop.
#
# Required:
#   for
#   range()
#   break
#
# Expected:
# 77

# Write your code below:
print("EXTRA Task 20 — Find first number divisible by 7 and 11")

for i in range(1, 501):
    if i % 7 == 0 and i % 11 == 0:
        print(i)
        break
print()

# ============================================================
# EXTRA Task 21 — Limited number guessing
# ============================================================
print("EXTRA Task 21 — Limited number guessing")

secret_number: int = 37

# Give the user at most 5 attempts to guess the secret number.
#
# After each incorrect guess:
#
#   if guess < secret_number:
#       print "Too low"

#   if guess > secret_number:
#       print "Too high"
#
# Correct guess:
#   print "Correct"
#   stop immediately
#
# If all 5 attempts are used without success:
#   print "Out of attempts"
#
# Required:
#   for
#   range()
#   if / elif / else
#   break
#
# Do NOT use while.

# Write your code below:
for attempt in range(5):
    guess: int = int(input(f"Enter your guess (attempt {attempt + 1}/5): "))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct")
        break
else:
    print("Out of attempts")

print()

# ============================================================
# EXTRA Task 22 — Count increases
# ============================================================
# Count how many times a value is greater than
# the value immediately before it.
#
# Comparisons:
# 10 -> 14   increase
# 14 -> 13   no
# 13 -> 18   increase
# ...
#
# Expected:
# Increases: 5
#
# Hint:
# Start looping from index 1:
#
# for i in range(1, len(values)):
#
# Compare:
# values[i]
# values[i - 1]

# Write your code below:
print("EXTRA Task 22 — Count increases")

increases: int = 0
values: List[int] = [10, 14, 13, 18, 22, 20, 25, 25, 30]

for i in range(1, len(values)):
    if values[i] > values[i - 1]:
        increases += 1
        print(f"{values[i - 1]} -> {values[i]}   increase")
    else:
        print(f"{values[i - 1]} -> {values[i]}   no")

print(f"Increases: {increases}")
print()

# ============================================================
# EXTRA Task 23 — Prime number check
# ============================================================
# Ask the user to enter an integer greater than 1.
#
# Determine whether the number is prime.
#
# A prime number is divisible only by 1 and itself.
#
# Examples:
# 7  -> Prime
# 12 -> Not prime
# 29 -> Prime
#
# Required:
# Use a for loop to test divisors.
#
# Do NOT use any library.
#
# Hint:
# Try dividing by numbers from 2 up to number - 1.
# If one divides exactly, the number is not prime.

# Write your code below:
print("EXTRA Task 23 — Prime number check")

required_number: int = int(input("Please, type a number greater than 1: "))
if required_number <= 1:
    while required_number <= 1:
        required_number = int(input("The number is less than zero. Please retype it: "))

is_prime: bool = True

for i in range(2, required_number):
    if required_number % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")

print()

# ============================================================
# EXTRA Task 24 — Multiplication table
# ============================================================
# Print a multiplication table from 1 to 5.
#
# Expected format:
#
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25
#
# Required:
# Use nested for loops.
#
# Hint:
#
# for row in range(...):
#     for column in range(...):
#         ...

# Write your code below:
print("EXTRA Task 24 — Multiplication table")

for row in range(1, 6):
    for col in range(1, 6):
        print(row * col, end=" ")
    print()

print()