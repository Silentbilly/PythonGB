# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_file = open("text_3.txt", encoding="utf-8")
common_salary = 0
entry_counter = 0

for string in my_file:
    employee = string.split()[0]
    salary = string.split()[1]
    entry_counter += 1
    if float(salary) > 20000:
        print(employee)
    common_salary += float(salary)
average_wage = common_salary / entry_counter
print(f"Средняя зарплата: {average_wage}")

my_file.close()
