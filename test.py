# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 524)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(144, 0, 85, 255), stop:1 rgba(58, 41, 41, 255));\n"
"border-color: rgb(84, 16, 77);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(130, 150, 461, 221))
        self.frame.setStyleSheet("border-color: rgb(71, 25, 80);\n"
";\n"
"background-color: rgba(42, 42, 42, 100);\n"
"gridline-color: rgb(31, 31, 31);\n"
"selection-background-color: rgb(62, 62, 62);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(10)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(120, 190, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 190, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.inputUsername = QtWidgets.QLineEdit(self.frame)
        self.inputUsername.setGeometry(QtCore.QRect(120, 70, 221, 20))
        self.inputUsername.setObjectName("inputUsername")
        self.inputPassword = QtWidgets.QLineEdit(self.frame)
        self.inputPassword.setGeometry(QtCore.QRect(120, 130, 221, 20))
        self.inputPassword.setAutoFillBackground(False)
        self.inputPassword.setObjectName("inputPassword")
        self.usernameLabel = QtWidgets.QLabel(self.frame)
        self.usernameLabel.setGeometry(QtCore.QRect(200, 40, 61, 16))
        self.usernameLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.frame)
        self.passwordLabel.setGeometry(QtCore.QRect(200, 100, 61, 21))
        font = QtGui.QFont()
        font.setKerning(True)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setAutoFillBackground(False)
        self.passwordLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.passwordLabel.setObjectName("passwordLabel")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(130, 50, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 25 26pt \"Yu Gothic Light\";")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setStyleSheet("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Create Account"))
        self.usernameLabel.setText(_translate("MainWindow", "  Username"))
        self.passwordLabel.setText(_translate("MainWindow", "  Password"))
        self.titleLabel.setText(_translate("MainWindow", "Overwatch Stat Viewer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

