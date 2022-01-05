# 4. Реализуйте базовый класс Car.
#
# * у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# * опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# * добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# * для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы, и покажите результат.
from random import choice


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = "полицейский" if is_police else "гражданский"

    def show_speed(self):
        print(f"Скорость {self.name} цвета {self.color} равна {self.speed} км/ч")

    def get_exceeded_speed_limit(self, speed_limit):
        print(f"Скорость {self.name} цвета {self.color} равна {self.speed} км/ч") if self.speed <= speed_limit else\
            print(f"Скорость {self.name} цвета {self.color} превышена на {self.speed - speed_limit} км/ч")

    def go(self):
        print(f"{self.is_police.title()} автомобиль {self.name} цвета {self.color} поехал.")
        return self

    def stop(self):
        print(f"{self.is_police.title()} автомобиль {self.name} цвета {self.color} остановился.")

    def turn(self):
        direction = choice(["налево", "направо"])
        print(f"{self.is_police.title()} автомобиль {self.name} повернул {direction}.")
        return self


class TownCar(Car):
    def show_speed(self):
        self.get_exceeded_speed_limit(speed_limit=60)


class WorkCar(Car):
    def show_speed(self):
        self.get_exceeded_speed_limit(speed_limit=40)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = "полицейский" if is_police else "спортивный гражданский"


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)
        self.speed = speed
        self.color = color
        self.name = name


def main():
    oriemac_sr20m = WorkCar(41, "yellow", "Oriemac SR20M 20t Горячая резиновая шина дорожный каток", False)
    oriemac_sr21m = WorkCar(39, "yellow", "Oriemac SR21M 20t Горячая резиновая шина дорожный каток", False)
    audi_x5 = TownCar(69, "black", "Audi X5", False)
    lamborgini_solaris = SportCar(120, "red", "Laborgini Diablo", False)
    octavia_a8_police = PoliceCar(420, "White-Blue", "Octavia a8")
    oriemac_sr20m.show_speed()
    oriemac_sr21m.show_speed()
    audi_x5.show_speed()
    octavia_a8_police.show_speed()
    print("*-" * 300)
    print(f"Автомобиль {octavia_a8_police.name} - {octavia_a8_police.is_police}")
    print(f"Автомобиль {oriemac_sr20m.name} - {oriemac_sr20m.is_police}")
    print("*-" * 300)
    octavia_a8_police.go().turn().turn().turn().turn().turn().stop()
    print("*-" * 300)
    oriemac_sr21m.go().turn().turn().turn().stop()
    print("*-" * 300)
    lamborgini_solaris.go().turn().turn().turn().stop()


if __name__ == "__main__":
    main()
