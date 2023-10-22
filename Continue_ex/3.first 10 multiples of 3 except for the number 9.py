# 3. Write a Python program to print the first 10 multiples of 3 except for the number 9 using a for loop and continue statement.
index = 0
for i in range(1, 31):
    if i == 9:
        continue
    if i % 3 == 0:
        print(i)
        index += 1
    if index == 10:
        break
