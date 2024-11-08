from calc import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from datetime import datetime
import taylorseries
import sys
import math

print("номер варианта", (17 - 1) % 20 + 1)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class FirstWindow(QtWidgets.QDialog):
    def __init__(self):
        super(FirstWindow, self).__init__()
        self.application = None
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)

        self.ui.pushButton.clicked.connect(self.__openOther)

    def __openOther(self):
        if (not self.ui.input_x1.text()) or (not self.ui.input_x2.text()) or (not self.ui.delta.text()) or (not self.ui.E.text()):
            msg_box_warning = QMessageBox()
            msg_box_warning.setWindowTitle("Ошибка")
            msg_box_warning.setText("Не заполнено одно из полей")
            msg_box_warning.setIcon(QMessageBox.Warning)
            msg_box_warning.exec_()
        elif (not self.ui.input_x1.text().isdigit()) or (not self.ui.input_x2.text().isdigit()) or (not self.ui.delta.text().isdigit()):
            msg_box_warning = QMessageBox()
            msg_box_warning.setWindowTitle("Ошибка")
            msg_box_warning.setText("Поля X1, X2, Delta, заполняются целочисленными значениями")
            msg_box_warning.setIcon(QMessageBox.Warning)
            msg_box_warning.exec_()
        elif not is_number(self.ui.E.text()):
            msg_box_warning = QMessageBox()
            msg_box_warning.setWindowTitle("Ошибка")
            msg_box_warning.setText("Поле E заполняется вещественным типом данных")
            msg_box_warning.setIcon(QMessageBox.Warning)
            msg_box_warning.exec_()
        else:
            global x1, x2, delta, E
            x1 = int(self.ui.input_x1.text())
            x2 = int(self.ui.input_x2.text())
            delta = int(self.ui.delta.text())
            E = float(self.ui.E.text())

            self.application = MainWindow()
            self.Dialog.close()
            self.application.show()



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        start = datetime.now()
        result = taylorseries.TaylorSeries(x1, x2, delta, E)
        res = result.compute_range()
        end = datetime.now()
        count = 0
        for key in res:
            count += 1
        self.setMinimumSize(510, 200)
        self.setWindowTitle("Таблица значений")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        table = QTableWidget(self)
        table.setColumnCount(5)
        table.setRowCount(count)

        table.setHorizontalHeaderLabels(["X", "Результат" ,"Math", "Разница", "N"])


        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(4).setTextAlignment(Qt.AlignHCenter)

        i = 0
        for key, value in res.items():
            # print(key, value)
            table.setItem(i, 0, QTableWidgetItem(f"{key}"))
            table.setItem(i, 1, QTableWidgetItem(f"{value}"))
            table.setItem(i, 2, QTableWidgetItem(f"{math.log(int(key))}"))
            table.setItem(i, 3, QTableWidgetItem(f"{math.log(int(key)) - float(value)}"))
            table.setItem(i, 4, QTableWidgetItem(f"{i + 1}"))
            i += 1

        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)

        info = QMessageBox()
        info.setWindowTitle("Время работы программы")
        info.setIcon(QMessageBox.Information)
        td = (end - start).total_seconds() * 10 ** 3
        info.setText(f"{td:.03f}ms")
        info.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = FirstWindow()
    application.Dialog.show()
    sys.exit(app.exec_())