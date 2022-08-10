# import oop2

# m = oop2.Items('laptop', 2000, 1)
# print(m.name)

# import p

# # a = p.Numbers
# # Numbers =200
# # print(Numbers)


# a = p.Numbers
# print(a)
# try:
#     num1 = int(input('enter a number: '))
#     num2 = int(input('enter a second number: '))
#     total = num1 / num2
#     print(total)
    
 
    

    
# except ZeroDivisionError:
#     # print(f'{num1} cannot be divided with {num2}')
#     print(f'Error')
    



# def divide(x,y):
#     try:
#         results = x//y
#         print('good')
#     except ZeroDivisionError:
#         print('bad')

# a = int(input('enter a number'))    
# b = int(input('enter another number'))    
# divide(a,b)

# Program to depict else clause with try-except
  
  
# Function which returns a/b
# def AbyB(a , b):
#     try:
#         c = ((a+b) // (a-b))
#     except ZeroDivisionError:
#         print ("a/b result in 0")
#     else:
#         print (c)
  
# # Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)
    

'''
RELATIONAL OPERATORS
greater than --> means >
less than --> means <
greaterthan or equal to --> means >=
lessthan or equal to --> means <=
not equal to  --> means 
equal equal to --> means ==
'''
# num1 = 1000
# num2 = 1000
# d = num1  num2
# print(d)

# x = 4
# y = 5
# print(('x > y  is',x>y))

# num1 = 4
# num2 = 5
# res = num1 + num2
# res += num1
# print(("Line 1 - Result of + is ", res))

# a = True
# b = True
# print(('a and b is',a and b))
# print(('a or b is',a or b))
# print(('not a is', not a))

# num1 = 4
# num2 = 5

# if num1 > num2:
#     print(f'{num1} is greater than {num2}')
# elif num1 == num2:
#     print(f'{num1} is not equal than {num2}')
# # elif num2 < num1:
# #      print(f'{num2} is not less than {num1}')
# # elif num1 < num2:
# #      print(f'{num1} is  less than {num2}')

# else:
#     print('nothing is happening here')

#nested conditions it is kinda having a condition(s) inside an existing condition
# print(dic.get(1))
# words = {'man':'a man is a male human being',
#          'woman': 'a woman can be said to be a female human being',
#          'animal':'animals are not human'
#          }

# print(words.items())
# for w in words.values():
#     print(w)

# meaning = input('please search here:\n')
# if  meaning ==  'man' :
#     print(words.get('man'))
# if meaning  == 'woman':
#     print(words.get('woman'))
# if 'animal' in meaning:
#     print(words.get('animal'))


# class Dog:
#    def ekuke():
#         voice = 'I can bark'
#         walk = 'i can walk with 4 legs'
#         smell = 'i ca snif very well'
#         print(voice, walk, smell)
        
#    def jshephad():
#        voice = input('enter the  voice attribute')
#        walks = input('enter the  walking attribute')
#        print(voice, walks)
        
    
        
# c =Dog
# c.jshephad()

# class Item:
    
#     def __init__(self): #this __init__ is said to be one of the magic methods in classes and it passes the method  without calling it as an attrbute but the values are passed in the instances of that class
#         price = 2000
#         quantity = 2
#         print(price * quantity)
    
#     '''we can add more parameters in this  constructors all we need to do is to pass the name when caling the class'''  
#     def __init__(self, name, price, quantity):
#         total = price + quantity 
#         print(f'the price for item: {name} is {total}')
        

# item1 = Item('Laptop', 2000, 2) #this can be said to be the instance of the class in a variable


# item2 = Item('Phone',1500,5)


# class Products:
#     def __init__(self, name, price, quantity ):
#         totalPrice = price * quantity
#         print(f'product name: {name} price: {price} quantity: {quantity} and total price {totalPrice}')

# users_input = int(input('enter the quantity you want: '))
# prod1 = Products('Phone', 200000, users_input)


# class Items:
#     def __init__(self, name: str, price: float, quantity): 
#         # run validation to the  recieved argument
#         assert price >= 0 #when you put a negetive number in the price it is going to trow an assetion error
#         assert quantity >= 0
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

class Items:
    def __init__(self, name: str, price: float, quantity): 
        assert price >= 20,  f'{price} is not the price we are selling our product'
        assert quantity >= 5, f'{quantity} is not aloowed you should have more than 5 products'

        self.name = name  
        self.price = price
        self.quantity = quantity
 

    def total_price(self):
        return self.price * self.quantity

name = input('enter you name: ')
price = input('enter your price here: ')
quantity = int(input('enter quantity you want: '))
item1 = Items(name,price,quantity)
print(item1.price)