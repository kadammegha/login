# 1. Write a Python program to find the sum of all elements in a list.
# l = [2,3,1,1,8,9]
# sum = 0
# for i in range(len(l)):
#     sum = sum + l[i]
# print(sum)
# =================================================
# 2. Write a Python program to find the maximum and minimum elements in a list.
# l = [44, 2, 33, 4, 86, 99,0 ]
# max = 0
# min = l[0]
# for i in range(0, len(l)):
#     for j in range(i+1,len(l)+1):
#         if l[i] > max:
#             max = l[i]
#         if l[i] < min:
#             min = l[i]
# print(max)
# print(min)
# ================================
# 3. Write a Python program to remove duplicates from a list.
# li = [1,3,4,2,1,4,1,2,4]
# l = set(li)
# print(l)
# ===========================================
# 4. Write a Python program to check if a list is sorted in ascending order.
# l = [40,50,10,50,40,100,200]
# l.sort()
# print(l)
# for i in range(0,len(l)-1):
#     l[i] <= l[i+1]
#     print(l[i])
# ====================================================
# 5. Write a Python program to find the second largest element in a list.
# l=[6,7,4,9,22,34,10]
# l.sort()
# print(l)
# print("second largest element:",l[-2])
# ====================================
# 6. Write a Python program to sort a list of strings in alphabetical order.
# alpha = ['pqr','xyz','mno','str','cde','abc']
# alpha.sort()
# print(alpha)
# =======================================
# 7. Write a Python program to find the common elements between two lists.
# def comm_elements(l1, l2):
#     return list(set(l1) & set(l2))
# l1 = [1,4,13,33,12]
# l2 = [33,66,4,12,17]
# print(comm_elements(l1, l2))
# =================================================
# 8. Write a Python program to remove the nth occurrence of an element from a list.
# def remove_nth_occurrence(lst, element, n):
#     count = 0
#     for i, item in enumerate(lst):
#         if item == element:
#             count += 1
#             if count == n:
#                 del lst[i]
#                 break
#
# my_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
# element_to_remove = int(input("Enter the element to remove: "))
# occurrence_to_remove = int(input("Enter the occurrence to remove: "))
# remove_nth_occurrence(my_list, element_to_remove, occurrence_to_remove)
# print("List with the specified occurrence removed:", my_list)

# ========================================
# 9. Write a Python program to find the difference between two lists.
# l1 = [2,4,6,8,9]
# l2 = [1,3,5,6,8]
# print(set(l1)-set(l2))
# Second Approch input from user
# def list_difference(lst1, lst2):
#     return list(set(lst1) - set(lst2))
#
# list1 = [int(x) for x in input("Enter the first list of numbers separated by spaces: ").split()]
# list2 = [int(x) for x in input("Enter the second list of numbers separated by spaces: ").split()]
# difference_list = list_difference(list1, list2)
# print("Difference between lists:", difference_list)
# ======================================================
# 10. Write a Python program to remove the elements of a list that are divisible by 3.
# l = [3,9,12,30,4,7,27]
# l.sort()
# print(l)
# l2 = []
# for i in range(0,len(l)-1):
#     if i%3!=0:
#         l2.append(i)
# print(l2)



