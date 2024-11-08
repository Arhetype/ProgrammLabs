print("Номер варианта:", (17 - 1) % 3 + 1)

f = open('C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-6\\3\\3.txt', 'r')
file = f.readlines()
for i, line in enumerate(file):
    if "FuncResult" in line:
        break
new_lines = file[i:]
f1 = open('C:\\Users\\Daniil\\Desktop\\Study\\Programm\\Half-2\\Lab-6\\3\\3out.txt', 'w')
f1.writelines(new_lines)