from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QPushButton, QLineEdit, QDialog
import sys

class Ui(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Ui, self).__init__(*args, **kwargs)
        uic.loadUi('mainWindow.ui', self)
        self.setWindowTitle("Script Select Menu")

        self.button = self.findChild(QPushButton, 'printButton') 
        
        self.newDepartment = self.findChild(QAction, 'action_NewDepartment')

        self.newSite = self.findChild(QAction, 'action_NewSite')
        self.newEquipment = self.findChild(QAction, 'action_NewEquipment')

        # self.button.clicked.connect(self.printButtonPressed)
        self.newDepartment.triggered.connect(self.gotocreate)
        self.input = self.findChild(QLineEdit, 'input')

        self.show()

    def gotocreate(self):
        dlg = CreateDepartmentScreen()
        dlg.exec_()
        

class CreateDepartmentScreen(QDialog):
    def __init__(self):
        super(CreateDepartmentScreen, self).__init__()
        uic.loadUi("createdepartment.ui", self)
        

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

