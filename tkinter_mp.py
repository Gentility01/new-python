'''
Building multiple pages in tkinter and navigate through them
2 ways of creating multiple pages in tkinter
building pages all together... raise the page you need (working with this)
create the page you need and destroy when you leave the page
'''

import tkinter as tk
from tkinter import font as tkfont

# creating our base class
#frame object holding all our diffrient page object and controller of my pages setting up the IDs and functions
class MainFrame(tk.Tk):
    def __init__(self, *args, **kwargs):  #note: args and kwargs will make our method take any type od arguments
        tk.Tk.__init__(self, *args, **kwargs)  #getting the init method from the tk object and linking it to mine meaning all the object in the base class should also be relevant to the tk

        self.titlefont = tkfont.Font(family='Verdana', size=12, weight='bold', slant='roman')  #setting some fonts we will be using later on

        container = tk.Frame() #creating a container that wil hold my pages
        container.grid(row=0, column=0, sticky='nesw') #sticky='nesw' means north, east , south west it going to be streching out filling in any blank space and this will work in all our frame because this is tje base frame


        self.id=tk.StringVar() #id of the user
        self.id.set("mr Douglas")

        self.listing = {} # ceating a list in a dictionary that will be holding the name of our pages   example welcomme page

        #creating a loop that will fill in the empty list we just created
        for p in(Welcomepage, Pageone):
            page_name = p.__name__  # __name__ is a donder method what it does is it goes into our class  oobject and take the namme that it is save with
            frame = p(parent=container, controller=self)
            #p is the object from our loop which is the welcome page clas and the pageone class so we are trying to create a new objet of thaat class for each page
            #where the parents will be the container and the controller will be the iteration of those class so there fore we are trying to link them togetger
            frame.grid(row=0, column=0, sticky='nsew')
            self.listing[page_name] = frame
        self.up_frame('Welcomepage')
        
    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()



class Welcomepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        label = tk.Label(self, text= f"Welcome page \n, {controller.id.get()}", font =controller.titlefont)
        label.pack()
        button = tk.Button(self, text = "to page one", command= lambda: controller.up_frame("Pageone"))
        button.pack()


class Pageone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        label = tk.Label(self, text= f"Page one \n, {controller.id.get()}", font =controller.titlefont)
        label.pack()
        button = tk.Button(self, text = "back to main", command= lambda: controller.up_frame("Welcomepage"))
        button.pack()

if __name__ == '__main__':
    app = MainFrame()
    app.mainloop()