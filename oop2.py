'''CREATING A CLASS WITH INSTACE ATRRIBUTE'''
# class Item:
#     # we can write a method that can be used or executte in the instances
#     # methods are functions inside a class
#     def calculate_price(self, x, y): #self: python passes the object itself as the first augment when u call the methods you can call the self something else . 
#         return x , y
        
        
    

# item1 = Item() #this can be said to be the instance of the class in a variable

# item1.name = 'phone' #this can be said to be the attribute of a class
# item1.price= 2000  #this can be said to be the attribute of a class
# item1.quantity= 2  #this can be said to be the attribute of a class

# a = item1.calculate_price(item1.price, item1.quantity)
# print(a)

# item2 = Item()
# item1.name = 'laptop'
# item2.price = 20000
# item2.quantity = 3
# a = item2.calculate_price(item2.price, item2.quantity)
# print(a)


'''using the __init__method  and __init__ are called the constructor'''

class Item:
    
    
    
    # def __init__(self): #this __init__ is said to be one of the magic methods in classes and it passes the method  without calling it as an attrbute but the values are passed in the instances of that vlass
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
#     def __init__(self, name: str, price: float, quantity): 
        #run validation to the  recieved argument
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

class Items:
    pay_rate = 10
    def __init__(self, name: str, price: float, quantity): 
        assert price >= 0 #when you put a negetive number in the price it is going to trow an assetion error
        assert quantity >= 0
        
        self.name = name  #assigning the attribute of name to the instance  that is going to be created
        self.price = price
        self.quantity = quantity
        
    def total_price(self):
            return self.price * self.quantity
        
    def appy_discount(self):
        # self.price = self.price * Items.pay_rate  #classattribute
        self.price = self.price * self.pay_rate  #classattribute : with self we can no overwrite the class attribute
            
# item1 = Items.pay_rate  #class attribute
# item2 = Items.pay_rate
# item3 = Items.pay_rate
# print(item1)
# print(item2)
# print(item3)

item1 = Items('Laptop',23,3)
item1.appy_discount()
print(item1.price)

item2 = Items('Phone',23,3)
item2.pay_rate = 0.4  # overwite the class class attribute here
item2.appy_discount()
print(item2.price)

#40:50
    

'''using magic  class attribute __dict__ this will bring all the attribute that belong tot the object '''
# item1 = Items.__dict__ #all the attribute for  class level
# item2 = Items('Laptop',23,3)
# print(item1)
# print(item2.__dict__) #all ithe attribute for the instance level

    
    
