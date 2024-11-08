import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from uix import Ui_MainWindow
from ArrayList import ArrayList


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.output = []
        self.output_str = str
        self.MW = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MW)
        self.TestArray = ArrayList()
        self.setup_UI()

        self.ui.pushButton.clicked.connect(self.append)
        self.ui.pushButton_3.clicked.connect(self.print)
        self.ui.pushButton_2.clicked.connect(self.appindex)
        self.ui.pushButton_4.clicked.connect(self.ChangeSize)
        self.ui.pushButton_5.clicked.connect(self.appstart)
        self.ui.pushButton_6.clicked.connect(self.upper)
        self.ui.pushButton_8.clicked.connect(self.doubleSlash)
        self.ui.pushButton_9.clicked.connect(self.DeleteSpace)
        self.ui.pushButton_10.clicked.connect(self.reverseSlash)

    def setup_UI(self):
        self.ui.lineEdit.setPlaceholderText("Введите одну строку")
        self.ui.lineEdit_2.setPlaceholderText("Введите одну строку и индекс через точку")
        self.ui.lineEdit_5.setPlaceholderText("Введите строки через запятые")
        self.ui.lineEdit_4.setPlaceholderText("Размер не может быть меньше текущего размера")
        self.ui.lineEdit_6.setPlaceholderText("Введите индекс")
        self.ui.lineEdit_8.setPlaceholderText("Введите индекс")
        self.ui.lineEdit_9.setPlaceholderText("Введите индекс")
        self.ui.lineEdit_10.setPlaceholderText("Введите индекс")
        self.ui.lineEdit_3.setPlaceholderText("Ввод без индекса- вывод всего массива")

    def print(self):
        index = self.ui.lineEdit_3.text()
        if index == "":
            self.ui.label_6.clear()
            self.ui.label_6.setText(self.TestArray.PrintStr())
            self.ui.lineEdit_3.clear()
        else:
            if int(index) <= len(self.TestArray.print()):
                self.ui.label_6.clear()
                self.ui.label_6.setText(self.TestArray.PrintStr(int(index)))
                self.ui.lineEdit_3.clear()
            else:
                self.ui.lineEdit_3.clear()
                warning = QMessageBox()
                warning.setWindowTitle("Ошибка")
                warning.setText("Индекс больше колличества строк")
                warning.setIcon(QMessageBox.Warning)
                warning.exec_()

    def append(self):
        s = self.ui.lineEdit.text()
        self.TestArray.append(s)
        self.ui.lineEdit.clear()

    def appindex(self):
        input_index = self.ui.lineEdit_2.text()
        input_index_array = input_index.split(".")
        self.TestArray.appindex(int(input_index_array[1]), input_index_array[0])
        self.ui.lineEdit_2.clear()

    def ChangeSize(self):
        if int(self.ui.lineEdit_4.text()) <= len(self.TestArray.print()):
            if self.ui.lineEdit_4.text().isdigit():
                size = self.ui.lineEdit_4.text()
                self.TestArray.EditSize(int(size))
                self.ui.lineEdit_4.clear()
            else:
                self.ui.lineEdit_4.clear()
                warning = QMessageBox()
                warning.setWindowTitle("Ошибка")
                warning.setText("Введите целочисленное значение")
                warning.setIcon(QMessageBox.Warning)
                warning.exec_()
        else:
            self.ui.lineEdit_4.clear()
            warning = QMessageBox()
            warning.setWindowTitle("Ошибка")
            warning.setText("Новый размер не может быть меньше старого")
            warning.setIcon(QMessageBox.Warning)
            warning.exec_()

    def appstart(self):
        input_str = self.ui.lineEdit_5.text()
        input_str_array = input_str.split(",")
        self.TestArray.appstart(input_str_array)
        self.ui.lineEdit_5.clear()

    def DeleteSpace(self):
        print("huy")
        index = int(self.ui.lineEdit_9.text())
        self.TestArray.DeleteSpace(index)
        self.ui.lineEdit_9.clear()

    def reverseSlash(self):
        index = int(self.ui.lineEdit_10.text())
        self.TestArray.reverseSlash(index)
        self.ui.lineEdit_10.clear()

    def doubleSlash(self):
        index = int(self.ui.lineEdit_8.text())
        self.TestArray.doubleSlash(index)
        self.ui.lineEdit_8.clear()

    def upper(self):
        index = int(self.ui.lineEdit_6.text())
        self.TestArray.upper(index)
        self.ui.lineEdit_6.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = App()
    application.MW.show()
    sys.exit(app.exec_())
