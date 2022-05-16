from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QMainWindow, QMenu, QAction, QPushButton, QMessageBox,
                             QLineEdit, QDialog, QTableView, QHeaderView, QAbstractItemView)
import sys
import Database


class CreateOwnerScreen(QDialog):
    def __init__(self):
        super(CreateOwnerScreen, self).__init__()
        uic.loadUi("ui/createowner.ui", self)
        self.setWindowTitle("Owner")
        self.initui()

    def initui(self):
        self.owner_input = self.findChild(QLineEdit, 'owner_input')
        self.owner_note_input = self.findChild(QLineEdit, 'owner_note_input')
        self.new_button = self.findChild(QPushButton, 'new_button')

        self.new_button.clicked.connect(lambda: self.addowner(
            self.owner_input.text(),
            self.owner_note_input.text()
        ))

        self.show()

    def addowner(self, owner, note):
        try:
            Database.add_owner(owner, note)
            self.close()
            QMessageBox.information(
                QMessageBox(), 'Successful', 'Owner is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Could not add owner to the database.')
