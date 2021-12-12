# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

num_input = int(input("Введите число n: "))

sum_n = num_input + int(f"{num_input}{num_input}") + int(f"{num_input}{num_input}{num_input}")

print(f"Сумма n + nn + nnn равна: {sum_n}")
