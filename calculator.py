
from tkinter import *
root = Tk()
root.title('Simple Calculator')
e = Entry(root, width=35, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
f_num = int("")

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def button_clear():
    e.delete(1)

def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
  
# define buttons
button1 = Button(root, text='1', padx=40, pady=20, command= lambda:button_click(1))
button2 = Button(root, text='2', padx=40, pady=20, command= lambda:button_click(2))
button3 = Button(root, text='3', padx=40, pady=20, command= lambda:button_click(3))
button4 = Button(root, text='4', padx=40, pady=20, command= lambda:button_click(4))
button5 = Button(root, text='5', padx=40, pady=20, command= lambda:button_click(5))
button6 = Button(root, text='6', padx=40, pady=20, command= lambda:button_click(6))
button7 = Button(root, text='7', padx=40, pady=20, command= lambda:button_click(7))
button8 = Button(root, text='8', padx=40, pady=20, command= lambda:button_click(8))
button9 = Button(root, text='9', padx=40, pady=20, command= lambda:button_click(9))
button0 = Button(root, text='0', padx=40, pady=20, command= lambda:button_click(0))
buttonequal = Button(root, text='=', padx=39, pady=20, command= lambda:button_click())
buttonadd = Button(root, text='+', padx=91, pady=20, command= button_add())
buttonclear = Button(root, text='clear', padx=79, pady=20, command= lambda:button_clear())
    
#put the button on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonclear.grid(row=4,column=1, columnspan=2) 
buttonadd.grid(row=5,column=1,  columnspan=2)
buttonequal.grid(row=5,column=0)


    
# myButton.pack()

root.mainloop()
#1:00:00
