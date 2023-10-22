# 4.writ a python program check if a number is present in a list using a while loop and break statement
def num_is_present(l, find):
    i = 0
    flag =False
    while i < len(l):
        if l[i] == find:
            flag = True
            break
        i += 1
    if flag:
        print("number is present in list")
    else:
        print("number is not present in list")
l = [4, 5, 6, 7, 8, 9]
find = 17
num_is_present(l, find)
