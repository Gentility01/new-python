# strings  = 'hello'
# x = 1
# print(strings.upper())

# ''' creating our own class 
# method can also be defined as functions inside a class'''
# class Dog:
#     def bark(self):
#         print('bark')
        
#     def bite(self):
#         return 'a dog can bite'
        
# d = Dog()
# d.bark()
# d.bite()
# # print(d)
# # print(type(d))


# class Products:
#     def sumProduct(self, x, y): 
#         return x + y
        
        
        

# myproduct = Products()
# myproduct.name = 'phone'
# myproduct.quantity = 10
# myproduct.price = 100
# p = myproduct.sumProduct(myproduct.price, myproduct.quantity)
# print(p)
    

# myproduct = Products()
# myproduct.name = 'Laptop'
# # print(myproduct.name)
# myproduct.quantity = 20
# myproduct.price = 100
# g = myproduct.sumProduct(myproduct.price, myproduct.quantity)
# print(g)
        

# creatibg class with constructor

class Products:
    def __init__(self, name, price, quantity) :
        self.name = name
        self.price = price
        self.quantity = quantity
        
# class Products:
#     # __init__ is also known as magic method
#     def __init__(self, name, price, quantity):
#         sum = price + quantity
#         print(f'the price of {name} is {sum}')
        
        

# product = Products('laptop',1000,2)
# """i am a man
# my name is emeka
# anitasssssssssssssssssssssssssssssssssssssssssssssssssssss
# uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
# eeeeeeeeeeeee"""     
# product2 = Products('phone', 100, 2)
# total = product2.price + product2.quantity
# print(total)

# print(product.name)   

# for a in range(5):
#     print('a' * 5)
    
# for m in range(10):
#     print('#'*(m+1))


a = ['obinna','uchennaa','adaku']

for b in a:
    print(b)



    
    

    
        
        
        

