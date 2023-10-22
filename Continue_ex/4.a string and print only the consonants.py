# 4. Write a Python program to iterate over a string and print only
# the consonants using a for loop and continue statement.
str = 'hello world'
cons = []
for i in range(0, len(str)-1):
    if str[i] not in 'aeiou':
        cons.append(str[i])
        continue
print(cons)
