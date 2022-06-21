
'''
Python programming language provides the following types of loops to handle looping requirements. Python provides three ways
for executing the loops. While all the ways provide similar basic functionality, they differ in their syntax and condition checking time.

While Loop: 
In python, while loop is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition
becomes false, the line immediately after the loop in the program is executed.

Syntax :
while expression:
    statement(s)
'''
# example
count = 0
while (count > 3):    
    count = count + 1
    print("Hello world")
    
'''
Using else statement with while loops: As discussed above, while loop executes the block until a condition is satisfied. When the condition becomes false, 
the statement immediately after the loop is executed. 
The else clause is only executed when your while condition becomes false. If you break out of the loop, or if an exception is raised,
it won’t be executed. 
'''
# example
count = 0
while (count < 3):    
    count = count + 1
    print("Hello world")
else:
    print("In Else Block")
    
'''
for in Loop: For loops are used for sequential traversal. For example: traversing a list or string or array etc. In Python,
there is no C style for loop, i.e., for (i=0; i<n; i++). There is “for in” loop which is similar to for each loop in other languages.
Let us learn how to use for in loop for sequential traversals
'''
name  = ['obinna','nneka','mma']
for n in name:
    print(n)
    
t = ('okeke', 'rice')
for i in t:
    print(i)
    
dics = {
    'name':'a persons real name',
    'school': 'a place to study'
        
        }
for d in dics:
    print(d)
    
d= dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i]))
    
set1 = {1,2,3,4,5}
for s in set1:
    print(s)
    
r = 10
for i in range(r+1):
    print(i)





























# import re
# # password = "R@m@_f0rtu9e$"
# password = input('enter your password')
# flag = 0
# while True:  
#     if (len(password)<8):
#         flag = -1
#         print('password should not be less than 8')
#         break
#     elif not re.search("[a-z]", password):
#         flag = -1
#         break
#     elif not re.search("[A-Z]", password):
#         flag = -1
#         break
#     elif not re.search("[0-9]", password):
#         flag = -1
#         break
#     elif not re.search("[_@$]", password):
#         flag = -1
#         break
#     elif re.search("\s", password):
#         flag = -1
#         break
#     else:
#         flag = 0
#         print("Valid Password")
#         break
  
# if flag ==-1:
#     print("Not a Valid Password")
        