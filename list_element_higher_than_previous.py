# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
import random


def list_generator(initial_list):
    new_list = [el for el in initial_list if el > initial_list[initial_list.index(el) - 1]][1:]
    print(f"Initial list: {initial_list}\nNew list: {new_list}\n")


def main():
    initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    random_list = random.sample(range(1, 500), 13)
    list_generator(initial_list)
    list_generator(random_list)


if __name__ == "__main__":
    main()
