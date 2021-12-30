# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

with open("text_7.txt", encoding="utf-8") as f_obj:
    pl_dict = {}
    average_dict = {}
    average_profit = 0
    for line in f_obj:
        pl = int(line.split()[2]) - int(line.split()[3])
        average_profit = average_profit if pl < 0 else average_profit + pl
        pl_dict.update({f"{line.split()[0]}": pl})
        average_dict.update({"average_profit": average_profit})
    overall_list = [pl_dict, average_dict]
    print(overall_list)
    with open("pl_json.json", "w") as write_f:
        json.dump(overall_list, write_f)
