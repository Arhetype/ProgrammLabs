import random
print("Номер варианта:", (17 - 1) % 5 + 1)

#Функция для сглаживания

def matr(v):
    matr_edited = v
    for i in range(0, len(v)):
        for j in range(0, len(v[i])):
            suma = 0
            count = 0
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if k >= 0 and k < len(v) and l >= 0 and l < len(v[i]) and (k != i or l != j):
                        suma += v[k][l]
                        count += 1
            matr_edited[i][j] = suma / count
    return matr_edited

#Создание матрицы и исправление ее

def main():
    n = int(input("Кол-во строк:"))
    m = int(input("Кол-во столбцов:"))
    mas = [[random.randint(0, 150) for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            print(mas[i][j], end=" ")
        print()
    print()

    mas_edited = matr(mas)
    for i in range(n):
        for j in range(m):
            print(f"{mas_edited[i][j]:0.4f}", end=" ")
        print()

if __name__ == "__main__":
    main()