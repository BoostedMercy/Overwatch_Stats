from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import config


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, config.WINDOW_SIZE[0], config.WINDOW_SIZE[1])
    win.setWindowTitle("Testing stuff :D")

    label = QtWidgets.QLabel(win)
    label.setText("Hello This is Text")
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())

window()