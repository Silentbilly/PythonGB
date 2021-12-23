# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
# необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count
from itertools import cycle


def get_number_from_start_to_end(start, end):
    for el in count(start):
        if el > end:
            break
        else:
            print(el)


def get_repeatable_list(initial_list):
    i = 0
    for el in cycle(initial_list):
        if i > 7:
            break
        print(el)
        i += 1


def main():
    get_number_from_start_to_end(3, 10)
    get_repeatable_list(range(0, 20))


if __name__ == "__main__":
    main()
