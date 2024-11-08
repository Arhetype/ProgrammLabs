print("Вариант номер:", (17 - 1) % 3 + 1)

with open('C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-4\\in.txt', 'r') as f:

    #Чтение ко-во студентов и объявление нужных переменных

    n = int(f.readline())
    math_digit = 0
    phys_digit = 0
    inf_digit = 0
    sr_ball = 0
    best_students = []

    #Поиск среднего балла студентов

    for i in range(n):
        line = f.readline().split()
        name = line[0] + ' ' + line[1]
        math_grade = int(line[2])
        phys_grade = int(line[3])
        inf_grafe = int(line[4])
        math_digit += math_grade
        phys_digit += phys_grade
        inf_digit += inf_grafe
        avg = (math_grade + phys_grade + inf_grafe) / 3

        #Поиск лучшего студента

        if avg > sr_ball:
            sr_ball = avg
            best_students = [name]
        elif avg == sr_ball:
            best_students.append(name)

#Рассчет среднего балла

math_avg = math_digit / n
phys_avg = phys_digit / n
inf_avg = inf_digit / n
print("Средний балл по математике:", math_avg)
print("Средний балл по физике:", phys_avg)
print("Средний балл по информатике:", inf_avg)

#Создание и запись в файл лучшего студента

with open('C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-4\\out.txt', 'w') as file:
    for student in best_students:
        file.write(student + '\n')0
        