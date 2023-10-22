# 7. Write a Python program to print the elements of a list until a specific condition is met using a for loop and break statement.
def until_condition(numbers, condition):
    for n in numbers:
        if n == condition:
            break
        print(n, end=' ')

numbers = [12,13,14,15,16,60]
condition = 15
until_condition(numbers, condition)