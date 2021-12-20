# 4. Решение 4 задачи через замыкание

def my_func(x, y):
    try:
        if x <= 0:
            raise ValueError("Первое число должно быть положительное")
        if y >= 0 or type(y) == float:
            raise ValueError("Второе число должно быть целым отрицательным")

        result_1 = x ** y
        result_2 = 1 / x
        counter = 0
        counter += 1
        if counter == abs(y):
            return result_2, result_1
        return my_func(x * x, -counter)

    except ValueError as err:
        print(err)


def main():
    print(my_func(3, -4))


if __name__ == "__main__":
    main()
