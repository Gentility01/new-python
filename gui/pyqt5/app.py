'''
Introduction

A Graphical User Interface, better known as GUI, is a characteristic feature of most personal computers today.
It provides an intuitive experience to users of varying levels of computing skills.
Though they may use more resources, 
GUI applications are generally user-friendly due to their point-and-click nature.

PyQt is one of the toolkits you can use to develop cross-platform GUI applications in Python. 
It is powerful and easy to learn if you already have a firm grasp of this language.
PyQt is Python binding for the cross-platform application development framework, Qt.
Using PyQt gives you the benefit of developing GUI applications using a simple but powerful language like Python.
 It exposes all the functionalities of the Qt API.

Riverbank Computing is the company behind the development and maintenance of PyQt. 
Its latest stable release is PyQt6. 
The release cycle of the PyQt major version appears to be in sync with that of Qt,
 judging from the release history.
 
 how to install pyqt5 
 first you need to create a virtual enviroment 
 then you install by typing pip install PyQt5
'''

'''
steps in using pyqt
CREATING A HELLOWORLD GUI

Step 1: Import the required classes
PyQt comes with several built-in modules.However, the module you will interact with most regularly when
building a GUI is the QtWidgets module. It has classes you will use for creating your GUI.

Step 2: Initialize the application

We need to initialize the application by creating an instance of QApplication.
It is responsible for managing the application’s main settings and control flow.
Therefore, you should instantiate this class before creating any other object related to the user interface.

Step 3: Create the main window

The main window, also referred to as a top-level window,
 is a widget that doesn’t have a parent. Every GUI must have a main window.

Step 4: Show the main window

The window we have created in the previous step is not visible by default.
We need to show it by invoking the show method:

Step 5: Start the event loop

Finally, you need to fire up the event loop by invoking the application.exec method:
'''
from PyQt5.QtWidgets import QApplication, QWidget

application = QApplication([])
mainWindow = QWidget()
mainWindow.setGeometry(0, 0, 350, 400)
mainWindow.setWindowTitle('Hello World')

mainWindow.show()

application.exec()