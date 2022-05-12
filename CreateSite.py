from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QMainWindow, QMenu, QAction, QPushButton, QComboBox,
                             QLineEdit, QDialog, QTableView, QHeaderView, QAbstractItemView)
import sys
import Database


class CreateSiteScreen(QDialog):
    def __init__(self):
        super(CreateSiteScreen, self).__init__()
        uic.loadUi("ui/createSite.ui", self)
        self.initui()

    def initui(self):
        self.site_dept_comboBox = self.findChild(
            QComboBox, 'site_dept_comboBox')
        options = Database.query_allDepartments()

        for option in options:
            self.site_dept_comboBox.addItems(option)

        value = self.site_dept_comboBox.currentTextChanged.connect(
            self.text_changed)

        def text_changed(self):
            item = self.deptCombobox.currentText()
            print(item)

        self.siteNameInput = self.findChild(QLineEdit, 'siteNameInput')
        self.siteAliasInput = self.findChild(QLineEdit, 'siteAliasInput')
        self.confirmButton = self.findChild(QPushButton, 'confirmButton')

        self.confirmButton.clicked.connect(lambda: self.add_site(
            value,
            self.siteNameInput.text(),
            self.siteAliasInput.text()
        ))

        self.show()

    def add_site(self, department_name, name, alias):
        Database.add_site(department_name, name, alias)
        self.close()
