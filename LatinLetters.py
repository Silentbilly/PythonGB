# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
# буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(string):
    try:
        symbol_list = list(string)
        for i in symbol_list:
            if ord(i) not in range(65, 90) and ord(i) not in range(97, 122) and ord(i) != 32:
                raise ValueError("Необходимо вводить только латинские буквы")
        str_list = string.split()
        return " ".join(map(str, str_list)).title()
    except ValueError as err:
        return err


def main():
    string = input("Введите предложение: ")

    print(int_func(string))


if __name__ == "__main__":
    main()
