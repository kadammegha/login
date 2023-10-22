# String Exercises:
# 1. Write a Python program to count the number of characters in a string.
# str = 'CodeNucleus'
# print(len(str))
# --------------------------------------------------
# 2. Write a Python program to reverse a string.
# s = 'CodeNucleus'
# print('reverse string:',s[::-1])
# l = len(s)
# for i in range((l-1), -1, -1):
#     print(s[i], end='')
#------------------------------------------------------
# 3. Write a Python program to check if a string is a palindrome.
# s = input("Enter string for checking palindrome:")
# n = len(s)
# old = s
# rev = ""
# for i in range((n-1), -1, -1):
#     rev = rev + s[i]
# print(rev)
# if rev == old:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")
# ---------------------------------------------
# 4. Write a Python program to remove all the vowels from a string.
# str = "CodeNucleus"
# vowels ={'a','e','i','o','u'}
# s = ''
# for i in str.lower():
#     if i not in vowels:
#         s = s + i
# print(s)
# --------------------------------------------------------------
# 5. Write a Python program to find the first non-repeating character in a string.
# str = "CodeNucleus"
# s = set(str.lower())
# char_order = []
# chr = {}
# for i in s:
#     if i in chr:
#         chr[i] += 1
#     else:
#         chr[i] = 1
#         char_order.append(i)
# for i in char_order:
#     if chr[i] == 1:
#         print(i, end='')
# ---------------------------------------------------------------
# 6. Write a Python program to capitalize the first letter of each word in a string.
# new = "i love python"
# print(new.title())
#-------------------------------------------------------------
# 7. Write a Python program to check if a string is an anagram of another string.
# def is_anagram(string1, string2):
#     return sorted(str1) == sorted(str2)
#
# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")
# result = is_anagram(str1, str2)
# print("Is anagram: ", result)
#--------------------------------------------------------
# 8. Write a Python program to find the most frequent character in a string.
# from collections import Counter
#
# def most_frequent_char(str):
#     char_count = Counter(str)
#     return max(char_count, key=char_count.get)
#
# string = input("Enter a string: ")
# most_frequent = most_frequent_char(string)
# print("Most frequent character:", most_frequent)

#------------------------------------------------------------------------
# 9. Write a Python program to check if a string is a valid email address.
# import re
# email = input("Enter email to test: ")
# pattern = r'[A-Za-z0-9@#$%^&+=]{8,}'
# if re.match(pattern, email):
#     print("valid Email")
# else:
#     print("Invalid email")

#--------------------------------------------------------------------
# 10. Write a Python program to find the length of the longest substring without repeating characters.
# def longest_substring_length(string):
#     char_index = {}
#     max_length = start = 0
#
#     for i, char in enumerate(string):
#         if char in char_index and char_index[char] >= start:
#             start = char_index[char] + 1
#         char_index[char] = i
#         max_length = max(max_length, i - start + 1)
#
#     return max_length
#
# input_string = input("Enter a string: ")
# length = longest_substring_length(input_string)
# print("Length of longest substring without repeating characters:", length)