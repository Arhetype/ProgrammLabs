print("Номер варианта:", (17 - 1) % 3 + 1)
import random

a = int(input("Введите длину строки:"))
str = "jklmnopqr012345?!;"
str_1 = ""
str_2 = ""
str_1_1 = ""
for i in range(a):
    str_1 += random.choice(str)
for i in str_1:
    if i != "!":
        str_2 += i
    else:
        str_2 += "_"
str_1_1 = str_2
print(str_1)
print(str_1_1)