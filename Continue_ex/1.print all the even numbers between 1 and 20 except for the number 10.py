# 1. Write a Python program to print all the even numbers between 1 and 20 except for the number 10 using a for loop and continue statement.
for num in range(1, 21):
    if num % 2 == 0:
        if num == 10:
            continue
        print(num)

