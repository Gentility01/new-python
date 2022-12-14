# from tkinter import *
# root = Tk()
# e = Entry(root, width=50, bg='yellow', borderwidth=10, border=10)
# f = Entry(root, width=50, bg='yellow', borderwidth=10, border=10)
# e.pack()
# f.pack()

# def myclick():
#     myLabel = Label(root, text=e.get().capitalize()) # we use .get  to get th value of a function
#     myLabel2 = Label(root, text=f.get().capitalize())
#     myLabel.pack()
#     myLabel2.pack()
    
# myButton = Button(root, text='Click Me', command=myclick)
# myButton.pack()

# root.mainloop()


# Importing tkinter module
# from tkinter import * 
# from tkinter.ttk import *

# # creating Tk window
# master = Tk()

# # setting geometry of tk window
# master.geometry("200x200")

# # button widget
# b1 = Button(master, text = "Click me !")
# b1.place(relx = 1, x =-2, y = 2, anchor = NE)

# # label widget
# l = Label(master, text = "I'm a Label")
# l.place(anchor = NW)

# # button widget
# b2 = Button(master, text = "GFG")
# b2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# # infinite loop which is required to
# # run tkinter program infinitely
# # until an interrupt occurs
# mainloop()

# # Importing tkinter module
# from tkinter import * 
# from tkinter.ttk import *

# # creating Tk window
# master = Tk()

# # setting geometry of tk window
# master.geometry("200x200")

# # button widget
# b2 = Button(master, text = "GFG")
# b2.pack(fill = X, expand = True, ipady = 10)

# # button widget
# b1 = Button(master, text = "Click me !")

# # This is where b1 is placed inside b2 with in_ option
# b1.place(in_= b2, relx = 0.5, rely = 0.5, anchor = CENTER)

# # label widget
# l = Label(master, text = "I'm a Label")
# l.place(anchor = NW)

# # infinite loop which is required to
# # run tkinter program infinitely
# # until an interrupt occurs
# mainloop()

# Import the tkinter module
import tkinter

# Create the default window
root = tkinter.Tk()
root.title("Welcome to GeeksForGeeks")
root.geometry('700x500')

# Create the list of options
options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Variable to keep track of the option
# selected in OptionMenu
value_inside = tkinter.StringVar(root)

# Set the default value of the variable
value_inside.set("Select an Option")

# Create the optionmenu widget and passing
# the options_list and value_inside to it.
question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
question_menu.pack()

# Function to print the submitted option-- testing purpose


def print_answers():
	print("Selected Option: {}".format(value_inside.get()))
	return None


# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
submit_button = tkinter.Button(root, text='Submit', command=print_answers)
submit_button.pack()

root.mainloop()
