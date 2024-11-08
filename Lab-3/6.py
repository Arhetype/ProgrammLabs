print("Номер варианта:", (17 - 1) % 3 + 1)

print("Введите строку:")
string = input()
string = string.split()
a = max(string, key = len)
print(f'Самое большое слово: {a}, его длинна: {len(a)} символов')