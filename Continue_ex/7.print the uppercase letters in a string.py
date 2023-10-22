# 7. Write a Python program to print the uppercase letters in a string
# using a while loop and continue statement.
str = 'Python is Easy'
i = 0
while i < len(str):
    if str[i].islower():
        i += 1
        continue
    print(str[i])
    i += 1