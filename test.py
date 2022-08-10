class Items:
    discount = 20

    def __init__(self, name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        # print('this is just me')

    def total_price(self):
        return self.price * self.quantity

    def discount_price(self):
        self.price = self.price * self.quantity

        

item1 = Items('laptop', 3000, 2)
item1.discount_price()
# print(item1.discount_price())