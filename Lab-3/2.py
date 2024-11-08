print("Номер варианта:", (17 - 1) % 2 + 1)
import random
from itertools import chain

#Массив с четным кол-во чисел

mass1 = random.sample(range(-100, 100), 10)
print("Массив 1:", mass1)
print("Массив 1 измена:", list(chain(*(x for x in zip(mass1[1::2], mass1[::2])))))

#Массив с нечетным кол-во чисел

mass2 = random.sample(range(-100, 100), 9)
print("Массив нечетный:", mass2)
mass = list(chain(*(x for x in zip(mass2[1::2], mass2[::2]))))
mass.append(mass2[-1])
print("Массив 2 измена:", mass)