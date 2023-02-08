import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QMainWindow
# from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot



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

        # adding a text box
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20,80)
        self.textbox1.resize(280, 40)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(350,80)
        self.textbox2.resize(280, 40)


        # adding a button
        button =QPushButton(self, text="Submit")
        button.setToolTip("this is a n example")
        button.move(20,150)
        button.clicked.connect(self.when_clicked)

        self.show()

    @pyqtSlot()
    def when_clicked(self):
        textbox_value1 = self.textbox1.text()
        textbox_value2 = self.textbox2.text()
        # print(textbox_value1, textbox_value2)
        QMessageBox.question(self, "message",  f"first name is {textbox_value1} and last name is {textbox_value2}", QMessageBox.Ok, QMessageBox.Ok,)
        
        self.textbox1.setText("")
        self.textbox2.setText("")
        

    

# main method to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    execute = App()
    sys.exit(app.exec_())

    #42:00