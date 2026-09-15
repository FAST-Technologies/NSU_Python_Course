"""Truthiness and conditional expressions."""

name = input("Name: ")

if name:
    print(f"Hello, {name}")
else:
    print("Name is empty")

score = 72
status = "Pass" if score >= 60 else "Fail"

print("Status:", status)
