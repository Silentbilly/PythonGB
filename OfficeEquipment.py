# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
import uuid


class OfficeEquipment:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model
        self.tool_id = uuid.uuid4()
        self.name = f"{mark}{model}_{str(self.tool_id)[:-28]}"

    def get_info(self):
        return f"{self.name} - {self.tool_id}"


class WareHouse:
    def __init__(self, count=0):
        self.max_count = count
        self.dict = {}

    def add_to_warehouse(self, office_equipment):
        self.dict.setdefault(office_equipment.name, str(office_equipment.tool_id))

    def get_from_warehouse_to_new(self, name, new_dict):
        new_dict.setdefault(name, str(self.dict[name]))
        del self.dict[name]


def main():
    warehouse = WareHouse()
    hp1005 = OfficeEquipment("HP", "1005")
    hp1010 = OfficeEquipment("HP", "1010")
    xerox666 = OfficeEquipment("Xerox", "666")

    print(hp1005.tool_id)
    print(hp1010.tool_id)
    print(hp1010.name)
    warehouse.add_to_warehouse(hp1005)
    warehouse.add_to_warehouse(hp1010)
    warehouse.add_to_warehouse(xerox666)
    print(f"На складе: {warehouse.dict}")
    new_office = {}
    warehouse.get_from_warehouse_to_new(hp1005.name, new_office)
    warehouse.get_from_warehouse_to_new(xerox666.name, new_office)
    print(f"На старом складе: {warehouse.dict}")
    print(f"На новом складе: {new_office}")


if __name__ == "__main__":
    main()
