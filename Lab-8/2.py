import threading
import time
import random

print("Номер варианта:", (17 - 1) % 3 + 1)

class Sport:
    def __init__(self, number):
        self.number = number
        self.events = ['Тренировка', 'Начало соревнования', 'Окончание соревнования']

class Venue:
    def __init__(self, number):
        self.number = number
        self.event = None
        self.lock = threading.Lock()

    def set_event(self, event):
        self.event = event

    def clear_event(self):
        self.event = None

def run_sport(sport, venue):
    while True:
        with venue.lock:
            if venue.event is None:
                event = random.choice(sport.events)
                venue.set_event(event)
                print(f'Соревнования по виду спорта {sport.number} начинаются на площадке {venue.number}: {event}')
            else:
                print(f'Соревнования по виду спорта {sport.number} на площадке {venue.number} уже проходят: {venue.event}')

            time.sleep(1)

            venue.clear_event()
            print(f'Соревнования по виду спорта {sport.number} заканчиваются на площадке {venue.number}: {event}')
            time.sleep(1)


sports = [Sport(i) for i in range(1, 11)]
venues = [Venue(i) for i in range(1, 6)]
for sport in sports:
    for venue in venues:
        thread = threading.Thread(target=run_sport, args=(sport, venue))
        thread.start()