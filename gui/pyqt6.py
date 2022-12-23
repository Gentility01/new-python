''' 
first install pyqt6 by typing  pip install PyQt6
also install pyside by typing pip install PySide6
 '''
 #open it on your virtual env  C:\Users\GENTILITY\Desktop\lessons\venvs\pyqtvenv\Lib\site-packages\PySide6
'''There are basically two ways to set up our design the first is running as a python program
]next is to use designer in order to use the desiger we need to install pyqt5-tools by typing pip install pyqt5-tools'''
'''
creating our first window
there are three diffrient type of window  and they are Qwidget, Qmenu window and Qdialog(this is just like a dialog window)
it is used to create dialogs
Qmenu can be used to create windows with menu items status bars

NOTE:
The sys module in Python provides various functions and variables that are used to manipulate
 different parts of the Python runtime environment. It allows operating on the interpreter
 as it provides access to the variables and functions that interact strongly with the interpreter. 
'''

from PyQt6.QtWidgets import  QApplication, QWidget
import sys


# when you want to create a window you need to create an object of the window

#CREATING A SIMPLE WINDOW
# first step
#  creating an object of the window
app = QApplication(sys.argv)  #in the parameter you can can remove the sys.argv and just add [], argv is a list in Python that contains all the command-line arguments passed to the script


window = QWidget()

window.show()

sys.exit(app.exec())