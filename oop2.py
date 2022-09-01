'''CREATING A CLASS WITH INSTACE ATRRIBUTE'''
# class Item:
    # we can write a method that can be used or executte in the instances
    # methods are functions inside a class
    # def calculate_price(self, x, y): #self: python passes the object itself as the first augment when u call the methods you can call the self something else . 
    #     return x + y
        
        
    

# item1 = Item() #this can be said to be the instance of the class in a variable

# item1.name = 'phone' #this can be said to be the attribute of a class
# item1.price= 2000  #this can be said to be the attribute of a class
# item1.quantity= 2  #this can be said to be the attribute of a class

# a = item1.calculate_price(item1.price, item1.quantity)
# print(a)

# item2 = Item()
# item2.name = 'laptop'
# item2.price = 20000
# item2.quantity = 3
# a = item2.calculate_price(item2.price, item2.quantity)
# print(a)


'''using the __init__method  and __init__ are called the constructor'''

# class Item:
    
    
    
    # def __init__(self): #this __init__ is said to be one of the magic methods in classes and it passes the method  without calling it as an attrbute but the values are passed in the instances of that class
    #     price = 2000
    #     quantity = 2
    #     print(price * quantity)
    
'''we can add more parameters in this  constructors all we need to do is to pass the name when caling the class'''  
#     def __init__(self, name, price, quantity):
#         total = price + quantity 
#         print(f'the price for item: {name} is {total}')
        

# item1 = Item('Laptop', 2000, 2) #this can be said to be the instance of the class in a variable


# item2 = Item('Phone',1500,5)
         
'''another way of doing this is by passing the self  that is in the parameter and we can now print the values 
when callint it as an instance'''
#     def __init__(self, name, price, quantity):
#         self.name = name  #assigning the attribute of name to the instance  that is going to be created
#         self.price = price
#         self.quantity = quantity
        
# item1 = Item('Laptop',2000, 2)
# print(item1.name, item1.price + item1.quantity)

# a = item2.calculate_price(item2.price, item2.quantity)
# print(a)


# class Items:
#     def __init__(self, name, price, quantity):
#         self.name = name  #assigning the attribute of name to the instance  that is going to be created
#         self.price = price
#         self.quantity = quantity
#     '''creating another method that will calculate the total price of the item we hve'''
#     def total_price(self):
#         return self.price * self.quantity
    
# item1 = Items('Laptop', 2000, 2)
# print(item1.total_price())

        

'''how to specify the type of data you want either a string or an integer'''
# class Items:
#     def __init__(self, name: str, price: float, quantity): #the str means it needs to accept atrings only
#         self.name = name  #assigning the attribute of name to the instance  that is going to be created
#         self.price = price
#         self.quantity = quantity

#     def total_price(self):
#         return self.price * self.quantity
    
# item1 = Items('Laptop',23,3)
# print(item1.price)

'''using assert statement: assert statement is a keyword that is used to  check if there is a match with what is ha
ppening to your expectation'''

# class Items:
    # def __init__(self, name: str, price: float, quantity): 
        # run validation to the  recieved argument
        # assert price >= 0 #when you put a negetive number in the price it is going to trow an assetion error
        # assert quantity >= 0
'''we can also add our own error messages'''
        # assert price >= 0 , f'price of {price} must not be a negetive number'
        # assert quantity >= 0, f'price of {quantity} must not be a negetive number'
        
        
        
        #assign to self.object
#         self.name = name  #assigning the attribute of name to the instance  that is going to be created
#         self.price = price
#         self.quantity = quantity
     

#     def total_price(self):
#         return self.price * self.quantity
    
# item1 = Items('Laptop',23,3)
# print(item1.price)


'''CREATING A CLASS WITH CLASS ATRRIBUTE'''

# class Items:
#     pay_rate = 10
#     def __init__(self, name: str, price: float, quantity): 
#         assert price >= 0 #when you put a negetive number in the price it is going to trow an assetion error
#         assert quantity >= 0
        
#         self.name = name  #assigning the attribute of name to the instance  that is going to be created
#         self.price = price
#         self.quantity = quantity
        
#     # def total_price(self):
#     #         return self.price * self.quantity
        
