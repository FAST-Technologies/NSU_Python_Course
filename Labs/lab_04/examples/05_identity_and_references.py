"""Equality, identity, and mutable references."""

a = [1, 2]
b = [1, 2]
c = a

print("a == b:", a == b)
print("a is b:", a is b)
print("a is c:", a is c)

print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))

c.append(3)

print("a:", a)
print("b:", b)
print("c:", c)

copied = a.copy()
print("copied == a:", copied == a)
print("copied is a:", copied is a)
