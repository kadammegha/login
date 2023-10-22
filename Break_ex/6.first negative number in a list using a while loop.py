#6. Write a Python program to find the first negative number in a list using a while loop and break statement.
def first_negative(num):
    index = 0
    while index < len(num):
        if num[index] < 0:
            print(f"first negative number is {num[index]}")
            break
        index += 1
    else:
        print("There is no negative num present in list")

l = [1,2,3,2,-5,-7]
first_negative(l)

