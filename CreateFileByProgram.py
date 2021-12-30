# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open("text_1.txt", "w+", encoding="utf-8")
input_text = " "
while input_text != "":
    input_text = input(">/")
    my_file.write(input_text + "\n") if input_text != "" else my_file.write(input_text)
my_file.close()
