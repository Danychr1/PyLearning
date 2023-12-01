# Write a program that calculates and displays the letter grade for a given numerical score
# (e.g.,A, B, C, D, or F) based on the following grading scale:
# input - score - 89
# output- B
# A: 90- 100
# B: 80-89
# C: 70-79
# D: 60-69
# F:0-59

a = float(input("Enter the score"))
if 90 <= a <= 100:
    result = "A"
elif 80 <= a + 89:
    result = "B"
elif 70 <= a <= 79:
    result = "C"
elif 60 <= a <= 69:
    result = "C"
else:
    result = "F"
print(f"the grate for the marks {a} is {result}")
