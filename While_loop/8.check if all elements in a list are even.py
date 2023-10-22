# 8. Write a Python program to check if all elements in a list are even using a while loop.
num = [2, 4, 6, 8, 12, 3, 5]
index = 0
all_even = False
while index < len(num):
    if num[index] % 2 != 0:
        all_even = True
        break
    index += 1
if all_even == False:
    print("all elements in list are even")
else:
    print("all elements in list are not even")
