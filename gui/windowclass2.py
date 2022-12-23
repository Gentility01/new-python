from PyQt6.QtWidgets import  QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys


#using object oriented
#The super() function allows us to avoid using the base class name explicitly
#The super() function returns an object that represents the parent class.
# class Window(QWidget):

#     def __init__(self):
#         super().__init__()
       





# app = QApplication([])
# window = Window()
# window.show()
# sys.exit(app.exec())

#adding thing to our window
class Window(QWidget):

    def __init__(self):
        super().__init__()
        # adding a window title
        self.setWindowTitle("pyqt tutorials")
        #adding icons (we need to import QIcon from QtGui)
        self.setWindowIcon(QIcon("../picture/info.png"))
        #adding a fixed height and width
        self.setFixedHeight(200)
        # self.setFixedWidth(200)
        #setting the height and with with the geometry
        self.setGeometry(500,300,400,300) #500,300 is the x and y position , 400,300 is the width and height
        #changing the background color 
        # self.setStyleSheet('background-color:red')
        #another way we can change background color
        stylesheet = (
            'background-color:blue'
        )
        self.setStyleSheet(stylesheet)





app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())