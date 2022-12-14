'''WHAT IS NUMPY
numpy can be defined as a python core library for scientific and numerical computing in python
it provides high    perfomance multidimentional array oject and tool for working with arrays

WHY USE NUMPY instead of list 
1. it is fast
2. it is convinient
3. it takes less memory

to start numpy we need to install it by typing 'pip install numpy'
then import it by typing 'import numpy as np'
'''

import numpy as np

#creating a numpy array
# a = np.array([1,2,3])
# print(a)

#lets confirm that numpy takes less memory and time by using the time and memory nodule
# import time #this moddule will check for the time
# import sys #this module will check for the memory

# # checking memory in nomal python range
# c = range(1000)
# print(sys.getsizeof(2)*len(c))

# # checking memory in numpy 
# c = np.arange(1000)
# print(c.size * c.itemsize)


'''
What is an array?
An array is a central data structure of the NumPy library. An array is a grid of values and it contains information
about the raw data, how to locate an element, and how to interpret an element.
It has a grid of elements that can be indexed in various ways. 
The elements are all of the same type, referred to as the array dtype.

An array can be indexed by a tuple of nonnegative integers, by booleans, by another array, or by integers.
The rank of the array is the number of dimensions. 
The shape of the array is a tuple of integers giving the size of the array along each dimension.

One way we can initialize NumPy arrays is from Python lists, using nested lists for two- or higher-dimensional data.
'''

# examples of array
# 1 dimentional array
# a = np.array([1, 2, 3, 4, 5, 6])

# 2 dimetion array
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8])

# 3 dimetion array
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a[0])


#CHECKING FOR  DIMENTIONS IN AN ARRAYS
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# # print(a.ndim)
# print(a.shape)  #this will print the number of dimentions it is


# HOW TO CHECK THE TYPE OF ARRAY
# print(a.dtype)

#ACCESSING OR INDEXING, AND CHANGING SPECIFIC ELEMENT, ROWS AND COLUMS
# accessing a particular number in an array (eg getting 7 in the second dimention)
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a[1,2])  
# print(a[0,-2])  

#accessing a particular row in an array
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a[2, :])  # this means the second row counting from 0

#accessing a particular column in an array

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a[:,3])  #this means all the rows then the third column



'''more features about list and numpy is that in list we can just insert, delete, append, concertinate etc
but in numpy we can do more than that for example with numpy we can multiply elements but cant in a list eg'''

# list
# a = [1,2,3]
# b = [4,5,6]
# print(a*b)

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(a*b)


'''Numpy application/uses
mathematies(MATLAP replacement)
Plotting
backend(Pandas,connect4, digital photograpy)
machine learning
'''


