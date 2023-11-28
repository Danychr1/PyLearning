# String
# Bunch of char
name = "denise"

# String Funtions
# Python string Immutable in Nature - They can't changed! One Created
# name[0] = "h" #TypeError: 'str' object does not support item assignment

# Capitalizer()
# Returs a copy of the string with its first character  capitalized.
result = name.capitalize()
print(result)
print(name)

print(id(result))
print(id(name))

# Upper Case
result2 = name.upper()
print(result2)
print(name)

# Lower
result3 = name.lower()
print(result3)
print(id(result3))

# Swapcase
# Returs a copy of the string with uppercase characters converted to lowercase and viceversa

name = "dAnY"
print(name.swapcase())
print(name)

# Title
# Returns a titlecase version of the string
# Where words start with an uppercase character and the remaining character are lowercase
name = "hello world"
print(name.title())
print(name)

t1 = "valentina jr"
t2 = "padres jr"
print(t1.capitalize())
print(t2.upper())

# t1 is ref or variable name

name = "valentina jr"
print(len(name))

# Replace
text = "hello world"
# result_rep = text.replace(__old: "World", __new: "Python")
# print(result_rep)


# index amd len
name = "Denise"
# len -> 1
print(len(name))

# index - 0 to len - 1
# D - 0, e - 1, n - 2, i - 3, s - 4, e - 5

# find()
# Returns the lowest index of a subtring in the string.
# Returns - 1 if the substring is not found.

text = "hello world"
index = text.find("world")
print(index)

# cound () - count the characters
count = text.count("l")
print(count)

name = "Dan "
print(len(name))

name = "valentino"
print(name)
del name
print(name)
