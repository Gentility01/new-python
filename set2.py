'''In Python, frozenset is the same as set except the frozensets are immutable
which means that elements from the frozenset cannot be added or removed once created.
This function takes input as any iterable object and converts them into an immutable object. 
The order of elements is not guaranteed to be preserved.'''


# Python program to understand frozenset() function
 
# tuple of numbers
# nu = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# na = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
# # converting tuple to frozenset
# fnum = frozenset(nu)
# fnum2 = frozenset(na)
 
# # printing details
# print("frozenset Object is : ", fnum)
# print("frozenset Object is : ", fnum2)


# Python program to understand use
# of frozenset function
 
# creating a dictionary
# Student = {"name": "Ankit", "age": 21, "sex": "Male",
#            "college": "MNNIT Allahabad", "address": "Allahabad"}
 
# # making keys of dictionary as frozenset
# a = frozenset(Student)
 
# # printing keys details
# print('The frozen set is:', a)

'''Set
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.'''

thisset = {"apple", "banana", "cherry"}
# print(thisset)

'''
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.
Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
'''
thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset)

'''
The set() Constructor
It is also possible to use the set() constructor to make a set.
'''
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

q =set(('apples','banana','orange'))
q1 =set('apples')
print(q)
print(q1)