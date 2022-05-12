from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QMainWindow, QMenu, QAction, QPushButton,
                             QLineEdit, QDialog, QTableView, QHeaderView, QAbstractItemView)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
import sys
from CreateDepartment import CreateDepartmentScreen
from allDepartments import AllDepartmentsScreen


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('ui/mainWindow.ui', self)

        self.setWindowTitle("Script Select Menu")
        self.button = self.findChild(QPushButton, 'printButton')

        self.newDepartment = self.findChild(QAction, 'action_NewDepartment')

        self.newSite = self.findChild(QAction, 'action_NewSite')
        self.allDepartments = self.findChild(QAction, 'action_Departments')

        # self.button.clicked.connect(self.printButtonPressed)
        self.newDepartment.triggered.connect(self.gotocreate)
        self.input = self.findChild(QLineEdit, 'input')

        self.allDepartments.triggered.connect(self.gotoAllDepartments)

        self.show()

    def gotocreate(self):
        dlg = CreateDepartmentScreen()
        dlg.exec_()

    def gotoAllDepartments(self):
        dlg = AllDepartmentsScreen()
        dlg.exec_()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()
