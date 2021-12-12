# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

output_text = "Вывести несколько переменных на экран: "
a = 8
is_text_equals_number = output_text == a
print(output_text, a, is_text_equals_number)

first_int = int(input("Введите первое число: "))
second_int = int(input("Введите второе число: "))
first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")
print(first_int, second_int, first_string, second_string, is_text_equals_number)
