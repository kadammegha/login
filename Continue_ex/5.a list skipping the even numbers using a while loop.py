# 5. Write a Python program to print the elements of a list
# skipping the even numbers using a while loop and continue statement.
l = [1,2,3,4,5,6,7,8]
index = 0
while index < len(l):
    if l[index] % 2 == 0:
        index += 1
        continue
    print(l[index])
    index += 1


