import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QMainWindow,  QSpinBox
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
        

        self.showtext = QLabel(self)
        self.showtext.move(20,20)
        self.showtext.setStyleSheet("QLabel{font-size: 18pt;}")
        self.showtext.setText("Welcome")
        
        # adding a text box
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20,80)
        self.textbox1.resize(280, 40)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(350,80)
        self.textbox2.resize(280, 40)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(20,160)
        self.textbox3.resize(280, 40)

        self.textbox4 = QSpinBox(self)
        self.textbox4.setMinimum(0)
        self.textbox4.setMaximum(300)
        self.textbox4.move(350, 160)
        self.textbox4.resize(280, 40)

        self.textbox5 = QLineEdit(self)
        self.textbox5.setEchoMode(QLineEdit.Password)
        self.textbox5.move(20,250)
        self.textbox5.resize(280, 40)


        # adding a button
        button =QPushButton(self, text="Submit")
        button.setToolTip("this is a n example")
        button.move(20,250)
        button.clicked.connect(self.when_clicked)

        self.show()

    @pyqtSlot()
    def when_clicked(self):
        textbox_value1 = self.textbox1.text()
        textbox_value2 = self.textbox2.text()
        textbox_value3 = self.textbox3.text()
        print(textbox_value1, textbox_value2)
        if "gmail.com" not in textbox_value3:
            QMessageBox.question(self, "message",  "email not good", QMessageBox.Ok, QMessageBox.Ok,)
        if len(textbox_value1) < 2:
            QMessageBox.question(self, "message",  "your name must be more than 2 character", QMessageBox.Ok, QMessageBox.Ok,)
        # QMessageBox.question(self, "message",  f"first name is {textbox_value1} and last name is {textbox_value2}", QMessageBox.Ok, QMessageBox.Ok,)
        
        # self.textbox1.setText("dddddd")
        # self.textbox2.setText("xxx")
        

    

# main method to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    execute = App()
    sys.exit(app.exec_())

    #42:00