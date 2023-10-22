# 9. Write a Python program to iterate over a list of tuples and print only the tuples
# with a specific condition using a while loop and continue statement.
tuple_list = [(10, 20), (40, 40), (50, 60), (80, 80)]
i = 0
while i < len(tuple_list):
    if sum(tuple_list[i]) % 4 != 0:
        i += 1
        continue
    print(tuple_list[i])
    i += 1