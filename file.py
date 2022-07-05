# opening and reading files
'''taking notes of this when working with files
'r stands for reading
a stands for append'
w stands for write
'''
'''to read a content in a file'''
# f = open('oop.txt', 'r')  # second parameter is to show the mode of the file
# print(f.name)  #print the name of the file
# print(f.mode)  #print the mode of the file which is reading


'''closing the file and this is very important'''
# f.close()

'''using a context managee with he keyword with  (better way to read file)
with this context manager it help us close the file with or without the close command
'''

with open('oop.txt', 'r') as f:  #as f is now the variable
    # contents = f.read()
    # contents = f.readlines()  #print out all the files in a list
    # contents = f.readline()  #print out particular files in a list this will keep reading the next line of the file if we print it again and again
    # print(contents)
    
    # contents = f.readline()  #print out particular files in a list this will keep reading the next line of the file if we print it again and again
    # print(contents)
    
    '''iterating over the lines'''
    # for line in f:
    #     print(line, end='')
    '''specify the amount of character to be printed out'''
    content = f.read(100) #this will print out 100 characters only and if we print it out again it will print the next 100 after the first one
    print(content, end='')


'''to check if our file is closed'''
# print(f.closed)
    
    
    