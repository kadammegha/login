# 3.prime numbers between 1 and 100 using for loop and break statement
def prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
            break
    return True
for num in range(2, 101):
    if prime(num):
        print(num, end=' ')

