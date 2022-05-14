from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QMainWindow, QMenu, QAction, QPushButton, QComboBox,QMessageBox,
                             QLineEdit, QDialog, QTableView, QHeaderView, QAbstractItemView)
import sys
import Database


class CreateSiteScreen(QDialog):
    def __init__(self):
        super(CreateSiteScreen, self).__init__()
        uic.loadUi("ui/createSite.ui", self)
        self.setWindowTitle("Create Site")
        self.initui()

    def initui(self):
        self.site_dept_comboBox = self.findChild(
            QComboBox, 'site_dept_comboBox')
        options = Database.query_allDepartments()

        for option in options:
            self.site_dept_comboBox.addItems(option)


        dept = self.site_dept_comboBox.itemText(self.site_dept_comboBox.currentIndex())
        self.siteNameInput = self.findChild(QLineEdit, 'siteNameInput')
        self.siteAliasInput = self.findChild(QLineEdit, 'siteAliasInput')
        self.confirmButton = self.findChild(QPushButton, 'confirmButton')

        self.confirmButton.clicked.connect(lambda: self.add_site(
            dept,
            self.siteNameInput.text(),
            self.siteAliasInput.text()
        ))

        self.show()


    def add_site(self, department_name, name, alias):
        try:
            print("select:" + department_name)
            Database.add_site(department_name, name, alias)
            self.close()
            QMessageBox.information(QMessageBox(),'Successful','Site is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add site to the database.')
