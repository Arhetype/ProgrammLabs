class Product:
    def __init__(self, name, Id, count, value):
        self.__name = name
        self.__id = Id
        self.__count = count
        self.__value = value

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def count(self):
        return self.__count

    @property
    def value(self):
        return self.__value


class Warehouse:
    def __init__(self):
        self.__warehouse = []

    def add(self, product: Product):
        self.__warehouse.append(product)

    def searchId(self, Id: int):
        for item in self.__warehouse:
            if item.id == Id:
                return item

    def searchName(self, name: str):
        for item in self.__warehouse:
            if item.name == name:
                return item

    def sortByName(self):
        new_list = sorted(self.__warehouse, key=lambda x: x.name, reverse=False)
        return new_list

    def sortByValue(self):
        new_list = sorted(self.__warehouse, key=lambda x: x.value, reverse=False)
        return new_list

    def sortByCount(self):
        new_list = sorted(self.__warehouse, key=lambda x: x.count, reverse=False)
        return new_list

    @property
    def getItem(self):
        return self.__warehouse

