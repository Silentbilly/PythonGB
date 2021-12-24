# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета
# для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

try:
    script_name, output_per_hour, wage_per_hour, bonus = argv
    salary = int(output_per_hour) * int(wage_per_hour) + int(bonus)
    print(f"Зарплата сотрудника при выработке в часах = {output_per_hour}$, ставке в час = {wage_per_hour}$ + "
          f"премия {bonus}$: {salary}$")
except ValueError as err:
    print(err)
