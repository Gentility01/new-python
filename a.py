# import oop2
# obj1 = oop2.Derived()
 
# obj2 = oop2.Base()
# # Calling protected member
# # Can be accessed but should not be done due to convention
# print("Accessing protected member of obj1: ", obj1._a)
 
# # Accessing the protected variable outside
# print("Accessing protected member of obj2: ", obj2._a)


# declaring the string
# str ="manchester"
 
# slicing using indexing sequence
# print(str[: 3])
# print(str[1 : 5 : 2])
# print(str[-1 : -12 : -2])
# str1 = "united"
# str ="manchester" + " " + str1 + str(1)
# print(str)



# xt = str(1000)

# x = xt.split()

# print(x)

# items = {
#     'man':'this is a man',
#     'woman':'this is a woman',
#     'boy':'this is a boy',
#     }

# name =input('enter a name')
# for k , v in items.items():
#     if name in k:
#         print('good')
#         break


# class Product:

#     def __init__(self, name, quantity, price):
#         self.name = name
#         self.quantity = quantity
#         self.price = price

#     def my_products(self):
#         print(f'products name = {self.name}, products quantity = {self.quantity}, and the product price = {self.price}')

#     def total(self):
#         print(f'the total price of {self.name} is {self.price * self.quantity}')

# product1 = Product('Laptop', 20,3000000 )
# product2 = Product('phone', 2,30000 )

# product1.my_products()
# product2.total()

# a = [1,2,3]
# print(a)

class TeknoPhone:
    def __init__(self):
        