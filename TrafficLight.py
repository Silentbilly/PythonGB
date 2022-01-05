# 1. Создать класс TrafficLight (светофор).
#
# * определить у него один атрибут color (цвет) и метод running (запуск);
# * атрибут реализовать как приватный;
# * в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# * продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
# — на ваше усмотрение;
# * переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# * проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.
from time import sleep
import turtle


class TrafficLight:
    __color = ["grey", "red", "yellow", "green"]

    def running(self):
        num_input = turtle.Screen()
        number_of_iterations = num_input.numinput("Счётчик ресурса", "Введите число:", 2, minval=1, maxval=10)

        red_light = turtle.Turtle()
        red_light.shape("circle")
        red_light.shapesize(5)
        red_light.setposition(0, 100)
        red_light.fillcolor(self.__color[0])
        yellow_light = turtle.Turtle()
        yellow_light.shape("circle")
        yellow_light.setposition(0, 0)
        yellow_light.shapesize(5)
        yellow_light.fillcolor(self.__color[0])
        green_light = turtle.Turtle()
        green_light.shape("circle")
        green_light.setposition(0, -100)
        green_light.shapesize(5)
        green_light.fillcolor(self.__color[0])

        traffic_light_list = [red_light, yellow_light, green_light]

        for i in range(int(number_of_iterations)):
            for el, light in zip(self.__color[1:], traffic_light_list):
                light.fillcolor(el)
                if el == "red":
                    sleep(7)
                elif el == "yellow":
                    sleep(2)
                else:
                    sleep(4)
                light.fillcolor(self.__color[0])


def main():
    trafficlight = TrafficLight()
    trafficlight.running()


if __name__ == "__main__":
    main()
