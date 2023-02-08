import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
 
class App(QMainWindow):
    def __init__(self):
        super().__init__()  #The super() function allows us to avoid using the base class name explicitly
        self.initUi()
        
        


# define a method for the title
    def initUi(self):
        self.title = "Simple Window"
        self.setWindowTitle(self.title)
        self.resize(800, 500)
        

         #this is the next method where we will apply all the functionality in this init method
        self.show_images()
        self.set_button()   #this is the next method where we will apply all the functionality in this init method
        self.show()

    
    def show_images(self):
        
        self.label = QLabel(self)
        self.pixmap = QPixmap('gentlehub.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),self.pixmap.height())

        
    def set_button(self):
        self.button =QPushButton(self, text="Submit")
        self.button.setToolTip("this is a n example")
        self.button.move(100, 70)
        self.button.clicked.connect(self.when_clicked)


    @pyqtSlot()
    def when_clicked(self):
        print("welcome")

        

    

# main method to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    execute = App()
    sys.exit(app.exec_())
 
 
 
 