# Break and Continue with the loops
# Break
# 1 to 10 -> break when value of count = 5 -> 1, 2, 3, 4, 5, x


count = 1
while count <= 10:
    print(count)
    if count >= 5:
        break
    count = count + 1
