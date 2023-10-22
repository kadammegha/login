# 1.Write a Python program to find the first occurrence of a number in a list using a for loop and break statement.
def first_occurrence(num, target):
    for i, n in enumerate(num):
        if n == target:
            print(f"The first occurrence of {target} is at index {i}.")
            break
    else:
        print(f"{target} not found in the list.")

num = [30, 10, 30, 30, 50, 90]
target = 30
first_occurrence(num, target)
