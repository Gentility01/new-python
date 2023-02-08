import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow, QAction
# from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


# defining  a method
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

        # creating menu
        main_menu = self.menuBar()
        filemenu = main_menu.addMenu('File')
        editmenu = main_menu.addMenu('Edit')
        viewmenu = main_menu.addMenu('View')
        searchmenu = main_menu.addMenu('Search')
        toolmenu = main_menu.addMenu('Tools')
        helpmenu = main_menu.addMenu('Help')

        exit_button =QAction('Exit', self)
        exit_button.setShortcut('ctrl+a')
        exit_button.triggered.connect(self.close)

        filemenu.addAction(exit_button)
        self.show()

    

# main method to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    execute = App()
    sys.exit(app.exec_())


