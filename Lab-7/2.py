print("Номер варианта:", (17 - 1) % 3 + 1)

from abc import *

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def info(self):
        pass

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def info(self):
        return f'{self.name} (возраст {self.age}), зарплата {self.salary}'
    
class Boss(Employee):
    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age, salary)
        self.bonus = bonus

    def info(self):
        return f'{self.name} (возраст {self.age}) с зарплатой {self.salary}, который получил бонус в размере {self.bonus}'
    
class Department:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
    
    def info(self):
        return f'В {self.name} работает сотрудник - {self.manager.info()}'
    
class Firm():
    def __init__(self, name, departaments):
        self.name = name
        self.departaments = departaments

    def info(self):
        inf = f'{self.name} компания имеет различные отделы: '
        for departament in self.departaments:
            inf += departament.info() + "\n"
        return inf

sotrydnik = Employee("Осанов Владимир", 25, 100000)
sotrydnik_2 = Employee("Якупов Денис", 23, 900000)
bigboss = Boss("Алышев Юрий", 60, 150000, 7500)
it_dep = Department("IT департаменте", bigboss)
pr_dep = Department("PR департаменте", sotrydnik)
hr_dep = Department("IT департаменте", sotrydnik_2)
company = Firm("DN & Friends", [it_dep, pr_dep, hr_dep])
print(company.info())