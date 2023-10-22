# 6. Write a Python program to find the sum of all numbers between 1 and 100,
# excluding the multiples of 5 using a for loop and continue statement.
sum = 0
for i in range(1, 101):
    if i % 5 == 0:
        continue
    sum += i
print("sum of all numbers between 1 and 100:",sum)

        