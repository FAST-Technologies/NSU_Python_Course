"""if-elif-else and simple validation."""

score = int(input("Score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Fail")
