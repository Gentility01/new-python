import oop2
obj1 = oop2.Derived()
 
obj2 = oop2.Base()
# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)
 
# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)


# declaring the string
str ="manchester"
 
# slicing using indexing sequence
print(str[: 3])
# print(str[1 : 5 : 2])
# print(str[-1 : -12 : -2])