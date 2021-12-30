# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

try:
    write_file = open("text_5.txt", "w+", encoding="utf-8")
    read_file = open("text_5.txt", "r", encoding="utf-8")
    input_text = input(">/")
    write_file.write(input_text)
    write_file.close()
    number_list = read_file.read().split()
    print(f"Сумма чисел в файле: {sum(map(int, number_list))}")
    read_file.close()
except ValueError as err:
    print(err)
