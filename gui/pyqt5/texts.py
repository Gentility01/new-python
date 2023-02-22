# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
import sys
  
# app = QApplication(sys.argv)
# win = QMainWindow()
# win.setGeometry(400,400,500,300)
# win.setWindowTitle("CodersLegacy")
  
# label = QLabel(win)
# label.setText("GUI application with PyQt5")
# label.adjustSize()
# label.move(100,100)
  
# win.show()
# sys.exit(app.exec_())

#include <QWidget>




class App(QWidget):
    def __init__(self):
        super().__init__()  #The super() function allows us to avoid using the base class name explicitly
        self.title = "Simple Window"
        self.left_axis = 50
        self.top_axis = 50
        self.width = 650
        self.height =480
        self.initUi() 
        

# define a method for the title
    def initUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left_axis, self.top_axis, self.width, self.height)
        self.label = QLabel()
        self.label.setText("GUI application with PyQt5")
        self.show()




# main method to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    execute = App()
    sys.exit(app.exec_())

# class App(QWidget):
#     def __init__(self):
#         super().__init__()  #The super() function allows us to avoid using the base class name explicitly
#         self.title = "Simple Window"
#         self.left_axis = 50
#         self.top_axis = 50
#         self.width = 650
#         self.height =480 
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left_axis, self.top_axis, self.width, self.height)
#         self.label = QLabel(self)
#         self.label.setText("GUI application with PyQ")

#         # self.label.setAlignment(Qt.AlignCenter)
#         # self.label.resize(650, 480)

# # # main method to run the application
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     execute = App()
#     sys.exit(app.exec_())




        


