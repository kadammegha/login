# 8.Write a Python program to search for a specific character in a string using a while loop and break statement.
def search_char(str, char):
    index = 0
    while index < len(str):
        if str[index] == char:
            print(f"{char} found at specific index is {index}")
            break
        index += 1

str ='python language is easy'
char = 'e'
search_char(str, char)