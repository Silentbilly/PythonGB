# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce


def list_generator():
    new_list = [el for el in range(100, 1001, 2)]

    print(f"The list: {new_list}\nMultip: {reduce(lambda prev_el, el: prev_el * el, new_list )}\n")


def main():
    list_generator()


if __name__ == "__main__":
    main()
