print("Номер варианта:", (17 - 1) % 3 + 1)
import random

#Генерация рандомного массива

mass = random.sample(range(-100, 100), 15)
print(mass)

class Massive:
    def __init__(self, mass):
        self.mass = mass

#Количество положительных чисел

    def digitpol(self):
        kol = 0
        for i in self.mass:
            if i >= 0:
                kol += 1
        print("Количество положительных чисел:", kol)

#Сумма отрицательных чисел

    def digitotr(self):
        sum = 0
        for i in self.mass:
            if i < 0:
                sum += i
        print("Сумма отрицательных чисел:", sum)

#Номер минимального отрицательного числа

    def mindigit(self):
        t = min(self.mass)
        print("Номер минимального числа:", self.mass.index(t) + 1)

#Вывод с нечетными индексами

    def index(self):
        for i in range(len(self.mass)):
            if(i % 2 != 0):
                print(f"a[{i}] = {self.mass[i]}")

def main():
    mass_vyvod = Massive(mass)
    mass_vyvod.digitpol()
    mass_vyvod.digitotr()
    mass_vyvod.mindigit()
    mass_vyvod.index()

if __name__ == "__main__":
    main()