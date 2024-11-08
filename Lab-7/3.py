print("Номер варианта", (17 - 1) % 3 + 1)

#Создание класса с генератором

class Array:
    def __init__(self):
        self.s = []
    def generate(self):
        self.a = (i**2 for i in range(1, 5))
    def print(self):
        for i in self.a:
            print(i)

#Мейн

test = Array()
test.generate()
test.print()