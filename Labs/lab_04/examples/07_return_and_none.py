"""return values and None."""


def divide_total(total, count):
    if count == 0:
        return None

    return total / count


result = divide_total(100, 4)

if result is None:
    print("No result")
else:
    print(result)

missing_result = divide_total(100, 5)

if missing_result is None:
    print("Cannot divide by zero")
