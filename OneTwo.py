# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

my_file = open("text_4.txt", encoding="utf-8")
new_file = open("text_4-2.txt", "w+", encoding="utf-8")

russian_numbers = ["Раз", "Два", "Три", "Четыре", "Пять", "Шесть"]
english_numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

for string, i, j in zip(my_file, russian_numbers, english_numbers):
    new_file.write(string.replace(j, i))
    print(string.replace(j, i), end="")
