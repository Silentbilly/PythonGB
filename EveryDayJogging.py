# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

daily_result = 2
final_target = 3
RESULT_ENHANCING = 10
day_counter = 1

while daily_result <= final_target:
    daily_result += daily_result / 100 * RESULT_ENHANCING
    day_counter += 1
    # print(f"{day_counter}-й день: {a:.2f}")

print(f"Спортсмен достиг результата на {int(day_counter)} день")
