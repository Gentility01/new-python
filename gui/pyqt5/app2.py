'''
steps in  creating simple gui application
1 import pyqt modules
2 defining  a method
3 define a method for the title
4 display the method using the show method
5 main method to run the application
'''


#import pyqt modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow
# from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


#defining  a method
# class App(QWidget):
#     def __init__(self):
#         super().__init__()  #The super() function allows us to avoid using the base class name explicitly
#         self.title = "Simple Window"
#         self.left_axis = 50
#         self.top_axis = 50
#         self.width = 650
#         self.height =480
#         self.initUi()  #this is the next method where we will apply all the functionality in this init method


# # define a method for the title
#     def initUi(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left_axis, self.top_axis, self.width, self.height)
#         self.show()

    

# # main method to run the application
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     execute = App()
#     sys.exit(app.exec_())


'''note 
__name__ is a built-in variable which evaluates to the name of the current module.
 Thus it can be used to check whether the current script is being run on its own 
or being imported somewhere else by combining it with if statement, as shown below.'''


'''ADDING A BUTTON TO OUR WINDOW'''
class App(QMainWindow):
    def __init__(self):
        super().__init__()  #The super() function allows us to avoid using the base class name explicitly
        self.title = "Simple Window"
        self.left_axis = 50
        self.top_axis = 50
        self.width = 650
        self.height =480
        self.initUi()  #this is the next method where we will apply all the functionality in this init method


# define a method for the title
    def initUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left_axis, self.top_axis, self.width, self.height)

        self.button =QPushButton(self, text="Submit")
        self.button.setToolTip("this is a n example")
        self.button.move(100, 70)
        self.button.clicked.connect(self.when_clicked)

        self.show()

    @pyqtSlot()
    def when_clicked(self):
        print("welcome")

        

    

# main method to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    execute = App()
    sys.exit(app.exec_())


