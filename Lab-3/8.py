print("Номер варианта:", (17 - 1) % 3 + 1)
import random 

#Создание матрицы и вывод

import random
matr1 = [[random.randint(0,9) for x in range(2)] for y in range(2)]
matr2 = [[random.randint(0,9) for x in range(2)] for y in range(3)]
matr3 = [[random.randint(0,9) for x in range(3)] for y in range(2)]
print(matr1)
print(matr2)
print(matr3)

#Создание листа минимума и поиск

minimums = []

min_row1_matr1 = min(matr1[0])
min_row2_matr1 = min(matr1[1])

min_row1_matr2 = min(matr2[0])
min_row2_matr2 = min(matr2[1])
min_row3_matr2 = min(matr2[2])

min_row1_matr3 = min(matr3[0])
min_row2_matr3 = min(matr3[1])

#Занесение в лист минимумов

minimums.append(min_row1_matr1)
minimums.append(min_row2_matr1)
minimums.append(min_row1_matr2)
minimums.append(min_row2_matr2)
minimums.append(min_row3_matr2)
minimums.append(min_row1_matr3)
minimums.append(min_row2_matr3)
print("Минимумы в каждой строке:", minimums)

#Вывод суммы минимумов

sum_minimums = sum(minimums)
print("Сумма минимумов:", sum_minimums)