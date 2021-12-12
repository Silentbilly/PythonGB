# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

SECONDS_IN_HOUR = 3600
SECMINS_IN_MINHOUR = 60
SECONDS_IN_DAY = SECONDS_IN_HOUR * 24

time_input = int(input("Введите время в секундах: "))

if time_input >= SECONDS_IN_DAY:
    time_input %= SECONDS_IN_DAY

hours = time_input // SECONDS_IN_HOUR
minutes = int((time_input / SECONDS_IN_HOUR * SECMINS_IN_MINHOUR) % SECMINS_IN_MINHOUR)
seconds = time_input % SECMINS_IN_MINHOUR

print(f"Ваше время: "
      f"{hours if hours >= 10 else f'0{hours}'}:{minutes if minutes >= 10 else f'0{minutes}'}:"
      f"{seconds if seconds >= 10 else f'0{seconds}'}")
