from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QMainWindow, QMenu, QAction, QPushButton, QComboBox, QMessageBox,
                             QLineEdit, QDialog, QTableView, QHeaderView, QAbstractItemView)
import sys
import Database


class CreatePlantScreen(QDialog):
    def __init__(self):
        super(CreatePlantScreen, self).__init__()
        uic.loadUi("ui/createPlant.ui", self)
        self.setWindowTitle("Plant Properties (New)")
        self.initui()

    def initui(self):
        self.owner_comboBox = self.findChild(
            QComboBox, 'owner_comboBox')
        options = Database.query_allOwners()

        for option in options:
            self.owner_comboBox.addItems(option)

        self.plant_input = self.findChild(QLineEdit, 'plant_input')
        self.plant_number_input = self.findChild(
            QLineEdit, 'plant_number_input')
        self.plant_description_input = self.findChild(
            QLineEdit, 'plant_description_input')
        self.plant_note_input = self.findChild(QLineEdit, 'plant_note_input')
        self.address_input = self.findChild(QLineEdit,'address_input')
        self.new_button = self.findChild(QPushButton, 'new_button')
        self.owner_comboBox.currentTextChanged.connect(
            self.handleOwnerComboBox)


    def handleOwnerComboBox(self, value):
        owner = value

        self.new_button.clicked.connect(lambda: self.addplant(
            self.plant_input.text(),
            self.plant_number_input.text(),
            self.plant_description_input.text(),
            self.plant_note_input.text(),
            owner
        ))

        self.new_button.clicked.connect(lambda: self.addaddress(
            self.address_input.text(),
            self.plant_input.text(),           
        ))

        self.show()

    def addplant(self, plant, number, description, note, owner):
        try:
            Database.add_plant(plant, number, description, note, owner)
            self.close()
            QMessageBox.information(
                QMessageBox(), 'Successful', 'Plant is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Could not add plant to the database.')

    def addaddress(self, plus_code, plant_plant):
        try:
            Database.add_address(plus_code, plant_plant)
            self.close()
            QMessageBox.information(
                QMessageBox(), 'Successful', 'Address is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Could not add address to the database.')
