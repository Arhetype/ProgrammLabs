import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vibor import Ui_Dialog
from ui2 import Ui_MainWindow
from firma import calculate_preference


class FirstWindow(QtWidgets.QDialog):
    def __init__(self):
        super(FirstWindow, self).__init__()
        self.application2 = None
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)

        self.ui.pushButton_2.clicked.connect(self.openTwo)
        self.ui.pushButton.clicked.connect(self.openOne)

    def openOne(self):
        self.application2 = App2()
        self.Dialog.close()
        self.application2.show()

    def openTwo(self):
        self.application = App()
        self.Dialog.close()
        self.application.show()


class Groom:
    def __init__(self, properties):
        self.properties = properties


class Bride:
    def __init__(self, properties):
        self.properties = properties


class App(QtWidgets.QMainWindow):
    def __init__(self):
        #Наследование родительского класса
        super(App, self).__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.ui.pushButton.clicked.connect(self.ClickButton)

    def init_UI(self):
        self.setWindowTitle("Marry")
        self.setFixedSize(562, 342)

    def ClickButton(self):
        self.input1 = self.ui.Input.text()
        self.input2 = self.ui.Input_2.text()
        if not self.input1 or not self.input2:
            msg_box_warning = QMessageBox()
            msg_box_warning.setWindowTitle("Ошибка")
            msg_box_warning.setText("Не заполнено одно из полей")
            msg_box_warning.setIcon(QMessageBox.Warning)
            msg_box_warning.exec_()


        elif (self.input1 != "Negative" and self.input1 != "Positive") or (
                self.input2 != "Negative" and self.input2 != "Positive"):
            erorr = QMessageBox()
            erorr.setWindowTitle("Ошибка")
            erorr.setIcon(QMessageBox.Warning)
            erorr.setText("Данные поля заполняются словами Positive или Negative")
            erorr.exec_()
        else:
            self.Solution()

    def Solution(self):
        Candidate1 = Groom({"Property1": f"{self.input1}", "Property2": f"{self.input2}"})
        Brides = [
            Bride({"Property1": "Negative", "Property2": "Negative"}),
            Bride({"Property1": "Negative", "Property2": "Positive"}),
            Bride({"Property1": "Positive", "Property2": "Positive"})
        ]
        count = 0
        canditate_choice = {}
        for bride in Brides:
            count += 1
            canditate_choice[f'Bride {count}'] = calculate_preference(Candidate1, bride)

        sorted_tuples = sorted(canditate_choice.items(), key=lambda item: item[1])
        sorted_dict = {k: v for k, v in sorted_tuples}
        s = ''
        for key, value in sorted_dict.items():
            s += ("{0}: {1} предпочтение \n".format(key, value))
        info = QMessageBox()
        info.setWindowTitle("Информация")
        info.setText(s)
        info.setStyleSheet(
            """
            QMessageBox {
                color: white;
                border: 5px solid #f66867;
                border-radius: 5px;
                background-color: white;
            }
            """
        )
        info.exec_()


class App2(QtWidgets.QMainWindow):
    def __init__(self):
        super(App2, self).__init__()  # наследование от родительского класса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

        self.ui.pushButton.clicked.connect(self.ClickButton)

    def init_UI(self):
        self.setWindowTitle("Подбор работников")
        self.setFixedSize(562, 342)

    def ClickButton(self):
        self.input1 = self.ui.Input.text()
        self.input2 = self.ui.Input_2.text()
        if not self.input1 or not self.input2:
            msg_box_warning = QMessageBox()
            msg_box_warning.setWindowTitle("Ошибка")
            msg_box_warning.setText("Не заполнено одно из полей")
            msg_box_warning.setIcon(QMessageBox.Warning)
            msg_box_warning.exec_()


        elif (self.input1 != "Negative" and self.input1 != "Positive") or (
                self.input2 != "Negative" and self.input2 != "Positive"):
            erorr = QMessageBox()
            erorr.setWindowTitle("Ошибка")
            erorr.setIcon(QMessageBox.Warning)
            erorr.setText("Данные поля заполняются словами Positive или Negative")
            erorr.exec_()
        else:
            self.Solution()

    def Solution(self):
        Bride1 = Bride({"Property1": f"{self.input1}", "Property2": f"{self.input2}"})
        Grooms = [
            Groom({"Property1": "Negative", "Property2": "Negative"}),
            Groom({"Property1": "Negative", "Property2": "Positive"}),
            Groom({"Property1": "Positive", "Property2": "Positive"})
        ]
        count = 0
        canditate_choice = {}
        for groom in Grooms:
            count += 1
            canditate_choice[f'Groom {count}'] = calculate_preference(Bride1, groom)

        sorted_tuples = sorted(canditate_choice.items(), key=lambda item: item[1])
        sorted_dict = {k: v for k, v in sorted_tuples}
        s = ''
        for key, value in sorted_dict.items():
            s += ("{0}: {1} рейтниг \n".format(key, value))
        info = QMessageBox()
        info.setWindowTitle("Информация")
        info.setText(s)
        info.setStyleSheet(
            """
            QMessageBox {
                color: white;
                border: 5px solid #f66867;
                border-radius: 5px;
                background-color: white;
            }
            """
        )
        info.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = FirstWindow()
    application.Dialog.show()
    sys.exit(app.exec_())
