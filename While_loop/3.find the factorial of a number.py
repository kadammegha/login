# 3. Write a Python program to find the factorial of a number using a while loop.
num = 5
fact = 1
while num != 0:
    fact = fact * num
    num -= 1
print(f"factorial of 5 is {fact}")