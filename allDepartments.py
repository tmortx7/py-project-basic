from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QComboBox,
                             QLineEdit, QDialog, QTableView, QHeaderView, QAbstractItemView)
import sys
import Database


class AllDepartmentsScreen(QDialog):
    def __init__(self):
        super(AllDepartmentsScreen, self).__init__()
        uic.loadUi("ui/alldepartments.ui", self)
        self.initui()

    def initui(self):
        self.deptCombobox = self.findChild(QComboBox, 'department_combobox')
        #self.deptCombobox.setMinimumWidth(200)

        options = Database.query_allDepartments()

        for option in options:
            self.deptCombobox.addItems(option)

        self.deptCombobox.currentTextChanged.connect(self.text_changed)
        self.show()

    def text_changed(self):
        item = self.deptCombobox.currentText()
        print(item)
        
        

        
