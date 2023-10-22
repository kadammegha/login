# 4. Write a Python program to print all odd numbers in a given range.
start = 1
end = 10
for i in range(start,end+1):
    if i%2!=0:
        print(i)