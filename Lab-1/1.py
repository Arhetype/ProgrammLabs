print("Номер варианта: 17")

import math

e = 2.718
a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
d = int(input("Введите значение d: "))
t = int(input("Введите значение t: "))

#Стандартное уравнение

y =  ((math.tan(a * e ** (d ** 3))) / (4 + 4 * math.tan(a * (e ** (d ** 3))) ** 2)) * (math.cos(4 * b ** t * d ** (3 * t)) + 4 * math.cos(2 * b ** t * d ** (3 * t)) + 3)

#Упрощенное уравнение

y2 = (math.tan(a * e ** (d ** 3)) * math.cos(4 * b ** t * d ** (3 * t)) + 4 * math.tan(a * e ** (d ** 3)) * math.cos(2 * b ** t * d ** (3 * t)) + 3 * math.tan(a * e ** (d ** 3))) / (4 + 4 * math.tan((a * e ** (d ** 3))) ** 2)

#Проверка ОДД

if (4 + 4 * math.tan(a * e ** (d ** 3)) > 0) and (math.cos(4 * (b ** t) * d **(3 * t)) >= -1 ) and (math.cos(4 * (b ** t) * d **(3 * t)) <= 1 ) and (-1 < (4 * math.cos(2 * b ** t * d ** (3 * t))) < 1):
    print("Уравнение без упрощения:", y)
    print("Уравнение с упрощением:", y2)
else:
    print("Числа не в ОДД")

#Условные единицы стандартного уравнения

y_str = "((math.tan(a * e ** (d ** 3))) / (4 + 4 * math.tan(a * (e ** (d ** 3))) ** 2)) * (math.cos(4 * b ** t * d ** (3 * t)) + 4 * math.cos(2 * b ** t * d ** (3 * t)) + 3)"
digit_1 = 0
for i in range(len(y_str)):
    if y_str[i] == "+" or y_str[i] == "-":
        digit_1 += 3
    elif y_str[i] == "/":
        digit_1 += 7
    elif y_str[i] == "*" and y_str[i + 1] == "*":
        digit_1 += 13
    elif y_str[i] == "*" and y_str[i + 1] == " ":
        digit_1 += 5
    elif y_str[i] == "m" and y_str[i + 1] == "a":
        digit_1 += 13
print("Условные единицы стандартного уравнения:", digit_1)

#Условные единицы упрощенного уравнения

y2_str = "(math.tan(a * e ** (d ** 3)) * math.cos(4 * b ** t * d ** (3 * t)) + 4 * math.tan(a * e ** (d ** 3)) * math.cos(2 * b ** t * d ** (3 * t)) + 3 * math.tan(a * e ** (d ** 3))) / (4 + 4 * math.tan((a * e ** (d ** 3))) ** 2)"
digit_2 = 0
for i in range(len(y2_str)):
    if y2_str[i] == "+" or y2_str[i] == "-":
        digit_2 += 3
    elif y2_str[i] == "/":
        digit_2 += 7
    elif y2_str[i] == "*" and y2_str[i + 1] == "*":
        digit_2 += 13
    elif y2_str[i] == "*" and y2_str[i + 1] == " ":
        digit_2 += 5
    elif y2_str[i] == "m" and y2_str[i + 1] == "a":
        digit_2 += 13
print("Условные единицы упрощенного уравнения:", digit_2)