from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QMainWindow, QMenu, QAction, QPushButton,
                             QLineEdit, QDialog, QTableView, QHeaderView, QAbstractItemView)
import sys
import Database

class CreateDepartmentScreen(QDialog):
    def __init__(self):
        super(CreateDepartmentScreen, self).__init__()
        uic.loadUi("createdepartment.ui", self)
        self.initui()

    def initui(self):
        self.deptNameInput = self.findChild(QLineEdit, 'deptNameInput')
        self.deptAliasInput = self.findChild(QLineEdit, 'deptAliasInput')
        self.confirmButton = self.findChild(QPushButton, 'confirmButton')

        self.confirmButton.clicked.connect(lambda: self.add_dept(
            self.deptNameInput.text(),
            self.deptAliasInput.text()
        ))

        self.show()
    def add_dept(self, name, alias):
        Database.add_department(name, alias)
        self.close()
