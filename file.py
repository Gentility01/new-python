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


# '''closing the file and this is very important'''
# f.close()

'''using a context managee with he keyword with  (better way to read file)
with this context manager it help us close the file with or without the close command
'''

with open('oop.txt', 'r') as f:  #as f is now the variable
    # contents = f.read()
    contents = f.readlines()  #print out all the files in a list
    # contents = f.readline()  #print out particular files in a list this will keep reading the next line of the file if we print it again and again
    for c in contents:
        print(c)
    
    # contents = f.readline()  #print out particular files in a list this will keep reading the next line of the file if we print it again and again
    # print(contents)
    
    '''iterating over the lines'''
    # for line in f:
    #     print(line, end='')
    '''specify the amount of character to be printed out'''
    # content = f.read(100) #this will print out 100 characters only and if we print it out again it will print the next 100 after the first one
    # print(content, end='')
    
    #another way of reading amount of content 
    size_to_read = 100
    content = f.read(size_to_read) 
    # # looping through the amount of content
    # while len(content) > 0:
    #     print(content, end='|')
    #     content = f.read(size_to_read) 


'''to check if our file is closed'''
# print(f.closed)
    

'''WRITING TO FILE
in order th write to file we will change the parameters r to w and also create a file tht is not onou folder
if the file exits already it will overwrite it
'''
#this will create a newfile
# with open('oop2.txt', 'w') as f:
#     pass

with open('oop2.txt', 'w') as f:
    f.write('writing into file \n') #this will add what we have in this bracket into the new file that is created
    f.write('this is just another line written ') #this will add what we have in this bracket into the new file that is created
    
# 16:50