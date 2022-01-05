# 3. Реализовать базовый класс Worker (работник).
#
# * определить атрибуты: name, surname, position (должность), income (доход);
# * последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# * создать класс Position (должность) на базе класса Worker;
# * в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
# (get_total_income);
# * проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.

class Worker:
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income


class Position(Worker):
    def get_full_name(self):
        return " ".join([self.name, self.surname])

    def get_total_income(self):
        return sum(self.income.values())


def main():
    worker = Position("Alex", "Johns", "Tester", {"wage": 50000, "bonus": 5000})
    print(f"Полное имя сотрудника {worker.name} {worker.surname} - {worker.get_full_name()}\nЕго зарплата: "
          f"{worker.get_total_income()}$ за оговоренный период")


if __name__ == "__main__":
    main()
