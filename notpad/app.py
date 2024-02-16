import sys

from PyQt6.QtWidgets import QApplication

from .views import Window


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
