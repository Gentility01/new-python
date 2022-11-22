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
import time #this moddule will check for the time
import sys #this module will check for the memory

# checking memory in nomal python range
c = range(1000)
print(sys.getsizeof(2)*len(c))

# checking memory in numpy 
c = np.arange(1000)
print(c.size * c.itemsize)



