# from cgitb import text


from cgitb import text
from msilib.schema import CheckBox
import this
from tkinter import *
import tkinter
from webbrowser import get

from setuptools import Command

"""in tkinter everything is a widget form widget button widget etc 
and the first widget we need to create is the windows widget"""

# root = Tk()
# #now lets create a label widget by first defining it and then putting it up on the screen 
# myLabel = Label(root, text='helloworld') #defining   our label widget(step one)
# myLabel.pack() #step 2 (shoving or packing it to the screen)
# #last thing to do is to create an evetloop(GUI loops constantly and this figures out what the program does)
# root.mainloop()


# POSITIONING WITH TKINTER GRID SYSTEM
'''take all ur programs to be a grid which have colums and rows'''

# root = Tk()
# myLabel1 = Label(root,text='hello world').grid(row=0, column=0) #this is where you set the colums and rows u can do it anotehr way in line 21
# myLabel2 = Label(root,text='my name is Douglas').grid(row=1, column=0)
# # myLabel1.grid(row=0, column=0) #this is where you set the colums and rows
# myLabel2.grid(row=1, column=0)

# root.mainloop()

# CREATING BUTTONS

# bottons = Tk()
# label1 = Label(bottons, text='first name')
# label2 = Label(bottons, text='lastname')
# label1.grid(row=0, column=0)
# label2.grid(row=1, column=0)

# myBotton = Button(bottons, text='Submit')
# # myBotton = Button(bottons, text='Submit', state=DISABLED) #state DISABLE will make it unclickable
# myBotton = Button(bottons, text='Submit', padx=10, pady=5) #this  will pad the button
# myBotton.grid(row=2, column=0)

# bottons.mainloop()
'''while creating a button and we want the button to do something we need to first create a function
'''
# root = Tk()
# def myClick():
#     mylabel = Label(root, text="ypuve clicked a button...", fg='green')
#     mylabel.pack()
    
# myBotton = Button(root, text='click me', command=myClick, bg='red', fg='white') # fg changes the color of the text
# myBotton.pack()

# root.mainloop()


# CREATING AN INPUT FIELD
# root = Tk()
# e = Entry(root, width=50, bg='yellow', borderwidth=10, border=10)
# f = Entry(root, width=50, bg='yellow', borderwidth=10, border=10)
# e.pack()
# f.pack()

# def myclick():
#     myLabel = Label(root, text=e.get()) # we use .get  to get th value of a function
#     myLabel2 = Label(root, text=f.get())
#     myLabel.pack()
#     myLabel2.pack()
    
# myButton = Button(root, text='Click Me', command=myclick)
# myButton.pack()

# root.mainloop()


# CREATING CHECKBOX

# root = Tk()
# root.title('this is my title')
# root.geometry('400x400')

# def show():
#     mylabel = Label(root, text=var.get())
#     mylabel.pack()
    
# def show2():
#     mylabel2 =Label(root, text= var2.get()).pack()
    
# # this is how to create a virable in tkinter
# # var = IntVar() #this is for integer value
# var2 = StringVar()#this is for strings

# # mybox = Checkbutton(root, text='remeber me', variable=var) #calling the variable here in variable=var
# # mybox.pack()
# mybox2 = Checkbutton(root, text='remeber me2', variable=var2, onvalue='True', offvalue='False') #calling the variable here in variable=var,
# mybox2.deselect()
# mybox2.pack()
# '''on value and off value will change the defult of the variable that is off and on to a string'''


# # mybutton = Button(root,text='show selected', command=show ).pack()
# mybutton2 = Button(root,text='show selected2', command=show2 ).pack()

# root.mainloop()



# MAKE AN IMAGE,ICONS AND EXIT BUTTON
root = Tk()
# root.iconbitmap('c:/lesson/download(1).ico')
root.title('this is my title')
root.geometry('400x400')

exitbutton = Button(root, text='exit', command=root.quit).pack()


root.mainloop()




    





# # raiz= tkinter.Tk()

# # raiz.mainloop()

# import tkinter as tk
# master = tk.Tk()
# tk.Label(master, text="First Name").grid(row=0)
# tk.Label(master, text="Last Name").grid(row=1)


# e1 = tk.Entry(master)
# e2 = tk.Entry(master)

# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

# master.mainloop()

# import tkinter as tk
# def show_entry_fields():
#     print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

# master = tk.Tk()
# tk.Label(master, text="First Name").grid(row=0)
# tk.Label(master, text="Last Name").grid(row=1)
# e1 = tk.Entry(master)
# e2 = tk.Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

# tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
# tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)
# tk.mainloop()



# Add an ordinary text
# root = tk.Tk()
# T = tk.Text(root, height=2, width=30)
# T.pack()
# T.insert(tk.END, "Just a text Widget\nin two lines\n")
# tk.mainloop()

#making frames 
# from tkinter import *      
# a= Tk()  
# a.geometry("400x400")  
# frame1=Frame(a,bg = "grey",bd=10,width=100,  height=50,cursor = "target").pack(side=TOP)  
# frame2=Frame(a,bg = "red",width=100,  height=50,cursor = "target").pack(side=RIGHT)  
# frame3=Frame(a,bg = "yellow",bd=10,width=100,  height=50,cursor = "target").pack(side=LEFT)  
# frame4=Frame(a,bg = "blue",bd=10,width=100,  height=50,cursor = "target").pack(side=BOTTOM)  
# a.mainloop() 

# a= Tk()  
# a.geometry("400x400")
# frame1=Frame(a,bg = "grey",bd=10,width=100,  height=50,cursor = "target").pack(side=TOP)
# frame2=Frame(a,bg = "blue",bd=10,width=500,  height=50,cursor = "target").pack(side=TOP)
# a.mainloop() 


# root = Tk() #declearing the window
# root.title('Ashpot class') #declearing the title
# # photo = PhotoImage(file= 'python/lesson\download(2).png')
# # root.iconphoto(False, photo)
# root.geometry('400x400') #setting the sizes

# # Creating GUI classes

# class Myclass():
#     def __init__(self, master):
#         # using a frame here
#         myFrame = Frame(master) #we suppose to pass  in root but replacing root with master
#         myFrame.pack()
        
#         # creating a button
#         self.myButton = Button(master, text="Submit", command=self.clicker)
#         self.myButton.pack(pady=20)
        
#     def clicker(self): # creating a function with the clicker clicker is from the button we created 
#         print('look... you clicked a button')
        
# # m = Myclass(root) #classing the classs and passing the root window to the class
        
# Myclass(root)
# root.mainloop()

# class AnotherClass():
#     def __init__(self, master):
#         print('this is good')









# a= Tk()  
# a.geometry("400x400")  
# frame1=Frame(a,width=500,height=300,  highlightcolor="yellow",highlightbackground="red",  highlightthickness=10).pack(side=TOP)
# T = tk.Text( height=2, width=30)
# T.pack()
# T.insert(tk.END, "Just a text Widget\nin two lines\n")  
# a.mainloop()
