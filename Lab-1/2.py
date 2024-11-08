print("Номер варианта:", (17 - 1) % 4 + 1)

def digit(a, b, c):

#a - результат
#b - номер переменной
#с - знак операции

    if b == 6:
        if a == 35:
            print("((((1 " + c[1] + " ",end="")
            for i in range(2, 6):
                print(str(i) + ")" + c[i] + " ",end="")
            print("6 = 35")
    else:
        c[b] = "+"
        digit(a + b + 1, b + 1, c)
        c[b] = "-"
        digit(a - b - 1, b + 1, c)
        c[b] = "*"
        digit(a * (b + 1), b + 1, c)
        c[b] = "/"
        digit(a / (b + 1), b + 1, c)

def main():
    c = ["" for i in range(6)]
    digit(1, 1, c)

if __name__ == ("__main__"):
    main()