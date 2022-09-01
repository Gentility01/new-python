
# stop = 10
# for i in range(10):
#     print(i, end=' ')
    
# for i in range(1, 10):
#     print(i)

# a = range(10)
# print(a)

# for i in range(1, 10, 2):
#     print("Current value of i is:", i)

# class Employee:
#     # class variables
#     company_name = 'ABC Company'

#     # constructor to initialize the object
#     def __init__(self, name, salary):
#         # instance variables
#         self.name = name
#         self.salary = salary

#     # instance method
#     def show(self):
#         print('Employee:', self.name, self.salary, self.company_name)

# # create first object
# emp1 = Employee("Harry", 12000)
# # emp1.show()

# # create second object
# emp2 = Employee("Emma", 10000)
# emp2.show()
# a = 'Winner' 
# print(a[-2]) 

# email = input('please ener your email: ')
# check = '@' in email and '.' in email and 'com' in email
# print(check)

# name = input('Please enter your name ').capitalize()

# passw = input('please enter a passwor ')

# if len(passw) <= 6 :
#     print('Your password should be more than 6 characters...')
# if   passw.istitle():
#     pass
# else:
#     print(f'{name}there must be an upper case in your password')
# if '_' not in passw:
#     print('there must be a special character')
from ntpath import join


# a = ('msaeesg')
# b = [a[0], a[0:4] , a[1] , a[5] , a[2] , a[-1], a[3]]
# new = (''.join(b))
# print(new)




# class Bird:
   
#     def intro(self):
#         print("There are many types of birds.")
 
#     def flight(self):
#         print("Most of the birds can fly but some cannot.")
 
# class Sparrow(Bird):
   
#     def flight(self):
#         print("Sparrows can fly.")
 
# class Ostrich(Bird):
 
#     def flight(self):
#          print("Ostriches cannot fly.")

# class Duck(Bird):
#     def swim(self):
#         print("Ducks can swim")
 
# obj_bird = Bird()
# obj_spr = Sparrow()
# obj_ost = Ostrich()
# obj_duck = Duck()
 
# obj_bird.intro()
# obj_bird.flight()
 
# obj_spr.intro()
# obj_spr.flight()
 
# obj_ost.intro()
# obj_ost.flight()

# class Products:
#     def __init__(self, name, quantity, price):
#         self.name=name
#         self.quantity=quantity
#         self.price=price
    
#     def details(self):
#         product_details = f'product name is {self.name} its quantity is {self.quantity} and its price is {self.price}'
#         print(product_details)

#     def calculate_product(self):
#         cal = self.price * self.quantity
#         print(cal)

# product1 = Products('Laptop', 4, 100000)
# # product1.details()

# from math import pi


# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         return "I am a two-dimensional shape."

#     def __str__(self):
#         return self.name


# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length

#     def area(self):
#         return self.length**2

#     def fact(self):
#         return "Squares have each angle equal to 90 degrees."


# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     def area(self):
#         return pi*self.radius**2


# a = Square(4)
# b = Circle(7)
# print(b)
# print(b.fact())
# print(a.fact())
# print(b.area())



# initialize my_set
# my_set = {1, 3}
# print(my_set)

# my_set[0]
# if you uncomment the above line
# you will get an error
# TypeError: 'set' object does not support indexing

# add an element
# Output: {1, 2, 3}
# my_set.add(2)
# print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
# my_set.update([2, 3, 4])
# print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
# my_set.update([4, 5], {1, 6, 8})
# print(my_set)


# Difference between discard() and remove()

# initialize my_set
# my_set = {1, 3, 4, 5, 6}
# print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
# my_set.discard(4)
# print(my_set)

# remove an element
# Output: {1, 3, 5}
# my_set.remove(6)
# print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
# my_set.discard(2)
# print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

# def product(firstname, lastname, age):
#     print(f'my firstname is {firstname}, and my last name is {lastname} and my age is {age} ')


# product('emeka', 'chidi', 21)

# def product(name, price, quantity):
#     total = price * quantity
#     print(f'{name} price {price} quantity {quantity} and total {total}')

# product('Laptop', 2000, 5)

# try:
#     age = int(input('enter ur age'))
#     print(age)
# except:
#     print('hey you only need to put in an integer')

# import module sys to get the type of exception
# import sys

# randomList = [2, 4, 8]

# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 2/int(entry)
#         # break
#     except:
#         print("Oops!", sys.exc_info()[0], "occurred.")
#         print("Next entry.")
#         print()
# print("The reciprocal of", entry, "is", r)
try:
    name = obi
    name2 = 'obi'
    print(name2)
except NameError:
    print('there is no quote in ur string')

