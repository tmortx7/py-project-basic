from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QMainWindow, QMenu, QAction, QPushButton, QMessageBox,
                             QLineEdit, QDialog, QTableView, QHeaderView, QAbstractItemView)
import sys
import Database


class CreateDepartmentScreen(QDialog):
    def __init__(self):
        super(CreateDepartmentScreen, self).__init__()
        uic.loadUi("ui/createdepartment.ui", self)
        self.setWindowTitle("Create Departments")
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
        try:
            Database.add_department(name, alias)
            self.close()
            QMessageBox.information(
                QMessageBox(), 'Successful', 'Department is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Could not add department to the database.')
