# Write a python program to calculate the area of a circle given its radius using the formula
# area = 3.14 * r^2


radius = float(input("Enter the radius of the circle : \n"))
print("Area of circle using math library is : ", 3.14 * (radius ** 2), end="\n\n")

# Create a program that takes two numbers as input and print whether
# the first number is greater than, less than or equal to the second number.
num1 = int(input("Enter the First number : \n"))
num2 = int(input("Enter the Second number : \n"))
num3 = int(input("Enter the Third number : \n"))

if num1 > num2:
    print(num1, "is GREATER than", num2, end="\n\n")
elif num1 == num2:
    print(num1, "is EQUAL than", num2, end="\n\n")
else:
    print(num1, "is LESSL than", num2, end="\n\n")

# Use the ternary operator to find the maximun of three numbers entered by the user
max = num1 if (num1 > num2 and num2 > num3) else num2 if (num2 > num1 and num1 > num3) else num3
print(f"Max of three numbers{num1}, {num2}, and {num3} is : {max}", end="\n\n")

# Develop a Python Script that calculates the square and cube of a give number.

print(f"Square of {num3} is : {num1 ** 2}")
print(f"Cube of {num3} is : {num1 ** 3}", end="\n\n")
