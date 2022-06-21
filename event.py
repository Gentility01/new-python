import tkinter as tkr
Log = []
master = tkr.Tk()

"""function"""
def char(event):
    print("pressed", repr(event.char))
    # key1 =repr(event.char)
    key1 = event.char
    Log.append(key1)
    print(Log)
    
    
def click(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)
    key2 =event.x, event.y
    Log.append(key2)
    print(Log)



"""frame"""
frame = tkr.Frame(master, height=500, width=500)
frame.bind("<Key>", char)
frame.bind("<Button-1>", click)
frame.bind("<Button-2>", click)
frame.bind("<Button-3>", click)
frame.pack()

"""activate"""
master.mainloop()