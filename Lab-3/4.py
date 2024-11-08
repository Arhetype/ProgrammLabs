print("Номер варианта:", (17 - 1) % 3 + 1)
import random
import statistics

#Создание и вывод матрицы

a = int(input("Введите кол-во строк: "))
b = int(input("Введите кол-во столбцов: "))
matr = [ [0] * b for i in range(a)]
for i in range(a):
    for j in range(b):
        matr[i][j] = random.randint(-50, 50)
print("Матрица:")
for i in matr:
    print(*[f"{x:>4}" for x in i])

#Максимальный элемент в каждом столбце

print("Максимальные элементы в каждой строке:")
for x in zip(*matr):
    print(max(x), end = ' ')
print()

#Среднее значение нечетных элементов

digit = 0
summ = 0
for i in range(a):
    for j in range(b):
        if matr[i][j] % 2 != 0:
            digit += 1
            summ += matr[i][j]
print("Среднее арифм неченых чисел:", summ/digit)