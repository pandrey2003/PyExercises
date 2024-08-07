import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle("Adding labels")
        self.setWindowIcon(QIcon("python.png"))
        self.add_label()

    def add_label(self):
        label = QtWidgets.QLabel(self)
        label.setText("Hi, this is my application")
        label.adjustSize()
        label.move(50, 50)


def run():
    app = QApplication(sys.argv)
    gui = Window()
    gui.show()
    sys.exit(app.exec_())


run()
