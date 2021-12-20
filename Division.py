def division(x, y):
    try:
        return float(x / y)
    except ZeroDivisionError as err:
        print(err)


def main():
    x = float(input("Input dividend: "))
    y = float(input("Input divisor: "))
    print(division(x, y))


if __name__ == "__main__":
    main()
