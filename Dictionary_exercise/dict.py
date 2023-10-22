# 1. Write a Python program to iterate over a dictionary and print its keys and values.
# d = {1:'mango',2:'banana',3:'cherry',4:'orange'}
# print(d.keys(),":",d.values())
# print(d.items())
# -----------------------------------------------------------
# 2. Write a Python program to check if a key exists in a dictionary.
# d = {1:100,2:200,3:300,4:400,5:500}
# print(d[4])
# ---------------------------------------------------
# 3. Write a Python program to get the value associated with a key in a dictionary.
# dict = {'a': 10, 'b': 'one', 'c': 30}
# key_to_get = 'b'
#
# value = dict.get(key_to_get)
# if value is not None:
#     print(f'Value for key {key_to_get}: {value}')
# else:
#     print(f'Key {key_to_get} not found in the dictionary.')
# ---------------------------------------------------------
# 4. Write a Python program to remove a key from a dictionary.
# dict1 = {'pune': 100, 'satara': 200, 'mumbai': 300}
# key_to_delete = 'satara'
# if key_to_delete in dict1:
#     del dict1[key_to_delete]
#     print(f' {key_to_delete}:Value for key is delete')
# else:
#     print(f'Key {key_to_delete} not found in the dictionary.')
# --------------------------------------------------------
# 5. Write a Python program to sort a dictionary by its values.
# dict = {1:"doctor", 4:"engineer", 5:"teacher",2:"farmer",3:"student"}
#
# sorted_dict = dict(sorted(dict.items(), key=lambda item: item[1]))
# print(sorted_dict)
# # ----------------------------------
# 6. Write a Python program to merge two dictionaries.
# def merge(dict1,dict2):
#     return (dict2.update(dict1))
# dict1 = {1:'python',2:'java',3:'.net'}
# dict2 = {2:'c',3:'ruby',4:'c#'}
# dict = merge(dict1,dict2)
# print(dict)
# print(dict2)

# -----------------------------------------------------------------
# 7. Write a Python program to count the frequency of each element in a dictionary.
# d = {1:'computer',2:'laptop',3:'mobile',4:'computer',5:'mobile',6:'system'}
# count={}
# for v in d.values():
#     if v not in count:
#         count[v] = 0
#     count[v]+=1
# print(count)
# -----------------------------------------
# 8. Write a Python program to find the length of a dictionary.
# places = {'a':'satara','b':'pune','c':'latur','d':'kholapur','r':'sangali'}
# print("length of dict:",len(places))
#--------------------------------------------------
# 9. Write a Python program to check if a dictionary is empty.
# approch 1
# empty_dict = dict()
# print(empty_dict)
# approch 2
# dict = {1:100,2:700,3:500}
# if len(dict) == 0:
#     print("dictionary is empty!")
# else:
#     print("dictionary is not empty")
#------------------------------------------------
# 10. Write a Python program to find the keys with the maximum and minimum values in a dictionary.
# def test(d):
#     return max(d,key=d.get),min(d,key=d.get)
#
# d = {'ram':90,'gopal':88,'madhav':99,'vishnu':98}
# print(test(d))