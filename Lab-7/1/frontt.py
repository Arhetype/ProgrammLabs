# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Daniil\Desktop\Study\Programm\Half-2\Lab-7\1\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1112, 846)
        MainWindow.setStyleSheet("background-color: #FF1493;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 40, 661, 751))
        self.tableWidget.setStyleSheet("background-color: #FFC0CB;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(810, 40, 93, 28))
        self.Add.setStyleSheet("background-color: #FFB6C1;")
        self.Add.setObjectName("Add")
        self.Skill = QtWidgets.QPushButton(self.centralwidget)
        self.Skill.setGeometry(QtCore.QRect(810, 440, 93, 28))
        self.Skill.setStyleSheet("background-color: #FFB6C1;")
        self.Skill.setObjectName("Skill")
        self.Improve = QtWidgets.QPushButton(self.centralwidget)
        self.Improve.setGeometry(QtCore.QRect(810, 120, 93, 28))
        self.Improve.setStyleSheet("background-color: #FFB6C1;")
        self.Improve.setObjectName("Improve")
        self.Dellete = QtWidgets.QPushButton(self.centralwidget)
        self.Dellete.setGeometry(QtCore.QRect(800, 760, 93, 28))
        self.Dellete.setStyleSheet("background-color: #FFB6C1;")
        self.Dellete.setObjectName("Dellete")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(800, 190, 281, 151))
        self.comboBox.setStyleSheet("background-color: #FFB6C1;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(800, 510, 291, 141))
        self.comboBox_2.setStyleSheet("background-color: #FFB6C1;")
        self.comboBox_2.setObjectName("comboBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "HP"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "A"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "B"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CZ"))
        self.Add.setText(_translate("MainWindow", "Добавить"))
        self.Skill.setText(_translate("MainWindow", "Навык"))
        self.Improve.setText(_translate("MainWindow", "Прокачать"))
        self.Dellete.setText(_translate("MainWindow", "Очистить"))