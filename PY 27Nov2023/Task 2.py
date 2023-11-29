# Write a python program to calculate the area of a circle given its radius using the formula
# area = 3.14 * r^2


radius = float(input("Enter the radius of the circle : \n"))
print("Area of circle using math library is : ", 3.14 * (radius ** 2), end="\n\n")

# Create a program that takes two numbers as input and print whether
# the first number is greater than, less than or equal to the second number.
a = int(input("Enter the First number : \n"))
b = int(input("Enter the Second number : \n"))
c = int(input("Enter the Third number : \n"))

if a > b:
    print(a, "is GREATER than", b, end="\n\n")
elif a == b:
    print(a, "is EQUAL than", b, end="\n\n")
else:
    print(a, "is LESSL than", b, end="\n\n")

# Use the ternary operator to find the maximun of three numbers entered by the user
max = a if (a > b and b > c) else b if (b > a and b > c) else c
print(f"Max of three numbers{a}, {b}, and {c} is : {max}", end="\n\n")

# Develop a Python Script that calculates the square and cube of a give number.

print(f"Square of {c} is : {a ** 2}")
print(f"Cube of {c} is : {a ** 3}", end="\n\n")
