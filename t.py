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

name = 'Divine'


if len(name) > 5:
    
    if 'y' in name :
        print(f'we also have the letter N in {name}')
    elif 'v' in name:
        print(f'we also have the letter Y in {name}')
        
        
    print(f'the length of {name} is greater than 5')
else:
    print(f'the length of {name} is not greater than 5')