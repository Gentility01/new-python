# import sqlite3

#connect to database
# conn = sqlite3.connect('customer.db')

#create a cursor
# c = conn.cursor()





#query the database
# c.execute("SELECT * FROM customers")

# #fetch
# item = c.fetchall()
# print(item)


# def market(name, number_of_phone, price):

#     total = number_of_phone*price
#     print(f"Dear {name} your are buying{number_of_phone} phone which is ${total}")

# customer_name = input('enter your name: ')
# amount_of_phone = int(input('how many phone do you want to buy: '))
# prices = 30000
# total_price = amount_of_phone * prices

# market(customer_name,amount_of_phone,30000)

# def phones(customer_name, name_of_phone, number_of_phone, price):
#     a = print('oooooooooooo')
#     print(customer_name, name_of_phone,number_of_phone, price )


# customers_name = input('enter your name: ')
# customers_phone = input('enter the phone you want to buy: ')
# number_of_phone_to_buy = int(input('enter your name: '))
# price_of_phone = 90000

# c = phones(customers_name,customers_phone,number_of_phone_to_buy,price_of_phone)
# print(c)


# class Product:
#     def __init__(self, name: str, price:float, quantity):
#         assert quantity > 0, f'the quantity  {quantity} must be more than 0'
# #         assert quantity >= 0
#         self.name = name
#         self.price = price
#         self.quantity = quantity




# p1 =  Product('phone', 20000, 20)
# print(p1.quantity)

'''write a class where the user will input the quantity of product he or she wants and also and also have a fixed 
price for each brand'''


class Phones:
        tekno = 60000
        infinix = 70000
        iphone = 90000

        def __init__(self, name, quantity):
                self.name = name
                self.quantity = quantity

        def total_price(self):
                if self.name == 1:
                        print(f'the total price of Tekno is {self.tekno * self.quantity}')
                elif self.name == 2:
                        print(f'the total price of Infinix is {self.infinix * self.quantity}')
                elif self.name == 3:
                        print(f'the total price of Iphone is {self.iphone * self.quantity}')

print('List of phones in stuck')
phone = int(input("""
       1. tekno = 60000
       2. infinix = 70000
       3. iphone = 90000
"""))
qty =  int(input('enter the quantity of phone: '))
p = Phones(phone, qty)
p.total_price()