#     def appy_discount(self):
#         # self.price = self.price * Items.pay_rate  #classattribute
#         self.price = self.price * self.pay_rate  #classattribute : with self we can now overwrite the class attribute
            
# item1 = Items.pay_rate  #class attribute
# item2 = Items.pay_rate
# item3 = Items.pay_rate
# print(item1)
# print(item2)
# print(item3)

# item1 = Items('Laptop',23,3)
# item1.appy_discount()
# print(item1.price)

# item2 = Items('Phone',23,3)
# item2.pay_rate = 0.4  # overwite the class class attribute here
# item2.appy_discount()
# print(item2.price)

'''Storing and printing all the items we have in a list using a class attribute'''

# class Items:
#     pay_rate = 10
#     all = []
#     def __init__(self, name: str, price: float, quantity): 
#         assert price >= 0 #when you put a negetive number in the price it is going to trow an assetion error
#         assert quantity >= 0
        
#         #assign to self object
#         self.name = name  #assigning the attribute of name to the instance  that is going to be created
#         self.price = price
#         self.quantity = quantity

#         #actions to execute
#         Items.all.append(self)  #this is going to append(add) whatever that have self in it because of the  magic method __init__
        
#     # def total_price(self):
#     #         return self.price * self.quantity
        
#     def appy_discount(self):
#         # self.price = self.price * Items.pay_rate  #classattribute
#         self.price = self.price * self.pay_rate  #classattribute : with self we can now overwrite the class attribute
            


# item1 = Items('Laptop',23000,3)
# item2 = Items('phone',20000,5)
# item3 = Items('moderm',8000,5)
# item4 = Items('watch',2000,3)
# item5 = Items('simcard', 600,1)

# # print(Items.all) #printing all the items in a list

# # getting all the name of products we have
# # for instances in Items.all:
# #     print(instances.name)

# for instances in Items.all:
#     print(f'name: {instances.name}, price: {instances.price}, quantity: {instances.quantity}')  



'''Storing and printing all the items we have in a list using a magic method called __repr__'''
# class Items:
#     pay_rate = 10
#     all = []
#     def __init__(self, name: str, price: float, quantity): 
#         assert price >= 0 #when you put a negetive number in the price it is going to trow an assetion error
#         assert quantity >= 0
        
#         #assign to self object
#         self.name = name  #assigning the attribute of name to the instance  that is going to be created
#         self.price = price
#         self.quantity = quantity
#         Items.all.append(self)


#     #actions to execute
#     def __repr__(self): #repr stands for representing your object
#         return f"Items name:{self.name}, price{self.price}, quantity{self.quantity}"

#     '''this __repr__ will print all the items the way we want we can remove the method and then 
#     print and see the diffrience'''
        
   
# item1 = Items('Laptop',23000,3)
# item2 = Items('phone',20000,5)
# item3 = Items('moderm',8000,5)
# item4 = Items('watch',2000,3)
# item5 = Items('simcard', 600,1)

# print(Items.all)

 



'''using magic  class attribute __dict__ this will bring all the attribute that belong tot the object '''
# item1 = Items.__dict__ #all the attribute for  class level
# item2 = Items('Laptop',23,3)
# print(item1)
# print(item2.__dict__) #all ithe attribute for the instance level

'''extending and adding more features to our class like adding them to a database to make it simple we will 
be using something called csv(comma sepeated value) it is just a file and we can use it to store our values
before we start we nee to create a csv file we will be making use of the csv in the insances'''

import csv

class Items:
    pay_rate = 10
    all = []
    def __init__(self, name: str, price: float, quantity): 
        assert price >= 0 #when you put a negetive number in the price it is going to trow an assetion error
        assert quantity >= 0
        
        #assign to self object
        self.name = name  #assigning the attribute of name to the instance  that is going to be created
        self.price = price
        self.quantity = quantity
        Items.all.append(self)
