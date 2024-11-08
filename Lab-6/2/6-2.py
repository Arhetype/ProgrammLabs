from dan_ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from libr import Product, Warehouse
import sys


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.MW = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MW)

        Moloko = Product("Молоко", 1, 10, 100)
        Eggs = Product("Яйца", 2, 50, 75)
        Voda = Product("Вода", 3, 200, 55)
        Potato = Product("Картошка", 4, 15, 70)

        self.Sclad = Warehouse()
        self.Sclad.add(Moloko)
        self.Sclad.add(Eggs)
        self.Sclad.add(Voda)
        self.Sclad.add(Potato)


        zip = self.Sclad.getItem
        self.ui.tableWidget.setRowCount(len(zip))
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Имя", "ID", "Колл-во", "Цена"])
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        for i in range(len(zip)):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(zip[i].name))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(zip[i].id)))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(zip[i].count)))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(zip[i].value)))

        self.ui.SearchName.clicked.connect(self.searchName)
        self.ui.searhID.clicked.connect(self.searchID)
        self.ui.SortName.clicked.connect(self.sortByName)
        self.ui.SortNum.clicked.connect(self.sortByCount)
        self.ui.SortSale.clicked.connect(self.sortByValue)

    def searchName(self):
        name = self.ui.lineEdit.text()
        result = self.Sclad.searchName(name)
        if result is None:
            warning = QMessageBox()
            warning.setWindowTitle("Ошибка")
            warning.setText("Такого имени нет")
            warning.setIcon(QMessageBox.Warning)
            self.ui.lineEdit.clear()
            warning.exec_()
        else:
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setRowCount(1)
            self.ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(result.name))
            self.ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(result.id)))
            self.ui.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(result.count)))
            self.ui.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(result.value)))
            self.ui.lineEdit.clear()

    def searchID(self):
        id = self.ui.lineEdit_2.text()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(1)
        result = self.Sclad.searchId(int(id))
        self.ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(result.name))
        self.ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(result.id)))
        self.ui.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(result.count)))
        self.ui.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(result.value)))
        self.ui.lineEdit_2.clear()

    def sortByName(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(self.Sclad.getItem))
        zip = self.Sclad.sortByName()

        for i in range(len(zip)):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(zip[i].name))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(zip[i].id)))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(zip[i].count)))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(zip[i].value)))

    def sortByCount(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(self.Sclad.getItem))
        zip = self.Sclad.sortByCount()

        for i in range(len(zip)):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(zip[i].name))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(zip[i].id)))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(zip[i].count)))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(zip[i].value)))

    def sortByValue(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(self.Sclad.getItem))
        zip = self.Sclad.sortByValue()

        for i in range(len(zip)):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(zip[i].name))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(zip[i].id)))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(zip[i].count)))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(zip[i].value)))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = App()
    application.MW.show()
    sys.exit(app.exec_())