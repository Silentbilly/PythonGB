# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

try:
    month_num = int(input("Введите номер месяца: "))
    if month_num > 12 or month_num < 1:
        raise ValueError('Некорректное значение месяца')
except ValueError:
    print("Некорректное значение месяца")

seasons_dict = {"зима": [12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}

try:
    for i in seasons_dict.items():
        if month_num in i[1]:
            print(i[0])
            break
except NameError:
    print("Введена строка. Введите число от 1 до 12")
