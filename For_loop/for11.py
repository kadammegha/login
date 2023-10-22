# 1. Write a Python program to print the numbers from 1 to 10 using a for loop.
# for i in range(1,11):
#     print(i,end=' ')
# --------------------------------------------------------------
# 2. Write a Python program to calculate the sum of all numbers in a list using a for loop.
# l = [1,2,3,4,5,6]
# sum = 0
# for i in range(len(l)):
#     sum = sum + l[i]
# print(sum)
# --------------------------------------------------------------
# 3. Write a Python program to find the factorial of a number using a for loop.
# num = int(input("enter num for factorial:"))
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print(fact)
#----------------------------------------------
# 4. Write a Python program to print all the even numbers between 1 and 50 using a for loop.
# for i in range(1,51):
#     if i%2==0:
#         print(i,end=' ')
#---------------------------------------------------------------------------
# 5. Write a Python program to iterate over a string and print each character using a for loop.
# str = 'python is easy language'
# for i in range(len(str)):
#     print(str[i],end=' ')
#-------------------------------------------------------------------
# 6. Write a Python program to iterate over a list of tuples and print each element using a for loop.
# list_of_tuples = [(1,2,3),(4,5,6),(7,8,9)]
# for i,v in enumerate(list_of_tuples):
#     element_one = v[0]
#     element_two = v[1]
#     element_three = v[2]
#     print(element_one,element_two,element_three)
# ------------------------------------------------------------
# 7. Write a Python program to find the largest element in a list using a for loop.
# list = [11,33,55,65,3,78,90]
# max = list[0]
# for i in range(len(list)):
#     if list[i]> max:
#         max = list[i]

# print(max)
# -------------------------------------------------------------------
# 8. Write a Python program to check if all elements in a list are even using a for loop.
# list = [2,4,6,8,10,9,14]
# for i in list:
#     if i%2==0:
#         print("list have all even numbers")
#     else:
#         print("list haven't all even numbers")
# ----------------------------------------------------------------
# 9. Write a Python program to find the common elements between two lists using a for loop.
# list1 = [2,3,4,5]
# list2 = [1,2,3,4]
# comm_element =[]
# for i in list1:
#     if i in list2:
#         comm_element.append(i)
# print(comm_element)
# ----------------------------------------------------------------
# 10. Write a Python program to calculate the sum of the digits of a number using a for loop.
# num = int(input("Enter number for digit sum:"))
# sum = 0
# for n in str(num):
#     sum+=int(n)
# print("sum of digits:",sum)
