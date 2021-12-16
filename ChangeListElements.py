# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

my_list = [42, "hello", False, (3, 4), 6.9, [1, "hi"], {"hey", 420}, dict(key_1='val_1', key_2='val_2'), 666]

print(len(my_list))
print(my_list[1])
new_list = []

for i in range(1, len(my_list), 2):
    print(my_list[i])
    new_list.append(my_list[i])
    new_list.append(my_list[i - 1])

if len(my_list) % 2 != 0:
    new_list.append(my_list[len(my_list) - 1])

print(new_list)
