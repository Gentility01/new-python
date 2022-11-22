# class Book:
#     def __init__(self, title, quantity, author, price):
#         self.title = title
#         self.quantity = quantity
#         self.author = author
#         self.price = price

#     def __repr__(self):
#         return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"


# book1 = Book('Book 1', 12, 'Author 1', 120)
# book2 = Book('Book 2', 18, 'Author 2', 220)
# book3 = Book('Book 3', 28, 'Author 3', 320)

# print(book1)
# print(book2)
# print(book3)





# types of functions
# function that perform a task and functions that return a value 
# functions that performs a tasks will only be locked in a print and cannot be rewritten or reused
# functions that returns a value will just return a value a nd we can do what ever thing er want with it


'''using many arguments at a time '''
def return_value(**args):
    return args
    

a = return_value(firstname='man', lastname='www', age=2, height=4, score=5)
print(a)
