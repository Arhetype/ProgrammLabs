from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 342)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: #22222e")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -30, 600, 721))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(230, 280, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid #f66867;\n"
"    border-radius: 20px;\n"
"    background-color: #22222e;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #f66867;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.Title = QtWidgets.QLabel(self.frame)
        self.Title.setGeometry(QtCore.QRect(180, 60, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setAutoFillBackground(False)
        self.Title.setStyleSheet("background-color: #22222e;\n"
"border-radius: 20px;\n"
"border: 2px solid #f66867;\n"
"color:white;\n"
"")
        self.Title.setScaledContents(False)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Input = QtWidgets.QLineEdit(self.frame)
        self.Input.setGeometry(QtCore.QRect(120, 130, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Input.setFont(font)
        self.Input.setStyleSheet("background-color: #22222e;\n"
"border-radius: 20px;\n"
"border: 2px solid #f66867;\n"
"color:white;")
        self.Input.setCursorPosition(0)
        self.Input.setAlignment(QtCore.Qt.AlignCenter)
        self.Input.setObjectName("Input")
        self.Input_2 = QtWidgets.QLineEdit(self.frame)
        self.Input_2.setGeometry(QtCore.QRect(120, 210, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Input_2.setFont(font)
        self.Input_2.setStyleSheet("background-color: #22222e;\n"
"border-radius: 20px;\n"
"border: 2px solid #f66867;\n"
"color:white;")
        self.Input_2.setCursorPosition(0)
        self.Input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Input_2.setObjectName("Input_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Отправить"))
        self.Title.setText(_translate("MainWindow", "Введите свои данные"))
        self.Input.setPlaceholderText(_translate("MainWindow", "Property 1"))
        self.Input_2.setPlaceholderText(_translate("MainWindow", "Property 2"))


