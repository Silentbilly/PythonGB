# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(arg_1, arg_2, arg_3):
    args_list = [arg_1, arg_2, arg_3]
    min_arg = min(args_list)
    args_list.remove(min_arg)
    return sum(args_list)


def main():
    arg_1 = 1
    arg_2 = 2
    arg_3 = 3
    print(f"Сумма наибольших аргументов: {my_func(arg_1, arg_2, arg_3)}")


if __name__ == "__main__":
    main()
