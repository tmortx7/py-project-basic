from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QMainWindow, QMenu, QAction, QPushButton,
                             QLineEdit, QDialog, QTableView, QHeaderView, QAbstractItemView)
import sys
from AllOwners import ChartOwnersScreen
from CreateOwner import CreateOwnerScreen
from CreatePlant import CreatePlantScreen

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('ui/mainWindow.ui', self)

        self.setWindowTitle("Control Systems")
        self.button = self.findChild(QPushButton, 'printButton')

        self.newOwner = self.findChild(QAction, 'action_NewOwner')
        self.newPlant = self.findChild(QAction, 'action_NewPlant')
        self.allOwners = self.findChild(QAction, 'action_AllOwners')
        # self.button.clicked.connect(self.printButtonPressed)
        self.newOwner.triggered.connect(self.gotocreateOwner)
        self.newPlant.triggered.connect(self.gotocreatePlant)
        self.allOwners.triggered.connect(self.gotoallOwners)

        self.show()

    def gotocreateOwner(self):
        dlg = CreateOwnerScreen()
        dlg.exec_()

    def gotocreatePlant(self):
        dlg = CreatePlantScreen()
        dlg.exec_()

    def gotoallOwners(self):
        dlg = ChartOwnersScreen()
        dlg.exec_()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()
