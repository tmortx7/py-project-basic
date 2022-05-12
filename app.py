from PyQt5.QtWidgets import QApplication
from main import MainWindow
import sys


App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec())