# 10. Write a Python program to calculate the sum of the digits of a number using a while loop.
d = int(input("Enter number: "))
sum = 0
while d > 0:
     rem = d % 10
     sum += rem
     d //= 10
print(sum)