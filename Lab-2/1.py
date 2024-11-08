print("Вариант:", (17 - 1)%5 + 1)
import time 
a = input("Введите число: ")

def digit(a):
    b = 0
    for i in a:
        if int(i) % 2 != 0:
            b = b + 1
    return b

start = time.time()
for i in range(1000000):
    digit(a)
end = time.time() - start

print(digit(a))
print(end, "секунд")