'''there are two ways we can use the qtdesign  the first is to load directly from the design.txt app
how we can do this is to save the window in a uifile fomat in any directory we want 
the second way is to convert the uifile to a python file by thping this in our terminal
pyuic6 -x Mywindow.ui -o mywindow.py (Mywindow.ui is our ui file name and mywindow.py is the name of the python file
we want to convert it to'''



from PyQt6.QtWidgets import  QApplication, QWidget
from PyQt6 import uic  #beacuse we are loading  from uifile we need to import thistoo
import sys


# loading  from ui (first way)
class Ui(QWidget):
    def __init__(self):
        super().__init__()

        #loading our ui file with uic
        uic.loadUi("Mywindow.ui", self) # Window.ui is the name of the ui file




app = QApplication(sys.argv)
window = Ui()
window.show()
sys.exit(app.exec())