# 8. Write a Python program to print the elements of
# a list skipping the elements divisible by 3 using a for loop and continue statement.
l = [1,2,3,6,9,12,15,60,40]
for i in l:
    if i % 3 == 0:
        continue
    print(i)