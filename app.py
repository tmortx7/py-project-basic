from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
import sys


App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec())