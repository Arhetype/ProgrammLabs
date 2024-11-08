from frontt import Ui_MainWindow
from PyQt5 import QtWidgets
from backk import *
import sys
import pickle
import os

#Заполнение таблицы, сохранение

class App(QtWidgets.QMainWindow): 
    def __init__(self):
        super(App, self).__init__()
        self.MW = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MW)
        self.ui.Add.clicked.connect(self.Add)
        self.ui.Dellete.clicked.connect(self.delete)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.Improve.clicked.connect(self.upgrade_hero)
        self.ui.Skill.clicked.connect(self.upgrade_stats)
        self.ui.comboBox_2.addItem("HP")
        self.ui.comboBox_2.addItem("A")
        self.ui.comboBox_2.addItem("B")
        self.ui.comboBox_2.addItem("D")
        self.ui.comboBox_2.addItem("CZ")

        self.persons = []
        self.name = ["Archer"]
        self.count = 0
        self.save = []
        if os.stat("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save").st_size > 5:
            with open("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save", "rb") as f:
                self.save = pickle.load(f)
            self.ui.tableWidget.setRowCount(len(self.save))
            self.persons += self.save
            self.count = len(self.persons)
            for i in range(len(self.save)):
                self.ui.comboBox.addItem(f"Person {i + 1}")
            for i in range(len(self.save)):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.save[i].HP)))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.save[i].A)))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.save[i].B)))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.save[i].D)))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.save[i].CZ)))

#Добавление в таблицу

    def Add(self):
        if os.stat("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save").st_size < 5:
            self.persons.append(Archer())
            self.ui.tableWidget.setRowCount(self.count + 1)
            self.count += 1
            for i in range(len(self.persons)):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.persons[i].HP)))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.persons[i].A)))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.persons[i].B)))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.persons[i].D)))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.persons[i].CZ)))

            #Archer пишется в столбце
            self.ui.tableWidget.setVerticalHeaderLabels(self.name)
            self.ui.tableWidget.setItem(self.count - 1, 0, QtWidgets.QTableWidgetItem(str(self.persons[self.count - 1].HP)))
            self.ui.tableWidget.setItem(self.count - 1, 1, QtWidgets.QTableWidgetItem(str(self.persons[self.count - 1].A)))
            self.ui.tableWidget.setItem(self.count - 1, 2, QtWidgets.QTableWidgetItem(str(self.persons[self.count - 1].B)))
            self.ui.tableWidget.setItem(self.count - 1, 3, QtWidgets.QTableWidgetItem(str(self.persons[self.count - 1].D)))
            self.ui.tableWidget.setItem(self.count - 1, 4, QtWidgets.QTableWidgetItem(str(self.persons[self.count - 1].CZ)))
            self.ui.comboBox.addItem(f"Person {self.count}")
            self.name.append("Archer")

            with open("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save", "wb") as f:
                pickle.dump(self.persons, f)

        else:
            self.count += 1        
            self.persons.append(Archer())
            self.ui.tableWidget.setRowCount(self.count)
            for i in range(len(self.persons)):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.persons[i].HP)))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.persons[i].A)))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.persons[i].B)))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.persons[i].D)))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.persons[i].CZ)))
            
            self.ui.tableWidget.setVerticalHeaderLabels(self.name)
            self.ui.tableWidget.setItem(self.count - 1, 0, QtWidgets.QTableWidgetItem(str(self.persons[self.count - 1].HP)))
            self.ui.tableWidget.setItem(self.count - 1, 1, QtWidgets.QTableWidgetItem(str(self.persons[self.count - 1].A)))
            self.ui.tableWidget.setItem(self.count - 1, 2, QtWidgets.QTableWidgetItem(str(self.persons[self.count - 1].B)))
            self.ui.tableWidget.setItem(self.count - 1, 3, QtWidgets.QTableWidgetItem(str(self.persons[self.count - 1].D)))
            self.ui.tableWidget.setItem(self.count - 1, 4, QtWidgets.QTableWidgetItem(str(self.persons[self.count - 1].CZ)))
            self.ui.comboBox.addItem(f"Person {self.count}")
            self.name.append("Archer")

            with open("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save", "wb") as f:
                pickle.dump(self.persons, f)

#Удаление таблицы

    def delete(self):
        del self.persons[::]
        with open("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save", "wb") as f:
            pickle.dump(self.persons, f)
        self.ui.tableWidget.setRowCount(0)

#Улучшение персонажа

    def upgrade_hero(self):
        index = self.ui.comboBox.currentIndex()
        if type(self.persons[index]) == type(Archer()):
            self.persons[index] = Ranger(self.persons[index])
            for i in range(len(self.persons)):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.persons[i].HP)))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.persons[i].A)))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.persons[i].B)))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.persons[i].D)))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.persons[i].CZ)))
            self.name[index] = "Ranger"
            self.ui.tableWidget.setVerticalHeaderLabels(self.name)
            with open("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save", "wb") as f:
                pickle.dump(self.persons, f)
        elif type(self.persons[index]) == type(Ranger(self.persons[index])):
            self.persons[index] = Grifon(self.persons[index])
            for i in range(len(self.persons)):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.persons[i].HP)))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.persons[i].A)))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.persons[i].B)))
                self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.persons[i].D)))
                self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.persons[i].CZ)))
            self.name[index] = "Grifon"
            self.ui.tableWidget.setVerticalHeaderLabels(self.name)
            with open("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save", "wb") as f:
                pickle.dump(self.persons, f)

#Улучшение навыков

    def upgrade_stats(self):
        index = self.ui.comboBox_2.currentIndex()
        index2 = self.ui.comboBox.currentIndex()
        if index == 0:
            self.persons[index2].improve_HP()
            self.ui.tableWidget.setItem(index2, 0, QtWidgets.QTableWidgetItem(str(self.persons[index2].HP)))
            with open("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save", "wb") as f:
                pickle.dump(self.persons, f)

        if index == 1:
            self.persons[index2].improve_A()
            self.ui.tableWidget.setItem(index2, 1, QtWidgets.QTableWidgetItem(str(self.persons[index2].A)))
            with open("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save", "wb") as f:
                pickle.dump(self.persons, f)

        if index == 2:
            self.persons[index2].improve_B()
            self.ui.tableWidget.setItem(index2, 2, QtWidgets.QTableWidgetItem(str(self.persons[index2].B)))
            with open("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save", "wb") as f:
                pickle.dump(self.persons, f)

        if index == 3:
            self.persons[index2].improve_D()
            self.ui.tableWidget.setItem(index2, 3, QtWidgets.QTableWidgetItem(str(self.persons[index2].D)))
            with open("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save", "wb") as f:
                pickle.dump(self.persons, f)

        if index == 4:
            self.persons[index2].improve_CZ()
            self.ui.tableWidget.setItem(index2, 4, QtWidgets.QTableWidgetItem(str(self.persons[index2].CZ)))
            with open("C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-7\\1\\Save", "wb") as f:
                pickle.dump(self.persons, f)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = App()
    application.MW.show()
    sys.exit(app.exec_())