import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QVBoxLayout, QLabel, QDesktopWidget, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot, Qt




# class App(QWidget):
#     def __init__(self):
#         super().__init__()  #The super() function allows us to avoid using the base class name explicitly
#         self.title = "Simple Window"
#         self.left_axis = 50
#         self.top_axis = 50
#         self.width = 650
#         self.height =480
#         self.main_method()  #this is the next method where we will apply all the functionality in this init method

#     def main_method(self):
#         #set geometry
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left_axis, self.top_axis, self.width, self.height)
#          # set images
#         self.label = QLabel(self)
#         self.pixmap = QPixmap('gentlehub.jpg')
#         self.label.setPixmap(self.pixmap)
#         self.label.resize(self.pixmap.width(),self.pixmap.height())


#         self.show() 



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     execute = App()
#     sys.exit(app.exec_())




class MyApp(QMainWindow):

    def __init__(self):
            super().__init__()
            self.initUI()

    def initUI(self):
            self.setWindowTitle('Centering')
            self.resize(800, 500)
            self.center()
            self.add_image()
            self.add_form()
            self.set_button()
            self.show()

    def center(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
    
    def add_image(self):
        # set images
        self.label = QLabel(self)
        self.pixmap = QPixmap('gentlehub.jpg')
        self.label.setPixmap(self.pixmap)
        # self.label.move(-100, 100)
        self.label.resize(self.pixmap.width(),self.pixmap.height())


    


    def add_form(self):
        self.texts = QLabel("Registration Form")
        self.texts.setText("Registration Form")
        self.texts.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        vbox.addWidget(self.texts)



        self.firstname = ( QLineEdit(self))
        self.firstname.move(20,80)
        self.firstname.resize(280, 40)
        self.firstname.setPlaceholderText("First Name")

        self.lastname = QLineEdit(self)
        self.lastname.move(350,80)
        self.lastname.setPlaceholderText("Last Name")
        self.lastname.resize(280, 40)

        self.email = QLineEdit(self)
        self.email.move(20,150)
        self.email.setPlaceholderText("Email")
        self.email.resize(280, 40)

        self.phone = QLineEdit(self)
        self.phone.move(350,150)
        self.phone.setPlaceholderText("Phone number")
        self.phone.resize(280, 40)

        self.address = QLineEdit(self)
        self.address.move(20,200)
        self.address.setPlaceholderText("Address")
        self.address.resize(610,100)
        

    def set_button(self):
        self.button =QPushButton(self, text="Submit")
        self.button.setToolTip("this is a n example")
        self.button.move(100, 70)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())