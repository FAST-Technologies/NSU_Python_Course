"""Basic while-loop patterns."""

count = 1

while count <= 5:
    print(count)
    count += 1

print("Done")

password = ""

while password != "python":
    password = input("Password: ")

print("Access granted")
