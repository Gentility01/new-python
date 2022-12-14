''' 
first install pyqt6 by typing  pip install PyQt6
also install pyside by typing pip install PySide6
 '''
 #open it on your virtual env  C:\Users\GENTILITY\Desktop\lessons\venvs\pyqtvenv\Lib\site-packages\PySide6

'''
creating our first window
there are three diffrient type of window  and they are Qwidget, Qmenu window and Qdialog(this is just like a dialog window)
it is used to create dialogs
Qmenu can be used to create windows with menu items status bars
'''

from PyQt6.QtWidgets import  QApplication, QWidget
import sys


# when you want to create a window you need to create an object of the window

#CREATING A SIMPLE WINDOW
# first step
#  creating an object of the window
app = QApplication(sys.argv)  #in the parameter you can can remove the sys.argv and just add []


window = QWidget()

window.show()

sys.exit(app.exec())