# 2. Write a Python program to print the elements of a list skipping the negative numbers using a while loop and continue statement.
element = [1, 2, 3, -1, -3, 8, -9]
index = 0
while index < len(element):
    if element[index] < 0:
        index += 1
        continue
    print(element[index])
    index += 1