#making use of the csv here we need to convert the method to a class method by using @classmethod  decorators
#when using a class method we will be using the cls insread of  self and
# this means that when we call our class metod the class object itself is passed as the first argument but we must 
#always remeber to import csv
    @classmethod
    def instanciating_from_csvfile(cls): 
        with open('items.csv', 'r') as f:  #this willl read the csvfile
            reading = csv.DictReader(f) #DictReader will read our file as a list of dictionary
            items = list(reading) #here we are trying to put the csv back to a list so it can contain the  price and quantity
        

        for item in items:#iterating the csv file  
            print(item)

        

       
            


    # #actions to execute
    def __repr__(self): #repr stands for representing your object
        return f"Items name:{self.name}, price{self.price}, quantity{self.quantity}"

    # '''this __repr__ will print all the items the way we want we can remove the method and then 
    # print and see the diffrience'''
        
   


Items.instanciating_from_csvfile()
print(Items.all)



'''
Inheritance
Inheritance is the capability of one class to derive or inherit the properties from another class.
The class that derives properties is called the derived class or child class and the class from
which the properties are being derived is called the base class or parent class.
The benefits of inheritance are:
It represents real-world relationships well.
It provides the reusability of a code.
We don’t have to write the same code again and again.
Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A,
then all the subclasses of B would automatically inherit from class A.
'''
'''
Types of Inheritance – 
Single Inheritance:
Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.

Multilevel Inheritance:
Multi-level inheritance enables a derived class to inherit properties from an immediate parent class 
which in turn inherits properties from his parent class.

Hierarchical Inheritance:
Hierarchical level inheritance enables more than one derived class to inherit properties from a parent class.

Multiple Inheritance:
Multiple level inheritance enables one derived class to inherit properties from more than one base class.

Example: Inheritance in Python
'''
#Python code to demonstrate how parent constructors
# are called.
 
# parent class
# class Person(object):
 
#     # __init__ is known as the constructor
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
 
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
         
#     def details(self):
#         # print("My name is {}".format(self.name))
#         print(f"My name is {self.name}")
#         print("IdNumber: {}".format(self.idnumber))
#         # child class
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
 
#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
         
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("Post: {}".format(self.post))
 
# # creation of an object variable or an instance
# a = Employee('douglas', 886012, 200000, "Intern")
 
# # calling a function of the class Person using
# # its instance
# a.display()
# a.details()

'''Polymorphism
Polymorphism simply means having many forms. For example,we need to determine if the given species of birds fly or not,
using polymorphism we can do this using a single function.
 '''

# class Bird:
   
#     def intro(self):
#         print("There are many types of birds.")
 
#     def flight(self):
#         print("Most of the birds can fly but some cannot.")
 
# class sparrow(Bird):
   
#     def flight(self):
#         print("Sparrows can fly.")
 
# class ostrich(Bird):
 
#     def flight(self):
#          print("Ostriches cannot fly.")
 
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()
 
# obj_bird.intro()
# obj_bird.flight()
 
# obj_spr.intro()
# obj_spr.flight()
 
# obj_ost.intro()
# obj_ost.flight()

'''Encapsulation
# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
# It describes the idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
# To prevent accidental change, an object’s variable can only be changed by an object’s method.
# Those types of variables are known as private variables.
# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.'''

# # Creating a Base class
# # class Base:
# #     def __init__(self):
# #         self.a = "Products"
# #         self.__c = "Manager"
 
# # # Creating a derived class
# # class Derived(Base):
# #     def __init__(self):
 
# #         # Calling constructor of
# #         # Base class
# #         Base.__init__(self)
# #         print("Calling private member of base class: ")
        
# #         # Driver code
# # obj1 = Base()
# # print(obj1.a)

# # Python program to
# # demonstrate protected members
 
 
# # Creating a base class
# class Base:
#     def __init__(self):
 
#         # Protected member
#         self._a = 2
 
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
 
#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling protected member of base class: ",
#               self._a)
 
#         # Modify the protected variable:
#         self._a = 3
#         print("Calling modified protected member outside class: ",
#               self._a)
# # obj1 = Derived()
 
# # obj2 = Base()
# # # Calling protected member
# # # Can be accessed but should not be done due to convention
# # print("Accessing protected member of obj1: ", obj1._a)
 
# # # Accessing the protected variable outside
# # print("Accessing protected member of obj2: ", obj2._a)
 
    
    
