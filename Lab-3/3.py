print("Номер варианта:", (17 - 1) % 3 + 1)
import random

#Создание массива

mass = [random.randint(1, 9) for i in range(10)]
print(mass)

#Подсчет кол-во символов

print("Кол-во символов:", mass.count(1), mass.count(2), mass.count(3), mass.count(4), mass.count(5), mass.count(6), mass.count(7), mass.count(8), mass.count(9), end = " ")