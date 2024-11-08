print("Вариант номер:", (17 - 1) % 3 + 1)

#Инициализация класса и функции

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        try:
            if hours not in range(0, 24) or minutes not in range(0, 60) or seconds not in range(0, 60):
                raise ValueError("Неправильно указано время")
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
        except ValueError as err:
            print(err)
            exit()

#Установка времени

    def set_time(self, hours, minutes, seconds):
        try:
            if hours not in range(0, 24) or minutes not in range(0, 60) or seconds not in range(0, 60):
                raise ValueError("Неправильно указано время")
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
        except ValueError as err:
            print(err)

#Функция добавление секунд

    def add_seconds(self, seconds):
        original_seconds = self.seconds
        self.seconds += seconds
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60
        if self.hours >= 24:
            self.hours = self.hours % 24
        if original_seconds + seconds >= 60:
            print(f"Добавлено {seconds} секунд, новое время {'{:02}'.format(self.hours)}:{'{:02}'.format(self.minutes)}:{'{:02}'.format(self.seconds)}")
        else:
            print(f"Добавлено {seconds} секунд, новое время {'{:02}'.format(self.hours)}:{'{:02}'.format(self.minutes)}:{'{:02}'.format(self.seconds)}")



    def add_minutes(self, minutes):
        self.add_seconds(minutes * 60)

    def add_hours(self, hours):
        self.add_seconds(hours * 60 * 60)

    def __str__(self):
        return f"{'{:02}'.format(self.hours)}:{'{:02}'.format(self.minutes)}:{'{:02}'.format(self.seconds)}"

#Мейн

h = int(input("Введите часы: "))
m = int(input("Введите минуты: "))
s = int(input("Введите секунды: "))
time = Time(h, m, s)
print(time)

hd = int(input("Сколько добавить часов: "))
md = int(input("Сколько добавить минут: "))
sd = int(input("Сколько добавить секунд: "))
time.add_seconds(sd)
time.add_minutes(md)
time.add_hours(hd)

time.set_time(7, 30, 43)
print("Установленно время: ", time)
