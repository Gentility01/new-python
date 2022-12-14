# # Import module
# from tkinter import *

# # Create object
# root = Tk()

# # Adjust size
# root.geometry("400x400")
# root.title('man')

# # Add image file
# bg = PhotoImage(file = "picture/info.png")

# # Show image using label
# label1 = Label( root, image = bg)
# label1.place(x = 0, y = 0)

# label2 = Label( root, text = "Welcome")
# label2.pack(pady = 50)

# # Create Frame
# frame1 = Frame(root)
# frame1.pack(pady = 20 )

# # Add buttons
# button1 = Button(frame1,text="Exit")
# button1.pack(pady=20)

# button2 = Button( frame1, text = "Start", bg='#000000', fg='white')
# button2.pack(pady = 20, padx=40)

# button3 = Button( frame1, text = "Reset")
# button3.pack(pady = 20)

# # Execute tkinter
# root.mainloop()

from tkinter import *
parent = Tk()
parent.geometry("150x150")
button1 = Button(parent, text = "Hi I am button! Click me to start!!")
button1.place(relx = 1, rely =1, anchor = N)
mainloop()
