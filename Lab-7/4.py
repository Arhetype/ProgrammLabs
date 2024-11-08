print("Номер варианта:", (17 - 1) % 3 + 1)

#Создание класса

class Func:

    #Создание функции x/y

    def divide(x, y):
        return x / y
    
    #Создание декоратора

    def zero(operate):
        def inner(x, y):
            if y == 0:
                print("Нельзя делить на 0")
                return
            return operate(x,y)
        return inner

    #Декорирование функции

    @zero
    def divide(x, y):
        return x / y

#Мейн

test = Func
print(test.divide(5, 0))
print(test.divide(5, 2))
