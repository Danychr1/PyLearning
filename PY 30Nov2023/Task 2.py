# Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# input = 2024
# output = Leap year

year = int(input("Enter a year to check if it's a leap year or not :\n"))

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is an leap year.")
elif year % 400 ==0:
    print(f"{year} is an leap year.")
else:
    print(f"{year} is not an leap year")


