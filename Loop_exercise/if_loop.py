# 1. Write a Python program to check if a number is positive, negative, or zero.
# num = 10000
# if num>0:
#     print("positive number")
# elif num<0:
#     print("negative number")
# else:
#     print("number is 'Zero'")
# ---------------------------------------------------
# 2. Write a Python program to check if a number is even or odd.
# num = int(input("enter num for check even or not:"))
# if num%2==0:
#     print("Even num")
# else:
#     print("Odd num")
# -------------------------------------------------------
# 3. Write a Python program to check if a year is a leap year or not.
# year = int(input("Enter a year:"))
# if year%400==0 and year%100==0:
#     print("leap year is:",year)
# elif year%4==0 and  year%100!=0:
#     print("leap year is:", year)
# else:
#     print("not a leap year is:", year)
# ------------------------------------------------------------
# 4. Write a Python program to find the maximum of three numbers using if-else.
# num1 = float(input("Enter 1 num for max :"))
# num2 = float(input("Enter 2 num for max :"))
# num3 = float(input("Enter 3 num for max :"))
# if num1 >= num2 and num1 >= num3:
#     print("max num is:",num1)
# elif num2 >= num1 and num2 >= num3:
#     print("max num is:",num2)
# else:
#     print("max num is:",num3)
# --------------------------------------------------
# 5. Write a Python program to check if a number is prime.
# num = int(input("Enter num for prime or not:"))
# flag = False
# if num==1:
#     print(num,"num is not a prime number")
# elif num>1:
#     for i in range(2,num):
#         if num%i ==0:
#             flag = True
#             break
#     if flag:
#         print(num,"is not a prime number")
#     else:
#         print(num, "is a prime number")
# --------------------------------------------
# 6. Write a Python program to check if a number is divisible by both 3 and 5.
# n =int(input("Enter num for divisible by 3,5:"))
# if n%3==0 and n%5==0:
#     print("num divisible by both 3 and 5")
# else:
#     print("num is not divisible by both 3 and 5")
# ===========================================================
# 7. Write a Python program to check if a character is a vowel or consonant.
# char = input("enter character for vowel or consonant:")
# vowels = 'aeiou'
# char = char.lower()
# for cha in char:
#     if cha in vowels:
#         print("char is vowels")
#     else:
#         print("char is consonant")
# ----------------------------------------------------------------------------
# 8. Write a Python program to check if a given string is a palindrome using if-else.
# str = 'pop'
# rev = str[::-1]
# print(rev)
# if str==rev:
#     print("string is a palindrome")
# else:
#     print("string is not a palindrome")
# -----------------------------------------------------------------------------
# 9. Write a Python program to determine the largest among three numbers using nested if-else.
# num1 = int(input("Enter 1st no:"))
# num2 = int(input("Enter 2nd no:"))
# num3 = int(input("Enter 3rd no:"))
# if num1>=num2 and num1>=num3:
#     print("num1 is greater")
# elif num2>=num3 and num2>=num1:
#     print("num2 is greater")
# else:
#     print("num3 is greater")
#------------------------------------------------------------
# 10. Write a Python program to check if a triangle is equilateral,
# isosceles, or scalene based on its side lengths using if-else.
# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))
# if a == b == c:
#     print("Equilateral triangle ")
# elif a == b or b == c or c ==a:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle ")