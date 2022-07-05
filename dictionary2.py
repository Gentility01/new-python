
# Python program to demonstrate working
# of dictionary copy
# dic = {1:'Chealsea', 2:'Manchester', 3:'Arsenal'}
# print('original: ', dic)
 
# Accessing value for key
# print(dic.get(1))
 
# Accessing keys for the dictionary
# print(dic.keys())
 
# Accessing keys for the dictionary
# print(dic.values())

# Poping keys for the dictionary
# print(dic.pop(1))

# Printing all the items of the Dictionary
# print(dic.items())



# seq = {'a', 'b', 'c', 'd', 'e'}
 
# using fromkeys() to convert sequence to dict
# initializing with None
# res_dict = dict.fromkeys(seq)
 
# Printing created dict
# print("The newly created dict with None values : " + str(res_dict))
 
 
# using fromkeys() to convert sequence to dict
# initializing with 1
# res_dict2 = dict.fromkeys(seq, 1)
 
# Printing created dict
# print("The newly created dict with 1 as value : " + str(res_dict2))

# names  = {1,2,3,4,5,6,7,8,9}
# print(type(names))

# for o in names:
#     print(o)
# words = 0

# while 0 <= 9:
#     words += 1
#     print(words)
    
    
dics = {
    'value':'something that is worth having',
    'person':'a human being'
}

meaning = input('search')
if 'value' in meaning or 'value'.capitalize() or 'value'.upper():
    print(dics.get('value'))

