import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui2 import Ui_MainWindow
from firma import calculate_preference


class Candidate:
    def __init__(self, properties):
        self.properties = properties


class Firm:
    def __init__(self, properties):
        self.properties = properties


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__() # наследование от родительского класса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.ui.pushButton.clicked.connect(self.ClickButton)


    def init_UI(self):
        self.setWindowTitle("Подбор фирм")
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


        elif (self.input1 != "Negative" and self.input1 != "Positive") or (self.input2 != "Negative" and self.input2 != "Positive"):
            erorr = QMessageBox()
            erorr.setWindowTitle("Ошибка")
            erorr.setIcon(QMessageBox.Warning)
            erorr.setText("Данные поля заполняются словами Positive или Negative")
            erorr.exec_()
        else:
            self.Solution()



    def Solution(self):
        Candidate1 = Candidate({"Property1": f"{self.input1}", "Property2": f"{self.input2}"})
        firms = [
            Firm({"Property1": "Negative", "Property2": "Negative"}),
            Firm({"Property1": "Negative", "Property2": "Positive"}),
            Firm({"Property1": "Positive", "Property2": "Positive"})
        ]
        count = 0
        canditate_choice = {}
        for firm in firms:
            count += 1
            canditate_choice[f'Firm {count}'] = calculate_preference(Candidate1, firm)

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



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = App()
    application.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()