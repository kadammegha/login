# 9.Write a Python program to find the first occurrence of a vowel in a string using a for loop and break statement.
def first_vowel(str):
    for i, v in enumerate(str):
        if v.lower() in 'aeiou':
            print(f"The first vowel {v} is at index {i} ")
            break
    else:
        print("No vowels present in the string")

str1 = 'hello world'
first_vowel(str1)