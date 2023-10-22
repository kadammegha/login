# 2.write a prog to search for a specific element in a list using a while loop and break statement
def verify_element(list, target):
    i = 0
    while i < len(list):
        if list[i] == target:
            print(f"{target} is found  at index {i}.")
            break
        i += 1
    else:
        print(f"{target} not found in the list.")

list = [22,45,55,58,77,12]
ver_element = 12
verify_element(list,ver_element)