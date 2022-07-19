# Importing Tkinter module
# from tkinter import *
# from tkinter.ttk import *
  
# Creating master Tkinter window
# master = Tk()
  
# # Creating object of photoimage class
# # Image should be in the same folder
# # in which script is saved
# p1 = PhotoImage(file = 'picture/info.png')
  
# # Setting icon of master window
# master.iconphoto(False, p1)
  
# # Creating button
# b = Button(master, text = 'Click me !')
# b.pack(side = TOP)
  
# # Infinite loop can be terminated by
# # keyboard or mouse interrupt
# # or by any predefined function (destroy())
# mainloop()


from tkinter import *      
root = Tk()      
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack()      
img = PhotoImage(file="picture/info.png")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()  