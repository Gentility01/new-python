import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QBoxLayout,QGroupBox,QDialog,QGridLayout, QVBoxLayout
# from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


#defining  a method
class App(QDialog):
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
        self.createGridLayout()
        windowlayout = QVBoxLayout()
        windowlayout.addWidget(self.horizontalGroupBox)
        self.show()

    

# main method to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    execute = App()
    sys.exit(app.exec_())