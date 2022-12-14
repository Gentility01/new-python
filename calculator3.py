import tkinter as tk
GREY_COLOR = "#f5f5f5"
LEBEL_COLOR = "#25265e"
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_SIZE = ("Arial", 40, "bold")
WHITE = "#fff"

class Calculator:
    # first method (the initiilizer)
    def __init__(self):
        #setting up windows
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)  #this is make your window not to be resizeable
        self.window.title("Calculator")
        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()
        self.total_lebel, self.lebel = self.create_display_lebels()
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), ".":(4,1)
        }
        self.create_digit_buttons()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=WHITE,fg=LEBEL_COLOR).grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
            return button



    # fifth method(method to display the total lebel and main lebel note: this lebels will be insid the frame in the third method which was initialized in the first method ie the __init__() egself.display_frame = self.create_display_frame() ) 
    def create_display_lebels(self):
        total_lebel = tk.Label(self.display_frame, text=self.total_expression,bg=GREY_COLOR, fg=LEBEL_COLOR, padx=24,  anchor=tk.E, font=SMALL_FONT_STYLE).pack(expand=True, fill="both") # the text passed in this lebel is from the __init__() eg self.total_expression = "0"

        lebel = tk.Label(self.display_frame, text=self.current_expression,bg=GREY_COLOR, fg=LEBEL_COLOR, padx=24,  anchor=tk.E, font=LARGE_FONT_SIZE).pack(expand=True, fill="both") # the text passed in this lebel is from the __init__() eg self.total_current = "0"

        return total_lebel, lebel



    # third method(method to create the display ie where number and other things entered will bbe showing)
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=GREY_COLOR).pack(expand=True, fill="both") #expand and fill will allow it to fill in any space around
        return frame



    # forth method (method to display the buttons)
    def create_button_frame(self):
        frame = tk.Frame(self.window, bg=GREY_COLOR).pack(expand=True, fill="both")
        return frame
       

    
    # second method  (method to run the open the window)
    def run(self):
         self.window.mainloop()





if __name__ == "__main__":
    cal = Calculator()
    cal.run()