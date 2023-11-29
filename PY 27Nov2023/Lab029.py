# Identity Operators:
# is Returns True if both variable are the same object.
# is not Returns True if both variable are not the same object

x = [2, 3, 4]
y = [2, 3, 4]

print(x is y)
print(id(x))
print(id(y))

print(x is y)
print(x is not y)
print(id(x))
print(id(y))
