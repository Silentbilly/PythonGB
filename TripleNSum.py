# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

num_input = int(input("Введите число n: "))

sum_n = num_input + int(f"{num_input}" * 2) + int(f"{num_input}" * 3)

print(f"Сумма {num_input} + {num_input}{num_input} + {num_input}{num_input}{num_input} равна: {sum_n}")
