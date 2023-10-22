# 5.Write a Python program to find the largest palindrome number in a given range using a for loop and break statement.
def is_palindrome(num):
    return str(num) == str(num)[::-1]
palindrome_num = 0
for num in range(100,0,-1):
    if is_palindrome(num):
        palindrome_num = num
        break
print("largest palindrome number in a given range:",palindrome_num)

# newnum=[]
# for i in range(99,152):
#     n=str(i)
#     num=n[::-1]
#     if int(num)==int(i):
#         newnum.append(i)
# print(max(newnum))