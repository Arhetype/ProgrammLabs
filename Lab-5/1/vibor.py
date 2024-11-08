import firma_gui
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 401, 301))
        self.frame.setStyleSheet("background-color: #22222e")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(130, 90, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: 2px solid #f66867;    \n"
"    border-radius: 20px;\n"
"    background-color: #22222e;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #fa4244\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 180, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: 2px solid #f66867;    \n"
"    border-radius: 20px;\n"
"    background-color: #22222e;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #fa4244\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Вы"))
        self.pushButton.setText(_translate("Dialog", "Я юноша"))
        self.pushButton_2.setText(_translate("Dialog", "Я девушка"))

    def pushButton1(self):
        firma_gui.main()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
