# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '666.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 574)
        MainWindow.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 150, 1141, 351))
        self.tableWidget.setStyleSheet("background-color: white;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(710, 50, 221, 81))
        self.lineEdit.setStyleSheet("background-color:white;\n"
"border: 3px solid gray;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 50, 221, 81))
        self.lineEdit_2.setStyleSheet("background-color:white;\n"
"border: 3px solid gray;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, -20, 1141, 71))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SortNum = QtWidgets.QPushButton(self.widget)
        self.SortNum.setStyleSheet("background-color:white;")
        self.SortNum.setObjectName("SortNum")
        self.horizontalLayout.addWidget(self.SortNum)
        self.SortSale = QtWidgets.QPushButton(self.widget)
        self.SortSale.setStyleSheet("background-color:white;")
        self.SortSale.setObjectName("SortSale")
        self.horizontalLayout.addWidget(self.SortSale)
        self.searhID = QtWidgets.QPushButton(self.widget)
        self.searhID.setStyleSheet("background-color:white;")
        self.searhID.setObjectName("searhID")
        self.horizontalLayout.addWidget(self.searhID)
        self.SearchName = QtWidgets.QPushButton(self.widget)
        self.SearchName.setStyleSheet("background-color:white;")
        self.SearchName.setObjectName("SearchName")
        self.horizontalLayout.addWidget(self.SearchName)
        self.SortName = QtWidgets.QPushButton(self.widget)
        self.SortName.setStyleSheet("background-color:white;")
        self.SortName.setObjectName("SortName")
        self.horizontalLayout.addWidget(self.SortName)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1184, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SortNum.setText(_translate("MainWindow", "Сортировка по кол-ву"))
        self.SortSale.setText(_translate("MainWindow", "Сортировка по цене"))
        self.searhID.setText(_translate("MainWindow", "Поиск по ID"))
        self.SearchName.setText(_translate("MainWindow", "Поиск по названию"))
        self.SortName.setText(_translate("MainWindow", "Сортировка по названию"))
