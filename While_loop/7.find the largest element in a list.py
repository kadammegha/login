# 7. Write a Python program to find the largest element in a list using a while loop.
l = [22,55,3,87,90,83,4,1]
index = 0
max = 0
while index < len(l):
    if max < l[index]:
        max = l[index]

    index += 1
print(max)