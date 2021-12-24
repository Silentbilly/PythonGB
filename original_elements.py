# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
import random


def list_generator(initial_list):
    new_list = [el for el in initial_list if initial_list.count(el) == 1]
    print(f"Initial list: {initial_list}\nNew list: {new_list}\n")


def get_random_list():
    random_list = []
    for i in range(0, 10):
        random_int = random.randint(1, 10)
        random_list.append(random_int)
    return random_list


def main():
    initial_list = [300, 12, 12, 44, 1, 1, 4, 10, 7, 7, 78, 123, 55]
    list_generator(initial_list)
    list_generator(get_random_list())


if __name__ == "__main__":
    main()
