# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

class TrafficLight:
    __color__


def main():
    initial_list = [300, 12, 12, 44, 1, 1, 4, 10, 7, 7, 78, 123, 55]
    list_generator(initial_list)
    list_generator(get_random_list())


if __name__ == "__main__":
    main()
