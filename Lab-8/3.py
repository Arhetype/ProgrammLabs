print("Номер варианта:", (17 - 1) % 3 + 1)
perfect_numbers = lambda n: [x for x in range(1, n) if sum([i for i in range(1, x) if x % i == 0]) == x]
n = int(input("Введите диапазон для поиска: "))
print("Совершенные числа в диапазоне", n, "это:", perfect_numbers(n))