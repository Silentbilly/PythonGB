# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_f = open("text_2.txt", encoding="utf-8")
content = my_f.readlines()
print(content)
print(f"Количество строк в файле: {len(content)}")

for el in content:
    print(f"В строке номер {content.index(el) + 1}: {len(el.split())} слов")

my_f.close()
