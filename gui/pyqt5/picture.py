# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys


# class Window(QMainWindow):
# 	def __init__(self):
# 		super().__init__()

# 		self.acceptDrops()
# 		# set the title
# 		self.setWindowTitle("Image")

# 		# setting the geometry of window
# 		self.setGeometry(0, 0, 400, 300)

# 		# creating label
# 		self.label = QLabel(self)
		
# 		# loading image
# 		self.pixmap = QPixmap('info.png')

# 		# adding image to label
# 		self.label.setPixmap(self.pixmap)

# 		# Optional, resize label to image size
# 		self.label.resize(self.pixmap.width(),
# 						self.pixmap.height())

# 		# show all the widgets
# 		self.show()

# # create pyqt5 app
# App = QApplication(sys.argv)

# # create the instance of our Window
# window = Window()

# # start the app
# sys.exit(App.exec())



# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import (
#     QLabel,
#     QWidget,
#     QApplication,
#     QHBoxLayout,
# )

# application = QApplication([])

# mainWindow = QWidget()

# mainWindow.setGeometry(0, 0, 350, 400)
# mainWindow.setWindowTitle('Horizontal Layout')

# horizontalLayout = QHBoxLayout()

# for num in range(6):
#     label = QLabel()
#     pixmap = QPixmap('info.png')
#     label.setPixmap(pixmap)
#     horizontalLayout.addWidget(label)

# mainWindow.setLayout(horizontalLayout)
# mainWindow.show()

# application.exec()



# class ImageWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.show_image()

#     def show_image(self):
#         image = QPixmap("gentlehub.jpg")
#         label = QLabel(self)
#         label.setPixmap(image)


# def main():
#     application = QApplication(sys.argv)
#     widget = ImageWidget()
#     widget.resize(500, 500)
#     widget.setWindowTitle("display image")
#     widget.show()
#     sys.exit(application.exec_())


# if __name__ == '__main__':
#     main()

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys


class Window(QMainWindow):

    x_axis = 0
    y_axis = 0
    height = 700
    width = 700
    def __init__(self):
        super().__init__()
        self.acceptDrops()
        # set window title
        self.setWindowTitle("Load Image on Window")
        #set window size
        self.setGeometry(self.x_axis, self.y_axis, self.width, self.height)

        self.label = QLabel(self)
        self.pixmap = QPixmap('gentlehub.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),self.pixmap.height())
        self.show()

# Instantiate pyqt5 application
App = QApplication(sys.argv)

# create window instance
window = Window()

# start the app
sys.exit(App.exec())
