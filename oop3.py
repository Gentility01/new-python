'''using some magic method in class '''

# class Items:
    #we can use this attribute to get all the items we have in this class like this
    # all = []
    # def __init__(self, name, price: float, quantity):
    #     self.name=name
    #     self.price=price
    #     self.quantity=quantity

    #     #trying to get all the items here
    #     Items.all.append(self) #this will append all the items that return itself (self)

    # def details(self):
    #     print(f"{self.name}, {self.price}, {self.quantity}")


    #this magic method stands for representing your object when you print Items.all it will bring it out well
    # def __repr__ (self):
    #     return f" items {self.name} {self.price} {self.quantity}"
        


# item1 = Items('Phone', 20000, 3)
# item2 = Items('Laptops', 40000, 2)
# item1 = Items('chargers', 10000, 3)
# item1 = Items('Cord', 40000, 4)
# item1 = Items('Pods', 50000, 9)


# print(item1.__dict__) # this will get all the attribute in a dictionary
# print(Items.all) #this will print all the instances created earlier


#using loop to get the instances
# for instance in Items.all:
#     print(f'{instance.name}, {instance.price}, {instance.quantity}')





# Creating a Base class
class Base:
    def __init__(self):
        self.a = "Products"
        self.__c = "Manager"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")

        self.a = 4
        
        # Driver code
obj1 = Base()
try:
    print(obj1.a)
except AttributeError:
    print('this object is restricted')



# Python program to
# demonstrate protected members
 
 
# Creating a base class
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
#         print("Calling protected member of base class: ",self._a)
 
#         # Modify the protected variable:
#         self._a = 3
#         print("Calling modified protected member outside class: ",
#               self._a)
# obj1 = Derived()
 
# obj2 = Base()
# # # Calling protected member
# # # Can be accessed but should not be done due to convention
# print("Accessing protected member of obj1: ", obj1._a)
 
# # # Accessing the protected variable outside
# print("Accessing protected member of obj2: ", obj2._a)