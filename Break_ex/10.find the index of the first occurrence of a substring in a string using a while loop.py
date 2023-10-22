# 10.Write a Python program to find the index of the first occurrence of a substring in a string using a while loop and break statement.
def first_substring(string, substring):
    idx = 0
    while idx < len(string):
        if string[idx:idx + len(substring)] == substring:
            print(f"The substring '{substring}' found at index {idx}")
            break
        idx += 1
    else:
        print(f"The substring '{substring}' is not in the string")


string = 'wel come and come in'
substring = 'come'
first_substring(string, substring)
