# 1. Explain the difference between the = operator and the == operator in python


# = is the assignment operator. it sets a particular variable equal to a particular value.
# for example
# c = 10
# we are declaring the c variable, assigning it the value of 10

# == is the equality operator.
# It is used in true and false expressions to check whether one value is equal to another one.
# the equality operator does not set any value, it only checks whether two value are equal.
# for example
# (5+3) == 9 evaluate to false, since 5+3 == 8, since 8 is not equal to 9

# 2. What does the ** operator do in Python, and how is it used?

# Double asterisks (**) acts as an exponentiation operator for numeric value.
# ** operator is lightweight as comparared to the pow () function because functions takes more processing and compilation
# power.
a = 5
b = 3
c = a ** b
print(c)

# 3 What does the ^operator do in Python, and how is it used?
# '^' is XOR operator
# Sets each bit and set it to 1 if only is 1,
# otherwise if both are 1 or both are 0 it is set to 0:
