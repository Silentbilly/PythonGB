# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
# буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(string):
    try:
        symbol_list = list(string)
        for i in symbol_list:
            if ord(i) not in range(97, 122) and ord(i) != 32:
                raise ValueError("Необходимо вводить только маленькие латинские буквы")
        str_list = string.split()
        return " ".join(map(str, str_list)).title()
    except ValueError as err:
        return err


def main():
    print(int_func("honestly speaking i wanna say"))
    print(int_func("as a MAN I WANT TO tell U"))
    print(int_func("Что ничего не получится прямо СЕЙЧАС"))
    print(int_func("Bu may be in december 31th"))


if __name__ == "__main__":
    main()
