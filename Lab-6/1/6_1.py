print("Номер варианта", (17 - 1) % 3 + 1)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui1 import Ui_Dialog
from ui2 import Ui_MainWindow

class FirstWindow(QtWidgets.QDialog):
    def __init__(self):
        super(FirstWindow, self).__init__()
        self.application = None
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)

        self.ui.pushButton.clicked.connect(self.__buttomClick)

    def __buttomClick(self):
        global input1, input2
        input1 = self.ui.lineEdit.text()
        input2 = self.ui.lineEdit_2.text()
        if (not input1) or (not input2):
            Null_Text = QMessageBox()
            Null_Text.setWindowTitle("Ошибка")
            Null_Text.setText("Все поля должны быть заполнены")
            Null_Text.setIcon(QMessageBox.Warning)
            Null_Text.exec_()
        elif (not input1.isdigit()) or (not input2.isdigit()):
            NaN = QMessageBox()
            NaN.setWindowTitle("Ошибка")
            NaN.setText("Вводимое значение должно быть числом")
            NaN.setIcon(QMessageBox.Warning)
            NaN.exec_()
        else:
            self.application = BackEnd()
            self.Dialog.close()
            self.application.show()



class BackEnd(QtWidgets.QMainWindow):
    def __init__(self):
        super(BackEnd, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__out()

    def __out(self):
        n = input1
        m = input2
        A = [[0] * int(m) for i in range(int(n))]
        s = ""


        for i in range(int(n)):
            for j in range(int(m)):
                A[i][j] = i + j + sum(range(max(i,j)))

        for i in range(int(n)):
            for j in range(int(m)):
                s += str(A[i][j]) + " "
            s += "\n"
        self.ui.label.setText(s)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = FirstWindow()
    application.Dialog.show()
    sys.exit(app.exec_())