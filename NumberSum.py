# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.

def main():
    def get_sum_string():
        sign_of_exit = '@'
        input_str = ''
        sum_collector = 0
        try:
            input_str = input("Введите числа: ")
            sum_int = sum(int(i) for i in input_str.split())
            sum_collector += sum_int
            return sum_collector if input_str == sign_of_exit else get_sum_string() + sum_collector
        except ValueError as err:
            print(err)
            return get_sum_string() if input_str != sign_of_exit else sum_collector

    print(get_sum_string())


if __name__ == "__main__":
    main()
