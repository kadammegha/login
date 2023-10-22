# 9. Write a Python program to find the common elements between two lists using a while loop.
l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]
common = []
i = 0
while i < len(l1):
    j = 0
    while j < len(l2):
        if l1[i] == l2[j]:
            common.append(l1[i])
            break
        j += 1
    i += 1

print("common elements between 2 list are :",common)

