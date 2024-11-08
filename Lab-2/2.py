print("Вариант:", (17 - 1) % 4 + 1)
a, n = map(int, input("Введите число и его степень: ").split())

def digit(a, n):
    if n==1:
        return a
    elif n != 1:
        return a * digit(a, n - 1)

print(digit(a, n))