# 2. Реализовать класс Road (дорога).
#
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    __length = 0
    __width = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_asphalt_mass(self, mass_per_m, height):
        return self.length * self.width * mass_per_m * height / 1000


def main():
    road = Road(20, 5000)
    print(f"Масса асфальта c длиной {road.length} и шириной {road.width} = {road.get_asphalt_mass(25, 5)} т.")


if __name__ == "__main__":
    main()
