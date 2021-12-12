# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

num_input = int(input("Введите целое положительное число: "))

if num_input > 0:
    the_biggest_digit = 1

    while num_input != 0:
        last_digit = num_input % 10
        if last_digit > the_biggest_digit:
            the_biggest_digit = last_digit
            num_input //= 10
        else:
            num_input = num_input // 10
    print(f"Самая большая цифра в числе: {the_biggest_digit}")
else:
    print("Ошибка, введите ЦЕЛОЕ число")
